# Deployment prerequisites

Make sure the following steps are complete before you start a deployment.

## Deployment prerequisites on an

AWS Lambda compute platform

- Create an application that includes at least one deployment group. For
  information, see [Create an application with CodeDeploy](applications-create.md "applications-create.md") and [Create a deployment group with CodeDeploy](deployment-groups-create.md "deployment-groups-create.md").
- Prepare the application revision, also known as the AppSpec file, that
  specifies the Lambda function version you want to deploy. The AppSpec file
  can also specify Lambda functions to validate your deployment. For more
  information see [Working with application revisions for CodeDeploy](application-revisions.md "application-revisions.md").
- If you want to use a custom deployment configuration for your deployment,
  create it before you start the deployment process. For information, see
  [Create a Deployment Configuration](deployment-configurations-create.md "deployment-configurations-create.md").

## Deployment prerequisites on an

EC2/on-premises compute platform

- For an in-place deployment, create or configure the instances you want to
  deploy to. For information, see [Working with instances for CodeDeploy](instances.md "instances.md"). For a blue/green deployment, you either
  have an existing Amazon EC2 Auto Scaling group to use as a template for your replacement
  environment, or you have one or more instances or Amazon EC2 Auto Scaling groups that you
  specify as your original environment. For more information, see [Tutorial: Use CodeDeploy to deploy an application
  to an Amazon EC2 Auto Scaling group](tutorials-auto-scaling-group.md "tutorials-auto-scaling-group.md") and [Integrating CodeDeploy with Amazon EC2 Auto Scaling](integrations-aws-auto-scaling.md "integrations-aws-auto-scaling.md").
- Create an application that includes at least one deployment group. For
  information, see [Create an application with CodeDeploy](applications-create.md "applications-create.md") and [Create a deployment group with CodeDeploy](deployment-groups-create.md "deployment-groups-create.md").
- Prepare the application revision that you want to deploy to the instances
  in your deployment group. For information, see [Working with application revisions for CodeDeploy](application-revisions.md "application-revisions.md").
- If you want to use a custom deployment configuration for your deployment,
  create it before you start the deployment process. For information, see
  [Create a Deployment Configuration](deployment-configurations-create.md "deployment-configurations-create.md").
- If you are deploying your application revision from an Amazon S3 bucket, the
  bucket is in the same AWS Region as the instances in your deployment
  group.
- If you are deploying your application revision from an Amazon S3 bucket, an
  Amazon S3 bucket policy has been applied to the bucket. This policy grants your
  instances the permissions required to download the application
  revision.

For example, the following Amazon S3 bucket policy allows any Amazon EC2 instance
with an attached IAM instance profile containing the ARN
`arn:aws:iam::444455556666:role/CodeDeployDemo` to download from anywhere in the Amazon S3
bucket named `amzn-s3-demo-bucket`:

```
{
    "Statement": [
        {
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::444455556666:role/CodeDeployDemo"
                ]
            }
        }
    ]
}
```

The following Amazon S3 bucket policy allows any on-premises instance with an
associated IAM user containing the ARN `arn:aws:iam::444455556666:user/CodeDeployUser` to
download from anywhere in the Amazon S3 bucket named
`amzn-s3-demo-bucket`:

```
{
    "Statement": [
        {
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::444455556666:user/CodeDeployUser"
                ]
            }
        }
    ]
}
```

For information about how to generate and attach an Amazon S3 bucket policy,
see [Bucket policy
examples](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md").

- If you are creating a blue/green deployment, or you have specified an
  optional Classic Load Balancer, Application Load Balancer, or Network Load Balancer in the deployment group for an in-place
  deployment, you have created a VPC using Amazon VPC that contains at least two
  subnets. (CodeDeploy uses ELB, which requires all instances in a load balancer
  group to be in a single VPC.)

If you have not created a VPC yet, see the [Amazon VPC Getting Started Guide](../../../AmazonVPC/latest/GettingStartedGuide/ExerciseOverview.md "../../../AmazonVPC/latest/GettingStartedGuide/ExerciseOverview.md").

- If you are creating a blue/green deployment, you have configured at least
  one Classic Load Balancer, Application Load Balancer, or Network Load Balancer in ELB and used it to register the instances
  that make up your original environment.

###### Note

The instances in your replacement environment will be registered with
the load balancer later.

For more information about configuring a load balancer, see [Set up a load balancer in ELB
for CodeDeploy Amazon EC2 deployments](deployment-groups-create-load-balancer.md "deployment-groups-create-load-balancer.md"), and [Set up a load balancer,
target groups, and listeners for CodeDeploy Amazon ECS deployments](deployment-groups-create-load-balancer-for-ecs.md "deployment-groups-create-load-balancer-for-ecs.md").

## Deployment prerequisites for a

blue/green deployment through CloudFormation

- Your template does not need to model resources for a CodeDeploy application or
  deployment group.
- Your template must include resources for a VPC using Amazon VPC that contains
  at least two subnets.
- Your template must include resources for one or more Classic Load Balancers, Application Load Balancers, or Network Load Balancers in ELB
  that are used to direct traffic to your target groups.
