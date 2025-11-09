# Access Amazon Bedrock foundation models

Access to all Amazon Bedrock foundation models is enabled by default with the correct AWS
Marketplace permissions. To get started, simply select a model from the model catalog in the
Amazon Bedrock console and open it in the playground or invoke the model using the [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or
[Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") API operations. For information about the different models supported in Amazon Bedrock, see
[Amazon Bedrock foundation model
information](foundation-models-reference.md "foundation-models-reference.md"). For information about model pricing, see [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

Access to all Amazon Bedrock foundation models is enabled by default with the correct AWS
Marketplace permissions in all commercial AWS regions. For access to models in
non-commercial regions, see [Access Amazon Bedrock foundation models in AWS
GovCloud (US)](#model-access-modify "#model-access-modify").

###### Note

Anthropic requires first-time customers to submit use case details before invoking a
model once per account or once at the organization's management account. You can submit
use case details by selecting an Anthropic model from the model catalog in the Amazon Bedrock
console or calling the `PutUseCaseForModelAccess` API command.
Access
to the model is granted immediately after use case details are successfully submitted.
The form submission at the root account will be inherited by other accounts in the same
AWS Organizations.

###### Note

For 3P models, by invoking/using the model for the first time you are agreeing to the
applicable End User License Agreement. For more information, see [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/") and [Serverless
Third-Party Model License Agreements](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/").

Organizations that need to review and agree to EULA before allowing model usage
should:

1. Initially block model access using Service Control Policies (SCP) or IAM
   policies
2. Review the EULA terms
3. Enable model access through SCP/IAM policies only if you agree to the EULA
   terms

###### Topics

- [Grant IAM permissions to request access to
  Amazon Bedrock foundation models with a product ID](#model-access-permissions "#model-access-permissions")
- [Use product ID condition keys to control
  access](model-access-product-ids.md "model-access-product-ids.md")
- [Access Amazon Bedrock foundation models in AWS
  GovCloud (US)](#model-access-modify "#model-access-modify")

## Grant IAM permissions to request access to

Amazon Bedrock foundation models with a product ID

You can manage model access permissions by creating custom IAM policies. To modify
access to Amazon Bedrock foundation models, you first need to attach an identity-based IAM
policy with the following [AWS Marketplace actions](../../../service-authorization/latest/reference/list_awsmarketplace.md#awsmarketplace-actions-as-permissions "../../../service-authorization/latest/reference/list_awsmarketplace.md#awsmarketplace-actions-as-permissions") to the IAM role that allows access to Amazon Bedrock.

When you first invoke an Amazon Bedrock serverless model served from AWS Marketplace in an
account, Bedrock attempts to automatically enable the model for your account. For this
auto-enablement to work, AWS Marketplace permissions are required.

If you can’t assume AWS Marketplace permission, someone with AWS Marketplace permissions must enable the
model for the account as a one-time step (either manually or via auto-enablement). Once
enabled, all users in the account can invoke the model without needing AWS Marketplace
permissions. Users don't need AWS Marketplace subscription permissions to invoke models after
they've been enabled. These permissions are only required the first time a model is
being used in an account.

Access to Amazon Bedrock serverless foundation models with a product ID is controlled by the
following IAM actions:

| IAM action                        | Description                                                                                                         | Applies to which models                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| aws-marketplace:Subscribe         | Allows an IAM entity to subscribe to AWS Marketplace products, including<br>Amazon Bedrock foundation models.       | Only Amazon Bedrock serverless models that have a product ID in AWS Marketplace. |
| aws-marketplace:Unsubscribe       | Allows an IAM identity to unsubscribe from AWS Marketplace products,<br>including Amazon Bedrock foundation models. | Only Amazon Bedrock serverless models that have a product ID in AWS Marketplace. |
| aws-marketplace:ViewSubscriptions | Allows an IAM identity to return a list of AWS Marketplace products,<br>including Amazon Bedrock foundation models. | Only Amazon Bedrock serverless models that have a product ID in AWS Marketplace. |

###### Note

For the `aws-marketplace:Subscribe` action only, you can use the `aws-marketplace:ProductId` [condition key](../../../service-authorization/latest/reference/list_awsmarketplace.md#awsmarketplace-policy-keys "../../../service-authorization/latest/reference/list_awsmarketplace.md#awsmarketplace-policy-keys") to restrict subscription to specific models.

###### For an IAM identity to request access to models with a product ID

The identity must have a policy attached that allows
`aws-marketplace:Subscribe`.

###### Note

If an identity has already subscribed to a model in one AWS Region, the model
becomes available for the identity to request access in all AWS Regions in which
the model is available, even if `aws-marketplace:Subscribe` is denied for
other Regions.

For information on creating the policy, see [I already have an
AWS account](getting-started.md#getting-started-bedrock-role "getting-started.md#getting-started-bedrock-role").

For the `aws-marketplace:Subscribe` action only, you can use the `aws-marketplace:ProductId` [condition key](../../../service-authorization/latest/reference/list_awsmarketplace.md#awsmarketplace-policy-keys "../../../service-authorization/latest/reference/list_awsmarketplace.md#awsmarketplace-policy-keys") to restrict subscription to specific models.

###### Note

Models from the following providers aren't sold through AWS Marketplace and don't have product keys, so you can't scope the `aws-marketplace` actions to them:

- Amazon
- DeepSeek
- Mistral AI
- Meta
- Qwen
- OpenAI
  You can, however, prevent the usage of these models by denying Amazon Bedrock actions and specifying these model IDs in the `Resource` field. For an example, see [Prevent an identity from using a model
  after access has already been granted](#model-access-prevent-usage "#model-access-prevent-usage").

Select a section to see IAM policy examples for a specific use case:

###### Topics

- [Prevent an identity from
  requesting access to a model with a product ID](#model-access-prevent-subscription "#model-access-prevent-subscription")
- [Prevent an identity from using a model
  after access has already been granted](#model-access-prevent-usage "#model-access-prevent-usage")

### Prevent an identity from

requesting access to a model with a product ID

To prevent an IAM entity from requesting access to a specific model that has a
product ID, attach an IAM policy to the user that denies the
`aws-marketplace:Subscribe` action and scope the
`Condition` field to the product ID of the model.

For example, you can attach the following policy to an identity to prevent it from
subscribing to the Anthropic Claude 3.5 Sonnet model:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "aws-marketplace:Subscribe"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws-marketplace:ProductId": [
 "prod-m5ilt4siql27k"
 ]
 }
 }
 }
 ]
}`

```

###### Note

With this policy, the IAM entity will have access to any newly added models
by default.

If the identity has already subscribed to the model in at least one Region,
this policy doesn't prevent access in other Regions. Instead, you can prevent
its usage by seeing the example in [Prevent an identity from using a model
after access has already been granted](#model-access-prevent-usage "#model-access-prevent-usage").

### Prevent an identity from using a model

after access has already been granted

If an IAM identity has already been granted access to a model, you can prevent
usage of the model by denying all Amazon Bedrock actions and scoping the `Resource`
field to the ARN of the foundation model.

For example, you can attach the following policy to an identity to prevent it from
using the Anthropic Claude 3.5 Sonnet model in all AWS Regions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "bedrock:*"
 ],
 "Resource": [
 "arn:aws:bedrock:*::foundation-model/anthropic.claude-3-5-sonnet-20240620-v1:0"
 ]
 }
 ]
}`

```

## Access Amazon Bedrock foundation models in AWS

GovCloud (US)

Before you can use a foundation model in Amazon Bedrock, you must request access to it. If you
no longer need access to a model, you can remove access from it.

###### Note

Models from the following providers aren't sold through AWS Marketplace and don't have product keys, so you can't scope the `aws-marketplace` actions to them:

- Amazon
- DeepSeek
- Mistral AI
- Meta
- Qwen
- OpenAI
  You can, however, prevent the usage of these models by denying Amazon Bedrock actions and specifying these model IDs in the `Resource` field. For an example, see [Prevent an identity from using a model
  after access has already been granted](#model-access-prevent-usage "#model-access-prevent-usage").

Once access is provided to a model, it is available for all users in the AWS
account.

###### To add or remove access to foundation models

1. Make sure you have [permissions](#model-access-permissions "#model-access-permissions")
   to request access, or modify access, to Amazon Bedrock foundation models.
2. Sign into the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/").
3. In the left navigation pane, under **Bedrock
   configurations**, choose **Model access**.
4. On the **Model access** page, choose **Modify model
   access**.
5. Select the models that you want the account to have access to and unselect the
   models that you don't want the account to have access to. You have the following
   options:

Be sure to review the **End User License Agreement
(EULA)** for terms and conditions of using a model before
requesting access to it.

    * Select the check box next to an individual model to check or uncheck
     it.
    * Select the top check box to check or uncheck all models.
    * Select how the models are grouped and then check or uncheck all the
     models in a group by selecting the check box next to the group. For
     example, you can choose to **Group by provider** and
     then select the check box next to **Cohere** to check
     or uncheck all Cohere models.

6. Choose **Next**.
7. If you add access to Anthropic models, you must describe your use case
   details. Choose **Submit use case details**, fill out the
   form, and then select **Submit form**. Notification of access
   is granted or denied based on your answers when completing the form for the
   provider.
8. Review the access changes you're making, and then read the
   **Terms**.

###### Note

Your use of Amazon Bedrock foundation models is subject to the [seller's pricing terms](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/"),
EULA, and the [AWS service
terms](https://aws.amazon.com/service-terms "https://aws.amazon.com/service-terms"). 9. If you agree with the terms, choose **Submit**. The changes
can take several minutes to be reflected in the console.

###### Note

If you revoke access to a model, it can still be accessed through the API
for some time after you complete this action while the changes propagate. To
immediately remove access in the meantime, add an [IAM
policy to a role to deny access to the model](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-deny-inference "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-deny-inference"). 10. If your request is successful, the **Access status** changes
to **Access granted** or **Available to
request**.

###### Note

For AWS GovCloud (US) customers, follow these steps to access models that are
available in AWS GovCloud (US):

- AWS GovCloud (US) users must locate their standard AWS account ID
  associated with their AWS GovCloud (US) account ID. To find your
  associated ID, you can follow this guide [Finding your associated standard AWS account ID](../../../govcloud-us/latest/UserGuide/govcloud-account-ID-alias.md#find-standard-id "../../../govcloud-us/latest/UserGuide/govcloud-account-ID-alias.md#find-standard-id").
- AWS GovCloud (US) customers can use their standard AWS account ID to
  access models in the Amazon Bedrock console in either the `us-east-1` or
  `us-west-2` region. If you would like to use a model in a
  different region, you can manually create a foundation model agreement by
  calling [ListFoundationModelAgreementOffers](../APIReference/API_ListFoundationModelAgreementOffers.md "../APIReference/API_ListFoundationModelAgreementOffers.md") and then [CreateFoundationModelAgreement](../APIReference/API_CreateFoundationModelAgreement.md "../APIReference/API_CreateFoundationModelAgreement.md") in the AWS API.
- Once you have completed the previous steps, log into your AWS GovCloud
  (US) account and navigate to Amazon Bedrock in `us-gov-west-1`. You should
  now have access to the models that are available in AWS GovCloud.
