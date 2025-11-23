# Step 2: Deploy the

application to the Amazon EC2 Auto Scaling group

In this step, you'll deploy the revision to the single Amazon EC2 instance in the Amazon EC2 Auto Scaling
group.

###### Topics

- [To create the
  deployment (CLI)](#tutorials-auto-scaling-group-create-deployment-cli "#tutorials-auto-scaling-group-create-deployment-cli")
- [To create
  the deployment (console)](#tutorials-auto-scaling-group-create-deployment-console "#tutorials-auto-scaling-group-create-deployment-console")

## To create the

deployment (CLI)

1. Call the **create-application** command to create an
   application named `SimpleDemoApp`:

```
aws deploy create-application --application-name SimpleDemoApp
```

2. You should have already created a service role by following the
   instructions in [Step 2: Create a service role for
   CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md"). The service role
   will give CodeDeploy permission to access your Amazon EC2 instances to expand (read)
   their tags. You will need the service role ARN. To get the service role ARN,
   follow the instructions in [Get the service role ARN (CLI)](getting-started-create-service-role.md#getting-started-get-service-role-cli "getting-started-create-service-role.md#getting-started-get-service-role-cli") .
3. Now that you have a service role ARN, call the
   **create-deployment-group** command to create a
   deployment group named `SimpleDemoDG`,
   associated with the application named
   `SimpleDemoApp`, using the Amazon EC2 Auto Scaling group
   named `CodeDeployDemo-AS-Group` and deployment
   configuration named `CodeDeployDefault.OneAtATime`, with the
   specified service role ARN.

###### Note

The [create-deployment-group](../../../cli/latest/reference/deploy/create-deployment-group.md "../../../cli/latest/reference/deploy/create-deployment-group.md") command provides support for creating
triggers that result in the sending of Amazon SNS notifications to topic subscribers about
specified events in deployments and instances. The command also supports options for
automatically rolling back deployments and setting up alarms to stop deployments when
monitoring thresholds in Amazon CloudWatch alarms are met. Commands for these actions are
not included in this tutorial.

On local Linux, macOS, or Unix machines:

```
aws deploy create-deployment-group \
  --application-name SimpleDemoApp \
  --auto-scaling-groups CodeDeployDemo-AS-Group \
  --deployment-group-name SimpleDemoDG \
  --deployment-config-name CodeDeployDefault.OneAtATime \
  --service-role-arn `service-role-arn`
```

On local Windows machines:

```
aws deploy create-deployment-group --application-name SimpleDemoApp --auto-scaling-groups CodeDeployDemo-AS-Group --deployment-group-name SimpleDemoDG --deployment-config-name CodeDeployDefault.OneAtATime --service-role-arn `service-role-arn`
```

4. Call the **create-deployment** command to create a
   deployment associated with the application named
   `SimpleDemoApp`, the deployment
   configuration named `CodeDeployDefault.OneAtATime`, the
   deployment group named `SimpleDemoDG`,
   using the revision at the specified location.

**For Amazon Linux and RHEL Amazon EC2 instances, calling from
local Linux, macOS, or Unix machines**

```
aws deploy create-deployment \
  --application-name SimpleDemoApp \
  --deployment-config-name CodeDeployDefault.OneAtATime \
  --deployment-group-name SimpleDemoDG \
  --s3-location bucket=`bucket-name`,bundleType=zip,key=samples/latest/SampleApp_Linux.zip
```

`bucket-name` is the name of the Amazon S3
bucket that contains the CodeDeploy Resource Kit files for your region. For example, for the
US East (Ohio) Region, replace `bucket-name` with
`aws-codedeploy-us-east-2`. For a list of bucket names, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names "resource-kit.md#resource-kit-bucket-names").

**For Amazon Linux and RHEL Amazon EC2 instances, calling from
local Windows machines**

```
aws deploy create-deployment --application-name SimpleDemoApp --deployment-config-name CodeDeployDefault.OneAtATime --deployment-group-name SimpleDemoDG --s3-location bucket=`bucket-name`,bundleType=zip,key=samples/latest/SampleApp_Linux.zip
```

`bucket-name` is the name of the Amazon S3
bucket that contains the CodeDeploy Resource Kit files for your region. For example, for the
US East (Ohio) Region, replace `bucket-name` with
`aws-codedeploy-us-east-2`. For a list of bucket names, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names "resource-kit.md#resource-kit-bucket-names").

**For Windows Server Amazon EC2 instances, calling from local
Linux, macOS, or Unix machines**

```
aws deploy create-deployment \
  --application-name SimpleDemoApp \
  --deployment-config-name CodeDeployDefault.OneAtATime \
  --deployment-group-name SimpleDemoDG \
  --s3-location bucket=`bucket-name`,bundleType=zip,key=samples/latest/SampleApp_Windows.zip
```

`bucket-name` is the name of the Amazon S3
bucket that contains the CodeDeploy Resource Kit files for your region. For example, for the
US East (Ohio) Region, replace `bucket-name` with
`aws-codedeploy-us-east-2`. For a list of bucket names, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names "resource-kit.md#resource-kit-bucket-names").

**For Windows Server Amazon EC2 instances, calling from local
Windows machines**

```
aws deploy create-deployment --application-name SimpleDemoApp --deployment-config-name CodeDeployDefault.OneAtATime --deployment-group-name SimpleDemoDG --s3-location bucket=`bucket-name`,bundleType=zip,key=samples/latest/SampleApp_Windows.zip
```

`bucket-name` is the name of the Amazon S3
bucket that contains the CodeDeploy Resource Kit files for your region. For example, for the
US East (Ohio) Region, replace `bucket-name` with
`aws-codedeploy-us-east-2`. For a list of bucket names, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names "resource-kit.md#resource-kit-bucket-names").

###### Note

Currently, CodeDeploy does not provide a sample revision to deploy to
Ubuntu Server Amazon EC2 instances. To create a revision on your own, see [Working with application revisions for CodeDeploy](application-revisions.md "application-revisions.md"). 5. Call the **get-deployment** command to make sure the
deployment was successful.

Before you call this command, you will need the ID of the deployment,
which should have been returned by the call to the
**create-deployment** command. If you need to get the
deployment ID again, call the **list-deployments** command
against the application named
`SimpleDemoApp` and the deployment
group named `SimpleDemoDG`:

```
aws deploy list-deployments --application-name SimpleDemoApp --deployment-group-name SimpleDemoDG --query "deployments" --output text
```

Now, call the **get-deployment** command using the
deployment ID:

```
aws deploy get-deployment --deployment-id `deployment-id` --query "deploymentInfo.status" --output text
```

Do not continue until the returned value is `Succeeded`.

## To create

the deployment (console)

1. You should have already created a service role by following the
   instructions in [Step 2: Create a service role for
   CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md"). The service role
   will give CodeDeploy permission to access your instances to expand (read) their
   tags. Before you use the CodeDeploy console to deploy your application revision,
   you will need the service role ARN. To get the service role ARN, follow the
   instructions in [Get the service role ARN (console)](getting-started-create-service-role.md#getting-started-get-service-role-console "getting-started-create-service-role.md#getting-started-get-service-role-console") .
2. Now that you have the service role ARN, you can use the CodeDeploy console to
   deploy your application revision.

Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 3. In the navigation pane, expand **Deploy**, then choose **Applications**. 4. Choose **Create application**. 5. Choose **Custom application**. 6. In **Application name**, enter
`SimpleDemoApp`. 7. In **Compute platform**, choose
**EC2/On-premises**. 8. Choose **Create application**. 9. On the **Deployment groups** tab, choose **Create
deployment group**. 10. In **Deployment group name**, enter
`SimpleDemoDG`. 11. In **Service Role**, choose the name of your service
role. 12. In **Deployment type**, choose
**In-place**. 13. In **Environment configuration** select **Amazon EC2 Auto Scaling
groups**, and then choose
`CodeDeployDemo-AS-Group`. 14. In **Deployment configuration**, choose
**CodeDeployDefault.OneAtATime**. 15. Clear **Enable load balancing**. 16. Choose **Create deployment group**. 17. In the deployment group page, choose **Create
deployment**. 18. In **Revision type**, choose **My application is
stored in Amazon S3**. 19. In **Revision location**, enter the location of the
sample application for your operating system and region.

**For Amazon Linux and RHEL Amazon EC2
instances**

| Region                           | Location of sample application                                                                             |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| US East (Ohio) Region            | `http://s3-us-east-2.amazonaws.com/aws-codedeploy-us-east-2/samples/latest/SampleApp_Linux.zip`            |
| US East (N. Virginia) Region     | `http://s3.amazonaws.com/aws-codedeploy-us-east-1/samples/latest/SampleApp_Linux.zip`                      |
| US West (N. California) Region   | `http://s3-us-west-1.amazonaws.com/aws-codedeploy-us-west-1/samples/latest/SampleApp_Linux.zip`            |
| US West (Oregon) Region          | `http://s3-us-west-2.amazonaws.com/aws-codedeploy-us-west-2/samples/latest/SampleApp_Linux.zip`            |
| Canada (Central) Region          | `http://s3-ca-central-1.amazonaws.com/aws-codedeploy-ca-central-1/samples/latest/SampleApp_Linux.zip`      |
| Europe (Ireland) Region          | `http://s3-eu-west-1.amazonaws.com/aws-codedeploy-eu-west-1/samples/latest/SampleApp_Linux.zip`            |
| Europe (London) Region           | `http://s3-eu-west-2.amazonaws.com/aws-codedeploy-eu-west-2/samples/latest/SampleApp_Linux.zip`            |
| Europe (Paris) Region            | `http://s3-eu-west-3.amazonaws.com/aws-codedeploy-eu-west-3/samples/latest/SampleApp_Linux.zip`            |
| Europe (Frankfurt) Region        | `http://s3-eu-central-1.amazonaws.com/aws-codedeploy-eu-central-1/samples/latest/SampleApp_Linux.zip`      |
| Israel (Tel Aviv) Region         | `https://aws-codedeploy-il-central-1.s3.il-central-1.amazonaws.com/samples/latest/SampleApp_Linux.zip`     |
| Asia Pacific (Hong Kong) Region  | `https://aws-codedeploy-ap-east-1.s3.ap-east-1.amazonaws.com/samples/latest/SampleApp_Linux.zip`           |
| Asia Pacific (Tokyo) Region      | `http://s3-ap-northeast-1.amazonaws.com/aws-codedeploy-ap-northeast-1/samples/latest/SampleApp_Linux.zip`  |
| Asia Pacific (Seoul) Region      | `http://s3-ap-northeast-2.amazonaws.com/aws-codedeploy-ap-northeast-2/samples/latest/SampleApp_Linux.zip`  |
| Asia Pacific (Singapore) Region  | `http://s3-ap-southeast-1.amazonaws.com/aws-codedeploy-ap-southeast-1/samples/latest/SampleApp_Linux.zip`  |
| Asia Pacific (Sydney) Region     | `http://s3-ap-southeast-2.amazonaws.com/aws-codedeploy-ap-southeast-2/samples/latest/SampleApp_Linux.zip`  |
| Asia Pacific (Melbourne) Region  | `https://aws-codedeploy-ap-southeast-4.s3.ap-southeast-4.amazonaws.com/samples/latest/SampleApp_Linux.zip` |
| Asia Pacific (Mumbai) Region     | `http://s3-ap-south-1.amazonaws.com/aws-codedeploy-ap-south-1/samples/latest/SampleApp_Linux.zip`          |
| South America (São Paulo) Region | `http://s3-sa-east-1.amazonaws.com/aws-codedeploy-sa-east-1/samples/latest/SampleApp_Linux.zip`            |

**For Windows Server Amazon EC2 instances**

| Region                           | Location of sample application                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| US East (Ohio) Region            | `http://s3-us-east-2.amazonaws.com/aws-codedeploy-us-east-2/samples/latest/SampleApp_Windows.zip`            |
| US East (N. Virginia) Region     | `http://s3.amazonaws.com/aws-codedeploy-us-east-1/samples/latest/SampleApp_Windows.zip`                      |
| US West (N. California) Region   | `http://s3-us-west-1.amazonaws.com/aws-codedeploy-us-west-1/samples/latest/SampleApp_Windows.zip`            |
| US West (Oregon) Region          | `http://s3-us-west-2.amazonaws.com/aws-codedeploy-us-west-2/samples/latest/SampleApp_Windows.zip`            |
| Canada (Central) Region          | `http://s3-ca-central-1.amazonaws.com/aws-codedeploy-ca-central-1/samples/latest/SampleApp_Windows.zip`      |
| Europe (Ireland) Region          | `http://s3-eu-west-1.amazonaws.com/aws-codedeploy-eu-west-1/samples/latest/SampleApp_Windows.zip`            |
| Europe (London) Region           | `http://s3-eu-west-2.amazonaws.com/aws-codedeploy-eu-west-2/samples/latest/SampleApp_Windows.zip`            |
| Europe (Paris) Region            | `http://s3-eu-west-3.amazonaws.com/aws-codedeploy-eu-west-3/samples/latest/SampleApp_Windows.zip`            |
| Europe (Frankfurt) Region        | `http://s3-eu-central-1.amazonaws.com/aws-codedeploy-eu-central-1/samples/latest/SampleApp_Windows.zip`      |
| Israel (Tel Aviv) Region         | `https://aws-codedeploy-il-central-1.s3.il-central-1.amazonaws.com/samples/latest/SampleApp_Windows.zip`     |
| Asia Pacific (Hong Kong) Region  | `https://aws-codedeploy-ap-east-1.s3.ap-east-1.amazonaws.com/samples/latest/SampleApp_Windows.zip`           |
| Asia Pacific (Seoul) Region      | `http://s3-ap-northeast-2.amazonaws.com/aws-codedeploy-ap-northeast-2/samples/latest/SampleApp_Windows.zip`  |
| Asia Pacific (Singapore) Region  | `http://s3-ap-southeast-1.amazonaws.com/aws-codedeploy-ap-southeast-1/samples/latest/SampleApp_Windows.zip`  |
| Asia Pacific (Sydney) Region     | `http://s3-ap-southeast-2.amazonaws.com/aws-codedeploy-ap-southeast-2/samples/latest/SampleApp_Windows.zip`  |
| Asia Pacific (Melbourne) Region  | `https://aws-codedeploy-ap-southeast-4.s3.ap-southeast-4.amazonaws.com/samples/latest/SampleApp_Windows.zip` |
| Asia Pacific (Mumbai) Region     | `http://s3-ap-south-1.amazonaws.com/aws-codedeploy-ap-south-1/samples/latest/SampleApp_Windows.zip`          |
| South America (São Paulo) Region | `http://s3-sa-east-1.amazonaws.com/aws-codedeploy-sa-east-1/samples/latest/SampleApp_Windows.zip`            |

**For Ubuntu Server Amazon EC2 instances**

Type the location of your custom application revision stored in
Amazon S3. 20. Leave **Deployment description** blank. 21. Expand **Advanced**. 22. Choose **Create deployment**.

###### Note

If **Failed** appears instead of
**Succeeded**, you may want to try some of the
techniques in [Monitor and troubleshoot your
deployment](tutorials-wordpress-deploy-application.md#tutorials-wordpress-deploy-application-monitor "tutorials-wordpress-deploy-application.md#tutorials-wordpress-deploy-application-monitor")
(using the application name of
`SimpleDemoApp` and the deployment
group name of `SimpleDemoDG`).
