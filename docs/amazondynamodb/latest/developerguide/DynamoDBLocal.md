# Deploying DynamoDB locally on

your computer

###### Note

- DynamoDB local is available in three versions: v3.x (Current), v2.x
  (Legacy), and v1.x (Deprecated).
- DynamoDB v3.x is recommended for your local testing and development
  use.
- Migration from DynamoDB local V2.x to V3.x requires updating import
  statements from `com.amazonaws.services.dynamodbv2` to
  `software.amazon.dynamodb` and updating Maven
  dependencies for Maven users.
- If you're migrating an application that uses the SDK for Java v1.x to
  the SDK for Java 2.x, follow the steps for [AWS SDK for Java 2.x](../../../sdk-for-java/latest/developer-guide/migration.md "../../../sdk-for-java/latest/developer-guide/migration.md").
  Follow these steps to set up and run DynamoDB on your computer.

###### To set up DynamoDB on your computer

1. Download DynamoDB local for free from one of the following
   locations.

| Download Links                                                                                                                                               | Checksums                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [.tar.gz](https://d1ni2b6xgvw0s0.cloudfront.net/v2.x/dynamodb_local_latest.tar.gz "https://d1ni2b6xgvw0s0.cloudfront.net/v2.x/dynamodb_local_latest.tar.gz") | <br>[.zip](https://d1ni2b6xgvw0s0.cloudfront.net/v2.x/dynamodb_local_latest.zip "https://d1ni2b6xgvw0s0.cloudfront.net/v2.x/dynamodb_local_latest.zip") | [.tar.gz.sha256](https://d1ni2b6xgvw0s0.cloudfront.net/v2.x/dynamodb_local_latest.tar.gz.sha256 "https://d1ni2b6xgvw0s0.cloudfront.net/v2.x/dynamodb_local_latest.tar.gz.sha256") | <br>[.zip.sha256](https://d1ni2b6xgvw0s0.cloudfront.net/v2.x/dynamodb_local_latest.zip.sha256 "https://d1ni2b6xgvw0s0.cloudfront.net/v2.x/dynamodb_local_latest.zip.sha256") |

###### Important

To run DynamoDB v2.6.0 or greater on your computer, you must
have the Java Runtime Environment (JRE) version 17.x or newer.
The application doesn't run on earlier JRE versions. 2. After you download the archive, extract the contents and copy the
extracted directory to a location of your choice. 3. To start DynamoDB on your computer, open a command prompt window,
navigate to the directory where you extracted
`DynamoDBLocal.jar`, and enter the following command.

```
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
```

###### Note

If you're using Windows PowerShell, be sure to enclose the
parameter name or the entire name and value like this:

`java -D"java.library.path=./DynamoDBLocal_lib" -jar
 DynamoDBLocal.jar`

DynamoDB processes incoming requests until you stop it. To stop
DynamoDB, press Ctrl+C at the command prompt.

DynamoDB uses port 8000 by default. If port 8000 is unavailable,
this command throws an exception. For a complete list of DynamoDB
runtime options, including `-port`, enter this
command.

`java -Djava.library.path=./DynamoDBLocal_lib -jar
 DynamoDBLocal.jar -help` 4. Before you can access DynamoDB programmatically or through the
AWS Command Line Interface (AWS CLI), you must configure your credentials to enable
authorization for your applications. Downloadable DynamoDB requires any
credentials to work, as shown in the following example.

```
AWS Access Key ID: "fakeMyKeyId"
AWS Secret Access Key: "fakeSecretAccessKey"
Default Region Name: "fakeRegion"
```

You can use the `aws configure` command of the AWS CLI
to set up credentials. For more information, see [Using the AWS CLI](AccessingDynamoDB.md#Tools.CLI "AccessingDynamoDB.md#Tools.CLI"). 5. Start writing applications. To access DynamoDB running locally with
the AWS CLI, use the `--endpoint-url` parameter. For
example, use the following command to list DynamoDB tables.

```
aws dynamodb list-tables --endpoint-url http://localhost:8000
```

The downloadable version of Amazon DynamoDB is available as a Docker image. For
more information, see [dynamodb-local](https://hub.docker.com/r/amazon/dynamodb-local "https://hub.docker.com/r/amazon/dynamodb-local"). To see your current DynamoDB local version, enter
the following command:

```
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -version
```

For an example of using DynamoDB local as part of a REST application built
on the AWS Serverless Application Model (AWS SAM), see [SAM DynamoDB
application for managing orders](https://github.com/aws-samples/aws-sam-java-rest "https://github.com/aws-samples/aws-sam-java-rest"). This sample application
demonstrates how to use DynamoDB local for testing.

If you want to run a multi-container application that also uses the
DynamoDB local container, use Docker Compose to define and run all the services
in your application, including DynamoDB local.

###### To install and run DynamoDB local with Docker compose:

1. Download and install [Docker
   desktop](https://www.docker.com/products/docker-desktop "https://www.docker.com/products/docker-desktop").
2. Copy the following code to a file and save it as
   `docker-compose.yml`.

```

services:
 dynamodb-local:
   command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
   image: "amazon/dynamodb-local:latest"
   container_name: dynamodb-local
   ports:
     - "8000:8000"
   volumes:
     - "./docker/dynamodb:/home/dynamodblocal/data"
   working_dir: /home/dynamodblocal
```

If you want your application and DynamoDB local to be in separate
containers, use the following yaml file.

```
version: '3.8'
services:
 dynamodb-local:
   command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
   image: "amazon/dynamodb-local:latest"
   container_name: dynamodb-local
   ports:
     - "8000:8000"
   volumes:
     - "./docker/dynamodb:/home/dynamodblocal/data"
   working_dir: /home/dynamodblocal
 app-node:
   depends_on:
     - dynamodb-local
   image: amazon/aws-cli
   container_name: app-node
   ports:
    - "8080:8080"
   environment:
     AWS_ACCESS_KEY_ID: 'DUMMYIDEXAMPLE'
     AWS_SECRET_ACCESS_KEY: 'DUMMYEXAMPLEKEY'
   command:
     dynamodb describe-limits --endpoint-url http://dynamodb-local:8000 --region us-west-2
```

This docker-compose.yml script creates an `app-node`
container and a `dynamodb-local` container. The script
runs a command in the `app-node` container that uses the
AWS CLI to connect to the `dynamodb-local` container and
describes the account and table limits.

To use with your own application image, replace the
`image` value in the example below with that of your
application.

```
version: '3.8'
services:
 dynamodb-local:
   command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
   image: "amazon/dynamodb-local:latest"
   container_name: dynamodb-local
   ports:
     - "8000:8000"
   volumes:
     - "./docker/dynamodb:/home/dynamodblocal/data"
   working_dir: /home/dynamodblocal
 app-node:
   image: `location-of-your-dynamodb-demo-app:latest`
   container_name: app-node
   ports:
     - "8080:8080"
   depends_on:
     - "dynamodb-local"
   links:
     - "dynamodb-local"
   environment:
     AWS_ACCESS_KEY_ID: 'DUMMYIDEXAMPLE'
     AWS_SECRET_ACCESS_KEY: 'DUMMYEXAMPLEKEY'
     REGION: 'eu-west-1'
```

###### Note

The YAML scripts require that you specify an AWS access key
and an AWS secret key, but they are not required to be valid
AWS keys for you to access DynamoDB local. 3. Run the following command-line command:

```
docker-compose up
```

###### Note

If you're migrating an application that uses the SDK for Java v1.x to
the SDK for Java 2.x, follow the steps for [AWS SDK for Java 2.x](../../../sdk-for-java/latest/developer-guide/migration.md "../../../sdk-for-java/latest/developer-guide/migration.md").

Follow these steps to use Amazon DynamoDB in your application as a dependency.

###### To deploy DynamoDB as an Apache Maven repository

1. Download and install Apache Maven. For more information, see
   [Downloading
   Apache Maven](https://maven.apache.org/download.cgi "https://maven.apache.org/download.cgi") and [Installing Apache
   Maven](https://maven.apache.org/install.html "https://maven.apache.org/install.html").
2. Add the DynamoDB Maven repository to your application's Project
   Object Model (POM) file.

```
<!--Dependency:-->
<dependencies>
   <dependency>
      <groupId>com.amazonaws</groupId>
      <artifactId>DynamoDBLocal</artifactId>
      <version>3.1.0</version>
   </dependency>
</dependencies>
```

Example template for use with Spring Boot 3 and/or Spring
Framework 6:

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>

<groupId>org.example</groupId>
<artifactId>SpringMavenDynamoDB</artifactId>
<version>1.0-SNAPSHOT</version>

<properties>
   <spring-boot.version>3.0.1</spring-boot.version>
   <maven.compiler.source>17</maven.compiler.source>
   <maven.compiler.target>17</maven.compiler.target>
   <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>

   <parent>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-parent</artifactId>
       <version>3.0.1</version>
   </parent>

<dependencies>
   <dependency>
       <groupId>com.amazonaws</groupId>
       <artifactId>DynamoDBLocal</artifactId>
       <version>3.1.0</version>
   </dependency>
   <!-- Spring Boot -->
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter</artifactId>
       <version>${spring-boot.version}</version>
   </dependency>
   <!-- Spring Web -->
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-web</artifactId>
       <version>${spring-boot.version}</version>
   </dependency>
   <!-- Spring Data JPA -->
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-data-jpa</artifactId>
       <version>${spring-boot.version}</version>
   </dependency>
   <!-- Other Spring dependencies -->
   <!-- Replace the version numbers with the desired version -->
   <dependency>
       <groupId>org.springframework</groupId>
       <artifactId>spring-context</artifactId>
       <version>6.0.0</version>
   </dependency>
   <dependency>
       <groupId>org.springframework</groupId>
       <artifactId>spring-core</artifactId>
       <version>6.0.0</version>
   </dependency>
   <!-- Add other Spring dependencies as needed -->
   <!-- Add any other dependencies your project requires -->
</dependencies>
</project>
```

###### Note

You can also use the [Maven central repository](https://mvnrepository.com/artifact/com.amazonaws/DynamoDBLocal?repo=dynamodb-local-release "https://mvnrepository.com/artifact/com.amazonaws/DynamoDBLocal?repo=dynamodb-local-release") URL.
AWS CloudShell is a browser-based, pre-authenticated shell that you can launch
directly from the AWS Management Console. You can navigate to AWS CloudShell from the AWS Management Console
a few different ways. For more information, see [Getting started with AWS CloudShell](../../../cloudshell/latest/userguide/getting-started.md "../../../cloudshell/latest/userguide/getting-started.md").

Follow these steps to run DynamoDB local in your AWS CloudShell anywhere in the AWS Management Console.

###### To run DynamoDB local in your AWS CloudShell in the AWS Management Console

1. Launch AWS CloudShell from the console interface, choose an available AWS Region, and
   switch to your preferred shell, such as Bash, PowerShell, or Z shell.
2. To choose an AWS Region, go to the **Select a
   Region** menu and select a [supported AWS Region](../../../cloudshell/latest/userguide/supported-aws-regions.md "../../../cloudshell/latest/userguide/supported-aws-regions.md"). (Available Regions are
   highlighted.)
3. From the AWS Management Console, launch AWS CloudShell by choosing one of
   the following options:
   1. On the navigation bar, choose the **AWS CloudShell** icon.
   2. In the **Search** box, enter the word CloudShell, and then choose **CloudShell**.
   3. In the **Recently visited** widget, choose **CloudShell**.
   4. From the console toolbar, choose **CloudShell**.

4. To run DynamoDB local in AWS CloudShell you can use the
   `dynamodb-local` alias. You can specify additional
   command line options for changing DynamoDB local settings. See [DynamoDB local usage notes](DynamoDBLocal.md "DynamoDBLocal.md") for available
   options.

###### Note

To run DynamoDB local in the background, run DynamoDB local
in AWS CloudShell using: `dynamodb-local &`. 5. To access DynamoDB running locally in AWS CloudShell with the AWS CLI, use the `--endpoint-url` parameter.
For example, use the following command to list DynamoDB tables:

`aws dynamodb list-tables --endpoint-url http://localhost:8000`
For an example of a sample project that showcases multiple approaches to set up
and use DynamoDB local, including downloading JAR files, running it as a Docker image,
and using it as a Maven dependency, see [DynamoDB
Local Sample Java Project](https://github.com/awslabs/amazon-dynamodb-local-samples/tree/main "https://github.com/awslabs/amazon-dynamodb-local-samples/tree/main").
