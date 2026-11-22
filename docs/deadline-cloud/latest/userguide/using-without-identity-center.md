

# Using Deadline Cloud without IAM Identity Center

You can submit, monitor, and manage AWS Deadline Cloud (Deadline Cloud) jobs with AWS Identity and Access Management (IAM) credentials instead of AWS IAM Identity Center (IAM Identity Center) users. The Deadline Cloud CLI, the submitters, and the Deadline Cloud monitor desktop application all accept an AWS profile, such as one that uses the instance profile of an Amazon EC2 virtual workstation. Your IAM policies then decide what each person or workstation can do.

## What IAM Identity Center gives you
<a name="without-idc-what-idc-provides"></a>

When people sign in to the monitor through IAM Identity Center, Deadline Cloud provides the following:
+ A sign-in for each person, with your existing identity provider
+ Access levels (viewer, contributor, manager, and owner) that you grant on farms, queues, and fleets without writing IAM policies
+ Grants to groups that follow group membership in your identity provider
+ A record of the person who created or updated each job
+ The monitor in a web browser, in addition to the desktop application
+ Revocation of a disabled user's credentials within 15 minutes

For details, see [How permissions work in Deadline Cloud](permissions-overview.md).

## Choose an approach
<a name="without-idc-choose"></a>

Use the following table to choose how people sign in.


| Approach | Use it when | Access controlled by | 
| --- | --- | --- | 
| IAM Identity Center users sign in to the monitor | You can use IAM Identity Center. We recommend it for most organizations. | Access levels | 
| Console sign-in profile | Your organization can't adopt IAM Identity Center, or you're trying out Deadline Cloud. People sign in to the desktop monitor with their AWS Management Console identity. | IAM policies | 
| Local AWS profile | You already manage credentials on your workstations, for example with an Amazon EC2 instance profile, IAM Roles Anywhere, or a `credential_process` tool. | IAM policies | 
| Both | People sign in through IAM Identity Center, and workstations or automation use IAM credentials. | Access levels for IAM Identity Center users, and IAM policies for everything else | 

For the sign-in steps for a console sign-in profile or a local profile, see [Sign in to the desktop monitor with the AWS Management Console or an AWS profile](monitor-sign-in-aws-credentials.md).

## What works without IAM Identity Center
<a name="without-idc-what-works"></a>

With an AWS profile and the IAM policy in [Grant IAM permissions to artists](#without-idc-iam-policy), the following tools work in an account that has no IAM Identity Center instance and no monitor:
+ The `deadline` CLI, including job submission, output download, job logs, and job cancellation.
+ The Deadline Cloud submitter (`deadline bundle gui-submit`) and the submitters inside host applications such as Blender, Maya, and Nuke. All submitters use the same credentials as the `deadline` CLI.
+ Job attachments, both uploading inputs when you submit and downloading outputs.
+ The Deadline Cloud monitor desktop application, version 1.3.0 or later, with a local profile or a console sign-in profile. You can view farms, queues, jobs, steps, and tasks, read task logs, and view fleet details. To try these views with sample data, open the [demo job monitor](https://_demo.us-east-1.deadlinecloud.amazonaws.com/us-west-2/farms/farm-94d29d9475dd814529b87a52f20ff9cb/queues/queue-8df336a45cbed661f57da93efa5b14db?demo=moonrise).

A farm doesn't need a monitor. You can create and use farms in an account that has no monitor.

## What you give up without IAM Identity Center
<a name="without-idc-give-up"></a>

**Important**  
The `AWSDeadlineCloud-UserAccessFarms`, `AWSDeadlineCloud-UserAccessQueues`, `AWSDeadlineCloud-UserAccessJobs`, and `AWSDeadlineCloud-UserAccessFleets` managed policies don't grant an IAM role or user access to farms, queues, jobs, or fleets. Every statement in them that grants access to a resource requires a membership condition key. Only an IAM Identity Center user's access level provides that key. Write your own policy instead, starting from the one in [Grant IAM permissions to artists](#without-idc-iam-policy).
+ **Access levels** – Assigning an access level to a farm, queue, or fleet requires an IAM Identity Center user or group, so your IAM policies are the only control over what each person or workstation can do.
+ **The web monitor** – The monitor in a web browser requires IAM Identity Center. Use the desktop application instead.
+ **Attribution to a person** – Jobs record the Amazon Resource Name (ARN) of the IAM principal that created them, and the **User** column in the monitor shows that ARN. With an instance profile, the ARN has the form `arn:aws:sts::{{account-id}}:assumed-role/{{role-name}}/{{instance-id}}`, so jobs identify the workstation, not the person who used it. For the formats of these values, see [Retrieving user metadata using userID](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/query-session-data-map-userid.html) in the *Deadline Cloud Developer Guide*.
+ **Farm visibility** – The `deadline:ListFarms` action can't be limited to specific farms. Anyone who can list farms sees every farm name in the account, in every AWS Region, even farms that they can't open.

## Grant IAM permissions to artists
<a name="without-idc-iam-policy"></a>

The following policy lets an artist submit jobs to one farm, monitor and cancel them, read their logs, and use the desktop monitor. Replace the following values with your own:

{{region}}  
The AWS Region that contains your farm, such as `us-west-2`.

{{account-id}}  
The ID of the AWS account that contains your farm.

{{farm-id}}  
The ID of your farm, such as `farm-1234567890abcdef1234567890abcdef`.

```json
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Sid": "ListFarms",
      "Effect": "Allow",
      "Action": [
        "deadline:ListFarms",
        "deadline:GetApplicationVersion"
      ],
      "Resource": "*"
    },
    {
      "Sid": "DiscoverAndRead",
      "Effect": "Allow",
      "Action": [
        "deadline:GetFarm",
        "deadline:ListQueues",
        "deadline:GetQueue",
        "deadline:ListFleets",
        "deadline:GetFleet",
        "deadline:ListStorageProfiles",
        "deadline:ListStorageProfilesForQueue",
        "deadline:GetStorageProfile",
        "deadline:GetStorageProfileForQueue",
        "deadline:ListQueueEnvironments",
        "deadline:GetQueueEnvironment",
        "deadline:ListQueueFleetAssociations",
        "deadline:GetQueueFleetAssociation",
        "deadline:ListWorkers",
        "deadline:SearchWorkers",
        "deadline:GetWorker",
        "deadline:ListSessionsForWorker",
        "deadline:ListVolumes",
        "deadline:GetVolume",
        "deadline:AssumeFleetRoleForRead"
      ],
      "Resource": [
        "arn:aws:deadline:{{region}}:{{account-id}}:farm/{{farm-id}}",
        "arn:aws:deadline:{{region}}:{{account-id}}:farm/{{farm-id}}/*"
      ]
    },
    {
      "Sid": "SubmitAndMonitorJobs",
      "Effect": "Allow",
      "Action": [
        "deadline:CreateJob",
        "deadline:GetJob",
        "deadline:ListJobs",
        "deadline:UpdateJob",
        "deadline:SearchJobs",
        "deadline:ListSteps",
        "deadline:ListStepDependencies",
        "deadline:ListStepConsumers",
        "deadline:GetStep",
        "deadline:UpdateStep",
        "deadline:SearchSteps",
        "deadline:ListTasks",
        "deadline:GetTask",
        "deadline:UpdateTask",
        "deadline:SearchTasks",
        "deadline:ListSessions",
        "deadline:GetSession",
        "deadline:ListSessionActions",
        "deadline:GetSessionAction",
        "deadline:GetJobTemplate",
        "deadline:ListJobParameterDefinitions",
        "deadline:AssumeQueueRoleForUser",
        "deadline:AssumeQueueRoleForRead"
      ],
      "Resource": [
        "arn:aws:deadline:{{region}}:{{account-id}}:farm/{{farm-id}}",
        "arn:aws:deadline:{{region}}:{{account-id}}:farm/{{farm-id}}/*"
      ]
    },
    {
      "Sid": "ReadJobLogs",
      "Effect": "Allow",
      "Action": [
        "logs:GetLogEvents",
        "logs:DescribeLogStreams"
      ],
      "Resource": "arn:aws:logs:{{region}}:{{account-id}}:log-group:/aws/deadline/{{farm-id}}/*"
    }
  ]
}
```

Some of the permissions in the policy aren't obvious:
+ `deadline:ListFarms` – Keep this action even if you limit everything else. The `deadline auth status` command uses it to check your credentials and reports `CONFIGURATION_ERROR` without it.
+ `deadline:ListQueueEnvironments` – Required to submit a job.
+ `deadline:ListQueueFleetAssociations` – Without it, the fleet page in the monitor shows no associated queues and doesn't report an error.
+ `deadline:AssumeQueueRoleForUser` – The client tools use the queue role to upload and download job attachments, so the artist doesn't need any Amazon S3 permissions of their own.
+ `ReadJobLogs`, `deadline:AssumeQueueRoleForRead`, and `deadline:AssumeFleetRoleForRead` – The monitor reads task and worker logs through the queue and fleet roles. The `deadline job logs` command reads them with your own credentials, so it needs the `ReadJobLogs` statement.

To limit an artist to one queue, in the `SubmitAndMonitorJobs` statement replace `farm/{{farm-id}}/*` with `farm/{{farm-id}}/queue/{{queue-id}}` and `farm/{{farm-id}}/queue/{{queue-id}}/*`. Jobs, steps, and tasks are under the queue, so the ARN that ends in `/*` is required. Keep the `DiscoverAndRead` statement as it is, because fleets and storage profiles aren't under a queue. For more examples, see [Identity-based policy examples for Deadline Cloud](security_iam_id-based-policy-examples.md).

### Optional: Budgets and usage in the monitor
<a name="without-idc-budgets-usage"></a>

The preceding policy doesn't include the budget manager or the usage explorer. To let someone open them in the monitor, add a policy like the following one. Replace {{region}}, {{account-id}}, and {{farm-id}} with the same values as in the preceding policy.

```json
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Sid": "BudgetsAndUsage",
      "Effect": "Allow",
      "Action": [
        "deadline:ListBudgets",
        "deadline:GetBudget",
        "deadline:StartSessionsStatisticsAggregation",
        "deadline:GetSessionsStatisticsAggregation"
      ],
      "Resource": [
        "arn:aws:deadline:{{region}}:{{account-id}}:farm/{{farm-id}}",
        "arn:aws:deadline:{{region}}:{{account-id}}:farm/{{farm-id}}/*"
      ]
    }
  ]
}
```

When the budget manager or the usage explorer is missing a permission, the monitor shows a banner that names the denied action and the resource. Add that action and resource to your policy. For more information about these features, see [Manage costs and usage for Deadline Cloud farms](manage-costs.md).

To try these features with sample data, open the [demo budget manager](https://_demo.us-east-1.deadlinecloud.amazonaws.com/us-west-2/farms/farm-94d29d9475dd814529b87a52f20ff9cb/budget?demo=moonrise) and the [demo usage explorer](https://_demo.us-east-1.deadlinecloud.amazonaws.com/us-west-2/farms/farm-94d29d9475dd814529b87a52f20ff9cb/usage?filterBy=QUEUES&groupBy=JOB_ID&units=COST&interval=DAILY&range=last-7-days&demo=moonrise).

### Optional: Access equivalent to every monitor access level
<a name="without-idc-full-access"></a>

The following policy grants the Deadline Cloud actions from the `AWSDeadlineCloud-UserAccessFarms`, `AWSDeadlineCloud-UserAccessQueues`, `AWSDeadlineCloud-UserAccessJobs`, and `AWSDeadlineCloud-UserAccessFleets` managed policies, without their membership conditions. It has no resource restrictions, so it grants owner-level access to every farm in the account. Use it for administrators, or as a starting point that you limit to specific farms and actions.

```json
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Sid": "AllMonitorAccessLevels",
      "Effect": "Allow",
      "Action": [
        "deadline:AssumeFleetRoleForRead",
        "deadline:AssumeQueueRoleForRead",
        "deadline:AssumeQueueRoleForUser",
        "deadline:CreateBudget",
        "deadline:CreateJob",
        "deadline:DeleteBudget",
        "deadline:GetApplicationVersion",
        "deadline:GetBudget",
        "deadline:GetFarm",
        "deadline:GetFleet",
        "deadline:GetJob",
        "deadline:GetJobTemplate",
        "deadline:GetMonitorSettings",
        "deadline:GetQueue",
        "deadline:GetQueueEnvironment",
        "deadline:GetQueueFleetAssociation",
        "deadline:GetSession",
        "deadline:GetSessionAction",
        "deadline:GetSessionsStatisticsAggregation",
        "deadline:GetStep",
        "deadline:GetStorageProfile",
        "deadline:GetStorageProfileForQueue",
        "deadline:GetTask",
        "deadline:GetVolume",
        "deadline:GetWorker",
        "deadline:ListBudgets",
        "deadline:ListFarms",
        "deadline:ListFleets",
        "deadline:ListJobParameterDefinitions",
        "deadline:ListJobs",
        "deadline:ListQueueEnvironments",
        "deadline:ListQueueFleetAssociations",
        "deadline:ListQueues",
        "deadline:ListSessionActions",
        "deadline:ListSessions",
        "deadline:ListSessionsForWorker",
        "deadline:ListStepConsumers",
        "deadline:ListStepDependencies",
        "deadline:ListSteps",
        "deadline:ListStorageProfiles",
        "deadline:ListStorageProfilesForQueue",
        "deadline:ListTasks",
        "deadline:ListVolumes",
        "deadline:ListWorkers",
        "deadline:SearchJobs",
        "deadline:SearchSteps",
        "deadline:SearchTasks",
        "deadline:SearchWorkers",
        "deadline:StartSessionsStatisticsAggregation",
        "deadline:UpdateBudget",
        "deadline:UpdateJob",
        "deadline:UpdateSession",
        "deadline:UpdateStep",
        "deadline:UpdateTask"
      ],
      "Resource": "*"
    }
  ]
}
```

The policy leaves out the actions from the managed policies that work only with IAM Identity Center: adding and removing members, listing members and memberships, looking up users and groups in the identity store, and decrypting with an AWS AWS KMS key through IAM Identity Center. It also leaves out `ec2:DescribeInstanceTypes`, which the monitor no longer uses. To read job logs with the `deadline` CLI, also add the `ReadJobLogs` statement from the artist policy.

## Set up an Amazon EC2 workstation with an instance profile
<a name="without-idc-ec2-workstation"></a>

An Amazon EC2 virtual workstation can use its instance profile for Deadline Cloud, so artists don't manage credentials of their own.

**Important**  
You pay for the Amazon EC2 instance while it runs. For more information, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/).

Before you begin, install the submitter and the Deadline Cloud monitor desktop application, version 1.3.0 or later, on the workstation. The scripts in [Set up a virtual workstation for Deadline Cloud with a script](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-virtual-workstation.html) in the *Deadline Cloud Developer Guide* install both. The scripts require a monitor URL and end by creating a monitor profile. If you don't use a monitor, edit the script to remove the monitor URL argument, its checks, and the profile step, and create the profile in the following procedure instead.

**To set up an Amazon EC2 workstation with an instance profile**

1. Create an IAM role that Amazon EC2 can assume, attach the artist policy from [Grant IAM permissions to artists](#without-idc-iam-policy), and attach the role to the workstation through an instance profile. For more information, see [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the *Amazon EC2 User Guide*.

1. On the workstation, signed in as the artist, add the following profile to `~/.aws/config` (on Windows, `%USERPROFILE%\.aws\config`). Replace {{region}} with the Region that contains your farm.

   ```ini
   [profile workstation]
   region = {{region}}
   ```

   The profile must use the `[profile {{name}}]` form and set a Region. The monitor doesn't list the `[default]` profile or profiles that exist only in `~/.aws/credentials`, and the CLI can't submit jobs without a Region. The profile doesn't need any credential settings. The tools fall back to the default credential chain, which gets credentials from the instance profile.

1. Make the profile the default for the Deadline Cloud tools. Either sign in to the monitor with the profile, which the monitor labels **Local Profile**, and select **Set this profile as default for Deadline Cloud tools**, or run the following command.

   ```bash
   deadline config set defaults.aws_profile_name workstation
   ```

1. Set the default farm and queue for the profile, or choose them in a submitter.

   ```bash
   deadline config set defaults.farm_id {{farm-id}}
   deadline config set defaults.queue_id {{queue-id}}
   ```

   The Deadline Cloud tools store the default farm and queue for each profile separately. When you switch to a different profile, set them again.

1. To confirm that the setup works, run `deadline auth status`. The output shows `AUTHENTICATED` and a `source` of `HOST_PROVIDED`, which means that the tools use the profile's credentials rather than a monitor sign-in. A monitor sign-in shows `DEADLINE_CLOUD_MONITOR_LOGIN` instead.

   ```
   {"profile_name": "workstation", "source": "HOST_PROVIDED", "status": "AUTHENTICATED", "api_availability": true}
   ```

To require that artists work from workstations in your VPC, see [Allow access only from your VPC](restrict-network-access.md#restrict-network-access-vpc).

## Other credential sources
<a name="without-idc-other-credentials"></a>

The Deadline Cloud tools find credentials the same way as the AWS Command Line Interface (AWS CLI), so you can also use the following sources:
+ **Assumed role** – A profile with `role_arn` and `source_profile`. For more information, see [Use an IAM role in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html) in the *AWS CLI User Guide*.
+ **External credential process** – A profile with `credential_process`, such as the IAM Roles Anywhere credential helper for workstations outside AWS. For more information, see [Get temporary security credentials from IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/credential-helper.html) in the *IAM Roles Anywhere User Guide*.
+ **Environment variables** – Such as `AWS_ACCESS_KEY_ID`. The CLI and submitters use them, but the monitor lists only profiles.
+ **IAM user access keys** – Use temporary credentials from one of the preceding sources instead, because access keys don't expire.

With an assumed role, jobs record the role session name as the last part of the ARN. To make jobs easier to attribute, set `role_session_name` in the profile to a name that identifies the person, such as their user name. Anyone who can edit the profile can change the session name, so treat it as a label for reporting.

## Troubleshooting IAM credentials for Deadline Cloud
<a name="without-idc-troubleshooting"></a>

Most problems with IAM credentials come from a profile that isn't a named profile, a profile without a Region, or a policy that's missing a permission. The following entries describe specific problems and how to fix them.

My profile isn't listed in the desktop monitor  
The monitor lists only `[profile {{name}}]` sections in `~/.aws/config`. Move the settings from `[default]` or from `~/.aws/credentials` into a named profile in `~/.aws/config`. On Windows, these files are in `%USERPROFILE%\.aws`. Make sure that you're using version 1.3.0 or later of the monitor.

My profile is listed in the monitor but I can't select it  
The profile doesn't set a Region. Add a `region` line to the profile.

`deadline auth status` reports `CONFIGURATION_ERROR`, or a command fails with `NoRegionError`  
Make sure that the Deadline Cloud default profile exists in `~/.aws/config` (on Windows, `%USERPROFILE%\.aws\config`) and sets a Region. If it does, check that your policy allows `deadline:ListFarms`, which `deadline auth status` uses to check your credentials.

Submitting fails with an AccessDenied error for `deadline:ListQueueEnvironments`  
Add `deadline:ListQueueEnvironments` and `deadline:GetQueueEnvironment` to the policy, for the farm or queue that you submit to.

`Missing '--farm-id' or default Farm ID configuration`  
The default profile for the Deadline Cloud tools changed, and the new profile has no default farm and queue. Run `deadline config set defaults.farm_id` and `deadline config set defaults.queue_id`, or choose the farm and queue in a submitter.

`Cross-account pass role is not allowed` when you create a queue or fleet  
If you created the queue or fleet role in the last few minutes, the role might not be available yet, even if it's in the same account. Wait a few minutes and try again.

A submitter keeps saying that you need to sign in  
Update the submitter to the latest version. Older submitters don't support console sign-in profiles. For more information, see [Tool support for console sign-in profiles](monitor-sign-in-aws-credentials.md#monitor-console-tool-support).

## Related topics
<a name="without-idc-related"></a>
+ [How permissions work in Deadline Cloud](permissions-overview.md)
+ [Sign in to the desktop monitor with the AWS Management Console or an AWS profile](monitor-sign-in-aws-credentials.md)
+ [Identity-based policy examples for Deadline Cloud](security_iam_id-based-policy-examples.md)
+ [Allow access only from your VPC](restrict-network-access.md#restrict-network-access-vpc)
+ [Set up a virtual workstation for Deadline Cloud with a script](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-virtual-workstation.html) in the *Deadline Cloud Developer Guide*