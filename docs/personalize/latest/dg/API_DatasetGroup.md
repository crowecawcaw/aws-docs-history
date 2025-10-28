# DatasetGroup

A dataset group is a collection of related datasets (Item interactions,
Users, Items, Actions, Action interactions). You create a dataset group by calling [CreateDatasetGroup](API_CreateDatasetGroup.md "API_CreateDatasetGroup.md"). You then create a dataset and add it to a
dataset group by calling [CreateDataset](API_CreateDataset.md "API_CreateDataset.md"). The dataset group is used to create and train a
solution by calling [CreateSolution](API_CreateSolution.md "API_CreateSolution.md"). A dataset group can contain only one of each
type of dataset.

You can specify an AWS Key Management Service (KMS) key to encrypt the datasets in
the group.

## Contents

**creationDateTime**

The creation date and time (in Unix time) of the dataset group.

Type: Timestamp

Required: No

**datasetGroupArn**

The Amazon Resource Name (ARN) of the dataset group.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**domain**

The domain of a Domain dataset group.

Type: String

Valid Values: `ECOMMERCE | VIDEO_ON_DEMAND`

Required: No

**failureReason**

If creating a dataset group fails, provides the reason why.

Type: String

Required: No

**kmsKeyArn**

The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to
encrypt the datasets.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `arn:aws.*:kms:.*:[0-9]{12}:key/.*`

Required: No

**lastUpdatedDateTime**

The last update date and time (in Unix time) of the dataset
group.

Type: Timestamp

Required: No

**name**

The name of the dataset group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**roleArn**

The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access
the AWS Key Management Service (KMS) key. Supplying an IAM role is only valid when also
specifying a KMS key.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: No

**status**

The current status of the dataset group.

A dataset group can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE
  FAILED
- DELETE PENDING

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DatasetGroup.md "../../../goto/SdkForCpp/personalize-2018-05-22/DatasetGroup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetGroup.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DatasetGroup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetGroup.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DatasetGroup.md")
