# JupyterLab administrator guide

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

This guide for administrators describes SageMaker AI JupyterLab resources, such as those from
Amazon Elastic Block Store (Amazon EBS) and Amazon Elastic Compute Cloud (Amazon EC2). The topics also show how to provide user access and
change storage size.

A SageMaker AI JupyterLab space is composed of the following resources:

- A distinct Amazon EBS volume that stores all of the data, such as the code and the
  environment variables.
- The Amazon EC2 instance used to run the space.
- The image used to run JupyterLab.

###### Note

Applications do not have access to the EBS volume of other applications. For example,
Code Editor, based on Code-OSS, Visual Studio Code - Open Source doesn't have access to the EBS volume for JupyterLab. For more information
about EBS volumes, see [Amazon Elastic Block Store (Amazon EBS)](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md").

You can use the Amazon SageMaker API to do the following:

- Change the default storage size of the EBS volume for your users.
- Change the maximum size of the EBS storage
- Specify the user settings for the application. For example, you can specify
  whether the user is using a custom image or a code repository.
- Specify the support application type.
  The default size of the Amazon EBS volume is 5 GB. You can increase the volume size to a
  maximum of 16,384 GB. If you don't do anything, your users can increase their volume size to
  100 GB. The volume size can be changed only once within a six hour period.

The kernels associated with the JupyterLab application run on the same Amazon EC2 instance
that runs JupyterLab. When you create a space, the latest version of the SageMaker Distribution
Image is used by default. For more information about SageMaker Distribution Images, see [SageMaker Studio image support policy](sagemaker-distribution.md "sagemaker-distribution.md").

###### Important

For information about updating the space to use the latest version of the SageMaker AI
Distribution Image, see [Update the SageMaker
Distribution Image](studio-updated-jl-update-distribution-image.md "studio-updated-jl-update-distribution-image.md").

The working directory of your users within the storage volume is
`/home/sagemaker-user`. If you specify your own AWS KMS key to encrypt the
volume, everything in the working directory is encrypted using your customer managed key. If you don't
specify an AWS KMS key, the data inside `/home/sagemaker-user` is encrypted with an
AWS managed key. Regardless of whether you specify an AWS KMS key, all of the data outside
of the working directory is encrypted with an AWS Managed Key.

The following sections walk you through the configurations that you need to perform as an
administrator.

###### Topics

- [Give your users access to
  spaces](studio-updated-jl-admin-guide-permissions.md "studio-updated-jl-admin-guide-permissions.md")
- [Change the default storage
  size for your JupyterLab users](studio-updated-jl-admin-guide-storage-size.md "studio-updated-jl-admin-guide-storage-size.md")
- [Lifecycle configurations with JupyterLab](jl-lcc.md "jl-lcc.md")
- [Git repos in JupyterLab](studio-updated-jl-admin-guide-git-attach.md "studio-updated-jl-admin-guide-git-attach.md")
- [Custom images](studio-updated-jl-admin-guide-custom-images.md "studio-updated-jl-admin-guide-custom-images.md")
- [Update the SageMaker
  Distribution Image](studio-updated-jl-update-distribution-image.md "studio-updated-jl-update-distribution-image.md")
- [Delete unused resources](studio-updated-jl-admin-guide-clean-up.md "studio-updated-jl-admin-guide-clean-up.md")
- [Quotas](studio-updated-jl-admin-guide-quotas.md "studio-updated-jl-admin-guide-quotas.md")
