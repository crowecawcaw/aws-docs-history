# Creating environments for your application in

AWS AppConfig

For each AWS AppConfig application, you define one or more environments. An environment is a
logical deployment group of AppConfig targets, such as applications in a `Beta` or
`Production` environment, AWS Lambda functions, or containers. You can also define
environments for application subcomponents, such as the `Web`, `Mobile`,
and `Back-end`. You can configure Amazon CloudWatch alarms for each environment. The system
monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls
back the configuration.

###### Before You Begin

If you want to enable AWS AppConfig to roll back a configuration in response to a CloudWatch alarm,
then you must configure an AWS Identity and Access Management (IAM) role with permissions to enable AWS AppConfig to
respond to CloudWatch alarms. You choose this role in the following procedure. For more
information, see [Configure permissions for automatic rollback](setting-up-appconfig.md#getting-started-with-appconfig-cloudwatch-alarms-permissions "setting-up-appconfig.md#getting-started-with-appconfig-cloudwatch-alarms-permissions").

###### Topics

- [Creating an AWS AppConfig environment
  (console)](#appconfig-creating-environment-console "#appconfig-creating-environment-console")
- [Creating an AWS AppConfig environment
  (command line)](#appconfig-creating-environment-commandline "#appconfig-creating-environment-commandline")

## Creating an AWS AppConfig environment

(console)

Use the following procedure to create an AWS AppConfig environment by using the AWS Systems Manager
console.

###### To create an environment

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/ "https://console.aws.amazon.com/systems-manager/appconfig/").
2. In the navigation pane, choose **Applications**, and then choose
   the name of an application to open the details page.
3. Choose the **Environments** tab, and then choose **Create
   environment**.
4. For **Name**, enter a name for the environment.
5. For **Description**, enter information about the
   environment.
6. (Optional) In the **Monitors** section, choose the **IAM
   role** field, and then choose an IAM role with permission to call
   `cloudwatch:DescribeAlarms` on the metrics you want to monitor for
   alarms.
7. In the **CloudWatch alarms** list, enter the Amazon Resource Names (ARNs)
   one or more metrics to monitor. AWS AppConfig rolls back your configuration deployment if one
   of these metrics goes into an `ALARM` state. For information about
   recommended metrics, see [Monitoring deployments for automatic rollback](monitoring-deployments.md "monitoring-deployments.md")
8. (Optional) In the **Associate extensions** section, choose an
   extension from the list. For more information, see [Understanding AWS AppConfig
   extensions](working-with-appconfig-extensions-about.md "working-with-appconfig-extensions-about.md").
9. (Optional) In the **Tags** section, enter a key and an optional
   value. You can specify a maximum of 50 tags for a resource.
10. Choose **Create environment**.

AWS AppConfig creates the environment and then displays the **Environment
details** page. Proceed to [Creating a configuration profile in
AWS AppConfig](appconfig-creating-configuration-profile.md "appconfig-creating-configuration-profile.md").

## Creating an AWS AppConfig environment

(command line)

The following procedure describes how to use the AWS CLI (on Linux or Windows) or
AWS Tools for PowerShell to create an AWS AppConfig environment.

###### To create an environment step by step

1. Open the AWS CLI.
2. Run the following command to create an environment.

Linux

```
aws appconfig create-environment \
  --application-id `The_application_ID` \
  --name `A_name_for_the_environment` \
  --description `A_description_of_the_environment` \
  --monitors "AlarmArn=`ARN_of_the_Amazon_CloudWatch_alarm`,AlarmArnRole=`ARN_of_the_IAM role_for_AWS AppConfig_to_monitor_AlarmArn`" \
  --tags `User_defined_key_value_pair_metadata_of_the_environment`
```

Windows

```
aws appconfig create-environment ^
  --application-id `The_application_ID` ^
  --name `A_name_for_the_environment` ^
  --description `A_description_of_the_environment` ^
  --monitors "AlarmArn=`ARN_of_the_Amazon_CloudWatch_alarm`,AlarmArnRole=`ARN_of_the_IAM role_for_AWS AppConfig_to_monitor_AlarmArn`" ^
  --tags `User_defined_key_value_pair_metadata_of_the_environment`
```

PowerShell

```
New-APPCEnvironment `
  -Name `Name_for_the_environment` `
  -ApplicationId `The_application_ID`
  -Description `Description_of_the_environment` `
  -Monitors @{"AlarmArn=`ARN_of_the_Amazon_CloudWatch_alarm`,AlarmArnRole=`ARN_of_the_IAM role_for_AWS AppConfig_to_monitor_AlarmArn`"} `
  -Tag `Hashtable_type_user_defined_key_value_pair_metadata_of_the_environment`
```

The system returns information like the following.

Linux

```
{
   "ApplicationId": "The application ID",
   "Id": "The_environment ID",
   "Name": "Name of the environment",
   "State": "The state of the environment",
   "Description": "Description of the environment",

   "Monitors": [
      {
         "AlarmArn": "ARN of the Amazon CloudWatch alarm",
         "AlarmRoleArn": "ARN of the IAM role for AppConfig to monitor AlarmArn"
      }
   ]
}
```

Windows

```
{
   "ApplicationId": "The application ID",
   "Id": "The environment ID",
   "Name": "Name of the environment",
   "State": "The state of the environment"
   "Description": "Description of the environment",

   "Monitors": [
      {
         "AlarmArn": "ARN of the Amazon CloudWatch alarm",
         "AlarmRoleArn": "ARN of the IAM role for AppConfig to monitor AlarmArn"
      }
   ]
}
```

PowerShell

```
ApplicationId     : The application ID
ContentLength     : Runtime of the command
Description       : Description of the environment
HttpStatusCode    : HTTP Status of the runtime
Id                : The environment ID
Monitors          : {ARN of the Amazon CloudWatch alarm, ARN of the IAM role for AppConfig to monitor AlarmArn}
Name              : Name of the environment
Response Metadata : Runtime Metadata
State             : State of the environment
```

Proceed to [Creating a configuration profile in
AWS AppConfig](appconfig-creating-configuration-profile.md "appconfig-creating-configuration-profile.md").
