# Amazon EMR Studio

Amazon EMR Studio is a web-based integrated development environment (IDE) for fully managed
Jupyter notebooks that run on Amazon EMR clusters. You can set up an EMR Studio for your team to
develop, visualize, and debug applications written in R, Python, Scala, and PySpark.
EMR Studio is integrated with AWS Identity and Access Management (IAM) and IAM Identity Center so users can log in using
their corporate credentials.

You can create an EMR Studio at no cost. Applicable charges for Amazon S3
storage and for Amazon EMR clusters apply when you use EMR Studio. For product details and
highlights, see the service page for [Amazon EMR Studio](https://aws.amazon.com/emr/features/studio/ "https://aws.amazon.com/emr/features/studio/").

## Key features of EMR Studio

Amazon EMR Studio provides the following features:

- Authenticate users with AWS Identity and Access Management (IAM), or with AWS IAM Identity Center with or without
  [trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation.md "../../../singlesignon/latest/userguide/trustedidentitypropagation.md") and
  your enterprise identity provider.
- Access and launch Amazon EMR clusters on-demand to run Jupyter Notebook jobs.
- Connect to Amazon EMR on EKS clusters to submit work as job runs.
- Explore and save example notebooks. For more information about example notebooks, see
  the [EMR Studio Notebook examples GitHub repository](https://github.com/aws-samples/emr-studio-notebook-examples "https://github.com/aws-samples/emr-studio-notebook-examples").
- Analyze data using Python, PySpark, Spark Scala, Spark R, or SparkSQL, and install
  custom kernels and libraries.
- Collaborate in real time with other users in the same Workspace. For more
  information, see [Configure Workspace
  collaboration in EMR Studio](emr-studio-workspace-collaboration.md "emr-studio-workspace-collaboration.md").
- Use the EMR Studio SQL Explorer to browse your data catalog, run SQL queries, and
  download results before you work with the data in a notebook.
- Run parameterized notebooks as part of scheduled workflows with an orchestration tool
  such as Apache Airflow or Amazon Managed Workflows for Apache Airflow. For more
  information, see [Orchestrating analytics jobs on EMR Notebooks using MWAA](https://aws.amazon.com/blogs/big-data/orchestrating-analytics-jobs-on-amazon-emr-notebooks-using-amazon-mwaa/ "https://aws.amazon.com/blogs/big-data/orchestrating-analytics-jobs-on-amazon-emr-notebooks-using-amazon-mwaa/") in the AWS Big Data
  Blog.
- Link code repositories such as GitHub and BitBucket.
- Track and debug jobs using the Spark History Server, Tez UI, or YARN timeline server.

EMR Studio is HIPAA eligible and is certified under HITRUST CSF and SOC 2. For
more information about HIPAA compliance for AWS services, see [https://aws.amazon.com/compliance/hipaa-compliance/](https://aws.amazon.com/compliance/hipaa-compliance/ "https://aws.amazon.com/compliance/hipaa-compliance/"). To learn more about HITRUST CSF
compliance for AWS services, see [https://aws.amazon.com/compliance/hitrust/](https://aws.amazon.com/compliance/hitrust/ "https://aws.amazon.com/compliance/hitrust/").

EMR Studio is also FedRamp compliant. For more information about compliance programs Amazon EMR conforms with, see [Compliance validation for Amazon EMR](emr-compliance.md "emr-compliance.md"). For more information
about additional compliance programs for AWS services, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").

## Amazon SageMaker Unified Studio integrated development environment

Amazon SageMaker Unified Studio provides an integrated development environment (IDE) for your [Jupyter notebooks](../../../sagemaker-unified-studio/latest/userguide/jupyterlab.md "../../../sagemaker-unified-studio/latest/userguide/jupyterlab.md") that runs
on [Amazon EMR on EC2 clusters](../../../sagemaker-unified-studio/latest/userguide/managing-emr-on-ec2.md "../../../sagemaker-unified-studio/latest/userguide/managing-emr-on-ec2.md") or
using [EMR Serverless compute connections](../../../sagemaker-unified-studio/latest/userguide/adding-deleting-emr-serverless.md "../../../sagemaker-unified-studio/latest/userguide/adding-deleting-emr-serverless.md"). By combining the power of Amazon EMR with
the end-to-end workflow capabilities of Amazon SageMaker Unified Studio, teams can streamline data preparation, pipeline development, and ML experimentation in a single environment. Amazon EMR in SageMaker
revolutionizes big data processing by supporting open-source frameworks like Apache Spark, Trino, and Apache Flink. Eliminate infrastructure management complexities while
scaling analytics workloads effortlessly. To learn more, see [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/").

## Amazon EMR Studio feature history

This table lists updates to the Amazon EMR managed scaling capability.

| Release date          | Capability                                                                                                                                                |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **January 5, 2024**   | Added support for EMR Studio in AWS GovCloud (US-East) and AWS GovCloud (US-West).                                                                        |
| **November 26, 2023** | Added support for trusted identity propagation for EMR Studio with IAM Identity Center authentication.                                                    |
| **October 26, 2023**  | Added ability to create an EMR Serverless application with interactive capability.                                                                        |
| **February 28, 2023** | Added AWS KMS customer-managed key support for application log storage for EMR Serverless applications.                                                   |
| **February 23, 2023** | Added one-click IAM role creation for EMR Serverless job submission. Added ECR lookup for when you select a custom image for EMR Serverless applications. |
| **January 27, 2023**  | Headless execution notebooks can track the progress of each cell execution with `%execute_notebook` magic.                                                |
| **January 23, 2023**  | Persistent application have been optimized for faster launch times.                                                                                       |
