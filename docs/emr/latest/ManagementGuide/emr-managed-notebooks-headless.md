# Sample programmatic commands for EMR Notebooks

## Overview

You can execute EMR notebooks with execution APIs from a script or from
command line. When you start, stop, list, and describe EMR notebook
executions outside of the AWS console, you can programmatically control an
EMR notebook. You can pass different parameter values to a notebook with a
parameterized notebook cell. This eliminates the need to create a copy of the
notebook for each new set of parameter values. For more information, see [Amazon EMR API
actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md").

You can schedule or batch EMR notebook executions with Amazon CloudWatch events and
AWS Lambda. For more information, see [Using AWS Lambda with
Amazon CloudWatch Events](../../../lambda/latest/dg/services-cloudwatchevents.md "../../../lambda/latest/dg/services-cloudwatchevents.md").

###### Note

EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Amazon EMR console](whats-new-in-console.md "whats-new-in-console.md").

## Role permissions for

programmatic execution

To use programmatic execution with EMR Notebooks, you must configure user
permissions with the following policies:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowExecutionActions",
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:StartNotebookExecution",
 "elasticmapreduce:DescribeNotebookExecution",
 "elasticmapreduce:ListNotebookExecutions"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AllowPassingServiceRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/EMR_Notebooks_DefaultRole"
 ]
 }
 ]
}`

```

When you programmatically execute EMR Notebooks on an EMR Notebooks cluster, you must
add these additional permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowRetrievingManagedEndpointCredentials",
 "Effect": "Allow",
 "Action": [
 "emr-containers:GetManagedEndpointSessionCredentials"
 ],
 "Resource": [
 "arn:aws:emr-containers:*:123456789012:/virtualclusters/virtual-cluster-id/endpoints/managed-endpoint-id"
 ],
 "Condition": {
 "StringEquals": {
 "emr-containers:ExecutionRoleArn": [
 "arn:aws:iam::123456789012:role/emr-on-eks-execution-role"
 ]
 }
 }
 },
 {
 "Sid": "AllowDescribingManagedEndpoint",
 "Effect": "Allow",
 "Action": [
 "emr-containers:DescribeManagedEndpoint"
 ],
 "Resource": [
 "arn:aws:emr-containers:*:123456789012:/virtualclusters/virtual-cluster-id/endpoints/managed-endpoint-id"
 ]
 }
 ]
}`

```

## Limitations with programmatic

execution

- A maximum of 100 concurrent executions are supported per AWS Region per
  account.
- An execution is terminated if it runs for more than 30 days.
- Programmatic execution of notebooks isn't supported with
  Amazon EMR Serverless interactive applications.

## Examples of programmatic

EMR notebook execution

The following sections provide several examples of programmatic
EMR notebook execution with the AWS CLI, Boto3 SDK (Python), and Ruby:

- [Notebook CLI command
  samples in EMR Studio](emr-managed-notebooks-headless-cli.md "emr-managed-notebooks-headless-cli.md")
- [Python
  samples for an EMR notebook](emr-managed-notebooks-headless-python.md "emr-managed-notebooks-headless-python.md")
- [Ruby
  samples for an EMR notebook](emr-managed-notebooks-headless-ruby.md "emr-managed-notebooks-headless-ruby.md")

You can also run parameterized notebooks as part of scheduled workflows with an
orchestration tool such as Apache Airflow or Amazon Managed Workflows for Apache
Airflow (MWAA). For more information, see [Orchestrating analytics jobs on EMR Notebooks using MWAA](https://aws.amazon.com/blogs/big-data/orchestrating-analytics-jobs-on-amazon-emr-notebooks-using-amazon-mwaa/ "https://aws.amazon.com/blogs/big-data/orchestrating-analytics-jobs-on-amazon-emr-notebooks-using-amazon-mwaa/") in the
_AWS Big Data Blog_.
