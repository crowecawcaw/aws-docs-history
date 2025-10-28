# Amazon EC2 setup

In this section, you learn how to set up AWS Deep Learning Containers with Amazon Elastic Compute Cloud.

Complete the following steps to configure your instance:

- Create an AWS Identity and Access Management user or modify an existing user with the following policies.
  You can search for them by name in the IAM console's policy tab.

      + [AmazonECS\_FullAccess Policy](https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAmazonECS_FullAccess "https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAmazonECS_FullAccess")
      + [AmazonEC2ContainerRegistryFullAccess](https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess "https://console.aws.amazon.com/iam/home?region=us-east-1#/policies/arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess")

  For more information about creating or editing an IAM user, see [Adding and
  Removing IAM Identity Permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the IAM user guide.

- Launch an Amazon Elastic Compute Cloud instance (CPU or GPU), preferably a [Deep
  Learning Base AMI](../../../dlami/latest/devguide/overview-base.md "../../../dlami/latest/devguide/overview-base.md"). Other AMIs work, but require relevant GPU
  drivers.
- Connect to your instance by using SSH. For more information about connections,
  see [Troubleshooting Connecting to Your Instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md") in the _Amazon EC2 user
  guide._.
- Ensure your AWS CLI is up to date using the steps in [Installing the current AWS CLI Version](../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled "../../../cli/latest/userguide/install-cliv1.md#install-tool-bundled").
- In your instance, run `aws configure` and provide the credentials of your created user.
- In your instance, run the following command to log in to the Amazon ECR repository
  where Deep Learning Containers images are hosted.

```
`aws ecr get-login-password --region `us-east-1` | docker login --username AWS --password-stdin `763104351884`.dkr.ecr.`us-east-1`.amazonaws.com`
```

## Next steps

To learn about training and inference on Amazon EC2 with Deep Learning Containers, see [Amazon EC2 Tutorials](deep-learning-containers-ec2.md "deep-learning-containers-ec2.md").
