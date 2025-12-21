# Connecting to Amazon Neptune databases using IAM authentication with Java and

SPARQL

This section shows how to connect to Neptune using either RDF4J or Apache Jena with
Signature Version 4 authentication.

###### Prerequisites

- Java 8 or higher.
- Apache Maven 3.3 or higher.

For information about installing these prerequisites on an EC2 instance running Amazon
Linux, see [Prerequisites for connecting Amazon Neptune databases using IAM authentication](iam-auth-connect-prerq.md "iam-auth-connect-prerq.md").

- IAM credentials to sign the requests. For more information, see [Using the Default Credential Provider Chain](../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default "../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default") in the
  _AWS SDK for Java Developer Guide_.

###### Note

If you are using temporary credentials, they expire after a specified interval,
_including the session token_.

You must update your session token when you request new credentials. For more
information, see [Using Temporary Security Credentials to Request Access to AWS Resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the
_IAM User Guide_.

- Set the `SERVICE_REGION` variable to one of the following, indicating the
  Region of your Neptune DB instance:
  - US East (N. Virginia):   `us-east-1`
  - US East (Ohio):   `us-east-2`
  - US West (N. California):   `us-west-1`
  - US West (Oregon):   `us-west-2`
  - Canada (Central):   `ca-central-1`
  - Canada West (Calgary):   `ca-west-1`
  - South America (São Paulo):   `sa-east-1`
  - Europe (Stockholm):   `eu-north-1`
  - Europe (Spain):   `eu-south-2`
  - Europe (Ireland):   `eu-west-1`
  - Europe (London):   `eu-west-2`
  - Europe (Paris):   `eu-west-3`
  - Europe (Frankfurt):   `eu-central-1`
  - Europe (Zurich):   `eu-central-2`
  - Middle East (Bahrain):   `me-south-1`
  - Middle East (UAE):   `me-central-1`
  - Israel (Tel Aviv):   `il-central-1`
  - Africa (Cape Town):   `af-south-1`
  - Asia Pacific (Hong Kong):   `ap-east-1`
  - Asia Pacific (Tokyo):   `ap-northeast-1`
  - Asia Pacific (Seoul):   `ap-northeast-2`
  - Asia Pacific (Osaka):   `ap-northeast-3`
  - Asia Pacific (Singapore):   `ap-southeast-1`
  - Asia Pacific (Sydney):   `ap-southeast-2`
  - Asia Pacific (Jakarta):   `ap-southeast-3`
  - Asia Pacific (Melbourne):   `ap-southeast-4`
  - Asia Pacific (Malaysia):   `ap-southeast-5`
  - Asia Pacific (Mumbai):   `ap-south-1`
  - China (Beijing):   `cn-north-1`
  - China (Ningxia):   `cn-northwest-1`
  - AWS GovCloud (US-West):   `us-gov-west-1`
  - AWS GovCloud (US-East):   `us-gov-east-1`

###### To connect to Neptune using either RDF4J or Apache Jena with Signature Version 4

signing

1. Clone the sample repository from GitHub.

```
git clone https://github.com/aws/amazon-neptune-sparql-java-sigv4.git
```

2. Change into the cloned directory.

```
cd amazon-neptune-sparql-java-sigv4
```

3. Get the latest version of the project by checking out the branch
   with the latest tag.

```
git checkout $(git describe --tags `git rev-list --tags --max-count=1`)
```

4. Enter one of the following commands to compile and run the example code.

Replace `your-neptune-endpoint` with the hostname or IP
address of your Neptune DB instance. The default port is 8182.

###### Note

For information about finding the hostname of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md")
section.

###### Eclipse RDF4J

Enter the following to run the RDF4J example.

```
mvn compile exec:java \
    -Dexec.mainClass="com.amazonaws.neptune.client.rdf4j.NeptuneRdf4JSigV4Example" \
    -Dexec.args="https://`your-neptune-endpoint`:`port`"
```

###### Apache Jena

Enter the following to run the Apache Jena example.

```
mvn compile exec:java \
    -Dexec.mainClass="com.amazonaws.neptune.client.jena.NeptuneJenaSigV4Example" \
    -Dexec.args="https://`your-neptune-endpoint`:`port`"
```

5. To view the source code for the example, see the examples in the
   `src/main/java/com/amazonaws/neptune/client/` directory.
   To use the SigV4 signing driver in your own Java application, add the
   `amazon-neptune-sigv4-signer` Maven package to the `<dependencies>`
   section of your `pom.xml`. We recommend that you use the examples as a starting
   point.
