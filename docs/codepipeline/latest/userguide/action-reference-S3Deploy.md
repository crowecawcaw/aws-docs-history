# Amazon S3 deploy action reference

You use an Amazon S3 deploy action to deploy files to an Amazon S3 bucket for static web site
hosting or archive. You can specify whether to extract deployment files before upload to
your bucket.

###### Note

This reference topic describes the Amazon S3 deployment action for CodePipeline where the
deployment platform is an Amazon S3 bucket configured for hosting. For reference information
about the Amazon S3 source action in CodePipeline, see [Amazon S3 source action reference](action-reference-S3.md "action-reference-S3.md").

###### Topics

- [Action type](#action-reference-S3Deploy-type "#action-reference-S3Deploy-type")
- [Configuration parameters](#action-reference-S3Deploy-config "#action-reference-S3Deploy-config")
- [Input artifacts](#action-reference-S3Deploy-input "#action-reference-S3Deploy-input")
- [Output artifacts](#action-reference-S3Deploy-output "#action-reference-S3Deploy-output")
- [Service role permissions: S3 deploy action](#edit-role-s3deploy "#edit-role-s3deploy")
- [Example action configuration](#action-reference-S3Deploy-example "#action-reference-S3Deploy-example")
- [See also](#action-reference-S3Deploy-links "#action-reference-S3Deploy-links")

## Action type

- Category: `Deploy`
- Owner: `AWS`
- Provider: `S3`
- Version: `1`

## Configuration parameters

**BucketName**

Required: Yes

The name of the Amazon S3 bucket where files are to be deployed.

**Extract**

Required: Yes

If true, specifies that files are to be extracted before upload.
Otherwise, application files remain zipped for upload, such as in the case
of a hosted static web site. If false, then the `ObjectKey` is
required.

**ObjectKey**

Conditional. Required if `Extract` = false

The name of the Amazon S3 object key that uniquely identifies the object in the
S3 bucket.

**KMSEncryptionKeyARN**

Required: No

The ARN of the AWS KMS encryption key for the host bucket. The
`KMSEncryptionKeyARN` parameter encrypts uploaded artifacts
with the provided AWS KMS key. For a KMS key, you can use the key ID,
the key ARN, or the alias ARN.

###### Note

Aliases are recognized only in the account that created the KMS key.
For cross-account actions, you can only use the key ID or key ARN to
identify the key. Cross-account actions involve using the role from the
other account (AccountB), so specifying the key ID will use the key from
the other account (AccountB).

###### Important

CodePipeline only supports symmetric KMS keys. Do not use an asymmetric KMS key to encrypt the
data in your S3 bucket.

**CannedACL**

Required: No

The `CannedACL` parameter applies the specified [canned ACL](../../../AmazonS3/latest/userguide/acl-overview.md#canned-acl "../../../AmazonS3/latest/userguide/acl-overview.md#canned-acl") to
objects deployed to Amazon S3. This overwrites any existing ACL that was applied
to the object.

**CacheControl**

Required: No

The `CacheControl` parameter controls caching behavior for
requests/responses for objects in the bucket. For a list of valid values,
see the [`Cache-Control`](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9 "http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9") header field for HTTP
operations. To enter multiple values in `CacheControl`, use a
comma between each value. You can add a space after each comma (optional),
as shown in this example for the CLI:

```
"CacheControl": "public, max-age=0, no-transform"
```

## Input artifacts

- **Number of Artifacts:**
  `1`
- **Description:** The files for deployment or
  archive are obtained from the source repository, zipped, and uploaded by
  CodePipeline.

## Output artifacts

- **Number of artifacts:**
  `0`
- **Description:** Output artifacts do not apply
  for this action type.

## Service role permissions: S3 deploy action

For S3 deploy action support, add the following to your policy statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl",
 "s3:PutObjectVersionAcl",
 "s3:GetBucketVersioning",
 "s3:GetBucketAcl",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::[[s3DeployBuckets]]",
 "arn:aws:s3:::[[s3DeployBuckets]]/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

For the S3 deploy action support, if your S3 objects have tags, you must also add the
following permissions to your policy statement:

```
"s3:GetObjectTagging",
"s3:GetObjectVersionTagging",
"s3:PutObjectTagging"
```

## Example action configuration

The following show examples for the action configuration.

### Example configuration when

`Extract` is set to `false`

The following example shows the default action configuration when the action is
created with the `Extract` field set to `false`.

YAML

```
Name: Deploy
Actions:
  - Name: Deploy
    ActionTypeId:
      Category: Deploy
      Owner: AWS
      Provider: S3
      Version: '1'
    RunOrder: 1
    Configuration:
      BucketName: website-bucket
      Extract: 'false'
      ObjectKey: MyWebsite
    OutputArtifacts: []
    InputArtifacts:
      - Name: SourceArtifact
    Region: us-west-2
    Namespace: DeployVariables
```

JSON

```
{
    "Name": "Deploy",
    "Actions": [
        {
            "Name": "Deploy",
            "ActionTypeId": {
                "Category": "Deploy",
                "Owner": "AWS",
                "Provider": "S3",
                "Version": "1"
            },
            "RunOrder": 1,
            "Configuration": {
                "BucketName": "website-bucket",
                "Extract": "false",
                "ObjectKey": "MyWebsite"
                },
            "OutputArtifacts": [],
            "InputArtifacts": [
                {
                    "Name": "SourceArtifact"
                }
            ],
            "Region": "us-west-2",
            "Namespace": "DeployVariables"
        }
    ]
},
```

### Example configuration when

`Extract` is set to `true`

The following example shows the default action configuration when the action is
created with the `Extract` field set to `true`.

YAML

```
Name: Deploy
Actions:
  - Name: Deploy
    ActionTypeId:
      Category: Deploy
      Owner: AWS
      Provider: S3
      Version: '1'
    RunOrder: 1
    Configuration:
      BucketName: website-bucket
      Extract: 'true'
    OutputArtifacts: []
    InputArtifacts:
      - Name: SourceArtifact
    Region: us-west-2
    Namespace: DeployVariables
```

JSON

```
{
    "Name": "Deploy",
    "Actions": [
        {
            "Name": "Deploy",
            "ActionTypeId": {
                "Category": "Deploy",
                "Owner": "AWS",
                "Provider": "S3",
                "Version": "1"
            },
            "RunOrder": 1,
            "Configuration": {
                "BucketName": "website-bucket",
                "Extract": "true"
                },
            "OutputArtifacts": [],
            "InputArtifacts": [
                {
                    "Name": "SourceArtifact"
                }
            ],
            "Region": "us-west-2",
            "Namespace": "DeployVariables"
        }
    ]
},
```

## See also

The following related resources can help you as you work with this action.

- [Tutorial: Create a pipeline that uses Amazon S3 as a
  deployment provider](tutorials-s3deploy.md "tutorials-s3deploy.md")
  – This tutorial walks you through two examples for creating a pipeline
  with an S3 deploy action. You download sample files, upload the files to your
  CodeCommit repository, create your S3 bucket, and configure your bucket for hosting.
  Next, you use the CodePipeline console to create your pipeline and specify an Amazon S3
  deployment configuration.
- [Amazon S3 source action reference](action-reference-S3.md "action-reference-S3.md")
  – This action reference provides reference information and examples for
  Amazon S3 source actions in CodePipeline.
