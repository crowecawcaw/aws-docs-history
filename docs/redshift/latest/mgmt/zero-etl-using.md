Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configure authorization for your Amazon Redshift data

warehouse

To replicate data from your integration source into your Amazon Redshift data warehouse, you
must initially add the following two entities:

- _Authorized principal_ – identifies the user or role that
  can create zero-ETL integrations into the data warehouse.
- _Authorized integration source_ – identifies the source
  database that can update the data warehouse.
  You can configure authorized principals and authorized integration sources from the
  **Resource Policy** tab on the Amazon Redshift console or using the Amazon Redshift
  `PutResourcePolicy` API operation.

## Add authorized principals

To create a zero-ETL integration into your Redshift Serverless workgroup or provisioned cluster, authorize
access to the associated namespace or provisioned cluster.

You can skip this step if both of the following conditions are true:

- The AWS account that owns the Redshift Serverless workgroup or provisioned cluster also owns
  the source database.
- That principal is associated with an identity-based IAM policy with permissions
  to create zero-ETL integrations into this Redshift Serverless namespace or provisioned cluster.

### Add authorized principals to an Amazon Redshift Serverless

namespace

1. In the Amazon Redshift console, in the left navigation pane, choose
   **Redshift Serverless**.
2. Choose **Namespace configuration**, then choose your namespace,
   and go to the **Resource Policy** tab.
3. Choose **Add authorized principals**.
4. For each authorized principal that you want to add, enter into the namespace
   either the ARN of the AWS user or role, or the ID of the AWS account that you
   want to grant access to create zero-ETL integrations. An account ID is stored as an
   ARN.
5. Choose **Save changes**.

### Add authorized principals to an Amazon Redshift provisioned

cluster

1. In the Amazon Redshift console, in the left navigation pane, choose **Provisioned
   clusters dashboard**.
2. Choose **Clusters**, then choose the cluster, and go to the
   **Resource Policy** tab.
3. Choose **Add authorized principals**.
4. For each authorized principal that you want to add, enter into the cluster
   either the ARN of the AWS user or role, or the ID of the AWS account that you
   want to grant access to create zero-ETL integrations. An account ID is stored as an
   ARN.
5. Choose **Save changes**.

## Add authorized integration

sources

To allow your source to update your Amazon Redshift data warehouse, you must add it as an
authorized integration source to the namespace.

### Add an authorized integration source to an

Amazon Redshift Serverless namespace

1. In the Amazon Redshift console, go to **Serverless dashboard**.
2. Choose the name of the namespace.
3. Go to the **Resource Policy** tab.
4. Choose **Add authorized integration source**.
5. Specify the ARN of the source for the zero-ETL integration.

###### Note

Removing an authorized integration source stops data from replicating into the
namespace. This action deactivates all zero-ETL integrations from that source into this
namespace.

### Add an authorized integration source to an Amazon Redshift

provisioned cluster

1. In the Amazon Redshift console, go to **Provisioned clusters dashboard**.
2. Choose the name of the provisioned cluster.
3. Go to the **Resource Policy** tab.
4. Choose **Add authorized integration source**.
5. Specify the ARN of the source that's the data source for the
   zero-ETL integration.

###### Note

Removing an authorized integration source stops data from replicating into the
provisioned cluster. This action deactivates all zero-ETL integrations from that source into
this Amazon Redshift provisioned cluster.

## Configure authorization using the Amazon Redshift

API

You can use the Amazon Redshift API operations to configure resource policies that work with
zero-ETL integrations.

To control the source that can create an inbound integration into the namespace,
create a resource policy and attach it to the namespace. With the resource policy, you can
specify the source that has access to the integration. The resource policy is attached to
the namespace of your target data warehouse to allow the source to create an inbound
integration to replicate live data from the source into Amazon Redshift.

The following is a sample resource policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "redshift:AuthorizeInboundIntegration",
 "Resource": "arn:aws:redshift:*:*:integration:*",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:rds:*:111122223333:cluster:*"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111122223333:root"
 },
 "Action": "redshift:CreateInboundIntegration",
 "Resource": "arn:aws:redshift:*:*:integration:*"
 }
 ]
}`

```

The following summarizes the Amazon Redshift API operations applicable to configuring resource
policies for integrations:

- Use the [PutResourcePolicy](../APIReference/API_PutResourcePolicy.md "../APIReference/API_PutResourcePolicy.md") API operation to persist the resource policy. When you
  provide another resource policy, the previous resource policy on the resource is
  replaced. Use the previous example resource policy, which grants permissions for the
  following actions:
  - `CreateInboundIntegration` – Allows the source principal to
    create an inbound integration for data to be replicated from the source into the
    target data warehouse.
  - `AuthorizeInboundIntegration` – Allows Amazon Redshift to continuously
    validate that the target data warehouse can receive data replicated from the
    source ARN.

- Use the [GetResourcePolicy](../APIReference/API_GetResourcePolicy.md "../APIReference/API_GetResourcePolicy.md") API operation is to view existing resource
  policies.
- Use the [DeleteResourcePolicy](../APIReference/API_DeleteResourcePolicy.md "../APIReference/API_DeleteResourcePolicy.md") API operation to remove a resource policy from the
  resource.

To update a resource policy, you can also use the [put-resource-policy](../../../cli/latest/reference/redshift/put-resource-policy.md "../../../cli/latest/reference/redshift/put-resource-policy.md")
AWS CLI command. For example, to put a resource policy on your Amazon Redshift namespace ARN for a
DynamoDB source, run a AWS CLI command similar to the following.

```
aws redshift put-resource-policy \
--policy file://rs-rp.json \
--resource-arn "arn:aws:redshift-serverless:us-east-1:123456789012:namespace/cc4ffe56-ad2c-4fd1-a5a2-f29124a56433"
```

Where `rs-rp.json` contains:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "redshift:AuthorizeInboundIntegration",
 "Resource": "arn:aws:redshift-serverless:us-east-1:123456789012:namespace/cc4ffe56-ad2c-4fd1-a5a2-f29124a56433",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:dynamodb:us-east-1:123456789012:table/test_ddb"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:root"
 },
 "Action": "redshift:CreateInboundIntegration",
 "Resource": "arn:aws:redshift-serverless:us-east-1:123456789012:namespace/cc4ffe56-ad2c-4fd1-a5a2-f29124a56433"
 }
 ]
}`

```
