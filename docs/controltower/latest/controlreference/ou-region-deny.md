# Region deny control applied to the OU

_This control is commonly referred to as the OU Region deny
control, or the configurable Region deny control._

This control disallows access to unlisted operations in global and regional AWS services, outside of the specified Regions for an organizational unit (OU). You can apply this control to any subset of the Regions that are governed by your AWS Control Tower landing zone.

You may wish to review the information at [Configure the Region deny control](../userguide/region-deny.md "../userguide/region-deny.md") before you enable this control.

###### Warning

If you enforce this control, the configurations for the OU can conflict with the landing zone version of this control. For more information, see the section called "Policy evaluation of SCP controls" in this chapter, and [SCP evaluation](../../../organizations/latest/userguide/orgs_manage_policies_scps_evaluation.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_evaluation.md") in the AWS Organizations documentation.

**CT.MULTISERVICE.PV.1**: Deny access to
AWS based on the requested AWS Region for an organizational unit

**Service:** Multiple AWS services

- **Control objective:** Protect configurations
- **Implementation:** Service control policy
  (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Groups:** Digital sovereignty

###### Limitations

The OU Region deny control is subject to limitations of the [`aws:RequestedRegion`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion") global condition key and [Service Control Policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in general.

**Enable this control from the console**

In the AWS Control Tower console, you can view the OUs on which this control is enabled, if any, by navigating to the **Control details** page for this control.

###### To enable this control from the **Control details** page

1. Select **Enable control** in the upper right
2. Select the target OU, then select **Next** to continue.
3. Select the Regions you wish to activate. You must select at least one Region.
4. You can add **NotAction** elements, IAM principals, and tags.
5. You'll be able to see a summary of your selected values before you enable the control.
6. Select **Enable control** at the lower right.

## CT.MULTISERVICE.PV.1: Deny access to AWS based on the requested

AWS Region for an organizational unit

The OU Region deny control, **CT.MULTISERVICE.PV.1**, is configurable. You can select specific OUs to which
it applies, rather than applying it to your entire AWS Control Tower landing zone. This control
accepts one or more parameters, such as **AllowedRegions**,
**ExemptedPrincipalARNs**, and **ExemptedActions**, which describe operations that are allowed for accounts
that are part of this OU.

- **AllowedRegions**: Specifies the Regions selected, in which the OU is
  allowed to operate. This parameter is **mandatory**.
- **ExemptedPrincipalARNs**: Specifies the IAM principals that are exempt
  from this control, so that they are allowed to operate certain AWS services
  globally.
- **ExemptedActions**: Specifies actions that are exempt from this control, so that the actions are allowed.

Interactions between the separate Region deny controls for the landing zone and the OU can
be complicated to predict. They are predictable with the logic by which SCPs are evaluated
by AWS.

**Policy evaluation of SCP controls**

The policy evaluation process involves checking all applicable policies, starting from the
most permissive and gradually moving towards the most restrictive. Any SCP applied at the Root
level will impact all accounts and OUs, unless it is overridden by a more specific policy.

**Evaluation Logic**: When a request is made to perform an action (for
example, launching an Amazon EC2 instance), AWS evaluates policies to determine whether the
action is allowed or denied. The evaluation logic follows these rules:

- _Explicit Deny Overrides All:_ If any policy explicitly denies
  the requested action, that denial takes precedence over all other policies.
- _Explicit Allow Overrides Implicit Deny:_ If a policy
  explicitly allows the action and no higher-level policy explicitly denies it, the
  action is allowed.
- _Inherited Allow and No Explicit Deny:_ If there is no explicit
  allow or deny at the requested level, AWS looks at higher-level policies. If there
  is an inherited allow and no explicit deny, the action is allowed.
- _Explicit Deny at a Higher Level:_ If there's an explicit deny
  in a higher-level policy, but no explicit allow or deny at the requested level, the
  action is denied.

For more information about the evaluation logic, see [SCP evaluation](../../../organizations/latest/userguide/orgs_manage_policies_scps_evaluation.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_evaluation.md") in the AWS Organizations documentation.

###### Note

With this control, you can allow any AWS Region at the OU level, even if your
landing zone does not govern that Region, by design. We recommend that you use caution
when allowing Regions that your AWS Control Tower landing zone does not govern.

### CLI Example

This example shows how to enable this control, with parameters, from the CLI.

```

aws controltower enable-control \
    --target-identifier arn:aws:organizations::01234567890:ou/o-EXAMPLE/ou-zzxx-zzx0zzz2 \
    --control-identifier arn:aws:controltower:us-east-1::control/EXAMPLE_NAME \
    --parameters '[{"key":"AllowedRegions","value":["us-east-1","us-west-2"]},{"key":"ExemptedPrincipalArns","value":["arn:aws:iam::*:role/ReadOnly","arn:aws:sts::*:assumed-role/ReadOnly/*"]},{"key":"ExemptedActions","value":["logs:DescribeLogGroups","logs:StartQuery","logs:GetQueryResults"]}]'
```

**Validating parameters**

When you enter a parameter into the OU Region deny control, AWS Control Tower validates the
parameter's syntax and checks it against JSON datatypes. AWS Control Tower does not make semantic
validations for domain-specific correctness. This is the same approach that is followed by
AWS Organizations.

Parameters for this control are entered by means of a JSON schema.

Here is the SCP template of an example JSON schema for the OU-level Region deny control.
In the AWS Control Tower console, you can view it on the **Artifacts** tab of the
**Control details** page.

This short example schema shows that the **AllowedRegions**, **ExemptedActions** and
**ExemptedPrincipalArns** parameters accept a list of strings. Also, you can add descriptions to the schema, or restrict allowed values to be a
subset of pre-defined values, using enumerated types (`enums`).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTMULTISERVICEPV1",
            "Effect": "Deny",
            "NotAction": [
                {{ExemptedActions}}
                ...
                "s3:CreateMultiRegionAccessPoint",
                "s3:DeleteMultiRegionAccessPoint",
                "s3:DescribeMultiRegionAccessPointOperation",
                "s3:GetAccountPublicAccessBlock",
                "s3:GetBucketLocation"
                ...
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:RequestedRegion": {{AllowedRegions}}
                },
                "ArnNotLike": {
                    "aws:PrincipalARN": [
                        "arn:aws:iam::*:role/AWSControlTowerExecution",
                        {{ExemptedPrincipalARNs}}
                    ]
                }
            }
        }
    ]
}
```

The following example shows a full SCP artifact for the control. It shows the actions and principals that are exempted by default when you apply this control to an OU. Remember that **AllowedRegions** is a mandatory parameter for this control. You can view the most recent version of this SCP in the AWS Control Tower console.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTMULTISERVICEPV1",
            "Effect": "Deny",
            "NotAction": [
                {{ExemptedActions}}
                "a4b:*",
                "access-analyzer:*",
                "account:*",
                "acm:*",
                "activate:*",
                "artifact:*",
                "aws-marketplace-management:*",
                "aws-marketplace:*",
                "aws-portal:*",
                "billing:*",
                "billingconductor:*",
                "budgets:*",
                "ce:*",
                "chatbot:*",
                "chime:*",
                "cloudfront:*",
                "cloudtrail:LookupEvents",
                "compute-optimizer:*",
                "config:*",
                "consoleapp:*",
                "consolidatedbilling:*",
                "cur:*",
                "datapipeline:GetAccountLimits",
                "devicefarm:*",
                "directconnect:*",
                "ec2:DescribeRegions",
                "ec2:DescribeTransitGateways",
                "ec2:DescribeVpnGateways",
                "ecr-public:*",
                "fms:*",
                "freetier:*",
                "globalaccelerator:*",
                "health:*",
                "iam:*",
                "importexport:*",
                "invoicing:*",
                "iq:*",
                "kms:*",
                "license-manager:ListReceivedLicenses",
                "lightsail:Get*",
                "mobileanalytics:*",
                "networkmanager:*",
                "notifications-contacts:*",
                "notifications:*",
                "organizations:*",
                "payments:*",
                "pricing:*",
                "quicksight:DescribeAccountSubscription",
                "resource-explorer-2:*",
                "route53-recovery-cluster:*",
                "route53-recovery-control-config:*",
                "route53-recovery-readiness:*",
                "route53:*",
                "route53domains:*",
                "s3:CreateMultiRegionAccessPoint",
                "s3:DeleteMultiRegionAccessPoint",
                "s3:DescribeMultiRegionAccessPointOperation",
                "s3:GetAccountPublicAccessBlock",
                "s3:GetBucketLocation",
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketPublicAccessBlock",
                "s3:GetMultiRegionAccessPoint",
                "s3:GetMultiRegionAccessPointPolicy",
                "s3:GetMultiRegionAccessPointPolicyStatus",
                "s3:GetStorageLensConfiguration",
                "s3:GetStorageLensDashboard",
                "s3:ListAllMyBuckets",
                "s3:ListMultiRegionAccessPoints",
                "s3:ListStorageLensConfigurations",
                "s3:PutAccountPublicAccessBlock",
                "s3:PutMultiRegionAccessPointPolicy",
                "savingsplans:*",
                "shield:*",
                "sso:*",
                "sts:*",
                "support:*",
                "supportapp:*",
                "supportplans:*",
                "sustainability:*",
                "tag:GetResources",
                "tax:*",
                "trustedadvisor:*",
                "vendor-insights:ListEntitledSecurityProfiles",
                "waf-regional:*",
                "waf:*",
                "wafv2:*"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:RequestedRegion": {{AllowedRegions}}
                },
                "ArnNotLike": {
                    "aws:PrincipalARN": [
                        {{ExemptedPrincipalArns}}
                        "arn:*:iam::*:role/AWSControlTowerExecution",
                        "arn:*:iam::*:role/aws-controltower-ConfigRecorderRole",
                        "arn:*:iam::*:role/aws-controltower-ForwardSnsNotificationRole",
                        "arn:*:iam::*:role/AWSControlTower_VPCFlowLogsRole"
                    ]
                }
            }
        }
    ]
}


```
