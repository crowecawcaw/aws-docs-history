Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Tutorial: Deploy an application to Amazon ECS

In this tutorial, you learn how to deploy a serverless application into Amazon Elastic Container Service (Amazon ECS) using a
workflow, Amazon ECS, and a few other AWS services. The deployed application is a simple Hello
World website built on an Apache web server Docker image. The tutorial walks you through the
required preparation work such as setting up a cluster, and then describes how to create a
workflow to build and deploy the application.

###### Tip

Instead of working your way through this tutorial, you can use a blueprint that does a
complete Amazon ECS setup for you. You'll need to use either the
**Node.js API with AWS Fargate** or **Java API with AWS Fargate**
blueprint. For more information, see [Creating a project with a
blueprint](projects-create.md#projects-create-console-template "projects-create.md#projects-create-console-template").

###### Topics

- [Prerequisites](#deploy-tut-ecs-prereqs "#deploy-tut-ecs-prereqs")
- [Step 1: Set up an AWS user and
  AWS CloudShell](#deploy-tut-ecs-user-cloudshell "#deploy-tut-ecs-user-cloudshell")
- [Step 2: Deploy a placeholder application into
  Amazon ECS](#deploy-tut-ecs-placeholder "#deploy-tut-ecs-placeholder")
- [Step 3: Create an Amazon ECR image repository](#deploy-tut-ecs-ecr "#deploy-tut-ecs-ecr")
- [Step 4: Create AWS roles](#deploy-tut-ecs-build-deploy-roles "#deploy-tut-ecs-build-deploy-roles")
- [Step 5: Add AWS roles to CodeCatalyst](#deploy-tut-ecs-import-roles "#deploy-tut-ecs-import-roles")
- [Step 6: Create a source repository](#deploy-tut-ecs-source-repo "#deploy-tut-ecs-source-repo")
- [Step 7: Add source files](#deploy-tut-ecs-source-files "#deploy-tut-ecs-source-files")
- [Step 8: Create and run a workflow](#deploy-tut-ecs-workflow "#deploy-tut-ecs-workflow")
- [Step 9: Make a change to your source files](#deploy-tut-ecs-change "#deploy-tut-ecs-change")
- [Clean up](#deploy-tut-ecs-cleanup "#deploy-tut-ecs-cleanup")

## Prerequisites

Before you begin:

- You need a CodeCatalyst **space** with a connected AWS account. For
  more information, see [Creating a space](spaces-create.md "spaces-create.md").
- In your space, you need an empty project called:

```
codecatalyst-ecs-project
```

Use the **Start from scratch** option to create this project.

For more information, see [Creating an empty project in Amazon CodeCatalyst](projects-create.md#projects-create-empty "projects-create.md#projects-create-empty").

- In your project, you need a CodeCatalyst **environment** called:

```
codecatalyst-ecs-environment
```

Configure this environment as follows:

    + Choose any type, such as **Non-production**.
    + Connect your AWS account to it.
    + For the **Default IAM role**, choose any role.
     You'll specify a different role later.

For more information, see [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md").

## Step 1: Set up an AWS user and

AWS CloudShell

The first step in this tutorial is to create a user in AWS IAM Identity Center, and launch an AWS CloudShell
instance as this user. For the duration of this tutorial, CloudShell is your development
computer and is where you configure AWS resources and services. Delete this user after
completing the tutorial.

###### Note

Do not use your root user for this tutorial. You must create a separate user or else you
may experience problems when performing actions in the AWS Command Line Interface (CLI) later on.

For more information about IAM Identity Center users and CloudShell, see the
_AWS IAM Identity Center User Guide_ and _AWS CloudShell User Guide_.

###### To create an IAM Identity Center user

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").

###### Note

Make sure you sign in using the AWS account that is connected to your CodeCatalyst
space. You can verify which account is connected by navigating to your space
and choosing the **AWS accounts** tab. For more information, see [Creating a space](spaces-create.md "spaces-create.md"). 2. In the navigation pane, choose **Users**, and then choose
**Add user**. 3. In **Username**, enter:

```
`CodeCatalystECSUser`
```

4. Under **Password**, choose **Generate a one-time password
   that you can share with this user**.
5. In **Email address** and **Confirm email address**,
   enter an email address that doesn't already exist in IAM Identity Center.
6. In **First name** and **Last name**, enter:

```
`CodeCatalystECSUser`
```

7. In **Display name**, keep the automatically generated name:

```
`CodeCatalystECSUser CodeCatalystECSUser`
```

8. Choose **Next**.
9. On the **Add user to groups** page, choose
   **Next**.
10. On the **Review and add user** page, review the information and
    choose **Add user**.

A **One-time password** dialog box appears. 11. Choose **Copy** and then paste the sign-in information, including the
AWS access portal URL and the one-time password. 12. Choose **Close**.

###### To create a permission set

You'll assign this permission set to `CodeCatalystECSUser` later.

1. In the navigation pane, choose **Permission sets**, and then choose
   **Create permission set**.
2. Choose **Predefined permission set** and then select
   **AdministratorAccess**. This policy provides full permissions to all
   AWS services.
3. Choose **Next**.
4. In **Permission set name**, enter:

```
`CodeCatalystECSPermissionSet`
```

5. Choose **Next**.
6. On the **Review and create** page, review the information and choose
   **Create**.

###### To assign the permission set to CodeCatalystECSUser

1. In the navigation pane, choose **AWS accounts**, and then select
   the check box next to the AWS account that you're currently signed in to.
2. Choose **Assign users or groups**.
3. Choose the **Users** tab.
4. Select the check box next to `CodeCatalystECSUser`.
5. Choose **Next**.
6. Select the check box next to `CodeCatalystECSPermissionSet`.
7. Choose **Next**.
8. Review the information and choose **Submit**.

You have now assigned `CodeCatalystECSUser` and
`CodeCatalystECSPermissionSet` to your AWS account, binding them together.

###### To sign out and sign back in as CodeCatalystECSUser

1. Before you sign out, make sure you have the AWS access portal URL and the username
   and one-time password for `CodeCatalystECSUser`. You should have copied this
   information to a text editor earlier.

###### Note

If you do not have this information, go to the `CodeCatalystECSUser` details
page in IAM Identity Center, choose **Reset password**, **Generate a one-time
password [...]**, and **Reset password** again to display
the information on the screen. 2. Sign out of AWS. 3. Paste the AWS access portal URL into your browser's address bar. 4. Sign in with the username and one-time password for
`CodeCatalystECSUser`. 5. In **New password**, enter a password, and choose **Set new
password**.

An **AWS account** box appears on the screen. 6. Choose **AWS account**, and then choose the name of the AWS account to
which you assigned the `CodeCatalystECSUser` user and permission set. 7. Next to the `CodeCatalystECSPermissionSet`, choose **Management
console**.

The AWS Management Console appears. You are now signed in as `CodeCatalystECSUser` with the
appropriate permissions.

###### To launch an AWS CloudShell instance

1. As `CodeCatalystECSUser`, in the top navigation bar, choose the AWS icon (
   ![AWS icon](images/deploy/aws-logo.png)
   ).

The main page of the AWS Management Console appears. 2. In the top navigation bar, choose the AWS CloudShell icon (
![CloudShell icon](images/deploy/CloudShell.png)
).

CloudShell opens. Wait while the CloudShell environment is created.

###### Note

If you don't see the CloudShell icon, make sure that you're in a [Region supported by CloudShell](../../../cloudshell/latest/userguide/faq-list.md#regions-available "../../../cloudshell/latest/userguide/faq-list.md#regions-available"). This tutorial assumes you are in the
US West (Oregon) Region.

###### To verify that the AWS CLI is installed

1. In the CloudShell terminal, enter:

```
aws --version
```

2. Check that a version appears.

The AWS CLI is already configured for the current user, `CodeCatalystECSUser`, so
there is no need to configure AWS CLI keys and credentials, as is normally the case.

## Step 2: Deploy a placeholder application into

Amazon ECS

In this section, you manually deploy a placeholder application into Amazon ECS. This
placeholder application will be replaced by the Hello World application deployed by your
workflow. The placeholder application is Apache Web Server.

For more information about Amazon ECS, see the _Amazon Elastic Container Service Developer Guide_.

Complete the following series of procedures to deploy the placeholder application.

###### To create the task execution

role

This role grants Amazon ECS and AWS Fargate permission to make API calls on your behalf.

1. Create a trust policy:
   1. In AWS CloudShell, enter the following command:

   ```
   cat > codecatalyst-ecs-trust-policy.json
   ```

   A blinking prompt appears in the CloudShell terminal. 2. Enter the following code at the prompt:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "",
    "Effect": "Allow",
    "Principal": {
    "Service": "ecs-tasks.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
    }
    ]
   }`

   ```

   3. Place your cursor after the last curly bracket (`}`).
   4. Press `Enter` and then `Ctrl+d` to save
      the file and exit cat.

2. Create a task execution role:

```
aws iam create-role \
      --role-name codecatalyst-ecs-task-execution-role \
      --assume-role-policy-document file://codecatalyst-ecs-trust-policy.json
```

3. Attach the AWS managed `AmazonECSTaskExecutionRolePolicy` policy to the
   role:

```
aws iam attach-role-policy \
      --role-name codecatalyst-ecs-task-execution-role \
      --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
```

4. Display the role’s details:

```
aws iam get-role \
      --role-name codecatalyst-ecs-task-execution-role
```

5. Note the role's `"Arn":` value, for example,
   `arn:aws:iam::111122223333:role/codecatalyst-ecs-task-execution-role`. You
   will need this Amazon Resource Name (ARN) later.

###### To create an Amazon ECS cluster

This cluster will contain the Apache placeholder application, and later, the Hello World
application.

1. As `CodeCatalystECSUser`, in AWS CloudShell, create an empty cluster:

```
aws ecs create-cluster --cluster-name codecatalyst-ecs-cluster
```

2. (Optional) Verify that the cluster was created successfully:

```
aws ecs list-clusters
```

The ARN of the `codecatalyst-ecs-cluster` cluster should appear in the
list, indicating a successful creation.

###### To create a task definition file

The task definition file indicates to run the [Apache 2.4 Web server](https://hub.docker.com/_/httpd "https://hub.docker.com/_/httpd") Docker image
(`httpd:2.4`) which is pulled from DockerHub.

1. As `CodeCatalystECSUser`, in AWS CloudShell, create a task definition file:

```
cat > taskdef.json
```

2. Paste the following code at the prompt:

```
{
    "executionRoleArn": "`arn:aws:iam::111122223333:role/codecatalyst-ecs-task-execution-role`",
    "containerDefinitions": [
        {
            "name": "codecatalyst-ecs-container",
            "image": "httpd:2.4",
            "essential": true,
            "portMappings": [
                {
                    "hostPort": 80,
                    "protocol": "tcp",
                    "containerPort": 80
                }
            ]
        }
    ],
    "requiresCompatibilities": [
        "FARGATE"
    ],
    "cpu": "256",
    "family": "codecatalyst-ecs-task-def",
    "memory": "512",
    "networkMode": "awsvpc"
}
```

In the preceding code, replace
`arn:aws:iam::111122223333:role/codecatalyst-ecs-task-execution-role`

with the ARN of the task execution role that you noted in [To create the task execution
role](#deploy-tut-ecs-create-task-execution-role "#deploy-tut-ecs-create-task-execution-role"). 3. Place your cursor after the last curly bracket (`}`). 4. Press `Enter` and then `Ctrl+d` to save the
file and exit cat.

###### To register the task definition file with Amazon ECS

1. As `CodeCatalystECSUser`, in AWS CloudShell, register the task definition:

```
aws ecs register-task-definition \
    --cli-input-json file://taskdef.json
```

2. (Optional) Verify that the task definition was registered:

```
aws ecs list-task-definitions
```

The `codecatalyst-ecs-task-def` task definition should appear in the
list.

###### To create the Amazon ECS service

The Amazon ECS service runs the tasks (and associated Docker containers) of the Apache
placeholder application, and later, the Hello World application.

1.  As `CodeCatalystECSUser`, switch to the Amazon Elastic Container Service console if you haven't done so
    already.
2.  Choose the cluster you created earlier,
    `codecatalyst-ecs-cluster`.
3.  In the **Services** tab, choose **Create**.
4.  In the **Create** page, do the following:
    1. Keep all default settings except for those listed next.
    2. For **Launch type**, choose **FARGATE**.
    3. Under **Task definition**, in the **Family**
       drop-down list, choose:

    `codecatalyst-ecs-task-def` 4. For **Service name**, enter:

    ```
    `codecatalyst-ecs-service`
    ```

    5. For **Desired tasks**, enter:

    ```
    `3`
    ```

    In this tutorial, each task launches a single Docker container. 6. Expand the **Networking** section. 7. For **VPC**, choose any VPC. 8. For **Subnets**, choose any subnet.

    ###### Note

    Only specify one subnet. That's all that is needed for this tutorial.

    ###### Note

    If you don’t have a VPC and subnet, create them. See [Create a VPC](../../../vpc/latest/userguide/working-with-vpcs.md#Create-VPC "../../../vpc/latest/userguide/working-with-vpcs.md#Create-VPC"),
    and [Create a subnet in
    your VPC](../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet "../../../vpc/latest/userguide/working-with-vpcs.md#AddaSubnet") in the _Amazon VPC User Guide_. 9. For **Security group**, choose **Create a new security
    group**, and then do the following:

        1. For **Security group name**, enter:



        ```
        `codecatalyst-ecs-security-group`
        ```
        2. For **Security group description**, enter:



        ```
        `CodeCatalyst ECS security group`
        ```
        3. Choose **Add rule**. For **Type**,
         choose **HTTP**, and for **Source**, choose
         **Anywhere**.

    10. At the bottom, choose **Create**.
    11. Wait while the service is created. This may take a few minutes.

5.  Choose the **Tasks** tab, and then choose the refresh button. Verify
    that all three tasks have their **Last Status** column set to
    **Running**.

###### (Optional) To verify that your Apache placeholder application is running

1. In the **Tasks** tab, choose any one of the three tasks.
2. In the **Public IP** field, choose **open
   address**.

An `It Works!` page appears. This indicates that the Amazon ECS service
successfully started a task that launched a Docker container with the Apache image.

At this point in the tutorial, you have manually deployed an Amazon ECS cluster, service,
and task definition, as well as an Apache placeholder application. With all these items in
place, you are now ready to create a workflow that will replace the Apache placeholder
application with the tutorial’s Hello World application.

## Step 3: Create an Amazon ECR image repository

In this section, you create a private image repository in Amazon Elastic Container Registry (Amazon ECR). This
repository stores the tutorial’s Docker image that will replace the Apache placeholder image
you deployed previously.

For more information about Amazon ECR, see the _Amazon Elastic Container Registry User Guide_.

###### To create an image repository in Amazon ECR

1. As `CodeCatalystECSUser`, in AWS CloudShell, create an empty repository in
   Amazon ECR:

```
aws ecr create-repository --repository-name codecatalyst-ecs-image-repo
```

2. Display the Amazon ECR repository’s details:

```
aws ecr describe-repositories \
      --repository-names codecatalyst-ecs-image-repo

```

3. Note the `“repositoryUri”:` value, for example,
   `111122223333.dkr.ecr.us-west-2.amazonaws.com/codecatalyst-ecs-image-repo`.

You need it later when adding the repository to your workflow.

## Step 4: Create AWS roles

In this section, you create AWS IAM roles that your CodeCatalyst workflow will need in order
to function. These roles are:

- **Build role** – Grants the CodeCatalyst build action
  (in the workflow) permission to access your AWS account and write to Amazon ECR and
  Amazon EC2.
- **Deploy role** – Grants the CodeCatalyst **Deploy to ECS** action (in the workflow) permission to access your
  AWS account, Amazon ECS, and a few other AWS services.

For more information about IAM roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _AWS Identity and Access Management User
Guide_.

###### Note

To save time, you can create a single role, called the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role, instead of
 the two roles listed previously. For more information, see [Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
 and space](ipa-iam-roles.md#ipa-iam-roles-service-create "ipa-iam-roles.md#ipa-iam-roles-service-create").
 Understand that the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role has very broad permissions which may pose a security
risk. We recommend that you only use this role in tutorials and scenarios where security is
less of a concern. This tutorial assumes you are creating the two roles listed
previously.

To create the build and deploy roles, you can use either the AWS Management Console or the
AWS CLI.

AWS Management Console
To create the build and deploy roles, complete the following series of
procedures.

###### To create a build role

1. Create a policy for the role, as follows:
   1. Sign in to AWS.
   2. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   3. In the navigation pane, choose **Policies**.
   4. Choose **Create policy**.
   5. Choose the **JSON** tab.
   6. Delete the existing code.
   7. Paste the following code:

   JSONJSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "ecr:*",
    "ec2:*"
    ],
    "Resource": "*"
    }
    ]
   }`

   ```

   ###### Note

   The first time the role is used to run workflow actions, use the wildcard
   in the resource policy statement and then scope down the policy with the
   resource name after it is available.

   ```
   "Resource": "*"
   ```

   8. Choose **Next: Tags**.
   9. Choose **Next: Review**.
   10. In **Name**, enter:

   ```
   `codecatalyst-ecs-build-policy`
   ```

   11. Choose **Create policy**.

   You have now created a permissions policy.

2. Create the build role, as follows:
   1. In the navigation pane, choose **Roles**, and then choose
      **Create role**.
   2. Choose **Custom trust policy**.
   3. Delete the existing custom trust policy.
   4. Add the following custom trust policy:
   5. Choose **Next**.
   6. In **Permissions policies**, search for
      `codecatalyst-ecs-build-policy`, select its check box.
   7. Choose **Next**.
   8. For **Role name**, enter:

   ```
   `codecatalyst-ecs-build-role`
   ```

   9. For **Role description**, enter:

   ```
   `CodeCatalyst ECS build role`
   ```

   10. Choose **Create role**.You have now created a build role with a permissions policy and a trust
       policy.

3. Obtain the build role ARN, as follows:
   1. In the navigation pane, choose **Roles**.
   2. In the search box, enter the name of the role you just created
      (`codecatalyst-ecs-build-role`).
   3. Choose the role from the list.

   The role's **Summary** page appears. 4. At the top, copy the **ARN** value. You need it
   later.

###### To create a deploy role

1. Create a policy for the role, as follows:
   1. Sign in to AWS.
   2. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   3. In the navigation pane, choose **Policies**.
   4. Choose **Create Policy**.
   5. Choose the **JSON** tab.
   6. Delete the existing code.
   7. Paste the following code:

   JSONJSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [{
    "Action":[
    "ecs:DescribeServices",
    "ecs:CreateTaskSet",
    "ecs:DeleteTaskSet",
    "ecs:ListClusters",
    "ecs:RegisterTaskDefinition",
    "ecs:UpdateServicePrimaryTaskSet",
    "ecs:UpdateService",
    "elasticloadbalancing:DescribeTargetGroups",
    "elasticloadbalancing:DescribeListeners",
    "elasticloadbalancing:ModifyListener",
    "elasticloadbalancing:DescribeRules",
    "elasticloadbalancing:ModifyRule",
    "lambda:InvokeFunction",
    "lambda:ListFunctions",
    "cloudwatch:DescribeAlarms",
    "sns:Publish",
    "sns:ListTopics",
    "s3:GetObject",
    "s3:GetObjectVersion",
    "codedeploy:CreateApplication",
    "codedeploy:CreateDeployment",
    "codedeploy:CreateDeploymentGroup",
    "codedeploy:GetApplication",
    "codedeploy:GetDeployment",
    "codedeploy:GetDeploymentGroup",
    "codedeploy:ListApplications",
    "codedeploy:ListDeploymentGroups",
    "codedeploy:ListDeployments",
    "codedeploy:StopDeployment",
    "codedeploy:GetDeploymentTarget",
    "codedeploy:ListDeploymentTargets",
    "codedeploy:GetDeploymentConfig",
    "codedeploy:GetApplicationRevision",
    "codedeploy:RegisterApplicationRevision",
    "codedeploy:BatchGetApplicationRevisions",
    "codedeploy:BatchGetDeploymentGroups",
    "codedeploy:BatchGetDeployments",
    "codedeploy:BatchGetApplications",
    "codedeploy:ListApplicationRevisions",
    "codedeploy:ListDeploymentConfigs",
    "codedeploy:ContinueDeployment"
    ],
    "Resource":"*",
    "Effect":"Allow"
   },{"Action":[
    "iam:PassRole"
    ],
    "Effect":"Allow",
    "Resource":"*",
    "Condition":{"StringLike":{"iam:PassedToService":[
    "ecs-tasks.amazonaws.com",
    "codedeploy.amazonaws.com"
    ]
    }
    }
   }]
   }`

   ```

   ###### Note

   The first time the role is used to run workflow actions, use the wildcard
   in the resource policy statement. You can then scope down the policy with the
   resource name after it is available.

   ```
   "Resource": "*"
   ```

   8. Choose **Next: Tags**.
   9. Choose **Next: Review**.
   10. In **Name**, enter:

   ```
   `codecatalyst-ecs-deploy-policy`
   ```

   11. Choose **Create policy**.

   You have now created a permissions policy.

2. Create the deploy role, as follows:
   1. In the navigation pane, choose **Roles**, and then choose
      **Create role**.
   2. Choose **Custom trust policy**.
   3. Delete the existing custom trust policy.
   4. Add the following custom trust policy:
   5. Choose **Next**.
   6. In **Permissions policies**, search for
      `codecatalyst-ecs-deploy-policy`, select its check box.
   7. Choose **Next**.
   8. For **Role name**, enter:

   ```
   `codecatalyst-ecs-deploy-role`
   ```

   9. For **Role description**, enter:

   ```
   `CodeCatalyst ECS deploy role`
   ```

   10. Choose **Create role**.You have now created a deploy role with a trust policy.

3. Obtain the deploy role ARN, as follows:
   1. In the navigation pane, choose **Roles**.
   2. In the search box, enter the name of the role you just created
      (`codecatalyst-ecs-deploy-role`).
   3. Choose the role from the list.

   The role's **Summary** page appears. 4. At the top, copy the **ARN** value. You need it
   later.

AWS CLI
To create the build and deploy roles, complete the following series of
procedures.

###### To create a trust policy for both roles

As `CodeCatalystECSUser`, in AWS CloudShell, create a trust policy file:

1. Create the file:

```
cat > codecatalyst-ecs-trust-policy.json
```

2. At the terminal prompt, paste the following code:
3. Place your cursor after the last curly bracket (`}`).
4. Press `Enter` and then `Ctrl+d` to
   save the file and exit cat.

###### To create the build policy and build role

1. Create the build policy:
   1. As `CodeCatalystECSUser`, in AWS CloudShell, create a build policy
      file:

   ```
   cat > codecatalyst-ecs-build-policy.json
   ```

   2. At the prompt, enter the following code:

   JSONJSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "ecr:*",
    "ec2:*"
    ],
    "Resource": "*"
    }
    ]
   }`

   ```

   3. Place your cursor after the last curly bracket (`}`).
   4. Press `Enter` and then `Ctrl+d` to
      save the file and exit cat.

2. Add the build policy to AWS:

```
aws iam create-policy \
    --policy-name codecatalyst-ecs-build-policy \
    --policy-document file://codecatalyst-ecs-build-policy.json
```

3. In the command output, note the `"arn":` value, for example,
   `arn:aws:iam::111122223333:policy/codecatalyst-ecs-build-policy`.
   You need this ARN later.
4. Create the build role and attach the trust policy to it:

```
aws iam create-role \
      --role-name codecatalyst-ecs-build-role \
      --assume-role-policy-document file://codecatalyst-ecs-trust-policy.json
```

5. Attach the build policy to the build role:

```
aws iam attach-role-policy \
      --role-name codecatalyst-ecs-build-role \
      --policy-arn `arn:aws:iam::111122223333:policy/codecatalyst-ecs-build-policy`
```

Where
`arn:aws:iam::111122223333:policy/codecatalyst-ecs-build-policy`
is replaced with the ARN of the build policy you noted earlier. 6. Display the build role’s details:

```
aws iam get-role \
      --role-name codecatalyst-ecs-build-role
```

7. Note the role's `"Arn":` value, for example,
   `arn:aws:iam::111122223333:role/codecatalyst-ecs-build-role`. You
   need this ARN later.

###### To create the deploy policy and deploy role

1. Create a deploy policy:
   1. In AWS CloudShell, create a deploy policy file:

   ```
   cat > codecatalyst-ecs-deploy-policy.json
   ```

   2. At the prompt, enter the following code:

   JSONJSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [{
    "Action":[
    "ecs:DescribeServices",
    "ecs:CreateTaskSet",
    "ecs:DeleteTaskSet",
    "ecs:ListClusters",
    "ecs:RegisterTaskDefinition",
    "ecs:UpdateServicePrimaryTaskSet",
    "ecs:UpdateService",
    "elasticloadbalancing:DescribeTargetGroups",
    "elasticloadbalancing:DescribeListeners",
    "elasticloadbalancing:ModifyListener",
    "elasticloadbalancing:DescribeRules",
    "elasticloadbalancing:ModifyRule",
    "lambda:InvokeFunction",
    "lambda:ListFunctions",
    "cloudwatch:DescribeAlarms",
    "sns:Publish",
    "sns:ListTopics",
    "s3:GetObject",
    "s3:GetObjectVersion",
    "codedeploy:CreateApplication",
    "codedeploy:CreateDeployment",
    "codedeploy:CreateDeploymentGroup",
    "codedeploy:GetApplication",
    "codedeploy:GetDeployment",
    "codedeploy:GetDeploymentGroup",
    "codedeploy:ListApplications",
    "codedeploy:ListDeploymentGroups",
    "codedeploy:ListDeployments",
    "codedeploy:StopDeployment",
    "codedeploy:GetDeploymentTarget",
    "codedeploy:ListDeploymentTargets",
    "codedeploy:GetDeploymentConfig",
    "codedeploy:GetApplicationRevision",
    "codedeploy:RegisterApplicationRevision",
    "codedeploy:BatchGetApplicationRevisions",
    "codedeploy:BatchGetDeploymentGroups",
    "codedeploy:BatchGetDeployments",
    "codedeploy:BatchGetApplications",
    "codedeploy:ListApplicationRevisions",
    "codedeploy:ListDeploymentConfigs",
    "codedeploy:ContinueDeployment"
    ],
    "Resource":"*",
    "Effect":"Allow"
   },{"Action":[
    "iam:PassRole"
    ],
    "Effect":"Allow",
    "Resource":"*",
    "Condition":{"StringLike":{"iam:PassedToService":[
    "ecs-tasks.amazonaws.com",
    "codedeploy.amazonaws.com"
    ]
    }
    }
   }]
   }`

   ```

   ###### Note

   The first time the role is used to run workflow actions, use the wildcard
   in the resource policy statement and then scope down the policy with the
   resource name after it is available.

   ```
   "Resource": "*"
   ```

   3. Place your cursor after the last curly bracket (`}`).
   4. Press `Enter` and then `Ctrl+d` to
      save the file and exit cat.

2. Add the deploy policy to AWS:

```
aws iam create-policy \
    --policy-name codecatalyst-ecs-deploy-policy \
    --policy-document file://codecatalyst-ecs-deploy-policy.json
```

3. In the command output, note the deploy policy's `"arn":` value, for
   example,
   `arn:aws:iam::111122223333:policy/codecatalyst-ecs-deploy-policy`.
   You need this ARN later.
4. Create the deploy role and attach the trust policy to it:

```
aws iam create-role \
      --role-name codecatalyst-ecs-deploy-role \
      --assume-role-policy-document file://codecatalyst-ecs-trust-policy.json
```

5. Attach the deploy policy to the deploy role, where
   `arn:aws:iam::111122223333:policy/codecatalyst-ecs-deploy-policy`
   is replaced with the ARN of the deploy policy you noted earlier.

```
aws iam attach-role-policy \
      --role-name codecatalyst-ecs-deploy-role \
      --policy-arn `arn:aws:iam::111122223333:policy/codecatalyst-ecs-deploy-policy`
```

6. Display the deploy role’s details:

```
aws iam get-role \
      --role-name codecatalyst-ecs-deploy-role
```

7. Note the role's `"Arn":` value, for example,
   `arn:aws:iam::111122223333:role/codecatalyst-ecs-deploy-role`. You
   need this ARN later.

## Step 5: Add AWS roles to CodeCatalyst

In this step, you add the build role (`codecatalyst-ecs-build-role`) and
deploy role (`codecatalyst-ecs-deploy-role`) to the CodeCatalyst account connection in
your space.

###### To add build and deploy roles to your account connection

1. In CodeCatalyst, navigate to your space.
2. Choose **AWS accounts**. A list of account connections
   appears.
3. Choose the account connection that represents the AWS account where you created your
   build and deploy roles.
4. Choose **Manage roles from AWS management console**.

The **Add IAM role to Amazon CodeCatalyst space** page appears. You
might need to sign in to access the page. 5. Select **Add an existing role you have created in IAM**.

A drop-down list appears. The list displays all IAM roles with a trust policy that
includes the `codecatalyst-runner.amazonaws.com` and
`codecatalyst.amazonaws.com` service principals. 6. In the drop-down list, choose `codecatalyst-ecs-build-role`, and choose
**Add role**.

###### Note

If you see `The security token included in the request is invalid`, it
might be because you do not have the right permissions. To fix this issue, sign out of
AWS as sign back in with the AWS account that you used when you created your CodeCatalyst
space. 7. Choose **Add IAM role**, choose **Add an existing role you
have created in IAM**, and in the drop-down list, choose
`codecatalyst-ecs-deploy-role`. Choose **Add
role**.

You have now added the build and deploy roles to your space. 8. Copy the value of the **Amazon CodeCatalyst display name**. You'll need this
value later, when creating your workflow.

## Step 6: Create a source repository

In this step, you create a source repository in CodeCatalyst. This repository stores the
tutorial's source files, such as the task definition file.

For more information about source repositories, see [Creating a source repository](source-repositories-create.md "source-repositories-create.md").

###### To create a source repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your project, `codecatalyst-ecs-project`.
3. In the navigation pane, choose **Code**, and then choose
   **Source repositories**.
4. Choose **Add repository**, and then choose **Create
   repository**.
5. In **Repository name**, enter:

```
`codecatalyst-ecs-source-repository`
```

6. Choose **Create**.

## Step 7: Add source files

In this section, you add the Hello World source files to your CodeCatalyst repository,
`codecatalyst-ecs-source-repository`. They consist of:

- An `index.html` file – Displays a Hello World message in the
  browser.
- A Dockerfile – Describes the base image to use for your Docker image and the
  Docker commands to apply to it.
- A `taskdef.json` file – Defines the Docker image to use when
  launching tasks into your cluster.

The folder structure is as follows:

```
.
|— public-html
|  |— index.html
|— Dockerfile
|— taskdef.json
```

###### Note

The following instructions show you how to add the files using the CodeCatalyst console but
you can use Git if you prefer. For details, see [Cloning a source repository](source-repositories-clone.md "source-repositories-clone.md").

###### Topics

- [index.html](#deploy-tut-ecs-source-files-index "#deploy-tut-ecs-source-files-index")
- [Dockerfile](#deploy-tut-ecs-source-files-dockerfile "#deploy-tut-ecs-source-files-dockerfile")
- [taskdef.json](#deploy-tut-ecs-source-files-taskdef "#deploy-tut-ecs-source-files-taskdef")

### index.html

The `index.html` file displays a Hello World message in the browser.

###### To add the index.html file

1. In the CodeCatalyst console, go to your source repository,
   `codecatalyst-ecs-source-repository`.
2. In **Files**, choose **Create file**.
3. For **File name**, enter:

```
`public-html/index.html`
```

###### Important

Make sure to include the `public-html/` prefix to create a
folder of the same name. The `index.html` is expected to be in this
folder. 4. In the text box, enter the following code:

```
<html>
  <head>
    <title>Hello World</title>
    <style>
      body {
      background-color: black;
      text-align: center;
      color: white;
      font-family: Arial, Helvetica, sans-serif;
      }
    </style>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

5. Choose **Commit**, and then choose **Commit**
   again.

The `index.html` is added to your repository in a
`public-html` folder.

### Dockerfile

The Dockerfile describes the base Docker image to use and the Docker commands to apply
to it. For more information about the Dockerfile, see the [Dockerfile
Reference](https://docs.docker.com/engine/reference/builder/ "https://docs.docker.com/engine/reference/builder/").

The Dockerfile specified here indicates to use the Apache 2.4 base image
(`httpd`). It also includes instructions for copying a source file called
`index.html` to a folder on the Apache server that serves webpages. The
`EXPOSE` instruction in the Dockerfile tells Docker that the container is
listening on port 80.

###### To add the Dockerfile

1. In your source repository, choose **Create file**.
2. For **File name**, enter:

```
`Dockerfile`
```

Do not include a file extension.

###### Important

The Dockerfile must reside in your repository’s root folder. The workflow’s
`Docker build` command expects it to be there. 3. In the text box, enter the following code:

```
FROM httpd:2.4
COPY ./public-html/index.html /usr/local/apache2/htdocs/index.html
EXPOSE 80
```

4. Choose **Commit**, and then choose **Commit**
   again.

The Dockerfile is added to your repository.

### taskdef.json

The `taskdef.json` file that you add in this step is the same as the
one you already specified in [Step 2: Deploy a placeholder application into
Amazon ECS](#deploy-tut-ecs-placeholder "#deploy-tut-ecs-placeholder") with the following difference:

Instead of specifying a hardcoded Docker image name in the `image:` field
(`httpd:2.4`), the task definition here uses a couple of variables to denote
the image: `$REPOSITORY_URI` and `$IMAGE_TAG`. These variables will be
replaced with real values generated by the workflow’s build action when you run the workflow
in a later step.

For details on the task definition parameters, see [Task definition
parameters](../../../AmazonECS/latest/developerguide/task_definition_parameters.md "../../../AmazonECS/latest/developerguide/task_definition_parameters.md") in the _Amazon Elastic Container Service Developer Guide_.

###### To add the taskdef.json file

1. In your source repository, choose **Create file**.
2. For **File name**, enter:

```
`taskdef.json`
```

3. In the text box, enter the following code:

```
{
    "executionRoleArn": "`arn:aws:iam::account_ID:role/codecatalyst-ecs-task-execution-role`",
    "containerDefinitions": [
        {
            "name": "codecatalyst-ecs-container",
            # The $REPOSITORY_URI and $IMAGE_TAG variables will be replaced
            # by the workflow at build time (see the build action in the
            # workflow)
            "image": $REPOSITORY_URI:$IMAGE_TAG,
            "essential": true,
            "portMappings": [
                {
                    "hostPort": 80,
                    "protocol": "tcp",
                    "containerPort": 80
                }
            ]
        }
    ],
    "requiresCompatibilities": [
        "FARGATE"
    ],
    "networkMode": "awsvpc",
    "cpu": "256",
    "memory": "512",
    "family": "codecatalyst-ecs-task-def"
}
```

In the preceding code, replace

`arn:aws:iam::account_ID:role/codecatalyst-ecs-task-execution-role`

with the ARN of the task execution role that you noted in [To create the task execution
role](#deploy-tut-ecs-create-task-execution-role "#deploy-tut-ecs-create-task-execution-role"). 4. Choose **Commit**, and then choose **Commit**
again.

The `taskdef.json` file is added to your repository.

## Step 8: Create and run a workflow

In this step, you create a workflow that takes your source files, builds them into a
Docker image, and then deploys the image to your Amazon ECS cluster. This deployment replaces the
existing Apache placeholder application.

The workflow consists of the following building blocks that run sequentially:

- A trigger – This trigger starts the workflow run automatically when you push a
  change to your source repository. For more information about triggers, see [Starting a workflow run automatically using
  triggers](workflows-add-trigger.md "workflows-add-trigger.md").
- A build action (`BuildBackend`) – On trigger, the action builds the
  Docker image using the Dockerfile and pushes the image to Amazon ECR. The build action also
  updates the `taskdef.json` with the correct `image` field value, and
  then creates an output artifact of this file. This artifact is used as the input for the
  deploy action, which is next.

For more information about the build action, see [Building with workflows](build-workflow-actions.md "build-workflow-actions.md").

- A deploy action (`DeployToECS`) – On completion of the build action,
  the deploy action looks for the output artifact generated by the build action
  (`TaskDefArtifact`), finds the `taskdef.json` inside of
  it, and registers it with your Amazon ECS service. The service then follows the instructions in
  the `taskdef.json` file to run three Amazon ECS tasks—and associated Hello
  World Docker containers—inside your Amazon ECS cluster.

###### To create a workflow

1. In the CodeCatalyst console, in the navigation pane, choose **CI/CD**, and
   then choose **Workflows**.
2. Choose **Create workflow**.
3. For **Source repository**, choose
   `codecatalyst-ecs-source-repository`.
4. For **Branch**, choose `main`.
5. Choose **Create**.
6. Delete the YAML sample code.
7. Add the following YAML code:

###### Note

In the YAML code that follows, you can omit the `Connections:` sections
if you want. If you omit these sections, you must ensure that the role specified in the
**Default IAM role** field in your environment includes the
permissions and trust policies of both roles described in [Step 5: Add AWS roles to CodeCatalyst](#deploy-tut-ecs-import-roles "#deploy-tut-ecs-import-roles").
For more information about setting up an environment with a default IAM role, see
[Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").

```
Name: codecatalyst-ecs-workflow
SchemaVersion: 1.0

Triggers:
  - Type: PUSH
    Branches:
      - main
Actions:
  BuildBackend:
    Identifier: aws/build@v1
    Environment:
      Name: `codecatalyst-ecs-environment`
      Connections:
        - Name: `codecatalyst-account-connection`
          Role: `codecatalyst-ecs-build-role`
    Inputs:
      Sources:
        - WorkflowSource
      Variables:
        - Name: REPOSITORY_URI
          Value: `111122223333.dkr.ecr.us-west-2.amazonaws.com/codecatalyst-ecs-image-repo`
        - Name: IMAGE_TAG
          Value: ${WorkflowSource.CommitId}
    Configuration:
      Steps:
        #pre_build:
        - Run: echo Logging in to Amazon ECR...
        - Run: aws --version
        - Run: aws ecr get-login-password --region `us-west-2` | docker login --username AWS --password-stdin `111122223333.dkr.ecr.us-west-2.amazonaws.com`
        #build:
        - Run: echo Build started on `date`
        - Run: echo Building the Docker image...
        - Run: docker build -t $REPOSITORY_URI:latest .
        - Run: docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
        #post_build:
        - Run: echo Build completed on `date`
        - Run: echo Pushing the Docker images...
        - Run: docker push $REPOSITORY_URI:latest
        - Run: docker push $REPOSITORY_URI:$IMAGE_TAG
        # Replace the variables in taskdef.json
        - Run: find taskdef.json -type f | xargs sed -i "s|\$REPOSITORY_URI|$REPOSITORY_URI|g"
        - Run: find taskdef.json -type f | xargs sed -i "s|\$IMAGE_TAG|$IMAGE_TAG|g"
        - Run: cat taskdef.json
        # The output artifact will be a zip file that contains a task definition file.
    Outputs:
      Artifacts:
        - Name: TaskDefArtifact
          Files:
            - taskdef.json
  DeployToECS:
    DependsOn:
      - BuildBackend
    Identifier: aws/ecs-deploy@v1
    Environment:
      Name: `codecatalyst-ecs-environment`
      Connections:
        - Name: `codecatalyst-account-connection`
          Role: `codecatalyst-ecs-deploy-role`
    Inputs:
      Sources: []
      Artifacts:
        - TaskDefArtifact
    Configuration:
      region: `us-west-2`
      cluster: codecatalyst-ecs-cluster
      service: codecatalyst-ecs-service
      task-definition: taskdef.json
```

In the preceding code, replace:

    * Both instances of `codecatalyst-ecs-environment` with
     the name of the environment you created in [Prerequisites](#deploy-tut-ecs-prereqs "#deploy-tut-ecs-prereqs").
    * Both instances of `codecatalyst-account-connection`
     with the display name of your account connection. The display name might be a number.
     For more information, see [Step 5: Add AWS roles to CodeCatalyst](#deploy-tut-ecs-import-roles "#deploy-tut-ecs-import-roles").
    * `codecatalyst-ecs-build-role` with the name of the
     build role you created in [Step 4: Create AWS roles](#deploy-tut-ecs-build-deploy-roles "#deploy-tut-ecs-build-deploy-roles").
    * `111122223333.dkr.ecr.us-west-2.amazonaws.com/codecatalyst-ecs-image-repo`
     (in the `Value:` property) with the URI of the Amazon ECR repository you created
     in [Step 3: Create an Amazon ECR image repository](#deploy-tut-ecs-ecr "#deploy-tut-ecs-ecr").
    * `111122223333.dkr.ecr.us-west-2.amazonaws.com` (in the
     `Run: aws ecr` command) with the URI of the Amazon ECR repository without the
     image suffix (`/codecatalyst-ecs-image-repo`).
    * `codecatalyst-ecs-deploy-role` with the name of the
     deploy role you created in [Step 4: Create AWS roles](#deploy-tut-ecs-build-deploy-roles "#deploy-tut-ecs-build-deploy-roles").
    * Both instances of `us-west-2` with your AWS Region
     code. For a list of Region codes, see [Regional endpoints](../../../general/latest/gr/rande.md#regional-endpoints "../../../general/latest/gr/rande.md#regional-endpoints") in
     the *AWS General Reference*.

###### Note

If you decided not to create build and deploy roles, replace
`codecatalyst-ecs-build-role` and
`codecatalyst-ecs-deploy-role` with the name of the
`CodeCatalystWorkflowDevelopmentRole-`spaceName`` role. For more information about this role, see [Step 4: Create AWS roles](#deploy-tut-ecs-build-deploy-roles "#deploy-tut-ecs-build-deploy-roles").

###### Tip

Instead of using the `find` and `sed` commands shown in the
previous workflow code to update the repository and image name, you can use the
**Render Amazon ECS task definition** action for this purpose. For more
information, see [Modifying an Amazon ECS task definition](render-ecs-action.md "render-ecs-action.md"). 8. (Optional) Choose **Validate** to make sure that the YAML code is
valid before committing. 9. Choose **Commit**. 10. In the **Commit workflow** dialog box, enter the following:

    1. For **Commit message**, remove the text and enter:



    ```
    `Add first workflow`
    ```
    2. For **Repository**, choose
     `codecatalyst-ecs-source-repository`.
    3. For **Branch name**, choose main.
    4. Choose **Commit**.You have now created a workflow. A workflow run starts automatically because of the

trigger defined at the top of the workflow. Specifically, when you committed (and pushed)
the `workflow.yaml` file to your source repository, the trigger started
the workflow run.

###### To view the workflow run progress

1. In the navigation pane of the CodeCatalyst console, choose **CI/CD**, and
   then choose **Workflows**.
2. Choose the workflow you just created,
   `codecatalyst-ecs-workflow`.
3. Choose **BuildBackend** to see the build progress.
4. Choose **DeployToECS** to see the deployment progress.

For more information about viewing run details, see [Viewing workflow run status and details](workflows-view-run.md "workflows-view-run.md").

###### To verify the deployment

1. Open the Amazon ECS classic console at
   [https://console.aws.amazon.com/ecs/](https://console.aws.amazon.com/ecs/ "https://console.aws.amazon.com/ecs/").
2. Choose your cluster, `codecatalyst-ecs-cluster`.
3. Choose the **Tasks** tab.
4. Choose any one of the three tasks.
5. In the **Public IP** field, choose **open
   address**.

A "Hello World" page appears in the browser, indicating that the Amazon ECS service
successfully deployed your application.

## Step 9: Make a change to your source files

In this section, you make a change to the `index.html` file in your
source repository. This change causes the workflow to build a new Docker image, tag it with a
commit ID, push it to Amazon ECR, and deploy it to Amazon ECS.

###### To change the index.html

1. In the CodeCatalyst console, in the navigation pane, choose **Code**, then
   choose **Source repositories**, and then choose your repository,
   `codecatalyst-ecs-source-repository`.
2. Choose `public-html`, and then choose
   `index.html`.

The contents of `index.html` appear. 3. Choose **Edit**. 4. On line 14, change the `Hello World` text to `Tutorial
 complete!`. 5. Choose **Commit**, and then choose **Commit**
again.

The commit causes a new workflow run to start. 6. (Optional) Go to your source repository's main page, choose **View
commits**, and then note the commit ID for the `index.html`
change. 7. Watch the deployment progress:

    1. In the navigation pane, choose **CI/CD**, and then choose
     **Workflows**.
    2. Choose `codecatalyst-ecs-workflow` to view the latest run.
    3. Choose **BuildBackend**, and **DeployToECS** to
     see the workflow run progress.

8. Verify that your application was updated, as follows:
   1. Open the Amazon ECS classic console at
      [https://console.aws.amazon.com/ecs/](https://console.aws.amazon.com/ecs/ "https://console.aws.amazon.com/ecs/").
   2. Choose your cluster, `codecatalyst-ecs-cluster`.
   3. Choose the **Tasks** tab.
   4. Choose any one of the three tasks.
   5. In the **Public IP** field, choose **open
      address**.

   A `Tutorial complete!` page appears.

9. (Optional) In AWS, switch to the Amazon ECR console and verify that the new Docker image
   was tagged with the commit ID from step 6.

## Clean up

Clean up the files and services used in this tutorial to avoid being charged for
them.

In the AWS Management Console, clean up in this order:

1. In Amazon ECS, do the following:
   1. Delete `codecatalyst-ecs-service`.
   2. Delete `codecatalyst-ecs-cluster`.
   3. Deregister `codecatalyst-ecs-task-definition`.

2. In Amazon ECR, delete `codecatalyst-ecs-image-repo`.
3. In Amazon EC2, delete `codecatalyst-ecs-security-group`.
4. In IAM Identity Center, delete:
   1. `CodeCatalystECSUser`
   2. `CodeCatalystECSPermissionSet`

In the CodeCatalyst console, clean up as follows:

1. Delete `codecatalyst-ecs-workflow`.
2. Delete `codecatalyst-ecs-environment`.
3. Delete `codecatalyst-ecs-source-repository`.
4. Delete `codecatalyst-ecs-project`.

In this tutorial, you learned how to deploy an application to an Amazon ECS service using a
CodeCatalyst workflow and a **Deploy to Amazon ECS** action.
