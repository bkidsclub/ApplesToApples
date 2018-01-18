import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Json.Encode exposing (..)
import WebSocket
import Random
import Style exposing (..)

-- CONSTANTS
address : String
address = "ws://127.0.0.1:8123/"


main =
  Html.program
    { init = init
    , view = view
    , update = update
    , subscriptions = subscriptions
    }


-- MODEL

type alias Model =
  { player : Int
  , name : String
  , green : String
  , hand : List String
  , submitted : String
  , judging : Bool
  , winner : String
  , score : Int
  }

init : (Model, Cmd Msg)
init =
  (Model 0 "" "" ["nadya", "is", "the", "best"] "" False "" 0, Cmd.none)


-- UPDATE

type Msg
  = Select String
  | Winner String
  | EnterName String
  | SubmitName
  | SubmitID Int
  | ServerMsg String

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    Select card ->
      ({ model | submitted = card }
      , WebSocket.send address
        (Json.Encode.encode 0
          (Json.Encode.object
            [ ("id", Json.Encode.int model.player)
            , ("red", Json.Encode.string card)
            ]
          )
        )
      )

    Winner card ->
      ({ model | winner = card }
      , WebSocket.send address
        (Json.Encode.encode 0
          (Json.Encode.object
            [ ("id", Json.Encode.int model.player)
            , ("winner", Json.Encode.string card)
            ]
          )
        )
      )

    EnterName name ->
      ({ model | name = name }, Cmd.none)

    SubmitName ->
      (model, Random.generate SubmitID (Random.int 0 999999999))

    SubmitID identifier ->
      ({ model | player = identifier }
      , WebSocket.send address
        (Json.Encode.encode 0
          (Json.Encode.object
            [ ("id", Json.Encode.int identifier)
            , ("name", Json.Encode.string model.name)
            ]
          )
        )
      )

    ServerMsg content ->
      (model, Cmd.none)
      -- TODO: handle


-- SUBSCRIPTIONS

subscriptions : Model -> Sub Msg
subscriptions model =
  WebSocket.listen address ServerMsg


-- VIEW

selectedApple : List Style
selectedApple =
  [ color "#FF0000"
  ]

unselectedApple : List Style
unselectedApple =
  [ color "#00FF00"
  ]

view : Model -> Html Msg
view model =
  div [] 
    [ div [] [text "Apples to Apples"]
    , div [] (if model.player == 0 then
        [ input [onInput EnterName] [text "Lunch"]
        , button [onClick SubmitName] [text "go"]
        ]
      else
        [ div [] [ text ("player is " ++ model.name ++ " : " ++ toString model.player)]
        , div [] [ text (model.green) ]
        , (if String.length model.submitted == 0 
          then div [] (List.map (\ card -> button [onClick (Select card)] [text card]) model.hand)
          else div [] (List.map (\ card -> button [style (if model.submitted == card then selectedApple else unselectedApple)] [text card]) model.hand))
        ]
      )
    ]
