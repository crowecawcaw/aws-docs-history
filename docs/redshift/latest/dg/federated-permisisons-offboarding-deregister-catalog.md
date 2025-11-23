Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Deregister from AWS Glue Data Catalog

## IAM Policy Requirements for Amazon Redshift Federated Permissions Deregistration

To deregister your cluster or serverless namespace from AWS Glue Data Catalog, below IAM permissions are required.

For Redshift Provisioned Clusters

- `redshift:ModifyLakehouseConfiguration`
- `redshift:DregisterNamespace`

For Redshift Serverless

- `redshift-serverless:UpdateLakehouseConfiguration`
- `redshift:DregisterNamespace`

For AWS Glue Data Catalog Integration

- `glue:DeleteCatalog`
- `glue:GetCatalog`

For Lake Formation Resource Registration

- `lakeformation:DeregisterResource`

## Deregister Redshift from AWS Glue Data Catalog

CLI
You can use `modify-lakehouse-configuration` command to deregister your cluster from AWS Glue Data Catalog, if you have IdC provider associated with your cluster, it will put
the IdC provider in the cluster to disabled mode.

```
aws redshift modify-lakehouse-configuration \
--cluster-identifier 'redshift-cluster' \
--lakehouse-registration Deregister
```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the provisioned cluster that you want to de-register and select it.
3. From the cluster’s details page, select **Deregister from AWS Glue Data Catalog**
   from the **Actions** drop-down menu and choose **Deregister**.

## Deregister Redshift Serverless namespace from AWS Glue Data Catalog

CLI
You can use `update-lakehouse-configuration` command to deregister your Redshift Serverless namespace from AWS Glue Data Catalog,
if you have IdC provider associated with your cluster, it will put the IdC provider in the cluster to disabled mode.

```
aws redshift modify-lakehouse-configuration \
--cluster-identifier 'redshift-cluster' \
--lakehouse-registration Deregister
```

Console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to serverless namespace cluster that you want to de-register and select it.
3. From the cluster’s details page, select **Deregister from AWS Glue Data Catalog**
   from the **Actions** drop-down menu and choose **Deregister**.
