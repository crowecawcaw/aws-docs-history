**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS managed policies for AWS Firewall Manager

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: `AWSFMAdminFullAccess`

Use the `AWSFMAdminFullAccess` AWS managed policy to allow your administrators to access AWS Firewall Manager resources, including all Firewall Manager policy types. This policy doesn't include permissions for setting up Amazon Simple Notification Service notifications in AWS Firewall Manager. For information about how to setting up access for Amazon Simple Notification Service, see [Setting up access for Amazon Simple Notification Service](../../../sns/latest/dg/sns-setting-up.md "../../../sns/latest/dg/sns-setting-up.md").

For the policy listing and details, see the IAM console at [AWSFMAdminFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSFMAdminFullAccess$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSFMAdminFullAccess$serviceLevelSummary"). The rest of this section gives an overview of the policy settings.

**Permission statements**

This policy is grouped into statements based on the set of permissions.

- **AWS Firewall Manager policy resources** - Allows full administrative permissions to resources in AWS Firewall Manager, including all Firewall Manager policy types.
- **Write AWS WAF logs to Amazon Simple Storage Service** - Allows Firewall Manager to write and read AWS WAF logs in Amazon S3.
- **Create service-linked role** – Allows the administrator to create a service-linked role, which allows Firewall Manager to access resources in other services on your behalf. This permission allows creating the service-linked role only for use by Firewall Manager. For information about how Firewall Manager uses service-linked roles, see [Using service-linked roles for Firewall Manager](fms-using-service-linked-roles.md "fms-using-service-linked-roles.md").
- **AWS Organizations** – Allows administrators to use Firewall Manager for an organization in AWS Organizations. After enabling trusted access for Firewall Manager in AWS Organizations, members of the admin account can view findings across their organization. For information about using AWS Organizations with AWS Firewall Manager, see [Using AWS Organizations with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") in the _AWS Organizations User Guide_.

**Permission categories**

The following lists the types of permissions in the policy and the permissions that they
provide.

- `fms` – Work with AWS Firewall Manager resources.
- `waf` and `waf-regional` – Work with AWS WAF
  Classic policies.
- `elasticloadbalancing` – Associate AWS WAF web ACLsto Elastic
  Load Balancers.
- `firehose` – View information about AWS WAF logs.
- `organizations` – Work with AWS Organizations
  resources.
- `shield` – View the subscription state of AWS Shield
  policies.
- `route53resolver` – Work with Route 53 Private DNS for VPCs rule groups in an
  Route 53 Private DNS for VPCs policy.
- `wafv2` – Work with AWS WAFV2 policies.
- `network-firewall` – Work with AWS Network Firewall policies.
- `ec2` – View policy Availability Zones and Regions.
- `s3` – View information about AWS WAF logs.

## AWS managed policy: `FMSServiceRolePolicy`

This policy allows AWS Firewall Manager to manage AWS resources on your behalf in
Firewall Manager and in integrated services. This policy is attached to the service-linked role
`AWSServiceRoleForFMS`. For more information about the service-linked role, see
[Using service-linked roles for Firewall Manager](fms-using-service-linked-roles.md "fms-using-service-linked-roles.md").

For policy details, see the IAM console at [FMSServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary").

## AWS managed policy: AWSFMAdminReadOnlyAccess

Grants read-only access to all AWS Firewall Manager resources.

For the policy listing and details, see the IAM console at [AWSFMAdminReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSFMAdminReadOnlyAccess$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSFMAdminReadOnlyAccess$serviceLevelSummary"). The rest of this section gives an overview of the policy settings.

**Permission categories**

The following lists the types of permissions in the policy and the information that the permissions allow read only access to.

- `fms` – AWS Firewall Manager resources.
- `waf` and `waf-regional` – AWS WAF Classic policies.
- `firehose` – AWS WAF logs.
- `organizations` – AWS Organizations resources.
- `shield` – AWS Shield policies.
- `route53resolver` – Route 53 Private DNS for VPCs rule groups in an Route 53 Private DNS for VPCs policy.
- `wafv2` – Your AWS WAFV2 rule groups and AWS Managed Rules rule groups that are
  available in AWS WAFV2.
- `network-firewall` – AWS Network Firewall rule groups and rule group metadata.
- `ec2` – AWS Network Firewall policy Availability Zones and Regions .
- `s3` – AWS WAF logs.

## AWS managed policy: AWSFMMemberReadOnlyAccess

Grants read-only access to AWS Firewall Manager member resources. For the policy listing and details, see the IAM console at [AWSFMMemberReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSFMMemberReadOnlyAccess$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSFMMemberReadOnlyAccess$serviceLevelSummary").

## Firewall Manager updates to AWS managed

policies

View details about updates to AWS managed policies for Firewall Manager since this
service began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the Firewall Manager document history page at [Document history](doc-history.md "doc-history.md").

| Change                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Date       |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [FMSServiceRolePolicy](#security-iam-awsmanpol-FMSServiceRolePolicy "#security-iam-awsmanpol-FMSServiceRolePolicy") – Updated policy             | Added permissions to the Firewall Manager service policy.<br>Added the following permissions required for Amazon CloudFront:<br>• `cloudfront:AssociateDistributionWebACL` – Grants<br>permission to associate an AWS WAF web ACL with a CloudFront distribution<br>• `cloudfront:DisassociateDistributionWebACL` – Grants<br>permission to disassociate an AWS WAF web ACL with a CloudFront distribution                                                                                               | 2025-05-21 |
| [FMSServiceRolePolicy](#security-iam-awsmanpol-FMSServiceRolePolicy "#security-iam-awsmanpol-FMSServiceRolePolicy") – Updated policy             | Added permissions to the Firewall Manager service policy.<br>Added `BatchGetResourceConfig` permissions to get resource configuration statuses in batches. See the updated policy in the IAM console: [FMSServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary"). | 2025-02-10 |
| [FMSServiceRolePolicy](#security-iam-awsmanpol-FMSServiceRolePolicy "#security-iam-awsmanpol-FMSServiceRolePolicy") – Updated policy             | Added permissions to the Firewall Manager service role policy.<br>Added the ability to read Network Firewall TLS configuration information. See the updated policy in the IAM console: [FMSServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary").                | 2024-07-22 |
| [FMSServiceRolePolicy](#security-iam-awsmanpol-FMSServiceRolePolicy "#security-iam-awsmanpol-FMSServiceRolePolicy") – Updated policy             | Added permissions for managing network ACLs.<br>See the updated policy in the IAM console: [FMSServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary").                                                                                                            | 2024-04-22 |
| [FMSServiceRolePolicy](#security-iam-awsmanpol-FMSServiceRolePolicy "#security-iam-awsmanpol-FMSServiceRolePolicy") – Updated policy             | Added permissions that allow Firewall Manager to describe whether the specified AWS Config rules are compliant.<br>See the updated policy in the IAM console: [FMSServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary").                                         | 2023-04-21 |
| [FMSServiceRolePolicy](#security-iam-awsmanpol-FMSServiceRolePolicy "#security-iam-awsmanpol-FMSServiceRolePolicy") – Updated policy             | Added permissions that allow Firewall Manager to describe Amazon EC2 instance and network interface attributes.<br>See the updated policy in the IAM console: [FMSServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/FMSServiceRolePolicy$serviceLevelSummary").                                         | 2022-11-15 |
| [AWSFMAdminReadOnlyAccess](#security-iam-awsmanpol-AWSFMAdminReadOnlyAccess "#security-iam-awsmanpol-AWSFMAdminReadOnlyAccess") – Updated policy | Added permissions to support AWS WAFV2, Shield, Network Firewall, DNS Firewall, Amazon VPC security group, policies.<br>See the updated policy in the IAM console: [AWSFMAdminReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSFMAdminReadOnlyAccess$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSFMAdminReadOnlyAccess$serviceLevelSummary").                                                          | 2022-11-02 |
| [AWSFMAdminFullAccess](#security-iam-awsmanpol-AWSFMAdminFullAccess "#security-iam-awsmanpol-AWSFMAdminFullAccess") – Updated policy             | Added permissions to support AWS WAFV2, Shield, Network Firewall, DNS Firewall, Amazon VPC security group, policies. Removed Amazon SNS permissions.<br>See the updated policy in the IAM console: [AWSFMAdminFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSFMAdminFullAccess$serviceLevelSummary "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSFMAdminFullAccess$serviceLevelSummary").                                      | 2022-10-21 |
| `FMSServiceRolePolicy` – New permissions for AWS Firewall Manager third-party firewall policies                                                  | This change allows Firewall Manager to create and delete the Amazon EC2 VPC endpoints associated with a third-party firewall policy.                                                                                                                                                                                                                                                                                                                                                                     | 2022-03-30 |
| `FMSServiceRolePolicy` – New permissions for AWS Network Firewall policies                                                                       | Added new permissions to support deployment of firewalls for Network Firewall policies. The new permissions allow the retrieval of information about Availability Zones for accounts that are in scope of a policy.                                                                                                                                                                                                                                                                                      | 2022-02-16 |
| `FMSServiceRolePolicy` – New permissions for AWS Shield policies                                                                                 | Added new permissions to retrieve tags for AWS WAF regional and AWS WAF global resources. Added AWS WAF regional<br>permissions to retrieve web ACLs using a resource ARN. Added permissions to support Shield automatic application<br>layer DDoS mitigation.                                                                                                                                                                                                                                           | 2022-01-07 |
| `FMSServiceRolePolicy` – New permissions for AWS Shield policies                                                                                 | Added new permission to retrieve tags for Elastic Load Balancing resources.                                                                                                                                                                                                                                                                                                                                                                                                                              | 2021-11-18 |
| `FMSServiceRolePolicy` – New permissions for security group and AWS Network Firewall policies                                                    | Added new permissions to enable centralized logging for AWS Network Firewall policies.<br>Additionally, read-only Amazon EC2 permissions were added to support changes to the Config service<br>that impact how AWS Firewall Manager queries resources for security group policies.                                                                                                                                                                                                                      | 2021-09-29 |
| `FMSServiceRolePolicy` – ARN formats for AWS WAF resources                                                                                       | Updated the `FMSServiceRolePolicy` to standardize the ARN formats for<br>AWS WAF resources. The updated ARN formats are `arn:aws:waf:*:*:*` and<br>`arn:aws:waf-regional:*:*:*`.                                                                                                                                                                                                                                                                                                                         | 2021-08-12 |
| `FMSServiceRolePolicy` – Additional regions in China                                                                                             | AWS Firewall Manager has enabled `FMSServiceRolePolicy` for the BJS and ZHY regions in China.                                                                                                                                                                                                                                                                                                                                                                                                            | 2021-08-12 |
| `FMSServiceRolePolicy` – Update to the existing<br>policy                                                                                        | Added new permissions to allow AWS Firewall Manager to manage<br>Amazon Route 53 Resolver DNS Firewall.<br>This change allows Firewall Manager to configure<br>Amazon Route 53 Resolver DNS Firewall associations. This permits you to use<br>Firewall Manager to provide DNS Firewall protections for your VPCs throughout your<br>organization in AWS Organizations.                                                                                                                                   | 2021-03-17 |
| Firewall Manager started tracking changes                                                                                                        | Firewall Manager started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                  | 2021-03-02 |
