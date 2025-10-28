# Create an Amazon SageMaker Notebook Instance for the

tutorial

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

An Amazon SageMaker notebook instance is a fully-managed machine learning (ML) Amazon Elastic Compute Cloud (Amazon EC2)
compute instance. An Amazon SageMaker notebook instance runs the Jupyter Notebook application. Use
the notebook instance to create and manage Jupyter notebooks for preprocessing data, train
ML models, and deploy ML models.

###### To create a SageMaker notebook instance

![Animated screenshot that shows how to create a SageMaker notebook instance.](/images/sagemaker/latest/dg/images/get-started-ni/gs-ni-create-instance.gif)

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **Notebook instances**, and then choose **Create
   notebook instance**.
3. On the **Create notebook instance** page, provide the following
   information (if a field is not mentioned, leave the default values):
   1. For **Notebook instance name**, type a name for your
      notebook instance.
   2. For **Notebook Instance type**, choose
      `ml.t2.medium`. This is the least expensive instance type
      that notebook instances support, and is enough for this exercise. If a
      `ml.t2.medium` instance type isn't available in your current
      AWS Region, choose `ml.t3.medium`.
   3. For **Platform Identifier**, choose a platform type to create the notebook
      instance on. This platform type defines the Operating System and the
      JupyterLab version that your notebook instance is created with. The latest and recommended version is
      `notebook-al2023-v1`, for an Amazon Linux 2023 notebook instance. For information about platform identifier types, see
      [AL2023 notebook instances](nbi-al2023.md "nbi-al2023.md") and
      [Amazon Linux 2 notebook instances](nbi-al2.md "nbi-al2.md"). For information about JupyterLab versions,
      see [JupyterLab versioning](nbi-jl.md "nbi-jl.md").
   4. For **IAM role**, choose **Create a new
      role**, and then choose **Create role**. This
      IAM role automatically gets permissions to access any S3 bucket that has
      `sagemaker` in the name. It gets these permissions through
      the `AmazonSageMakerFullAccess` policy, which SageMaker AI attaches to
      the role.

   ###### Note

   If you want to grant the IAM role permission to access S3 buckets without
   `sagemaker` in the name, you need to attach the
   `S3FullAccess` policy. You can also limit the permissions
   to specific S3 buckets to the IAM role. For more information and
   examples of adding bucket policies to the IAM role, see [Bucket
   Policy Examples](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md"). 5. Choose **Create notebook instance**.

   In a few minutes, SageMaker AI launches a notebook instance and attaches a 5 GB of
   Amazon EBS storage volume to it. The notebook instance has a preconfigured
   Jupyter notebook server, SageMaker AI and AWS SDK libraries, and a set of Anaconda
   libraries.

   For more information about creating a SageMaker notebook instance, see
   [Create a Notebook Instance](howitworks-create-ws.md "howitworks-create-ws.md").

## (Optional) Change SageMaker Notebook Instance Settings

To change the ML compute instance type or the size of the Amazon EBS storage of a SageMaker AI
notebook instance, edit the notebook instance settings.

###### To change and update the SageMaker Notebook instance type and the EBS volume

1. On the **Notebook instances** page in the SageMaker AI console, choose your notebook
   instance.
2. Choose **Actions**, choose **Stop**, and then wait until the
   notebook instance fully stops.
3. After the notebook instance status changes to **Stopped**, choose
   **Actions**, and then choose **Update
   settings**.

![Animated screenshot that shows how to update SageMaker notebook instance settings.](/images/sagemaker/latest/dg/images/get-started-ni/gs-ni-update-instance.gif)

    1. For **Notebook instance type**, choose a different ML instance type.
    2. For **Volume size in GB**, type a different integer to specify a new EBS
     volume size.


    ###### Note

    EBS storage volumes are encrypted, so SageMaker AI can't determine the amount of available free space
     on the volume. Because of this, you can increase the volume size
     when you update a notebook instance, but you can't decrease the
     volume size. If you want to decrease the size of the ML storage
     volume in use, create a new notebook instance with the desired size.

4. At the bottom of the page, choose **Update notebook
   instance**.
5. When the update is complete, **Start** the notebook instance with the new
   settings.

For more information about updating SageMaker notebook instance settings, see [Update a Notebook
Instance](nbi-update.md "nbi-update.md").

## (Optional) Advanced Settings for SageMaker Notebook Instances

The following tutorial video shows how to set up and use SageMaker notebook instances
through the SageMaker AI console. It includes advanced options, such as SageMaker AI lifecycle
configuration and importing GitHub repositories. (Length: 26:04)

For complete documentation about SageMaker notebook instance, see [Use Amazon SageMaker
notebook Instances](nbi.md "nbi.md").
