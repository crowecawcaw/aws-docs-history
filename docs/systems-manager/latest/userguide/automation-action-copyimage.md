AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# `aws:copyImage` – Copy

or encrypt an Amazon Machine Image

Copies an Amazon Machine Image (AMI) from any AWS Region into the current Region. This action
can also encrypt the new AMI.

###### Note

The `aws:copyImage` action supports automatic throttling retry. For
more information, see [Configuring automatic retry for
throttled operations](automation-throttling-retry.md "automation-throttling-retry.md").

###### Input

This action supports most `CopyImage` parameters. For more information,
see [CopyImage](../../../AWSEC2/latest/APIReference/API_CopyImage.md "../../../AWSEC2/latest/APIReference/API_CopyImage.md").

The following example creates a copy of an AMI in the Seoul region
(`SourceImageID`: ami-0fe10819. `SourceRegion`:
ap-northeast-2). The new AMI is copied to the region where you initiated the
Automation action. The copied AMI will be encrypted because the optional
`Encrypted` flag is set to `true`.

YAML

```
name: createEncryptedCopy
action: aws:copyImage
maxAttempts: 3
onFailure: Abort
inputs:
  SourceImageId: ami-0fe10819
  SourceRegion: ap-northeast-2
  ImageName: Encrypted Copy of LAMP base AMI in ap-northeast-2
  Encrypted: true
```

JSON

```
{
    "name": "createEncryptedCopy",
    "action": "aws:copyImage",
    "maxAttempts": 3,
    "onFailure": "Abort",
    "inputs": {
        "SourceImageId": "ami-0fe10819",
        "SourceRegion": "ap-northeast-2",
        "ImageName": "Encrypted Copy of LAMP base AMI in ap-northeast-2",
        "Encrypted": true
    }
}

```

SourceRegion

The region where the source AMI exists.

Type: String

Required: Yes

SourceImageId

The AMI ID to copy from the source Region.

Type: String

Required: Yes

ImageName

The name for the new image.

Type: String

Required: Yes

ImageDescription

A description for the target image.

Type: String

Required: No

Encrypted

Encrypt the target AMI.

Type: Boolean

Required: No

KmsKeyId

The full Amazon Resource Name (ARN) of the AWS KMS key to use when
encrypting the snapshots of an image during a copy operation. For more
information, see [CopyImage](../../../AWSEC2/latest/APIReference/api_copyimage.md "../../../AWSEC2/latest/APIReference/api_copyimage.md").

Type: String

Required: No

ClientToken

A unique, case-sensitive identifier that you provide to ensure request
idempotency. For more information, see [CopyImage](../../../AWSEC2/latest/APIReference/api_copyimage.md "../../../AWSEC2/latest/APIReference/api_copyimage.md").

Type: String

Required: No

###### Output

ImageId

The ID of the copied image.

ImageState

The state of the copied image.

Valid values: `available` | `pending` |
`failed`
