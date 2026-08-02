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
[AWS Transform web application (Optional)](ct-working-with.md#ct-web-application "ct-working-with.md#ct-web-application").
