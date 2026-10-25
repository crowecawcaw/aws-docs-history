

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Prerequisites
<a name="federated-permissions-prereqs"></a>

## IAM policy requirements for Amazon Redshift federated permissions setup
<a name="federated-permissions-prereqs-iam"></a>

With Amazon Redshift federated permissions, you can centrally manage data access across your analytics workloads, with permissions managed by the Redshift warehouse directly.

To enable Amazon Redshift federated permissions, specific IAM permissions are required beyond the standard permissions needed for creating Redshift provisioned clusters and serverless namespaces.

For Redshift provisioned warehouse to enable Redshift federated permissions:
+ `redshift:ModifyLakehouseConfiguration`
+ `redshift:RegisterNamespace`

For Redshift Serverless warehouse to enable Redshift federated permissions:
+ `redshift-serverless:UpdateLakehouseConfiguration`
+ `redshift:RegisterNamespace`

If you register with the AWS Glue Data Catalog instead of Amazon Redshift multi-warehouse, additional IAM permissions and setup are required. See [AWS Glue Data Catalog Prerequisites](federated-permissions-prereqs-glue.md).

## IAM Identity Center application configuration for Redshift warehouse with federated permissions
<a name="federated-permissions-prereqs-configuration"></a>

Amazon Redshift supports identity center identity propagation to seamlessly pass user identities between Redshift instances and AWS Lake Formation and AWS Glue services. This capability requires configuring dedicated IdC applications.

*Required IAM Permissions*

To create and manage the identity center application for identity center identity propagation, make sure your IAM permissions include the following permissions:

*For Amazon Redshift IdC application management:*
+ `redshift:CreateRedshiftIdcApplication`
+ `redshift:ModifyRedshiftIdcApplication`
+ `redshift:DescribeRedshiftIdcApplications`

**Create corresponding IdC applications and configuration**

To establish identity propagation for your analytics workloads, create an Amazon Redshift IdC application of type Lakehouse. It manages permissions without requiring explicit user assignments. Redshift warehouses linked to this application require CONNECT privileges for IdC users to authenticate connections.

You can create only one Amazon Redshift IdC application of type Lakehouse per AWS account. This application handles identity propagation across all Redshift warehouses enabled for federated permissions.

**Prepare the IAM role assumed by Redshift and used by IdC identity propagation**

Redshift Lakehouse IdC application creation requires an IAM role from your account with certain IAM permissions. Your IAM role used in your Redshift IdC Applications should have the following trust relationship to allow Redshift to assume it and set context for IdC identity propagation.

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
+  [AmazonRedshiftFederatedAuthorization](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRedshiftFederatedAuthorization.html) – This policy enables Amazon Redshift to query AWS Glue Data Catalog databases through federated permissions. 
+ AWSIDC Set Context Policy

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
+ [ Setting up Redshift as an AWS managed application with AWS IAM Identity Center](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect-console.html#redshift-iam-access-control-idp-connect-admin-tasks).
+ AWSIDC identity center SSO IAM policy:
  + `sso:DescribeApplication` – Required to create an identity provider (IdP) entry in the catalog.
  + `sso:DescribeInstance` – Used to manually create IdP federated roles or users.

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

------
#### [ CLI ]

Create your Lakehouse IdC application by specifying the Lakehouse application type in `create-redshift-idc-application` request, which eliminates the need for explicit user assignments in Identity Center while enabling `CONNECT` privileges requirement for IdC user authentication:

```
aws redshift create-redshift-idc-application \
--idc-instance-arn <your_idc_instance_arn> \
--idc-display-name '<name_of_idc_application_display_on_idc_console>' \
--iam-role-arn <idc_carrier_role_arn> \
--application-type Lakehouse \
--redshift-idc-application-name '<name_of_idc_display_on_redshift_console>' \
--service-integrations '[
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

With this configuration, you can access data in Redshift warehouses using your Identity Center credentials, without additional permission assignments.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. Navigate to IAM Identity Center connections page and select **Create application**.

1. Configure your general idc application settings.

1. Select **Configure Amazon Redshift federated permissions using AWS IAM Identity Center (Recommended)** to set the application type.

1. Leave the Redshift connect identity propagation integration at its default (enabled) setting.

1. Complete the remaining cluster settings and choose **Create application**.

------

Modify an existing Redshift IdC application

If you have an existing Redshift IdC application that doesn't have the required service integrations enabled, you can update it to support identity propagation between services and clusters/namespaces.

------
#### [ CLI ]

Use the `modify-redshift-idc-application` command to enable `Redshift:Connect` authorization. This integration is essential for cross-cluster IdC identity propagation:

```
aws redshift modify-redshift-idc-application \
--redshift-idc-application-arn '<arn_of_the_target_redshift_idc_application>' \
--service-integrations '[
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

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. Navigate to IAM Identity Center connections page and choose an existing IDC application you want to edit.

1. Choose Identity propagation integrations to enable and configure other settings and choose **Save changes**.

------

If you register with the AWS Glue Data Catalog instead of Amazon Redshift multi-warehouse, you must also create or update a Lake Formation identity center configuration. See [AWS Glue Data Catalog Prerequisites](federated-permissions-prereqs-glue.md).

## Network configuration for enhanced VPC routing
<a name="federated-permissions-prereqs-network"></a>

If enhanced VPC routing is turned on, your VPC must be able to reach the AWS IAM Identity Center services. Otherwise, identity propagation fails. For more information about the network requirements, see [Using AWS IAM Identity Center with enhanced VPC routing](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect-evr.html).

## Connect privileges
<a name="federated-permissions-prereqs-connect"></a>

As part of Amazon Redshift federated permissions, Amazon Redshift has introduced CONNECT privileges to manage AWS IAM Identity Center federated users' access to Amazon Redshift workgroups or clusters. This feature is available when Amazon Redshift federated permissions are enabled on the workgroup or cluster.

This privilege enables administrators to control user access through granular permissions at each Amazon Redshift workgroup(s) or clusters(s) where Amazon Redshift federated permissions are enabled. Amazon Redshift administrator can specify which AWS IAM Identity Center federated user(s) or group(s) have access to directly connect to the Amazon Redshift workgroup or cluster, providing fine-grained control over the AWS IAM Identity Center user access at each workgroup or cluster.

### Syntax
<a name="federated-permissions-prereqs-connect-syntax"></a>

```
GRANT CONNECT [ON WORKGROUP]
TO <prefix>:<username> | ROLE <prefix>:<rolename> | PUBLIC;
```

CONNECT [ON WORKGROUP]  
Grants permission to connect to a workgroup. The CONNECT permission is applicable only for AWS IAM Identity Center identities (users and roles).

TO <prefix>:<username>  
Indicates the AWS IAM Identity Center federated user receiving the permissions.

TO ROLE <prefix>:<rolename>  
Indicates the AWS IAM Identity Center federated group receiving the permissions.

PUBLIC  
Grants the CONNECT permissions to all AWS IAM Identity Center federated users, including users created later.