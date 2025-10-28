Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Registering Amazon Redshift clusters and namespaces to the AWS Glue Data Catalog

You can add Amazon Redshift provisioned clusters and serverless namespaces to the AWS Glue Data Catalog to access them using the Apache Iceberg REST API.
You do this by registering the Amazon Redshift data warehouse to the AWS Glue Data Catalog using the Amazon Redshift console or AWS CLI,
then creating a Amazon Redshift federated catalog for the warehouse using AWS Lake Formation.

Amazon Redshift data warehouses registered to the Data Catalog act as producer datashares.
Changes that you make to clusters or serverless namespaces from their catalogs are
reflected in the cluster or namespace in Redshift, and vice versa.

Registering using the Amazon Redshift console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Navigate to the serverless namespace or provisioned cluster that you want to register and select it.
3. From the namespace or cluster’s details page, select **Register to AWS Glue Data Catalog** from the **Actions** drop-down menu.
4. Enter the destination account ID that you want to register the namespace or cluster to and choose **Register**.
5. If you’re registering from your account to the same account in AWS Glue,
   you’ll be taken directly to the AWS Lake Formation console to finish the process.
   If you’re registering to a different account, a link appears that takes you to Lake Formation.

Registering using the AWS CLI
To register a cluster or namespace to the AWS Glue Data Catalog using the AWS CLI,
use the `register-namespace` command with the following options:

- `namespace-identifier`: An object with the unique identifier of the cluster or namespace you’re registering.
  This object is different depending on whether you’re registering a provisioned cluster
  or a serverless namespace. Consider the following:
  - For provisioned clusters, you provide a `ProvisionedIdentifier` object, which
    contains a `ClusterIdentifier` object with the unique identifier of the cluster you’re registering.
  - or serverless namespaces, you provide a `ServerlessIdentifier` object, which contains a
    `NamespaceIdentifier` object with the unique identifier of the namespace you’re registering,
    as well as a `WorkgroupIdentifier` object with the unique identifier of the workgroup associated with that namespace.

- `consumer-identifiers`:
  An array with a single element, containing the unique identifier of the account you’re registering the cluster or namespace to.

The following example registers the `mySampleNamespace` serverless namespace to the account ID `012345678910`.

```
aws redshift register-namespace /
--namespace-identifier {ServerlessIdentifier: {NamespaceIdentifer: mySampleNamespace, WorkgroupIdentifier: mySampleWorkgroup}} /
--consumer-identifiers [012345678910]
```
