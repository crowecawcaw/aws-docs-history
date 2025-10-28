# Elective controls with preventive behavior

The following elective controls have preventive behavior.

The elective controls with preventive behavior are configurable. For more information about configurable controls, see [Controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

###### Topics

- [[AWS-GR_AUDIT_BUCKET_ENCRYPTION_ENABLED] Disallow modification of Amazon S3 bucket encryption](#aws-gr_audit_bucket_encryption_enabled "#aws-gr_audit_bucket_encryption_enabled")
- [[AWS-GR_AUDIT_BUCKET_LOGGING_ENABLED] Disallow modification of server access logging for an Amazon S3 bucket](#aws-gr_audit_bucket_logging_enabled "#aws-gr_audit_bucket_logging_enabled")
- [[AWS-GR_AUDIT_BUCKET_POLICY_CHANGES_PROHIBITED] Disallow policy changes to an Amazon S3 bucket](#aws-gr_audit_bucket_policy_changes_prohibited "#aws-gr_audit_bucket_policy_changes_prohibited")
- [[AWS-GR_AUDIT_BUCKET_RETENTION_POLICY] Set a retention policy for log archive](#aws-gr_audit_bucket_retention_policy "#aws-gr_audit_bucket_retention_policy")
- [[AWS-GR_DISALLOW_CROSS_REGION_NETWORKING] Disallow cross-region networking for Amazon EC2, Amazon CloudFront, and AWS Global Accelerator](#aws-gr_disallow_cross_region_networking "#aws-gr_disallow_cross_region_networking")
- [[AWS-GR_DISALLOW_VPC_INTERNET_ACCESS] Disallow internet access for an Amazon VPC instance managed by a customer](#aws-gr_disallow_vpc_internet_access "#aws-gr_disallow_vpc_internet_access")
- [[AWS-GR_DISALLOW_VPN_CONNECTIONS] Disallow Amazon Virtual Private Network (VPN) connections](#aws-gr_disallow_vpn_connections "#aws-gr_disallow_vpn_connections")
- [[AWS-GR_RESTRICT_ROOT_USER_ACCESS_KEYS] Disallow creation of access keys for the root user](#aws-gr_restrict_root_user_access_keys "#aws-gr_restrict_root_user_access_keys")
- [[AWS-GR_RESTRICT_ROOT_USER] Disallow actions as a root user](#aws-gr_restrict_root_user "#aws-gr_restrict_root_user")
- [[AWS-GR_RESTRICT_S3_CROSS_REGION_REPLICATION] Disallow cross region replication for Amazon S3 buckets](#aws-gr_restrict_s3_cross_region_replication "#aws-gr_restrict_s3_cross_region_replication")
- [[AWS-GR_RESTRICT_S3_DELETE_WITHOUT_MFA] Disallow delete actions on S3 buckets without MFA](#aws-gr_restrict_s3_delete_without_mfa "#aws-gr_restrict_s3_delete_without_mfa")
- [[CT.CLOUDFORMATION.PR.1] Disallow management of resource types, modules, and hooks within the AWS CloudFormation registry](#disallow-cfn-extensions "#disallow-cfn-extensions")

## [AWS-GR\_AUDIT\_BUCKET\_ENCRYPTION\_ENABLED] Disallow modification of Amazon S3 bucket encryption

This control disallows modification of Amazon S3 bucket encryption configuration.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Encrypt data at rest
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control groups:** digital-sovereignty
- **Resource types:** `AWS::S3::Bucket`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRAUDITBUCKETENCRYPTIONENABLED",
            "Effect": "Deny",
            "Action": "s3:PutEncryptionConfiguration",
            "Resource": "*",
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalARN": [
                        {{ExemptedPrincipalArns}}
                        "arn:*:iam::*:role/AWSControlTowerExecution"
                    ]
                }
            }
        }
    ]
}


```

## [AWS-GR\_AUDIT\_BUCKET\_LOGGING\_ENABLED] Disallow modification of server access logging for an Amazon S3 bucket

This control disallows modification of server access logging for an Amazon S3 bucket.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Establish logging and monitoring
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::S3::Bucket`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRAUDITBUCKETLOGGINGENABLED",
            "Effect": "Deny",
            "Action": "s3:PutBucketLogging",
            "Resource": "*",
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalARN": [
                        {{ExemptedPrincipalArns}}
                        "arn:*:iam::*:role/AWSControlTowerExecution"
                    ]
                }
            }
        }
    ]
}


```

## [AWS-GR\_AUDIT\_BUCKET\_POLICY\_CHANGES\_PROHIBITED] Disallow policy changes to an Amazon S3 bucket

This control disallows modification of an Amazon S3 bucket policy.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Protect data integrity
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::S3::Bucket`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRAUDITBUCKETPOLICYCHANGESPROHIBITED",
            "Effect": "Deny",
            "Action": "s3:PutBucketPolicy",
            "Resource": "*",
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalARN": [
                        {{ExemptedPrincipalArns}}
                        "arn:*:iam::*:role/AWSControlTowerExecution"
                    ]
                }
            }
        }
    ]
}


```

## [AWS-GR\_AUDIT\_BUCKET\_RETENTION\_POLICY] Set a retention policy for log archive

Limit data retention in the log archive using a retention policy that defaults to 365 days.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Improve resiliency
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::S3::Bucket`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRAUDITBUCKETRETENTIONPOLICY",
            "Effect": "Deny",
            "Action": "s3:PutLifecycleConfiguration",
            "Resource": "*",
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalARN": [
                        {{ExemptedPrincipalArns}}
                        "arn:*:iam::*:role/AWSControlTowerExecution"
                    ]
                }
            }
        }
    ]
}


```

## [AWS-GR\_DISALLOW\_CROSS\_REGION\_NETWORKING] Disallow cross-region networking for Amazon EC2, Amazon CloudFront, and AWS Global Accelerator

Disallow cross-region networking connections from Amazon EC2, Amazon CloudFront, and AWS Global Accelerator services.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon CloudFront, Amazon EC2, AWS Global Accelerator

###### Control metadata

- **Control objective:** Limit network access
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::CloudFront::Distribution`, `AWS::EC2::VPCPeeringConnection`, `AWS::EC2::TransitGatewayPeeringAttachment`, `AWS::GlobalAccelerator::Accelerator`, `AWS::GlobalAccelerator::EndpointGroup`, `AWS::GlobalAccelerator::Listener`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRDISALLOWCROSSREGIONNETWORKING",
            "Effect": "Deny",
            "Action": [
                "cloudfront:CreateDistribution",
                "cloudfront:UpdateDistribution",
                "ec2:AcceptTransitGatewayPeeringAttachment",
                "ec2:AcceptVpcPeeringConnection",
                "ec2:CreateTransitGatewayPeeringAttachment",
                "ec2:CreateVpcPeeringConnection",
                "globalaccelerator:Create*",
                "globalaccelerator:Update*"
            ],
            "Resource": "*"{% if ExemptedPrincipalArns %},
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }
            }{% endif %}
        }
    ]
}


```

## [AWS-GR\_DISALLOW\_VPC\_INTERNET\_ACCESS] Disallow internet access for an Amazon VPC instance managed by a customer

Disallow internet access for an Amazon Virtual Private Cloud (VPC) instance managed by a customer, rather than by an AWS service.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon EC2

###### Control metadata

- **Control objective:** Limit network access
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control groups:** digital-sovereignty
- **Resource types:** `AWS::EC2::InternetGateway`, `AWS::EC2::EgressOnlyInternetGateway`, `AWS::EC2::VPC`, `AWS::EC2::Subnet`, `AWS::EC2::CarrierGateway`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRDISALLOWVPCINTERNETACCESS",
            "Effect": "Deny",
            "Action": [
                "ec2:AttachEgressOnlyInternetGateway",
                "ec2:AttachInternetGateway",
                "ec2:CreateCarrierGateway",
                "ec2:CreateDefaultSubnet",
                "ec2:CreateDefaultVpc",
                "ec2:CreateEgressOnlyInternetGateway",
                "ec2:CreateInternetGateway"
            ],
            "Resource": "*",
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalARN": [
                        {{ExemptedPrincipalArns}}
                        "arn:*:iam::*:role/AWSControlTowerExecution"
                    ]
                }
            }
        }
    ]
}


```

## [AWS-GR\_DISALLOW\_VPN\_CONNECTIONS] Disallow Amazon Virtual Private Network (VPN) connections

Disallows Virtual Private Network (VPN) connections (Site-to-Site VPN and Client VPN) to an Amazon Virtual Private Cloud (VPC).

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon EC2

###### Control metadata

- **Control objective:** Limit network access
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::EC2::VPNGateway`, `AWS::EC2::CustomerGateway`, `AWS::EC2::VPNConnection`, `AWS::EC2::ClientVpnEndpoint`, `AWS::EC2::ClientVpnTargetNetworkAssociation`, `AWS::EC2::ClientVpnAuthorizationRule`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRDISALLOWVPNCONNECTIONS",
            "Effect": "Deny",
            "Action": [
                "ec2:AssociateClientVpnTargetNetwork",
                "ec2:AttachVPNGateway",
                "ec2:AuthorizeClientVpnIngress",
                "ec2:CreateClientVpnEndpoint",
                "ec2:CreateCustomerGateway",
                "ec2:CreateVPNGateway",
                "ec2:CreateVpnConnection",
                "ec2:ModifyClientVpnEndpoint",
                "ec2:ModifyVpnConnection"
            ],
            "Resource": "*"{% if ExemptedPrincipalArns %},
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }
            }{% endif %}
        }
    ]
}


```

## [AWS-GR\_RESTRICT\_ROOT\_USER\_ACCESS\_KEYS] Disallow creation of access keys for the root user

Secure your AWS accounts by disallowing creation of access keys for the root user, which will allow unrestricted access to all resources in the account. We recommend that you instead create access keys for an AWS Identity and Access Management (IAM) user for everyday interaction with your AWS account.

This is a preventive control with strongly-recommended guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** AWS Identity and Access Management (IAM)

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::::Account`, `AWS::IAM::AccessKey`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRRESTRICTROOTUSERACCESSKEYS",
            "Effect": "Deny",
            "Action": "iam:CreateAccessKey",
            "Resource": "*",
            "Condition": {
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:*:iam::*:root"
                    ]
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}


```

## [AWS-GR\_RESTRICT\_ROOT\_USER] Disallow actions as a root user

Secure your AWS accounts by disallowing account access with root user credentials, which are credentials of the account owner and allow unrestricted access to all resources in the account. We recommend that you instead create AWS Identity and Access Management (IAM) users for everyday interaction with your AWS account.

This is a preventive control with strongly-recommended guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** AWS Identity and Access Management (IAM)

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::::Account`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRRESTRICTROOTUSER",
            "Effect": "Deny",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "aws:PrincipalArn": [
                        "arn:*:iam::*:root"
                    ]
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}


```

## [AWS-GR\_RESTRICT\_S3\_CROSS\_REGION\_REPLICATION] Disallow cross region replication for Amazon S3 buckets

Contain the location of your Amazon S3 data to a single region by disabling any automatic, asynchronous copying of objects across buckets to other AWS Regions.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Improve resiliency
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::S3::Bucket`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRRESTRICTS3CROSSREGIONREPLICATION",
            "Effect": "Deny",
            "Action": "s3:PutReplicationConfiguration",
            "Resource": "*"{% if ExemptedPrincipalArns %},
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }
            }{% endif %}
        }
    ]
}


```

## [AWS-GR\_RESTRICT\_S3\_DELETE\_WITHOUT\_MFA] Disallow delete actions on S3 buckets without MFA

Protect your S3 buckets by requiring multi-factor authentication (MFA) for delete actions. MFA adds an extra authentication code on top of a user name and password.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Protect data integrity
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::S3::Bucket`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GRRESTRICTS3DELETEWITHOUTMFA",
            "Effect": "Deny",
            "Action": [
                "s3:DeleteObject",
                "s3:DeleteBucket"
            ],
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:MultiFactorAuthPresent": [
                        "false"
                    ]
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}


```

## [CT.CLOUDFORMATION.PR.1] Disallow management of resource types, modules, and hooks within the AWS CloudFormation registry

This elective control disallows management of the following extension types in the AWS CloudFormation registry: resource types, modules, and hooks. For more information about AWS CloudFormation extensions, see [Using the AWS CloudFormationregistry](../../../AWSCloudFormation/latest/UserGuide/registry.md "../../../AWSCloudFormation/latest/UserGuide/registry.md").

A typical use case for this control is a situation in which you do not wish to allow your organization to register AWS CloudFormation types. It prevents registration of types, and it prevents disabling existing AWS CloudFormation hooks.

- **Control objective:** Protect configurations
- **Implementation** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control guidance:** Elective
- **Control owner:** AWS Control Tower
- **Control ID:** CT.CLOUDFORMATION.PR.1
- **Severity:** Critical
- **AWS Service:** AWS CloudFormation
- **Resource types:** `AWS::CloudFormation::HookDefaultVersion,
AWS::CloudFormation::HookTypeConfig,
AWS::CloudFormation::HookVersion,
AWS::CloudFormation::ModuleDefaultVersion,
AWS::CloudFormation::ModuleVersion,
AWS::CloudFormation::ResourceDefaultVersion,
AWS::CloudFormation::ResourceVersion`

The following example shows the SCP artifact for this control.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRDISALLOWMODIFICATIONCFNREGISTRY",
 "Effect": "Deny",
 "Action": [
 "cloudformation:RegisterType",
 "cloudformation:DeregisterType",
 "cloudformation:SetTypeConfiguration",
 "cloudformation:SetTypeDefaultVersion",
 "cloudformation:PublishType"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalARN": "arn:aws:iam::*:role/AWSControlTowerExecution"
 }
 }
 }
 ]
}`

```
