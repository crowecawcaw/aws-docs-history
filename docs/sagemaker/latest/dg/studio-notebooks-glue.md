# Data preparation using AWS Glue interactive

sessions

[AWS Glue
interactive sessions](../../../glue/latest/dg/interactive-sessions-overview.md "../../../glue/latest/dg/interactive-sessions-overview.md") is a serverless service that you can enlist to collect,
transform, clean, and prepare data for storage in your data lakes and data pipelines.
AWS Glue interactive sessions provides an on-demand, serverless Apache Spark
runtime environment that you can initialize in seconds on a dedicated Data Processing Unit
(DPU) without having to provision and manage complex compute cluster
infrastructure. After initialization, you can browse the AWS Glue data
catalog, run large queries, access data governed by AWS Lake Formation, and interactively analyze and
prepare data using Spark, right in your Studio or Studio Classic notebooks. You can then
use the prepared data to train, tune, and deploy models using the purpose-built ML tools
within SageMaker Studio or Studio Classic. You should consider AWS Glue Interactive
Sessions for your data preparation workloads when you want a serverless Spark service with
moderate control of configurability and flexibility.

You can initiate an AWS Glue interactive session by starting a JupyterLab notebook in
Studio or Studio Classic. When starting your notebook, choose the built-in `Glue
 PySpark and Ray` or `Glue Spark` kernel. This automatically starts an
interactive, serverless Spark session. You do not need to provision or manage any compute
cluster or infrastructure. After initialization, you can explore and interact with your data
from within your Studio or Studio Classic notebooks.

Before starting your AWS Glue interactive session in Studio or Studio Classic, you need to
set the appropriate roles and policies. Additionally, you may need to provide access to
additional resources, such as a storage Amazon S3 bucket. For more information about required
IAM policies, see [Permissions for AWS Glue interactive sessions in
Studio or Studio Classic](getting-started-glue-sm.md#glue-sm-iam "getting-started-glue-sm.md#glue-sm-iam").

Studio and Studio Classic provide a default configuration for your AWS Glue interactive
session, however, you can use AWS Glue’s full catalog of Jupyter magic commands to further
customize your environment. For information about the default and additional Jupyter magics
that you can use in your AWS Glue interactive session, see [Configure your AWS Glue interactive session in
Studio or Studio Classic](getting-started-glue-sm.md#glue-sm-magics "getting-started-glue-sm.md#glue-sm-magics").

- For Studio Classic users initiating an AWS Glue interactive session, they can select from
  the following images and kernels:
  - Images: `SparkAnalytics 1.0`, `SparkAnalytics
2.0`
  - Kernel: `Glue Python [PySpark and Ray]` and `Glue
Spark`

- For Studio users, use the default [SageMaker Distribution
  image](https://github.com/aws/sagemaker-distribution "https://github.com/aws/sagemaker-distribution") and select a `Glue Python [PySpark and Ray]` or a
  `Glue Spark` kernel.
