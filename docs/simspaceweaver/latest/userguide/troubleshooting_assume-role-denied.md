End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# AssumeRoleAccessDenied

You might receive the following error if your simulation fails to start:

```
Unable to assume role arn:aws:iam::111122223333:role/weaver-`project-name`-app-role; verify the role exists and has trust policy on SimSpace Weaver
```

You can receive this error if one of the following is true about the AWS Identity and Access Management (IAM)
role for your simulation:

- The Amazon Resource Name (ARN) refers to an IAM role that
  doesn't exist.
- The trust policy for the IAM role that doesn't allow the name of the new
  simulation to assume the role.
  Check to make sure that the role exists. If the role exists, check your trust policy
  for the role. The `aws:SourceArn` in following example trust policy only
  allows a simulation (in account 111122223333) whose name begins with
  `MySimulation` to assume the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "simspaceweaver.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:simspaceweaver:us-west-2:111122223333:simulation/MySimulation*"
 }
 }
 }
 ]
}`

```

To allow another simulation whose name begins with `MyOtherSimulation` to
assume the role, the trust policy must be modified as in the following edited
example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "simspaceweaver.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:simspaceweaver:us-west-2:111122223333:simulation/MySimulation*",
 "arn:aws:simspaceweaver:us-west-2:111122223333:simulation/MyOtherSimulation*"
 ]
 }
 }
 }
 ]
}`

```
