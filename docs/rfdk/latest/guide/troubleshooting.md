

# Troubleshooting issues in the RFDK
<a name="troubleshooting"></a>

**Important**  
On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/) for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com) or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html).

This section covers common problems that users of the RFDK may come across, and actions that can be taken to solve them.

## Finding logs
<a name="finding-logs"></a>

**Note**  
This section assumes you are not setting a custom prefix, so the default `/renderfarm/` prefix is used.

The logs are always a good place to start when trying to debug issues with the RFDK. Logs in the RFDK are written into Amazon CloudWatch. After tearing down a render farm, the logs will be persisted so additional debugging can be performed. The same log groups will be continue to be used if another render farm is deployed. When creating RFDK constructs, a log prefix can be passed in using the [`LogGroupFactoryProps.logGroupPrefix`](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.LogGroupFactoryProps.html) field to allow you to use a different log group. This is useful if you would like to run more than one render farm in a single AWS account.

### General
<a name="general"></a>

#### AWS Lambda logs
<a name="aws-lambda-logs"></a>

There are many AWS Lambda functions used throughout RFDK. These will not be reused like the log groups for the construct logs. To find a function’s log group for your current render farm:

1. Navigate to AWS CloudFormation and open the stack that the function is contained in.

1. On the resources tab, you will see entries for `AWS::Lambda::Function`.

1. If the render farm is still deployed:

   1. The physical ID will link you to the function’s page in the AWS Lambda console.

   1. From there you can select the **Monitoring** tab and click the **View logs in CloudWatch** button to be taken to the logs.

1. If your render farm was rolled back or destroyed already:

   1. The logs will still be in Amazon CloudWatch even though the AWS Lambda function is gone. In AWS CloudFormation, note the physical ID that the function had.

   1. Navigate to Amazon CloudWatch to find the log group containing that physical ID.

#### Amazon DocumentDB logs
<a name="amazon-documentdb-logs"></a>

If audit logging is enabled for your Amazon DocumentDB instance, it will generate [audit logs](https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html). The log group for these will start with `/aws/docdb/` and end with `/audit`. It will also contain a unique string that is a part of the physical ID of the Amazon DocumentDB Cluster. To be sure you are looking at the correct logs, you can find this string by looking at your stack in AWS CloudFormation and finding and entry for `AWS::DocDB::DBInstance`. It’s important to realize that while the [Deadline Repository](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.deadline.Repository.html) has a flag to enable audit logging, this will only work if you let the Deadline Repository create the database as well. If you are creating the database yourself and passing it into the Deadline Repository, you will need to ensure you are enabling the audit logging yourself.

#### MongoDB logs
<a name="mongodb-logs"></a>

If MongoDB is chosen as the backing database for your Deadline render farm, then there will be logs saved into a log group that is named based on the ID that is passed into the [`MongoDbInstance` constructor](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.MongoDbInstance.html). For instance, if the construct ID is `MongoDb`, then the log group will be named `/renderfarm/MongoDb`. Inside this log group, you will find log streams for the initialization of the host, named `cloud-init-output-i-[instance-id]`, and for the logs written by the MongoDB daemon, named `MongoDB-i-[instance-id]`. The instance ID can be found by navigating to your Amazon EC2 instances panel and locating the ID of the instance that is named based on the ID that was given to the construct and the AWS CloudFormation stack it’s in. It should appear as `[stack-name]/[construct-id]/Server/Asg`.

### Deadline
<a name="deadline"></a>

#### Usage Based Licensing logs
<a name="usage-based-licensing-logs"></a>

The Deadline Usage Based Licensing logs will be in a log group based on the ID passed into the [Deadline `UsageBasedLicensing` constructor](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.deadline.UsageBasedLicensing.html). For example, if you pass in the ID `UBL`, then the logs will appear at `/renderfarm/UBL`. Inside this log group, you will find log streams for the server running the [Deadline License Forwarder](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/license-forwarder.html). This server is run inside a container, so to find the correct log stream for your forwarder, you will need to find the task ID of the running service. To find this task ID, follow these instructions:

1. Navigate to AWS CloudFormation and open the **resources** tab of the stack the Usage Based Licensing construct is deployed to.

1. In the resources list, find the Amazon ECS Cluster, which should have an `AWS::ECS::Cluster` type, and use the link in the physical ID column to view it.

1. On the **tasks** tab, there should be one task running, with a task definition that starts with `[stack-id][construct-id]TaskDefinition`. Note its UUID.

1. Navigate to AWS CloudWatch and open the log group. Inside it you should see a log stream with the UUID that was found in the task column.

#### Render Queue logs
<a name="render-queue-logs"></a>

The Deadline Render Queue logs will be in a log group based on the ID passed into the [Deadline `RenderQueue` constructor](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.deadline.RenderQueue.html). For example, if you pass in the ID `RenderQueue`, then the logs will appear at `/renderfarm/RenderQueue`. Inside this log group, you will find log streams for the [Deadline Remote Connection Server (RCS)](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/remote-connection-server.html). The RCS is run inside a container, so to find the correct log stream for your RCS, you will need to find the task ID of the running service. To find this task ID, follow these instructions:

1. Navigate to AWS CloudFormation and open the **resources** tab of the stack the Render Queue is deployed to.

1. In the resources list, find the RenderQueue Cluster which should have an `AWS::ECS::Cluster` type and use the link in the physical ID column to view it.

1. On the **tasks** tab, there should be one task running, with a task definition that starts with `[stack-id][construct-id]RCSTask`. Note its UUID.

1. Navigate to AWS CloudWatch and open the log group. Inside it you should see a log stream with the UUID that was found in the task column.

#### Repository logs
<a name="repository-logs"></a>

The Deadline Repository logs will be in a log group based on the ID passed to the [Deadline `Repository` constructor](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.deadline.Repository.html). For example, if you pass in the ID `Repository`, then the logs will appear at `/renderfarm/Repository`. These logs can be used to debug issues either with initializing the repository host, or with the installation of the Deadline repository on that host. Inside this log group, you will find log streams from the initialization of the host, named `cloud-init-output-i-[instance-id]` as well as logs from the Deadline Repository installer, named `deadlineRepositoryInstallationLogs-i-[instance-id]`.

#### Worker Fleet logs
<a name="worker-fleet-logs"></a>

All Deadline Worker Fleet logs will be in a log group based on the ID passed into the constructor of the [Deadline Worker Fleet construct](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.deadline.WorkerInstanceFleet.html). For example, if you pass in the ID `WorkerFleet`, then the logs will appear at `/renderfarm/WorkerFleet`. If your Deadline Worker Fleet fails to start a host or you are having fleet health issues, you can look into the logs for that host. First go into the Amazon EC2 Console and look up the instance ID for the terminated host, then navigate to **CloudWatch > log groups > /renderfarm/WorkerFleet**. There will be three log streams that get written here:

1. One that contains logs from the host’s initialization named `cloud-init-output-i-[instance-id]` on Linux or `UserdataExecution-i-[instance-id]` on Windows.

1. One that contains Deadline specific logs and will be named `WorkerLogs-i-[instance-id]`.

1. One that contains logs from the [Deadline Launcher](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/launcher.html) and will be named `LauncherLogs-i-[instance-id]`.

## Staging Deadline
<a name="troubleshoot-staging-deadline"></a>

### Error fetching Deadline
<a name="error-fetching-deadline"></a>

When running `stage-deadline` you may get the following error message:

```
ERROR: Could not fetch s3://thinkbox-installers/DeadlineDocker/[version-number]/DeadlineDocker-[version-number].tar.gz (Are you authenticated with the AWS CLI?)
```

There can be two reasons for this message:

1. You are trying to pull a version that really does not exist or is incompatible with the RFDK.

1. You are not properly configured to make authenticated calls with the AWS CLI using a user or role with the `s3:GetObject` IAM action. This is required because the staging script uses the AWS CLI to fetch the required files from S3.

 **Action to Take** 

If you aren’t properly configured to make authenticated requests with the AWS CLI, you can follow the [AWS CLI guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to configure credentials for a user or role in your AWS account. The easiest options are either using `aws configure` to set the credentials file’s default or named profiles, or setting environment variables.

The `stage-deadline` command requires that the IAM entity you authenticate with has the `s3:GetObject` IAM action on the `s3://thinkbox-installer/*` resources; A root user or one with admin permissions would suffice. However, if you would like to follow better security practices and use a user with access limited to just these files, you can follow these instructions:

First create an IAM policy with the following JSON. You can follow the [Create a Customer Managed Policy guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html#step1-create-policy) if you aren’t familiar with how to do this.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::thinkbox-installers/*"
        }
    ]
}
```

After finishing the policy setup, create a user that has your new policy applied. If you aren’t familiar with how to do this, follow the [Adding a User guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html). When it gets to the step about setting permissions, choose **Attach existing policies to user directly** and attach your policy.

### Changing Deadline versions
<a name="changing-deadline-versions"></a>

If you attempt to use a different value for {{DEADLINE\_VERSION}} and rerun the `stage-deadline` script, you may get the following message:

```
stage-deadline {{DEADLINE_VERSION}} --output {{STAGE_PATH}}
The target directory is not empty.
```

 **Action to Take** 

Changing the Deadline version can be done in two ways:

1. Use a different directory for staging by providing a different {{STAGE\_PATH}} to the `--output` flag. Remember to update the stage property that gets passed into the [ThinkboxDockerRecipes constructor](https://docs.aws.amazon.com/rfdk/api/latest/docs/aws-rfdk.deadline.ThinkboxDockerRecipes.html) to this new location.

1. Rename the existing staging directory (or delete it if you don’t need it anymore) that was created when you first ran the staging script, and then rerun the script with the new Deadline version number. The staging directory will be the value sent to `--output` or `./stage` by default.

## Connecting to the bastion host
<a name="connecting-to-the-bastion-host"></a>

The [BastionHostLinux construct](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-ec2.BastionHostLinux.html) in the CDK does not allow an Amazon EC2 key pair to be set, so attempting to SSH to it via the command line will not work out-of-the-box.

 **Action to Take** 

If you would like to access this host, it can be done from the Amazon EC2 Console or by adding an SSH key via the AWS CLI.

**To access via the Amazon EC2 console**

1. Navigate to your Amazon EC2 instances

1. Right click on the **Bastion Host**.

1. Select **Connect**.

1. Select either **Session Manager** or **EC2 Instance Connect** to get an SSH session to open in the browser.

**To access via SSH using the AWS CLI**  
If you would prefer to connect via the command line with an SSH key then one can be added manually with the AWS CLI’s [`ec2-instance-connect send-ssh-public-key`](https://docs.aws.amazon.com/cli/latest/reference/ec2-instance-connect/send-ssh-public-key.html) command. Note that this will only install the key temporarily, so you’ll have 60 seconds to create any ssh sessions you require, and then you’ll need to re-upload the key.

## Dependencies between tiered stacks
<a name="dependencies-between-tiered-stacks"></a>

### Removing dependencies from tiered stacks
<a name="removing-dependencies-from-tiered-stacks"></a>

The RFDK suggests to use tiered stacks so that parts of the render farm can be taken down or updated without having to affect the whole render farm. While this saves time and resources overall, it can lead to a known bug in CDK that occurs when a stack has a dependency on another stack and then removes that dependency. You may see an error message like the following:

```
 0/1 | 12:13:45 | UPDATE_ROLLBACK_IN_P | AWS::CloudFormation::Stack              | dep-stack Export dep-stack:ResourceFromPrimaryStack cannot be deleted as it is in use by primary-stack
```

 **Action to Take** 

There is an open issue with the CDK to fix this: [\#3414](https://github.com/aws/aws-cdk/issues/3414). Until that is fixed, the workaround is to deploy your dependent stack first with `cdk deploy -e [dep-stack]` and then run `cdk deploy [primary-stack]` to clean up the unused export. This may not always work depending on how the dependencies between the stacks get resolved, and you may need to destroy your stacks and redeploy.

### Moving constructs between dependent stacks
<a name="moving-constructs-between-dependent-stacks"></a>

If you are trying to move a construct from one stack to a stack that it depends on, then you may encounter errors deploying the revised stacks.

 **Action to Take** 

The stack that you are moving the construct to and all the stacks that depend on it will need to be destroyed and then redeployed. Using `cdk deploy -e` will not work in this case.

## Default removal policies
<a name="default-removal-policies"></a>

Some constructs cannot be destroyed due to their default [removal policies](https://docs.aws.amazon.com/cdk/latest/guide/resources.html#resources_removal). This can then prevent the destruction of other constructs that those other constructs depend on. An example of this happening in the RFDK is the [Amazon DocumentDB Cluster](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-docdb.DatabaseCluster.html) and [Amazon Elastic File System](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-efs.FileSystem.html) constructs having default removal policies of `RemovalPolicy.RETAIN` and dependencies on the [VPC](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-ec2.Vpc.html).

 **Action to Take** 

**Warning**  
Make sure you evaluate whether or not using `RemovalPolicy.DESTROY` is acceptable for your use case. It’s possible that you may not want certain constructs destroyed if you believe they will contain important data that you want persisted after the rest of your render farm is destroyed.

To preemptively avoid this problem, you can modify the removal policy to `RemovalPolicy.DESTROY` before performing your deployment. If you have not modified this property and would like to clean these leftover constructs up, they can be deleted from the AWS console. Once deleted, `cdk destroy [stack-name]` can be rerun to finish destroying anything else that failed to be deleted.