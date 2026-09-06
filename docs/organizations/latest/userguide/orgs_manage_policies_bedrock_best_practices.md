

# Best practices for using Amazon Bedrock policies
<a name="orgs_manage_policies_bedrock_best_practices"></a>

## Use a valid guardrail identifier
<a name="use-valid-guardrail-identifier"></a>

An incorrect or malformed identifier will cause all Amazon Bedrock API calls across the target organization to fail. [Monitor CloudTrail for invalid effective policy alerts to detect misconfigurations quickly](https://docs.aws.amazon.com/organizations/latest/userguide/invalid-policy-alerts.html).

## Exclude automated reasoning policies
<a name="exclude-automated-reasoning-policies"></a>

Guardrails that include an automated reasoning policy are not supported for organization-level enforcement. Verify that your selected Amazon Bedrock Guardrail does not contain one.

## Grant the necessary IAM permissions
<a name="grant-necessary-iam-permissions"></a>

Use [Amazon Bedrock Guardrails resource-based policies](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-resource-based-policies.html) to grant the organization and its member accounts permissions to evaluate the enforced guardrail at runtime.

## Review Amazon Bedrock Service Limits for Guardrails
<a name="review-service-limits"></a>

Member account calls using the Amazon Bedrock Policy will count towards the Service Quotas for the member. Review the Service Quotas Console and be sure that your Guardrails runtime limits are sufficient for your call volume.

## Start small, then scale
<a name="start-small-scale"></a>

Attach your policy to a few accounts to start, making sure the policy is being applied in the way you expect. Make sure to test that the Guardrail permissions are configured to allow cross-account access.

## Validate changes to your Amazon Bedrock policies using DescribeEffectivePolicy
<a name="validate-policy-changes-bedrock"></a>

After you make a change to an Amazon Bedrock policy, check the effective policies for representative accounts below the level where you made the change. You can view the effective policy by using the AWS Management Console, or by using the `DescribeEffectivePolicy` API operation or one of its AWS CLI or AWS SDK variants. Ensure that the change you made had the intended impact on the effective policy.

## Communicate and train
<a name="communicate-and-train-bedrock"></a>

Ensure your organizations understand the purpose and impact of your Amazon Bedrock policies. Provide clear guidance on Amazon Bedrock Guardrails behavior and what to expect.