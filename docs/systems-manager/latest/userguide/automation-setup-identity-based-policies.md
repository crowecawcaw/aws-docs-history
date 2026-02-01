• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Setting up identity based policies examples

The following sections provide example IAM identity-based policies for AWS Systems Manager Automation service.
For more information about how to create an IAM identity-based policy using these example JSON Policy documents,
see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Note

All examples contain fictitious account IDs. The account ID shouldn't be specified in the Amazon Resource
Name (ARN) for AWS owned public documents.

**Examples**

- [Example 1: Allow a user to run an automation document and view the automation execution](#automation-setup-identity-based-policies-example-1 "#automation-setup-identity-based-policies-example-1")
- [Example 2: Allow a user to run a specific version of an automation document](#automation-setup-identity-based-policies-example-2 "#automation-setup-identity-based-policies-example-2")
- [Example 3: Allow a user to execute automation documents with a specific tag](#automation-setup-identity-based-policies-example-3 "#automation-setup-identity-based-policies-example-3")
- [Example 4: Allow a user to run an automation document when a specific tag parameter is provided for the automation execution](#automation-setup-identity-based-policies-example-4 "#automation-setup-identity-based-policies-example-4")

## Example 1: Allow a user to run an automation document and view the automation execution

The following example IAM policy allows a user to do the following:

- Run the automation document specified in the policy. The
  name of the document is determined by the following entry.

```
arn:aws:ssm:*:`111122223333`:document/{{DocumentName}}
```

- Stop and send signals to an automation execution.
- View details about the automation execution after it has been started.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "ssm:StartAutomationExecution",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:document/{{DocumentName}}",
 "arn:aws:ssm:*:`111122223333`:automation-execution/*"
 ]
 },
 {
 "Action": [
 "ssm:StopAutomationExecution",
 "ssm:GetAutomationExecution",
 "ssm:DescribeAutomationExecutions",
 "ssm:DescribeAutomationStepExecutions",
 "ssm:SendAutomationSignal"
 ],
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:automation-execution/*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

## Example 2: Allow a user to run a specific version of an automation document

The following example IAM policy allows a user to run a specific version of an automation document:

- The name of the automation document is determined by the following entry.

```
arn:aws:ssm:*:`111122223333`:document/{{DocumentName}}
```

- The version of the automation document is determined by the following entry.

```
"ssm:DocumentVersion": "5"
```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "ssm:StartAutomationExecution",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:document/{{DocumentName}}"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "ssm:DocumentVersion": ["5"]
 }
 }
 },
 {
 "Action": [
 "ssm:StartAutomationExecution"
 ],
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:automation-execution/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "ssm:StopAutomationExecution",
 "ssm:GetAutomationExecution",
 "ssm:DescribeAutomationExecutions",
 "ssm:DescribeAutomationStepExecutions",
 "ssm:SendAutomationSignal"
 ],
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:automation-execution/*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

## Example 3: Allow a user to execute automation documents with a specific tag

The following example IAM policy allows a user to run any automation document that has a specific tag:

- The name of the automation document is determined by the following entry.

```
arn:aws:ssm:*:`111122223333`:document/{{DocumentName}}
```

- The tag of the automation document is determined by the following entry.

```
"ssm:DocumentVersion": "5"
```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "ssm:StartAutomationExecution",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:document/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/stage": "production"
 }
 }
 },
 {
 "Action": [
 "ssm:StartAutomationExecution"
 ],
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:automation-execution/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "ssm:StopAutomationExecution",
 "ssm:GetAutomationExecution",
 "ssm:DescribeAutomationExecutions",
 "ssm:DescribeAutomationStepExecutions",
 "ssm:SendAutomationSignal"
 ],
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:automation-execution/*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

## Example 4: Allow a user to run an automation document when a specific tag parameter is provided for the automation execution

The following example IAM policy grants permissions to a user to run automation documents when a specific tag parameter is provided for the automation execution:

- Run the automation document specified in the policy. The
  name of the document is determined by the following entry.

```
arn:aws:ssm:*:`111122223333`:document/{{DocumentName}}
```

- Must provide a specific tag parameter for the automation execution. The tag parameter for the automation execution resource is determined by the following entry.

```
"aws:ResourceTag/stage": "production"
```

- Stop and send signals to automation executions that have the specified tag.
- View details about the automation executions that have the specified tag.
- Add the specified tag to SSM resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "ssm:StartAutomationExecution",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:document/{{DocumentName}}"
 ]
 },
 {
 "Action": [
 "ssm:StartAutomationExecution",
 "ssm:StopAutomationExecution",
 "ssm:GetAutomationExecution",
 "ssm:DescribeAutomationExecutions",
 "ssm:DescribeAutomationStepExecutions",
 "ssm:SendAutomationSignal"
 ],
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:automation-execution/*"
 ],
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/environment": "beta"
 }
 }
 },
 {
 "Action": "ssm:AddTagsToResource",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:ssm:*:`111122223333`:automation-execution/*"
 ]
 }
 ]
}`

```
