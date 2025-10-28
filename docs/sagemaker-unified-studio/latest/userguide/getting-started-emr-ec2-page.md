# Get started adding on-demand Amazon EMR on EC2 instances

## Overview

[Amazon EMR](../../../emr/latest/ManagementGuide/emr-what-is-emr.md "../../../emr/latest/ManagementGuide/emr-what-is-emr.md") on EC2 is a managed big data platform that simplifies running distributed data processing frameworks like Apache Spark, Hadoop, and Hive on [Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/concepts.md "../../../AWSEC2/latest/UserGuide/concepts.md"). Amazon EMR handles the complexities of cluster provisioning, configuration, and scaling, allowing you to focus on your data processing tasks. For more details on Amazon EMR, visit the [Amazon EMR webpage](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/").

The Amazon EMR on EC2 integration with Amazon SageMaker Unified Studio streamlines your data analytics workflow, giving you a unified data and compute experience. This integration lets you easily access and create Amazon EMR clusters alongside other data tools in a single interface. You can organize Amazon EMR resources within Amazon SageMaker Unified Studio projects, connect Amazon EMR workloads with your data catalog, and provision clusters on-demand. With this integration, you can experiment by creating and terminating Amazon EMR clusters as needed, optimizing costs while maintaining a cohesive data experience.

With the help of this getting started guide you will be able to configure Amazon EMR cluster settings for EC2 deployment and launch Amazon EMR clusters.

## Prerequisites

You must complete the following procedure through the AWS management console to create an Amazon EMR on EC2 in an Amazon SageMaker Unified Studio project.

### Set up Amazon SageMaker Unified Studio

Before you get started with creating an Amazon EMR on EC2, you must access Amazon SageMaker Unified Studio and create a project with the **All capabilities** project profile.

1. If you haven't created an Amazon SageMaker Unified Studio domain, follow the steps in [Create a Amazon SageMaker Unified Studio domain - quick setup](../adminguide/create-domain-sagemaker-unified-studio-quick.md "../adminguide/create-domain-sagemaker-unified-studio-quick.md") .
2. To access Amazon SageMaker Unified Studio:
   1. Open the Amazon SageMaker Unified Studio console at [https://console.aws.amazon.com/sagemaker/.](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/")
   2. Choose **Studio**.
   3. Choose **Open Studio**.
   4. Sign in using your SSO or AWS credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").

3. Create a project with the **All capabilities** profile:
   1. In Amazon SageMaker Unified Studio, choose the **Projects** icon in the left sidebar.
   2. Choose **Create project**.
   3. Select the **All capabilities** project profile.
   4. Follow the prompts to complete project creation.
   5. This profile grants you access to Amazon EMR resources. For more information, see [Create a project](getting-started-create-a-project.md "getting-started-create-a-project.md").

### PEM certificate configuration

1. Create a PEM certificate, which saves your ZIP file on your local machine:
   1. Open your terminal on your local machine.
   2. The following commands demonstrate how to use [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/") to generate a self-signed X.509 certificate with a 2048-bit RSA private key. Consider changing `us-west-2` to the region you are using throughout this tutorial. Other optional subject items such as country (C), state (S), and Locale (L), are specified.

   ###### Important

   This example is a proof-of-concept demonstration only. Using self-signed certificates is not recommended and presents a potential security risk. For production systems, use a trusted certification authority (CA) to issue certificates. For more information see [Providing certificates for encrypting data in transit with Amazon EMR encryption](../../../emr/latest/ManagementGuide/emr-encryption-enable.md#emr-encryption-certificates "../../../emr/latest/ManagementGuide/emr-encryption-enable.md#emr-encryption-certificates").

   ```

   $ openssl req -x509 -newkey rsa:2048 -keyout privateKey.pem -out certificateChain.pem -days 365 -nodes -subj '/C=US/ST=Washington/L=Seattle/O=MyOrg/OU=MyDept/CN=*.us-west-2.compute.internal'
   $ cp certificateChain.pem trustedCertificates.pem
   $ zip -r -X my-certs.zip certificateChain.pem privateKey.pem trustedCertificates.pem

   ```

2. Upload the PEM certificate ZIP file to an Amazon S3 bucket:
   1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
   2. Under **General purpose buckets**, choose your amazon-sagemaker bucket.
   3. Navigate to your domain folder. For multiple domains, locate the folder matching your Domain ID. You can find your Domain ID in the **project details** tab of Amazon SageMaker Unified Studio.
   4. Choose **Create folder** and enter `certificate_location` as the folder name. You do not need to specify an encryption key during folder creation.

   ###### Note

   The name `certificate_location` is required for this folder and cannot be customized. 5. Select your new folder to open it. 6. Under **Objects**, select **Upload** and **Add files**. Select your PEM certificate ZIP file (named "my-certs.zip") from your local machine, then choose **Upload**. 7. Select the uploaded ZIP file and choose **Copy S3 URI**. You'll need this location value in step 3.

3. Specify your certificate location in Amazon SageMaker Unified Studio, following the instructions in [Specify PEM certificate for EmrOnEc2 blueprint](../adminguide/blueprints.md#enable-emr-on-ec2-blueprint "../adminguide/blueprints.md#enable-emr-on-ec2-blueprint").

## Creating your Amazon EMR cluster

1. In Amazon SageMaker Unified Studio, choose your project to enter the project overview page and select **Compute** from the navigation bar.
2. In the **Compute** panel, select the **Data processing** tab.
3. To create a new Amazon EMR on EC2 cluster choose **Add compute**.
4. In the **Add compute** modal, you can select the type of compute you would like to add to your project. Select **Create new compute resources**.
5. Select **Amazon EMR on EC2 cluster** and choose **Next**.
6. The **Add compute** dialog box allows you to specify the name of the Amazon EMR on EC2 cluster. Default settings for the Amazon EMR are fine. Choose your EMR configuration according to your choice from the prerequisites.
7. After configuring any settings if you choose, select **Add compute**. After some time, your Amazon EMR on EC2 cluster will be added to your project.
