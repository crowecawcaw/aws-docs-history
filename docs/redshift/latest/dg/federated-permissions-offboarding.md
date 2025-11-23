Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Disabling AWS IAM Identity Center propagation

Before you can disable AWS IAM Identity Center propagation, you must have Amazon Redshift Cluster or Amazon Redshift Serverless Namespace has registered with AWS Glue Data Catalog and associated with a Lakehouse Redshift IdC Application. An
Amazon Redshift Serverless namespace requires a workgroup attached to perform the related operations.

## Disable AWS IAM Identity Center Identity Propagation for Amazon Redshift provisioned clusters

When disabling the AWS IAM Identity Center Identity Propagation for your Amazon Redshift Provisioned Clusters, the Lakehouse Redshift IdC Application attached to it will be marked as disabled in the cluster.

CLI
You can use `modify-lakehouse-configuration` command to disable IdC identity propagation for your clusters with Redshift Federated Permissions,
note it doesn’t delete the IdC provider from your cluster but put them into disabled mode.

```
aws redshift modify-lakehouse-configuration \
    --cluster-identifier 'redshift-cluster' \
    --lakehouse-idc-registration Disassociate \
```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the provisioned cluster that you want to edit registration for and select it.
3. From the cluster’s details page, select **Edit AWS Glue Data Catalog registration** from the **Actions** drop-down menu.
4. Select **Disable** from the Amazon Redshift federated permissions using AWS IAM Identity Center drop-down to disassociate IDC application and choose **Save changes**.

## Disable AWS IAM Identity Center Identity Propagation for Amazon Redshift Serverless namespaces

CLI
You can use `modify-lakehouse-configuration` command to disable IdC identity propagation for your namespace with Redshift Federated Permissions,
note it doesn’t delete the IdC provider from your cluster but put them into disabled mode.

```
aws redshift-serverless update-lakehouse-configuration \
--namespace-name 'serverless-namespace-name' \
--lakehouse-idc-registration Disassociate \
```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the serverless namespace that you want to edit registration for and select it.
3. From the namespace’s details page, select **Edit AWS Glue Data Catalog registration** from the **Actions** drop-down menu.
4. Select **Disable** from the Amazon Redshift federated permissions using AWS IAM Identity Center drop-down to disassociate IDC application and choose **Save changes**.
