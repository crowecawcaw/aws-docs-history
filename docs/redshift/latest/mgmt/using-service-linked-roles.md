Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using service-linked roles for

Amazon Redshift

Amazon Redshift uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon Redshift. Service-linked roles are predefined by Amazon Redshift and
include all the permissions that the service requires to call AWS services on behalf of your
Amazon Redshift cluster.

A service-linked role makes setting up Amazon Redshift easier because you don't have
to add the necessary permissions manually. The role is linked to Amazon Redshift use cases and
has predefined permissions. Only Amazon Redshift can assume the role, and only the
service-linked role can use the predefined permissions policy. Amazon Redshift creates a
service-linked role in your account the first time you create a cluster or a Redshift-managed VPC endpoint.
You can delete the
service-linked role only after you delete all of the Amazon Redshift clusters or Redshift-managed VPC endpoints in your account.
This protects your Amazon Redshift resources because you can't inadvertently remove
permissions needed for access to the resources.

Amazon Redshift supports using service-linked roles in all of the Regions where the service is
available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md#redshift_region "../../../general/latest/gr/rande.md#redshift_region").

For information about other services that support service-linked roles, see [AWS services that work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the
**Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for

Amazon Redshift

Amazon Redshift uses the service-linked role named **AWSServiceRoleForRedshift** –
Allows Amazon Redshift to call AWS services on your behalf. This service-linked role is attached to the following managed policy: `AmazonRedshiftServiceLinkedRolePolicy`. For updates to this policy, see [AWS-managed (predefined) policies for Amazon Redshift](redshift-iam-access-control-identity-based.md#redshift-policy-resources.managed-policies "redshift-iam-access-control-identity-based.md#redshift-policy-resources.managed-policies").

The AWSServiceRoleForRedshift service-linked role trusts only `redshift.amazonaws.com` to assume the
role.

The AWSServiceRoleForRedshift service-linked role permissions policy allows Amazon Redshift to complete the
following on all related resources:

- `ec2:DescribeVpcs`
- `ec2:DescribeSubnets`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribeAddress`
- `ec2:AssociateAddress`
- `ec2:DisassociateAddress`
- `ec2:CreateNetworkInterface`
- `ec2:DeleteNetworkInterface`
- `ec2:ModifyNetworkInterfaceAttribute`
- `ec2:CreateVpcEndpoint`
- `ec2:DeleteVpcEndpoints`
- `ec2:DescribeVpcEndpoints`
- `ec2:ModifyVpcEndpoint`
- `ec2:DescribeVpcAttribute`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeInternetGateways`
- `ec2:DescribeSecurityGroupRules`
- `ec2:DescribeAvailabilityZones`
- `ec2:DescribeNetworkAcls`
- `ec2:DescribeRouteTables`
- `ec2:AssignIpv6Addresses`
- `ec2:UnassignIpv6Addresses`

**Permissions for network resources**

The following permissions allow action on Amazon EC2 for creation and management of security group rules. These security groups and rules are specifically associated with the Amazon Redshift `aws:RequestTag/Redshift` resource tag. This limits the scope of the permissions to specific Amazon Redshift resources.

- `ec2:CreateSecurityGroup`
- `ec2:AuthorizeSecurityGroupEgress`
- `ec2:AuthorizeSecurityGroupIngress`
- `ec2:RevokeSecurityGroupEgress`
- `ec2:RevokeSecurityGroupIngress`
- `ec2:ModifySecurityGroupRules`
- `ec2:DeleteSecurityGroup`

**Permissions for service quotas**

The following permissions allow the caller to get service quotas.

`servicequotas:GetServiceQuota`

The following JSON fragment shows action and resource scope for service quotas.

```
{
   "Sid": "ServiceQuotasToCheckCustomerLimits",
   "Effect": "Allow",
   "Action": [
      "servicequotas:GetServiceQuota"
   ],
   "Resource": [
      "arn:aws:servicequotas:*:*:ec2/L-0263D0A3",
      "arn:aws:servicequotas:*:*:vpc/L-29B6F2EB"
   ]
}
```

The quota codes are the following:

- _L-0263D0A3_ – The quota code for EC2-VPC Elastic IPs.
- _L-29B6F2EB_ – The quota code for Interface VPC endpoints per VPC.

For more information, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

**Actions for audit logging**

Actions listed with the `logs` prefix pertain to audit logging and related
features. Specifically, creation and management of log groups and log streams.

- `logs:CreateLogGroup`
- `logs:PutRetentionPolicy`
- `logs:CreateLogStream`
- `logs:PutLogEvents`
- `logs:DescribeLogStreams`
- `logs:GetLogEvents`

The following JSON shows actions and resource scope, to Amazon Redshift, for audit logging.

```
[
    {
        "Sid": "EnableCreationAndManagementOfRedshiftCloudwatchLogGroups",
        "Effect": "Allow",
        "Action": [
            "logs:CreateLogGroup",
            "logs:PutRetentionPolicy"
        ],
        "Resource": [
            "arn:aws:logs:*:*:log-group:/aws/redshift/*"
        ]
    },
    {
        "Sid": "EnableCreationAndManagementOfRedshiftCloudwatchLogStreams",
        "Effect": "Allow",
        "Action": [
            "logs:CreateLogStream",
            "logs:PutLogEvents",
            "logs:DescribeLogStreams",
            "logs:GetLogEvents"
        ],
        "Resource": [
            "arn:aws:logs:*:*:log-group:/aws/redshift/*:log-stream:*"
        ]
    }
]
```

For more information
about service-linked roles and their purpose in AWS, see [Using service-linked roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md"). For more information about
specific actions and other IAM resources for Amazon Redshift,
see [Actions, resources, and condition keys for Amazon Redshift](../../../service-authorization/latest/reference/list_amazonredshift.md "../../../service-authorization/latest/reference/list_amazonredshift.md").

**Actions for managing admin credentials with AWS Secrets Manager**

Actions listed with the `secretsmanager` prefix pertain to using Amazon Redshift to manage your admin credentials.
These actions let Amazon Redshift use AWS Secrets Manager to create and manage your admin credential secrets.

The following JSON shows actions and resource scope, to Amazon Redshift, for managing admin credentials with AWS Secrets Manager.

```
[
    {
        "Effect": "Allow",
        "Action": [
            "secretsmanager:DescribeSecret",
            "secretsmanager:DeleteSecret",
            "secretsmanager:PutSecretValue",
            "secretsmanager:UpdateSecret",
            "secretsmanager:UpdateSecretVersionStage",
            "secretsmanager:RotateSecret"
        ],
        "Resource": [
            "arn:aws:secretsmanager:*:*:secret:redshift!*"
        ],
        "Condition": {
            "StringEquals": {
                "secretsmanager:ResourceTag/aws:secretsmanager:owningService": "redshift"
            }
        }
    },
    {
        "Effect": "Allow",
        "Action": [
            "secretsmanager:GetRandomPassword"
        ],
        "Resource": "*"
    }
]
```

**Actions for registering clusters and serverless namespaces to the AWS Glue Data Catalog**

Actions listed with the `glue` prefix pertain to accessing catalogs in the AWS Glue Data Catalog made from
registering provisioned clusters or serverless namespaces. For more information, see [Apache Iceberg compatibility for Amazon Redshift](../dg/iceberg-integration_overview.md "../dg/iceberg-integration_overview.md") in the _Amazon Redshift Database Developer Guide_.

The following JSON shows actions and resource scope, to Amazon Redshift, for accessing catalogs in the AWS Glue Data Catalog:

```
[
    {
        "Sid": "DiscoverRedshiftCatalogs",
        "Effect": "Allow",
        "Action": [
            "glue:GetCatalogs",
            "glue:GetCatalog"
        ],
        "Resource": [
            "arn:aws:glue:*:*:catalog",
            "arn:aws:glue:*:*:catalog/*"
        ],
   "Condition":
    {
        "Bool":
        {
            "glue:EnabledForRedshiftAutoDiscovery": "true"
        },
        "StringEquals": {
             "aws:ResourceAccount": "${aws:PrincipalAccount}"
        }
    }
 },
 {
    "Sid": "LakeFormationGetMetadataAccessForFederatedCatalogs",
    "Effect": "Allow",
    "Action": [
        "lakeformation:GetDataAccess"
    ],
    "Resource": [ "*" ],
    "Condition":
    {
        "Bool":
        {
            "lakeformation:EnabledOnlyForMetaDataAccess":"true"
        },
        "StringEquals": {
             "aws:ResourceAccount": "${aws:PrincipalAccount}"
        },
        "ForAnyValue:StringEquals":
        {
            "aws:CalledVia": "glue.amazonaws.com"
        }
    }
 }
    }
]
```

The `glue:GetCatalog` and `glue:GetCatalogs` permissions have the condition
`glue:EnabledForRedshiftAutoDiscovery:true`, which means that Amazon Redshift grants IAM
access for automatically discovering catalogs. To opt-out, add an AWS Glue account-level
resource policy to selectively deny service-linked role access to the catalogs.
Since the service-linked role already has an explicit allow action in the policy,
the opt-out policy needs to explicitly deny that action. Consider the following
example, where an additional policy denies auto discovery for Amazon Redshift:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : {
 "Effect": "Deny",
 "Action": [
 "glue:GetCatalog",
 "glue:GetCatalogs"
 ],
 "Principal" : {
 "AWS" : "arn:aws:iam::`111122223333`:role/aws-service-role/redshift.amazonaws.com/AWSServiceRoleForRedshift"
 },
 "Resource": [
 "arn:aws:glue:*:*:catalog/<`s3_table_catalog_name`>",
 "arn:aws:glue:*:*:catalog/<`s3_table_catalog_name`>/*"
 ]
 }
}`

```

**To allow an IAM entity to create AWSServiceRoleForRedshift service-linked
roles**

```
{
    "Effect": "Allow",
    "Action": [
        "iam:CreateServiceLinkedRole"
    ],
    "Resource": "arn:aws:iam::`<AWS-account-ID>`:role/aws-service-role/redshift.amazonaws.com/AWSServiceRoleForRedshift",
    "Condition": {"StringLike": {"iam:AWSServiceName": "redshift.amazonaws.com"}}
}
```

**To allow an IAM entity to delete AWSServiceRoleForRedshift service-linked
roles**

Add the following policy statement to the permissions for that IAM entity:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:DeleteServiceLinkedRole",
        "iam:GetServiceLinkedRoleDeletionStatus"
    ],
    "Resource": "arn:aws:iam::`<AWS-account-ID>`:role/aws-service-role/redshift.amazonaws.com/AWSServiceRoleForRedshift",
    "Condition": {"StringLike": {"iam:AWSServiceName": "redshift.amazonaws.com"}}
}

```

Alternatively, you can use an AWS managed policy to [provide full access](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonRedshiftFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AmazonRedshiftFullAccess") to Amazon Redshift.

## Creating a service-linked role for

Amazon Redshift

You don't need to manually create an AWSServiceRoleForRedshift service-linked role. Amazon Redshift
creates the service-linked role for you. If the AWSServiceRoleForRedshift service-linked role has been
deleted from your account, Amazon Redshift creates the role when you launch a new
Amazon Redshift cluster.

###### Important

If you used the Amazon Redshift service before September 18, 2017, when it began supporting
service-linked roles, then Amazon Redshift created the AWSServiceRoleForRedshift role in your account. To
learn more, see [A new
role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

## Editing a service-linked role for

Amazon Redshift

Amazon Redshift does not allow you to edit the AWSServiceRoleForRedshift service-linked role. After you
create a service-linked role, you can't change the name of the role because various entities
might reference the role. However, you can edit the description of the role using the IAM
console, the AWS Command Line Interface (AWS CLI), or IAM API. For more information, see
[Modifying a role](../../../IAM/latest/UserGuide/id_roles_manage_modify.md "../../../IAM/latest/UserGuide/id_roles_manage_modify.md") in the
_IAM User Guide_.

## Deleting a service-linked role for

Amazon Redshift

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don't have an unused entity that is not
actively monitored or maintained.

Before you can delete a service-linked role for an account, you must shut down and delete
any clusters in the account. For more information, see [Shutting down and deleting a
cluster](rs-mgmt-shutdown-delete-cluster.md "rs-mgmt-shutdown-delete-cluster.md").

You can use the IAM console, the AWS CLI, or the IAM API to delete a service-linked role.
For more information, see [Deleting a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
