

# Getting the answers with GetMetadata

To get the answers, query the contextual metadata output with the `GetMetadata` operation, in the same way as for other contextual metadata. For more information, see [Querying contextual metadata](query-metadata-query.md#query-metadata-contextual). In the following command, replace {{region}}, {{data-endpoint}}, and {{feed-id}} with your Region, the data endpoint of your feed, and the ID of your feed.

```
# Query contextual metadata.
$ awscurl --service "elemental-inference" --region <{{region}}> \
  -X POST 'https://<{{data-endpoint}}>/v1/feed/<{{feed-id}}>/input/0/metadata' \
  -H "Content-Type: application/json" \
  -d '{"outputName": "contextual-metadata", "timeSpecification": { "ptsBased": { "startPts": 0, "endPts": 5000, "timescale": 1000 }}, "parameters": { "contextualMetadata": {}}}'
```

The following example shows one shot-level item with answers. For brevity, the example omits the other contextual metadata fields, such as `iabTaxonomy`, `garm`, and `mood`.

```json
{
  "items": [
    {
      "pts": 95000,
      "metadata": {
        "contextualMetadata": {
          "type": "SHOT",
          "startPts": 78000,
          "customQuestions": {
            "questionSetId": "abcd1234efgh5678ijk",
            "questionSetVersion": "1",
            "sha256": "7d860e0693ddd6ba617a8ddee809bd80804097fcf797ff3856f3a9ced23caace",
            "yesNo": [
              { "name": "scoreboard_visible", "score": 0.94 },
              { "name": "player_close_up", "score": 0.12 }
            ],
            "yesNoPerOption": [
              {
                "name": "sponsor_logo",
                "options": [
                  { "name": "anycompany", "score": 0.88 },
                  { "name": "example_corp", "score": 0.67 }
                ]
              }
            ],
            "chooseOne": [
              {
                "name": "play_type",
                "selectedOptionName": "rally",
                "options": [
                  { "name": "serve", "score": 0.05 },
                  { "name": "rally", "score": 0.81 },
                  { "name": "replay", "score": 0.09 },
                  { "name": "crowd", "score": 0.03 },
                  { "name": "timeout", "score": 0.02 }
                ]
              }
            ]
          }
        }
      }
    }
  ]
}
```

The `customQuestions` object contains the following fields:
+ `questionSetId` – The ID of the question set that produced the answers.
+ `questionSetVersion` – The version that produced the answers: `DRAFT`, or a version number.
+ `sha256` – The `sha256` value of the questions that produced the answers.
+ `yesNo` – The `name` and `score` of each `yesNo` question.
+ `yesNoPerOption` – For each `yesNoPerOption` question, its `name`, and the `name` and `score` of each option.
+ `chooseOne` – For each `chooseOne` question, its `name`, the `selectedOptionName`, and the `name` and `score` of each option.

The answers are in the same order as the questions in the version. If the version has no questions of a type, the response doesn't include that list.