# Prepare data using EMR Serverless

Beginning with [SageMaker distribution image](sagemaker-distribution.md "sagemaker-distribution.md")
version `1.10`, Amazon SageMaker Studio integrates with EMR Serverless. Within
JupyterLab notebooks in SageMaker Studio, data scientists and data engineers can discover
and connect to EMR Serverless applications, then interactively explore, visualize, and
prepare large-scale Apache Spark or Apache Hive workloads. This integration allows to
perform interactive data preprocessing at scale in preparation for ML model training and
deployment.

Specifically, the updated version of the [`sagemaker-studio-analytics-extension`](https://pypi.org/project/sagemaker-studio-analytics-extension/ "https://pypi.org/project/sagemaker-studio-analytics-extension/") in [SageMaker AI
distribution](https://github.com/aws/sagemaker-distribution/tree/main/build_artifacts/v1 "https://github.com/aws/sagemaker-distribution/tree/main/build_artifacts/v1") image version `1.10` leverages the integration between
Apache Livy and EMR Serverless, allowing the connection to an Apache Livy endpoint through
JupyterLab notebooks. This section assumes prior knowledge of [EMR Serverless interactive
applications](../../../EMR-Serverless-UserGuide/interactive-workloads.md "../../../EMR-Serverless-UserGuide/interactive-workloads.md").

###### Important

When using Studio, you can only discover and connect to EMR Serverless
applications for JupyterLab applications that are launched from private spaces. Ensure
that the EMR Serverless applications are located in the same AWS region as your
Studio environment.

## Prerequisites

Before you get started running interactive workloads with EMR Serverless from your
JupyterLab notebooks, make sure you meet the following prerequisites:

1. Your JupyterLab space must use a SageMaker Distribution image version
   `1.10` or higher.
2. Create an EMR Serverless interactive application with Amazon EMR version
   `6.14.0` or higher. You can create an EMR Serverless application
   from the Studio user interface by following the steps in [Create EMR Serverless applications
   from Studio](create-emr-serverless-application.md "create-emr-serverless-application.md").

###### Note

For the simplest setup, you can create your EMR Serverless application in
the Studio UI without changing any default settings for the
**Virtual private cloud (VPC)** option. This allows the
application to be created within your domain VPC without requiring any
networking configuration. In this case, you can skip the following
networking setup step. 3. Review the networking and security requirements in [Configure network access for your Amazon EMR cluster](studio-notebooks-emr-networking.md "studio-notebooks-emr-networking.md"). Specifically, ensure that
you:

    * Establish a VPC peering connection between your Studio account
     and your EMR Serverless account.
    * Add routes to the private subnet route tables in both accounts.
    * Set up the security group attached to your Studio domain to allow
     outbound traffic, and configure the security group of the VPC where you
     plan to run the EMR Serverless applications to allow inbound TCP
     traffic from the Studio instance's security group.

4. To access your interactive applications on EMR Serverless and run workloads
   submitted from your JupyterLab notebooks in SageMaker Studio, you must assign
   specific permissions and roles. Refer to the [Set up the permissions to enable
   listing and launching Amazon EMR applications from SageMaker Studio](studio-emr-serverless-permissions.md "studio-emr-serverless-permissions.md") section for details on
   the necessary roles and permissions.

###### List of topics

- [Set up the permissions to enable
  listing and launching Amazon EMR applications from SageMaker Studio](studio-emr-serverless-permissions.md "studio-emr-serverless-permissions.md")
- [Create EMR Serverless applications
  from Studio](create-emr-serverless-application.md "create-emr-serverless-application.md")
- [Connect to an EMR Serverless
  application from Studio](connect-emr-serverless-application.md "connect-emr-serverless-application.md")
- [Stop or delete an EMR Serverless
  application from the Studio UI](terminate-emr-serverless-application.md "terminate-emr-serverless-application.md")
