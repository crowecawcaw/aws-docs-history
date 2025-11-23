# Step 6: Clean up

In this step, you'll delete the Amazon EC2 Auto Scaling group to avoid ongoing charges for resources you
used during this tutorial. Optionally, you can delete the Amazon EC2 Auto Scaling configuration and CodeDeploy
deployment component records.

###### Topics

- [To clean up resources
  (CLI)](#tutorials-auto-scaling-group-clean-up-cli "#tutorials-auto-scaling-group-clean-up-cli")
- [To clean up
  resources (console)](#tutorials-auto-scaling-group-clean-up-console "#tutorials-auto-scaling-group-clean-up-console")

## To clean up resources

(CLI)

1. Delete the Amazon EC2 Auto Scaling group by calling the
   **delete-auto-scaling-group** command against
   `CodeDeployDemo-AS-Group`. This will also
   terminate the Amazon EC2 instances.

```
aws autoscaling delete-auto-scaling-group --auto-scaling-group-name CodeDeployDemo-AS-Group --force-delete
```

2. Optionally, delete the Amazon EC2 Auto Scaling launch template by calling the
   **delete-launch-template** command against the launch
   configuration named
   `CodeDeployDemo-AS-Launch-Template`:

```
aws ec2 delete-launch-template --launch-template-name CodeDeployDemo-AS-Launch-Template
```

3. Optionally, delete the application from CodeDeploy by calling the
   **delete-application** command against the application
   named `SimpleDemoApp`. This will also
   delete all associated deployment, deployment group, and revision records.

```
aws deploy delete-application --application-name SimpleDemoApp
```

4. To delete the Systems Manager State Manager association, call the
   **delete-association** command.

```
aws ssm delete-association --assocation-id `association-id`
```

You can get the `association-id` by calling the
**describe-association** command.

```
aws ssm describe-association --name AWS-ConfigureAWSPackage --targets Key=tag:Name,Values=CodeDeployDemo
```

## To clean up

resources (console)

To delete the Amazon EC2 Auto Scaling group, which also terminates the Amazon EC2 instances:

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the Amazon EC2 navigation pane, under **Amazon EC2 Auto Scaling**, choose **Amazon EC2 Auto Scaling
   Groups**, and then choose the
   `CodeDeployDemo-AS-Group` entry.
3. Choose **Actions**, choose **Delete**,
   and then choose **Yes, Delete**.

(Optional) To delete the launch template:

1. In the navigation bar, under **Amazon EC2 Auto Scaling**, choose
   **Launch Configurations**, and then choose
   `CodeDeployDemo-AS-Launch-Template`.
2. Choose **Actions**, choose **Delete launch
   configuration**, and then choose **Yes,
   Delete**.

3. Optionally, delete the application from CodeDeploy. This will also delete all
   associated deployment, deployment group, and revision records. Open the
   CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").
4. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md").

In the navigation pane, expand **Deploy**, then choose **Applications**. 3. In the list of applications, choose
**SimpleDemoApp**. 4. On the **Application details** page, choose
**Delete application**. 5. When prompted, enter `Delete`, and then choose
**Delete**.

To delete the Systems Manager State Manager association:

1. Open the AWS Systems Manager console at https://console.aws.amazon.com/systems-manager.
2. In the navigation pane, choose **State Manager**.
3. Choose the association you created and choose
   **Delete**.
