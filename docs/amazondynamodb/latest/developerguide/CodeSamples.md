# .NET code examples

###### Topics

- [.NET: Setting your AWS
  credentials](#CodeSamples.DotNet.Credentials "#CodeSamples.DotNet.Credentials")
- [.NET: Setting the AWS
  Region and endpoint](#CodeSamples.DotNet.RegionAndEndpoint "#CodeSamples.DotNet.RegionAndEndpoint")
  This guide contains .NET code snippets and ready-to-run programs. You can find these
  code examples in the following sections:

- [Working with items and attributes in DynamoDB](WorkingWithItems.md "WorkingWithItems.md")
- [Working with tables and data in DynamoDB](WorkingWithTables.md "WorkingWithTables.md")
- [Querying tables in DynamoDB](Query.md "Query.md")
- [Scanning tables in DynamoDB](Scan.md "Scan.md")
- [Improving data access with secondary indexes in
  DynamoDB](SecondaryIndexes.md "SecondaryIndexes.md")
- [Working with the .NET document model in DynamoDB](DotNetSDKMidLevel.md "DotNetSDKMidLevel.md")
- [Working with the .NET object persistence model and
  DynamoDB](DotNetSDKHighLevel.md "DotNetSDKHighLevel.md")
- [Change data capture for DynamoDB Streams](Streams.md "Streams.md")
  You can get started quickly by using the AWS SDK for .NET with the Toolkit for Visual Studio.

###### To run the .NET code examples (using Visual Studio)

1. Download and install [Microsoft
   Visual Studio](https://www.visualstudio.com "https://www.visualstudio.com").
2. Download and install the [Toolkit for Visual Studio](https://aws.amazon.com/visualstudio/ "https://aws.amazon.com/visualstudio/").
3. Start Visual Studio. Choose **File**,
   **New**, **Project**.
4. In **New Project**, choose **AWS Empty
   Project**, and then choose **OK**.
5. In **AWS Access Credentials**, choose **Use
   existing profile**, choose your credentials profile from the list,
   and then choose **OK**.

If this is your first time using Toolkit for Visual Studio, choose **Use a new
profile** to set up your AWS credentials. 6. In your Visual Studio project, choose the tab for your program's source code
(`Program.cs`). Copy the code example from the documentation page
into the Visual Studio editor, replacing any other code that you see in the
editor. 7. If you see error messages of the form **`The type or namespace
 name...could not be found`**, you need to install the AWS SDK
assembly for DynamoDB as follows:

    1. In Solution Explorer, open the context (right-click) menu for your
     project, and then choose **Manage NuGet
     Packages**.
    2. In NuGet Package Manager, choose **Browse**.
    3. In the search box, enter `AWSSDK.DynamoDBv2`, and
     wait for the search to complete.
    4. Choose **AWSSDK.DynamoDBv2**, and then choose
     **Install**.
    5. When the installation is complete, choose the
     **Program.cs** tab to return to your
     program.

8. To run the code, choose **Start** in the Visual Studio
   toolbar.
   The SDK for .NET provides thread-safe clients for working with DynamoDB. As a best practice,
   your applications should create one client and reuse the client between threads.

For more information, see [AWS SDK for
.NET](https://aws.amazon.com/sdk-for-net "https://aws.amazon.com/sdk-for-net").

###### Note

The code examples in this guide are intended for use with the latest version of
the AWS SDK for .NET.

## .NET: Setting your AWS

credentials

The SDK for .NET requires that you provide AWS credentials to your application at
runtime. The code examples in this guide assume that you are using the SDK Store to
manage your AWS credentials file, as described in [Using the SDK
store](../../../sdk-for-net/v3/developer-guide/net-dg-config-creds.md#sdk-store "../../../sdk-for-net/v3/developer-guide/net-dg-config-creds.md#sdk-store") in the _AWS SDK for .NET Developer Guide_.

The Toolkit for Visual Studio supports multiple sets of credentials from any number of accounts. Each
set is referred to as a _profile_. Visual Studio adds entries to
the project's `App.config` file so that your application can find
the AWS credentials at runtime.

The following example shows the default `App.config` file that
is generated when you create a new project using Toolkit for Visual Studio.

```
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
    <appSettings>
    <add key="AWSProfileName" value="default"/>
    <add key="AWSRegion" value="us-west-2" />
 </appSettings>
</configuration>
```

At runtime, the program uses the `default` set of AWS credentials, as
specified by the `AWSProfileName` entry. The AWS credentials themselves
are kept in the SDK Store in encrypted form. The Toolkit for Visual Studio provides a graphical user
interface for managing your credentials, all from within Visual Studio. For more
information, see [Specifying
credentials](../../../AWSToolkitVS/latest/UserGuide/tkv_setup.md#creds "../../../AWSToolkitVS/latest/UserGuide/tkv_setup.md#creds") in the _AWS Toolkit for Visual Studio User Guide_.

###### Note

By default, the code examples access DynamoDB in the US West (Oregon) Region.
You can change the Region by modifying the `AWSRegion` entry in the
App.config file. You can set `AWSRegion` to any Region where DynamoDB is
available. For a complete list, see [AWS regions and endpoints](../../../general/latest/gr/rande.md#ddb_region "../../../general/latest/gr/rande.md#ddb_region") in the
_Amazon Web Services General Reference_.

## .NET: Setting the AWS

Region and endpoint

By default, the code examples access DynamoDB in the US West (Oregon) Region. You
can change the Region by modifying the `AWSRegion` entry in the
`App.config` file. Or, you can change the Region by modifying
the `AmazonDynamoDBClient` properties.

The following code example instantiates a new `AmazonDynamoDBClient`.
The client is modified so that the code runs against DynamoDB in a different
Region.

```
AmazonDynamoDBConfig clientConfig = new AmazonDynamoDBConfig();
// This client will access the US East 1 region.
clientConfig.RegionEndpoint = RegionEndpoint.USEast1;
AmazonDynamoDBClient client = new AmazonDynamoDBClient(clientConfig);
```

For a complete list of Regions, see [AWS regions and endpoints](../../../general/latest/gr/rande.md#ddb_region "../../../general/latest/gr/rande.md#ddb_region") in the
_Amazon Web Services General Reference_.

If you want to run the code examples using DynamoDB locally on your computer, set the
endpoint as follows.

```
AmazonDynamoDBConfig clientConfig = new AmazonDynamoDBConfig();
// Set the endpoint URL
clientConfig.ServiceURL = "http://localhost:8000";
AmazonDynamoDBClient client = new AmazonDynamoDBClient(clientConfig);
```
