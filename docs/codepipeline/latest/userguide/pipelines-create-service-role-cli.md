# Create the CodePipeline service role

(CLI)

Before you create a pipeline with the AWS CLI or CloudFormation, you must create a CodePipeline
service role for your pipeline and attach the service role policy and the trust policy.
To use the CLI to create your service role, use the steps below to first create a trust
policy JSON and the role policy JSON as separate files in the directory where you will
run the CLI commands.

###### Note

We recommend that you allow only administrative users to create any service role.
A person with permissions to create a role and attach any policy can escalate their
own permissions. Instead, create a policy that allows them to create only the roles
that they need or have an administrator create the service role on their
behalf.

1. In a terminal window, enter the following command to create a file named
   `TrustPolicy.json`, where you will paste the role policy JSON.
   This example uses VIM.

```
vim TrustPolicy.json
```

2. Paste the following JSON into the file.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "codepipeline.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

To save and exit the file, enter the following VIM command:

```
:wq
```

3. In a terminal window, enter the following command to create a file named
   `RolePolicy.json`, where you will paste the role policy JSON.
   This example uses VIM.

```
vim RolePolicy.json
```

4. Paste the JSON policy into the file. Use the minimum service role policy as
   provided in [CodePipeline service role policy](how-to-custom-role.md#how-to-custom-role-policy "how-to-custom-role.md#how-to-custom-role-policy"). In addition, add the
   appropriate permissions to your service role based on the actions you plan to
   use. For a list of actions and a link to each action's required service role
   permissions, see [Add permissions to the CodePipeline
   service role](how-to-custom-role.md#how-to-update-role-new-services "how-to-custom-role.md#how-to-update-role-new-services").

Make sure to scope down permissions as much as possible by
scoping
down to the resource level in the
`Resource` field.

To save and exit the file, enter the following VIM command:

```
:wq
```

5. Enter the following command to create the role and attach the trust role
   policy. The policy name format is normally the same as the role name format.
   This examples uses the role name `MyRole` and the policy
   `TrustPolicy` that was created as a separate file.

```
aws iam create-role --role-name MyRole --assume-role-policy-document file://TrustPolicy.json
```

6. Enter the following command to create the role policy and attach it to the
   role. The policy name format is normally the same as the role name format. This
   examples uses the role name `MyRole` and the policy
   `MyRole` that was created as a separate file.

```
aws iam put-role-policy --role-name MyRole --policy-name RolePolicy --policy-document file://RolePolicy.json
```

7. To view the created role name and trust policy, enter the following command
   for the role named `MyRole`:

```
aws iam get-role --role-name MyRole
```

8. Use the service role ARN when you create your pipeline with the AWS CLI or
   CloudFormation.
