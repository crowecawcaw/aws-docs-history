

# Elective controls with preventive behavior
<a name="elective-preventive-controls"></a>

The following elective controls have preventive behavior.

The elective controls with preventive behavior are configurable. For more information about configurable controls, see [Controls with parameters](control-parameter-concepts.md).

**Topics**
+ [[AWS-GR\_AUDIT\_BUCKET\_ENCRYPTION\_ENABLED] Disallow modification of Amazon S3 bucket encryption](#aws-gr_audit_bucket_encryption_enabled)
+ [[AWS-GR\_AUDIT\_BUCKET\_LOGGING\_ENABLED] Disallow modification of server access logging for an Amazon S3 bucket](#aws-gr_audit_bucket_logging_enabled)
+ [[AWS-GR\_AUDIT\_BUCKET\_POLICY\_CHANGES\_PROHIBITED] Disallow policy changes to an Amazon S3 bucket](#aws-gr_audit_bucket_policy_changes_prohibited)
+ [[AWS-GR\_AUDIT\_BUCKET\_RETENTION\_POLICY] Set a retention policy for log archive](#aws-gr_audit_bucket_retention_policy)
+ [[AWS-GR\_DISALLOW\_CROSS\_REGION\_NETWORKING] Disallow cross-region networking for Amazon EC2, Amazon CloudFront, and AWS Global Accelerator](#aws-gr_disallow_cross_region_networking)
+ [[AWS-GR\_DISALLOW\_VPC\_INTERNET\_ACCESS] Disallow internet access for an Amazon VPC instance managed by a customer](#aws-gr_disallow_vpc_internet_access)
+ [[AWS-GR\_DISALLOW\_VPN\_CONNECTIONS] Disallow Amazon Virtual Private Network (VPN) connections](#aws-gr_disallow_vpn_connections)
+ [[AWS-GR\_RESTRICT\_S3\_CROSS\_REGION\_REPLICATION] Disallow cross region replication for Amazon S3 buckets](#aws-gr_restrict_s3_cross_region_replication)
+ [[AWS-GR\_RESTRICT\_S3\_DELETE\_WITHOUT\_MFA] Disallow delete actions on S3 buckets without MFA](#aws-gr_restrict_s3_delete_without_mfa)
+ [[CT.CLOUDFORMATION.PR.1] Disallow management of resource types, modules, and hooks within the CloudFormation registry](#disallow-cfn-extensions)

## [AWS-GR\_AUDIT\_BUCKET\_ENCRYPTION\_ENABLED] Disallow modification of Amazon S3 bucket encryption
<a name="aws-gr_audit_bucket_encryption_enabled"></a>

This control disallows modification of Amazon S3 bucket encryption configuration.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon S3

**Control metadata**
+ **Control objective: **Encrypt data at rest
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Control groups: **digital-sovereignty
+ **Resource types: **`AWS::S3::Bucket`

**Usage considerations**  
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

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
<a name="aws-gr_audit_bucket_logging_enabled"></a>

This control disallows modification of server access logging for an Amazon S3 bucket.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon S3

**Control metadata**
+ **Control objective: **Establish logging and monitoring
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Resource types: **`AWS::S3::Bucket`

**Usage considerations**  
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

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
<a name="aws-gr_audit_bucket_policy_changes_prohibited"></a>

This control disallows modification of an Amazon S3 bucket policy.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon S3

**Control metadata**
+ **Control objective: **Protect data integrity
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Resource types: **`AWS::S3::Bucket`

**Usage considerations**  
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

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
<a name="aws-gr_audit_bucket_retention_policy"></a>

Limit data retention in the log archive using a retention policy that defaults to 365 days.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon S3

**Control metadata**
+ **Control objective: **Improve resiliency
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Resource types: **`AWS::S3::Bucket`

**Usage considerations**  
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

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
<a name="aws-gr_disallow_cross_region_networking"></a>

Disallow cross-region networking connections from Amazon EC2, Amazon CloudFront, and AWS Global Accelerator services.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon CloudFront, Amazon EC2, AWS Global Accelerator

**Control metadata**
+ **Control objective: **Limit network access
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Resource types: **`AWS::CloudFront::Distribution`, `AWS::EC2::VPCPeeringConnection`, `AWS::EC2::TransitGatewayPeeringAttachment`, `AWS::GlobalAccelerator::Accelerator`, `AWS::GlobalAccelerator::EndpointGroup`, `AWS::GlobalAccelerator::Listener`

**Usage considerations**  
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

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
<a name="aws-gr_disallow_vpc_internet_access"></a>

Disallow internet access for an Amazon Virtual Private Cloud (VPC) instance managed by a customer, rather than by an AWS service.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon EC2

**Control metadata**
+ **Control objective: **Limit network access
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Control groups: **digital-sovereignty
+ **Resource types: **`AWS::EC2::InternetGateway`, `AWS::EC2::EgressOnlyInternetGateway`, `AWS::EC2::VPC`, `AWS::EC2::Subnet`, `AWS::EC2::CarrierGateway`

**Usage considerations**  
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

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
<a name="aws-gr_disallow_vpn_connections"></a>

Disallows Virtual Private Network (VPN) connections (Site-to-Site VPN and Client VPN) to an Amazon Virtual Private Cloud (VPC).

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon EC2

**Control metadata**
+ **Control objective: **Limit network access
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Resource types: **`AWS::EC2::VPNGateway`, `AWS::EC2::CustomerGateway`, `AWS::EC2::VPNConnection`, `AWS::EC2::ClientVpnEndpoint`, `AWS::EC2::ClientVpnTargetNetworkAssociation`, `AWS::EC2::ClientVpnAuthorizationRule`

**Usage considerations**  
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

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

## [AWS-GR\_RESTRICT\_S3\_CROSS\_REGION\_REPLICATION] Disallow cross region replication for Amazon S3 buckets
<a name="aws-gr_restrict_s3_cross_region_replication"></a>

Contain the location of your Amazon S3 data to a single region by disabling any automatic, asynchronous copying of objects across buckets to other AWS Regions.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon S3

**Control metadata**
+ **Control objective: **Improve resiliency
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Resource types: **`AWS::S3::Bucket`

**Usage considerations**  
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

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
<a name="aws-gr_restrict_s3_delete_without_mfa"></a>

Protect your S3 buckets by requiring multi-factor authentication (MFA) for delete actions. MFA adds an extra authentication code on top of a user name and password.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon S3

**Control metadata**
+ **Control objective: **Protect data integrity
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Resource types: **`AWS::S3::Bucket`

**Usage considerations**  
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

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

## [CT.CLOUDFORMATION.PR.1] Disallow management of resource types, modules, and hooks within the CloudFormation registry
<a name="disallow-cfn-extensions"></a>

This elective control disallows management of the following extension types in the CloudFormation registry: resource types, modules, and hooks. For more information about CloudFormation extensions, see [Using the CloudFormationregistry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html).

A typical use case for this control is a situation in which you do not wish to allow your organization to register CloudFormation types. It prevents registration of types, and it prevents disabling existing CloudFormation hooks.
+ **Control objective:** Protect configurations
+ **Implementation** Service control policy (SCP)
+ **Control behavior:** Preventive
+ **Control guidance:** Elective
+ **Control owner:** AWS Control Tower
+ **Control ID:** CT.CLOUDFORMATION.PR.1
+ **Severity:** Critical
+ **AWS Service:** CloudFormation
+ **Resource types: ** `AWS::CloudFormation::HookDefaultVersion, AWS::CloudFormation::HookTypeConfig, AWS::CloudFormation::HookVersion, AWS::CloudFormation::ModuleDefaultVersion, AWS::CloudFormation::ModuleVersion, AWS::CloudFormation::ResourceDefaultVersion, AWS::CloudFormation::ResourceVersion `

 The following example shows the SCP artifact for this control.

------
#### [ JSON ]

****  

```
{
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
}
```

------