# Java code examples

###### Topics

- [Java: Setting your AWS
  credentials](#CodeSamples.Java.Credentials "#CodeSamples.Java.Credentials")
- [Java: Setting the AWS Region
  and endpoint](#CodeSamples.Java.RegionAndEndpoint "#CodeSamples.Java.RegionAndEndpoint")
  This Developer Guide contains Java code snippets and ready-to-run programs. You can
  find these code examples in the following sections:

- [Working with items and attributes in DynamoDB](WorkingWithItems.md "WorkingWithItems.md")
- [Working with tables and data in DynamoDB](WorkingWithTables.md "WorkingWithTables.md")
- [Querying tables in DynamoDB](Query.md "Query.md")
- [Scanning tables in DynamoDB](Scan.md "Scan.md")
- [Improving data access with secondary indexes in
  DynamoDB](SecondaryIndexes.md "SecondaryIndexes.md")
- [Java 1.x: DynamoDBMapper](DynamoDBMapper.md "DynamoDBMapper.md")
- [Change data capture for DynamoDB Streams](Streams.md "Streams.md")
  You can get started quickly by using Eclipse with the [AWS Toolkit for Eclipse](https://aws.amazon.com/eclipse/ "https://aws.amazon.com/eclipse/"). In addition to a full-featured IDE,
  you also get the AWS SDK for Java with automatic updates, and preconfigured templates for
  building AWS applications.

###### To run the Java code examples (using Eclipse)

1. Download and install the [Eclipse](http://www.eclipse.org "http://www.eclipse.org")
   IDE.
2. Download and install the [AWS Toolkit for Eclipse](https://aws.amazon.com/eclipse/ "https://aws.amazon.com/eclipse/").
3. Start Eclipse, and on the **Eclipse** menu, choose
   **File**, **New**, and then
   **Other**.
4. In **Select a wizard**, choose **AWS**,
   choose **AWS Java Project**, and then choose
   **Next**.
5. In **Create an AWS Java**, do the following:
   1. In **Project name**, enter a name for your
      project.
   2. In **Select Account**, choose your credentials
      profile from the list.

   If this is your first time using the [AWS Toolkit for Eclipse](https://aws.amazon.com/eclipse/ "https://aws.amazon.com/eclipse/"), choose
   **Configure AWS Accounts** to set up your AWS
   credentials.

6. Choose **Finish** to create the project.
7. From the **Eclipse** menu, choose **File**,
   **New**, and then **Class**.
8. In **Java Class**, enter a name for your class in
   **Name** (use the same name as the code example that you
   want to run), and then choose **Finish** to create the
   class.
9. Copy the code example from the documentation page into the Eclipse
   editor.
10. To run the code, choose **Run** on the Eclipse menu.
    The SDK for Java provides thread-safe clients for working with DynamoDB. As a best practice,
    your applications should create one client and reuse the client between threads.

For more information, see the [AWS SDK for Java](https://aws.amazon.com/sdk-for-java "https://aws.amazon.com/sdk-for-java").

###### Note

The code examples in this guide are intended for use with the latest version of
the AWS SDK for Java.

If you are using the AWS Toolkit for Eclipse, you can configure automatic updates for the SDK for Java.
To do this in Eclipse, go to **Preferences** and choose
**AWS Toolkit**, **AWS SDK for Java**,
**Download new SDKs automatically**.

## Java: Setting your AWS

credentials

The SDK for Java requires that you provide AWS credentials to your application at
runtime. The code examples in this guide assume that you are using an AWS
credentials file, as described in [Set
up your AWS credentials](../../../sdk-for-java/latest/developer-guide/set-up-creds.md "../../../sdk-for-java/latest/developer-guide/set-up-creds.md") in the
_AWS SDK for Java Developer Guide_.

The following is an example of an AWS credentials file named
`~/.aws/credentials`, where the tilde character (`~`)
represents your home directory.

```
[default]
aws_access_key_id = `AWS access key ID goes here`
aws_secret_access_key = `Secret key goes here`
```

## Java: Setting the AWS Region

and endpoint

By default, the code examples access DynamoDB in the US West (Oregon) Region. You
can change the Region by modifying the `AmazonDynamoDB`
properties.

The following code example instantiates a new `AmazonDynamoDB`.

```
import software.amazon.dynamodb.AmazonDynamoDBClientBuilder;
import com.amazonaws.regions.Regions;
...
// This client will default to US West (Oregon)
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
.withRegion(Regions.US_WEST_2)
.build();
```

You can use the `withRegion` method to run your code against DynamoDB in
any Region where it is available. For a complete list, see [AWS regions and endpoints](../../../general/latest/gr/rande.md#ddb_region "../../../general/latest/gr/rande.md#ddb_region") in the
_Amazon Web Services General Reference_.

If you want to run the code examples using DynamoDB locally on your computer, set the
endpoint as follows.

### AWS SDK V1

```
AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().withEndpointConfiguration(
new AwsClientBuilder.EndpointConfiguration("http://localhost:8000", "us-west-2"))
.build();
```

### AWS SDK V2

```
DynamoDbClient client = DynamoDbClient.builder()
    .endpointOverride(URI.create("http://localhost:8000"))
    // The region is meaningless for local DynamoDb but required for client builder validation
    .region(Region.US_EAST_1)
    .credentialsProvider(StaticCredentialsProvider.create(
    AwsBasicCredentials.create("dummy-key", "dummy-secret")))
    .build();
```
