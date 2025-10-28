# Run interactive workloads with EMR Serverless through

EMR Studio

With EMR Serverless interactive applications, run interactive workloads for
Spark with EMR Serverless using notebooks that are hosted in EMR Studio.

## Overview

An _interactive application_ is an EMR Serverless application that has
interactive capabilities enabled. With Amazon EMR Serverless interactive applications, you can
execute interactive workloads with Jupyter notebooks that are managed in Amazon EMR Studio. This
helps data engineers, data scientists, and data analysts use EMR Studio to run interactive
analytics with datasets in data stores such as Amazon S3 and Amazon DynamoDB.

Use cases for interactive applications in EMR Serverless include the following:

- Data engineers use the IDE experience in EMR Studio to create an ETL script. The
  script ingests data from on-premises, transforms the data for analysis, and stores the
  data in Amazon S3.
- Data scientists use notebooks to explore datasets and train machine-learning (ML)
  models to detect anomalies in the datasets.
- Data analysts explore datasets and create scripts that generate daily reports to
  update applications like business dashboards.

## Prerequisites

To use interactive workloads with EMR Serverless, meet the following
requirements:

- EMR Serverless interactive applications are supported with Amazon EMR 6.14.0 and
  higher.
- To access your interactive application, execute the workloads that you submit, and run
  interactive notebooks from EMR Studio, you need specific permissions and roles. For
  more information, refer to [Required permissions for interactive
  workloads](#interactive-permissions "#interactive-permissions").

## Required permissions for interactive

workloads

In addition to the basic [permissions that are required to
access EMR Serverless](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam"), configure additional permissions for your IAM
identity or role:

**To access your interactive application**

Set up user and Workspace permissions for EMR Studio. For more information, refer to
[Configure
EMR Studio user permissions](../ManagementGuide/emr-studio-user-permissions.md "../ManagementGuide/emr-studio-user-permissions.md") in the
_Amazon EMR Management Guide_.

**To execute the workloads that you submit with EMR Serverless**

Set up a job runtime role. For more information, refer to [Create a job runtime role](getting-started.md#gs-runtime-role "getting-started.md#gs-runtime-role").

**To run the interactive notebooks from EMR Studio**

Add the following additional permissions to the IAM policy for the Studio
users:

- **`emr-serverless:AccessInteractiveEndpoints`** - Grants
  permission to access and connect to the interactive application that you specify as
  `Resource`. This permission is required to attach to an EMR Serverless
  application from an EMR Studio Workspace.
- **`iam:PassRole`** - Grants permission
  to access the IAM execution role that you plan to use when you attach to an
  application. The appropriate `PassRole`permission is required to attach
  to an EMR Serverless application from an EMR Studio Workspace.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EMRServerlessInteractiveAccess",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:AccessInteractiveEndpoints"
 ],
 "Resource": [
 "arn:aws:emr-serverless:*:123456789012:/applications/*"
 ]
 },
 {
 "Sid": "EMRServerlessRuntimeRoleAccess",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/EMRServerlessInteractiveRole"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "emr-serverless.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Configuring interactive applications

Use the following high-level steps to create an EMR Serverless application with
interactive capabilities from Amazon EMR Studio in the AWS Management Console.

1. Follow the steps in [Getting started with Amazon EMR Serverless](getting-started.md "getting-started.md")
   to create an application.
2. Then, launch a workspace from EMR Studio and attach to an EMR Serverless
   application as a compute option. For more information, refer to the **Interactive workload** tab in Step 2 of the [EMR Serverless Getting Started](getting-started.md#gs-job-run-console "getting-started.md#gs-job-run-console") documentation.

When you attach an application to a Studio Workspace, the application start triggers
automatically if it's not already running. You can also pre-start the application and keep it
ready before you attach it to the Workspace.

## Considerations with interactive

applications

- EMR Serverless interactive applications are supported with Amazon EMR 6.14.0 and
  higher.
- EMR Studio is the only client that is integrated with EMR Serverless interactive
  applications. The following EMR Studio capabilities aren't supported with
  EMR Serverless interactive applications: Workspace collaboration, SQL Explorer,
  and programmatic execution of notebooks.
- Interactive applications are only supported for Spark engine.
- Interactive applications support Python 3, PySpark and Spark Scala kernels.
- You can run up to 25 concurrent notebooks on a single interactive application.
- There isn't an endpoint or API interface that supports self-hosted Jupyter notebooks
  with interactive applications.
- For an optimized startup experience, we suggest that you configure pre-initialized
  capacity for drivers and executors, and that you pre-start your application. When you
  pre-start the application, you ensure that it's ready when you want to attach it to your
  Workspace.

```
aws emr-serverless start-application \
--application-id `your-application-id`
```

- By default, `autoStopConfig` is enabled for applications. This shuts down
  the application after 30 minutes of idle time. You can change this configuration as
  part of your `create-application` or `update-application`
  request.
- When using an interactive application, we suggest that you configure a pre-intialized capacity
  of kernels, drivers, and executors to run your notebooks. Each Spark interactive session requires
  one kernel and one driver, so EMR Serverless maintains a pre-initialized kernel worker for every
  pre-initialized driver. By default, EMR Serverless maintains a pre-initialized capacity of one kernel worker
  throughout the entire application even if you don't specify any pre-initialized capacity for drivers.
  Each kernel worker uses 4 vCPU and 16 GB of memory. For current pricing information, refer to the [Amazon EMR Pricing](https://aws.amazon.com/emr/pricing/ "https://aws.amazon.com/emr/pricing/") page.
- You must have sufficient vCPU service quota in your AWS account to run interactive
  workloads. If you don't run Lake Formation-enabled workloads, we suggest at least 24 vCPU. If you do,
  we suggest at least 28 vCPU.
- EMR Serverless automatically terminates the kernels from the notebooks if they have been idle for more than 60 minutes. EMR Serverless
  calculates the kernel idle time from the last activity completed during the notebook session. You can't currently modify
  the kernel idle timeout setting.
- To enable Lake Formation with interactive workloads, set the configuration `spark.emr-serverless.lakeformation.enabled`
  to `true` under the `spark-defaults` classification in the `runtime-configuration`
  object when you [create an EMR Serverless application](getting-started.md "getting-started.md").
  To learn more, refer to
  [Enabling Lake Formation in Amazon EMR](emr-serverless-lf-enable.md#emr-serverless-lf-enable-config "emr-serverless-lf-enable.md#emr-serverless-lf-enable-config").
