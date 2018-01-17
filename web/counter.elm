import Html exposing (..)
import Html.Events exposing (..)


main =
  Html.beginnerProgram { model = init, view = view, update = update }


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

init : Model
init =
  (Model 0 "" "" [] "" False "" 0)


-- UPDATE

type Msg = Select String | Winner String | EnterName String | SubmitName

update : Msg -> Model -> Model
update msg model =
  case msg of
    Select card ->
      { model | submitted = card }

    Winner card ->
      model
      --send to server

    EnterName name ->
      { model | name = name }

    SubmitName ->
      { model | player = 1 }
      --send to server


-- VIEW

view : Model -> Html Msg
view model =
  div [] (if model.player == 0
    then
      [input [onInput EnterName] [], button [onClick SubmitName] [text "go"]]
    else 
      [ div [] [ text ("player is " ++ model.name)]
      , div [] [ text (model.green) ]
      , div [] [ text (toString model.hand)]
      ]
    )
