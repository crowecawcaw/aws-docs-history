

# Creating a question set

To create a question set, use the `create-question-set` command. Specify a name, and at least one question in the `--yes-no`, `--yes-no-per-option`, or `--choose-one` lists. You can also add tags with `--tags`. Elemental Inference creates the question set with its `DRAFT`.

The following AWS CLI command creates a question set for a tennis broadcast. It has questions of all three types.

```
aws elemental-inference create-question-set \
  --name "tennis-questions" \
  --yes-no '[
    { "name": "scoreboard_visible", "question": "Is a scoreboard graphic visible on screen?" },
    { "name": "player_close_up", "question": "Is this a close-up of a player?" }
  ]' \
  --yes-no-per-option '[
    {
      "name": "sponsor_logo",
      "question": "Is the logo of this brand visible?",
      "options": [
        { "name": "anycompany", "text": "AnyCompany" },
        { "name": "example_corp", "text": "Example Corp" }
      ]
    }
  ]' \
  --choose-one '[
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
  ]'
```

This question set has 5 scored items: 2 `yesNo` questions, 2 options in the `yesNoPerOption` question, and 1 `chooseOne` question.

The response describes `DRAFT`. The `latestVersion` field is absent, because you haven't published a version yet. If you omit a list in the request, or send it empty, the response doesn't include that list.

```json
{
  "arn": "arn:aws:elemental-inference:us-west-2:111122223333:question-set/abcd1234efgh5678ijk",
  "id": "abcd1234efgh5678ijk",
  "name": "tennis-questions",
  "version": "DRAFT",
  "sha256": "d15b97b10e14b8861eaef70a7eb0c7741daef8e83bd8f7e9b117a8a34b6cc1bb",
  "yesNo": [
    { "name": "scoreboard_visible", "question": "Is a scoreboard graphic visible on screen?" },
    { "name": "player_close_up", "question": "Is this a close-up of a player?" }
  ],
  "yesNoPerOption": [
    {
      "name": "sponsor_logo",
      "question": "Is the logo of this brand visible?",
      "options": [
        { "name": "anycompany", "text": "AnyCompany" },
        { "name": "example_corp", "text": "Example Corp" }
      ]
    }
  ],
  "chooseOne": [
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
  ],
  "references": []
}
```

To view a question set later, use the `get-question-set` command. By default, it returns `DRAFT`. To view a published version, add `--question-set-version` with the version number. The response contains the name and questions as they were in that version, plus its description, `sha256` value, and references. It also contains the `latestVersion` of the question set.

```
aws elemental-inference get-question-set \
  --id abcd1234efgh5678ijk \
  --question-set-version 1
```