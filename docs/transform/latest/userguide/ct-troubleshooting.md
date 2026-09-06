# Troubleshooting

Checking system health
You no longer need to start a local server; the `atx ct server`
command is deprecated. Verify the system is reachable with
`atx ct status --health`.

Discovery scan returns zero repositories
For local sources, verify that `--path` points to a parent
directory that contains repositories as subdirectories (for example,
`/home/user/repos`), not to a repository directly (for example,
`/home/user/repos/my-app`). The scanner looks for child directories that
contain a `.git` folder.

SETUP\_REQUIRED error
The source exists in your account but credentials are not configured on this
machine. Run `atx ct source add --name `name`` to
configure credentials locally.

AUTH\_REQUIRED error
No valid token found for the source. Verify your token is correct and has the
required scopes. For GitHub, ensure the token has `repo` scope. For GitLab,
ensure `api` scope.

INVALID\_INPUT error
Verify you are using the correct analysis type name. Valid values are:
`rapid-techdebt-analysis`, `tech-debt-comprehensive`,
`security`, `agentic-readiness`,
`modernization-readiness`, `custom`.

Permission errors during remediation
Remediation creates branches and pull/merge requests, which requires write
access to the repository. Update your token with write permissions. For GitHub, ensure
full `repo` scope. For GitLab, ensure `api` scope. For Bitbucket,
ensure `write:repository:bitbucket` and
`write:pullrequest:bitbucket` scopes.

Security agent setup fails
Verify your IAM user or role has the required AWS CloudFormation, IAM, and Amazon S3
permissions listed in the Security agent setup section of
[How AWS Transform continuous modernization works](continuous-modernization.md#ct-how-it-works "continuous-modernization.md#ct-how-it-works"). Check the status with
`atx ct setup security-agent --status`.

Security analysis or security agent setup unavailable in a Region
The `security` analysis type is not available in Canada (Central)
(`ca-central-1`), Europe (London) (`eu-west-2`), or Asia Pacific
(Seoul) (`ap-northeast-2`). Run `security` analyses and
`atx ct setup security-agent` from a supported Region. The other analysis types
are unaffected. See the Security agent setup section of
[How AWS Transform continuous modernization works](continuous-modernization.md#ct-how-it-works "continuous-modernization.md#ct-how-it-works").

Remote provisioning fails with a permissions error
Provisioning, updating, and tearing down remote infrastructure
(`atx ct remote provision`, `update`, `teardown`) creates
and modifies AWS CloudFormation stacks and IAM roles, and requires administrator permissions. To run
analyses and remediations on already-provisioned infrastructure with least privilege, attach
`AWSTransformInfrastructureExecutorAccessEC2` or
`AWSTransformInfrastructureExecutorAccessBatch`. For details, see the compute
options in
[How AWS Transform continuous modernization works](continuous-modernization.md#ct-how-it-works "continuous-modernization.md#ct-how-it-works").

Remote network discovery returns no subnets
Remote compute must run in private subnets, and
`atx ct remote network discover` excludes public subnets. If no private subnets
exist, create networking with `atx ct remote network create`.

AWS Batch jobs fail with InsufficientFreeAddressesInSubnet
Each AWS Batch job needs one free private IPv4 address, and AWS Batch fails
a job it cannot place rather than queueing it. Run
`atx ct remote network discover --vpc `vpc-id` --json` and
read `availableIpCount` for every subnet in the stack, then compare the smallest
count against the concurrency limit for the analysis type you are running. Free addresses do
not add up across subnets — capacity is the smallest count, not the total. To resolve, use
larger subnets, remove the smallest subnet from the stack, submit fewer repositories at a time,
or run with `--mode ec2`, which uses one address in total. For the arithmetic and
minimum subnet sizes, see
[Sizing subnets and concurrency](ct-working-with.md#ct-remote-sizing "ct-working-with.md#ct-remote-sizing").

Repositories stay pending for a long time with no error
The run is being paced. AWS Transform limits how many remote jobs run at the same time in
an AWS account and Region — as few as 5 for `security` analysis — and holds the
rest until capacity frees up. A run can also wait for free IP addresses in your subnets. Both
appear as `pending` in `atx ct remote status`, which does not distinguish
waiting from running. Confirm the limit for your analysis type in
[Sizing subnets and concurrency](ct-working-with.md#ct-remote-sizing "ct-working-with.md#ct-remote-sizing") and expect the run to
progress at that rate. Do not submit the run again — resubmitting adds jobs that wait behind
the same limit. If free addresses are plentiful but jobs still wait, the run is at the
concurrency limit for its type and larger subnets will not help.

Remote status reports no jobs for a submission that was accepted
Expected while every job in the submission is still waiting for capacity.
AWS Transform records job details when the first job starts, so
`atx ct remote status --batch` can report nothing until then. Wait and run the
command again.

Repositories fail with no reason after several hours
A job waits for capacity for up to about 33 hours before AWS Transform abandons it.
Jobs are also abandoned if AWS Transform cannot evaluate subnet capacity, which happens on stacks
provisioned before capacity checking was added. Update the stack with
`atx ct remote update --mode batch --execute --ack`, then submit the affected
repositories again in smaller groups. If the run was large, size the subnets for the
concurrency limit of the analysis type first — see
[Sizing subnets and concurrency](ct-working-with.md#ct-remote-sizing "ct-working-with.md#ct-remote-sizing").

Remote run cannot clone repositories
Remote containers use tokens stored in AWS Secrets Manager. Register a
token for each source with
`atx ct remote credentials --source `name`--token`token``
before running remote analysis or remediation.

Schedule fails to run
Schedules run on remote infrastructure. Provision an Amazon EC2 or Batch stack
with `atx ct remote provision` before creating a schedule, and confirm the
schedule is enabled with
`atx ct schedule get `name``.

Continuous modernization not visible in the web application
If continuous modernization does not appear after you sign in to the AWS Transform web
application, sign in with the IAM credentials of the AWS account where AWS Transform is enabled
instead of AWS IAM Identity Center. For steps, see
[AWS Transform web application](ct-working-with.md#ct-web-application "ct-working-with.md#ct-web-application").
