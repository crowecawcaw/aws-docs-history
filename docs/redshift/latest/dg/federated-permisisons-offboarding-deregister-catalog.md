

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Deregister from Amazon Redshift federated permissions
<a name="federated-permisisons-offboarding-deregister-catalog"></a>

## IAM Policy Requirements for Amazon Redshift Federated Permissions Deregistration
<a name="federated-permisisons-offboarding-deregister-catalog-iam-reqs"></a>

 To deregister your cluster or serverless namespace, below IAM permissions are required. 

For Redshift Provisioned Clusters
+ `redshift:ModifyLakehouseConfiguration`
+ `redshift:DeregisterNamespace`

For Redshift Serverless
+ `redshift-serverless:UpdateLakehouseConfiguration`
+ `redshift:DeregisterNamespace`

If you are deregistering a warehouse that was registered with the AWS Glue Data Catalog, the following additional permissions are required:

For AWS Glue Data Catalog Integration
+ `glue:DeleteCatalog`
+ `glue:GetCatalog`

For Lake Formation Resource Registration
+ `lakeformation:DeregisterResource`

## Deregister Redshift cluster
<a name="federated-permisisons-offboarding-deregister-catalog-provisioned"></a>

------
#### [ CLI ]

Use the `modify-lakehouse-configuration` command to deregister your cluster. If you have an IdC provider associated with your cluster, it is put into disabled mode.

```
aws redshift modify-lakehouse-configuration \
--cluster-identifier 'redshift-cluster' \
--lakehouse-registration Deregister
```

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. Navigate to the provisioned cluster that you want to de-register and select it.

1. From the cluster's details page, select **Deregister from Amazon Redshift multi-warehouse** from the **Actions** drop-down menu and choose **Deregister**.

------

## Deregister Redshift Serverless namespace
<a name="federated-permisisons-offboarding-deregister-catalog-namespace"></a>

------
#### [ CLI ]

Use the `update-lakehouse-configuration` command to deregister your Redshift Serverless namespace. If you have an IdC provider associated with your namespace, it is put into disabled mode.

```
aws redshift-serverless update-lakehouse-configuration \
--namespace-name 'serverless-namespace-name' \
--lakehouse-registration Deregister
```

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. Navigate to serverless namespace cluster that you want to de-register and select it.

1. From the cluster's details page, select **Deregister from Amazon Redshift multi-warehouse** from the **Actions** drop-down menu and choose **Deregister**.

------