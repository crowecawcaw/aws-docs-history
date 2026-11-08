

# Troubleshooting: Creating and updating an Amazon MWAA environment
<a name="t-create-update-environment"></a>

The topics on this page contain errors you can encounter when creating and updating an Amazon Managed Workflows for Apache Airflow environment and how to resolve these errors.

**Contents**
+ [Environment errors](#troubleshooting-environment-errors)
  + [`AIRFLOW_COMPONENT_FAILURE`](#t-airflow-component-failure)
    + [Before you begin](#t-acf-before-you-begin)
    + [Stabilization and resources](#t-acf-stabilization-resources)
      + [My update fails or rolls back with a component at maximum utilization](#t-acf-max-utilization)
      + [My environment is stuck in `UPDATING` and old worker tasks will not terminate](#t-acf-stuck-updating)
    + [Dependencies and versions](#t-acf-dependencies-versions)
      + [My scheduler or worker cannot install Python packages during the update](#t-acf-pip-install)
  + [`VALID_KMS_KEY_REQUIRED`](#t-valid-kms-key-required)
    + [Before you begin](#t-vkkr-before-you-begin)
    + [Key policy](#t-vkkr-key-policy)
      + [My environment fails to create with a KMS validation error, or stops logging to CloudWatch after an update](#t-vkkr-missing-cwl-grant)
      + [I get an AccessDenied error on kms:Decrypt during DAG execution](#t-vkkr-runtime-decrypt)
      + [My key policy does not grant the other services that MWAA integrates with](#t-vkkr-other-services)
    + [Networking](#t-vkkr-networking)
      + [My KMS failure occurs alongside VPC or security group problems](#t-vkkr-vpc-sg)
  + [`VPC_ENDPOINT_LIMIT_EXCEEDED`](#t-vpc-endpoint-limit-exceeded)
    + [Infrastructure prerequisites](#t-vel-infra-prereqs)
      + [My update fails when increasing `MaxWorkers`](#t-vel-maxworkers-ip)
  + [`INCORRECT_CONFIGURATION`](#t-incorrect-configuration)
+ [Updating `requirements.txt`](#troubleshooting-reqs)
  + [I specified a new version of my `requirements.txt` and it's taking more than 20 minutes to update my environment](#t-requirements)
  + [I get a `Could not install packages due to an OSError [Error 28] No space left on device` error](#t-requirements-no-space)
+ [Plugins](#troubleshooting-plugins)
  + [Does Amazon MWAA support implementing custom UI?](#custom-ui)
+ [Create bucket](#troubleshooting-create-bucket)
  + [I can't select the option for S3 Block Public Access settings](#t-create-bucket)
+ [Create environment](#troubleshooting-create-environment)
  + [I tried to create an environment and it's stuck in the `Creating` state](#t-stuck-failure)
  + [I tried to create an environment but it displays the status as `Create failed`](#t-create-environ-failed)
  + [I tried to select a VPC and received a `Network Failure` error](#t-network-failure)
  + [I tried to create an environment and received a service, partition, or resource "must be passed" error](#t-service-partition)
  + [I tried to create an environment and it displays the status as `Available` but when I try to access the Airflow UI an `Empty Reply from Server` or `502 Bad Gateway` error is shown](#t-create-environ-empty-reply)
  + [I tried to create an environment and my user name is a bunch of random character names](#t-create-environ-random-un)
+ [Update environment](#troubleshooting-update-environment)
  + [I tried changing the environment class but the update failed](#t-rollback-billing-failure)
+ [Access environment](#troubleshooting-access-environment)
  + [I can't access the Apache Airflow UI](#t-no-access-airflow-ui)
+ [Multi-team environments](#troubleshooting-multi-team)
  + [I see "Teams require Identity Center to be configured" when I add teams](#t-multi-team-iic-required)
  + [I get an error that a team name is invalid or already in use](#t-multi-team-invalid-name)
  + [I get an error that DAG folders overlap](#t-multi-team-overlap)
  + [I can't disable IAM Identity Center integration](#t-multi-team-disable-iic)
  + [Users can't see a team's DAGs](#t-multi-team-no-access)

## Environment errors
<a name="troubleshooting-environment-errors"></a>

The following topics describe the errors you might receive for your Amazon MWAA environment.

### `AIRFLOW_COMPONENT_FAILURE`
<a name="t-airflow-component-failure"></a>

The worker, scheduler, or webserver component fails to stabilize during environment creation or update.

#### Before you begin
<a name="t-acf-before-you-begin"></a>

Before you apply a resolution, determine which update phase the environment is in and which component is failing the stabilization check. The recurring signal is a component failing its health check during stabilization, not a steady-state crash.

We recommend the following steps:

1. Determine whether the environment is in the `UPDATING` or `ROLLING_BACK` state, or is stuck.

1. Identify whether the scheduler, worker, or webserver is the component that fails the stabilization check.

1. Pull the affected component's CloudWatch Logs for the update window.

1. Review the following metrics for the update window:
   + CPU and memory utilization for the affected component
   + Metadata database freeable memory

#### Stabilization and resources
<a name="t-acf-stabilization-resources"></a>

##### My update fails or rolls back with a component at maximum utilization
<a name="t-acf-max-utilization"></a>

Resource saturation during stabilization is the most common cause of `AIRFLOW_COMPONENT_FAILURE`. Symptoms include the update failing or rolling back, the scheduler or webserver at maximum utilization, and slow worker stabilization.

We recommend the following steps:
+ Right-size the environment class.
+ Reduce load before you retry the update:
  + Fix DAG import errors and high parse time.
  + Pause and restore DAGs gradually rather than all at once.
  + Align your Apache Airflow concurrency settings with your worker capacity.
+ Increase the metadata database capacity to address worker instability, because low freeable memory can block stabilization.

For more information, see [Performance tuning for Apache Airflow on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/best-practices-tuning.html).

##### My environment is stuck in `UPDATING` and old worker tasks will not terminate
<a name="t-acf-stuck-updating"></a>

If the environment is stuck in the `UPDATING` state, tasks on old workers do not terminate. Graceful updates then fail because worker replacement cannot drain running tasks.

We recommend the following steps:
+ Set the [worker replacement strategy](https://docs.aws.amazon.com/mwaa/latest/userguide/update-environment.html#worker-replacement-strategy) to `FORCED`. Forced updates stop running tasks so that the update does not wait for them to drain, which prevents the environment from getting stuck.
+ If the environment is already stuck, release the workers so the update can complete. To do this, mark running tasks as failed.
+ To prevent recurrence, pause your DAGs, drain running tasks, and run the update when no extra workers are active.

#### Dependencies and versions
<a name="t-acf-dependencies-versions"></a>

##### My scheduler or worker cannot install Python packages during the update
<a name="t-acf-pip-install"></a>

If the scheduler or worker cannot install Python packages mid-update, the install is likely failing because of a transient `pip` or network stall. This stall typically occurs while pulling from public PyPI.

We recommend the following steps:
+ Deliver dependencies locally by using `plugins.zip` instead of public PyPI.
+ Pre-download and pin wheels so the install can survive transient `pip` or network stalls during the update.

### `VALID_KMS_KEY_REQUIRED`
<a name="t-valid-kms-key-required"></a>

Check that your AWS KMS customer managed key is enabled, and that the permissions policy attached to the key grants access to your environment.

#### Before you begin
<a name="t-vkkr-before-you-begin"></a>

Before you edit the key policy, confirm where the failure occurs and that the key itself is valid. The principals you add to the key policy differ depending on whether the failure happens at creation, at update, or at runtime during DAG execution.

We recommend the following steps:

1. Determine where the failure occurs:
   + Most occurrences are at environment creation, and some at update.
   + A few are runtime `kms:Decrypt` `AccessDenied` errors during DAG execution.

1. Confirm that the key is a valid, enabled customer managed key in the same AWS Region and account as the environment. Verify that you specified the key ARN correctly, and that the configuration does not reference an empty or invalid AWS KMS resource.

#### Key policy
<a name="t-vkkr-key-policy"></a>

Several key policy problems can cause this error. Review the following scenarios, and apply the fix that matches your symptoms.

##### My environment fails to create with a KMS validation error, or stops logging to CloudWatch after an update
<a name="t-vkkr-missing-cwl-grant"></a>

A missing CloudWatch Logs grant in the key policy is the most common root cause of `VALID_KMS_KEY_REQUIRED`. Symptoms include creation failing with the AWS KMS validation error, or components that stop logging to CloudWatch Logs after an update.

We recommend the following steps:
+ Add the CloudWatch Logs service principal, `logs.{{region}}.amazonaws.com`, to the AWS KMS key policy with permission to use the key.
+ Scope the grant by using the `kms:ViaService` condition for CloudWatch Logs.

##### I get an AccessDenied error on kms:Decrypt during DAG execution
<a name="t-vkkr-runtime-decrypt"></a>

Several symptoms point to this problem: a runtime `AccessDenied` error on `kms:Decrypt`, missing dependencies or import errors after a container is replaced, or a AWS KMS access-denied error during DAG execution. These symptoms indicate that the Amazon MWAA execution role lacks the required permissions on the key, or that the key policy scope is too restrictive.

We recommend the following steps:
+ Grant the Amazon MWAA execution role the required AWS KMS actions on the key, notably `kms:Decrypt`, as well as `kms:Encrypt` and `kms:GenerateDataKey` as applicable. These permissions are required to access encrypted Amazon S3 objects (your DAGs, plugins, and `requirements.txt`) and other encrypted dependencies.
+ Correct a policy scope that is too restrictive.

##### My key policy does not grant the other services that MWAA integrates with
<a name="t-vkkr-other-services"></a>

Creation validation checks that the key is usable by the full set of dependent principals, not CloudWatch Logs alone. If the key policy grants only CloudWatch Logs, validation can still fail.

We recommend the following steps:
+ Make sure that the key policy also allows the other services that Amazon MWAA integrates with and that need the customer managed key, including Amazon S3, Amazon SQS, and the execution role.

#### Networking
<a name="t-vkkr-networking"></a>

Networking problems can occur alongside this error. Review the following scenario.

##### My KMS failure occurs alongside VPC or security group problems
<a name="t-vkkr-vpc-sg"></a>

Several AWS KMS failures occur in combination with Amazon VPC or security group misconfiguration. Networking problems can block the environment from validating or using the key. When you fix the key policy at creation time, verify your networking in the same pass.

We recommend the following steps:
+ Check your security group inbound and outbound rules.
+ Verify that your Amazon VPC endpoints are reachable, including the AWS KMS endpoint, so that networking does not block key validation and use.

For more information, see [Using customer managed keys for encryption](https://docs.aws.amazon.com/mwaa/latest/userguide/encryption.html).

### `VPC_ENDPOINT_LIMIT_EXCEEDED`
<a name="t-vpc-endpoint-limit-exceeded"></a>

The Amazon VPC associated with your environment has reached the maximum number of Amazon VPC endpoints. Delete unused Amazon VPC endpoints or request a service quota increase before creating the environment.

#### Infrastructure prerequisites
<a name="t-vel-infra-prereqs"></a>

Environment infrastructure limits can cause an update to fail.

##### My update fails when increasing `MaxWorkers`
<a name="t-vel-maxworkers-ip"></a>

An update that increases `MinWorkers` or `MaxWorkers` can fail if the environment's subnets do not have enough free IP addresses for the additional workers.

We recommend the following steps:
+ Reclaim orphaned elastic network interfaces (ENIs) to free IP addresses.
+ Alternatively, move the environment to larger subnets with greater IP capacity.

### `INCORRECT_CONFIGURATION`
<a name="t-incorrect-configuration"></a>

Check the execution role permissions policy for your environment. Verify that each Amazon VPC networking component required by the environment allows traffic.

## Updating `requirements.txt`
<a name="troubleshooting-reqs"></a>

The following topic describes the errors you might receive when updating your `requirements.txt`.

### I specified a new version of my `requirements.txt` and it's taking more than 20 minutes to update my environment
<a name="t-requirements"></a>

If it takes more than twenty minutes for your environment to install a new version of a `requirements.txt` file, the environment update failed and Amazon MWAA is rolling back to the last stable version of the container image.

1. Check package versions. We recommend always specifying either a specific version (`==`) or a maximum version (`<=`) for the Python dependencies in your `requirements.txt`.

1. Check Apache Airflow logs. If you enabled Apache Airflow logs, verify your log groups were created successfully on the [Logs groups page](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups) on the CloudWatch console. If you get blank logs, the most common reason is due to missing permissions in your execution role for CloudWatch or Amazon S3 where logs are written. To learn more, refer to [Execution role](mwaa-create-role.md).

1. Check Apache Airflow configuration options. If you're using Secrets Manager, verify that the key-value pairs you specified as an Apache Airflow configuration option were configured correctly. To learn more, refer to [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md).

1. Check VPC network configuration. To learn more, refer to [I tried to create an environment and it's stuck in the `Creating` state](#t-stuck-failure).

1. Check execution role permissions. An execution role is an AWS Identity and Access Management (IAM) role with a permissions policy that grants Amazon MWAA permission to invoke the resources of other AWS services (such as Amazon S3, CloudWatch, Amazon SQS, Amazon ECR) on your behalf. Your [Customer-managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) or [AWS-owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) also needs to be permitted access. To learn more, refer to [Execution role](mwaa-create-role.md).

1. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA) script in AWS Support Tools on GitHub.

### I get a `Could not install packages due to an OSError [Error 28] No space left on device` error
<a name="t-requirements-no-space"></a>

Amazon MWAA containers have a finite amount of storage for the OS, DAGs, runtimes, and libraries. For more information, see [How much task storage is available to each environment?](mwaa-faqs.md#worker-storage).

To reduce the storage requirement, you might be able to use `--no-cache-dir` by installing the libraries with a startup script. For example:

```
#!/bin/sh

if [[ "${MWAA_AIRFLOW_COMPONENT}" != "webserver" ]]
then
     # place requirements.txt in DAGs folder, and replace existing requirements.txt with an empty text file
     pip3 install --no-cache-dir -r /usr/local/airflow/dags/requirements.txt
fi
```

For more information, see [Configure a startup script](using-startup-script.md#create-startup-script).

You can also install your libraries from Python wheel files. For more information, see [Option two: Python wheels (.whl)](best-practices-dependencies.md#best-practices-dependencies-python-wheels).

## Plugins
<a name="troubleshooting-plugins"></a>

The following topic describes issues you can encounter when configuring or updating Apache Airflow plugins.

### Does Amazon MWAA support implementing custom UI?
<a name="custom-ui"></a>

Starting with Apache Airflow v2.2.2, Amazon MWAA supports installing plugins on the Apache Airflow webserver, and implementing custom UI. If your Amazon MWAA environment is running Apache Airflow v2.0.2 or older, you will not be able to implement custom UI.

For more information about version management, and upgrading your existing environments, refer to [Apache Airflow versions on Amazon Managed Workflows for Apache Airflow](airflow-versions.md).

## Create bucket
<a name="troubleshooting-create-bucket"></a>

The following topic describes the errors you might receive when creating an Amazon S3 bucket.

### I can't select the option for S3 Block Public Access settings
<a name="t-create-bucket"></a>

The [execution role](mwaa-create-role.md) for your Amazon MWAA environment needs permission to the `GetBucketPublicAccessBlock` action on the Amazon S3 bucket to verify the bucket blocked public access. We recommend the following steps:

1. Follow the steps to [Attach a JSON policy to your execution role](mwaa-create-role.md).

1. Attach the following JSON policy:

   ```
   {
     "Effect":"Allow",
     "Action":[
       "s3:GetObject*",
       "s3:GetBucket*",
       "s3:List*"
     ],
     "Resource":[
       "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
       "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
     ]
   }
   ```

   Substitute the sample placeholders in {{amzn-s3-demo-bucket}} with your Amazon S3 bucket name.

1. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA) script in AWS Support Tools on GitHub.

## Create environment
<a name="troubleshooting-create-environment"></a>

The following topic describes the errors you might receive when creating an environment.

### I tried to create an environment and it's stuck in the `Creating` state
<a name="t-stuck-failure"></a>

We recommend the following steps:

1. Check VPC network with *public routing*. If you're using an Amazon VPC with internet access, verify the following:

   1. That your Amazon VPC is configured to allow network traffic between the different AWS resources used by your Amazon MWAA environment, as defined in [About networking on Amazon MWAA](networking-about.md). For example, your VPC security group must either allow all traffic in a self-referencing rule, or optionally specify the port range for HTTPS port range 443 and a TCP port range 5432.

1. Check VPC network with *private routing*. If you're using an Amazon VPC without internet access, verify the following:

   1. That your Amazon VPC is configured to allow network traffic between the different AWS resources for your Amazon MWAA environment, as defined in [About networking on Amazon MWAA](networking-about.md). For example, your two private subnets must **not** have a route table to a NAT gateway (or NAT instance), **nor** an internet gateway.

1. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA) script in AWS Support Tools on GitHub.

### I tried to create an environment but it displays the status as `Create failed`
<a name="t-create-environ-failed"></a>

We recommend the following steps:

1. Check VPC network configuration. To learn more, refer to [I tried to create an environment and it's stuck in the `Creating` state](#t-stuck-failure).

1. Check user permissions. Amazon MWAA performs a dry run against a user's credentials before creating an environment. Your AWS account might not have permission in AWS Identity and Access Management (IAM) to create some of the resources for an environment. For example, if you chose the **Private network** Apache Airflow access mode, your AWS account must have been granted access by your administrator to the [AmazonMWAAFullConsoleAccess](access-policies.md#console-full-access) access control policy for your environment, which allows your account to create VPC endpoints.

1. Check execution role permissions. An execution role is an AWS Identity and Access Management (IAM) role with a permissions policy that grants Amazon MWAA permission to invoke the resources of other AWS services (such as Amazon S3, CloudWatch, Amazon SQS, Amazon ECR) on your behalf. Your [Customer-managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) or [AWS-owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) also needs to be permitted access. To learn more, refer to [Execution role](mwaa-create-role.md).

1. Check Apache Airflow logs. If you enabled Apache Airflow logs, verify your log groups were created successfully on the [Logs groups page](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups) on the CloudWatch console. If you get blank logs, the most common reason is due to missing permissions in your execution role for CloudWatch or Amazon S3 where logs are written. To learn more, refer to [Execution role](mwaa-create-role.md).

1. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA) script in AWS Support Tools on GitHub.

1. If you are using an Amazon VPC *without* internet access, ensure that you've created an Amazon S3 gateway endpoint, and granted the minimum required permissions to Amazon ECR to access Amazon S3. To learn more about creating an Amazon S3 gateway endpoint, refer to the following:
   + [Creating an Amazon VPC network without internet access](vpc-create.md#vpc-create-template-private-only)
   + [Create the Amazon S3 gateway endpoint](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html#ecr-setting-up-s3-gateway) in the *Amazon Elastic Container Registry User Guide*

### I tried to select a VPC and received a `Network Failure` error
<a name="t-network-failure"></a>

We recommend the following steps:
+ If you get a `Network Failure` error when you try to select an Amazon VPC when creating your environment, turn off any in-browser proxies that are running, and then try again.

### I tried to create an environment and received a service, partition, or resource "must be passed" error
<a name="t-service-partition"></a>

We recommend the following steps:
+ You might be receiving this error because the URI you specified for your Amazon S3 bucket includes a '/' at the end of the URI. We recommend removing the '/' in the path. The value must be in the following format:

  ```
  s3://amzn-s3-demo-bucket
  ```

### I tried to create an environment and it displays the status as `Available` but when I try to access the Airflow UI an `Empty Reply from Server` or `502 Bad Gateway` error is shown
<a name="t-create-environ-empty-reply"></a>

We recommend the following steps:

1. Check VPC security group configuration. To learn more, refer to [I tried to create an environment and it's stuck in the `Creating` state](#t-stuck-failure).

1. Confirm that any Apache Airflow packages you listed in the `requirements.txt` correspond to the Apache Airflow version you're running on Amazon MWAA. To learn more, refer to [Installing Python dependencies](working-dags-dependencies.md).

1. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA) script in AWS Support Tools on GitHub.

### I tried to create an environment and my user name is a bunch of random character names
<a name="t-create-environ-random-un"></a>
+ Apache Airflow has a maximum of 64 characters for user names. If your AWS Identity and Access Management (IAM) role exceeds this length, a hash algorithm is used to reduce it, while remaining unique.

## Update environment
<a name="troubleshooting-update-environment"></a>

The following topic describes the errors you might receive when updating an environment.

### I tried changing the environment class but the update failed
<a name="t-rollback-billing-failure"></a>

If you update your environment to a different environment class (such as changing an `mw1.medium` to an `mw1.small`), and the request to update your environment failed, the environment status goes into an `UPDATE_FAILED` state and the environment is rolled back to, and is billed according to, the previous stable version of an environment.

We recommend the following steps:

1. Test your DAGs, custom plugins, and Python dependencies locally using [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images) on GitHub.

1. To run a troubleshooting script that checks the Amazon VPC network setup and configuration for your Amazon MWAA environment, refer to the [Verify Environment](https://github.com/awslabs/aws-support-tools/tree/master/MWAA) script in AWS Support Tools on GitHub.

## Access environment
<a name="troubleshooting-access-environment"></a>

The following topic describes the errors you might receive when accessing an environment.

### I can't access the Apache Airflow UI
<a name="t-no-access-airflow-ui"></a>

We recommend the following steps:

1. Check user permissions. You might not have been granted access to a permissions policy that you can use to access the Apache Airflow UI. To learn more, refer to [Accessing an Amazon MWAA environment](access-policies.md).

1. Check network access. This might be because you selected the **Private network** access mode. If the URL of your Apache Airflow UI is in the following format `387fbcn-8dh4-9hfj-0dnd-834jhdfb-vpce.c10.us-west-2.airflow.amazonaws.com`, it means that you're using *private routing* for your Apache Airflow webserver. You can either update the Apache Airflow access mode to the **Public network** access mode, or create a mechanism to access the VPC endpoint for your Apache Airflow *Web server*. To learn more, refer to [Managing access to service-specific Amazon VPC endpoints on Amazon MWAA](vpc-vpe-access.md).

## Multi-team environments
<a name="troubleshooting-multi-team"></a>

The following topics describe the errors you might receive when you configure teams in a multi-team environment. For team name and DAG folder rules, see [Multi-team environments](multi-team-environments.md).

### I see "Teams require Identity Center to be configured" when I add teams
<a name="t-multi-team-iic-required"></a>

The Amazon MWAA console shows the following message when IAM Identity Center integration isn't enabled: `Teams require Identity Center to be configured. Enable Identity Center above before adding teams.`

Enable IAM Identity Center integration on the same page, and then add the teams. For more information, see [Using IAM Identity Center with Amazon Managed Workflows for Apache Airflow](identity-center-integration.md).

### I get an error that a team name is invalid or already in use
<a name="t-multi-team-invalid-name"></a>

Team names must be unique within the environment, be 3 to 50 characters long, start with a letter or number, and contain only letters, numbers, hyphens (`-`), and underscores (`_`). Choose a name that meets these requirements and matches the display name of an IAM Identity Center group.

### I get an error that DAG folders overlap
<a name="t-multi-team-overlap"></a>

A team folder can't be inside the global DAG folder or another team's folder, and the global folder can't be inside a team folder. For example, if the global DAG folder is `s3://amzn-s3-demo-bucket/dags/`, use `s3://amzn-s3-demo-bucket/teams/team-a/` for a team instead of `s3://amzn-s3-demo-bucket/dags/team-a/`.

### I can't disable IAM Identity Center integration
<a name="t-multi-team-disable-iic"></a>

After you enable IAM Identity Center integration on an environment, you can't disable it, even if you remove all teams. To stop using IAM Identity Center, create a new environment without it. For more information, see [Known limitations](identity-center-integration.md#iic-integration-limitations).

### Users can't see a team's DAGs
<a name="t-multi-team-no-access"></a>

A user can see a team's DAGs only if they belong to the team's IAM Identity Center group and their Permission Set policy allows the access. We recommend the following steps:

1. Check that an IAM Identity Center group exists whose display name exactly matches the team name. Matching is case-sensitive, so a team named `data-engineering` doesn't match a group named `Data-Engineering`. If no group matches, the team has no members.

1. Check that the user is a member of that IAM Identity Center group.

1. Check the user's Permission Set policy. If it uses the `airflow:TeamNames` condition key, use the `ForAnyValue:StringEquals` operator and include the team name. For examples, see [Using IAM Identity Center with Amazon Managed Workflows for Apache Airflow](identity-center-integration.md).