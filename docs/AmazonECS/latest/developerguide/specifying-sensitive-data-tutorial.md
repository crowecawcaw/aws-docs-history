

# Specifying sensitive data using Secrets Manager secrets in Amazon ECS
<a name="specifying-sensitive-data-tutorial"></a>

Amazon ECS allows you to inject sensitive data into your containers by storing your sensitive data in AWS Secrets Manager secrets and then referencing them in your container definition. For more information, see [Pass sensitive data to an Amazon ECS container](specifying-sensitive-data.md).

Learn how to create an Secrets Manager secret, reference the secret in an Amazon ECS task definition, and then verify it worked by querying the environment variable inside a container showing the contents of the secret.

## Prerequisites
<a name="specifying-sensitive-data-tutorial-prereqs"></a>

This tutorial assumes that the following prerequisites have been completed:
+ The steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md) have been completed.
+ Your user has the required IAM permissions to create the Secrets Manager and Amazon ECS resources.

## Step 1: Create an Secrets Manager secret
<a name="specifying-sensitive-data-tutorial-create-secret"></a>

You can use the Secrets Manager console to create a secret for your sensitive data. In this tutorial we will be creating a basic secret for storing a username and password to reference later in a container. For more information, see [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *AWS Secrets Manager User Guide*.

The ** key/value pairs to be stored in this secret** is the environment variable value in your container at the end of the tutorial.

Save the **Secret ARN** to reference in your task execution IAM policy and task definition in later steps.

## Step 2: Add the secrets permissions to the task execution role
<a name="specifying-sensitive-data-tutorial-update-iam"></a>

In order for Amazon ECS to retrieve the sensitive data from your Secrets Manager secret, you must have the secrets permissions for the task execution role. For more information, see [Secrets Manager or Systems Manager permissions](task_execution_IAM_role.md#task-execution-secrets).

## Step 3: Create a task definition
<a name="specifying-sensitive-data-tutorial-create-taskdef"></a>

You can use the Amazon ECS console to create a task definition that references a Secrets Manager secret.

**To create a task definition that specifies a secret**

Use the IAM console to update your task execution role with the required permissions.

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Task definitions**.

1. Choose **Create new task definition**, **Create new task definition with JSON**.

1. In the JSON editor box, enter the following task definition JSON text, ensuring that you specify the full ARN of the Secrets Manager secret you created in step 1 and the task execution role you updated in step 2. Choose **Save**.

1. 

   ```
   {
       "executionRoleArn": "{{arn:aws:iam::{{aws_account_id}}:role/ecsTaskExecutionRole}}",
       "containerDefinitions": [
           {
               "entryPoint": [
                   "sh",
                   "-c"
               ],
               "portMappings": [
                   {
                       "hostPort": 80,
                       "protocol": "tcp",
                       "containerPort": 80
                   }
               ],
               "command": [
                   "/bin/sh -c \"echo '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p> </div></body></html>' >  /usr/local/apache2/htdocs/index.html && httpd-foreground\""
               ],
               "cpu": 10,
               "secrets": [
                   {
                       "valueFrom": "{{arn:aws:secretsmanager:{{region}}:{{aws_account_id}}:secret:username_value}}",
                       "name": "username_value"
                   }
               ],
               "memory": 300,
               "image": "public.ecr.aws/docker/library/httpd:2.4",
               "essential": true,
               "name": "ecs-secrets-container"
           }
       ],
       "family": "ecs-secrets-tutorial"
   }
   ```

1. Choose **Create**.

## Step 4: Create a cluster
<a name="specifying-sensitive-data-tutorial-create-cluster"></a>

You can use the Amazon ECS console to create a cluster containing a container instance to run the task on. If you have an existing cluster with at least one container instance registered to it with the available resources to run one instance of the task definition created for this tutorial you can skip to the next step.

For this tutorial we will be creating a cluster with one `t2.micro` container instance using the Amazon ECS-optimized Amazon Linux 2 AMI.

For information about how to create a cluster for EC2, see [Creating an Amazon ECS cluster for Amazon EC2 workloads](create-ec2-cluster-console-v2.md).

## Step 5: Run a task
<a name="specifying-sensitive-data-tutorial-run-task"></a>

You can use the Amazon ECS console to run a task using the task definition you created. For this tutorial we will be running a task using EC2, using the cluster we created in the previous step. 

For information about how to run a task, see [Running an application as an Amazon ECS task](standalone-task-create.md).

## Step 6: Verify
<a name="specifying-sensitive-data-tutorial-verify"></a>

You can verify all of the steps were completed successfully and the environment variable was created properly in your container using the following steps.

**To verify that the environment variable was created**

1. Find the public IP or DNS address for your container instance.

   1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

   1. In the navigation pane, choose **Clusters**, and then choose the cluster you created.

   1. Choose **Infrastructure**, and then choose the container instance.

   1. Record the **Public IP** or **Public DNS** for your instance.

1. If you are using a macOS or Linux computer, connect to your instance with the following command, substituting the path to your private key and the public address for your instance:

   ```
   $ ssh -i {{/path/to/my-key-pair}}.pem ec2-user@{{ec2-198-51-100-1.compute-1.amazonaws.com}}
   ```

   For more information about using a Windows computer, see [Connect to your Linux instance using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-from-windows.html) in the *Amazon EC2 User Guide*.
**Important**  
For more information about any issues while connecting to your instance, see [Troubleshooting Connecting to Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html) in the *Amazon EC2 User Guide*.

1. List the containers running on the instance. Note the container ID for `ecs-secrets-tutorial` container.

   ```
   docker ps
   ```

1. Connect to the `ecs-secrets-tutorial` container using the container ID from the output of the previous step.

   ```
   docker exec -it {{container_ID}} /bin/bash
   ```

1. Use the `echo` command to print the value of the environment variable.

   ```
   echo $username_value
   ```

   If the tutorial was successful, you should see the following output:

   ```
   password_value
   ```
**Note**  
Alternatively, you can list all environment variables in your container using the `env` (or `printenv`) command.

## Step 7: Clean up
<a name="specifying-sensitive-data-tutorial-cleanup"></a>

When you are finished with this tutorial, you should clean up the associated resources to avoid incurring charges for unused resources.

**To clean up the resources**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, choose the cluster.

1. Choose **Delete Cluster**. 

1. In the confirmation box, enter **delete {{cluster name}}**, and then choose **Delete**.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**. 

1. Search the list of roles for `ecsTaskExecutionRole` and select it.

1. Choose **Permissions**, then choose the **X** next to **ECSSecretsTutorial**. Choose **Remove**.

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Select the **username\_value** secret you created and choose **Actions**, **Delete secret**.