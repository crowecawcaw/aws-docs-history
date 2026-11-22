

# Data protection and encryption

Amazon Textract Insights encrypts your data at rest by default and lets you bring your own AWS KMS key for tighter control. This page covers default encryption, customer managed keys, the key policy and encryption context, and the IAM permissions a caller needs.

## Default encryption
<a name="insights-dp-default"></a>

By default, Amazon Textract Insights encrypts your data at rest using AWS owned keys at no additional charge. No configuration is required. Data is also encrypted in transit across Amazon's network.

## Using a customer managed KMS key
<a name="insights-dp-customer-key"></a>

To encrypt with your own AWS KMS key instead of the service default, pass `EncryptionConfiguration` with your KMS key ID on the relevant request. `EncryptionConfiguration` is accepted on `CreateProject`, `UpdateProject`, `CreateBlueprint`, `UpdateBlueprint`, and `StartDocumentInsights`.

```bash
aws textract start-document-insights \
  --region us-east-1 \
  --input-configuration  S3Uri=s3://amzn-s3-demo-bucket/documents/invoice.pdf \
  --output-configuration S3Uri=s3://amzn-s3-demo-destination-bucket/results \
  --project-arn "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh" \
  --encryption-configuration '{"KmsKeyId":"arn:aws:kms:us-east-1:111122223333:key/abcd1234-..."}'
```

You can also supply an optional `KmsEncryptionContext` map:

```json
"EncryptionConfiguration": {
  "KmsKeyId": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-...",
  "KmsEncryptionContext": { "KeyName": "value" }
}
```

On `UpdateProject`, an omitted `KmsKeyId` or `KmsEncryptionContext` keeps the stored value. To return to the service-managed key, send `KmsKeyId` as an empty string.

Using a customer managed key requires `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt` on that key.

## Example key policy
<a name="insights-dp-key-policy"></a>

The following key policy grants a role in your account the permissions Amazon Textract Insights needs. Every `GenerateDataKey` and `Decrypt` call that Amazon Textract Insights makes carries at least one encryption context key that starts with `aws:textract:`, so a single statement covers projects, blueprints, and jobs. Both statements are scoped to your account with `kms:CallerAccount`. Replace `<ACCOUNT-ID>` and `<ROLE-NAME>` with your values.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowTextractDescribeKey",
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::<ACCOUNT-ID>:role/<ROLE-NAME>"},
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:CallerAccount": "<ACCOUNT-ID>"
        }
      }
    },
    {
      "Sid": "AllowTextractInsightsEncryption",
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::<ACCOUNT-ID>:role/<ROLE-NAME>"},
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:CallerAccount": "<ACCOUNT-ID>"
        },
        "ForAnyValue:StringLike": {
          "kms:EncryptionContextKeys": ["aws:textract:*"]
        }
      }
    }
  ]
}
```

## Encryption context
<a name="insights-dp-encryption-context"></a>

Amazon Textract Insights attaches a resource-specific encryption context to every `GenerateDataKey` and `Decrypt` call. The preceding example key policy already covers all of them. To restrict the key to one resource type, add a separate statement that matches that row's context key with the condition shown.


**Encryption context keys by API group**  

| **API group** | **Encryption context key** | **Recommended match condition** | 
| --- | --- | --- | 
| `CreateBlueprint` / `GetBlueprint` / `UpdateBlueprint` | `aws:textract:blueprint-arn` | `StringLike` against `arn:aws:textract:<REGION>:<ACCOUNT-ID>:blueprint/*` for Create, Get, and Update alike. Pin to one blueprint's exact ARN with `StringEquals` only if you intentionally scope the key to a single, fixed blueprint. | 
| `CreateProject` / `GetProject` / `UpdateProject` | `aws:textract:project-arn` | `StringLike` against `arn:aws:textract:<REGION>:<ACCOUNT-ID>:project/*` for Create, Get, and Update alike. | 
| `StartDocumentInsights` and the async workflow | `aws:textract:customer-account-id`, `aws:textract:job-id` | `customer-account-id`: `StringEquals`, always your account ID. `job-id`: `StringLike` against the wildcard job-ARN pattern, because it is a system-generated random GUID, not a fixed value. | 

Because the service also attaches these context entries automatically, prefer `StringLike` with the preceding wildcard patterns over an exact `StringEquals` match on a full job or resource ARN, so that system-generated identifiers do not cause a `Decrypt` to be denied.

If you pass your own `KmsEncryptionContext`, Amazon Textract Insights adds your entries alongside its own context rather than replacing it. Your keys can't start with `aws:textract:`; a request that uses that prefix fails with a `ValidationException`.

## IAM permissions
<a name="insights-dp-iam"></a>

A caller needs the Amazon Textract Insights API actions for the workflow it runs, plus Amazon S3 permissions on the input and output locations, plus AWS KMS permissions when a customer managed key is used.

**Amazon Textract Insights actions**
+ `textract:CreateProject`
+ `textract:GetProject`
+ `textract:UpdateProject`
+ `textract:DeleteProject`
+ `textract:ListProjects`
+ `textract:CreateBlueprint`
+ `textract:CreateBlueprintVersion`
+ `textract:GetBlueprint`
+ `textract:UpdateBlueprint`
+ `textract:DeleteBlueprint`
+ `textract:ListBlueprints`
+ `textract:StartDocumentInsights`
+ `textract:GetDocumentInsights`
+ `textract:TagResource`
+ `textract:UntagResource`
+ `textract:ListTagsForResource`

**Amazon S3 permissions**
+ `s3:GetObject` on the input bucket.
+ `s3:PutObject` on the output bucket.

**AWS KMS permissions (only when using a customer managed key)**
+ `kms:DescribeKey`
+ `kms:GenerateDataKey`
+ `kms:Decrypt`

Grant only the actions needed for the workflow at hand. For an end-to-end job you need at minimum `textract:CreateProject`, `textract:StartDocumentInsights`, `textract:GetDocumentInsights`, and (if you create custom blueprints) `textract:CreateBlueprint`, together with `s3:GetObject` on your input bucket and `s3:PutObject` on your output bucket.