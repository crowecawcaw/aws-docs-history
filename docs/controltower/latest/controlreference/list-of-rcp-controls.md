# AWS Control Tower RCP controls

AWS Control Tower offers multiple RCP-based controls that each focus on a single type of
resource associated with a specific service, such as Amazon S3 buckets.

###### Topics

- [[CT.KMS.PV.7] Require that the organization's AWS Key Management Service resources are accessible only by IAM principals that belong to the organization, or by an AWS service](#ct-kms-pv-7 "#ct-kms-pv-7")
- [[CT.S3.PV.2] Require all requests to Amazon S3 resources use authentication based on an Authorization header](#ct-s3-pv-2 "#ct-s3-pv-2")
- [[CT.S3.PV.3] Require requests to Amazon S3 resources to use a minimum TLS version of 1.3](#ct-s3-pv-3 "#ct-s3-pv-3")
- [[CT.S3.PV.4] Require that the organization's Amazon S3 resources are accessible only by IAM principals that belong to the organization or by an AWS service](#ct-s3-pv-4 "#ct-s3-pv-4")
- [[CT.S3.PV.5] Require encryption of data in transit for calls to Amazon S3 resources](#ct-s3-pv-5 "#ct-s3-pv-5")
- [[CT.S3.PV.6] Require all object uploads to Amazon S3 buckets to use server-side encryption with an AWS KMS key (SSE-KMS)](#ct-s3-pv-6 "#ct-s3-pv-6")
- [[CT.SECRETSMANAGER.PV.1] Require that the organization's AWS Secrets Manager resources are accessible only by IAM principals that belong to the organization or by an AWS service](#ct-secretsmanager-pv-1 "#ct-secretsmanager-pv-1")
- [[CT.SQS.PV.1] Require that the organization's Amazon SQS resources are accessible only by IAM principals that belong to the organization, or by an AWS service](#ct-sqs-pv-1 "#ct-sqs-pv-1")
- [[CT.STS.PV.1] Require that the organization's AWS Security Token Service resources are accessible only by IAM principals that belong to the organization, or by an AWS service](#ct-sts-pv-1 "#ct-sts-pv-1")

## [CT.KMS.PV.7] Require that the organization's AWS Key Management Service resources are accessible only by IAM principals that belong to the organization, or by an AWS service

This control disallows AWS Key Management Service API operations for your organization's AWS Key Management Service (KMS) resources by an AWS IAM principal, when the principal is outside of the organization and is not an AWS service principal.

This is a preventive control with elective guidance, based on resource control policies (RCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or through the AWS Control Tower APIs.

**AWS service:** AWS Key Management Service (AWS KMS)

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Resource control policy (RCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `Multiple`

###### Usage considerations

- When you enable this control, AWS Control Tower populates the template RCP with the ID of the organization that your AWS Control Tower landing zone governs.
- Choose the Organizational Unit (OU) to which this control will apply. If AWS Key Management Service resources in that OU must be accessible by a trusted party besides your organization or an AWS service (for instance, another organization or specific IAM role), this control causes requests by that trusted party to be denied. Consider which principals need access to the AWS Key Management Service resources in your OU before you enable this control on that OU.
- This control does not provide protection for cross-service confused deputy scenarios. Consider enabling the related control for AWS Key Management Service, which applies an RCP to govern direct AWS service access to the organization's AWS Key Management Service resources. For more information about cross-service confused deputy prevention, see [Cross-service confused deputy prevention](../../../IAM/latest/UserGuide/confused-deputy.md#cross-service-confused-deputy-prevention "../../../IAM/latest/UserGuide/confused-deputy.md#cross-service-confused-deputy-prevention") in the _AWS Identity and Access Management User Guide_.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: ExemptedPrincipalArns. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following resource control policy (RCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTKMSPV7",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "kms:*",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:PrincipalIsAWSService": "false"
                },
                "StringNotEqualsIfExists": {
                    "aws:PrincipalOrgID": {{OrganizationIds}}
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}

```

## [CT.S3.PV.2] Require all requests to Amazon S3 resources use authentication based on an Authorization header

This control disallows requests to your Amazon S3 resources that use an authentication method other than HTTP `Authorization` header-based authentication (presigned URL or HTTP POST requests).

This is a preventive control with elective guidance, based on resource control policies (RCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Limit network access
- **Implementation:** Resource control policy (RCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `Multiple`

###### Usage considerations

- This control disallows authenticated operations on your S3 resources where authentication information has been provided in a location other than the HTTP `Authorization` header, which means that the `s3:authType` field in the request context is set to a value other than `REST-HEADER`. This approach prevents the use of S3-presigned URL or HTTP POST requests. For more information on available authentication methods for Amazon S3, see [Authenticating Requests (AWS Signature Version 4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md") in the _Amazon S3 User Guide_.
- If you need to use presigned URL or HTTP POST requests with your S3 resources, do not enable this control.
- This control does not help you manage public access to Amazon S3 resources. AWS Control Tower recommends using the Amazon S3 Block Public Access field to help manage public access to your Amazon S3 resources. For more information on **S3 Block Public Access**, see [Blocking public access to your Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") in the _Amazon S3 User Guide_.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following resource control policy (RCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTS3PV2",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "s3:authType": "REST-HEADER"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}

```

## [CT.S3.PV.3] Require requests to Amazon S3 resources to use a minimum TLS version of 1.3

This control requires connections to Amazon S3 resources in your organization use TLS version 1.3 or higher.

This is a preventive control with elective guidance, based on resource control policies (RCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Encrypt data in transit
- **Implementation:** Resource control policy (RCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `Multiple`

###### Usage considerations

- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following resource control policy (RCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTS3PV3",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": "*",
            "Condition": {
                "NumericLessThan": {
                    "s3:TlsVersion": "1.3"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}

```

## [CT.S3.PV.4] Require that the organization's Amazon S3 resources are accessible only by IAM principals that belong to the organization or by an AWS service

This control disallows Amazon S3 API operations for your organization's Amazon S3 resources by an AWS IAM principal, when the principal is outside of the organization and is not an AWS service principal.

This is a preventive control with elective guidance, based on resource control policies (RCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Resource control policy (RCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `Multiple`

###### Usage considerations

- When you enable this control, AWS Control Tower populates the template RCP with the ID of the organization that your AWS Control Tower landing zone governs.
- Choose the Organizational Unit (OU) to which this control will apply. If Amazon S3 resources in that OU must be accessible by a trusted party besides your organization or an AWS service (for instance, another organization or specific IAM role), this control causes requests by that trusted party to be denied. Consider which principals need access to the Amazon S3 resources in your OU before you enable this control on that OU.
- This control does not provide protection for cross-service confused deputy scenarios. Consider enabling the related control for Amazon S3, which applies an RCP to govern direct AWS service access to the organization's Amazon S3 resources. For more information about cross-service confused deputy prevention, see [Cross-service confused deputy prevention](../../../IAM/latest/UserGuide/confused-deputy.md#cross-service-confused-deputy-prevention "../../../IAM/latest/UserGuide/confused-deputy.md#cross-service-confused-deputy-prevention") in the _AWS Identity and Access Management User Guide_.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following resource control policy (RCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTS3PV4",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": "*",
            "Condition": {
               "BoolIfExists": {
                    "aws:PrincipalIsAWSService": "false"
                },
                "StringNotEqualsIfExists": {
                    "aws:PrincipalOrgID": {{OrganizationIds}}
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}



```

## [CT.S3.PV.5] Require encryption of data in transit for calls to Amazon S3 resources

This control prevents unencrypted connections to Amazon S3 resources in your organization, by using the `aws:SecureTransport` condition.

This is a preventive control with elective guidance, based on resource control policies (RCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Encrypt data in transit
- **Implementation:** Resource control policy (RCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `Multiple`

###### Usage considerations

- If you currently make HTTP connections to Amazon S3 endpoints, be sure that you migrate to HTTPS connections before you enable this control.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following resource control policy (RCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTS3PV5",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": "*",
            "Condition": {
                "Bool": {
                  "aws:SecureTransport": "false"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}


```

## [CT.S3.PV.6] Require all object uploads to Amazon S3 buckets to use server-side encryption with an AWS KMS key (SSE-KMS)

This control prevents object uploads to your Amazon S3 buckets if the request does not include an `x-amz-server-side-encryption-aws-kms-key-id` header, unless the bucket is configured with default SSE-KMS encryption.

This is a preventive control with elective guidance, based on resource control policies (RCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon S3

###### Control metadata

- **Control objective:** Encrypt data at rest
- **Implementation:** Resource control policy (RCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `Multiple`

###### Usage considerations

- During landing zone setup, AWS Control Tower creates Amazon S3 buckets. Optionally, you can configure AWS Control Tower to orchestrate other AWS services, such as AWS CloudTrail and AWS Config, to send log entries to these buckets. When you configure your landing zone, AWS Control Tower provides the option that the objects created by those other services are encrypted with an AWS KMS key that you manage. If you have not configured your landing zone to use a KMS key with those other services,this control prevents those other services from logging to the S3 buckets that AWS Control Tower created, for any targets, such as OUs, that contain these buckets.

As a best practice, configure AWS Control Tower to use KMS keys before you enable this control. Otherwise, this control could block `PutObject` requests from services that AWS Control Tower configures, such as AWS CloudTrail and AWS Config. To learn more about the resources that AWS Control Tower creates during landing zone setup, see [Resources created in the shared accounts](../userguide/shared-account-resources.md "../userguide/shared-account-resources.md") in the _AWS Control Tower User Guide_. To learn more about how AWS Control Tower uses KMS keys with other services, see [Optionally configure AWS KMS keys](../userguide/configure-kms-keys.md "../userguide/configure-kms-keys.md") in the _AWS Control Tower User Guide_.

- After you enable this control, if you try to upload an S3 object without the `x-amz-server-side-encryption-aws-kms-key-id` header in the request, the upload will fail for buckets that do not have default SSE-KMS encryption configured. Before enabling this control on a target, consider whether all Amazon S3 buckets in the target environment are configured with default SSE-KMS encryption. Alternatively, if you upload objects to buckets that are not configured with default SSE-KMS encryption, check that all clients set the `x-amz-server-side-encryption-aws-kms-key-id` explicitly.

The artifact for this control is the following resource control policy (RCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTS3PV6",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:PutObject",
            {% if ExemptedResourceArns %}
            "NotResource": {{ExemptedResourceArns}}
            {% else %}
            "Resource": "*"
            {% endif %},
            "Condition": {
                "Null": {
                    "s3:x-amz-server-side-encryption-aws-kms-key-id": "true"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}

```

## [CT.SECRETSMANAGER.PV.1] Require that the organization's AWS Secrets Manager resources are accessible only by IAM principals that belong to the organization or by an AWS service

This control disallows AWS Secrets Manager API operations for your organization's AWS Secrets Manager resources by an AWS IAM principal, when the principal is outside of the organization and is not an AWS service principal.

This is a preventive control with elective guidance, based on resource control policies (RCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** AWS Secrets Manager

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Resource control policy (RCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `Multiple`

###### Usage considerations

- When you enable this control, AWS Control Tower populates the template RCP with the ID of the organization that your AWS Control Tower landing zone governs.
- Choose the Organizational Unit (OU) to which this control will apply. If AWS Secrets Manager resources in that OU must be accessible by a trusted party besides your organization or an AWS service (for instance, another organization or specific IAM role), this control causes requests by that trusted party to be denied. Consider which principals need access to the AWS Secrets Manager resources in your OU before you enable this control on that OU.
- This control does not provide protection for cross-service confused deputy scenarios. Consider enabling the related control for AWS Secrets Manager, which applies an RCP to govern direct AWS service access to the organization's AWS Secrets Manager resources. For more information about cross-service confused deputy prevention, see [Cross-service confused deputy prevention](../../../IAM/latest/UserGuide/confused-deputy.md#cross-service-confused-deputy-prevention "../../../IAM/latest/UserGuide/confused-deputy.md#cross-service-confused-deputy-prevention") in the _AWS Identity and Access Management User Guide_.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following resource control policy (RCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTSECRETSMANAGERPV1",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "secretsmanager:*",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:PrincipalIsAWSService": "false"
                },
                "StringNotEqualsIfExists": {
                    "aws:PrincipalOrgID": {{OrganizationIds}}
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}



```

## [CT.SQS.PV.1] Require that the organization's Amazon SQS resources are accessible only by IAM principals that belong to the organization, or by an AWS service

This control disallows Amazon SQS API operations for your organization's Amazon SQS resources by an AWS IAM principal, when the principal is outside of the organization and is not an AWS service principal.

This is a preventive control with elective guidance, based on resource control policies (RCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon SQS

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Resource control policy (RCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `Multiple`

###### Usage considerations

- When you enable this control, AWS Control Tower populates the template RCP with the ID of the organization that your AWS Control Tower landing zone governs.
- Choose the Organizational Unit (OU) to which this control will apply. If Amazon SQS resources in that OU must be accessible by a trusted party besides your organization or an AWS service (for instance, another organization or specific IAM role), this control causes requests by that trusted party to be denied. Consider which principals need access to the Amazon SQS resources in your OU before you enable this control on that OU.
- This control does not provide protection for cross-service confused deputy scenarios. Consider enabling the related control for Amazon SQS, which applies an RCP to govern direct AWS service access to the organization's Amazon SQS resources. For more information about cross-service confused deputy prevention, see [Cross-service confused deputy prevention](../../../IAM/latest/UserGuide/confused-deputy.md#cross-service-confused-deputy-prevention "../../../IAM/latest/UserGuide/confused-deputy.md#cross-service-confused-deputy-prevention") in the _AWS Identity and Access Management User Guide_.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following resource control policy (RCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTSQSPV1",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "sqs:*",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:PrincipalIsAWSService": "false"
                },
                "StringNotEqualsIfExists": {
                    "aws:PrincipalOrgID": {{OrganizationIds}}
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}

```

## [CT.STS.PV.1] Require that the organization's AWS Security Token Service resources are accessible only by IAM principals that belong to the organization, or by an AWS service

This control disallows select AWS Security Token Service (STS) API operations by an AWS IAM principal for your organization's AWS Security Token Service resources, when the principal is outside of the organization and is not an AWS service principal.

This is a preventive control with elective guidance, based on resource control policies (RCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** AWS Security Token Service

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Resource control policy (RCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `Multiple`

###### Usage considerations

- When you enable this control, AWS Control Tower populates the template RCP with the ID of the organization that your AWS Control Tower landing zone governs.
- Choose the Organizational Unit (OU) to which this control will apply. If AWS Security Token Service (STS) resources in that OU must be accessible by a trusted party besides your organization or an AWS service (for instance, another organization or specific IAM role), this control causes requests by that trusted party to be denied. Consider which principals need access to the AWS Security Token Service resources in your OU before you enable this control on that OU.
- This control does not include `sts:AssumeRoleWithSAML` and `sts:AssumeRoleWithWebIdentity` permissions in its scope, as the respective STS operations do not use AWS security credentials, and therefore do not include the `aws:PrincipalOrgID` condition key value in the request context. To ensure that `AssumeRoleWithSAML` and `AssumeRoleWithWebIdentity` operations are not denied by this control, `sts:SetSourceIdentity` and `sts:TagSession` permissions are also excluded from the controls scope.
- This control does not include `sts:GetCallerIdentity` permissions in its scope. No permissions are required to perform the respective STS operation.
- This control includes only actions that have resources listed in the **Resource type** column of the [_AWS Security Token Service Authorization Reference_](../../../service-authorization/latest/reference/list_awssecuritytokenservice.md "../../../service-authorization/latest/reference/list_awssecuritytokenservice.md") that can be invoked from outside the organization. For more information about
  the behavior of IAM actions that do not have associated resource types, see [RCP Effects on Permissions](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md#rcp-effects-on-permissions "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md#rcp-effects-on-permissions") in
  the _AWS Organizations User Guide_
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").

The artifact for this control is the following resource control policy (RCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTSTSPV1",
            "Effect": "Deny",
            "Principal": "*",
            "Action": [
                "sts:AssumeRole",
                "sts:SetContext"
            ],
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:PrincipalIsAWSService": "false"
                },
                "StringNotEqualsIfExists": {
                    "aws:PrincipalOrgID": {{OrganizationIds}}
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}



```
