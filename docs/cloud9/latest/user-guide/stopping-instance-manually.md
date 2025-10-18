AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Manually stopping your environment's EC2
 instance

The [EC2 Instance](settings-project-change.md#settings-project-change-ec2-instance "settings-project-change.md#settings-project-change-ec2-instance") setting
 allows you to automatically stop your environment's Amazon EC2 instance as quickly as 30 minutes
 after you close all web browser instances that are connected to the IDE.

You also can manually stop the instance immediately using the console.

To manually stop an environment's EC2 instance, choose the following steps:

1. After you closed all web browser instances that are connected to the IDE, choose
 **Your environments** in the AWS Cloud9 console.
2. Choose the button in the top-right of the pane that shows details of the environment
 that you were using, and choose **View details**.
3. In **Environment details**, under **EC2
 Instance**, choose **Go To Instance**.
4. In the Amazon EC2 console, under **Instance state**, choose the check
 box to select your environment's instance. The **Instance state** might
 indicate that the instance is still running.
5. Choose **Instance state** and select **Stop
 instance**.
6. When prompted for confirmation, choose **Stop**. It can take a
 few minutes for the instance to stop.
