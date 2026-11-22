

# Question types

A question set contains questions of three types. You provide each type as a separate list in the request: `yesNo`, `yesNoPerOption`, and `chooseOne`. Every decision has a `name` and the `question` text. Answers identify questions and options by `name`, not by text.

The following table summarizes the question types.


| Type | What you provide | What Elemental Inference returns | 
| --- | --- | --- | 
| yesNo | A name and a question | One score for the question | 
| yesNoPerOption | A name, a question, and 1–50 options | An independent score for each option | 
| chooseOne | A name, a question, and 2–26 options | The selected option, plus a score for each option | 

`yesNo`  
A question that Elemental Inference answers with one score. For example:  

```json
{
  "name": "scoreboard_visible",
  "question": "Is a scoreboard graphic visible on screen?"
}
```

`yesNoPerOption`  
A question that you ask separately about each option. Each option gets its own yes score. The scores are independent, so they don't need to add up to any total, and several options can have high scores. Word the question so that it fits any of the options. For example:  

```json
{
  "name": "sponsor_logo",
  "question": "Is the logo of this brand visible?",
  "options": [
    { "name": "anycompany", "text": "AnyCompany" },
    { "name": "example_corp", "text": "Example Corp" }
  ]
}
```

`chooseOne`  
A multiple-choice question. Elemental Inference returns the option that it selects, plus a score for each option. For example:  

```json
{
  "name": "play_type",
  "question": "What type of play is shown?",
  "options": [
    { "name": "serve", "text": "Serve" },
    { "name": "rally", "text": "Rally" },
    { "name": "replay", "text": "Replay" },
    { "name": "crowd", "text": "Crowd shot" }
  ]
}
```