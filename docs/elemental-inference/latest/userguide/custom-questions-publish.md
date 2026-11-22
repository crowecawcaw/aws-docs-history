

# Publishing a question set version

To publish a version, use the `create-question-set-version` command. Elemental Inference copies `DRAFT` into the next version number. You can add these optional parameters:
+ `--sha256` – Publishes only if the `sha256` value of `DRAFT` still equals the value that you pass. Otherwise, the request fails with a `ConflictException`. Use this parameter to make sure that you publish exactly the questions that you reviewed.
+ `--description` – A description of the version. You can't change it later. For the rules, see [Version description rules](custom-questions-limits-description.md).

The following AWS CLI command publishes the `DRAFT` from the preceding update.

```
aws elemental-inference create-question-set-version \
  --id abcd1234efgh5678ijk \
  --sha256 7d860e0693ddd6ba617a8ddee809bd80804097fcf797ff3856f3a9ced23caace \
  --description "Tennis questions with timeout option"
```

The response describes the new version. Its `sha256` value equals the `sha256` value of `DRAFT`. The following example omits the question lists for brevity.

```json
{
  "arn": "arn:aws:elemental-inference:us-west-2:111122223333:question-set/abcd1234efgh5678ijk",
  "id": "abcd1234efgh5678ijk",
  "name": "tennis-questions",
  "version": "1",
  "latestVersion": "1",
  "description": "Tennis questions with timeout option",
  "sha256": "7d860e0693ddd6ba617a8ddee809bd80804097fcf797ff3856f3a9ced23caace",
  "references": []
}
```

If `DRAFT` hasn't changed since the latest version, Elemental Inference doesn't create a version. Instead, it returns the latest version, with that version's own description. Elemental Inference ignores the description in the request.

The name of the question set is part of the content of a version. If you only rename the question set, the next `create-question-set-version` request publishes a new version.