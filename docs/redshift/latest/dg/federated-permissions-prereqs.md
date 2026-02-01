Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Prerequisites

## IAM policy requirements for Amazon Redshift federated permissions setup

Amazon Redshift federated permissions enables you to centrally manage data access across your analytics workloads, with permissions managed by the Redshift warehouse directly.

To enable Amazon Redshift federated permissions, specific IAM permissions are required beyond the standard permissions needed for creating Redshift provisioned clusters and serverless namespaces.

For Redshift provisioned warehouse to enable Redshift federated permissions:

- `redshift:ModifyLakehouseConfiguration`
- `redshift:RegisterNamespace`

For Redshift Serverless warehouse to enable Redshift federated permissions:

- `redshift-serverless:UpdateLakehouseConfiguration`
- `redshift:RegisterNamespace`

For AWS Glue Data Catalog integration to create a catalog with Redshift federated permissions:

- `glue:CreateCatalog`
- `glue:GetCatalog`

_For Lake Formation resource registration as one time registration to enable Redshift permission federation from remote warehouse with federated permissions:_

- `lakeformation:RegisterResource`
- `lakeformation:RegisterResourceWithPrivilegedAccess`

## IAM Identity Center application configuration for Redshift warehouse with federated permissions

Amazon Redshift supports identity center identity propagation to seamlessly pass user identities between Redshift instances and AWS Lake Formation and AWS Glue services. This capability requires
configuring dedicated IdC applications.

_Required IAM Permissions_

To create and manage the identity center application for identity center identity propagation, ensure your IAM permissions include the following permissions:

_For Amazon Redshift IdC application management:_

- `redshift:CreateRedshiftIdcApplication`
- `redshift:ModifyRedshiftIdcApplication`
- `redshift:DescribeRedshiftIdcApplications`

_For Lake Formation IdC application management:_

- `lakeformation:CreateLakeFormationIdentityCenterConfiguration`
- `lakeformation:DescribeLakeFormationIdentityCenterConfiguration`
- `lakeformation:UpdateLakeFormationIdentityCenterConfiguration`

**Create corresponding IdC applications and configuration**

To establish identity propagation for your analytics workloads, create an Amazon Redshift IdC application of type Lakehouse. It manages permissions without requiring explicit user assignments.
Redshift warehouses linked to this application require CONNECT privileges for IdC users to authenticate connections.

You can create only one Amazon Redshift IdC application of type Lakehouse per AWS account. This application handles identity propagation across all
Redshift warehouses that are integrated with Lake Formation and AWS Glue services. The application can only be used with Redshift warehouses that are registered with the AWS Glue Data Catalog.

**Prepare the IAM role assumed by Redshift and used by IdC identity propagation**

Redshift Lakehouse IdC application creation requires an IAM role from your account with certain IAM permissions.
Your IAM role used in your Redshift IdC Applications should have the following trust relationship to allow Redshift to assume it and set context for IdC identity propagation.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "redshift-serverless.amazonaws.com",
                    "redshift.amazonaws.com"
                ]
            },
            "Action": [
                "sts:AssumeRole",
                "sts:SetContext"
            ]
        }
    ]
}
```

And below permissions for your IdC IAM role to support IdC identity propagation.

- [AmazonRedshiftFederatedAuthorization](../../../aws-managed-policy/latest/reference/AmazonRedshiftFederatedAuthorization.md "../../../aws-managed-policy/latest/reference/AmazonRedshiftFederatedAuthorization.md") – This policy enables Amazon Redshift to query AWS Glue Data Catalog databases through federated permissions.
- AWSIDC Set Context Policy

```
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:SetContext"
            ],
            "Resource": "*"
        }
    ]
}
```

- [Setting up Redshift as an AWS managed application with AWS IAM Identity Center](../mgmt/redshift-iam-access-control-idp-connect-console.md#redshift-iam-access-control-idp-connect-admin-tasks "../mgmt/redshift-iam-access-control-idp-connect-console.md#redshift-iam-access-control-idp-connect-admin-tasks").
- AWSIDC identity center SSO IAM policy:
  - `sso:DescribeApplication` – Required to create an identity provider (IdP) entry in the catalog.
  - `sso:DescribeInstance` – Used to manually create IdP federated roles or users.

  ```
  {
    "Sid": "VisualEditor1",
    "Effect": "Allow",
    "Action": [
      "sso:DescribeApplication",
      "sso:DescribeInstance"
    ],
    "Resource": [
      "arn:aws:sso:::instance/<IAM Identity Center Instance ID>",
      "arn:aws:sso::<AWS-account-id>:application/<IAM Identity Center Instance ID>/*"
    ]
  }

  ```

Create a new Lakehouse type Redshift IdC application

CLI
Create your Lakehouse IdC application by specifying the Lakehouse application type in `create-redshift-idc-application` request,
which eliminates the need for explicit user assignments in Identity Center while enabling `CONNECT` privileges requirement for IdC user authentication:

```
aws redshift create-redshift-idc-application \
--idc-instance-arn <your_idc_instance_arn> \
--idc-display-name '<name_of_idc_application_display_on_idc_console>' \
--iam-role-arn <idc_carrier_role_arn> \
--application-type Lakehouse \
--redshift-idc-application-name '<name_of_idc_display_on_redshift_console>' \
--service-integrations '[
        {
            "LakeFormation":[
                {
                    "LakeFormationQuery":{"Authorization": "Enabled"}
                }
            ]
        },
        {
            "Redshift":[
                {
                    "Connect" : {
                        "Authorization": "Enabled"
                    }
                }
            ]
        }
    ]'
```

This configuration enables trusted identity propagation between Redshift and Lake Formation, allowing users to access data
across services using their Identity Center credentials without additional permission assignments.

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to IAM Identity Center connections page and select **Create application**.
3. Configure your general idc application settings.
4. Select **Configure Amazon Redshift federated permissions using AWS IAM Identity Center (Recommended)** to set the application type.
5. The Lake Formation and Redshift connect identity propagation integrations are enabled by default.
6. Complete the remaining cluster settings and choose **Create application**.

Modify an existing Redshift IdC application

If you have an existing Redshift IdC application that doesn't have the required service integrations enabled, you can update it to
support identity propagation between services and clusters/namespaces.

CLI
Use the `modify-redshift-idc-application` command to enable both `LakeFormation:query` authorization and `Redshift:Connect` authorization.
These integrations are essential for cross-service and cross-cluster IdC identity propagation:

```
aws redshift modify-redshift-idc-application \
--redshift-idc-application-arn '<arn_of_the_target_redshift_idc_application>' \
--service-integrations '[
        {
            "LakeFormation":[
                {
                    "LakeFormationQuery":{"Authorization": "Enabled"}
                }
            ]
        },
        {
            "Redshift":[
                {
                    "Connect" : {
                        "Authorization": "Enabled"
                    }
                }
            ]
        }
    ]'
```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to IAM Identity Center connections page and choose an existing IDC application you want to edit.
3. Choose Identity propagation integrations to enable and configure other settings and choose **Save changes**.

**Create Lake Formation identity center configuration**

Your Lake Formation service requires a dedicated IdC application if one has not been created yet.
You must also enable `Redshift:Connect` authorization for the configuration to function properly.

CLI
Use the `create-lake-formation-identity-center-configuration` command to enable
`Redshift:Connect` authorization. These integrations are essential for Lake Formation
propagates IdC identity to Redshift clusters and Redshift Serverless Namespaces

```
aws lakeformation  create-lake-formation-identity-center-configuration \
--instance-arn <your_idc_instance_arn> \
--service-integrations '[{
  "Redshift": [{
    "RedshiftConnect": {
      "Authorization": "ENABLED"
    }
  }]
}]'
```

Console

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the left navigation pane, select **IAM Identity Center integration**.
3. On the IAM Identity Center integration page you can enable trusted identity propagation for
   Amazon Redshift connect. Lake Formation propagates identity to downstream based on the
   effective permissions, so that authorized applications can access data on behalf of users.

**Update Lake Formation identity center configuration**

If you had configured Lake Formation IdC application that doesn't have the required service integrations enabled,
you can update it to support identity propagation between services and clusters/namespaces.

CLI
Use the `update-lake-formation-identity-center-configuration` command to enable
`Redshift:Connect` authorization. These integrations are essential for
cross-service and cross-cluster IdC identity propagation:

```
aws lakeformation update-lake-formation-identity-center-configuration \
--service-integrations '[{
  "Redshift": [{
    "RedshiftConnect": {
      "Authorization": "ENABLED"
    }
  }]
}]'
```

Console

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the left navigation pane, select **IAM Identity Center integration**.
3. On the IAM Identity Center integration page you can enable trusted identity propagation for Amazon Redshift
   connect. Lake Formation propagates identity to downstream based on the effective permissions, so
   that authorized applications can access data on behalf of users.

## Lake Formation prerequisites

Customer need Lake Formation `CREATE_CATALOG` permissions to enable AWS Glue Data Catalog with Amazon Redshift
federated permissions.

1. If the account belongs to an existing Lake Formation customer, the Lake Formation
   administrator must explicitly grant CREATE_CATALOG permission to each cluster creator. Use the
   following sample CLI command:

```
aws lakeformation grant-permissions \
    --cli-input-json \
    '{
        "Principal": {
            "DataLakePrincipalIdentifier": "<PrincipalArn>"
        },
        "Resource": {
            "Catalog": {}
        },
        "Permissions": [
            "CREATE_CATALOG"
        ]
    }'
```

2. If the account has never used Lake Formation, verify that Catalog Creators is set to
   IAMAllowedPrincipals in the Administrative Roles and Tasks page of the Lake Formation console.
   If not configured, set up a Data Lake Administrator by following the
   [Create a data lake administrator](../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin "../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin"). Alternatively, you can create a
   Data Lake Administrator with the minimum required policies if you will
   only use AWS Glue Data Catalog with Amazon Redshift federated permissions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "lakeformation:PutDataLakeSettings",
                "lakeformation:GrantPermissions",
                "lakeformation:GetDataLakeSettings",
                "lakeformation:BatchGrantPermissions",
                "lakeformation:ListPermissions"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

3. Have the DataLake Admin grant permissions to the
   IAMAllowedPrincipals to Create Catalog. Access can be granted through the **Grant**
   button for Catalog Creators in the Administrative Role and Tasks page.

## Connect privileges

As part of Amazon Redshift federated permissions, Amazon Redshift has introduced CONNECT
privileges to manage AWS IAM Identity Center federated users' access to Amazon Redshift workgroups or clusters.
This feature is available when Amazon Redshift federated permissions are enabled on the workgroup or cluster.

This privilege enables administrators to control user access through granular permissions at each
Amazon Redshift workgroup(s) or clusters(s) where Amazon Redshift federated permissions are enabled.
Amazon Redshift administrator can specify which AWS IAM Identity Center federated user(s) or group(s) have
access to directly connect to the Amazon Redshift workgroup or cluster, providing fine-grained control
over the AWS IAM Identity Center user access at each workgroup or cluster.

### Syntax

```
GRANT CONNECT [ON WORKGROUP]
TO [USER] <prefix>:<username> | ROLE <prefix>:<rolename> | PUBLIC;
```

CONNECT [ON WORKGROUP]

Grants permission to connect to a workgroup. The CONNECT permission is
applicable only for AWS IAM Identity Center identities (users and roles).

TO <prefix>:<username>

Indicates the AWS IAM Identity Center federated user receiving the permissions.

TO ROLE <prefix>:<rolename>

Indicates the AWS IAM Identity Center federated group receiving the permissions.

PUBLIC

Grants the CONNECT permissions to all AWS IAM Identity Center federated users, including users created later.
