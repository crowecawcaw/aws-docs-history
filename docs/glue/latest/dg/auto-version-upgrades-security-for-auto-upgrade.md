

# Security for auto upgrade
<a name="auto-version-upgrades-security-for-auto-upgrade"></a>

## Encryption
<a name="auto-version-upgrades-encryption"></a>

AWS Glue keeps run metadata and the summaries apart for each evaluation. All of it is encrypted at rest.

### Encrypt the summaries with your own key
<a name="auto-version-upgrades-encrypt-the-summaries-with-your-own-key"></a>

To encrypt the summaries with a customer managed key, add the following job parameter.


| Key | Value | 
| --- | --- | 
| `--auto-upgrade-metadata-kms-key-arn` | The full ARN of a symmetric AWS KMS key, for example `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`. Aliases aren't supported. | 

For example, add it to the job's `DefaultArguments` when you turn on auto upgrade.

```
aws glue update-job \
  --job-name my-etl-job \
  --job-update '{
    "Role": "arn:aws:iam::111122223333:role/MyGlueJobRole",
    "Command": {"Name": "glueetl", "ScriptLocation": "s3://amzn-s3-demo-bucket/scripts/my-etl-job.py"},
    "GlueVersion": "auto",
    "MaxRetries": 1,
    "DefaultArguments": {"--auto-upgrade-metadata-kms-key-arn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"}
  }'
```

AWS Glue then uses the job role to encrypt the summaries with your key. Your key policy only needs to allow your own users and roles. Add a statement like the following to the key policy.

```
{
  "Sid": "AllowGlueJobRoleToEncryptAutoUpgradeSummaries",
  "Effect": "Allow",
  "Principal": { "AWS": "arn:aws:iam::111122223333:role/MyGlueJobRole" },
  "Action": [ "kms:GenerateDataKey", "kms:Decrypt" ],
  "Resource": "*"
}
```

Then give users who read the summaries `kms:Decrypt` on the key.

AWS Glue checks that the job role can use the key. AWS Glue runs this check when the evaluation starts and again before approval. If the check fails, the evaluation stops with the following reason.

```
The job execution role cannot use the KMS key in --auto-upgrade-metadata-kms-key-arn. Grant the role kms:GenerateDataKey and kms:Decrypt on that key.
```

To read a downloaded summary, decrypt it with the AWS Encryption CLI.

```
aws-encryption-cli --decrypt \
  --input auto_upgrade_summary.md \
  --wrapping-keys key=arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab \
  --commitment-policy require-encrypt-require-decrypt \
  --output auto_upgrade_summary.decrypted.md
```

## Data handling
<a name="auto-version-upgrades-data-handling"></a>
+ AWS Glue uses the job role to read your script and dependency files. It doesn't change your script.
+ AWS Glue collects run metadata to form a baseline. This includes the job's writes, output schema, record counts, and run time. AWS Glue doesn't access your input or output data. The metadata is encrypted at rest. It's kept apart for each account and evaluation. For more information, see [Encryption](#auto-version-upgrades-encryption).
+ The check uses generative AI to explain issues and suggest fixes. The check uses Amazon Bedrock with cross-Region inference. Requests stay in AWS Regions in your geography, such as the US. Your data stays in your primary Region. Prompts and results might go to another Region in that geography. All data is encrypted in transit. Cross-Region inference has no extra cost. For more information, see [Increase throughput with cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html).