# Step 6: Clean up your WordPress application and

related resources

You've now successfully made an update to the WordPress code and redeployed the site. To
avoid ongoing charges for resources you created for this tutorial, you should delete:

- Any AWS CloudFormation stacks (or terminate any Amazon EC2 instances, if you created them outside of
  AWS CloudFormation).
- Any Amazon S3 buckets.
- The `WordPress_App` application in CodeDeploy.
- The AWS Systems Manager State Manager association for the CodeDeploy agent.
  You can use the AWS CLI, the AWS CloudFormation, Amazon S3, Amazon EC2, and CodeDeploy consoles, or the AWS APIs to
  perform the cleanup.

###### Topics

- [To clean up resources (CLI)](#tutorials-wordpress-clean-up-cli "#tutorials-wordpress-clean-up-cli")
- [To clean up resources (console)](#tutorials-wordpress-clean-up-console "#tutorials-wordpress-clean-up-console")
- [What's next?](#tutorials-wordpress-clean-up-whats-next "#tutorials-wordpress-clean-up-whats-next")

## To clean up resources (CLI)

1. If you used our AWS CloudFormation template for this tutorial, call the
   **delete-stack** command against the stack named
   `CodeDeployDemoStack`. This will terminate all accompanying
   Amazon EC2 instances and delete all accompanying IAM roles the stack created:

```
aws cloudformation delete-stack --stack-name CodeDeployDemoStack
```

2. To delete the Amazon S3 bucket, call the **rm** command with the
   **--recursive** switch against the bucket named
   `amzn-s3-demo-bucket`. This will delete the bucket and
   all objects in the bucket:

```
aws s3 rm s3://amzn-s3-demo-bucket --recursive --region `region`
```

3. To delete the `WordPress_App` application, call the
   **delete-application** command. This will also delete all associated
   deployment group records and deployment records for the application:

```
aws deploy delete-application --application-name WordPress_App
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

If you did not use the AWS CloudFormation stack for this tutorial, call the
**terminate-instances** command to terminate any Amazon EC2 instances you manually
created. Supply the ID of the Amazon EC2 instance to terminate:

```
aws ec2 terminate-instances --instance-ids `instanceId`
```

## To clean up resources (console)

If you used our AWS CloudFormation template for this tutorial, delete the associated AWS CloudFormation
stack.

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. In the **Filter** box, type the AWS CloudFormation stack name you created earlier
   (for example, `CodeDeployDemoStack`).
3. Select the box beside stack name. In the **Actions** menu, choose
   **Delete Stack**.

AWS CloudFormation deletes the stack, terminates all accompanying Amazon EC2 instances, and deletes all
accompanying IAM roles.

To terminate Amazon EC2 instances you created outside of an AWS CloudFormation stack:

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the **INSTANCES** list, choose
   **Instances**.
3. In the search box, type the name of the Amazon EC2 instance you want to terminate (for
   example, `CodeDeployDemo`), and then press Enter.
4. Choose the Amazon EC2 instance name.
5. In the **Actions** menu, point to **Instance
   State**, and then choose **Terminate**. When prompted, choose
   **Yes, Terminate**.

Repeat these steps for each instance.

To delete the Amazon S3 bucket:

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the list of buckets, browse to and choose the name of the Amazon S3 bucket you created
   earlier (for example, `amzn-s3-demo-bucket`).
3. Before you can delete a bucket, you must first delete its contents. Select all of the
   files in the bucket, such as `WordPressApp.zip`.
   In the **Actions** menu, choose **Delete**. When
   prompted to confirm the deletion, choose **OK**.
4. After the bucket is empty, you can delete the bucket. In the list of buckets, choose
   the row of the bucket (but not the bucket name). Choose **Delete
   bucket**, and when prompted to confirm, choose **OK**.

To delete the `WordPress_App` application from CodeDeploy:

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, then choose **Applications**. 3. In the list of applications, choose
**WordPress_App**. 4. On the **Application details** page, choose **Delete
application**. 5. When prompted, enter the name of the application to confirm you want to delete it, and
then choose **Delete**.

To delete the Systems Manager State Manager association:

1. Open the AWS Systems Manager console at https://console.aws.amazon.com/systems-manager.
2. In the navigation pane, choose **State Manager**.
3. Choose the association you created and choose **Delete**.

## What's next?

If you've arrived here, congratulations! You have successfully completed a CodeDeploy
deployment, and then updated your site's code and redeployed it.
