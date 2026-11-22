

# Adding customer decisions to a feed

To add customer decisions, add a `customQuestions` object to the `contextualMetadata` configuration of an output. You can do this in a `CreateFeed`, `UpdateFeed`, or `AssociateFeed` request. For information about the other contextual metadata settings, see [Configuring contextual metadata](create-feed-outputs.md#create-feed-console-contextual-metadata).

The `customQuestions` object contains the following optional members. You must include at least one of them.
+ `shot` – The question set and version to ask about each shot.
+ `scene` – The question set and version to ask about each scene.

Each member contains a `questionSetId` and a `version`. Set `version` to `DRAFT`, or to a published version number as a string, such as `"1"`.

The following AWS CLI command creates a feed with a contextual metadata output. The output asks Elemental Inference version 1 of the question set about each shot and each scene.

```
aws elemental-inference create-feed \
  --name "my-feed" \
  --outputs '[{
    "name": "contextual-metadata",
    "status": "ENABLED",
    "outputConfig": {
      "contextualMetadata": {
        "extendedAnalysis": "DISABLED",
        "customQuestions": {
          "shot": { "questionSetId": "abcd1234efgh5678ijk", "version": "1" },
          "scene": { "questionSetId": "abcd1234efgh5678ijk", "version": "1" }
        }
      }
    }
  }]'
```

While you test new questions, you can use `DRAFT` instead, as in the following fragment.

```json
"customQuestions": {
  "scene": { "questionSetId": "abcd1234efgh5678ijk", "version": "DRAFT" }
}
```

To change the version that a feed uses, use the `update-feed` command. `UpdateFeed` is a PUT operation, so include every output that you want the feed to keep. For more information, see [Revising using the CLI](modify-delete-feed-cli.md). In the following command, replace {{feed-id}} with the ID of your feed.

```
aws elemental-inference update-feed \
  --id <{{feed-id}}> \
  --name "my-feed" \
  --outputs '[{
    "name": "contextual-metadata",
    "status": "ENABLED",
    "outputConfig": {
      "contextualMetadata": {
        "extendedAnalysis": "DISABLED",
        "customQuestions": {
          "shot": { "questionSetId": "abcd1234efgh5678ijk", "version": "2" },
          "scene": { "questionSetId": "abcd1234efgh5678ijk", "version": "2" }
        }
      }
    }
  }]'
```

If you remove `customQuestions` from the output in an `UpdateFeed` request, the feed stops using the question set.