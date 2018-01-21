import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Json.Encode exposing (..)
import Json.Decode exposing (..)
import Json.Decode.Pipeline exposing (decode, required)
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
  , serverError : String
  , green : String
  , hand : List String
  , submitted : String
  , winner : String
  , score : Int
  , round : Int
  , toJudge : List String
  , judgeName : String
  , allPlayers : List String
  , leaderboard : List (String, Int)
  }


modelDecoder : Decoder Model
modelDecoder =
  decode Model
  |> Json.Decode.Pipeline.required "player" Json.Decode.int
  |> Json.Decode.Pipeline.required "name" Json.Decode.string
  |> Json.Decode.Pipeline.required "serverError" Json.Decode.string
  |> Json.Decode.Pipeline.required "green" Json.Decode.string
  |> Json.Decode.Pipeline.required "hand" (Json.Decode.list Json.Decode.string)
  |> Json.Decode.Pipeline.required "submitted" Json.Decode.string
  |> Json.Decode.Pipeline.required "winner" Json.Decode.string
  |> Json.Decode.Pipeline.required "score" Json.Decode.int
  |> Json.Decode.Pipeline.required "round" Json.Decode.int
  |> Json.Decode.Pipeline.required "toJudge" (Json.Decode.list Json.Decode.string)
  |> Json.Decode.Pipeline.required "judgeName" Json.Decode.string
  |> Json.Decode.Pipeline.required "allPlayers" (Json.Decode.list Json.Decode.string)
  |> Json.Decode.Pipeline.required "leaderboard" (Json.Decode.keyValuePairs Json.Decode.int)


init : (Model, Cmd Msg)
init =
  (Model 0 "" "" "" [] "" "" 0 0 [] "" [] [], Cmd.none)


-- UPDATE

type Msg
  = Select String
  | Winner String
  | EnterName String
  | SubmitName
  | SubmitID Int
  | ServerMsg String
  | NextRound

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    Select card ->
      (model
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
      (model
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
      if String.length content == 0 then
        (model, WebSocket.send address "")
      else
        let
          updated = case Json.Decode.decodeString modelDecoder content of
            Ok decoded -> decoded
            Err msg -> { model | serverError = "unable to parse server response: " ++ msg }
        in
          (updated, Cmd.none)

    NextRound ->
      (model, WebSocket.send  address
        (Json.Encode.encode 0
          (Json.Encode.object
            [ ("id", Json.Encode.int model.player)
            , ("nextRound", Json.Encode.bool True)
            ]
          )
        )
      )


-- SUBSCRIPTIONS

subscriptions : Model -> Sub Msg
subscriptions model =
  WebSocket.listen address ServerMsg


-- VIEW

mainContainer : List Style
mainContainer =
  [ fontFamily "sans-serif"
  , fontSize "18px"
  , padding "50px"
  ]

titleStyle : List Style
titleStyle =
  [ fontSize "32px"
  , fontWeight "bold"
  , marginBottom "20px"
  ]

judgingTitle : List Style
judgingTitle =
  [ marginBottom "20px"
  , fontSize "24px"
  , fontWeight "bold"
  ]

serverError : List Style
serverError =
  [ fontSize "22px"
  , fontWeight "bold"
  , color "red"
  ]

nameBox : List Style
nameBox =
  [ ]

enterName : List Style
enterName =
  [ margin "0 10px 0 10px"
  , padding "5px"
  , fontSize "18px"
  , border "none"
  , borderBottomStyle "solid"
  , borderBottomWidth "2px"
  , borderBottomColor "black"
  , fontWeight "bold"
  ]

enterButton : List Style
enterButton =
  [ padding "5px"
  , fontSize "16px"
  , border "2px solid black"
  , background "white"
  , fontWeight "bold"
  ]

info : List Style
info =
  [ margin "0 0 30px 0"]

spacer : List Style
spacer =
  [ paddingTop "20px"
  , borderStyle "none"
  ]

playerLabel : List Style
playerLabel =
  [ color "#ABABAB" ]

playerName : List Style
playerName =
  [ ]

gameMain : List Style
gameMain =
  [ border "1px solid black"
  , padding "20px"
  , display "inline-block"
  ]

greenStyle : List Style
greenStyle =
  [ fontSize "22px"
  , fontWeight "bold"
  , marginTop "10px"
  ]

greenUnderline : List Style
greenUnderline =
  [ display "inline-block"
  , Style.width "140px"
  , borderBottomStyle "solid"
  , borderBottomWidth "2px"
  , borderBottomColor "#000000"
  , marginLeft "5px"
  , marginTop "10px"
  ]

appleStyle : List Style
appleStyle =
  [ Style.width "140px"
  , padding "10px"
  , border "2px solid black"
  , marginRight "20px"
  , fontSize "18px"
  ]

selectedApple : List Style
selectedApple =
  List.concat
    [ appleStyle,
      [ background "#FFFFFF"
      , color "#000000"
      , fontWeight "bold"
      ]
    ]

unselectedApple : List Style
unselectedApple =
  List.concat
    [ appleStyle,
      [ background "#000000"
      , color "#FFFFFF"
      ]
    ]

greenApples : List Style
greenApples =
  [ marginTop "20px"

  ]

winner : List Style
winner =
  [ fontSize "24px"
  , fontWeight "bold"
  ]

nextRound : List Style
nextRound =
  [ margin "20px 0 0 0"
  , padding "8px"
  , fontSize "24px"
  , border "2px solid black"
  , background "white"
  , fontWeight "bold"
  ]

leaderboard : List Style
leaderboard =
  [ Style.float "right" ]

leaderboardTbl : List Style
leaderboardTbl =
  [ border "1px solid black"
  ]


view : Model -> Html Msg
view model =
  div [style mainContainer]
    [ div [style titleStyle] [text "Apples to Apples"]
    , (if String.length model.serverError == 0 then
        div [] []
      else
        div [style serverError] [text model.serverError]
      )
    , div [style nameBox] (if model.player == 0 then
        [ span [] [text "Enter your name:"]
        , input [style enterName, onInput EnterName] []
        , button [style enterButton, onClick SubmitName] [text "Start Game"]
        ]
      else
        [ div [style info]
          [ div []
            [ span [style playerLabel] [text "Player "]
            , span [style playerName] [text model.name]
            ]
          , div []
            [ span [style playerLabel] [text "Players "]
            , span [style playerName] (List.map (\player -> text (player ++ ", ")) model.allPlayers)
            ]
          , div []
            [ span [style playerLabel] [text "Score "]
            , span [style playerName] [text (toString model.score)]
            ]
          ]
        , div [style leaderboard]
          -- Leaderboard
          [ Html.table [style leaderboardTbl]
            (List.concat
              [ [ th [style leaderboardTbl] [text "Player"], th [style leaderboardTbl] [text "Score"]]
              , (List.map (\(name, score) -> tr [] [td [style leaderboardTbl] [text name], td [style leaderboardTbl] [text (toString score)]]) model.leaderboard)
              ]
            )
          ]
        , (if model.judgeName /= model.name && List.length model.toJudge == 0 then
          -- Playing
            div [style gameMain]
            [ div []
              [ span [style playerLabel] [text "Round "]
              , span [style playerName] [text (toString model.round)]
              ]
            , div []
              [ span [style playerLabel] [text "Judge "]
              , span [style playerName] [text model.judgeName]
              ]
            , hr [style spacer] []
            , div []
              [ span [style greenStyle] [text (model.green)]
              , (if String.length model.submitted == 0 then
                  span [style greenUnderline] []
                else
                  span [style greenStyle] [text (" " ++ model.submitted)])
              ]
            , div [style greenApples]
              (if String.length model.submitted == 0 then
                (List.map (\card -> button [style unselectedApple, onClick (Select card)] [text card]) model.hand)
              else
                (List.map (\card -> button [style (if model.submitted == card then selectedApple else unselectedApple)] [text card]) model.hand))
            ]

        else if model.judgeName == model.name && String.length model.winner == 0 then
          -- Judging
          div []
          [ div [style judgingTitle] [ text (model.name ++ ", you are judging!")]
          , div [style gameMain]
            [ div []
              [ div []
                [ span [style greenStyle] [text (model.green)]
                , span [style greenUnderline] []
                ]
              , hr [style spacer] []
              , (if List.length model.toJudge == 0 then
                  div [] [text "Waiting for players to submit cards..."]
                else
                  div [] (List.map (\submitted -> button [style unselectedApple, onClick (Winner submitted)] [text submitted]) model.toJudge)
                )
              ]
            ]
          ]
        else
          -- Showing results
          div []
          [ div [style gameMain]
            [ (if String.length model.winner == 0 then
                span [style winner] [text ("Waiting for judge " ++ model.judgeName ++ ": " ++ model.green)]
              else
                span [style winner] [text ("Winner: " ++ model.green ++ " " ++ model.winner)]
              )
            , hr [style spacer] []
            , div [] (List.map (\card -> button [style (if model.winner == card then selectedApple else unselectedApple)] [text card]) model.toJudge)
            ]
          , (if model.judgeName == model.name then
              div [] [button [style nextRound, onClick NextRound] [text "Next round!"]]
            else
              div [] []
            )
          ]
        )
        ]
      )
    ]
