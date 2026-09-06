

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Disabling AWS IAM Identity Center propagation
<a name="federated-permissions-offboarding"></a>

Before you can disable AWS IAM Identity Center propagation, you must have Amazon Redshift Cluster or Amazon Redshift Serverless Namespace has registered with AWS Glue Data Catalog and associated with a Lakehouse Redshift IdC Application. An Amazon Redshift Serverless namespace requires a workgroup attached to perform the related operations.

## Disable AWS IAM Identity Center Identity Propagation for Amazon Redshift provisioned clusters
<a name="federated-permissions-offboarding-clusters"></a>

When disabling the AWS IAM Identity Center Identity Propagation for your Amazon Redshift Provisioned Clusters, the Lakehouse Redshift IdC Application attached to it will be marked as disabled in the cluster.

------
#### [ CLI ]

You can use `modify-lakehouse-configuration` command to disable IdC identity propagation for your clusters with Redshift Federated Permissions, note it doesn’t delete the IdC provider from your cluster but put them into disabled mode.

```
aws redshift modify-lakehouse-configuration \
    --cluster-identifier 'redshift-cluster' \
    --lakehouse-idc-registration Disassociate \
```

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. Navigate to the provisioned cluster that you want to edit registration for and select it.

1. From the cluster’s details page, select **Edit AWS Glue Data Catalog registration** from the **Actions** drop-down menu. 

1. Select **Disable** from the Amazon Redshift federated permissions using AWS IAM Identity Center drop-down to disassociate IDC application and choose **Save changes**.

------

## Disable AWS IAM Identity Center Identity Propagation for Amazon Redshift Serverless namespaces
<a name="federated-permissions-offboarding-namespace"></a>

------
#### [ CLI ]

You can use `modify-lakehouse-configuration` command to disable IdC identity propagation for your namespace with Redshift Federated Permissions, note it doesn’t delete the IdC provider from your cluster but put them into disabled mode.

```
aws redshift-serverless update-lakehouse-configuration \
--namespace-name 'serverless-namespace-name' \
--lakehouse-idc-registration Disassociate \
```

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. Navigate to the serverless namespace that you want to edit registration for and select it.

1. From the namespace’s details page, select **Edit AWS Glue Data Catalog registration** from the **Actions** drop-down menu. 

1. Select **Disable** from the Amazon Redshift federated permissions using AWS IAM Identity Center drop-down to disassociate IDC application and choose **Save changes**.

------