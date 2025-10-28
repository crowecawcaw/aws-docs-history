# Connect Athena to a Hive

metastore using an existing IAM execution role

To connect your external Hive metastore to Athena with a Lambda function that uses an
existing IAM role, you can use Athena's reference implementation of the Athena connector for
external Hive metastore.

The three major steps are as follows:

1. [Clone and build](#connect-data-source-hive-existing-iam-role-clone-and-build-the-lambda-function "#connect-data-source-hive-existing-iam-role-clone-and-build-the-lambda-function") – Clone the Athena reference
   implementation and build the JAR file that contains the Lambda function code.
2. [AWS Lambda console](#connect-data-source-hive-existing-iam-role-aws-lambda-console "#connect-data-source-hive-existing-iam-role-aws-lambda-console") – In the AWS Lambda console, create
   a Lambda function, assign it an existing IAM execution role, and upload the
   function code that you generated.
3. [Amazon Athena
   console](connect-data-source-hive-existing-lambda.md "connect-data-source-hive-existing-lambda.md") – In the Amazon Athena console, create a data
   source name that you can use to refer to your external Hive metastore in your Athena
   queries.
   If you already have permissions to create a custom IAM role, you can use a simpler
   workflow that uses the Athena console and the AWS Serverless Application Repository to create and configure a Lambda function.
   For more information, see [Connect Athena to an Apache Hive metastore](connect-to-data-source-hive-connecting-athena-to-an-apache-hive-metastore.md "connect-to-data-source-hive-connecting-athena-to-an-apache-hive-metastore.md").

## Prerequisites

- Git must be installed on your system.
- You must have [Apache Maven](https://maven.apache.org/ "https://maven.apache.org/")
  installed.
- You have an IAM execution role that you can assign to the Lambda function.
  For more information, see [Allow Lambda function access to external
  Hive metastores](hive-metastore-iam-access-lambda.md "hive-metastore-iam-access-lambda.md").

## Clone and build the Lambda function

The function code for the Athena reference implementation is a Maven project located on
GitHub at [awslabs/aws-athena-hive-metastore](https://github.com/awslabs/aws-athena-hive-metastore "https://github.com/awslabs/aws-athena-hive-metastore"). For detailed information about the
project, see the corresponding README file on GitHub or the [Modify the Athena external Hive
metastore connector](datastores-hive-reference-implementation.md "datastores-hive-reference-implementation.md") topic in this
documentation.

###### To clone and build the Lambda function code

1. Enter the following command to clone the Athena reference
   implementation:

```
git clone https://github.com/awslabs/aws-athena-hive-metastore
```

2. Run the following command to build the `.jar` file for the
   Lambda function:

```
mvn clean install
```

After the project builds successfully, the following `.jar`
file is created in the target folder of your project:

`hms-lambda-func-1.0-SNAPSHOT-withdep.jar`

In the next section, you use the AWS Lambda console to upload this file to your
Amazon Web Services account.

## Create

and configure the Lambda function in the AWS Lambda console

In this section, you use the AWS Lambda console to create a function that uses an
existing IAM execution role. After you configure a VPC for the function, you upload
the function code and configure the environment variables for the function.

### Create the Lambda function

In this step, you create a function in the AWS Lambda console that uses an existing
IAM role.

###### To create a Lambda function that uses an existing IAM role

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. In the navigation pane, choose **Functions**.
3. Choose **Create function**.
4. Choose **Author from scratch**.
5. For **Function name**, enter the name of your Lambda
   function (for example, `EHMSBasedLambda`).
6. For **Runtime**, choose **Java
   8**.
7. Under **Permissions**, expand **Change default
   execution role**.
8. For **Execution role**, choose **Use an existing
   role**.
9. For **Existing role**, choose the IAM execution role
   that your Lambda function will use for Athena (this example uses a role called
   `AthenaLambdaExecutionRole`).
10. Expand **Advanced settings**.
11. Select **Enable Network**.
12. For **VPC**, choose the VPC that your function will have
    access to.
13. For **Subnets**, choose the VPC subnets for Lambda to
    use.
14. For **Security groups**, choose the VPC security groups
    for Lambda to use.
15. Choose **Create function**. The AWS Lambda console and
    opens the configuration page for your function and begins creating your
    function.

### Upload the code and configure the Lambda function

When the console informs you that your function has been successfully created, you
are ready to upload the function code and configure its environment
variables.

###### To upload your Lambda function code and configure its environment

variables

1. In the Lambda console, make sure that you are on the
   **Code** tab of the page of the function that you
   specfied.
2. For **Code source**, choose **Upload
   from**, and then choose **.zip or .jar
   file**.
3. Upload the `hms-lambda-func-1.0-SNAPSHOT-withdep.jar`
   file that you generated previously.
4. On your Lambda function page, choose the **Configuration**
   tab.
5. From the pane on the left, choose **Environment
   variables**.
6. In the **Environment variables** section, choose
   **Edit**.

![Choose Edit to edit the environment variables for the Lambda function.](images/connect-data-source-hive-existing-iam-role-5.png) 7. On the **Edit environment variables** page, use the
**Add environment variable** option to add the
following environment variable keys and values:

    * HMS\_URIS – Use the following
     syntax to enter the URI of your Hive metastore host that uses the
     Thrift protocol at port 9083.



    ```
    thrift://`<host_name>`:9083
    ```
    * SPILL\_LOCATION – Specify an
     Amazon S3 location in your Amazon Web Services account to hold spillover metadata
     if the Lambda function response size exceeds 4 MB.



    ![Specifying values for the Lambda function environment variables.](images/connect-data-source-hive-existing-iam-role-6.png)

8. Choose **Save**.

At this point, you are ready to configure Athena to use your Lambda function to
connect to your Hive metastore. For steps, see [Configure Athena to use a deployed
Hive metastore connector](connect-data-source-hive-existing-lambda.md "connect-data-source-hive-existing-lambda.md").
