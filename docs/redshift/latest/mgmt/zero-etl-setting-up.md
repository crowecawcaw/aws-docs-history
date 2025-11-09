Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Turn on case sensitivity for your

data warehouse

You can attach a parameter group and enable case sensitivity for a provisioned cluster
during creation. However, you can update a serverless workgroup through the AWS Command Line Interface
(AWS CLI) only after it's been created. This is required to support the case sensitivity
of source tables and columns. The `enable_case_sensitive_identifier` is a
configuration value that determines whether name identifiers of databases, tables, and
columns are case sensitive. This parameter must be turned on to create zero-ETL integrations in the
data warehouse. For more information, see [enable_case_sensitive_identifier](../dg/r_enable_case_sensitive_identifier.md "../dg/r_enable_case_sensitive_identifier.md").

For Amazon Redshift Serverless – [Turn on case sensitivity for Amazon Redshift Serverless
using the AWS CLI](#case-sensitivity-serverless-cli "#case-sensitivity-serverless-cli"). Note that you can turn on case
sensitivity for Amazon Redshift Serverless only from the AWS CLI.

For Amazon Redshift provisioned clusters, enable case sensitivity for your target cluster using one
of the following topics:

- [Turn on case sensitivity for Amazon Redshift
  provisioned clusters using the Amazon Redshift console](#case-sensitivity-cluster-console "#case-sensitivity-cluster-console")
- [Turn on case sensitivity for Amazon Redshift
  provisioned clusters using the AWS CLI](#case-sensitivity-cluster-cli "#case-sensitivity-cluster-cli")

## Turn on case sensitivity for Amazon Redshift Serverless

using the AWS CLI

Run the following AWS CLI command to turn on case sensitivity for your workgroup.

```
aws redshift-serverless update-workgroup \
        --workgroup-name `target-workgroup` \
        --config-parameters parameterKey=enable_case_sensitive_identifier,parameterValue=true
```

Wait for the workgroup status to be `Active` before proceeding to the next
step.

## Turn on case sensitivity for Amazon Redshift

provisioned clusters using the Amazon Redshift console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. In the left navigation pane, choose **Provisioned clusters
   dashboard**.
3. Choose the provisioned cluster that you want to replicate data into.
4. In the left navigation pane, choose **Configurations** >
   **Workload management**.
5. On the workload management page, choose the parameter group.
6. Choose the **Parameters** tab.
7. Choose **Edit parameters**, then change
   **enable_case_sensitive_identifier** to
   **true**.
8. Then, choose **Save**.

## Turn on case sensitivity for Amazon Redshift

provisioned clusters using the AWS CLI

1. Because you can't edit the default parameter group, from your terminal
   program, run the following AWS CLI command to create a custom parameter group. Later,
   you will associate it with the provisioned cluster.

```
aws redshift create-cluster-parameter-group \
    --parameter-group-name `zero-etl-params` \
    --parameter-group-family redshift-2.0 \
    --description "Param group for zero-ETL integrations"
```

2. Run the following AWS CLI command to turn on case sensitivity for the parameter
   group.

```
aws redshift modify-cluster-parameter-group \
    --parameter-group-name `zero-etl-params` \
    --parameters ParameterName=enable_case_sensitive_identifier,ParameterValue=true
```

3. Run the following command to associate the parameter group with the
   cluster.

```
aws redshift modify-cluster \
    --cluster-identifier `target-cluster` \
    --cluster-parameter-group-name `zero-etl-params`
```

4. Wait for the provisioned cluster to be available. You can check the status of the
   cluster by using the `describe-cluster` command. Then, run the following
   command to reboot the cluster.

```
aws redshift reboot-cluster \
    --cluster-identifier `target-cluster`
```
