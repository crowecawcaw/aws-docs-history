# Migrate from CSE-KMS to SSE-KMS

You can specify CSE-KMS encryption in two ways – during the workgroup query
results encryption configuration and in the client-side settings. For more
information, see [Encrypt Athena query results stored in Amazon S3](encrypting-query-results-stored-in-s3.md "encrypting-query-results-stored-in-s3.md"). During the migration
process, it's important to audit your existing workflows that read and write CSE-KMS
data, identify workgroups where CSE-KMS is configured, and locate instances where
CSE-KMS is set through client-side parameters.

## Update workgroup query results encryption settings

Console###### To update encryption settings in the Athena console

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/ "https://console.aws.amazon.com/athena/").
2. In the Athena console navigation pane, choose
   **Workgroups**.
3. On the **Workgroups** page, select the button for the workgroup that you want
   to edit.
4. Choose **Actions**,
   **Edit**.
5. Open **Query result configuration** and choose **Encrypt query
   results**.
6. For **Encryption type** section, choose **SSE_KMS**
   encryption option.
7. Enter your KMS key under **Choose a different
   AWS KMS key (advanced)**.
8. Choose **Save changes**. The updated
   workgroup appears in the list on the
   **Workgroups** page.

CLIRun the following command to update your query results encryption configuration to SSE-KMS in
your workgroup.

```
aws athena update-work-group \
    --work-group "`my-workgroup`" \
    --configuration-updates '{
        "ResultConfigurationUpdates": {
            "EncryptionConfiguration": {
                "EncryptionOption": "SSE_KMS",
                "KmsKey": "`<my-kms-key>`"
            }
        }
    }'
```

## Update client-side query results encryption settings

ConsoleTo update your client-side settings for query results encryption from CSE-KMS to SSE-KMS, see
[Encrypt Athena query results stored in Amazon S3](encrypting-query-results-stored-in-s3.md "encrypting-query-results-stored-in-s3.md").

CLIYou can only specify query results encryption configuration in client-side settings with the
`start-query-execution` command. If you run this CLI
command and override the query results encryption configuration that
you specified in your workgroup with CSE-KMS, change the command to
encrypt query results using `SSE_KMS` as
following.

```
aws athena start-query-execution \
    --query-string "SELECT * FROM `<my-table>`;" \
    --query-execution-context "Database=`<my-database>`,Catalog=`<my-catalog>`" \
    --result-configuration '{
        "EncryptionConfiguration": {
            "EncryptionOption": "SSE_KMS",
            "KmsKey": "`<my-kms-key>`"
        }
    }' \
    --work-group "`<my-workgroup>`"
```

###### Note

- After you update the workgroup or client-side settings, any new data that you insert by write
  queries uses the SSE-KMS encryption instead of CSE-KMS. This is
  because query results encryption configurations also apply to newly
  inserted table data. Athena query result, metadata, and manifest
  files are also encrypted with SSE-KMS.
- Athena can still read tables with the
  `has_encrypted_data` table property even when there
  are a mix of CSE-KMS encrypted and SSE-S3/SSE-KMS objects.
