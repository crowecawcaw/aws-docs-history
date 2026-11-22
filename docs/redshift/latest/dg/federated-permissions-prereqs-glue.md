

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# AWS Glue Data Catalog prerequisites

The following setup is required only if you register your warehouse with the AWS Glue Data Catalog (available through the Redshift console). It is not required for Amazon Redshift multi-warehouse federated permissions, which Redshift manages directly.

## IAM permissions for AWS Glue Data Catalog registration
<a name="federated-permissions-prereqs-glue-iam"></a>

AWS Glue Data Catalog integration requires the following IAM permissions to create a catalog with Redshift federated permissions:
+ `glue:CreateCatalog`
+ `glue:GetCatalog`

The following IAM permissions are required for Lake Formation resource registration, a one-time registration that enables Redshift federated permissions from a remote warehouse:
+ `lakeformation:RegisterResource`
+ `lakeformation:RegisterResourceWithPrivilegedAccess`

The following IAM permissions are required for Lake Formation AWS IAM Identity Center application management:
+ `lakeformation:CreateLakeFormationIdentityCenterConfiguration`
+ `lakeformation:DescribeLakeFormationIdentityCenterConfiguration`
+ `lakeformation:UpdateLakeFormationIdentityCenterConfiguration`

## Integrating Lake Formation with the Redshift IAM Identity Center application
<a name="federated-permissions-prereqs-glue-lfidc"></a>

When you register with the AWS Glue Data Catalog, the Amazon Redshift IAM Identity Center application of type Lakehouse must also enable the `LakeFormation` service integration (in addition to `Redshift:Connect`). Use the same `create-redshift-idc-application` or `modify-redshift-idc-application` commands described in [IAM Identity Center application configuration for Redshift warehouse with federated permissions](federated-permissions-prereqs.md#federated-permissions-prereqs-configuration), with the Lake Formation integration added.

**To create the IAM Identity Center application with Lake Formation integration using the AWS CLI**
+ Add the `LakeFormation` integration when creating your Lakehouse IAM Identity Center application. Replace the placeholder values, such as {{your\_idc\_instance\_arn}} and {{idc\_carrier\_role\_arn}}, with your own values:

  ```bash
  aws redshift create-redshift-idc-application \
  --idc-instance-arn {{your_idc_instance_arn}} \
  --idc-display-name '{{name_of_idc_application_display_on_idc_console}}' \
  --iam-role-arn {{idc_carrier_role_arn}} \
  --application-type Lakehouse \
  --redshift-idc-application-name '{{name_of_idc_display_on_redshift_console}}' \
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

**To modify the IAM Identity Center application to enable Lake Formation integration using the AWS CLI**
+ Use the `modify-redshift-idc-application` command to enable both `LakeFormation:query` authorization and `Redshift:Connect` authorization. These integrations are essential for cross-service and cross-cluster IAM Identity Center identity propagation:

  ```bash
  aws redshift modify-redshift-idc-application \
  --redshift-idc-application-arn '{{arn_of_the_target_redshift_idc_application}}' \
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

## Creating Lake Formation identity center configuration
<a name="federated-permissions-prereqs-glue-lfconfig"></a>

Your Lake Formation service requires a dedicated IAM Identity Center application if one has not been created yet. You must also enable `Redshift:Connect` authorization for the configuration to function properly.

**To create the configuration using the AWS CLI**
+ Use the `create-lake-formation-identity-center-configuration` command to enable `Redshift:Connect` authorization. These integrations are essential for Lake Formation to propagate IAM Identity Center identity to Redshift clusters and Redshift Serverless namespaces:

  ```bash
  aws lakeformation  create-lake-formation-identity-center-configuration \
  --instance-arn {{your_idc_instance_arn}} \
  --service-integrations '[{
    "Redshift": [{
      "RedshiftConnect": {
        "Authorization": "ENABLED"
      }
    }]
  }]'
  ```

**To create the configuration using the console**

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. In the left navigation pane, choose **IAM Identity Center integration**.

1. On the IAM Identity Center integration page, enable trusted identity propagation for Amazon Redshift connect. Lake Formation propagates identity to downstream based on the effective permissions, so that authorized applications can access data on behalf of users.

### Updating Lake Formation identity center configuration
<a name="federated-permissions-prereqs-glue-lfconfig-update"></a>

If you had configured Lake Formation IAM Identity Center application that doesn't have the required service integrations enabled, you can update it to support identity propagation between services, clusters, and namespaces.

**To update the configuration using the AWS CLI**
+ Use the `update-lake-formation-identity-center-configuration` command to enable `Redshift:Connect` authorization. These integrations are essential for cross-service and cross-cluster IAM Identity Center identity propagation:

  ```bash
  aws lakeformation update-lake-formation-identity-center-configuration \
  --service-integrations '[{                                                            
    "Redshift": [{
      "RedshiftConnect": {
        "Authorization": "ENABLED"
      }
    }]
  }]'
  ```

**To update the configuration using the console**

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. In the left navigation pane, choose **IAM Identity Center integration**.

1. On the IAM Identity Center integration page, enable trusted identity propagation for Amazon Redshift connect. Lake Formation propagates identity to downstream based on the effective permissions, so that authorized applications can access data on behalf of users.

## Granting Lake Formation CREATE\_CATALOG permissions
<a name="federated-permissions-prereqs-glue-lfprereqs"></a>

You need Lake Formation `CREATE_CATALOG` permissions to enable AWS Glue Data Catalog with Amazon Redshift federated permissions.

**To grant CREATE\_CATALOG permissions**

1. If the account belongs to an existing Lake Formation customer, the Lake Formation administrator must explicitly grant `CREATE_CATALOG` permission to each cluster creator. Use the following sample CLI command. Replace {{my-principal-arn}} with the ARN of the principal to grant the permission to:

   ```bash
   aws lakeformation grant-permissions \
       --cli-input-json \
       '{
           "Principal": {
               "DataLakePrincipalIdentifier": "{{my-principal-arn}}"
           },
           "Resource": {
               "Catalog": {}
           },
           "Permissions": [
               "CREATE_CATALOG"
           ]
       }'
   ```

1. If the account has never used Lake Formation, verify that **Catalog Creators** is set to `IAMAllowedPrincipals` on the **Administrative Roles and Tasks** page of the Lake Formation console. If not configured, set up a data lake administrator by following the [ Create a data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin). Alternatively, you can create a data lake administrator with the minimum required policies if you only use AWS Glue Data Catalog with Amazon Redshift federated permissions:

   ```json
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

1. Have the data lake administrator grant permissions to `IAMAllowedPrincipals` to create catalogs. The administrator can grant this access by choosing **Grant** for **Catalog Creators** on the **Administrative Roles and Tasks** page.