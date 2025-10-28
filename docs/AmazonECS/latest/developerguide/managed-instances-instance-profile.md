# Amazon ECS Managed Instances instance profile

An instance profile is an IAM container that holds exactly one IAM role and allows
Amazon ECS Managed Instances to assume that role securely. The instance profile contains an instance
role that the ECS agent assumes to register instances with clusters and communicate with the
ECS service.

###### Important

If you are using Amazon ECS Managed Instances with the AWS-managed Infrastructure policy, the instance profile must be named `ecsInstanceRole`. If you are using a custom policy for the Infrastructure role, the instance profile can have an alternative name.

## Create the role with the trust policy

Replace all `user input` with your own
information.

1. Create a file named `ecsInstanceRole-trust-policy.json` that
   contains the trust policy to use for the IAM role. The file should contain the
   following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": { "Service": "ec2.amazonaws.com"},
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Use the following AWS CLI command to create a role named
   `ecsInstanceRole` by using the trust policy
   that you created in the previous step.

```
`aws iam create-role \
 --role-name ecsInstanceRole \
 --assume-role-policy-document file://`ecsInstanceRole-trust-policy.json``
```

3. Attach the AWS managed `AmazonECSInstanceRolePolicyForManagedInstances` policy to the `ecsInstanceRole`
   role.

```
`aws iam attach-role-policy \
 --role-name ecsInstanceRole \
 --policy-arn arn:aws:iam::aws:policy/AmazonECSInstanceRolePolicyForManagedInstances`
```

###### Note

If you choose to apply least-privilege permissions and specify your own permissions instead, you can add the following permissions to help with troubleshooting task-related issues with Amazon ECS Managed Instances:

    * `ecs:StartTelemetrySession`
    * `ecs:PutSystemLogEvents`

You can also use the IAM console's **Custom trust policy** workflow
to create the role. For more information, see [Creating a role using
custom trust policies (console)](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the _IAM User
Guide_.

After you create the file, you must grant your user permission to pass the role to
Amazon ECS.

## Create the instance profile using the AWS CLI

After creating the role, create the instance profile using the AWS CLI:

```
aws iam create-instance-profile --instance-profile-name ecsInstanceRole
```

Add the role to the instance profile:

```
aws iam add-role-to-instance-profile \
   --instance-profile-name ecsInstanceRole \
   --role-name ecsInstanceRole
```

Verify the profile was created successfully:

```
aws iam get-instance-profile --instance-profile-name ecsInstanceRole
```
