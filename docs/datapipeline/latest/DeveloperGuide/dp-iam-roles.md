AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# IAM Roles for AWS Data Pipeline

AWS Data Pipeline uses AWS Identity and Access Management roles. The permissions policies attached to IAM roles
determine what actions AWS Data Pipeline and your applications can perform, and what AWS
resources they can access. For more information, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the
_IAM User Guide_.

AWS Data Pipeline requires two IAM roles:

- **The pipeline role** controls AWS Data Pipeline access to your AWS
  resources. In pipeline object definitions, the `role` field specifies
  this role.
- **The EC2 instance role** controls the access that
  applications running on EC2 instances, including the EC2 instances in Amazon EMR clusters, have to AWS resources. In pipeline
  object definitions, the `resourceRole` field specifies this
  role.

###### Important

If you created a pipeline before October 3, 2022 using the AWS Data Pipeline console with default roles, AWS Data Pipeline created the `DataPipelineDefaultRole` for you and attached the `AWSDataPipelineRole` managed policy to the role. As of October 3, 2022, the `AWSDataPipelineRole` managed policy is deprecated and the pipeline role must be specified for a pipeline when using the console.

We recommend that you review existing pipelines and determine if the `DataPipelineDefaultRole` is associated with the pipeline and whether the `AWSDataPipelineRole` is attached to that role. If so, review the access that this policy allows to ensure it is appropriate for your security requirements. Add, update, or replace the policies and policy statements attached to this role as necessary. Alternatively, you can update a pipeline to use a role that you create with different permissions policies.

## Example Permissions Policies for AWS Data Pipeline Roles

Each role has one or more permissions policies attached to it that determine the
AWS resources that the role can access and the actions that the role can perform.
This topic provides an example permissions policy for the pipeline role. It also
provides the contents of the `AmazonEC2RoleforDataPipelineRole`, which is
the managed policy for the default EC2 instance role,
`DataPipelineDefaultResourceRole`.

### Example Pipeline Role Permissions Policy

The example policy that follows is scoped to allow essential functions that AWS Data Pipeline requires to run a pipeline with Amazon EC2 and Amazon EMR resources. It also provides permissions to access other AWS resources, such as Amazon Simple Storage Service and Amazon Simple Notification Service, that many pipelines require. If the objects defined in a pipeline do not require the resources of an AWS service, we strongly recommend that you remove permissions to access that service. For example, if your pipeline does not define a [DynamoDBDataNode](dp-object-dynamodbdatanode.md "dp-object-dynamodbdatanode.md") or use the [SnsAlarm](dp-object-snsalarm.md "dp-object-snsalarm.md") action, we recommend that you remove the allow statements for those actions.

- Replace `111122223333` with your AWS account ID.
- Replace `NameOfDataPipelineRole` with the name of pipeline role (the role to which this policy is attached).
- Replace `NameOfDataPipelineResourceRole` with the name of EC2 instance role.
- Replace `us-west-1` with the appropriate Region for your application.

### Default Managed Policy for the EC2 Instance Role

The contents of the `AmazonEC2RoleforDataPipelineRole` is shown below. This is the managed policy attached to the default resource role for AWS Data Pipeline, `DataPipelineDefaultResourceRole`. When you define a resource role for your pipeline, we recommend that you begin with this permissions policy and then remove permissions for AWS service actions that are not required.

Version 3 of the policy is shown, which is the most recent version at the time of this writing. View the most recent version of the policy using the IAM console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "cloudwatch:*",
 "datapipeline:*",
 "dynamodb:*",
 "ec2:Describe*",
 "elasticmapreduce:AddJobFlowSteps",
 "elasticmapreduce:Describe*",
 "elasticmapreduce:ListInstance*",
 "elasticmapreduce:ModifyInstanceGroups",
 "rds:Describe*",
 "redshift:DescribeClusters",
 "redshift:DescribeClusterSecurityGroups",
 "s3:*",
 "sdb:*",
 "sns:*",
 "sqs:*"
 ],
 "Resource": ["*"]
 }]
}`

```

## Creating IAM Roles for AWS Data Pipeline and Editing Role Permissions

Use the following procedures to create roles for AWS Data Pipeline using the IAM console. The process consists of two steps. First, you create a permissions policy to attach to the role. Next, you create the role and attach the policy. After you create a role, you can change the role's permissions by attaching and detaching permissions policies.

###### Note

When you create roles for AWS Data Pipeline using the console as described below, IAM creates and attaches the appropriate trust policies that the role requires.

###### To create a permissions policy to use with a role for AWS Data Pipeline

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, and then choose **Create policy**.
3. Choose the **JSON** tab.
4. If you are creating a pipeline role, copy and paste the contents of the policy example in [Example Pipeline Role Permissions Policy](#dp-role-example-policy "#dp-role-example-policy"), editing it as appropriate for your security requirements. Alternatively, if you are creating a custom EC2 instance role, do the same for the example in [Default Managed Policy for the EC2 Instance Role](#dp-resource-role-example-policy "#dp-resource-role-example-policy").
5. Choose **Review policy**.
6. Enter a name for the policy—for example, `MyDataPipelineRolePolicy`—and an optional **Description**, and then choose **Create policy**.
7. Note the name of the policy. You need it when you create your role.

###### To create an IAM role for AWS Data Pipeline

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, and then choose **Create Role**.
3. Under **Choose a use case**, choose **Data Pipeline**.
4. Under **Select your use case**, do one of the following:
   - Choose `Data Pipeline` to create a pipeline role.
   - Choose `EC2 Role for Data Pipeline` to create a resource role.

5. Choose **Next: Permissions**.
6. If the default policy for AWS Data Pipeline is listed, proceed with the following steps to create the role and then edit it according to the instructions in the next procedure. Otherwise, enter the name of the policy that you created in the procedure above, and then select it from the list.
7. Choose **Next: Tags**, enter any tags to add to the role, and then choose **Next: Review**.
8. Enter a name for the role—for example, `MyDataPipelineRole`—and an optional **Description**, and then choose **Create role**.

###### To attach or detach a permissions policy for an IAM role for AWS Data Pipeline

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**
3. In the search box, begin typing the name of the role you want to edit—for example, **DataPipelineDefaultRole** or **MyDataPipelineRole**—and then choose the **Role name** from the list.
4. On the **Permissions** tab, do the following:
   - To detach a permissions policy, under **Permissions policies**, choose the remove button on the far right of the policy entry. Choose **Detach** when prompted to confirm.
   - To attach a policy that you created earlier, choose **Attach policies**. In the search box, begin typing the name of the policy you want to edit, select it from the list, and then choose **Attach policy**.

## Changing Roles for an Existing Pipelines

If you want to assign a different pipeline role or resource role to a pipeline, you can use the architect editor in the AWS Data Pipeline console.

###### To edit the roles assigned to a pipeline using the console

1. Open the AWS Data Pipeline console at [https://console.aws.amazon.com/datapipeline/](https://console.aws.amazon.com/datapipeline/ "https://console.aws.amazon.com/datapipeline/").
2. Select the pipeline from the list, and then choose **Actions**, **Edit**.
3. In the right pane of the architect editor, choose **Others**.
4. From the **Resource Role** and **Role** lists, choose the roles for AWS Data Pipeline that you want to assign, and then choose **Save**.
