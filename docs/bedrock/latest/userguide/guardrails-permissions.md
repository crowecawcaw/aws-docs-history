# Set up permissions to use Amazon Bedrock Guardrails

To set up a role with permissions for guardrails, create an IAM role and attach the following permissions by following the steps at [Creating a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

If you're using guardrails with an agent, attach the permissions to a service role with
permissions to create and manage agents. You can set up this role in the console or create a
custom role by following the steps at [Create a service role for Amazon Bedrock Agents](agents-permissions.md "agents-permissions.md").

## Permissions to create and manage guardrails for the policy role

Append the following statement to the `Statement` field in the policy
for your role to use guardrails.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateAndManageGuardrails",
 "Effect": "Allow",
 "Action": [
 "bedrock:CreateGuardrail",
 "bedrock:CreateGuardrailVersion",
 "bedrock:DeleteGuardrail",
 "bedrock:GetGuardrail",
 "bedrock:ListGuardrails",
 "bedrock:UpdateGuardrail"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Permissions for invoking guardrails

to filter content

Append the following statement to the `Statement` field in the policy
for the role to allow for model inference and to invoke guardrails.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "InvokeFoundationModel",
 "Effect": "Allow",
 "Action": [
 "bedrock:InvokeModel",
 "bedrock:InvokeModelWithResponseStream"
 ],
 "Resource": [
 "arn:aws:bedrock:`us-east-1`::foundation-model/*"
 ]
 },
 {
 "Sid": "ApplyGuardrail",
 "Effect": "Allow",
 "Action": [
 "bedrock:ApplyGuardrail"
 ],
 "Resource": [
 "arn:aws:bedrock:`us-east-1`:`123456789012`:guardrail/`guardrail-id`"
 ]
 }
 ]
}`

```
