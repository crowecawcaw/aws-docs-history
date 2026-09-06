

# Preventing cross-environment Amazon S3 bucket access
<a name="AWSHowTo.iam.cross-env-s3-access"></a>

This topic explains how managed policies may allow cross-environment S3 bucket access and how you can create custom policies to manage this type of access.

Elastic Beanstalk provides managed polices to handle the AWS resources required by the Elastic Beanstalk environments in your AWS account. The permissions provided by default to one application in your AWS account have access to S3 resources that belong to other applications in the same AWS account.

If your AWS account runs multiple Beanstalk applications, you can scope down the security of your policies by creating your own [custom policy](AWSHowTo.iam.managed-policies.md#AWSHowTo.iam.policies) to attach to your own [service role](iam-servicerole.md#iam-servicerole-create) or [instance profile](iam-instanceprofile.md#iam-instanceprofile-create) for each environment. You can then limit the S3 permissions in your custom policy to a specific environment.

**Note**  
Be aware that you’re responsible for maintaining your custom policy. If an Elastic Beanstalk managed policy on which your custom policy is based changes, you’ll need to modify your custom policy with the respective changes to the base policy. For a change history of Elastic Beanstalk managed policies, see [Elastic Beanstalk updates to AWS managed policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates).

## Example of scoped down permissions
<a name="AWSHowTo.iam.cross-env-s3-access.example-env-ID"></a>

The following example is based on the [AWSElasticBeanstalkWebTier](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkWebTier.html) managed policy.

The default policy includes the following lines for permissions to S3 buckets. This default policy doesn’t limit the S3 bucket actions to specific environments or applications.

```
{
   "Sid" : "BucketAccess", 
   "Action" : [ 
      "s3:Get*",
      "s3:List*", 
      "s3:PutObject"
     ], 
   "Effect" : "Allow",
   "Resource" : [ 
      "arn:aws:s3:::elasticbeanstalk-*", 
      "arn:aws:s3:::elasticbeanstalk-*/*" 
     ] 
}
```

You can scope down the access by qualifying specific resources to a service role specified as a `Principal`. The following example provides the custom service role `aws-elasticbeanstalk-ec2-role-my-example-env` permissions to S3 buckets in the environment with id `my-example-env-ID`.

**Example Grant permissions to only a specific environment's S3 buckets**  

```
{
   "Sid": "BucketAccess",
   "Action": [
      "s3:Get*",
      "s3:List*",
      "s3:PutObject"
    ],
   "Effect": "Allow",
   "Principal": {
      "AWS": "arn:aws:iam::...:role/aws-elasticbeanstalk-ec2-role-my-example-env"
     },
   "Resource": [
      "arn:aws:s3:::elasticbeanstalk-my-region-account-id-12345",
      "arn:aws:s3:::elasticbeanstalk-my-region-account-id-12345/resources/environments/my-example-env-ID/*"
    ]
}
```

**Note**  
The Resource ARN must include the Elastic Beanstalk environment ID, (not the environment name). You can obtain the environment id from the Elastic Beanstalk console on the [Environment overview](environments-dashboard.md) page. You can also use the AWS CLI [ describe-environments](https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/describe-environments.html) command to obtain this information.

For more information to help you update S3 bucket permissions for your Elastic Beanstalk environments, see the following resources:
+ [Using Elastic Beanstalk with Amazon S3](AWSHowTo.S3.md) in this guide
+ [Resource types defined by Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies) in the *Service Authorization Reference* guide
+ [ARN format](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) in the *IAM User Guide*