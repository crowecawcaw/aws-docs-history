# Troubleshooting: Creating and updating an Amazon MWAA environment

The topics on this page contain errors you can encounter when creating and updating an Amazon Managed Workflows for Apache Airflow environment and how to resolve these errors.

###### Contents

- [Updating requirements.txt](t-create-update-environment.md#troubleshooting-reqs "t-create-update-environment.md#troubleshooting-reqs")
  - [I specified a new version of my requirements.txt and it's taking more than 20 minutes to update my environment](t-create-update-environment.md#t-requirements "t-create-update-environment.md#t-requirements")

- [Plugins](t-create-update-environment.md#troubleshooting-plugins "t-create-update-environment.md#troubleshooting-plugins")
  - [Does Amazon MWAA support implementing custom UI?](t-create-update-environment.md#custom-ui "t-create-update-environment.md#custom-ui")

- [Create bucket](t-create-update-environment.md#troubleshooting-create-bucket "t-create-update-environment.md#troubleshooting-create-bucket")
  - [I can't select the option for S3 Block Public Access settings](t-create-update-environment.md#t-create-bucket "t-create-update-environment.md#t-create-bucket")

- [Create environment](t-create-update-environment.md#troubleshooting-create-environment "t-create-update-environment.md#troubleshooting-create-environment")
  - [I tried to create an environment and it's stuck in the Creating state](t-create-update-environment.md#t-stuck-failure "t-create-update-environment.md#t-stuck-failure")
  - [I tried to create an environment but it displays the status as Create failed](t-create-update-environment.md#t-create-environ-failed "t-create-update-environment.md#t-create-environ-failed")
  - [I tried to select a VPC and received a Network Failure error](t-create-update-environment.md#t-network-failure "t-create-update-environment.md#t-network-failure")
  - [I tried to create an environment and received a service, partition, or resource "must be passed" error](t-create-update-environment.md#t-service-partition "t-create-update-environment.md#t-service-partition")
  - [I tried to create an environment and it displays the status as Available but when I try to access the Airflow UI an Empty Reply from Server or 502 Bad Gateway error is shown](t-create-update-environment.md#t-create-environ-empty-reply "t-create-update-environment.md#t-create-environ-empty-reply")
  - [I tried to create an environment and my user name is a bunch of random character names](t-create-update-environment.md#t-create-environ-random-un "t-create-update-environment.md#t-create-environ-random-un")

- [Update environment](t-create-update-environment.md#troubleshooting-update-environment "t-create-update-environment.md#troubleshooting-update-environment")
  - [I tried changing the environment class but the update failed](t-create-update-environment.md#t-rollback-billing-failure "t-create-update-environment.md#t-rollback-billing-failure")

- [Access environment](t-create-update-environment.md#troubleshooting-access-environment "t-create-update-environment.md#troubleshooting-access-environment")
  - [I can't access the Apache Airflow UI](t-create-update-environment.md#t-no-access-airflow-ui "t-create-update-environment.md#t-no-access-airflow-ui")

## Updating `requirements.txt`

The following topic describes the errors you might receive when updating your `requirements.txt`.

### I specified a new version of my `requirements.txt` and it's taking more than 20 minutes to update my environment

If it takes more than twenty minutes for your environment to install a new version of a `requirements.txt` file, the environment update failed and Amazon MWAA is rolling back to the last stable version of the container image.

1. Check package versions. We recommend always specifying either a specific version
   (`==`) or a maximum version (`<=`) for the Python
   dependencies in your `requirements.txt`.
2. Check Apache Airflow logs. If you enabled Apache Airflow logs, verify your log groups were created successfully on the [Logs groups page](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups "https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups") on the CloudWatch console. If you get blank logs, the most common reason is due to missing permissions in your execution role for CloudWatch or Amazon S3 where logs are written. To learn more, refer to [Execution role](mwaa-create-role.md "mwaa-create-role.md").
3. Check Apache Airflow configuration options. If you're using Secrets Manager, verify that the key-value pairs you specified as an Apache Airflow configuration option were configured correctly. To learn more, refer to [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md "connections-secrets-manager.md").
4. Check VPC network configuration. To learn more, refer to [I tried to create an environment and it's stuck in the Creating state](#t-stuck-failure "#t-stuck-failure").
5. Check execution role permissions. An execution role is an AWS Identity and Access Management (IAM) role with a permissions policy that grants Amazon MWAA permission to invoke the resources of other AWS services (such as Amazon S3, CloudWatch, Amazon SQS, Amazon ECR) on your behalf. Your [Customer-managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") or [AWS-owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") also needs to be permitted access. To learn more, refer to [Execution role](mwaa-create-role.md "mwaa-create-role.md").
6. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA "https://github.com/awslabs/aws-support-tools/tree/master/MWAA") script in AWS Support Tools on GitHub.

## Plugins

The following topic describes issues you can encounter when configuring or updating Apache Airflow plugins.

### Does Amazon MWAA support implementing custom UI?

Starting with Apache Airflow v2.2.2, Amazon MWAA supports installing plugins on the Apache Airflow webserver, and implementing custom UI. If your Amazon MWAA environment is running
Apache Airflow v2.0.2 or older, you will not be able to implement custom UI.

For more information about version management, and upgrading your existing environments, refer to
[Apache Airflow versions on Amazon Managed Workflows for Apache Airflow](airflow-versions.md "airflow-versions.md").

## Create bucket

The following topic describes the errors you might receive when creating an Amazon S3 bucket.

### I can't select the option for S3 Block Public Access settings

The [execution role](mwaa-create-role.md "mwaa-create-role.md") for your Amazon MWAA environment needs permission to the `GetBucketPublicAccessBlock` action on the Amazon S3 bucket to verify the bucket blocked public access. We recommend the following steps:

1. Follow the steps to [Attach a JSON policy to your execution role](mwaa-create-role.md "mwaa-create-role.md").
2. Attach the following JSON policy:

```
{
  "Effect":"Allow",
  "Action":[
    "s3:GetObject*",
    "s3:GetBucket*",
    "s3:List*"
  ],
  "Resource":[
    "arn:aws:s3:::`amzn-s3-demo-bucket`",
    "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
  ]
}
```

Substitute the sample placeholders in `amzn-s3-demo-bucket` with your Amazon S3 bucket name. 3. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA "https://github.com/awslabs/aws-support-tools/tree/master/MWAA") script in AWS Support Tools on GitHub.

## Create environment

The following topic describes the errors you might receive when creating an environment.

### I tried to create an environment and it's stuck in the `Creating` state

We recommend the following steps:

1. Check VPC network with _public routing_. If you're using an Amazon VPC with internet access, verify the following:
   1. That your Amazon VPC is configured to allow network traffic between the different AWS resources used by your Amazon MWAA environment, as defined in [About networking on Amazon MWAA](networking-about.md "networking-about.md"). For example, your VPC security group must either allow all traffic in a self-referencing rule, or optionally specify the port range for HTTPS port range 443 and a TCP port range 5432.

2. Check VPC network with _private routing_. If you're using an Amazon VPC without internet access, verify the following:
   1. That your Amazon VPC is configured to allow network traffic between the different AWS resources for your Amazon MWAA environment, as defined in [About networking on Amazon MWAA](networking-about.md "networking-about.md"). For example, your two private subnets must **not** have a route table to a NAT gateway (or NAT instance), **nor** an internet gateway.

3. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA "https://github.com/awslabs/aws-support-tools/tree/master/MWAA") script in AWS Support Tools on GitHub.

### I tried to create an environment but it displays the status as `Create failed`

We recommend the following steps:

1. Check VPC network configuration. To learn more, refer to [I tried to create an environment and it's stuck in the Creating state](#t-stuck-failure "#t-stuck-failure").
2. Check user permissions. Amazon MWAA performs a dry run against a user's credentials before creating an environment. Your AWS account might not have permission in AWS Identity and Access Management (IAM) to create some of the resources for an environment. For example, if you chose the **Private network** Apache Airflow access mode, your AWS account must have been granted access by your administrator to the
   [AmazonMWAAFullConsoleAccess](access-policies.md#console-full-access "access-policies.md#console-full-access") access control policy for your environment, which allows your account to create VPC endpoints.
3. Check execution role permissions. An execution role is an AWS Identity and Access Management (IAM) role with a permissions policy that grants Amazon MWAA permission to invoke the resources of other AWS services (such as Amazon S3, CloudWatch, Amazon SQS, Amazon ECR) on your behalf. Your [Customer-managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") or [AWS-owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") also needs to be permitted access. To learn more, refer to [Execution role](mwaa-create-role.md "mwaa-create-role.md").
4. Check Apache Airflow logs. If you enabled Apache Airflow logs, verify your log groups were created successfully on the [Logs groups page](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups "https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups") on the CloudWatch console. If you get blank logs, the most common reason is due to missing permissions in your execution role for CloudWatch or Amazon S3 where logs are written. To learn more, refer to [Execution role](mwaa-create-role.md "mwaa-create-role.md").
5. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA "https://github.com/awslabs/aws-support-tools/tree/master/MWAA") script in AWS Support Tools on GitHub.
6. If you are using an Amazon VPC _without_ internet access, ensure that you've created an Amazon S3 gateway endpoint, and granted
   the minimum required permisions to Amazon ECR to access Amazon S3. To learn more about creating an Amazon S3 gateway endpoint, refer to the following:
   - [Creating an Amazon VPC network without internet access](vpc-create.md#vpc-create-template-private-only "vpc-create.md#vpc-create-template-private-only")
   - [Create the Amazon S3 gateway endpoint](../../../AmazonECR/latest/userguide/vpc-endpoints.md#ecr-setting-up-s3-gateway "../../../AmazonECR/latest/userguide/vpc-endpoints.md#ecr-setting-up-s3-gateway")
     in the _Amazon Elastic Container Registry User Guide_

### I tried to select a VPC and received a `Network Failure` error

We recommend the following steps:

- If you get a `Network Failure` error when you try to select an Amazon VPC when creating your environment, turn off any in-browser proxies that are running, and then try again.

### I tried to create an environment and received a service, partition, or resource "must be passed" error

We recommend the following steps:

- You might be receiving this error because the URI you specified for your Amazon S3 bucket includes a '/' at the end of the URI. We recommend removing the '/' in the path. The value must be in the following format:

```
s3://amzn-s3-demo-bucket
```

### I tried to create an environment and it displays the status as `Available` but when I try to access the Airflow UI an `Empty Reply from Server` or `502 Bad Gateway` error is shown

We recommend the following steps:

1. Check VPC security group configuration. To learn more, refer to [I tried to create an environment and it's stuck in the Creating state](#t-stuck-failure "#t-stuck-failure").
2. Confirm that any Apache Airflow packages you listed in the `requirements.txt` correspond to the Apache Airflow version you're running on Amazon MWAA. To learn more, refer to [Installing Python dependencies](working-dags-dependencies.md "working-dags-dependencies.md").
3. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA "https://github.com/awslabs/aws-support-tools/tree/master/MWAA") script in AWS Support Tools on GitHub.

### I tried to create an environment and my user name is a bunch of random character names

- Apache Airflow has a maximum of 64 characters for user names. If your AWS Identity and Access Management (IAM) role exceeds this length, a hash algorithm is used to reduce it, while remaining unique.

## Update environment

The following topic describes the errors you might receive when updating an environment.

### I tried changing the environment class but the update failed

If you update your environment to a different environment class (such as changing an `mw1.medium` to an `mw1.small`), and the request to update your environment failed, the environment status goes into an `UPDATE_FAILED` state and the environment is rolled back to, and is billed according to, the previous stable version of an environment.

We recommend the following steps:

1. Test your DAGs, custom plugins, and Python dependencies locally using [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") on GitHub.
2. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA "https://github.com/awslabs/aws-support-tools/tree/master/MWAA") script in AWS Support Tools on GitHub.

## Access environment

The following topic describes the errors you might receive when accessing an environment.

### I can't access the Apache Airflow UI

We recommend the following steps:

1. Check user permissions. You might not have been granted access to a permissions policy that you can use to access the Apache Airflow UI. To learn more, refer to [Accessing an Amazon MWAA environment](access-policies.md "access-policies.md").
2. Check network access. This might be because you selected the **Private network** access mode. If the URL of your Apache Airflow UI is in the following format `387fbcn-8dh4-9hfj-0dnd-834jhdfb-vpce.c10.us-west-2.airflow.amazonaws.com`, it means that you're using _private routing_ for your Apache Airflow webserver. You can either update the Apache Airflow access mode to the **Public network** access mode, or create a mechanism to access the VPC endpoint for your Apache Airflow _Web server_. To learn more, refer to [Managing access to service-specific Amazon VPC endpoints on Amazon MWAA](vpc-vpe-access.md "vpc-vpe-access.md").
