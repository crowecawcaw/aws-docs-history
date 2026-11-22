

# Listing question sets and versions

To list the versions of a question set, use the `list-question-set-versions` command. The list starts with `DRAFT`, followed by the published versions from the highest number to the lowest.

```
aws elemental-inference list-question-set-versions \
  --id abcd1234efgh5678ijk
```

The following example shows a response.

```json
{
  "versions": [
    {
      "version": "DRAFT",
      "sha256": "7d860e0693ddd6ba617a8ddee809bd80804097fcf797ff3856f3a9ced23caace",
      "lastModifiedAt": "2026-11-27T18:05:12.345000+00:00"
    },
    {
      "version": "1",
      "description": "Tennis questions with timeout option",
      "sha256": "7d860e0693ddd6ba617a8ddee809bd80804097fcf797ff3856f3a9ced23caace",
      "lastModifiedAt": "2026-11-27T18:06:40.120000+00:00"
    }
  ]
}
```

To list the question sets in your account, use the `list-question-sets` command. Each item contains the ARN, ID, name, and `latestVersion` of a question set. The list doesn't include questions. A question set that you just created might take a moment to appear in the list.

```
aws elemental-inference list-question-sets
```

Both commands return results in pages. To control the page size, use `--max-results` with a value of 1–100. If the response contains a `nextToken`, pass it with `--next-token` to get the next page. The last page can be empty. Stop when the response doesn't contain a `nextToken`.