

# Interpreting the answers

Use the following information to interpret the answers.

Scores  
Each score is a number from 0 to 1. Scores are relative model scores, not calibrated probabilities. For example, a score of 0.8 doesn't mean that something is 80% likely. Use scores to rank or compare results. To choose thresholds, test them on your own content. Elemental Inference doesn't apply a threshold.

`chooseOne` answers  
The `selectedOptionName` field contains the option that the model picks. The `options` list contains a score for each option.

`yesNoPerOption` answers  
Elemental Inference scores each option independently. Several options can have high scores at the same time.

Shot answers  
The answers from the `shot` question set appear on items with the type `SHOT`. Each item has the latest answers for the shot. The answers are about the shot as a whole, up to that point.

Scene answers  
The answers from the `scene` question set appear on items with the type `SCENE`. Elemental Inference answers the questions periodically while a scene is in progress, and again when the scene ends. A `SCENE` item can have no `customQuestions` object until Elemental Inference first answers the questions for that scene. The final item for a scene has the final answers.

An item can also have no `customQuestions` object when Elemental Inference couldn't answer the questions for that shot or scene. For example, the analysis failed or returned unusable answers, or Elemental Inference couldn't read the version. A missing `customQuestions` object doesn't mean that the feed has no customer decisions.

To find out which questions produced an answer, use the `questionSetVersion` and `sha256` fields. The questions of a published version never change. `DRAFT` can change over time, so the `sha256` value tells you which content of `DRAFT` produced the answer. To compare, run `get-question-set` and check the `sha256` value in the response.