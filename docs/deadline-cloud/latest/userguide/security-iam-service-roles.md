# Service roles

## How Deadline Cloud uses IAM service roles

Deadline Cloud automatically assumes IAM roles and provides temporary credentials to workers, jobs, and the Deadline Cloud monitor. This approach eliminates manual credential management while maintaining security through role-based access control.

When you create monitors, fleets, and queues, you specify IAM roles that Deadline Cloud assumes on your behalf. Workers and the Deadline Cloud monitor then receive temporary credentials from these roles to access AWS services.

## Fleet role

Configure a fleet role to give Deadline Cloud workers the permissions they need to receive work and report progress on that work.

You usually do not have to configure this role yourself. This role can be created for you in the Deadline Cloud console to include the necessary permissions. Use the following guide to understand the specifics of this role for troubleshooting.

When creating or updating fleets programmatically, specify the fleet role ARN using the `CreateFleet` or `UpdateFleet` API operations.

### What the fleet role does

The fleet role provides workers with permissions to:

- Receive new work and report progress on ongoing work to the Deadline Cloud service
- Manage worker lifecycle and status
- Record log events to Amazon CloudWatch Logs for the worker logs

### Set up the fleet role trust policy

Your fleet role must trust the Deadline Cloud service and be scoped to your specific farm.

As a best practice, the trust policy should include security conditions for Confused Deputy protection. To learn more about Confused Deputy protection, see [Confused Deputy](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md") in the _Deadline Cloud User Guide_.

- `aws:SourceAccount` ensures only resources from the same AWS account can assume this role.
- `aws:SourceArn` restricts role assumption to a specific Deadline Cloud farm.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowDeadlineCredentialsService",
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "credentials.deadline.amazonaws.com"
      },
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`YOUR_ACCOUNT_ID`"
        },
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:deadline:`REGION`:`YOUR_ACCOUNT_ID`:farm/`YOUR_FARM_ID`"
        }
      }
    }
  ]
}
```

### Attach the Fleet role permissions

Attach the following AWS managed policy to your fleet role:

[AWSDeadlineCloud-FleetWorker](../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-FleetWorker.md "../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-FleetWorker.md")

This managed policy provides permissions for:

- `deadline:AssumeFleetRoleForWorker` - Allows workers to refresh their credentials.
- `deadline:UpdateWorker` - Allows workers to update their status (for example, to STOPPED when exiting).
- `deadline:UpdateWorkerSchedule` - For obtaining work and reporting progress.
- `deadline:BatchGetJobEntity` - For fetching job information.
- `deadline:AssumeQueueRoleForWorker` - For accessing queue role credentials during job execution.

### Add KMS permissions for encrypted farms

If your farm was created using a KMS key, add these permissions to your fleet role to ensure the worker can access encrypted data in the farm.

The KMS permissions are only necessary if your farm has an associated KMS key. The `kms:ViaService` condition must use the format `deadline.`{region}`.amazonaws.com`.

When creating a fleet, a CloudWatch Logs log group is created for that fleet. The worker's permissions are used by the Deadline Cloud service to create a log stream specifically for that particular worker. After the worker is set up and running, the worker will use these permissions to send log events directly to CloudWatch Logs.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateLogStream",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream"
      ],
      "Resource": "arn:aws:logs:`REGION`:`YOUR_ACCOUNT_ID`:log-group:/aws/deadline/`YOUR_FARM_ID`/*",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "aws:CalledVia": [
            "deadline.`REGION`.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid": "ManageLogEvents",
      "Effect": "Allow",
      "Action": [
        "logs:PutLogEvents",
        "logs:GetLogEvents"
      ],
      "Resource": "arn:aws:logs:`REGION`:`YOUR_ACCOUNT_ID`:log-group:/aws/deadline/`YOUR_FARM_ID`/*"
    },
    {
      "Sid": "ManageKmsKey",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey",
        "kms:GenerateDataKey"
      ],
      "Resource": "`YOUR_FARM_KMS_KEY_ARN`",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "deadline.`REGION`.amazonaws.com"
        }
      }
    }
  ]
}
```

### Modifying the fleet role

Permissions for the fleet role are not customizable. The described permissions are always required and adding additional permissions has no effect.

## Customer-managed fleet host role

Set up a WorkerHost role if you use customer-managed fleets on Amazon EC2 instances or on-premises hosts.

### What the WorkerHost role does

The WorkerHost role bootstraps workers on customer-managed fleet hosts. It provides the minimal permissions needed for a host to:

- Create a worker in Deadline Cloud
- Assume the fleet role to fetch operational credentials
- Tag workers with fleet tags (if tag propagation is enabled)

### Set up WorkerHost role permissions

Attach the following AWS managed policy to your WorkerHost role:

[AWSDeadlineCloud-WorkerHost](../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-WorkerHost.md "../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-WorkerHost.md")

This managed policy provides permissions for:

- `deadline:CreateWorker` - Allows the host to register a new worker.
- `deadline:AssumeFleetRoleForWorker` - Allows the host to assume the fleet role.
- `deadline:TagResource` - Allows tagging workers during creation (if enabled).
- `deadline:ListTagsForResource` - Allows reading fleet tags for propagation.

### Understand the bootstrap process

The WorkerHost role is only used during initial worker startup:

1. The worker agent starts on the host using WorkerHost credentials.
2. It invokes `deadline:CreateWorker` to register with Deadline Cloud.
3. It then invokes `deadline:AssumeFleetRoleForWorker` to fetch fleet role credentials.
4. From this point forward, the worker uses only fleet role credentials for all operations.

The WorkerHost role is not used after the worker starts running. This policy is not required for Service-managed fleets. In Service-managed fleets, bootstrapping is performed automatically.

## Queue role

The queue role is assumed by the worker when processing a task. This role provides the permissions needed to complete the task.

When creating or updating queues programmatically, specify the queue role ARN using the `CreateQueue` or `UpdateQueue` API operations.

### Set up the queue role trust policy

Your queue role must trust the Deadline Cloud service.

As a best practice, the trust policy should include security conditions for Confused Deputy protection. To learn more about Confused Deputy protection, see [Confused Deputy](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md") in the _Deadline Cloud User Guide_.

- `aws:SourceAccount` ensures only resources from the same AWS account can assume this role.
- `aws:SourceArn` restricts role assumption to a specific Deadline Cloud farm.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "credentials.deadline.amazonaws.com",
          "deadline.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`YOUR_ACCOUNT_ID`"
        },
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:deadline:us-west-2:123456789012:farm/{farm-id}"
        }
      }
    }
  ]
}
```

### Understand queue role permissions

The queue role doesn't use a single managed policy. Instead, when you configure your queue in the console, Deadline Cloud creates a custom policy for your queue based on your configuration.

This automatically created policy provides access to:

#### Job attachments

Read and write access to your specified Amazon S3 bucket for job input and output files:

```
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject",
    "s3:ListBucket",
    "s3:GetBucketLocation"
  ],
  "Resource": [
    "arn:aws:s3:::`YOUR_JOB_ATTACHMENTS_BUCKET`",
    "arn:aws:s3:::`YOUR_JOB_ATTACHMENTS_BUCKET`/`YOUR_PREFIX`/*"
  ],
  "Condition": {
    "StringEquals": {
      "aws:ResourceAccount": "`YOUR_ACCOUNT_ID`"
    }
  }
}
```

#### Job logs

Read access to CloudWatch Logs for jobs in this queue. Each queue has its own log group and each session has its own log stream:

```
{
  "Effect": "Allow",
  "Action": [
    "logs:GetLogEvents"
  ],
  "Resource": "arn:aws:logs:`REGION`:`YOUR_ACCOUNT_ID`:log-group:/aws/deadline/`YOUR_FARM_ID`/*"
}
```

#### Third-party software

Access to download third-party software supported by Deadline Cloud (such as Maya, Blender, and others):

```
{
  "Effect": "Allow",
  "Action": [
    "s3:ListBucket",
    "s3:GetObject"
  ],
  "Resource": "*",
  "Condition": {
    "ArnLike": {
      "s3:DataAccessPointArn": "arn:aws:s3:*:*:accesspoint/deadline-software-*"
    },
    "StringEquals": {
      "s3:AccessPointNetworkOrigin": "VPC"
    }
  }
}
```

### Add permissions for your jobs

Add permissions to your queue role for AWS services that your jobs need to access. When writing OpenJobDescription step scripts, the AWS CLI and SDK will automatically use credentials from your queue role. Use this to access additional services needed to complete your job.

Example use cases include:

- for fetching custom data
- SSM permissions to tunnel to a custom license server
- CloudWatch for emitting custom metrics
- Deadline Cloud permission to create new jobs for dynamic workflows

### How queue role credentials are used

Deadline Cloud provides queue role credentials to:

- Workers during job execution
- Users via Deadline Cloud CLI and monitor when interacting with job attachments and logs

Deadline Cloud creates separate CloudWatch Logs log groups for each queue. Jobs use queue role credentials to write logs to their queue's log group. The Deadline Cloud CLI and monitor use the queue role (through `deadline:AssumeQueueRoleForRead`) to read job logs from the queue's log group. The Deadline Cloud CLI and monitor use the queue role (through `deadline:AssumeQueueRoleForUser`) to upload or download job attachments data.

## Monitor role

Configure a monitor role to give the Deadline Cloud monitor web and desktop applications access to your Deadline Cloud resources.

When creating or updating monitors programmatically, specify the monitor role ARN using the `CreateMonitor` or `UpdateMonitor` API operations.

### What the monitor role does

The monitor role enables Deadline Cloud monitor to provide end users with access to:

- Basic functionality required for the Deadline Cloud Integrated Submitters, CLI and monitor
- Custom functionality for end users

### Set up the monitor role trust policy

Your monitor role must trust the Deadline Cloud service.

As a best practice, the trust policy should include security conditions for Confused Deputy protection. To learn more about Confused Deputy protection, see [Confused Deputy](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md") in the _Deadline Cloud User Guide_.

`aws:SourceAccount` ensures only resources from the same AWS account can assume this role.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "credentials.deadline.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`YOUR_ACCOUNT_ID`"
        }
      }
    }
  ]
}
```

### Attach monitor role permissions

Attach all of the following AWS managed policies to your monitor role for basic operation:

- [AWSDeadlineCloud-UserAccessFarms](../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessFarms.md "../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessFarms.md")
- [AWSDeadlineCloud-UserAccessFleets](../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessFleets.md "../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessFleets.md")
- [AWSDeadlineCloud-UserAccessJobs](../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessJobs.md "../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessJobs.md")
- [AWSDeadlineCloud-UserAccessQueues](../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessQueues.md "../../../aws-managed-policy/latest/reference/AWSDeadlineCloud-UserAccessQueues.md")

### How the monitor role works

When using the Deadline Cloud monitor, a service user signs in using (), and the monitor role is assumed. The assumed role credentials are used by the monitor application to display the monitor UI, including the list of farms, fleets, queues, and other information.

When using the Deadline Cloud monitor desktop application, these credentials are additionally made available on the workstation using a named AWS credential profile corresponding to the profile name provided by the end user. Learn more about named profiles in the [AWS SDK and Tools reference guide](../../../sdkref/latest/guide/file-format.md "../../../sdkref/latest/guide/file-format.md").

This named profile is how the Deadline CLI and submitters access Deadline Cloud resources.

### Customizing the monitor role for advanced use cases

You can customize the monitor role to modify what users can do at each access level
(Viewer, Contributor, Manager, Owner) or to add permissions for advanced workflows.

#### Customizing access level permissions

The four AWS managed policies attached to the monitor role control what each access
level can do. You can add custom policies to the monitor role to grant or restrict
permissions for specific access levels using the `deadline:MembershipLevel`
condition key.

For example, to allow Contributors to update and cancel jobs (which is normally
restricted to Managers and Owners), add a policy like the following:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "deadline:UpdateJob",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "deadline:MembershipLevel": "CONTRIBUTOR"
        }
      }
    }
  ]
}
```

With this policy, Contributors can update and cancel jobs in addition to submitting them.

#### Adding permissions for advanced workflows

You can add custom IAM policies to the monitor role to grant additional permissions
to all monitor users. This is useful for advanced scripting workflows where users need
access to AWS services beyond the standard Deadline Cloud functionality.

Follow these guidelines when modifying your monitor role:

- Don't remove any of the managed policies. Removing these policies breaks monitor functionality.

### How Deadline Cloud monitor uses monitor role credentials

Deadline Cloud monitor automatically obtains monitor role credentials when you authenticate. This capability enables the desktop application to provide enhanced monitoring capabilities beyond what's available in a standard web browser.

When you log in with Deadline Cloud monitor, it automatically creates a profile that you can use with the AWS CLI or any other AWS tool. This profile uses the monitor role credentials, giving you programmatic access to AWS services based on the permissions in your monitor role.

Deadline Cloud submitters work the same way - they use the profile created by Deadline Cloud monitor to access AWS services with the appropriate role permissions.

## Advanced customization of Deadline Cloud roles

You can extend Deadline Cloud roles with additional permissions to enable advanced use cases beyond basic rendering workflows. This approach leverages Deadline Cloud's access management system to control access to additional AWS services based on queue membership.

### Team collaboration with AWS CodeCommit

Add AWS CodeCommit permissions to your Queue role to enable team collaboration on project repositories. This approach uses Deadline Cloud's access management system for additional use cases - only users with access to the specific queue will receive these AWS CodeCommit permissions, allowing you to manage per-project repository access through Deadline Cloud queue membership.

This is useful for scenarios where artists need to access project-specific assets, scripts, or configuration files stored in AWS CodeCommit repositories as part of their rendering workflow.

#### Add AWS CodeCommit permissions to queue role

Add the following permissions to your queue role to enable AWS CodeCommit access:

```
{
  "Effect": "Allow",
  "Action": [
    "codecommit:GitPull",
    "codecommit:GitPush",
    "codecommit:GetRepository",
    "codecommit:ListRepositories"
  ],
  "Resource": "arn:aws:codecommit:`REGION`:`YOUR_ACCOUNT_ID`:`PROJECT_REPOSITORY`"
}
```

#### Set up credential provider on artist workstations

Configure each artist workstation to use Deadline Cloud queue credentials for AWS CodeCommit access. This setup is done once per workstation.

###### To configure the credential provider

1. Add a credential provider profile to your AWS config file (`~/.aws/config`):

```
[profile queue-codecommit]
credential_process = deadline queue export-credentials --farm-id `farm-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` --queue-id `queue-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
```

2. Configure Git to use this profile for AWS CodeCommit repositories:

```
git config --global credential.https://git-codecommit.`REGION`.amazonaws.com.helper '!aws codecommit credential-helper --profile queue-codecommit $@'
git config --global credential.https://git-codecommit.`REGION`.amazonaws.com.UseHttpPath true
```

Replace `farm-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` and `queue-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` with your actual farm and queue IDs. Replace `REGION` with your AWS region (for example, `us-west-2`).

#### Using AWS CodeCommit with queue credentials

Once configured, Git operations will automatically use the queue role credentials when accessing AWS CodeCommit repositories. The `deadline queue export-credentials` command returns temporary credentials that look like this:

```
{
  "Version": 1,
  "AccessKeyId": "ASIA...",
  "SecretAccessKey": "...",
  "SessionToken": "...",
  "Expiration": "2025-11-10T23:02:23+00:00"
}
```

These credentials are automatically refreshed as needed, and Git operations will work seamlessly:

```
git clone https://git-codecommit.`REGION`.amazonaws.com/v1/repos/`PROJECT_REPOSITORY`
git pull
git push
```

Artists can now access project repositories using their queue permissions without needing separate AWS CodeCommit credentials. Only users with access to the specific queue will be able to access the associated repository, enabling fine-grained access control through Deadline Cloud's queue membership system.
