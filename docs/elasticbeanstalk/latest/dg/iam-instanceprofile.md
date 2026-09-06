

# Managing Elastic Beanstalk instance profiles
<a name="iam-instanceprofile"></a>

An instance profile is a container for an AWS Identity and Access Management (IAM) role that you can use to pass role information to an Amazon EC2 instance when the instance starts. 

If your AWS account doesn’t have an EC2 instance profile, you must create one using the IAM service. You can then assign the EC2 instance profile to new environments that you create. The **Create environment** steps in the Elastic Beanstalk console provides you access to the IAM console, so that you can create an EC2 instance profile with the required permissions.

**Note**  
Previously Elastic Beanstalk created a default EC2 instance profile named `aws-elasticbeanstalk-ec2-role` the first time an AWS account created an environment. This instance profile included default managed policies. If your account already has this instance profile, it will remain available for you to assign to your environments.  
However, recent AWS security guidelines don’t allow an AWS service to automatically create roles with trust policies to other AWS services, EC2 in this case. Because of these security guidelines, Elastic Beanstalk no longer creates a default `aws-elasticbeanstalk-ec2-role` instance profile.



**Managed policies**  
Elastic Beanstalk provides several managed policies to allow your environment to meet different use cases. To meet the default use cases for an environment, these policies must be attached to the role for the EC2 instance profile. 
+ **AWSElasticBeanstalkWebTier** – Grants permissions for the application to upload logs to Amazon S3 and debugging information to AWS X-Ray. To view the managed policy content, see [AWSElasticBeanstalkWebTier](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkWebTier.html) in the *AWS Managed Policy Reference Guide*. 
+ **AWSElasticBeanstalkWorkerTier** – Grants permissions for log uploads, debugging, metric publication, and worker instance tasks, including queue management, leader election, and periodic tasks. To view the managed policy content, see [AWSElasticBeanstalkWorkerTier](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkWorkerTier.html) in the *AWS Managed Policy Reference Guide*.
+ **AWSElasticBeanstalkMulticontainerDocker** – Grants permissions for the Amazon Elastic Container Service to coordinate cluster tasks for Docker environments. To view the managed policy content, see [AWSElasticBeanstalkMulticontainerDocker](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkMulticontainerDocker.html) in the *AWS Managed Policy Reference Guide*.



**Important**  
Elastic Beanstalk managed policies don't provide granular permissions—they grant all permissions that are potentially needed for working with Elastic Beanstalk applications. In some cases you may wish to restrict the permissions of our managed policies further. For an example of one use case, see [Preventing cross-environment Amazon S3 bucket access](AWSHowTo.iam.cross-env-s3-access.md).  
Our managed policies also don't cover permissions to custom resources that you might add to your solution, and that aren't managed by Elastic Beanstalk. To implement more granular permissions, minimum required permissions, or custom resource permissions, use [custom policies](AWSHowTo.iam.managed-policies.md#AWSHowTo.iam.policies).

**Trust relationship policy for EC2**  
To allow the EC2 instances in your environment to assume the required role, the instance profile must specify Amazon EC2 as a trusted entity in the trust relationship policy, as follows.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

To customize permissions, you can add policies to the role attached to the default instance profile or create your own instance profile with a restricted set of permissions.

To use the [AI-powered environment analysis](health-ai-analysis.md) feature, add the `bedrock:InvokeModel`, `bedrock:ListFoundationModels`, `elasticbeanstalk:DescribeEvents`, and `elasticbeanstalk:DescribeEnvironmentHealth` permissions to your instance profile. These permissions allow Elastic Beanstalk to use Amazon Bedrock and access environment data for analyzing logs, events, and instance health. In commercial regions, if this is the first time an Anthropic Claude model is being used in your AWS account, also add the `aws-marketplace:Subscribe`, `aws-marketplace:Unsubscribe`, and `aws-marketplace:ViewSubscriptions` permissions. These AWS Marketplace permissions enable the automatic model subscription that Amazon Bedrock requires for first-time access to third-party models. In GovCloud regions, AI analysis uses the NVIDIA Nemotron model and does not require AWS Marketplace permissions.

**Topics**
+ [Creating an instance profile](#iam-instanceprofile-create)
+ [Adding permissions to the default instance profile](#iam-instanceprofile-addperms)
+ [Verifying the permissions assigned your instance profile](#iam-instanceprofile-verify)
+ [Updating an out-of-date default instance profile](#iam-instanceprofile-update)

## Creating an instance profile
<a name="iam-instanceprofile-create"></a>

An instance profile is a wrapper around a standard IAM role that allows an EC2 instance to assume the role. You can create an instance profile with the default Elastic Beanstalk managed policies. You can also create additional instance profiles to customize permissions for different applications. Or you can create an instance profile that doesn't include the two managed policies that grant permissions for worker tier or ECS managed Docker environments, if you don't use those features.

**To create an instance profile with the default managed policies**

1. Open the [**Roles** page](https://console.aws.amazon.com/iam/home#roles) in the IAM console.

1. Choose **Create role**.

1. For **Trusted entity type**, choose **AWS service**.

1. For **Service or use case**, choose **Elastic Beanstalk**.

1. For **Use case**, choose** Elastic Beanstalk – Compute**. 

1. Choose **Next**.

1. Enter a **Role name**.

   You can enter the name of the default role that the Elastic Beanstalk console suggests: `aws-elasticbeanstalk-ec2-role`.

1. Verify that **Permissions policies** include the following, then choose **Next**:
   + `AWSElasticBeanstalkWebTier`
   + `AWSElasticBeanstalkWorkerTier`
   + `AWSElasticBeanstalkMulticontainerDocker`

1. Choose **Create role**.

**To create an instance profile with your specific choice of managed policies**

1. Open the [**Roles** page](https://console.aws.amazon.com/iam/home#roles) in the IAM console.

1. Choose **Create role**.

1. Under **Trusted entity type**, choose **AWS service**.

1. Under **Use case**, choose **EC2**.

1. Choose **Next**.

1. Attach the appropriate managed policies provided by Elastic Beanstalk and any additional policies that provide permissions that your application needs.

1. Choose **Next**.

1. Enter a name for the role.

1. (Optional) Add tags to the role.

1. Choose **Create role**.

## Adding permissions to the default instance profile
<a name="iam-instanceprofile-addperms"></a>

If your application accesses AWS APIs or resources to which permissions aren't granted in the default instance profile, add policies that grant permissions in the IAM console.

**To add policies to the role attached to the default instance profile**

1. Open the [Roles page](https://console.aws.amazon.com/iam/home#roles) in the IAM console.

1. Choose the role assigned as your EC2 instance profile.

1. On the **Permissions** tab, choose **Attach policies**.

1. Select the managed policy for the additional services that your application uses. For example, `AmazonS3FullAccess` or `AmazonDynamoDBFullAccess`.

1. Choose **Attach policy**.

## Verifying the permissions assigned your instance profile
<a name="iam-instanceprofile-verify"></a>

The permissions assigned to your default instance profile can vary depending on when it was created, the last time you launched an environment, and which client you used. You can verify the permissions on the default instance profile in the IAM console.

**To verify the default instance profile's permissions**

1. Open the [**Roles** page](https://console.aws.amazon.com/iam/home#roles) in the IAM console.

1. Choose the role assigned as your EC2 instance profile.

1. On the **Permissions** tab, review the list of policies attached to the role.

1. To see the permissions that a policy grants, choose the policy.

## Updating an out-of-date default instance profile
<a name="iam-instanceprofile-update"></a>

If the default instance profile lacks the required permissions, you can add the managed policies to the role assigned as your EC2 instance profile manually.

**To add managed policies to the role attached to the default instance profile**

1. Open the [**Roles** page](https://console.aws.amazon.com/iam/home#roles) in the IAM console.

1. Choose the role assigned as your EC2 instance profile.

1. On the **Permissions** tab, choose **Attach policies**.

1. Type **AWSElasticBeanstalk** to filter the policies.

1. Select the following policies, and then choose **Attach policy**:
   + `AWSElasticBeanstalkWebTier`
   + `AWSElasticBeanstalkWorkerTier`
   + `AWSElasticBeanstalkMulticontainerDocker`