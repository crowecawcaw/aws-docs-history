

# Updating the DRAFT of a question set

To change your questions, use the `update-question-set` command. This command changes only `DRAFT`. It never changes a published version.

Elemental Inference handles each question type separately, as follows:
+ **Omit a list** – `DRAFT` keeps its questions of that type.
+ **Send a list** – The list replaces all of the questions of that type. You can't add or remove one question on its own. To add a question, send the complete list, including the new question.
+ **Send an empty list (`[]`)** – Elemental Inference removes all of the questions of that type.

You can also rename the question set with `--name`.

Elemental Inference checks the limits and rules on the result of the update, including the questions that you didn't send. For example, a new `yesNo` question name can conflict with the name of a `chooseOne` question that `DRAFT` keeps. The kept questions also count toward the limit of 100 scored items.

The following AWS CLI command replaces the `chooseOne` questions to add a `timeout` option. `DRAFT` keeps its `yesNo` and `yesNoPerOption` questions.

```
aws elemental-inference update-question-set \
  --id abcd1234efgh5678ijk \
  --choose-one '[
    {
      "name": "play_type",
      "question": "What type of play is shown?",
      "options": [
        { "name": "serve", "text": "Serve" },
        { "name": "rally", "text": "Rally" },
        { "name": "replay", "text": "Replay" },
        { "name": "crowd", "text": "Crowd shot" },
        { "name": "timeout", "text": "Break in play" }
      ]
    }
  ]'
```

The response describes the updated `DRAFT`, with a new `sha256` value. The following example omits the question lists for brevity.

```json
{
  "arn": "arn:aws:elemental-inference:us-west-2:111122223333:question-set/abcd1234efgh5678ijk",
  "id": "abcd1234efgh5678ijk",
  "name": "tennis-questions",
  "version": "DRAFT",
  "sha256": "7d860e0693ddd6ba617a8ddee809bd80804097fcf797ff3856f3a9ced23caace",
  "references": []
}
```

A request that changes nothing has no effect. `UpdateQuestionSet` has no precondition, so if two requests update `DRAFT` at the same time, the last one wins. If a request fails with a `ConflictException`, another change happened at the same time. Retry the request.