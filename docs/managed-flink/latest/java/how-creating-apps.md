Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Create a Managed Service for Apache Flink application

This topic contains information about creating a Managed Service for Apache Flink application.

###### This topic contains the following sections:

- [Build your Managed Service for Apache Flink application code](#how-creating-apps-building "#how-creating-apps-building")
- [Create your Managed Service for Apache Flink application](#how-creating-apps-creating "#how-creating-apps-creating")
- [Use customer managed keys](#how-creating-apps-use-cmk "#how-creating-apps-use-cmk")
- [Start your Managed Service for Apache Flink application](#how-creating-apps-starting "#how-creating-apps-starting")
- [Verify your Managed Service for Apache Flink application](#how-creating-apps-verifying "#how-creating-apps-verifying")
- [Enable system rollbacks for your Managed Service for Apache Flink
  application](how-system-rollbacks.md "how-system-rollbacks.md")

## Build your Managed Service for Apache Flink application code

This section describes the components that you use to build the application code for your
Managed Service for Apache Flink application.

We recommend that you use the latest supported version of Apache Flink for your
application code. For information about upgrading Managed Service for Apache Flink applications, see [Use in-place version upgrades for Apache
Flink](how-in-place-version-upgrades.md "how-in-place-version-upgrades.md").

You build your application code using [Apache Maven](https://maven.apache.org/ "https://maven.apache.org/").
An Apache Maven project uses a `pom.xml` file to specify the versions of components
that it uses.

###### Note

Managed Service for Apache Flink supports JAR files up to 512 MB in size. If you use a JAR file larger than this,
your application will fail to start.

Applications can now use the Java API from any Scala version. You must bundle the
Scala standard library of your choice into your Scala applications.

For information about creating a Managed Service for Apache Flink application that uses **Apache Beam**, see
[Use Apache Beam with Managed Service for Apache Flink
applications](how-creating-apps-beam.md "how-creating-apps-beam.md").

### Specify your application's Apache Flink

version

When using Managed Service for Apache Flink Runtime version 1.1.0 and later, you specify the version of
Apache Flink that your application uses when you compile your application. You
provide the version of Apache Flink with the `-Dflink.version` parameter.
For example, if you are using Apache Flink 1.19.1, provide the following:

```
mvn package -Dflink.version=1.19.1
```

For building applications with earlier versions of Apache Flink, see [Earlier versions](earlier.md "earlier.md").

## Create your Managed Service for Apache Flink application

After you've built your application code, you do the following to create your Managed Service for Apache Flink (Amazon MSF) application:

- **Upload your Application code**: Upload your application code to an Amazon S3 bucket.
  You specify the S3 bucket name and object name of your
  application code when you create your application. For a tutorial that shows how to upload
  your application code, see the [Tutorial: Get started using the DataStream API
  in Managed Service for Apache Flink](getting-started.md "getting-started.md") tutorial.
- **Create your Managed Service for Apache Flink application**: Use one of the following methods to create your Amazon MSF application:

###### Note

Amazon MSF encrypts your application by default using AWS owned keys. You can also create your new application using AWS KMS customer managed keys (CMKs) to create, own, and manage your keys yourself. For information about CMKs, see [Key management in Amazon Managed Service for Apache Flink](key-management-flink.md "key-management-flink.md").

    + **Create your Amazon MSF application using the AWS console:** You can create and configure
     your application using the AWS console.


    When you create your application using the console, your
     application's dependent resources (such as CloudWatch Logs streams, IAM roles, and IAM policies) are created for you.


    When you create your application using the console, you specify what
     version of Apache Flink your application uses by selecting it from the
     pull-down on the **Managed Service for Apache Flink - Create
     application** page.


    For a tutorial about how to use the console to create an application, see the [Tutorial: Get started using the DataStream API
     in Managed Service for Apache Flink](getting-started.md "getting-started.md") tutorial.
    + **Create your Amazon MSF application using the AWS CLI:** You can create and configure your application
     using the AWS CLI.

    When you create your application using the CLI, you must also create your
     application's dependent resources (such as CloudWatch Logs streams, IAM roles, and IAM policies) manually.


    When you create your application using the CLI, you specify what version of Apache Flink your application uses
     by using the `RuntimeEnvironment` parameter of the `CreateApplication` action.

###### Note

You can change the `RuntimeEnvironment` of an existing application. To learn how,
see [Use in-place version upgrades for Apache
Flink](how-in-place-version-upgrades.md "how-in-place-version-upgrades.md").

## Use customer managed keys

In Amazon MSF, customer managed keys (CMKs) is a feature using which you can encrypt your application's data with a key that you create, own, and manage on AWS Key Management Service (AWS KMS). For an Amazon MSF application, this means all data subject to a Flink [checkpoint](how-fault.md "how-fault.md") or [snapshot](how-snapshots.md "how-snapshots.md") are encrypted with a CMK you define for that application.

To use CMK with your application, you must first [create your new application](#how-creating-apps-creating "#how-creating-apps-creating"), and then apply a CMK. For more information about using CMKs, see [Key management in Amazon Managed Service for Apache Flink](key-management-flink.md "key-management-flink.md").

## Start your Managed Service for Apache Flink application

After you have built your application code, uploaded it to S3, and created your Managed Service for Apache Flink application, you then start your application. Starting a Managed Service for Apache Flink application typically takes several minutes.

Use one of the following methods to start your application:

- **Start your Managed Service for Apache Flink application using the AWS console:** You can run your application by choosing **Run** on your application's page in the AWS console.
- **Start your Managed Service for Apache Flink application using the AWS API:** You can run your application using the [StartApplication](../apiv2/API_StartApplication.md "../apiv2/API_StartApplication.md") action.

## Verify your Managed Service for Apache Flink application

You can verify that your application is working in the following ways:

- **Using CloudWatch Logs:** You can use CloudWatch Logs and CloudWatch Logs Insights to verify that your application is running properly.
  For information about using CloudWatch Logs with your Managed Service for Apache Flink application, see [Logging and monitoring in Amazon Managed Service for Apache Flink](monitoring-overview.md "monitoring-overview.md").
- **Using CloudWatch Metrics:** You can use CloudWatch Metrics to monitor your application's activity, or activity in the
  resources your application uses for input or output (such as Kinesis streams, Firehose streams, or Amazon S3 buckets.) For more information about CloudWatch metrics, see
  [Working with Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") in the Amazon CloudWatch User Guide.
- **Monitoring Output Locations:** If your application writes output to a location (such as an Amazon S3 bucket or database), you can monitor that location for written data.
