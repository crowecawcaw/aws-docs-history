# Restrict user access to certain notebook instances

To restrict access for certain users to specific Braket notebook instances, you can
add a _deny permissions_ policy to a specific role, user, or
group.

The following example uses [policy variables](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") to efficiently restrict permissions to start, stop, and
access specific notebook instances in the AWS account `123456789012`, which
is named according to the user who should have access (for example, user
`Alice` would have access to a notebook instance named
`amazon-braket-Alice`).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyCreateDeleteUpdateNotebookInstances",
 "Effect": "Deny",
 "Action": [
 "sagemaker:CreateNotebookInstance",
 "sagemaker:DeleteNotebookInstance",
 "sagemaker:UpdateNotebookInstance",
 "sagemaker:CreateNotebookInstanceLifecycleConfig",
 "sagemaker:DeleteNotebookInstanceLifecycleConfig",
 "sagemaker:UpdateNotebookInstanceLifecycleConfig"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DenyDescribeStartStopNotebookInstances",
 "Effect": "Deny",
 "Action": [
 "sagemaker:DescribeNotebookInstance",
 "sagemaker:StartNotebookInstance",
 "sagemaker:StopNotebookInstance"
 ],
 "NotResource": [
 "arn:aws:sagemaker:*:123456789012:notebook-instance/amazon-braket-${aws:username}"
 ]
 },
 {
 "Sid": "DenyNotebookInstanceUrl",
 "Effect": "Deny",
 "Action": [
 "sagemaker:CreatePresignedNotebookInstanceUrl"
 ],
 "NotResource": [
 "arn:aws:sagemaker:*:123456789012:notebook-instance/amazon-braket-${aws:username}*"
 ]
 }
 ]
}`

```
