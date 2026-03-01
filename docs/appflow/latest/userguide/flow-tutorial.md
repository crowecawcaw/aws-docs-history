# Tutorial: Transfer data between applications with Amazon AppFlow

This tutorial explains how to use Amazon AppFlow with [Amazon Simple Storage Service](https://aws.amazon.com/s3 "https://aws.amazon.com/s3") (Amazon S3) and Salesforce through the AWS Management Console. Optionally, if you want to use
a different supported software as a service (SaaS) application, the tutorial provides general
instructions for how to create a flow. A flow uses a connection to transfer data between a
source and a destination. When you run a flow, Amazon AppFlow verifies that the data is available in the
source, processes the data according to the flow configuration, and transfers the processed data
to the destination.

###### Objective

In this tutorial, you learn to transfer data between applications. Specifically, you
transfer data both from Amazon S3 to Salesforce, and from Salesforce to Amazon S3. First, you
synchronize additional account records with the customer relationship management (CRM) data
already stored in Salesforce (Flow 1). You can optionally add validations to this flow to only
transfer good data. Then, you transfer the account data in Salesforce to Amazon S3 in an
event-triggered flow (Flow 2). When Amazon AppFlow detects a change to the target data in the CRM
storage service, an event-triggered flow runs. This way, you have access to up-to-date
information in Amazon S3, where you can import it into an object for data lake hydration to
generate business value.

In this tutorial, you accomplish the following:

- Store a sample data set of accounts in [Amazon Simple Storage Service](https://aws.amazon.com/s3 "https://aws.amazon.com/s3")
  (Amazon S3).
- Flow 1 — Use [Amazon AppFlow](https://aws.amazon.com/appflow "https://aws.amazon.com/appflow") to transfer data from Amazon S3 to Salesforce.
- Flow 2 — Use Amazon AppFlow to transfer data from
  Salesforce to Amazon S3.
  The following diagram shows the two workflows.

![Amazon AppFlow tutorial diagram.](images/flow-tutorial.png)
**Estimated cost:** Some of the actions in this tutorial may
incur minor charges on your AWS account. The provided sample data is 1 KB. Should you choose
to use your own data, you might incur greater charges. Reduce charges by completing the tutorial
through [Step 5: Clean up your resources](flow-tutorial-clean-up.md "flow-tutorial-clean-up.md"). For
information about pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/")
and [Amazon AppFlow pricing](https://aws.amazon.com/appflow/pricing/ "https://aws.amazon.com/appflow/pricing/").

###### Topics

- [Prerequisites](#flow-tutorial-prerequisites "#flow-tutorial-prerequisites")
- [Step 1: Upload data to Amazon S3](flow-tutorial-set-up-source.md "flow-tutorial-set-up-source.md")
- [Step 2: Connect to an application](flow-tutorial-connection.md "flow-tutorial-connection.md")
- [Step 3: Transfer data from Amazon S3 to a SaaS destination](flow-tutorial-s3-salesforce.md "flow-tutorial-s3-salesforce.md")
- [Step 4: Transfer data from a SaaS source to Amazon S3](flow-tutorial-salesforce-s3.md "flow-tutorial-salesforce-s3.md")
- [Step 5: Clean up](flow-tutorial-clean-up.md "flow-tutorial-clean-up.md")

## Prerequisites

Before you begin, you need access to an AWS account and an account for a supported
application. This tutorial uses Salesforce, but you can follow the steps to create flows with
a different application. Before you can access the AWS services in this tutorial, your
administrator must grant the required permissions to your user, group, or role.

- Amazon AppFlow setup — If you haven't already done so,
  complete the [Getting started prerequisites](getting-started.md#prerequisites "getting-started.md#prerequisites").
- AWS Identity and Access Management (IAM) setup — You or your
  administrator must attach the AWS managed policy
  `AmazonAppFlowFullAccess` to your user, group, or role. For
  information on how to attach an IAM policy, see [Adding and removing
  IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_. Also,
  you must create and attach the following policy to your user, group, or role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketTagging",
 "s3:ListBucketVersions",
 "s3:CreateBucket",
 "s3:ListBucket",
 "s3:GetBucketPolicy",
 "s3:PutEncryptionConfiguration",
 "s3:GetEncryptionConfiguration",
 "s3:PutBucketTagging",
 "s3:GetObjectTagging",
 "s3:GetBucketOwnershipControls",
 "s3:PutObjectTagging",
 "s3:DeleteObject",
 "s3:DeleteBucket",
 "s3:DeleteObjectTagging",
 "s3:GetBucketPublicAccessBlock",
 "s3:GetBucketPolicyStatus",
 "s3:PutBucketPublicAccessBlock",
 "s3:PutAccountPublicAccessBlock",
 "s3:ListAccessPoints",
 "s3:PutBucketOwnershipControls",
 "s3:PutObjectVersionTagging",
 "s3:DeleteObjectVersionTagging",
 "s3:GetBucketVersioning",
 "s3:GetBucketAcl",
 "s3:PutObject",
 "s3:GetObject",
 "s3:GetAccountPublicAccessBlock",
 "s3:ListAllMyBuckets",
 "s3:GetAnalyticsConfiguration",
 "s3:GetBucketLocation"
 ],
 "Resource": "*"
 }
 ]
}`

```

For information on how to create IAM policies, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_. These two policies grant you all the permissions that you need
to complete this tutorial. For more information on the different types of policies, see [Managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") in the _IAM User Guide_.

- Salesforce setup (Optional) — If you already have
  a Salesforce account or you want to complete this tutorial with a different SaaS
  application, you can skip this step. Sign up for a free Salesforce developer account
  [here](https://developer.salesforce.com/signup "https://developer.salesforce.com/signup").
