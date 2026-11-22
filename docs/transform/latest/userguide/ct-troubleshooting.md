

# Troubleshooting

Checking system health  
You no longer need to start a local server; the `atx ct server` command is deprecated. Verify the system is reachable with `atx ct status --health`.

Finding the error for a failed analysis or remediation  
When an analysis or remediation hits an error for a repository, you can find an error record in the `/aws/TransformContinuousModernization` CloudWatch log group in the AWS account and Region where the analysis or remediation ran.  
Each repository of each analysis or remediation has its own log stream, named `{{mode}}/{{run-id}}/{{source}}%3A%3A{{repo}}/logs`. {{mode}} is the `computeMode` value in the following table, and {{run-id}} is the analysis or remediation ID. AWS Transform URL-encodes the source and repository name, so the `::` between them appears as `%3A%3A`. AWS Transform shortens a very long name in the middle.  
Each record is a JSON object with the following fields.  


<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><code>timestamp</code></td><td>When the error happened.</td></tr>
  <tr><td><code>logClass</code></td><td>Always <code>error</code>.</td></tr>
  <tr><td><code>resourceType</code></td><td><code>analysis</code> or <code>remediation</code>.</td></tr>
  <tr><td><code>analysisId</code> or <code>remediationId</code></td><td>The ID of the analysis or remediation.</td></tr>
  <tr><td><code>repositoryName</code></td><td>The repository, as <code>source::repo</code>.</td></tr>
  <tr><td><code>computeMode</code></td><td>Where the run happened: <code>local</code>, <code>batch</code> (AWS Batch), <code>ec2</code> (Amazon EC2), or <code>aws-managed</code>.</td></tr>
  <tr><td><code>message</code></td><td>The error message.</td></tr>
  <tr><td><code>rawLogGroup</code> and <code>rawLogStream</code></td><td>AWS Batch and Amazon EC2 runs only. The location of the run's full log.</td></tr>
</tbody>
</table>

Each execution of a scheduled analysis has its own analysis ID. To find it, use `atx ct analysis list --schedule-id {{schedule-id}}`.  
To read the errors of one analysis, use the following command. Replace {{analysis-id}} with the ID of the analysis.  

```bash
aws logs filter-log-events --log-group-name /aws/TransformContinuousModernization \
  --filter-pattern '{ $.analysisId = "{{analysis-id}}" }'
```
Occasionally, the log group contains a duplicate record.

No error records in /aws/TransformContinuousModernization  
If no error records appear, the credentials that ran the analysis or remediation are usually missing permissions on the log group. The credentials need permissions on two resources:  
+ `logs:CreateLogGroup` and `logs:PutRetentionPolicy` on the log group, `arn:aws:logs:{{region}}:{{account-id}}:log-group:/aws/TransformContinuousModernization`.
+ `logs:CreateLogStream` and `logs:PutLogEvents` on the log group's streams, `arn:aws:logs:{{region}}:{{account-id}}:log-group:/aws/TransformContinuousModernization:log-stream:*`.
Who grants these permissions depends on how the analysis or remediation runs:  
+ Roles that `atx ct remote provision` creates for AWS Batch and Amazon EC2 have these permissions. If you provisioned the stack with an earlier version of the AWS Transform CLI, run `atx ct remote update` to add them.
+ For runs with `--mode aws-managed`, the execution role that AWS Transform creates for you, for example when you choose **Create one for me** in the AWS Transform web application, has these permissions.
+ For local runs, and for roles that you create yourself, add these permissions to the credentials or role that runs the analysis or remediation.
The following example policy grants these permissions. Replace {{region}} and {{account-id}} with your values.  

```json
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["logs:CreateLogGroup", "logs:PutRetentionPolicy"],
      "Resource": "arn:aws:logs:{{region}}:{{account-id}}:log-group:/aws/TransformContinuousModernization"
    },
    {
      "Effect": "Allow",
      "Action": ["logs:CreateLogStream", "logs:PutLogEvents"],
      "Resource": "arn:aws:logs:{{region}}:{{account-id}}:log-group:/aws/TransformContinuousModernization:log-stream:*"
    }
  ]
}
```
A missing permission doesn't change the result of the analysis or remediation. AWS Transform still runs it, but doesn't write the error record.

Discovery scan returns zero repositories  
For local sources, verify that `--path` points to a parent directory that contains repositories as subdirectories (for example, `/home/user/repos`), not to a repository directly (for example, `/home/user/repos/my-app`). The scanner looks for child directories that contain a `.git` folder.

SETUP\_REQUIRED error  
The source exists in your account but credentials are not configured on this machine. Run `atx ct source add --name {{name}}` to configure credentials locally.

AUTH\_REQUIRED error  
No valid token found for the source. Verify your token is correct and has the required scopes. For GitHub, ensure the token has `repo` scope. For GitLab, ensure `api` scope.

INVALID\_INPUT error  
Verify you are using the correct analysis type name. Valid values are: `rapid-techdebt-analysis`, `tech-debt-comprehensive`, `security`, `agentic-readiness`, `modernization-readiness`, `graviton-readiness`, `aws-health-readiness`, `custom`.

AWS Health readiness findings don't name affected resources  
The analysis couldn't read AWS Health. Check that the credentials that run the analysis have the AWS Health read permissions. Also check that your account has an AWS Support plan that includes the AWS Health API. The findings themselves don't depend on AWS Health. See [Permissions and AWS Support plan](ct-aws-health.md#ct-aws-health-permissions).

Permission errors during remediation  
Remediation creates branches and pull/merge requests, which requires write access to the repository. Update your token with write permissions. For GitHub, ensure full `repo` scope. For GitLab, ensure `api` scope. For Bitbucket, ensure `write:repository:bitbucket` and `write:pullrequest:bitbucket` scopes.

Security agent setup fails  
Verify your IAM user or role has the required AWS CloudFormation, IAM, and Amazon S3 permissions listed in the Security agent setup section of [How AWS Transform continuous modernization works](continuous-modernization.md#ct-how-it-works). Check the status with `atx ct setup security-agent --status`.

Security analysis or security agent setup unavailable in a Region  
The `security` analysis type is not available in Canada (Central) (`ca-central-1`), Europe (London) (`eu-west-2`), or Asia Pacific (Seoul) (`ap-northeast-2`). Run `security` analyses and `atx ct setup security-agent` from a supported Region. The other analysis types are unaffected. See the Security agent setup section of [How AWS Transform continuous modernization works](continuous-modernization.md#ct-how-it-works).

Remote provisioning fails with a permissions error  
Provisioning, updating, and tearing down remote infrastructure (`atx ct remote provision`, `update`, `teardown`) creates and modifies AWS CloudFormation stacks and IAM roles, and requires administrator permissions. To run analyses and remediations on already-provisioned infrastructure with least privilege, attach `AWSTransformInfrastructureExecutorAccessEC2` or `AWSTransformInfrastructureExecutorAccessBatch`. For details, see the compute options in [How AWS Transform continuous modernization works](continuous-modernization.md#ct-how-it-works).

Remote network discovery returns no subnets  
Remote compute must run in private subnets, and `atx ct remote network discover` excludes public subnets. If no private subnets exist, create networking with `atx ct remote network create`.

AWS Batch jobs fail with InsufficientFreeAddressesInSubnet  
Each AWS Batch job needs one free private IPv4 address, and AWS Batch fails a job it cannot place rather than queueing it. Run `atx ct remote network discover --vpc {{vpc-id}} --json` and read `availableIpCount` for every subnet in the stack, then compare the smallest count against the concurrency limit for the analysis type you are running. Free addresses do not add up across subnets — capacity is the smallest count, not the total. To resolve, use larger subnets, remove the smallest subnet from the stack, submit fewer repositories at a time, or run with `--mode ec2`, which uses one address in total. For the arithmetic and minimum subnet sizes, see [Sizing subnets and concurrency](ct-working-with.md#ct-remote-sizing).

Repositories stay pending for a long time with no error  
The run is being paced. AWS Transform limits how many remote jobs run at the same time in an AWS account and Region — as few as 5 for `security` analysis — and holds the rest until capacity frees up. A run can also wait for free IP addresses in your subnets. Both appear as `pending` in `atx ct remote status`, which does not distinguish waiting from running. Confirm the limit for your analysis type in [Sizing subnets and concurrency](ct-working-with.md#ct-remote-sizing) and expect the run to progress at that rate. Do not submit the run again — resubmitting adds jobs that wait behind the same limit. If free addresses are plentiful but jobs still wait, the run is at the concurrency limit for its type and larger subnets will not help.

Remote status reports no jobs for a submission that was accepted  
Expected while every job in the submission is still waiting for capacity. AWS Transform records job details when the first job starts, so `atx ct remote status --batch` can report nothing until then. Wait and run the command again.

Repositories fail with no reason after several hours  
A job waits for capacity for up to about 33 hours before AWS Transform abandons it. Jobs are also abandoned if AWS Transform cannot evaluate subnet capacity, which happens on stacks provisioned before capacity checking was added. Update the stack with `atx ct remote update --mode batch --execute --ack`, then submit the affected repositories again in smaller groups. If the run was large, size the subnets for the concurrency limit of the analysis type first — see [Sizing subnets and concurrency](ct-working-with.md#ct-remote-sizing).

Remote run cannot clone repositories  
Remote containers use tokens stored in AWS Secrets Manager. Register a token for each source with `atx ct remote credentials --source {{name}} --token {{token}}` before running remote analysis or remediation.

Schedule fails to run  
Schedules run on remote infrastructure. Provision an Amazon EC2 or Batch stack with `atx ct remote provision` before creating a schedule, and confirm the schedule is enabled with `atx ct schedule get {{name}}`.

Continuous modernization not visible in the web application  
If continuous modernization does not appear after you sign in to the AWS Transform web application, sign in with the IAM credentials of the AWS account where AWS Transform is enabled instead of AWS IAM Identity Center. For steps, see [AWS Transform web application](ct-working-with.md#ct-web-application).

**Generate specialized skill** is unavailable  
Generating a specialized skill needs a deployed AWS Batch or Amazon EC2 stack and an up-to-date dispatcher. Deploy or update them on the **Settings** tab. The option is also unavailable when the group has no open findings, when a skill is already being generated for it, or when you don't have permission to generate skills.

Group doesn't start when you remediate a plan  
The **Remediate** dialog lists each group that doesn't start under **Not started with the rest**, with the reason. For example, the group has more than 250 open findings in one repository, one of its repositories was uploaded rather than connected, or its approved skill version is no longer in your registry. To approve a group again, choose **Change** in its row. For more information, see [Plan limits](ct-remediation-plans.md#ct-plans-limits).

Remediation plans aren't available for this account yet  
Remediation plans aren't available in your account yet. To remediate findings in the meantime, create remediations from the **All findings** view.