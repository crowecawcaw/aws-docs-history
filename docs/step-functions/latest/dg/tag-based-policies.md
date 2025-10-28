# Creating tag-based IAM policies in Step Functions

Step Functions supports policies based on tags. For example, you could restrict access to all
Step Functions resources that include a tag with the key `environment` and the value
`production`.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "states:TagResource",
 "states:UntagResource",
 "states:DeleteActivity",
 "states:DeleteStateMachine",
 "states:StopExecution"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/environment": "production"}
 }
 }
 ]
}`

```

This policy will `Deny` the ability to delete state machines or activities,
stop executions, and add or delete new tags for all resources that have been tagged as
`environment/production`.

For tag-based authorization, state machine execution resources as shown in the following example inherit the tags associated with a state machine.

```
arn:`partition`:states:`region`:`account-id`:execution:`<StateMachineName>:<ExecutionId>`
```

When you call [DescribeExecution](../apireference/API_DescribeExecution.md "../apireference/API_DescribeExecution.md") or other APIs in which you specify the execution resource ARN, Step Functions uses tags associated with the state machine to accept or deny the request while performing tag-based authorization. This helps you allow or deny access to state machine executions at the state machine level.

For more information about tagging, see the following:

- [Tagging state machines and activities in Step Functions](sfn-best-practices.md#concepts-tagging "sfn-best-practices.md#concepts-tagging")
- [Controlling Access Using IAM
  Tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md")
