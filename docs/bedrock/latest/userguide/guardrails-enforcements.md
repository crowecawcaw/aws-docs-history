# Apply cross-account safeguards with Amazon Bedrock Guardrails enforcements

###### Note

Amazon Bedrock Guardrails enforcements is in preview and subject to change.

Amazon Bedrock Guardrails enforcements enable you to automatically apply safety controls at an AWS account level and at an AWS Organizations level (across accounts) for all model invocations with Amazon Bedrock. This centralized approach maintains consistent safeguards across multiple accounts and applications, eliminating the need to configure guardrails for individual accounts and applications.

###### Key capabilities

The following are the key capabilities of guardrails enforcements:

- Organization-level enforcement – Apply guardrails for all model invocations with Amazon Bedrock across organization units (OUs), individual accounts, or your entire organization using Amazon Bedrock policies (in preview) with AWS Organizations.
- Account-level enforcement – Designate a particular version of a guardrail within an AWS account for all Amazon Bedrock model invocations from that account.
- Layered protection – Combine organization and application-specific guardrails when both are present. The effective safety control will be a union of both guardrails with the most restrictive controls taking precedence in case of the same control from both guardrails.
  The following topics describe how to use Amazon Bedrock Guardrails enforcements:

###### Topics

- [Implementation Guide](#guardrails-enforcements-implementation-guide "#guardrails-enforcements-implementation-guide")
- [Monitoring](#monitoring "#monitoring")
- [Pricing](#pricing "#pricing")
- [Frequently Asked Questions](#faq "#faq")

## Implementation Guide

The tutorials below walk through the steps needed to enforce guardrails for accounts with an AWS Organization and for a single AWS account. With these enforcements, all model invocations to Amazon Bedrock will enforce the safeguards configured within the designated guardrail.

### Tutorial: Organization-Level Enforcement

This tutorial walks you through setting up guardrail enforcement across your AWS organization. By the end, you'll have a guardrail that automatically applies to all Amazon Bedrock model invocations across specified accounts or OUs.

###### Who should follow this tutorial

AWS Organization administrators (with management account access) with permissions to create guardrails and manage AWS Organizations policies.

###### What you'll need

The following are required to complete this tutorial:

- An [AWS organization](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") with management account access
- [IAM permissions](guardrails-permissions.md#guardrails-permissions-use "guardrails-permissions.md#guardrails-permissions-use") to create guardrails and [manage AWS Organizations policies](../../../organizations/latest/userguide/orgs_permissions_overview.md "../../../organizations/latest/userguide/orgs_permissions_overview.md")
- Understanding of your organization's safety requirements

###### To set up organization-level guardrail enforcement

1. ###### Plan your guardrail configuration
   1. Define your safeguards:
      - Review available guardrail filters in the [Amazon Bedrock Guardrails documentation](guardrails.md "guardrails.md")
      - Identify which filter you need. Currently, content filters, denied topics, word filters, sensitive information filters, contextual grounding checks are supported.
      - **Note:** Do not include the automated reasoning policy, as it is unsupported for guardrail enforcements and will cause runtime failures.

   2. Identify target accounts:
      - Determine which OUs, accounts, or your entire organization will have this guardrail enforced

2. ###### Create your guardrail in the management account

Create a guardrail in every region where you want to enforce it with one of the following methods:

    * Using the AWS Management Console:


    	1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
    	 [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
    	2. In the left navigation panel, choose **Guardrails**
    	3. Choose **Create guardrail**
    	4. Follow the wizard to configure your desired filters or safeguards (content filters, denied topics, word filters, sensitive information filters, contextual grounding checks)
    	5. Do not enable the automated reasoning policy
    	6. Complete the wizard to create your guardrail
    * Using the API: Use the [CreateGuardrail](../APIReference/API_agent_CreateGuardrail.md "../APIReference/API_agent_CreateGuardrail.md") API###### Verify

Once created, you should see it in the list of guardrails on the Guardrails landing page or search for it in the list of guardrails using the guardrail name 3. ###### Create a Guardrail Version

Create a numeric version to ensure the guardrail configuration remains immutable and cannot be modified by member accounts.

    * Using the AWS Management Console:


    	1. Select the guardrail created in the previous step in the Guardrails page on the Amazon Bedrock console
    	2. Choose **Create version**
    	3. Note the guardrail ARN and the version number (e.g., "1", "2", etc.)
    * Using the API: Use the [CreateGuardrailVersion](../APIReference/API_agent_CreateGuardrailVersion.md "../APIReference/API_agent_CreateGuardrailVersion.md") API###### Verify

Confirm the version was created successfully by checking the list of versions on the Guardrail detail page. 4. ###### Attach a Resource-Based Policy

Enable cross-account access by attaching a resource-based policy to your guardrail.

    * Using the AWS Management Console – To attach a resource-based policy using the console:


    	1. In the Amazon Bedrock Guardrails console, select your guardrail
    	2. Click **Add** to add a resource-based policy
    	3. Add a policy that grants `bedrock:ApplyGuardrail` permission to all the member accounts or organization. See [Share guardrail with your organization](guardrails-resource-based-policies.md#share-guardrail-with-organization "guardrails-resource-based-policies.md#share-guardrail-with-organization") in [Using resource-based policies for guardrails](guardrails-resource-based-policies.md "guardrails-resource-based-policies.md").
    	4. Save the policy###### Verify

Test access from a member account using the [ApplyGuardrail](../APIReference/API_agent_ApplyGuardrail.md "../APIReference/API_agent_ApplyGuardrail.md") API to ensure authorization is configured correctly. 5. ###### Configure IAM Permissions in Member Accounts

Ensure all roles in member accounts have IAM permissions to access the enforced guardrail.

###### Required permissions

Member account roles need `bedrock:ApplyGuardrail` permission for the management account's guardrail. See [Set up permissions to use Amazon Bedrock Guardrails](guardrails-permissions.md "guardrails-permissions.md") for detailed IAM policy examples

###### Verify

Confirm that roles with scoped down permissions in member accounts can successfully call the `ApplyGuardrail` API with the guardrail. 6. ###### Enable the Amazon Bedrock Policy Type in AWS Organizations

    * Using the AWS Management Console – To enable the Amazon Bedrock policy type using the console:


    	1. Navigate to the AWS Organizations console
    	2. Choose **Policies**
    	3. Choose **Amazon Bedrock policies** (currently in preview)
    	4. Choose **Enable Amazon Bedrock policies** to enable the Amazon Bedrock policy type for your organization
    * Using the API – Use the AWS Organizations [EnablePolicyType](../../../organizations/latest/APIReference/API_EnablePolicyType.md "../../../organizations/latest/APIReference/API_EnablePolicyType.md") API with policy type `BEDROCK_POLICY`###### Verify

Confirm the Amazon Bedrock policy type shows as enabled in the AWS Organizations console. 7. ###### Create and Attach an AWS Organizations Policy

Create a management policy that specifies your guardrail and attach it to your target accounts or OUs.

    * Using the AWS Management Console – To create and attach an AWS Organizations policy using the console:


    	1. In the AWS Organizations console, navigate to **Policies** > **Amazon Bedrock policies**
    	2. Choose **Create policy**
    	3. Specify your guardrail ARN and version
    	4. Configure the `input_tags` setting (set to ignore to prevent member accounts from bypassing the guardrail on the input via [guardrails input tags](guardrails-tagging.md "guardrails-tagging.md")).



    	```
    	{
    	    "bedrock": {
    	        "guardrail_inference": {
    	            "us-east-1": {
    	                "config_1": {
    	                    "identifier": {
    	                        "@@assign": "arn:aws:bedrock:us-east-1:account_id:guardrail/guardrail_id:1"
    	                    },
    	                    "input_tags": {
    	                        "@@assign": "honor"
    	                    }
    	                }
    	            }
    	        }
    	    }
    	}
    	```
    	5. Save the policy
    	6. Attach the policy to your desired targets (organization root, OUs, or individual accounts) by navigating to the **Targets** tab and choosing **Attach**
    * Using the API – Use the AWS Organizations [CreatePolicy](../../../organizations/latest/APIReference/API_CreatePolicy.md "../../../organizations/latest/APIReference/API_CreatePolicy.md") API with policy type `BEDROCK_POLICY`. Use [AttachPolicy](../../../organizations/latest/APIReference/API_AttachPolicy.md "../../../organizations/latest/APIReference/API_AttachPolicy.md") to attach to targetsLearn more: [Amazon Bedrock policies in AWS Organizations](../../../organizations/latest/userguide/orgs_manage_policies_bedrock.md "../../../organizations/latest/userguide/orgs_manage_policies_bedrock.md")

###### Verify

Check that the policy is attached to the correct targets in the AWS Organizations console. 8. ###### Test and verify enforcement

Test that the guardrail is being enforced on member accounts.

###### Verify which guardrail is enforced

    * Using the AWS Management Console – From a member account, navigate to the Amazon Bedrock console, click on **Guardrails** in the left panel. On the Guardrails home page, you should see the organization enforced guardrail under the section **Organization-level enforcement configurations** in the management account and **Organization-level enforced guardrails** in the member account
    * Using the API – From a member account, call [DescribeEffectivePolicy](../../../organizations/latest/APIReference/API_DescribeEffectivePolicy.md "../../../organizations/latest/APIReference/API_DescribeEffectivePolicy.md") with your member account ID as the target ID

###### Test from a member account

    1. Make a Amazon Bedrock inference call using [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md"), [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md"), [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md"), or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md").
    2. The enforced guardrail should automatically apply to both inputs and outputs
    3. Check the response for guardrail assessment information. The guardrail response will include enforced guardrail information.

### Tutorial: Account-Level Enforcement

This tutorial walks you through setting up guardrail enforcement within a single AWS account. By the end, you'll have a guardrail that automatically applies to all Amazon Bedrock model invocations in your account.

###### Who should follow this tutorial

AWS account administrators with permissions to create guardrails and configure account-level settings.

###### What you'll need

The following are required to complete this tutorial:

- An AWS account with appropriate IAM permissions
- Understanding of your account's safety requirements

###### To set up account-level guardrail enforcement

1. ###### Plan you guardrail configuration

###### Define your safeguards

To define your safeguards:

    * Review available guardrail filters in the [Amazon Bedrock Guardrails documentation](guardrails.md "guardrails.md")
    * Identify which filter you need. Currently, content filters, denied topics, word filters, sensitive information filters, contextual grounding checks are supported.
    * **Note:** Do not include the automated reasoning policy, as it is unsupported for guardrail enforcements and will cause runtime failures

2. ###### Create your guardrail

Create a guardrail in every region where you want to enforce it.

###### Via AWS Management Console

To create a guardrail using the console:

    1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
     [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
    2. In the left navigation panel, choose **Guardrails**
    3. Choose **Create guardrail**
    4. Follow the wizard to configure your desired policies (content filters, denied topics, word filters, sensitive information filters)
    5. Do not enable the automated reasoning policy
    6. Complete the wizard to create your guardrail###### Via API

Use the `CreateGuardrail` API

###### Verify

Once created, you should see it in the list of guardrails on the Guardrails landing page or search for it in the list of guardrails using the guardrail name 3. ###### Create a guardrail version

Create a numeric version to ensure the guardrail configuration remains immutable and cannot be modified by member accounts.

###### Via AWS Management Console

To create a guardrail version using the console:

    1. Select the guardrail created in the previous step in the Guardrails page on the Amazon Bedrock console
    2. Choose **Create version**
    3. Note the guardrail ARN and the version number (e.g., "1", "2", etc.)###### Via API

Use the `CreateGuardrailVersion` API

###### Verify

Confirm the version was created successfully by checking the list of versions on the Guardrail detail page. 4. ###### Attach a resource-based policy (optional)

If you want to share the guardrail with specific roles in your account, attach a resource-based policy.

###### Via AWS Management Console

To attach a resource-based policy using the console:

    1. In the Amazon Bedrock Guardrails console, select your guardrail
    2. Click **Add** to add a resource-based policy
    3. Add a policy that grants `bedrock:ApplyGuardrail` permission to the desired roles
    4. Save the policy

5. ###### Enable account-level enforcement

Configure the account to use your guardrail for all Amazon Bedrock invocations. This must be done in every region where you want enforcement.

###### Via AWS Management Console

To enable account-level enforcement using the console:

    1. Navigate to the Amazon Bedrock console
    2. Choose **Guardrails** in the left navigation panel
    3. Under the **Account-level enforcement configurations** section, choose **Add**
    4. Select your guardrail and version
    5. Configure the `input_tags` setting (set to IGNORE to prevent member accounts from bypassing the guardrail on the input via Guardrails input tags)
    6. Submit the configuration
    7. Repeat for each region where you want enforcement###### Via API

Use the `PutEnforcedGuardrailConfiguration` API in every region where you want to enforce the guardrail

###### Verify

You should see the account enforced guardrail under the section **Account enforced guardrail configuration** on the Guardrails page. You can call [ListEnforcedGuardrailsConfiguration](../APIReference/API_agent_ListEnforcedGuardrailsConfiguration.md "../APIReference/API_agent_ListEnforcedGuardrailsConfiguration.md") API to ensure that the enforced guardrail is listed 6. ###### Test and verify enforcement

###### Test using a role in your account

To test enforcement from your account:

    1. Make a Amazon Bedrock inference call using `InvokeModel`, `Converse`, `InvokeModelWithResponseStream`, or `ConverseStream`
    2. The account-enforced guardrail should automatically apply to both inputs and outputs
    3. Check the response for guardrail assessment information. The guardrail response will include enforced guardrail information.

## Monitoring

- Track guardrail interventions and metrics using [CloudWatch metrics for Amazon Bedrock Guardrails](monitoring-guardrails-cw-metrics.md "monitoring-guardrails-cw-metrics.md")
- Review CloudTrail logs for `ApplyGuardrail` API calls to monitor usage patterns such as AccessDenied exceptions indicating IAM permission configuration issues. See [Amazon Bedrock data events in CloudTrail](logging-using-cloudtrail.md#service-name-data-events-cloudtrail "logging-using-cloudtrail.md#service-name-data-events-cloudtrail")

## Pricing

Amazon Bedrock Guardrails enforcement follows the current pricing model for Amazon Bedrock Guardrails based on the number of text units consumed per configured safeguard. Charges apply to each enforced guardrail according to its configured safeguards. For detailed pricing information on individual safeguards, please refer to [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

## Frequently Asked Questions

**How is consumption towards quotas calculated when enforced guardrails apply?**

Consumption will be calculated per guardrail ARN associated with each request and will be counted towards the AWS account making the API call. For example: an `ApplyGuardrail` call with 1000 characters of text and 3 guardrails would generate 3 text units of consumption per guardrail per safeguard in the guardrail.

Member account calls using the Amazon Bedrock Policy will count towards the Service Quotas for the member account. Review the Service Quotas Console or [Service Quotas documentation](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md") and be sure that your Guardrails runtime limits are sufficient for your call volume.

**How do I prevent member accounts from bypassing guardrails using input tags?**

Use the `input_tags` control available in:

- Amazon Bedrock AWS Organizations policies
- The [PutEnforcedGuardrailConfiguration](../APIReference/API_agent_PutEnforcedGuardrailConfiguration.md "../APIReference/API_agent_PutEnforcedGuardrailConfiguration.md") API

Set the value to ignore to prevent member accounts from tagging partial content.

**What happens if I have both organization-level and account-level enforced guardrails as well as a guardrail in my request?**

All 3 guardrails will be enforced at runtime. The net effect is a union of all guardrails, with the most restrictive control taking precedence.

**What happens with models that don't support guardrails?**

For models where Guardrails aren't supported (such as embedding models), a runtime validation error will be thrown.

**Can I delete a guardrail that's being used in an enforcement configuration?**

No. By default, the [DeleteGuardrail](../APIReference/API_agent_DeleteGuardrail.md "../APIReference/API_agent_DeleteGuardrail.md") API prevents deletion of guardrails associated with account-level or organization-level enforcement configurations.
