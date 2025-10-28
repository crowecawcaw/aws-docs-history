# Amazon ECS Anywhere IAM role

When you register an on-premises server or virtual machine (VM) to your cluster, the
server or VM requires an IAM role to communicate with AWS APIs. You only need to create
this IAM role once for each AWS account. However, this IAM role must be associated
with each server or VM that you register to a cluster. This role is the
`ECSAnywhereRole`. You can create this role manually. Alternatively, Amazon ECS
can create the role on your behalf when you register an external instance in the AWS Management Console.
You can use IAM console search to search for `ecsAnywhereRole` and see if your
account already has the role. For more information, see [IAM console search](../../../IAM/latest/UserGuide/console_search.md "../../../IAM/latest/UserGuide/console_search.md") in the
_IAM user guide_.

AWS provides two managed IAM policies that can be used when creating the ECS Anywhere
IAM role, the `AmazonSSMManagedInstanceCore` and
`AmazonEC2ContainerServiceforEC2Role` policies. The
`AmazonEC2ContainerServiceforEC2Role` policy includes permissions that likely
provide more access than you need. Therefore, depending on your specific use case, we
recommend that you create a custom policy adding only the permissions from that policy that
you require in it. For more information, see [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").

The task execution IAM role grants the Amazon ECS container agent permission to make AWS
API calls on your behalf. When a task execution IAM role is used, it must be specified in
your task definition. For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

The task execution role is required if any of the following conditions apply:

- You're sending container logs to CloudWatch Logs using the `awslogs` log
  driver.
- Your task definition specifies a container image that's hosted in an Amazon ECR private
  repository. However, if the `ECSAnywhereRole` role that's associated with
  your external instance also includes the permissions necessary to pull images from
  Amazon ECR then your task execution role doesn't need to include them.

## Creating the Amazon ECS Anywhere role

Replace all `user input` with your own information.

1. Create a local file named `ssm-trust-policy.json` with the
   following trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {"Service": [
 "ssm.amazonaws.com"
 ]},
 "Action": "sts:AssumeRole"
 }
}`

```

2. Create the role and attach the trust policy by using the following AWS CLI
   command.

```
`aws iam create-role --role-name `ecsAnywhereRole` --assume-role-policy-document file://ssm-trust-policy.json`
```

3. Attach the AWS managed policies by using the following command.

```
`aws iam attach-role-policy --role-name `ecsAnywhereRole` --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
aws iam attach-role-policy --role-name `ecsAnywhereRole` --policy-arn arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role`
```

You can also use the IAM custom trust policy workflow to create the role. For more
information, see [Creating a role using
custom trust policies (console)](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the _IAM User
Guide_.
