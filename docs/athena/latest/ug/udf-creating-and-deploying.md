# Create and deploy a UDF using Lambda

To create a custom UDF, you create a new Java class by extending the
`UserDefinedFunctionHandler` class. The source code for the [UserDefinedFunctionHandler.java](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-federation-sdk/src/main/java/com/amazonaws/athena/connector/lambda/handlers/UserDefinedFunctionHandler.java "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-federation-sdk/src/main/java/com/amazonaws/athena/connector/lambda/handlers/UserDefinedFunctionHandler.java") in the SDK is available on GitHub in the
awslabs/aws-athena-query-federation/athena-federation-sdk [repository](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-federation-sdk "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-federation-sdk"), along with [example UDF implementations](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-udfs "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-udfs") that you can examine and modify to create a
custom UDF.

The steps in this section demonstrate writing and building a custom UDF Jar file using
[Apache Maven](https://maven.apache.org/index.html "https://maven.apache.org/index.html") from the
command line and a deploy.

Perform the following steps to create a custom UDF for Athena using Maven

1. [Clone the SDK and prepare your development environment](#udf-create-install-sdk-prep-environment "#udf-create-install-sdk-prep-environment")
2. [Create your Maven project](#create-maven-project "#create-maven-project")
3. [Add dependencies and plugins to your Maven project](#udf-add-maven-dependencies "#udf-add-maven-dependencies")
4. [Write Java code for the UDFs](#udf-write-java "#udf-write-java")
5. [Build the JAR file](#udf-create-package-jar "#udf-create-package-jar")
6. [Deploy the JAR to AWS Lambda](#udf-create-deploy "#udf-create-deploy")

## Clone the SDK and prepare your development environment

Before you begin, make sure that git is installed on your system using `sudo
 yum install git -y`.

###### To install the AWS query federation SDK

- Enter the following at the command line to clone the SDK repository. This
  repository includes the SDK, examples and a suite of data source connectors.
  For more information about data source connectors, see [Use Amazon Athena Federated Query](federated-queries.md "federated-queries.md").

```
git clone https://github.com/awslabs/aws-athena-query-federation.git
```

###### To install prerequisites for this procedure

If you are working on a development machine that already has Apache Maven, the
AWS CLI, and the AWS Serverless Application Model build tool installed, you can skip this step.

1. From the root of the `aws-athena-query-federation` directory
   that you created when you cloned, run the [prepare_dev_env.sh](https://github.com/awslabs/aws-athena-query-federation/blob/master/tools/prepare_dev_env.sh "https://github.com/awslabs/aws-athena-query-federation/blob/master/tools/prepare_dev_env.sh") script that prepares your development
   environment.
2. Update your shell to source new variables created by the installation
   process or restart your terminal session.

```
source ~/.profile
```

###### Important

If you skip this step, you will get errors later about the AWS CLI or
AWS SAM build tool not being able to publish your Lambda function.

## Create your Maven project

Run the following command to create your Maven project. Replace
`groupId` with the unique ID of your organization, and
replace `my-athena-udf` with the name of your application
For more information, see [How do I make my first Maven project?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_make_my_first_Maven_project "https://maven.apache.org/guides/getting-started/index.html#How_do_I_make_my_first_Maven_project") in Apache Maven
documentation.

```
mvn -B archetype:generate \
-DarchetypeGroupId=org.apache.maven.archetypes \
-DgroupId=`groupId` \
-DartifactId=`my-athena-udfs`
```

## Add dependencies and plugins to your Maven project

Add the following configurations to your Maven project `pom.xml` file.
For an example, see the [pom.xml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-udfs/pom.xml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-udfs/pom.xml") file in GitHub.

```
<properties>
    <aws-athena-federation-sdk.version>2022.47.1</aws-athena-federation-sdk.version>
</properties>

<dependencies>
    <dependency>
        <groupId>com.amazonaws</groupId>
        <artifactId>aws-athena-federation-sdk</artifactId>
        <version>${aws-athena-federation-sdk.version}</version>
    </dependency>
</dependencies>

<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-shade-plugin</artifactId>
            <version>3.2.1</version>
            <configuration>
                <createDependencyReducedPom>false</createDependencyReducedPom>
                <filters>
                    <filter>
                        <artifact>*:*</artifact>
                        <excludes>
                            <exclude>META-INF/*.SF</exclude>
                            <exclude>META-INF/*.DSA</exclude>
                            <exclude>META-INF/*.RSA</exclude>
                        </excludes>
                    </filter>
                </filters>
            </configuration>
            <executions>
                <execution>
                    <phase>package</phase>
                    <goals>
                        <goal>shade</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>

```

## Write Java code for the UDFs

Create a new class by extending [UserDefinedFunctionHandler.java](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-federation-sdk/src/main/java/com/amazonaws/athena/connector/lambda/handlers/UserDefinedFunctionHandler.java "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-federation-sdk/src/main/java/com/amazonaws/athena/connector/lambda/handlers/UserDefinedFunctionHandler.java"). Write your UDFs inside the
class.

In the following example, two Java methods for UDFs, `compress()` and
`decompress()`, are created inside the class
`MyUserDefinedFunctions`.

```
*package *com.mycompany.athena.udfs;

public class MyUserDefinedFunctions
        extends UserDefinedFunctionHandler
{
    private static final String SOURCE_TYPE = "MyCompany";

    public MyUserDefinedFunctions()
    {
        super(SOURCE_TYPE);
    }

    /**
     * Compresses a valid UTF-8 String using the zlib compression library.
     * Encodes bytes with Base64 encoding scheme.
     *
     * @param input the String to be compressed
     * @return the compressed String
     */
    public String compress(String input)
    {
        byte[] inputBytes = input.getBytes(StandardCharsets.UTF_8);

        // create compressor
        Deflater compressor = new Deflater();
        compressor.setInput(inputBytes);
        compressor.finish();

        // compress bytes to output stream
        byte[] buffer = new byte[4096];
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(inputBytes.length);
        while (!compressor.finished()) {
            int bytes = compressor.deflate(buffer);
            byteArrayOutputStream.write(buffer, 0, bytes);
        }

        try {
            byteArrayOutputStream.close();
        }
        catch (IOException e) {
            throw new RuntimeException("Failed to close ByteArrayOutputStream", e);
        }

        // return encoded string
        byte[] compressedBytes = byteArrayOutputStream.toByteArray();
        return Base64.getEncoder().encodeToString(compressedBytes);
    }

    /**
     * Decompresses a valid String that has been compressed using the zlib compression library.
     * Decodes bytes with Base64 decoding scheme.
     *
     * @param input the String to be decompressed
     * @return the decompressed String
     */
    public String decompress(String input)
    {
        byte[] inputBytes = Base64.getDecoder().decode((input));

        // create decompressor
        Inflater decompressor = new Inflater();
        decompressor.setInput(inputBytes, 0, inputBytes.length);

        // decompress bytes to output stream
        byte[] buffer = new byte[4096];
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(inputBytes.length);
        try {
            while (!decompressor.finished()) {
                int bytes = decompressor.inflate(buffer);
                if (bytes == 0 && decompressor.needsInput()) {
                    throw new DataFormatException("Input is truncated");
                }
                byteArrayOutputStream.write(buffer, 0, bytes);
            }
        }
        catch (DataFormatException e) {
            throw new RuntimeException("Failed to decompress string", e);
        }

        try {
            byteArrayOutputStream.close();
        }
        catch (IOException e) {
            throw new RuntimeException("Failed to close ByteArrayOutputStream", e);
        }

        // return decoded string
        byte[] decompressedBytes = byteArrayOutputStream.toByteArray();
        return new String(decompressedBytes, StandardCharsets.UTF_8);
    }
}
```

## Build the JAR file

Run `mvn clean install` to build your project. After it successfully
builds, a JAR file is created in the `target` folder of your project
named
``artifactId`-`version`.jar`,
 where `artifactId`is the name you provided in the Maven
 project, for example,`my-athena-udfs`.

## Deploy the JAR to AWS Lambda

You have two options to deploy your code to Lambda:

- Deploy Using AWS Serverless Application Repository (Recommended)
- Create a Lambda Function from the JAR file

### Option 1: Deploy to the AWS Serverless Application Repository

When you deploy your JAR file to the AWS Serverless Application Repository, you create an AWS SAM template YAML
file that represents the architecture of your application. You then specify this
YAML file and an Amazon S3 bucket where artifacts for your application are uploaded
and made available to the AWS Serverless Application Repository. The procedure below uses the [publish.sh](https://github.com/awslabs/aws-athena-query-federation/blob/master/tools/publish.sh "https://github.com/awslabs/aws-athena-query-federation/blob/master/tools/publish.sh") script located in the
`athena-query-federation/tools` directory of the Athena Query
Federation SDK that you cloned earlier.

For more information and requirements, see [Publishing applications](../../../serverlessrepo/latest/devguide/serverlessrepo-publishing-applications.md "../../../serverlessrepo/latest/devguide/serverlessrepo-publishing-applications.md") in the
_AWS Serverless Application Repository Developer Guide_, [AWS SAM template concepts](../../../serverless-application-model/latest/developerguide/serverless-sam-template-basics.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-basics.md") in the
_AWS Serverless Application Model Developer Guide_, and [Publishing serverless applications using the AWS SAM CLI](../../../serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.md").

The following example demonstrates parameters in a YAML file. Add similar
parameters to your YAML file and save it in your project directory. See [athena-udf.yaml](https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-udfs/athena-udfs.yaml "https://github.com/awslabs/aws-athena-query-federation/blob/master/athena-udfs/athena-udfs.yaml") in GitHub for a full example.

```
Transform: 'AWS::Serverless-2016-10-31'
Metadata:
  'AWS::ServerlessRepo::Application':
    Name: `MyApplicationName`
    Description: '`The description I write for my application`'
    Author: '`Author Name`'
    Labels:
      - athena-federation
    SemanticVersion: 1.0.0
Parameters:
  LambdaFunctionName:
    Description: '`The name of the Lambda function that will contain your UDFs.`'
    Type: String
  LambdaTimeout:
    Description: 'Maximum Lambda invocation runtime in seconds. (min 1 - 900 max)'
    Default: 900
    Type: Number
  LambdaMemory:
    Description: 'Lambda memory in MB (min 128 - 3008 max).'
    Default: 3008
    Type: Number
Resources:
  ConnectorConfig:
    Type: 'AWS::Serverless::Function'
    Properties:
      FunctionName: !Ref LambdaFunctionName
      Handler: "`full.path.to.your.handler. For example, com.amazonaws.athena.connectors.udfs.MyUDFHandler`"
      CodeUri: "`Relative path to your JAR file. For example, ./target/athena-udfs-1.0.jar`"
      Description: "`My description of the UDFs that this Lambda function enables.`"
      Runtime: java8
      Timeout: !Ref LambdaTimeout
      MemorySize: !Ref LambdaMemory
```

Copy the `publish.sh` script to the project directory where you
saved your YAML file, and run the following command:

```
./publish.sh `MyS3Location` `MyYamlFile`
```

For example, if your bucket location is
`s3://amzn-s3-demo-bucket/mysarapps/athenaudf` and your YAML file
was saved as `my-athena-udfs.yaml`:

```
./publish.sh amzn-s3-demo-bucket/mysarapps/athenaudf my-athena-udfs

```

###### To create a Lambda function

1. Open the Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/"), choose **Create
   function**, and then choose **Browse serverless app
   repository**
2. Choose **Private applications**, find your
   application in the list, or search for it using key words, and select
   it.
3. Review and provide application details, and then choose
   **Deploy.**

You can now use the method names defined in your Lambda function JAR
file as UDFs in Athena.

### Option 2: Create a Lambda function directly

You can also create a Lambda function directly using the console or AWS CLI. The
following example demonstrates using the Lambda `create-function` CLI
command.

```
aws lambda create-function \
 --function-name `MyLambdaFunctionName` \
 --runtime java8 \
 --role arn:aws:iam::`1234567890123:role/my_lambda_role` \
 --handler `com.mycompany.athena.udfs.MyUserDefinedFunctions` \
 --timeout 900 \
 --zip-file fileb://`./target/my-athena-udfs-1.0-SNAPSHOT.jar`
```
