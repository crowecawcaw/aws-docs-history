# Revoking access to an AWS Data Exchange asset revision (AWS CLI)

As a provider of AWS Data Exchange data products, you can use the AWS CLI to revoke subscriber access
to a revision using the following instructions.

###### To revoke a revision (AWS CLI)

1. Use the `revoke-revision` command to revoke a revision.

```
$ AWS dataexchange revoke-revision \
--data-set-id $DATA_SET_ID \
--revision-id $REVISION_ID \
--comment 'Revoking Revision Example'

{
"Id": "ab7859881EXAMPLEdd3e8a4b88fc6a8d",
"Arn": "arn:aws:dataexchange:us-east-1:427362365172:data-sets/$DATA_SET_ID/revisions/$REVISION_ID",
"Comment": "Revoking Revision Example",
"CreatedAt": "2022-03-08T18:54:20.746Z",
"UpdatedAt": "2022-03-09T20:28:53.105Z",
"DataSetId": "24d30f8446a878237c35d011e7b22d0b",
"Finalized": true,
"Revoked": true,
"RevokedAt": "2022-03-09T20:28:53.105Z",
"RevocationComment": "revoking revision example"
}
```

2. After a revision is revoked, you can delete the assets of the revision using the
   AWS Data Exchange `DeleteAsset` API operation.
