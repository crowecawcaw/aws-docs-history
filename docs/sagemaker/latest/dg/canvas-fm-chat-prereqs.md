# Complete the prerequisites for foundation models in SageMaker Canvas

The following sections outline the prerequisites for interacting with foundation
models and using the document query feature in Canvas. The rest of the content on
this page assumes that you’ve met the prerequisites for foundation models. The document
query feature requires additional permissions.

## Prerequisites for foundation

models

The permissions you need for interacting with models are included in the
Canvas Ready-to-use models permissions. To use the generative AI-powered models
in Canvas, you must turn on the **Canvas Ready-to-use models
configuration** permissions when setting up your Amazon SageMaker AI domain. For
more information, see [Prerequisites for setting up Amazon SageMaker Canvas](canvas-getting-started.md#canvas-prerequisites "canvas-getting-started.md#canvas-prerequisites"). The **Canvas Ready-to-use
models configuration** attaches the [AmazonSageMakerCanvasAIServicesAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess") policy to your Canvas user's
AWS Identity and Access Management (IAM) execution role. If you encounter any issues with granting
permissions, see the topic [Troubleshooting issues with granting permissions through the SageMaker AI console](canvas-limits.md#canvas-troubleshoot-trusted-services "canvas-limits.md#canvas-troubleshoot-trusted-services").

If you’ve already set up your domain, you can edit your domain settings
and turn on the permissions. For instructions on how to edit your domain
settings, see [Edit domain settings](domain-edit.md "domain-edit.md").
When editing the settings for your domain, go to the **Canvas
settings** and turn on the **Enable Canvas Ready-to-use
models** option.

Certain JumpStart foundation models also require that you request a SageMaker AI
instance quota increase. Canvas hosts the models that you’re currently
interacting with on these instances, but the default quota for your account may be
insufficient. If you run into an error while running any of the following models,
request a quota increase for the associated instance types:

- Falcon-40B – `ml.g5.12xlarge`,
  `ml.g5.24xlarge`
- Falcon-13B – `ml.g5.2xlarge`,
  `ml.g5.4xlarge`, `ml.g5.8xlarge`
- MPT-7B-Instruct – `ml.g5.2xlarge`,
  `ml.g5.4xlarge`, `ml.g5.8xlarge`

For the preceding instances types, request an increase from 0 to 1 for the
endpoint usage quota. For more information about how to increase an instance quota
for your account, see [Requesting a
quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User
Guide_.

## Prerequisites for document

querying

###### Note

Document querying is supported in the following AWS Regions:
US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland),
Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), and
Asia Pacific (Mumbai).

The document querying feature requires that you already have an Amazon Kendra index that
stores your documents and document metadata. For more information about Amazon Kendra, see
the [Amazon Kendra
Developer Guide](../../../kendra/latest/dg/what-is-kendra.md "../../../kendra/latest/dg/what-is-kendra.md"). To learn more about the quotas for querying indexes,
see [Quotas](../../../kendra/latest/dg/quotas.md "../../../kendra/latest/dg/quotas.md") in
the _Amazon Kendra Developer Guide_.

You must also make sure that your Canvas user profile has the necessary
permissions for document querying. The [AmazonSageMakerCanvasFullAccess](../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSageMakerCanvasFullAccess.md") policy must be attached to the AWS
IAM execution role for the SageMaker AI domain that hosts your Canvas application
(this policy is attached by default to all new and existing Canvas user
profiles). You must also specifically grant document querying permissions and
specify access to one or more Amazon Kendra indexes.

If your Canvas administrator is setting up a new domain or user profile,
have them set up the domain by following the instructions in [Prerequisites for setting up Amazon SageMaker Canvas](canvas-getting-started.md#canvas-prerequisites "canvas-getting-started.md#canvas-prerequisites"). While
setting up the domain, they can turn on the document querying permissions
through the **Canvas Ready-to-use models
configuration**.

The Canvas administrator can manage document querying permissions at the user
profile level as well. For example, if the administrator wants to grant document
querying permissions to some user profiles but remove permissions for others, they
can edit the permissions for a specific user.

The following procedure shows how to turn on document querying permissions for a
specific user profile:

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations**.
3. Under **Admin configurations**, choose
   **domains**.
4. From the list of domains, select the user profile’s domain.
5. On the **domain details** page, choose the
   **User profile** whose permissions you want to
   edit.
6. On the **User Details** page, choose
   **Edit**.
7. In the left navigation pane, choose **Canvas
   settings**.
8. In the **Canvas Ready-to-use models configuration**
   section, turn on the **Enable document query using Amazon Kendra**
   toggle.
9. In the dropdown, select one or more Amazon Kendra indexes to which you want to
   grant access.
10. Choose **Submit** to save the changes to your domain
    settings.

You should now be able to use Canvas foundation models to query documents in
the specified Amazon Kendra indexes.
