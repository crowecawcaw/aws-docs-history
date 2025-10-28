# Set up service roles for AWS Clean Rooms ML

The roles needed to perform lookalike modeling differ from those needed to use a
custom model. The following sections describe the roles needed to perform each
task.

###### Topics

- [Set up service roles for lookalike
  modeling](#aws-model-roles "#aws-model-roles")
- [Set up service roles for custom modeling](#custom-model-roles "#custom-model-roles")

## Set up service roles for lookalike

modeling

###### Topics

- [Create a service role to read training
  data](#ml-create-role-training "#ml-create-role-training")
- [Create a service role to write a
  lookalike segment](#ml-create-role-write-segment "#ml-create-role-write-segment")
- [Create a service role to read seed
  data](#ml-create-role-read-seed "#ml-create-role-read-seed")

### Create a service role to read training

data

AWS Clean Rooms uses a service role to read training data. You can create this role
using the console if you have the necessary IAM permissions. If you don't have
`CreateRole` permissions, ask your administrator to create the
service role.

###### To create a service role to train a dataset

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")) with your
   administrator account.
2. Under **Access management**, choose
   **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor**, select the
   **JSON** tab, and then copy and paste the following
   policy.

###### Note

The following example policy supports the permissions needed to
read AWS Glue metadata and its corresponding Amazon S3 data. However, you
might need to modify this policy depending on how you've set up your
S3 data. This policy doesn't include a KMS key to decrypt
data.

Your AWS Glue resources and underlying Amazon S3 resources must be in the
same AWS Region as the AWS Clean Rooms collaboration.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:GetTable",
 "glue:GetTables",
 "glue:GetPartitions",
 "glue:GetPartition",
 "glue:BatchGetPartition",
 "glue:GetUserDefinedFunctions"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:database/`databases`",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/`databases`/`tables`",
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/default"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateDatabase"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:database/default"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket`"
 ],
 "Condition": {
 "StringEquals": {
 "s3:ResourceAccount": [
 "`111122223333`"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucketFolders`/*"
 ],
 "Condition": {
 "StringEquals": {
 "s3:ResourceAccount": [
 "`111122223333`"
 ]
 }
 }
 }
 ]
}`

```

If you need to use a KMS key to decrypt data, add this AWS KMS
statement to the previous template:

```
{
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
            ],
            "Resource": [
                "arn:aws:kms:`region`:`accountId`:key/`keyId`"
            ],
            "Condition": {
                "ArnLike": {
                        "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::`bucketFolders`*"
                }
            }
        }
    ]
}

```

5. Replace each `placeholder` with your own
   information:
   - `region` – The name of the
     AWS Region. For example,
     `us-east-1`.
   - `accountId` – The
     AWS account ID in which the S3 bucket is located.
   - `database/databases`,
     `table/databases/tables`,
     `catalog`, and
     `database/default` – The
     location of the training data that AWS Clean Rooms needs to access.
   - `bucket` – The
     **Amazon Resource Name (ARN)** of the S3
     bucket. The **Amazon Resource Name (ARN)** can
     be found on the **Properties** tab of the
     bucket in Amazon S3.
   - `bucketFolders` – The name of
     specific folders in the S3 bucket that AWS Clean Rooms needs to
     access.

6. Choose **Next**.
7. For **Review and create**, enter a **Policy
   name** and **Description**, and review the
   **Summary**.
8. Choose **Create policy**.

You have created a policy for AWS Clean Rooms. 9. Under **Access management**, choose
**Roles**.

With **Roles**, you can create short-term
credentials, which is recommended for increased security. You can also
choose **Users** to create long-term
credentials. 10. Choose **Create role**. 11. In the **Create role** wizard, for **Trusted
entity type**, choose **Custom trust
policy**. 12. Copy and paste the following custom trust policy into the JSON
editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAssumeRole",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEqualsIfExists": {
 "aws:SourceAccount": ["`111122223333`"]
 },
 "ArnLikeIfExists": {
 "aws:SourceArn": "arn:aws:cleanrooms-ml:`us-east-1`:`111122223333`:training-dataset/*"
 }
 }
 }
 ]
}`

```

The `SourceAccount` is always your AWS account. The
`SourceArn` can be limited to a specific training
dataset, but only after that dataset is created. Because you don't yet
know the training dataset ARN, the wildcard is specified here.

`accountId` is the ID of AWS account that
contains the training data. 13. Choose **Next** and under **Add
permissions**, enter the name of the policy you just
created. (You might need to reload the page.) 14. Select the check box next to the name of the policy you created, and
then choose **Next**. 15. For **Name, review, and create**, enter the
**Role name** and
**Description**.

###### Note

The **Role name** must match the pattern in the
`passRole` permissions granted to the member who can
query and receive results and member roles.

    1. Review **Select trusted entities**, and edit
     if necessary.
    2. Review the permissions in **Add
     permissions**, and edit if necessary.
    3. Review the **Tags**, and add tags if
     necessary.
    4. Choose **Create role**.

You have created the service role for AWS Clean Rooms.

### Create a service role to write a

lookalike segment

AWS Clean Rooms uses a service role to write lookalike segments to a bucket. You can
create this role using the console if you have the necessary IAM permissions.
If you don't have `CreateRole` permissions, ask your administrator to
create the service role.

###### To create a service role to write a lookalike segment

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")) with your
   administrator account.
2. Under **Access management**, choose
   **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor**, select the
   **JSON** tab, and then copy and paste the following
   policy.

###### Note

The following example policy supports the permissions needed to
read AWS Glue metadata and its corresponding Amazon S3 data. However, you
might need to modify this policy depending on how you've set up your
Amazon S3 data. This policy doesn't include a KMS key to decrypt
data.

Your AWS Glue resources and underlying Amazon S3 resources must be in the
same AWS Region as the AWS Clean Rooms collaboration.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`buckets`"
 ],
 "Condition":{
 "StringEquals":{
 "s3:ResourceAccount":[
 "`accountId`"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucketFolders`/*"
 ],
 "Condition":{
 "StringEquals":{
 "s3:ResourceAccount":[
 "`accountId`"
 ]
 }
 }
 }
 ]
}`

```

If you need to use a KMS key to encrypt data, add this AWS KMS
statement to the template:

```
{
            "Effect": "Allow",
            "Action": [
                "kms:Encrypt",
                "kms:GenerateDataKey*",
                "kms:ReEncrypt*",
            ],
            "Resource": [
                "arn:aws:kms:`region`:`accountId`:key/`keyId`"
            ],
            "Condition": {
                "ArnLike": {
                        "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::`bucketFolders`*"
                }
            }
        }
  ]
}
```

5. Replace each `placeholder` with your own
   information:
   - `buckets` – The
     **Amazon Resource Name (ARN)** of the S3
     bucket. The **Amazon Resource Name (ARN)** can
     be found on the **Properties** tab of the
     bucket in Amazon S3.
   - `accountId` – The
     AWS account ID in which the S3 bucket is located.
   - `bucketFolders` – The name of
     specific folders in the S3 bucket that AWS Clean Rooms needs to
     access.
   - `region` – The name of the
     AWS Region. For example,
     `us-east-1`.
   - `keyId` – The KMS key needed
     to encrypt your data.

6. Choose **Next**.
7. For **Review and create**, enter a **Policy
   name** and **Description**, and review the
   **Summary**.
8. Choose **Create policy**.

You have created a policy for AWS Clean Rooms. 9. Under **Access management**, choose
**Roles**.

With **Roles**, you can create short-term
credentials, which is recommended for increased security. You can also
choose **Users** to create long-term
credentials. 10. Choose **Create role**. 11. In the **Create role** wizard, for **Trusted
entity type**, choose **Custom trust
policy**. 12. Copy and paste the following custom trust policy into the JSON
editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAssumeRole",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEqualsIfExists": {
 "aws:SourceAccount": ["`111122223333`"]

 },
 "ArnLikeIfExists": {
 "aws:SourceArn": "arn:aws:cleanrooms-ml:`us-east-1`:`111122223333`:configured-audience-model/*"
 }
 }
 }
 ]
}`

```

The `SourceAccount` is always your AWS account. The
`SourceArn` can be limited to a specific training
dataset, but only after that dataset is created. Because you don't yet
know the training dataset ARN, the wildcard is specified here. 13. Choose **Next**. 14. Select the check box next to the name of the policy you created, and
then choose **Next**. 15. For **Name, review, and create**, enter the
**Role name** and
**Description**.

###### Note

The **Role name** must match the pattern in the
`passRole` permissions granted to the member who can
query and receive results and member roles.

    1. Review **Select trusted entities**, and edit
     if necessary.
    2. Review the permissions in **Add
     permissions**, and edit if necessary.
    3. Review the **Tags**, and add tags if
     necessary.
    4. Choose **Create role**.

You have created the service role for AWS Clean Rooms.

### Create a service role to read seed

data

AWS Clean Rooms uses a service role to read seed data. You can create this role
using the console if you have the necessary IAM permissions. If you don't have
`CreateRole` permissions, ask your administrator to create the
service role.

###### To create a service role to read seed data that is stored in an S3

bucket.

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")) with your
   administrator account.
2. Under **Access management**, choose
   **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor**, select the
   **JSON** tab, and then copy and paste one of the
   following policies.

###### Note

The following example policy supports the permissions needed to
read AWS Glue metadata and its corresponding Amazon S3 data. However, you
might need to modify this policy depending on how you've set up your
Amazon S3 data. This policy doesn't include a KMS key to decrypt
data.

Your AWS Glue resources and underlying Amazon S3 resources must be in the
same AWS Region as the AWS Clean Rooms collaboration.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`buckets`"
 ],
 "Condition": {
 "StringEquals": {
 "s3:ResourceAccount": [
 "`accountId`"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucketFolders`/*"
 ],
 "Condition": {
 "StringEquals": {
 "s3:ResourceAccount": [
 "`accountId`"
 ]
 }
 }
 }
 ]
}`

```

###### Note

The following example policy supports the permissions needed to
read the results of an SQL query and use that as the input data.
However, you might need to modify this policy depending on how your
query is structured. This policy doesn't include a KMS key to
decrypt data.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCleanRoomsStartQuery",
 "Effect": "Allow",
 "Action": [
 "cleanrooms:GetCollaborationAnalysisTemplate",
 "cleanrooms:GetSchema",
 "cleanrooms:StartProtectedQuery"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowCleanRoomsGetAndUpdateQuery",
 "Effect": "Allow",
 "Action": [
 "cleanrooms:GetProtectedQuery",
 "cleanrooms:UpdateProtectedQuery"
 ],
 "Resource": [
 "arn:aws:cleanrooms:`us-east-1`:`111122223333`:membership/`queryRunnerMembershipId`"
 ]
 }
 ]
}`

```

If you need to use a KMS key to decrypt data, add this AWS KMS
statement to the template:

```
{
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:DescribeKey"
            ],
            "Resource": [
                "arn:aws:kms:`region`:`accountId`:key/`keyId`"
            ],
            "Condition": {
                "ArnLike": {
                        "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::`bucketFolders`*"
                }
            }
        }
  ]
}
```

5. Replace each `placeholder` with your own
   information:
   - `buckets` – The
     **Amazon Resource Name (ARN)** of the S3
     bucket. The **Amazon Resource Name (ARN)** can
     be found on the **Properties** tab of the
     bucket in Amazon S3.
   - `accountId` – The
     AWS account ID in which the S3 bucket is located.
   - `bucketFolders` – The name of
     specific folders in the S3 bucket that AWS Clean Rooms needs to
     access.
   - `region` – The name of the
     AWS Region. For example,
     `us-east-1`.
   - `queryRunnerAccountId` – The
     AWS account ID of the account that will run queries.
   - `queryRunnerMembershipId` –
     The **Membership ID** of the member who can
     query. The **Membership ID** can be found on
     the **Details** tab of the collaboration. This
     ensures that AWS Clean Rooms is assuming the role only when this member
     runs the analysis in this collaboration.
   - `keyId` – The KMS key needed
     to encrypt your data.

6. Choose **Next**.
7. For **Review and create**, enter a **Policy
   name** and **Description**, and review the
   **Summary**.
8. Choose **Create policy**.

You have created a policy for AWS Clean Rooms. 9. Under **Access management**, choose
**Roles**.

With **Roles**, you can create short-term
credentials, which is recommended for increased security. You can also
choose **Users** to create long-term
credentials. 10. Choose **Create role**. 11. In the **Create role** wizard, for **Trusted
entity type**, choose **Custom trust
policy**. 12. Copy and paste the following custom trust policy into the JSON
editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAssumeRole",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEqualsIfExists": {
 "aws:SourceAccount": ["`111122223333`"]

 },
 "ArnLikeIfExists": {
 "aws:SourceArn": "arn:aws:cleanrooms-ml:`us-east-1`:`111122223333`:audience-generation-job/*"
 }
 }
 }
 ]
}`

```

The `SourceAccount` is always your AWS account. The
`SourceArn` can be limited to a specific training
dataset, but only after that dataset is created. Because you don't yet
know the training dataset ARN, the wildcard is specified here. 13. Choose **Next**. 14. Select the check box next to the name of the policy you created, and
then choose **Next**. 15. For **Name, review, and create**, enter the
**Role name** and
**Description**.

###### Note

The **Role name** must match the pattern in the
`passRole` permissions granted to the member who can
query and receive results and member roles.

    1. Review **Select trusted entities**, and edit
     if necessary.
    2. Review the permissions in **Add
     permissions**, and edit if necessary.
    3. Review the **Tags**, and add tags if
     necessary.
    4. Choose **Create role**.

You have created the service role for AWS Clean Rooms.

## Set up service roles for custom modeling

###### Topics

- [Create a service role for custom ML
  modeling - ML Configuration](#ml-roles-custom-configure "#ml-roles-custom-configure")
- [Create a service role to
  provide a custom ML model](#ml-roles-custom-model-provider "#ml-roles-custom-model-provider")
- [Create a service role to query a
  dataset](#ml-roles-custom-query-dataset "#ml-roles-custom-query-dataset")
- [Create a service role to
  create a configured table association](#ml-roles-custom-configure-table "#ml-roles-custom-configure-table")

### Create a service role for custom ML

modeling - ML Configuration

AWS Clean Rooms uses a service role to control who can create a custom ML
configuration. You can create this role using the console if you have the
necessary IAM permissions. If you don't have `CreateRole`
permissions, ask your administrator to create the service role.

This role allows you to use the [PutMLConfiguration](../../../cleanrooms-ml/latest/APIReference/API_PutMLConfiguration.md "../../../cleanrooms-ml/latest/APIReference/API_PutMLConfiguration.md") action.

###### To create a service role to allow creation of a custom ML

configuration

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")) with your
   administrator account.
2. Under **Access management**, choose
   **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor**, select the
   **JSON** tab, and then copy and paste the following
   policy.

###### Note

The following example policy supports the permissions needed to
access and write data to an S3 bucket and to publish CloudWatch metrics.
However, you might need to modify this policy depending on how
you've set up your Amazon S3 data. This policy doesn't include a
KMS key to decrypt data.

Your Amazon S3 resources must be in the same AWS Region as the
AWS Clean Rooms collaboration.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowS3ObjectWriteForExport",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket`/*"
 ],
 "Condition": {
 "StringEquals": {
 "s3:ResourceAccount": [
 "`111122223333`"
 ]
 }
 }
 },
 {
 "Sid": "AllowS3KMSEncryptForExport",
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`keyId`"
 ],
 "Condition": {
 "StringLike": {
 "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::`bucket`*"
 }
 }
 },
 {
 "Sid": "AllowCloudWatchMetricsPublishingForTrainingJobs",
 "Action": "cloudwatch:PutMetricData",
 "Resource": "*",
 "Effect": "Allow",
 "Condition": {
 "StringLike": {
 "cloudwatch:namespace": "/aws/cleanroomsml/*"
 }
 }
 },
 {
 "Sid": "AllowCloudWatchLogsPublishingForTrainingOrInferenceJobs",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/cleanroomsml/*"
 ]
 }
 ]
}`

```

5. Replace each `placeholder` with your own
   information:
   - `bucket` – The
     **Amazon Resource Name (ARN)** of the S3
     bucket. The **Amazon Resource Name (ARN)** can
     be found on the **Properties** tab of the
     bucket in Amazon S3.
   - `region` – The name of the
     AWS Region. For example,
     `us-east-1`.
   - `accountId` – The
     AWS account ID in which the S3 bucket is located.
   - `keyId` – The KMS key needed
     to encrypt your data.

6. Choose **Next**.
7. For **Review and create**, enter a **Policy
   name** and **Description**, and review the
   **Summary**.
8. Choose **Create policy**.

You have created a policy for AWS Clean Rooms. 9. Under **Access management**, choose
**Roles**.

With **Roles**, you can create short-term
credentials, which is recommended for increased security. You can also
choose **Users** to create long-term
credentials. 10. Choose **Create role**. 11. In the **Create role** wizard, for **Trusted
entity type**, choose **Custom trust
policy**. 12. Copy and paste the following custom trust policy into the JSON
editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:cleanrooms:`us-east-1`:`111122223333`:membership/`membershipID`"
 }
 }
 }
 ]
}`

```

The `SourceAccount` is always your AWS account. The
`SourceArn` can be limited to a specific training
dataset, but only after that dataset is created. Because you don't yet
know the training dataset ARN, the wildcard is specified here. 13. Choose **Next**. 14. Select the check box next to the name of the policy you created, and
then choose **Next**. 15. For **Name, review, and create**, enter the
**Role name** and
**Description**.

###### Note

The **Role name** must match the pattern in the
`passRole` permissions granted to the member who can
query and receive results and member roles.

    1. Review **Select trusted entities**, and edit
     if necessary.
    2. Review the permissions in **Add
     permissions**, and edit if necessary.
    3. Review the **Tags**, and add tags if
     necessary.
    4. Choose **Create role**.

You have created the service role for AWS Clean Rooms.

### Create a service role to

provide a custom ML model

AWS Clean Rooms uses a service role to control who can create a custom ML model
algorithm. You can create this role using the console if you have the necessary
IAM permissions. If you don't have `CreateRole` permissions, ask
your administrator to create the service role.

This role allows you to use the [CreateConfiguredModelAlgorithm](../../../cleanrooms-ml/latest/APIReference/API_CreateConfiguredModelAlgorithm.md "../../../cleanrooms-ml/latest/APIReference/API_CreateConfiguredModelAlgorithm.md") action.

###### To create a service role to allow a member to provide a custom ML

model

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")) with your
   administrator account.
2. Under **Access management**, choose
   **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor**, select the
   **JSON** tab, and then copy and paste the following
   policy.

###### Note

The following example policy supports the permissions needed to
retrieve the docker image that contains the model algorithm.
However, you might need to modify this policy depending on how
you've set up your Amazon S3 data. This policy doesn't include a
KMS key to decrypt data.

Your Amazon S3 resources must be in the same AWS Region as the
AWS Clean Rooms collaboration.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowECRImageDownloadForTrainingAndInferenceJobs",
 "Effect": "Allow",
 "Action": [
 "ecr:BatchGetImage",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "arn:aws:ecr:`us-east-1`:`111122223333`:repository/`repoName`"
 }
 ]
}`

```

5. Replace each `placeholder` with your own
   information:
   - `region` – The name of the
     AWS Region. For example,
     `us-east-1`.
   - `accountId` – The
     AWS account ID in which the S3 bucket is located.
   - `repoName` – The name of the
     repository that contains your data.

6. Choose **Next**.
7. For **Review and create**, enter a **Policy
   name** and **Description**, and review the
   **Summary**.
8. Choose **Create policy**.

You have created a policy for AWS Clean Rooms. 9. Under **Access management**, choose
**Roles**.

With **Roles**, you can create short-term
credentials, which is recommended for increased security. You can also
choose **Users** to create long-term
credentials. 10. Choose **Create role**. 11. In the **Create role** wizard, for **Trusted
entity type**, choose **Custom trust
policy**. 12. Copy and paste the following custom trust policy into the JSON
editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The `SourceAccount` is always your AWS account The
`SourceArn` can be limited to a specific training
dataset, but only after that dataset is created. Because you don't yet
know the training dataset ARN, the wildcard is specified here. 13. Choose **Next**. 14. Select the check box next to the name of the policy you created, and
then choose **Next**. 15. For **Name, review, and create**, enter the
**Role name** and
**Description**.

###### Note

The **Role name** must match the pattern in the
`passRole` permissions granted to the member who can
query and receive results and member roles.

    1. Review **Select trusted entities**, and edit
     if necessary.
    2. Review the permissions in **Add
     permissions**, and edit if necessary.
    3. Review the **Tags**, and add tags if
     necessary.
    4. Choose **Create role**.

You have created the service role for AWS Clean Rooms.

### Create a service role to query a

dataset

AWS Clean Rooms uses a service role to control who can query a dataset that will be
used for custom ML modeling. You can create this role using the console if you
have the necessary IAM permissions. If you don't have `CreateRole`
permissions, ask your administrator to create the service role.

This role allows you to use the [CreateMLInputChannel](../../../cleanrooms-ml/latest/APIReference/API_CreateMLInputChannel.md "../../../cleanrooms-ml/latest/APIReference/API_CreateMLInputChannel.md") action.

###### To create a service role to allow a member to query a dataset

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")) with your
   administrator account.
2. Under **Access management**, choose
   **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor**, select the
   **JSON** tab, and then copy and paste the following
   policy.

###### Note

The following example policy supports the permissions needed to
query a dataset that will be used for custom ML modeling. However,
you might need to modify this policy depending on how you've set up
your Amazon S3 data. This policy doesn't include a KMS key to decrypt
data.

Your Amazon S3 resources must be in the same AWS Region as the
AWS Clean Rooms collaboration.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCleanRoomsStartQueryForMLInputChannel",
 "Effect": "Allow",
 "Action": "cleanrooms:StartProtectedQuery",
 "Resource": "*"
 },
 {
 "Sid": "AllowCleanroomsGetSchemaAndGetAnalysisTemplateForMLInputChannel",
 "Effect": "Allow",
 "Action": [
 "cleanrooms:GetSchema",
 "cleanrooms:GetCollaborationAnalysisTemplate"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowCleanRoomsGetAndUpdateQueryForMLInputChannel",
 "Effect": "Allow",
 "Action": [
 "cleanrooms:GetProtectedQuery",
 "cleanrooms:UpdateProtectedQuery"
 ],
 "Resource": [
 "arn:aws:cleanrooms:`us-east-1`:`111122223333`:membership/`queryRunnerMembershipId`"
 ]
 }
 ]
}`

```

5. Replace each `placeholder` with your own
   information:
   - `region` – The name of the
     AWS Region. For example,
     `us-east-1`.
   - `queryRunnerAccountId` – The
     AWS account ID of the account that will run the
     queries.
   - `queryRunnerMembershipId` –
     The **Membership ID** of the member who can
     query. The **Membership ID** can be found on
     the **Details** tab of the collaboration. This
     ensures that AWS Clean Rooms is assuming the role only when this member
     runs the analysis in this collaboration.

6. Choose **Next**.
7. For **Review and create**, enter a **Policy
   name** and **Description**, and review the
   **Summary**.
8. Choose **Create policy**.

You have created a policy for AWS Clean Rooms. 9. Under **Access management**, choose
**Roles**.

With **Roles**, you can create short-term
credentials, which is recommended for increased security. You can also
choose **Users** to create long-term
credentials. 10. Choose **Create role**. 11. In the **Create role** wizard, for **Trusted
entity type**, choose **Custom trust
policy**. 12. Copy and paste the following custom trust policy into the JSON
editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The `SourceAccount` is always your AWS account The
`SourceArn` can be limited to a specific training
dataset, but only after that dataset is created. Because you don't yet
know the training dataset ARN, the wildcard is specified here. 13. Choose **Next**. 14. Select the check box next to the name of the policy you created, and
then choose **Next**. 15. For **Name, review, and create**, enter the
**Role name** and
**Description**.

###### Note

The **Role name** must match the pattern in the
`passRole` permissions granted to the member who can
query and receive results and member roles.

    1. Review **Select trusted entities**, and edit
     if necessary.
    2. Review the permissions in **Add
     permissions**, and edit if necessary.
    3. Review the **Tags**, and add tags if
     necessary.
    4. Choose **Create role**.

You have created the service role for AWS Clean Rooms.

### Create a service role to

create a configured table association

AWS Clean Rooms uses a service role to control who can create a configured table
association. You can create this role using the console if you have the
necessary IAM permissions. If you don't have `CreateRole`
permissions, ask your administrator to create the service role.

This role allows you to use the CreateConfiguredTableAssociation action.

###### To create a service role to allow creation of a configured table

association

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")) with your
   administrator account.
2. Under **Access management**, choose
   **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor**, select the
   **JSON** tab, and then copy and paste the following
   policy.

###### Note

The following example policy supports the creation of a configured
table association. However, you might need to modify this policy
depending on how you've set up your Amazon S3 data. This policy doesn't
include a KMS key to decrypt data.

Your Amazon S3 resources must be in the same AWS Region as the
AWS Clean Rooms collaboration.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS-key-ID`",
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`bucket-name`",
 "Effect": "Allow"
 },
 {
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::`bucket-name`/*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:GetTable",
 "glue:GetTables",
 "glue:GetPartitions",
 "glue:GetPartition",
 "glue:BatchGetPartition"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/`Glue database name`",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/`Glue database name`/`Glue table name`"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "glue:GetSchema",
 "glue:GetSchemaVersion"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

###### Replace Placeholder Resource ARNs

When using this policy, you must replace the placeholder resource identifiers
with the actual ARNs of your resources:

    * **AWS KMS Key Resource**: Replace `KMS-key-ID` with the
     actual AWS KMS key ID that encrypts your Amazon S3 data. The key must be in the same
     account (111122223333) that owns the AWS Glue catalog resources.
    * **Amazon S3 Bucket Resources**: Replace `bucket-name` with
     the actual name of the Amazon S3 bucket that contains your AWS Glue table data. Note that
     Amazon S3 bucket ARNs don't include account IDs since bucket names are globally unique.
    * **AWS Glue Resources**: Replace the following placeholders with your actual
     resource names:




    	+ `Glue database name` - The name of your AWS Glue database
    	+ `Glue table name` - The name of your AWS Glue tableAll AWS Glue resources (catalog, database, and table) must be in the same AWS account (111122223333) to ensure consistent access permissions. This

account should be the same one that owns the AWS KMS key used for data encryption,
creating a unified security boundary for your AWS Clean Rooms data resources. 5. Replace each `placeholder` with your own
information:

    * `KMS key used to encrypt the Amazon S3
     data` – The KMS key that was used to
     encrypt the Amazon S3 data. In order to decrypt the data, you need to
     provide the same KMS key that was used to encrypt the
     data.
    * `Amazon S3 bucket of AWS Glue table` –
     The name of the Amazon S3 bucket that contains the AWS Glue table that
     contains your data.
    * `region` – The name of the
     AWS Region. For example,
     `us-east-1`.
    * `accountId` – The
     AWS account ID of the account that owns the data.
    * `AWS Glue database name` – The
     name of the AWS Glue database that contains your data.
    * `AWS Glue table name` – The name
     of the AWS Glue table that contains your data.

6. Choose **Next**.
7. For **Review and create**, enter a **Policy
   name** and **Description**, and review the
   **Summary**.
8. Choose **Create policy**.

You have created a policy for AWS Clean Rooms. 9. Under **Access management**, choose
**Roles**.

With **Roles**, you can create short-term
credentials, which is recommended for increased security. You can also
choose **Users** to create long-term
credentials. 10. Choose **Create role**. 11. In the **Create role** wizard, for **Trusted
entity type**, choose **Custom trust
policy**. 12. Copy and paste the following custom trust policy into the JSON
editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

The `SourceAccount` is always your AWS account The
`SourceArn` can be limited to a specific training
dataset, but only after that dataset is created. Because you don't yet
know the training dataset ARN, the wildcard is specified here. 13. Choose **Next**. 14. Select the check box next to the name of the policy you created, and
then choose **Next**. 15. For **Name, review, and create**, enter the
**Role name** and
**Description**.

###### Note

The **Role name** must match the pattern in the
`passRole` permissions granted to the member who can
query and receive results and member roles.

    1. Review **Select trusted entities**, and edit
     if necessary.
    2. Review the permissions in **Add
     permissions**, and edit if necessary.
    3. Review the **Tags**, and add tags if
     necessary.
    4. Choose **Create role**.

You have created the service role for AWS Clean Rooms.
