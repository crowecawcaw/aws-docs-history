# Getting started with AWS IAM Identity Center and Amazon EMR

This section helps you configure Amazon EMR to integrate with AWS IAM Identity Center.

###### Topics

- [Create an Identity Center instance](#emr-idc-start-instance "#emr-idc-start-instance")
- [Create an IAM role for Identity Center](#emr-idc-start-role "#emr-idc-start-role")
- [Add permissions for services not integrated with IAM Identity Center](#emr-idc-start-securityconfig-nonidc "#emr-idc-start-securityconfig-nonidc")
- [Create an Identity Center enabled security
  configuration](#emr-idc-start-securityconfig "#emr-idc-start-securityconfig")
- [Create and launch an Identity Center enabled
  cluster](#emr-idc-cluster "#emr-idc-cluster")
- [Configure Lake Formation for an IAM Identity Center enabled
  EMR cluster](emr-idc-lf.md "emr-idc-lf.md")
- [Working with S3 Access Grants on an IAM Identity Center enabled
  EMR cluster](emr-idc-s3ag.md "emr-idc-s3ag.md")

###### Note

In order to use Identity Center integration with EMR, Lake Formation or S3 Access Grants must be enabled. You can also use both. If neither is
enabled, Identity Center integration isn't supported.

## Create an Identity Center instance

If you don't already have one, create an Identity Center instance in the AWS Region
where you want to launch your EMR cluster. An Identity Center instance can only exist
in a single Region for an AWS account.

Use the following AWS CLI command to create a new instance named
`MyInstance`:

```
aws sso-admin create-instance --name `MyInstance`
```

## Create an IAM role for Identity Center

To integrate Amazon EMR with AWS IAM Identity Center, create an IAM role that authenticates with
Identity Center from the EMR cluster. Under the hood, Amazon EMR uses SigV4
credentials to relay the Identity Center identity to downstream services such as
AWS Lake Formation. Your role should also have the respective permissions to invoke the
downstream services.

When you create the role, use the following permissions policy:

```
{
  "Statement": [
    {
      "Sid": "IdCPermissions",
      "Effect": "Allow",
      "Action": [
        "sso-oauth:*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "GlueandLakePermissions",
      "Effect": "Allow",
      "Action": [
        "glue:*",
        "lakeformation:GetDataAccess"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AccessGrantsPermissions",
      "Effect": "Allow",
      "Action": [
        "s3:GetDataAccess",
        "s3:GetAccessGrantsInstanceForPrefix"
      ],
      "Resource": "*"
    }
  ]
}
```

The trust policy for this role allows the InstanceProfile role to
let it assume the role.

```
{
    "Sid": "AssumeRole",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::12345678912:role/EMR_EC2_DefaultRole"
    },
    "Action": [
        "sts:AssumeRole",
        "sts:SetContext"
    ]
}
```

If the role doesn't have trusted credentials and accesses a Lake Formation-protected table, Amazon EMR automatically
sets the `principalId` of the assumed role to ``userID`-untrusted`. The following
 is a snippet of a CloudTrail event that displays the `principalId`.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "ABCDEFGH1JKLMNO2PQR3TU:5000-untrusted",
        "arn": "arn:aws:sts::123456789012:assumed-role/EMR_TIP/5000-untrusted",
        "accountId": "123456789012",
        "accessKeyId": "ABCDEFGH1IJKLMNOPQ7R3"
        ...

```

## Add permissions for services not integrated with IAM Identity Center

AWS credentials that use Trusted Identity Propagation the IAM policies defined in the IAM role for any calls
made to services not integrated with IAM Identity Center. This includes, for example, the AWS Key Management Service. Your role should also define any IAM permissions for any such
services you would attempt to access example AWS Key Management Service. Currently supported IAM Identity Center integrated services include AWS Lake Formation
and Amazon S3 Access Grants.

To learn more about Trusted Identity Propagation,
see [Trusted Identity Propagation across applications](../../../singlesignon/latest/userguide/trustedidentitypropagation.md "../../../singlesignon/latest/userguide/trustedidentitypropagation.md").

## Create an Identity Center enabled security

configuration

To launch an EMR cluster with IAM Identity Center integration, use the following example
command to create an Amazon EMR security configuration that has Identity Center enabled. Each
configuration is explained below.

```
aws emr create-security-configuration --name "IdentityCenterConfiguration-with-lf-accessgrants" --region "us-west-2" --security-configuration '{
    "AuthenticationConfiguration":{
        "IdentityCenterConfiguration":{
            "EnableIdentityCenter":true,
            "IdentityCenterApplicationAssigmentRequired":false,
            "IdentityCenterInstanceARN": "arn:aws:sso:::instance/ssoins-123xxxxxxxxxx789"
        }
    },
    "AuthorizationConfiguration": {
        "LakeFormationConfiguration": {
            "AuthorizedSessionTagValue": "Amazon EMR"
        },
        "IAMConfiguration": {
          "EnableApplicationScopedIAMRole": true,
          "ApplicationScopedIAMRoleConfiguration": {
            "PropagateSourceIdentity": true
          }
        }
    },
    "EncryptionConfiguration": {
        "EnableInTransitEncryption": true,
        "EnableAtRestEncryption": false,
        "InTransitEncryptionConfiguration": {
            "TLSCertificateConfiguration": {
                "CertificateProviderType": "PEM",
                "S3Object": "s3://amzn-s3-demo-bucket/cert/my-certs.zip"
            }
        }
    }
}'
```

- `EnableIdentityCenter` –
  (required) Enables Identity Center integration.
- `IdentityCenterInstanceARN`
  – (optional) The Identity Center instance ARN. If this isn't included, the existing IAM Identity Center instance ARN is looked up
  as part of the configuration step.
- `IAMRoleForEMRIdentityCenterApplicationARN`
  – (required) The IAM role that procures Identity Center tokens from the
  cluster.
- `IdentityCenterApplicationAssignmentRequired` – (boolean) Governs if an assignment will be
  required to use the Identity Center application. This field is optional. If a value isn't provided, the default is `false`.
- `AuthorizationConfiguration` /
  `LakeFormationConfiguration` –
  Optionally, configure authorization:
  - `IAMConfiguration`
    – Enables EMR Runtimes Roles feature to be used in addition to your TIP identity. If you enable this configuration, then you (or the caller AWS Service) will be
    required to specify an IAM Runtime Role in each call to the EMR Steps or EMR `GetClusterSessionCredentials` APIs. If the EMR cluster is being
    used with SageMaker Unified Studio, then this option is required if Trusted Identity Propagation
    is also enabled.
  - `EnableLakeFormation`
    – Enable Lake Formation authorization on the cluster.

To enable Identity Center integration with Amazon EMR, you must specify
`EncryptionConfiguration` and
`IntransitEncryptionConfiguration`.

## Create and launch an Identity Center enabled

cluster

Now that you've set up the IAM role that authenticates with Identity Center, and
created an Amazon EMR security configuration that has Identity Center enabled, you can create
and launch your identity-aware cluster. For steps to launch your cluster with the
required security configuration, see [Specify a security configuration
for an Amazon EMR cluster](emr-specify-security-configuration.md "emr-specify-security-configuration.md").

The following sections describe how to configure your Identity Center
enabled cluster with security options that Amazon EMR supports:

- [Working with S3 Access Grants on an IAM Identity Center enabled
  EMR cluster](emr-idc-s3ag.md "emr-idc-s3ag.md")
- [Configure Lake Formation for an IAM Identity Center enabled
  EMR cluster](emr-idc-lf.md "emr-idc-lf.md")
