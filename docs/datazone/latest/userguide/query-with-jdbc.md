# Analyze Amazon DataZone subscribed data with external

analytics applications via JDBC connection

Amazon DataZone enables data consumers to easily locate and subscribe to data from multiple
sources within a single project and analyze this data using Amazon Athena, Amazon
Redshift Query Editor, and Amazon SageMaker.

Amazon DataZone also supports authentication via the Athena JDBC driver that enables users
to query their subscribed Amazon DataZone data using popular external SQL and analytics
tools, such as SQL Workbench, DBeaver, Tableau, Domino, Power BI and many others. Users
can authenticate using their corporate credentials through SSO or IAM and begin
analyzing their subscribed data within their Amazon DataZone projects.

Amazon DataZone's support of the Athena JDBC driver provides the following benefits:

- Greater tool choice for querying and visualization - data consumers can
  connect to Amazon DataZone using their preferred tools from a wide range of analytics
  tools that support a JDBC connection. This enables them to continue using the
  software they are familiar with without the need to learn new tools for data
  consumption.
- Programmatic access - a JDBC connection to access-governed data via servers or
  custom applications enables data consumers to perform automated and more complex
  data operations.
  You can use your JDBC URL to connect your external analytics tools to your Amazon DataZone
  subscribed data. To obtain your JDBC URL, perform the following procedure:

###### Important

In the current release, Amazon DataZone supports authentication using the Amazon Athena
JDBC Driver. To complete this procedure, make sure that you have downloaded and
installed the latest [Athena
JDBC driver](../../../athena/latest/ug/jdbc-v3-driver.md "../../../athena/latest/ug/jdbc-v3-driver.md") for your analytics application of choice.

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. In the Amazon DataZone data portal, choose **Browse Projects
   List** and then find and choose the project where you have the data
   that you want to analyze.
3. In the right-hand side panel on the project's home page, choose
   **Connect with JDBC**.
4. In the **JDBC parameters** pop up window, choose your
   authentication method (SSO credentials or IAM credentials) and then copy the
   string or the individual parameters of the JDBC URL. You can then use it to
   connect to your external analytics application.
   When you connect your external analytics application to Amazon DataZone using your JBDC
   query or parameters, you invoke the `RedeemAccessToken` API. The
   `RedeemAccessToken` API exchanges an Identity Center access token for the
   `AmazonDataZoneDomainExecutionRole` credentials, which are used to call
   the `GetEnvironmentCredentials` API.

For more information about the authentication mechanism that uses IAM credentials to
connect to Amazon DataZone-governed data in Athena, see [DataZone IAM Credentials Provider](../../../athena/latest/ug/jdbc-v3-driver-datazone-iamcp.md "../../../athena/latest/ug/jdbc-v3-driver-datazone-iamcp.md"). For more information about the
authentication mechanism that enables connecting to Amazon DataZone-governed data in Athena
using IAM Identity Center, see [DataZone Idc Credentials Provider](../../../athena/latest/ug/jdbc-v3-driver-datazone-idc.md "../../../athena/latest/ug/jdbc-v3-driver-datazone-idc.md").

## RedeemAccessToken API Reference

**Request syntax**

```

POST /sso/redeem-token HTTP/1.1
Content-type: application/json

{
   "domainId": "string",
   "accessToken": "string"
}

```

**Request parameters**

The request uses the following parameters.

**DomainId**

The ID of the Amazon DataZone domain.

Pattern: ^dzd[-\_][a-zA-Z0-9\_-]{1,36}$

Required: yes

**accessToken**

The Identity Center access token.

Type: string

Required: yes

**Response syntax**

```

HTTP/1.1 200
Content-type: application/json

{
   "credentials": AwsCredentials
}

```

**Response elements**

**credentials**

The `AmazonDataZoneDomainExecutionRole` credentials that
are used to call the `GetEnvironmentCredentials` API.

Type: Array of `AwsCredentials` objects. This data type
includes the following properties:

- accessKeyId: AccessKeyId
- secretAccessKey: SecretAccessKey
- sessionToken: SessionToken
- expiration: Timestamp

**accessToken**

The Identity Center access token.

Type: string

Required: yes

**Errors**

**AccessDeniedException**

You do not have sufficient access to perform this action.

HTTP Status Code: 403

**ResourceNotFoundException**

The specified resource cannot be found.

HTTP Status Code: 404

**ValidationException**

The input fails to satisfy the constraints specified by the AWS
service.

HTTP Status Code: 400

**InternalServerException**

The request has failed because of an unknown error, exception or
failure.

HTTP Status Code: 500
