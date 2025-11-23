# Enforce "Required tag key" with IaC

Tag policies help you maintain consistent tagging across your infrastructure as code (IaC) deployments. With "Required tag keys", you can ensure that all resources created through IaC tools like CloudFormation, Terraform, and Pulumi include the mandatory tags defined by your organization.

This capability checks your IaC deployments against your organization's tag policies before resources are created. When a deployment is missing required tags, you can configure your IaC settings to either warn your development teams or prevent the deployment entirely. This proactive approach maintains tagging compliance from the moment resources are created, rather than requiring manual remediation later. The enforcement works across multiple IaC tools using a single tag policy definition, eliminating the need to configure separate tagging rules for each tool your organization uses.

###### Topics

- [Enforce with CloudFormation](#enforce-with-cloudformation "#enforce-with-cloudformation")
- [Enforce with Terraform](#enforce-with-terraform "#enforce-with-terraform")
- [Enforce with Pulumi](#enforce-with-pulumi "#enforce-with-pulumi")

## Enforce with CloudFormation

###### Note

To enforce required tag keys with CloudFormation, you must specify required tags for your resource type in tag policies. See the
[Reporting for "Required tag key"](orgs_manage_policies_tag-policies-report-tagging-compliance.md#reporting-required-tag-key "orgs_manage_policies_tag-policies-report-tagging-compliance.md#reporting-required-tag-key") section for more details.

**Setup Execution Role for the AWS::TagPolicies::TaggingComplianceValidator Hook**

Before activating the
`AWS::TagPolicies::TaggingComplianceValidator` hook, you must create an execution role that the hook uses to access AWS services. The role must have the following Trust Policy attached to it:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "resources.cloudformation.amazonaws.com",
                    "hooks.cloudformation.amazonaws.com"
                ]
            },
            "Action": [
                "sts:AssumeRole"
            ]
        }
    ]
}
```

The execution role must also have a Role Policy with at least the following permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "tag:ListRequiredTags"
            ],
            "Resource": "*"
        }
    ]
}
```

For more information about setting up execution roles for public extensions, see
[Configure an execution role with IAM permissions and a trust policy for public extension access](../../../AWSCloudFormation/latest/UserGuide/registry-public.md#registry-public-enable-execution-role "../../../AWSCloudFormation/latest/UserGuide/registry-public.md#registry-public-enable-execution-role") in the CloudFormation User Guide.

**Activate the AWS::TagPolicies::TaggingComplianceValidator Hook**

###### Important

Before you continue, verify that you have the permissions required to work with Hooks and view proactive controls from the CloudFormation console. For more information, see
[Grant IAM permissions for CloudFormation Hooks](../../../cloudformation-cli/latest/hooks-userguide/grant-iam-permissions-for-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/grant-iam-permissions-for-hooks.md").

After updating your tag policy, you must activate the
`AWS::TagPolicies::TaggingComplianceValidator` hook in every AWS account and Region where you want to enforce required tagging compliance.

This AWS-managed hook can be configured in two modes:

- **Warn mode**: Allows deployments to proceed but generates warnings when required tags are missing
- **Fail mode**: Blocks deployments that are missing required tags

To activate the hook using the AWS CLI:

```
aws cloudformation activate-type \
    --type HOOK \
    --type-name AWS::TagPolicies::TaggingComplianceValidator \
    --execution-role-arn arn:aws:iam::123456789012:role/MyHookExecutionRole \
    --publisher-id aws-hooks \
    --region us-east-1
```

```
aws cloudformation set-type-configuration \
  --configuration '{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus": "ENABLED", "FailureMode": "WARN", "TargetOperations": ["STACK"], "Properties":{}}}}' \
  --type-arn "arn:aws:cloudformation:us-east-1:123456789012:type/hook/AWS-TagPolicies-TaggingComplianceValidator" \
  --region us-east-1

```

Replace
`region` with your target AWS region, and change
`"FailureMode":"FAIL"` to
`"FailureMode":"WARN"` if you prefer warning mode.

**Activate the AWS::TagPolicies::TaggingComplianceValidator Hook across multiple accounts and Regions with CloudFormation StackSets**

For organizations with multiple AWS accounts, you can use AWS CloudFormation StackSets to activate the tagging compliance hook across all your accounts and Regions simultaneously.

CloudFormation StackSets allow you to deploy the same CloudFormation template to multiple accounts and Regions with a single operation. This approach ensures consistent tagging enforcement across your entire AWS organization without requiring manual configuration in each account.

To use CloudFormation StackSets for this purpose:

1. Create a CloudFormation template that activates the tagging compliance hook
2. Deploy the template using CloudFormation StackSets to target your organizational units or specific accounts
3. Specify all Regions where you want enforcement enabled

The CloudFormation StackSets deployment will automatically handle the activation process across all specified accounts and Regions, ensuring uniform tagging compliance throughout your organization. To learn how to deploy CloudFormation Hooks to an Organization with service-managed CloudFormation StackSets, see this
[AWS blog](https://aws.amazon.com/blogs/devops/deploy-cloudformation-hooks-to-an-organization-with-service-managed-stacksets/ "https://aws.amazon.com/blogs/devops/deploy-cloudformation-hooks-to-an-organization-with-service-managed-stacksets/").

Deploy the CloudFormation template below using CloudFormation StackSets to activate the AWS::TagPolicies::TaggingComplianceValidator Hook for accounts in your organization.

###### Important

This hook only functions as a StackHook. It has no effect when used as a resource hook.

```
Resources:
  # Activate the AWS-managed hook type
  HookTypeActivation:
    Type: AWS::CloudFormation::TypeActivation
    Properties:
        AutoUpdate: True
        PublisherId: "AWS"
        TypeName: "AWS::TagPolicies::TaggingComplianceValidator"

  # Configure the hook
  HookTypeConfiguration:
    Type: AWS::CloudFormation::HookTypeConfig
    DependsOn: HookTypeActivation
    Properties:
      TypeName: "AWS::TagPolicies::TaggingComplianceValidator"
      TypeArn: !GetAtt HookTypeActivation.Arn
      Configuration: !Sub |
        {
          "CloudFormationConfiguration": {
            "HookConfiguration": {
              "TargetStacks": "ALL",
              "TargetOperations": ["STACK"],
              "Properties": {},
              "FailureMode": "Warn",
              "TargetFilters": {
                "Actions": [
                    "CREATE",
                    "UPDATE"
                ]}
            }
          }
        }
```

###### Note

For more information on running CloudFormation hooks, see
[Activate a proactive control-based Hook in your account](../../../cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks-activate-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks-activate-hooks.md").

## Enforce with Terraform

To enforce required tag keys with Terraform, you need to update your Terraform AWS Provider to 6.22.0
or above and enable tag policy validation in your provider configuration. For implementation details and configuration examples,
see the
[Terraform AWS Provider documentation on tag policy enforcement](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/tag-policy-compliance "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/tag-policy-compliance").

## Enforce with Pulumi

To enforce required tag keys with Pulumi, you need to enable the Tag Policy Reporting policy pack in Pulumi Cloud and configure
your IAM role with tag policy read permissions. For implementation details and configuration examples, see the
[Pulumi documentation on tag policy enforcement](https://www.pulumi.com/docs/insights/policy/integrations/aws-organizations-tag-policies/#aws-organizations-tag-policies "https://www.pulumi.com/docs/insights/policy/integrations/aws-organizations-tag-policies/#aws-organizations-tag-policies").
