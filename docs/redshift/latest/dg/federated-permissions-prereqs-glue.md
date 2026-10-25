

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# AWS Glue Data Catalog Prerequisites
<a name="federated-permissions-prereqs-glue"></a>

The following setup is required only if you register your warehouse with the AWS Glue Data Catalog (available through the Redshift console). It is not required for Amazon Redshift multi-warehouse federated permissions, which is managed directly by Redshift.

## IAM permissions for AWS Glue Data Catalog registration
<a name="federated-permissions-prereqs-glue-iam"></a>

For AWS Glue Data Catalog integration to create a catalog with Redshift federated permissions:
+ `glue:CreateCatalog`
+ `glue:GetCatalog`

For Lake Formation resource registration as one-time registration to enable Redshift federated permissions from a remote warehouse:
+ `lakeformation:RegisterResource`
+ `lakeformation:RegisterResourceWithPrivilegedAccess`

For Lake Formation IdC application management:
+ `lakeformation:CreateLakeFormationIdentityCenterConfiguration`
+ `lakeformation:DescribeLakeFormationIdentityCenterConfiguration`
+ `lakeformation:UpdateLakeFormationIdentityCenterConfiguration`

## Lake Formation integration for the Redshift IdC application
<a name="federated-permissions-prereqs-glue-lfidc"></a>

When you register with the AWS Glue Data Catalog, the Amazon Redshift IdC application of type Lakehouse must also enable the `LakeFormation` service integration (in addition to `Redshift:Connect`). Use the same `create-redshift-idc-application` or `modify-redshift-idc-application` commands described in [IAM Identity Center application configuration for Redshift warehouse with federated permissions](federated-permissions-prereqs.md#federated-permissions-prereqs-configuration), with the Lake Formation integration added.

------
#### [ Create (CLI) ]

Add the `LakeFormation` integration when creating your Lakehouse IdC application:

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

With this configuration, you can access data across services using your Identity Center credentials, without additional permission assignments.

------
#### [ Modify (CLI) ]

Use the `modify-redshift-idc-application` command to enable both `LakeFormation:query` authorization and `Redshift:Connect` authorization. These integrations are essential for cross-service and cross-cluster IdC identity propagation:

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

------

## Create Lake Formation identity center configuration
<a name="federated-permissions-prereqs-glue-lfconfig"></a>

Your Lake Formation service requires a dedicated IdC application if one has not been created yet. You must also enable `Redshift:Connect` authorization for the configuration to function properly.

------
#### [ CLI ]

Use the `create-lake-formation-identity-center-configuration` command to enable `Redshift:Connect` authorization. These integrations are essential for Lake Formation propagates IdC identity to Redshift clusters and Redshift Serverless Namespaces

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

------
#### [ Console ]

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. In the left navigation pane, select **IAM Identity Center integration**.

1. On the IAM Identity Center integration page you can enable trusted identity propagation for Amazon Redshift connect. Lake Formation propagates identity to downstream based on the effective permissions, so that authorized applications can access data on behalf of users.

------

**Update Lake Formation identity center configuration**

If you had configured Lake Formation IdC application that doesn't have the required service integrations enabled, you can update it to support identity propagation between services and clusters/namespaces.

------
#### [ CLI ]

Use the `update-lake-formation-identity-center-configuration` command to enable `Redshift:Connect` authorization. These integrations are essential for cross-service and cross-cluster IdC identity propagation:

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

------
#### [ Console ]

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. In the left navigation pane, select **IAM Identity Center integration**.

1. On the IAM Identity Center integration page you can enable trusted identity propagation for Amazon Redshift connect. Lake Formation propagates identity to downstream based on the effective permissions, so that authorized applications can access data on behalf of users.

------

## AWS Glue Data Catalog prerequisites
<a name="federated-permissions-prereqs-glue-lfprereqs"></a>

You need Lake Formation `CREATE_CATALOG` permissions to enable AWS Glue Data Catalog with Amazon Redshift federated permissions.

1. If the account belongs to an existing Lake Formation customer, the Lake Formation administrator must explicitly grant CREATE\_CATALOG permission to each cluster creator. Use the following sample CLI command:

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

1. If the account has never used Lake Formation, verify that Catalog Creators is set to IAMAllowedPrincipals in the Administrative Roles and Tasks page of the Lake Formation console. If not configured, set up a Data Lake Administrator by following the [ Create a data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin). Alternatively, you can create a Data Lake Administrator with the minimum required policies if you will only use AWS Glue Data Catalog with Amazon Redshift federated permissions.

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

1. Have the DataLake Admin grant permissions to the IAMAllowedPrincipals to Create Catalog. Access can be granted through the **Grant** button for Catalog Creators in the Administrative Role and Tasks page.