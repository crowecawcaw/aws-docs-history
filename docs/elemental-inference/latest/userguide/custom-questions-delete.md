

# Deleting question set versions and question sets

You can't delete a version or a question set while a feed uses it. This includes archived feeds. A feed keeps its references until you delete the feed. Before you delete, update the feeds to use another version, or delete the feeds. To find the feeds that use a version, check the `references` field in the `get-question-set` response for that version.

To delete one published version, use the `delete-question-set-version` command. You can't delete `DRAFT` this way. To delete `DRAFT`, delete the question set. You can't restore a deleted version, and Elemental Inference doesn't reuse its number. The following AWS CLI command deletes version 1.

```
aws elemental-inference delete-question-set-version \
  --id abcd1234efgh5678ijk \
  --question-set-version 1
```

If a feed uses the version, the request fails with a `ConflictException`.

To delete a question set, with its `DRAFT` and all of its versions, use the `delete-question-set` command. Elemental Inference also removes the tags of the question set. The response contains the ARN and ID of the question set. The following AWS CLI command deletes a question set.

```
aws elemental-inference delete-question-set \
  --id abcd1234efgh5678ijk
```

If a feed uses any version of the question set, including `DRAFT`, the request fails with a `ConflictException`. The error message gives the number of feeds that use the question set.

You can safely retry both commands. If you retry a delete that already succeeded, the request returns a `ResourceNotFoundException`. Treat this error as success.