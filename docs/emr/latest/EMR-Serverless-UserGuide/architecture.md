# Amazon EMR Serverless architecture options

The instruction set architecture of your Amazon EMR Serverless application determines the
type of processors that the application uses to run the job. Amazon EMR provides two architecture
options for your application: **x86_64** and
**arm64**. EMR Serverless automatically updates to the latest generation of
instances as they become available, so your applications can use the newer instances
without requiring additional effort from you.

###### Topics

- [Using x86_64 architecture](#x86 "#x86")
- [Using arm64 architecture (Graviton)](#arm64 "#arm64")
- [Launching new applications with Graviton support](#arm64-new "#arm64-new")
- [Configuring existing applications to use Graviton](#arm64-existing "#arm64-existing")
- [Considerations when using Graviton](#arm64-considerations "#arm64-considerations")

## Using x86_64 architecture

The **x86_64** architecture is also known as x86 64-bit or x64.
**x86_64** is the default option for EMR Serverless applications. This
architecture uses x86-based processors and is compatible with most third-party tools and
libraries.

Most applications are compatible with the x86 hardware platform and can run successfully
on the default **x86_64** architecture. However, if your application is
compatible with 64-bit ARM, then switch to **arm64** to use Graviton
processors for improved performance, compute power, and memory. It costs less to run
instances on arm64 architecture than when you run instances of equal size on x86
architecture.

## Using arm64 architecture (Graviton)

AWS Graviton processors are custom designed by AWS with 64-bit ARM Neoverse cores and leverage the
arm64 architecture (also known as Arch64 or 64-bit ARM). The AWS Graviton line of processors
available on EMR Serverless include Graviton3 and Graviton2 processors. These processors
deliver superior price-performance for Spark and Hive workloads compared to equivalent workloads
that run on the x86_64 architecture. EMR Serverless automatically uses the latest generation of processors when available without any effort from
your side to upgrade to the latest generation of processors.

## Launching new applications with Graviton support

Use one of the following methods to launch an application that uses the
**arm64** architecture.

AWS CLI
To launch an application using Graviton processors from AWS CLI, specify
`ARM64` as the `architecture` parameter in the
`create-application` API. Provide the appropriate values for your
application in the other parameters.

```
aws emr-serverless create-application \
 --name my-graviton-app \
 --release-label emr-6.8.0 \
 --type "SPARK" \
 --architecture "ARM64" \
 --region `us-west-2`
```

EMR Studio
To launch an application using Graviton processors from EMR Studio, choose
**arm64** as the **Architecture** option when you
create or update an application.

## Configuring existing applications to use Graviton

You can configure your existing Amazon EMR Serverless applications to use the Graviton
(arm64) architecture with the SDK, AWS CLI, or EMR Studio.

###### To convert an existing application from x86 to arm64

1. Confirm that you are using the latest major version of the [AWS CLI/SDK](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-serverless/index.html#cli-aws-emr-serverless "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-serverless/index.html#cli-aws-emr-serverless") that supports the `architecture` parameter.
2. Confirm that there are no jobs running and then stop the application.

```
aws emr-serverless stop-application \
 --application-id `application-id` \
 --region `us-west-2`
```

3. To update the application to use Graviton, specify `ARM64` for the
   `architecture` parameter in the `update-application` API.

```
aws emr-serverless update-application \
 --application-id `application-id` \
 --architecture 'ARM64' \
 --region `us-west-2`
```

4. To verify that the CPU architecture of the application is now ARM64, use the
   `get-application` API.

```
aws emr-serverless get-application \
 --application-id `application-id` \
 --region `us-west-2`
```

5. When you're ready, restart the application.

```
aws emr-serverless start-application \
 --application-id `application-id` \
 --region `us-west-2`
```

## Considerations when using Graviton

Before you launch an EMR Serverless application using arm64 for Graviton support, confirm
the following.

### Library compatibility

When you select Graviton (arm64) as an architecture option, ensure that third-party
packages and libraries are compatible with the 64-bit ARM architecture. For information on
how to package Python libraries into a Python virtual environment that is compatible with
your selected architecture, refer to [Using Python libraries with
EMR Serverless](using-python-libraries.md "using-python-libraries.md").

To learn more, refer to
the [AWS Graviton
Getting Started](https://github.com/aws/aws-graviton-getting-started "https://github.com/aws/aws-graviton-getting-started") repository on GitHub. This repository contains essential
resources that can help you get started with the ARM-based Graviton.
