# Step 4: Deploy your Hello World

application

Now you deploy the sample Hello World application revision you uploaded to Amazon S3. You use the
AWS CLI or the CodeDeploy console to deploy the revision and monitor the deployment's progress. After
the application revision is successfully deployed, you check the results.

###### Topics

- [Deploy your
  application revision with CodeDeploy](#tutorials-windows-deploy-application-create-deployment "#tutorials-windows-deploy-application-create-deployment")
- [Monitor and troubleshoot your
  deployment](#tutorials-windows-deploy-application-monitor "#tutorials-windows-deploy-application-monitor")
- [Verify your deployment](#tutorials-windows-deploy-application-verify "#tutorials-windows-deploy-application-verify")

## Deploy your

application revision with CodeDeploy

You can deploy your application using the CLI or the console.

###### Topics

- [To deploy your
  application revision (CLI)](#tutorials-windows-deploy-application-create-deployment-cli "#tutorials-windows-deploy-application-create-deployment-cli")
- [To deploy
  your application revision (console)](#tutorials-windows-deploy-application-create-deployment-console "#tutorials-windows-deploy-application-create-deployment-console")

### To deploy your

application revision (CLI)

1. First, the deployment needs a deployment group. However, before you create the
   deployment group, you need a service role ARN. A service role is an IAM role that
   gives a service permission to act on your behalf. In this case, the service role gives
   CodeDeploy permission to access your Amazon EC2 instances to expand (read) their Amazon EC2 instance
   tags.

You should have already followed the instructions in [Create a service role (CLI)](getting-started-create-service-role.md#getting-started-create-service-role-cli "getting-started-create-service-role.md#getting-started-create-service-role-cli") to create a service role. To
get the ARN of the service role, see [Get the service role ARN (CLI)](getting-started-create-service-role.md#getting-started-get-service-role-cli "getting-started-create-service-role.md#getting-started-get-service-role-cli") . 2. Now that you have the ARN, call the **create-deployment-group**
command to create a deployment group named `HelloWorld_DepGroup`,
associated with the application named `HelloWorld_App`, using the
Amazon EC2 instance tag named `CodeDeployDemo` and deployment
configuration named `CodeDeployDefault.OneAtATime`, with the service role
ARN:

```
aws deploy create-deployment-group --application-name HelloWorld_App --deployment-group-name HelloWorld_DepGroup --deployment-config-name CodeDeployDefault.OneAtATime --ec2-tag-filters Key=Name,Value=CodeDeployDemo,Type=KEY_AND_VALUE --service-role-arn `serviceRoleARN`
```

###### Note

The [create-deployment-group](../../../cli/latest/reference/deploy/create-deployment-group.md "../../../cli/latest/reference/deploy/create-deployment-group.md") command provides support for creating
triggers that result in the sending of Amazon SNS notifications to topic subscribers about
specified events in deployments and instances. The command also supports options for
automatically rolling back deployments and setting up alarms to stop deployments when
monitoring thresholds in Amazon CloudWatch alarms are met. Commands for these actions are
not included in this tutorial. 3. Before you create a deployment, the instances in your deployment group must have the
CodeDeploy agent installed. You can install the agent from the command line with AWS Systems Manager
with the following command:

```
aws ssm create-association --name AWS-ConfigureAWSPackage --targets Key=tag:Name,Values=CodeDeployDemo --parameters action=Install,name=AWSCodeDeployAgent --schedule-expression "cron(0 2 ? * SUN *)"
```

This command creates an association in Systems Manager State Manager that will install the
CodeDeploy agent and then attempt to update it at 2:00 every Sunday morning. For more
information about the CodeDeploy agent, see [Working with the CodeDeploy agent](codedeploy-agent.md "codedeploy-agent.md"). For more information about Systems Manager, see [What is AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md"). 4. Now call the **create-deployment** command to create a deployment
associated with the application named `HelloWorld_App`, the
deployment configuration named `CodeDeployDefault.OneAtATime`, and the
deployment group named `HelloWorld_DepGroup`, using the application
revision named `HelloWorld_App.zip` in the bucket named
`amzn-s3-demo-bucket`:

```
aws deploy create-deployment --application-name HelloWorld_App --deployment-config-name CodeDeployDefault.OneAtATime --deployment-group-name HelloWorld_DepGroup --s3-location bucket=amzn-s3-demo-bucket,bundleType=zip,key=HelloWorld_App.zip
```

### To deploy

your application revision (console)

1. Before you use the CodeDeploy console to deploy your application revision, you need a
   service role ARN. A service role is an IAM role that gives a service permission to act
   on your behalf. In this case, the service role gives CodeDeploy permission to access your
   Amazon EC2 instances to expand (read) their Amazon EC2 instance tags.

You should have already followed the instructions in [Create a service role (console)](getting-started-create-service-role.md#getting-started-create-service-role-console "getting-started-create-service-role.md#getting-started-create-service-role-console") to create a service
role. To get the ARN of the service role, see [Get the service role ARN (console)](getting-started-create-service-role.md#getting-started-get-service-role-console "getting-started-create-service-role.md#getting-started-get-service-role-console") . 2. Now that you have the ARN, you can use the CodeDeploy console to deploy your application
revision.

Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 3. In the navigation pane, expand **Deploy**, then choose **Applications**. 4. Choose **HelloWorld_App**. 5. On the **Deployment groups** tab, choose **Create
deployment group**. 6. In **Deployment group name**, enter
`HelloWorld_DepGroup`. 7. In **Service Role**, choose the name of the service role. 8. In **Deployment type**, choose
**In-place**. 9. In **Environment configuration**, select **Amazon EC2
instances**. 10. In **Agent configuration with AWS Systems Manager**, keep the
defaults. 11. In **Key**, enter `Name`. 12. In **Value**, enter
`CodeDeployDemo`. 13. In **Deployment configuration**, choose
**CodeDeployDefault.OneAtATime**. 14. In **Load Balancer**, clear **Enable load
balancing**. 15. Choose **Create deployment group**. 16. Choose **Create deployment**. 17. In **Deployment group**, choose
**HelloWorld_DepGroup** 18. In **Revision type**, choose **My application is stored in
Amazon S3**, and then in **Revision location**, enter the
location of the sample Hello World application revision you previously uploaded to Amazon S3.
To get the location:

    1. Open the Amazon S3 console at
     [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
    2. In the list of buckets, choose
     **amzn-s3-demo-bucket** (or the name of the bucket
     where you uploaded your application revision).
    3. In the list of objects, choose **HelloWorld\_App.zip**.
    4. In the **Overview** tab, choose **Copy
     path**.
    5. Return to the CodeDeploy console, and in **Revision Location**,
     paste the **Link** field value.

19. For **Revision file type**, choose **.zip**.
20. (Optional) Enter a comment in **Deployment description**.
21. Choose **Create deployment**. Information about your newly created
    deployment appears on the **Deployments** page.

## Monitor and troubleshoot your

deployment

Use the AWS CLI or the console to monitor and troubleshoot your deployment.

###### Topics

- [To monitor and
  troubleshoot your deployment (CLI)](#tutorials-windows-deploy-application-monitor-cli "#tutorials-windows-deploy-application-monitor-cli")
- [To monitor and
  troubleshoot your deployment (console)](#tutorials-windows-deploy-application-monitor-console "#tutorials-windows-deploy-application-monitor-console")

### To monitor and

troubleshoot your deployment (CLI)

1. Get the deployment's ID by calling the **list-deployments** command
   against the application named `HelloWorld_App` and the deployment
   group named `HelloWorld_DepGroup`:

```
aws deploy list-deployments --application-name HelloWorld_App --deployment-group-name HelloWorld_DepGroup --query "deployments" --output text
```

2. Call the **get-deployment** command with the deployment ID:

```
aws deploy get-deployment --deployment-id `deploymentID` --query "deploymentInfo.status" --output text
```

3. The command returns the deployment's overall status. If successful, the value is
   `Succeeded`.

If the overall status is `Failed`, you can call commands such as
[list-deployment-instances](../../../cli/latest/reference/deploy/list-deployment-instances.md "../../../cli/latest/reference/deploy/list-deployment-instances.md") and [get-deployment-instance](../../../cli/latest/reference/deploy/get-deployment-instance.md "../../../cli/latest/reference/deploy/get-deployment-instance.md") to
troubleshoot. For more troubleshooting options, see [Analyzing log files to investigate
deployment failures on instances](troubleshooting-ec2-instances.md#troubleshooting-deploy-failures "troubleshooting-ec2-instances.md#troubleshooting-deploy-failures").

### To monitor and

troubleshoot your deployment (console)

On the **Deployments** page in the CodeDeploy console, you can monitor your
deployment's status in the **Status** column.

To get more information about your deployment, especially if the
**Status** column value has any value other than
**Succeeded**:

1. In the **Deployments** table, choose your deployment ID. After a
   deployment fails, a message that describes the reason for the failure appears in the
   deployment's details page.
2. . More information about the deployment's instances is displayed. After a deployment
   fails, you might be able to determine on which Amazon EC2 instances and at which step the
   deployment failed.
3. If you want to do more troubleshooting, you can use a technique like [View Instance Details](instances-view-details.md "instances-view-details.md"). You can
   also analyze the deployment log files on an Amazon EC2 instance. For more information, see
   [Analyzing log files to investigate
   deployment failures on instances](troubleshooting-ec2-instances.md#troubleshooting-deploy-failures "troubleshooting-ec2-instances.md#troubleshooting-deploy-failures").

## Verify your deployment

After your deployment is successful, verify your installation is working. Use the public
DNS address of the Amazon EC2 instance to view the web page in a web browser. (To get the public
DNS value, in the Amazon EC2 console, choose the Amazon EC2 instance, and on the
**Description** tab, look for the value in **Public
DNS**.)

For example, if the public DNS address of your Amazon EC2 instance is
`ec2-01-234-567-890.compute-1.amazonaws.com`, you would use the following URL:

```
http://ec2-01-234-567-890.compute-1.amazonaws.com
```

If successful, you should see a Hello World webpage.
