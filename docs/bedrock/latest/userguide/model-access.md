# Access Amazon Bedrock foundation models

Access to all Amazon Bedrock foundation models is enabled by default with the correct AWS
Marketplace permissions. To get started, simply select a model from the model catalog in the
Amazon Bedrock console and open it in the playground or invoke the model using the [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or
[Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") API operations. For information about the different models supported in Amazon Bedrock, see
[Amazon Bedrock foundation model
information](foundation-models-reference.md "foundation-models-reference.md"). For information about model pricing, see [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

Access to all Amazon Bedrock foundation models is enabled by default with the correct AWS
Marketplace permissions in all commercial AWS regions. For programtic access to third-party models, see [Manage model access using SDK and CLI](#model-access-modify "#model-access-modify").

###### Understanding automatic model access

When you invoke a third-party model for the first time in your account, Amazon Bedrock
automatically initiates the subscription process in the background. During this setup period
(up to 15 minutes), your API calls may succeed temporarily while the subscription is being
finalized. If any prerequisites are missing, initial API calls may succeed temporarily but will
fail with a 403 error after the setup period if the subscription cannot be completed. To avoid
interruptions, verify all prerequisites before invoking models in production.

**Prerequisites for successful model access:**

1. **AWS Marketplace permissions**: Your IAM role must
   have `aws-marketplace:Subscribe`, `aws-marketplace:Unsubscribe`,
   and `aws-marketplace:ViewSubscriptions` permissions. See [Grant IAM permissions to request access to
   Amazon Bedrock foundation models with a product ID](#model-access-permissions "#model-access-permissions") for details.
2. **Anthropic models**: For Anthropic models, you must
   complete the First Time Use (FTU) form before invoking the model.
3. **Valid payment method**: Your AWS account must have
   a valid payment method configured for AWS Marketplace purchases.

###### Note

Anthropic requires first-time customers to submit use case details before invoking a
model once per account or once at the organization's management account. You can submit
use case details by selecting an Anthropic model from the model catalog in the Amazon Bedrock
console or calling the `PutUseCaseForModelAccess` API command.
Access
to the model is granted immediately after use case details are successfully submitted.
The form submission at the root account will be inherited by other accounts in the same
AWS Organization.

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
- [Manage model access using SDK and CLI](#model-access-modify "#model-access-modify")
- [Access Amazon Bedrock foundation models in AWS GovCloud (US)](#model-access-govcloud "#model-access-govcloud")
- [Manage model subscriptions with License Manager](managed-entitlements.md "managed-entitlements.md")

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

For information on creating the policy, see [Quickstart](getting-started.md "getting-started.md").

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

## Manage model access using SDK and CLI

Model access can be managed using SDK in addition to invoking the model. Below steps can be used to create/delete model access as well as check if access already exists or not. Note this is applicable only for third-party models.

Follow these steps to manage model access programmatically:

- [Prerequisites](#model-access-sdk-prerequisites "#model-access-sdk-prerequisites")
- [Step 1: List foundation model agreement offers](#model-access-sdk-step1 "#model-access-sdk-step1")
- [Step 2: [Required one-time for Anthropic models only] Put use case for first-time user](#model-access-sdk-step2 "#model-access-sdk-step2")
- [Step 3: Create foundation model agreement](#model-access-sdk-step3 "#model-access-sdk-step3")
- [Step 4: Get foundation model availability](#model-access-sdk-step4 "#model-access-sdk-step4")
- [[Optional] Step 5: Delete foundation model agreement](#model-access-sdk-step5 "#model-access-sdk-step5")

### Prerequisites

- Attach the [AmazonBedrockFullAccess](../../../aws-managed-policy/latest/reference/AmazonBedrockFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonBedrockFullAccess.md") policy to the IAM user/role used for the SDK/CLI.
- Bedrock SDK Setup: [Set up the AWS SDK for Amazon Bedrock](sdk-general-information-section.md "sdk-general-information-section.md")

Note: Below instructions use python3 for the examples

- Note the modelId of the model for which the access needs to be managed.

### Step 1: List foundation model agreement offers

Use this API to get the agreement offers for a particular model. This will provide the offerToken used to create model access in next steps.

Documentation

- API: [ListFoundationModelAgreementOffers](../APIReference/API_ListFoundationModelAgreementOffers.md "../APIReference/API_ListFoundationModelAgreementOffers.md")
- CLI Documentation: [list-foundation-model-agreement-offers](../../../cli/latest/reference/bedrock/list-foundation-model-agreement-offers.md "../../../cli/latest/reference/bedrock/list-foundation-model-agreement-offers.md")

AWS CLI

```
aws bedrock list-foundation-model-agreement-offers --model-id <ModelId>
```

Python

```
# Placeholder for modelId
model_id = "<enter model id here>"
# Placeholder for offerId
offer_id = "<enter offer id here>"
try:
    # offerType= "ALL" means both public and private offers, if offerType isn't defined, the default would be "PUBLIC"
    model_agreement_offers_response = bedrock_client.list_foundation_model_agreement_offers(modelId=model_id,offerType="ALL")
    print(model_agreement_offers_response)
except ClientError as e:
    print(f"Failed to list foundation model offers for modelId: {model_id} due to the following error: {e}")
```

### Step 2: [Required one-time for Anthropic models only] Put use case for first-time user

Used to put the first-time user use-case form required only for Anthropic models. This is a pre-requisite for gaining access to Anthropic models in the account. This API is only required one time per account or per AWS organization across all commercial regions, with the exception of opt-in regions where this form needs to be filled again.

Documentation

- API: [PutUseCaseForModelAccess](../APIReference/API_PutUseCaseForModelAccess.md "../APIReference/API_PutUseCaseForModelAccess.md")
- CLI Documentation: [put-use-case-for-model-access](../../../cli/latest/reference/bedrock/put-use-case-for-model-access.md "../../../cli/latest/reference/bedrock/put-use-case-for-model-access.md")

AWS CLI

```
aws bedrock put-use-case-for-model-access \
  --form-data <Base64EncodedFormData>
```

Python

```
# Placeholder for form data, replace the names
COMPANY_NAME = "<enter company name here>"
COMPANY_WEBSITE = "<enter company website here>"
INTENDED_USERS = "1" #for external users
INDUSTRY_OPTION = "<enter industry option here>"
OTHER_INDUSTRY_OPTION = "<enter other industry option here>"
USE_CASES = "<enter use cases here>"
form_data = {
    "companyName": COMPANY_NAME,
    "companyWebsite": COMPANY_WEBSITE,
    "intendedUsers": INTENDED_USERS,
    "industryOption": INDUSTRY_OPTION,
    "otherIndustryOption": OTHER_INDUSTRY_OPTION,
    "useCases": USE_CASES
}
form_data_json = json.dumps(form_data)
model_access_response = bedrock_client.put_use_case_for_model_access(formData=form_data_json)
```

For CLI, the form data is base64 encoded json of the form below.

```
{
    "companyName": COMPANY_NAME,
    "companyWebsite": COMPANY_WEBSITE,
    "intendedUsers": INTENDED_USERS,
    "industryOption": INDUSTRY_OPTION,
    "otherIndustryOption": OTHER_INDUSTRY_OPTION,
    "useCases": USE_CASES
}
```

- COMPANY_NAME: String with maximum length of 128
- COMPANY_WEBSITE: String with a maximum length of 128
- INTENDED USERS: Either 0, 1 or 2. 0: Internal, 1: External, 2: Internal_and_External
- INDUSTRY_OPTION: String with maximum length of 128
- OTHER_INDUSTRY_OPTION: String with maximum length of 128
- USE_CASES: String with maximum length of 8192

### Step 3: Create foundation model agreement

Used to create agreement (access) for the foundation model. Use the offer token and modelId from above.

Documentation

- API: [CreateFoundationModelAgreement](../APIReference/API_CreateFoundationModelAgreement.md "../APIReference/API_CreateFoundationModelAgreement.md")
- CLI Documentation: [create-foundation-model-agreement](../../../cli/latest/reference/bedrock/create-foundation-model-agreement.md "../../../cli/latest/reference/bedrock/create-foundation-model-agreement.md")

AWS CLI

```
aws bedrock create-foundation-model-agreement \
  --model-id <ModelId> \
  --offer-token <OfferToken>
```

Python

```
offer_token= ''

for agreement_offer in model_agreement_offers_response['offers']:
    if  agreement_offer['offerId'] == offer_id:

            offer_token = agreement_offer['offerToken']
            print(f"offer token found. Offer token is {offer_token}")
            break


if(not offer_token):
    print(f"Offer token for  modelId: {model_id} is not found")

foundation_model_agreement_reponse = bedrock_client.create_foundation_model_agreement(offerToken= offer_token , modelId= model_id)
```

### Step 4: Get foundation model availability

Used to check if the foundation model currently has access or not. Use the modelId from above.

Documentation

- API: [GetFoundationModelAvailability](../APIReference/API_GetFoundationModelAvailability.md "../APIReference/API_GetFoundationModelAvailability.md")
- CLI Documentation: [get-foundation-model-availability](../../../cli/latest/reference/bedrock/get-foundation-model-availability.md "../../../cli/latest/reference/bedrock/get-foundation-model-availability.md")

AWS CLI

```
aws bedrock get-foundation-model-availability \
  --model-id <ModelId>
```

Python

```
model_availability_response = bedrock_client.get_foundation_model_availability(modelId=model_id)
```

###### Expected response

`agreementAvailability` - `AVAILABLE` if access exists, `NOT_AVAILABLE` is access does not exist.

```
{
  "modelId": "anthropic.claude-sonnet-4-20250514-v1:0",
  "agreementAvailability": {
    "status": "AVAILABLE"
  },
  "authorizationStatus": "AUTHORIZED",
  "entitlementAvailability": "AVAILABLE",
  "regionAvailability": "AVAILABLE"
}
```

### [Optional] Step 5: Delete foundation model agreement

Used to delete foundation model agreement (access). Use the modelId from above.

###### Note

Deleting model access is not enough for blocking access in the future since invoking the model will create the access again. To make sure access is not created again, apply restrictive deny IAM policies for the model.

Documentation

- API: [DeleteFoundationModelAgreement](../APIReference/API_DeleteFoundationModelAgreement.md "../APIReference/API_DeleteFoundationModelAgreement.md")
- CLI Documentation: [delete-foundation-model-agreement](../../../cli/latest/reference/bedrock/delete-foundation-model-agreement.md "../../../cli/latest/reference/bedrock/delete-foundation-model-agreement.md")

AWS CLI

```
aws bedrock delete-foundation-model-agreement \
  --model-id <ModelId>
```

Python

```
delete_foundation_model_agreement_reponse = bedrock_client.delete_foundation_model_agreement(modelId= model_id)
```

## Access Amazon Bedrock foundation models in AWS GovCloud (US)

AWS GovCloud (US) accounts are linked on a one-to-one basis with standard AWS commercial accounts. This linked commercial account is used for billing, service access, support purposes, and access to Amazon Bedrock Model Marketplace. For more information about the relationship between GovCloud and commercial accounts, see [Standard account linking in AWS GovCloud (US)](../../../govcloud-us/latest/UserGuide/getting-started-standard-account-linking.md "../../../govcloud-us/latest/UserGuide/getting-started-standard-account-linking.md").

For third-party models, model access needs to be enabled in both the linked AWS commercial account in addition the AWS GovCloud account. For models provided by Amazon Bedrock, model access only needs to be enabled in the GovCloud account. This is a manual process.

### Enabling model access for AWS GovCloud in linked AWS commercial account (only for third-party models)

Model access can be enabled in an AWS commercial account using 2 ways:

1. Invoke the required model for AWS commercial account in `us-east-1` or `us-west-2` region.
2. Programmatically enable access to the model using SDK/CLI for AWS commercial account in `us-east-1` or `us-west-2` region. This can be done by following the steps described in the previous sections.

### Enabling model access for AWS GovCloud account

In AWS GovCloud (US), you use the **Model access** page in the Amazon Bedrock console in the `us-gov-west-1` region to enable foundation models as described below:

1. Make sure you have [permissions to request model access](model-access.md#model-access-permissions "model-access.md#model-access-permissions") to request access, or modify access, to Amazon Bedrock foundation models. It is recommended to attach the [AmazonBedrockFullAccess](../../../aws-managed-policy/latest/reference/AmazonBedrockFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonBedrockFullAccess.md") policy to the user/role being used.
2. Sign into the Amazon Bedrock console in the `us-gov-west-1` region at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/").
3. In the left navigation pane, under **Bedrock configurations**, choose **Model access**.
4. On the **Model access** page, choose **Modify model access**.
5. Select the models that you want the account to have access to and unselect the models that you don't want the account to have access to. You have the following options:
   1. Be sure to review the **End User License Agreement (EULA)** for terms and conditions of using a model before requesting access to it.
   2. Select the check box next to an individual model to check or uncheck it.
   3. Select the top check box to check or uncheck all models.
   4. Select how the models are grouped and then check or uncheck all the models in a group by selecting the check box next to the group. For example, you can choose to **Group by provider** and then select the check box next to **Cohere** to check or uncheck all Cohere models.

6. Choose **Next**.
7. If you add access to Anthropic models, you must describe your use case details. Choose **Submit use case details**, fill out the form, and then select **Submit form**. Notification of access is granted or denied based on your answers when completing the form for the provider.
8. Review the access changes you're making, and then read the **Terms**.
9. If you agree with the terms, choose **Submit**. The changes can take several minutes to be reflected in the console.
10. If your request is successful, the **Access status** changes to **Access granted** or **Available to request**.
