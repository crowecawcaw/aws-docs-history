Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Create and run the application (CLI)

In this section, you use the AWS Command Line Interface to create and run the Managed Service for Apache Flink application. Use the _kinesisanalyticsv2_ AWS CLI command
to create and interact with Managed Service for Apache Flink applications.

## Create a permissions policy

###### Note

You must create a permissions policy and role for your application. If you do not create these IAM resources,
your application cannot access its data and log streams.

First, you create a permissions policy with two statements: one that grants permissions for the read action on the source stream,
and another that grants permissions for write actions on the sink stream. You then attach the policy to an IAM role
(which you create in the next section). Thus, when Managed Service for Apache Flink assumes the role, the service has the necessary permissions to read from the source stream and write to the sink stream.

Use the following code to create the `AKReadSourceStreamWriteSinkStream` permissions policy. Replace `username`
with the user name that you used to create the Amazon S3 bucket to store the application code. Replace the account ID in the Amazon Resource Names (ARNs)
`(012345678901)` with your account ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadCode",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::ka-app-code-`username`/getting-started-scala-1.0.jar"
 ]
 },
 {
 "Sid": "DescribeLogGroups",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:us-west-2:`123456789012`:*"
 ]
 },
 {
 "Sid": "DescribeLogStreams",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:us-west-2:`123456789012`:log-group:/aws/kinesis-analytics/MyApplication:log-stream:*"
 ]
 },
 {
 "Sid": "PutLogEvents",
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:us-west-2:`123456789012`:log-group:/aws/kinesis-analytics/MyApplication:log-stream:kinesis-analytics-log-stream"
 ]
 },
 {
 "Sid": "ReadInputStream",
 "Effect": "Allow",
 "Action": "kinesis:*",
 "Resource": "arn:aws:kinesis:us-west-2:`123456789012`:stream/ExampleInputStream"
 },
 {
 "Sid": "WriteOutputStream",
 "Effect": "Allow",
 "Action": "kinesis:*",
 "Resource": "arn:aws:kinesis:us-west-2:`123456789012`:stream/ExampleOutputStream"
 }
 ]
}`

```

For step-by-step instructions to create a permissions policy,
see [Tutorial: Create and Attach Your First Customer Managed Policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md#part-two-create-policy "../../../IAM/latest/UserGuide/tutorial_managed-policies.md#part-two-create-policy")
in the _IAM User Guide_.

## Create an IAM policy

In this section, you create an IAM role that the Managed Service for Apache Flink application can assume to read a source stream and write to the sink stream.

Managed Service for Apache Flink cannot access your stream without permissions. You grant these permissions via an IAM role. Each IAM role has two policies attached.
The trust policy grants Managed Service for Apache Flink permission to assume the role, and the permissions policy determines what Managed Service for Apache Flink can do after assuming the role.

You attach the permissions policy that you created in the preceding section to this role.

###### To create an IAM role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles** and then **Create Role**.
3. Under **Select type of trusted identity**, choose **AWS Service**
4. Under **Choose the service that will use this role**, choose **Kinesis**.
5. Under **Select your use case**, choose **Managed Service for Apache Flink**.
6. Choose **Next: Permissions**.
7. On the **Attach permissions policies** page, choose **Next: Review**.
   You attach permissions policies after you create the role.
8. On the **Create role** page, enter `MF-stream-rw-role` for the **Role name**.
   Choose **Create role**.

Now you have created a new IAM role called `MF-stream-rw-role`. Next,
you update the trust and permissions policies for the role 9. Attach the permissions policy to the role.

###### Note

For this exercise, Managed Service for Apache Flink assumes this role for both reading data from a Kinesis data stream (source) and writing output to another
Kinesis data stream. So you attach the policy that you created in the previous step,
[Create a Permissions Policy](get-started-exercise.md#get-started-exercise-7-cli-policy "get-started-exercise.md#get-started-exercise-7-cli-policy").

    1. On the **Summary** page, choose the **Permissions** tab.
    2. Choose **Attach Policies**.
    3. In the search box, enter `AKReadSourceStreamWriteSinkStream` (the policy that you created in the previous section).
    4. Choose the `AKReadSourceStreamWriteSinkStream` policy, and choose **Attach policy**.

You now have created the service execution role that your application uses to access resources. Make a note of the ARN of the new role.

For step-by-step instructions for creating a role, see [Creating an IAM Role (Console)](../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console "../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console") in the _IAM User Guide_.

## Create the application

Save the following JSON code to a file named `create_request.json`. Replace the sample role ARN with the ARN for the role that you created previously. Replace the bucket ARN suffix (username) with the suffix that you chose in the previous section. Replace the sample account ID (012345678901)
in the service execution role with your account ID.

```
{
    "ApplicationName": "getting_started",
    "ApplicationDescription": "Scala getting started application",
    "RuntimeEnvironment": "FLINK-1_19",
    "ServiceExecutionRole": "arn:aws:iam::012345678901:role/MF-stream-rw-role",
    "ApplicationConfiguration": {
        "ApplicationCodeConfiguration": {
            "CodeContent": {
                "S3ContentLocation": {
                    "BucketARN": "arn:aws:s3:::ka-app-code-`username`",
                    "FileKey": "getting-started-scala-1.0.jar"
                }
            },
            "CodeContentType": "ZIPFILE"
        },
        "EnvironmentProperties":  {
         "PropertyGroups": [
            {
               "PropertyGroupId": "ConsumerConfigProperties",
               "PropertyMap" : {
                    "aws.region" : "us-west-2",
                    "stream.name" : "ExampleInputStream",
                    "flink.stream.initpos" : "LATEST"
               }
            },
            {
               "PropertyGroupId": "ProducerConfigProperties",
               "PropertyMap" : {
                    "aws.region" : "us-west-2",
                    "stream.name" : "ExampleOutputStream"
               }
            }
         ]
      }
    },
    "CloudWatchLoggingOptions": [
      {
         "LogStreamARN": "arn:aws:logs:us-west-2:`012345678901`:log-group:MyApplication:log-stream:kinesis-analytics-log-stream"
      }
   ]
}
```

Execute the [CreateApplication](../apiv2/API_CreateApplication.md "../apiv2/API_CreateApplication.md")
with the following request to create the application:

```
aws kinesisanalyticsv2 create-application --cli-input-json file://create_request.json
```

The application is now created. You start the application in the next step.

## Start the application

In this section, you use the [StartApplication](../apiv2/API_StartApplication.md "../apiv2/API_StartApplication.md")
action to start the application.

###### To start the application

1. Save the following JSON code to a file named `start_request.json`.

```
{
    "ApplicationName": "getting_started",
    "RunConfiguration": {
        "ApplicationRestoreConfiguration": {
         "ApplicationRestoreType": "RESTORE_FROM_LATEST_SNAPSHOT"
         }
    }
}
```

2. Execute the `StartApplication` action with the preceding request to start the application:

```
aws kinesisanalyticsv2 start-application --cli-input-json file://start_request.json
```

The application is now running. You can check the Managed Service for Apache Flink metrics on the Amazon CloudWatch console to verify that the application is working.

## Stop the application

In this section, you use the [StopApplication](../apiv2/API_StopApplication.md "../apiv2/API_StopApplication.md")
action to stop the application.

###### To stop the application

1. Save the following JSON code to a file named `stop_request.json`.

```
{
   "ApplicationName": "s3_sink"
}
```

2. Execute the `StopApplication` action with the preceding request to stop the application:

```
aws kinesisanalyticsv2 stop-application --cli-input-json file://stop_request.json
```

The application is now stopped.

## Add a CloudWatch logging

option

You can use the AWS CLI to add an Amazon CloudWatch log stream to your application. For information about using CloudWatch Logs with your application,
see [Setting Up Application Logging](cloudwatch-logs.md "cloudwatch-logs.md").

## Update

environment properties

In this section, you use the [UpdateApplication](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") action to change the environment
properties for the application without recompiling the application code. In this example, you change the Region of the source and destination streams.

###### To update environment properties for the application

1. Save the following JSON code to a file named `update_properties_request.json`.

```
{
      "ApplicationName": "getting_started",
       "CurrentApplicationVersionId": 1,
       "ApplicationConfigurationUpdate": {
        "EnvironmentPropertyUpdates": {
           "PropertyGroups": [
            {
               "PropertyGroupId": "ConsumerConfigProperties",
               "PropertyMap" : {
                    "aws.region" : "us-west-2",
                    "stream.name" : "ExampleInputStream",
                    "flink.stream.initpos" : "LATEST"
               }
            },
            {
               "PropertyGroupId": "ProducerConfigProperties",
               "PropertyMap" : {
                    "aws.region" : "us-west-2",
                    "stream.name" : "ExampleOutputStream"
               }
            }
           ]
        }
    }
```

2. Execute the `UpdateApplication` action with the preceding request to update environment properties:

```
aws kinesisanalyticsv2 update-application --cli-input-json file://update_properties_request.json
```

## Update the application code

When you need to update your application code with a new version of your code package, you use the [UpdateApplication](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") CLI action.

###### Note

To load a new version of the application code with the same file name, you must specify the new object version.
For more information about using Amazon S3 object versions, see
[Enabling or Disabling Versioning](../../../AmazonS3/latest/user-guide/enable-versioning.md "../../../AmazonS3/latest/user-guide/enable-versioning.md").

To use the AWS CLI, delete your previous code package from your Amazon S3 bucket, upload the new version, and call `UpdateApplication`, specifying the same Amazon S3 bucket and object name,
and the new object version. The application will restart with the new code package.

The following sample request for the `UpdateApplication` action reloads the application code and restarts the application.
Update the `CurrentApplicationVersionId` to the current application version. You can check the current application version using the
`ListApplications` or `DescribeApplication` actions. Update the bucket name suffix (<username>) with the suffix
that you chose in the [Create dependent resources](examples-gs-scala.md#examples-gs-scala-resources "examples-gs-scala.md#examples-gs-scala-resources") section.

```
{{
    "ApplicationName": "getting_started",
    "CurrentApplicationVersionId": 1,
    "ApplicationConfigurationUpdate": {
        "ApplicationCodeConfigurationUpdate": {
            "CodeContentUpdate": {
                "S3ContentLocationUpdate": {
                    "BucketARNUpdate": "arn:aws:s3:::ka-app-code-<username>",
                    "FileKeyUpdate": "getting-started-scala-1.0.jar",
                    "ObjectVersionUpdate": "SAMPLEUehYngP87ex1nzYIGYgfhypvDU"
                }
            }
        }
    }
}
```
