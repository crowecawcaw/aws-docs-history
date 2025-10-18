AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Amazon ECS Exec in AWS Toolkit for AWS Cloud9

You can issue single commands in an Amazon Elastic Container Service (Amazon ECS) container with the AWS Toolkit for AWS Cloud9.
 You can do this using the Amazon ECS Exec feature. 

###### Important

Enabling and Disabling Amazon ECS Exec changes the state of your ECS resources in your
 AWS account. Changes include stopping and restarting the service. Moreover, altering
 the state of resources while the Amazon ECS Exec is enabled can lead to unpredictable
 results. For more information about Amazon ECS, see [Using
 Amazon ECS Exec for Debugging](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html#ecs-exec-considerations "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html#ecs-exec-considerations") in the *Amazon ECS Developer
 Guide*.


## Amazon ECS Exec prerequisites


Before you can use the Amazon ECS Exec feature, there are certain prerequisite conditions
 that you must meet.


### Amazon ECS requirements


Depending on whether your tasks are hosted on Amazon EC2 or AWS Fargate, and Amazon ECS
 Exec has different version requirements.



* If you use Amazon EC2, you must use an Amazon ECS optimized AMI that was released after January 20,
 2021, with an agent version 1.50.2 or later. For more information, see
 [Amazon ECS
 optimized AMIs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html") in the *Amazon ECS Developer
 Guide*.
* If you use AWS Fargate, you must use platform version 1.4.0 or later. For more information,
 see [AWS Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html") in the *Amazon ECS Developer Guide*.

### AWS account configuration and IAM permissions


To use the Amazon ECS Exec feature, you must have an existing Amazon ECS cluster associated
 with your AWS account. Amazon ECS Exec uses Systems Manager to establish a connection with the
 containers in your cluster. Amazon ECSrequires specific Task IAM Role Permissions to
 communicate with the SSM service.


For information about the IAM role and policy that's specific to Amazon ECS Exec, see
 [IAM permissions required for ECS Exec](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html#ecs-exec-enabling-and-using "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html#ecs-exec-enabling-and-using") in the *Amazon ECS* *Developer Guide*.


## 
 Working with the Amazon ECS Exec


You can enable or disable the Amazon ECS Exec directly from the AWS Explorer in the
 AWS Toolkit for AWS Cloud9. When you enabled Amazon ECS Exec, choose containers from the Amazon ECS
 menu, and run commands against them.


### 
 Enabling Amazon ECS Exec


1. From the AWS Explorer, locate and expand the Amazon ECS menu.
2. Expand the cluster with the service that you want to modify.
3. Open the context menu for (right-click) the service and choose **Enable Command Execution**.

###### Important

This step starts a new deployment of your service and might take a few minutes. For more
 information, see the note at the beginning of this section.


### 
 Disabling Amazon ECS Exec


1. From the AWS Explorer, locate and expand the Amazon ECS menu.
2. Expand the cluster that contains the service that you want.
3. Open the context menu for (right-click) the service and choose **Disable Command Execution**.

###### Important

This step starts a new deployment of your service and might take a few minutes. For more
 information, see the note at the beginning of this section.


### 
 Running commands against a Container


To run commands against a container using the AWS Explorer, Amazon ECS Exec must be enabled. If it's not enabled, see the [Enabling Amazon ECS Exec](#enabling-exec "#enabling-exec")  procedure in this section.


1. From the AWS Explorer, locate and expand the Amazon ECS menu.
2. Expand the cluster that
 the service that you want.
3. Expand the service to list the associated containers.
4. Open the context menu for (right-click) the container and choose **Run Command in Container**.
5. A **prompt** opens with a list of running Tasks. Choose the
 **Task ARN** that you want.


###### Note

If only one task is running, a prompt doesn't open. Instead, the task is auto-selected.
6. When prompted, enter the command that you want to run and press **Enter** to proceed.
