Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Deregistering Amazon Redshift clusters and namespaces from the AWS Glue Data Catalog

You can deregister a provisioned cluster or serverless namespace from the AWS Glue Data Catalog using the Amazon Redshift console or the AWS CLI.
Data warehouses that you deregister from the AWS Glue Data Catalog are only removed from the AWS Glue Data Catalog itself.
The warehouses remain part of your Amazon Redshift account. Additionally, the catalog remains in AWS Glue and must be manually removed.
When you remove the catalog from AWS Glue, the managed workgroup associated with it is also removed.

Deregistering using the Amazon Redshift console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the serverless namespace or provisioned cluster that you want to deregister and select it.
3. From the namespace or cluster’s details page, select **Deregister from AWS Glue Data Catalog**
   from the **Actions** drop-down menu. This option only appears if you’ve chosen a data warehouse
   that’s already been registered to the AWS Glue Data Catalog.
4. Enter the account ID that owns the catalog holding your cluster or namespace and choose **Deregister**.

Deregistering using the AWS CLI
To deregister a cluster or namespace from the AWS Glue Data Catalog using the AWS CLI,
use the `deregister-namespace` command with the following options:

- `namespace-identifier`: An object with the unique identifier of the cluster or namespace you’re deregistering.
  This object is different depending on whether you’re deregistering a provisioned cluster
  or a serverless namespace. Consider the following:
  - For provisioned clusters, you provide a `ProvisionedIdentifier` object, which
    contains a `ClusterIdentifier` object with the unique identifier of the cluster you’re deregistering.
  - or serverless namespaces, you provide a `ServerlessIdentifier` object, which contains a
    `NamespaceIdentifier` object with the unique identifier of the namespace you’re deregistering,
    as well as a `WorkgroupIdentifier` object with the unique identifier of the workgroup associated with that namespace.

- `consumer-identifiers`:
  An array with a single element, containing the unique identifier of the account you’re deregistering the cluster or namespace from.

The following example deregisters the `mySampleNamespace` serverless namespace from the account ID `012345678910`.

```
aws redshift deregister-namespace /
--namespace-identifier {ServerlessIdentifier: {NamespaceIdentifer: mySampleNamespace, WorkgroupIdentifier: mySampleWorkgroup}} /
--consumer-identifiers [012345678910]
```
