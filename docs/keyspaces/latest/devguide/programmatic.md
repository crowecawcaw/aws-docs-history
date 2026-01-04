# Service endpoints for Amazon Keyspaces

###### Topics

- [Ports and protocols](#ports "#ports")
- [Global endpoints](#global_endpoints "#global_endpoints")
- [AWS GovCloud (US) Region FIPS endpoints](#fips_endpoints "#fips_endpoints")
- [China Regions endpoints](#china_endpoints "#china_endpoints")
- [Streams endpoints](#streams_endpoints "#streams_endpoints")
- [Connecting to dual-stack endpoints](dualstack_endpoints.md "dualstack_endpoints.md")

## Ports and protocols

You can access Amazon Keyspaces programmatically by running a `cqlsh` client, with an Apache 2.0 licensed Cassandra driver, or by
using the AWS CLI and the AWS SDK.

The following table shows the ports and protocols for the different access mechanisms.

| Programmatic Access | Port | Protocol |
| ------------------- | ---- | -------- |
| CQLSH               | 9142 | TLS      |
| Cassandra Driver    | 9142 | TLS      |
| AWS CLI             | 443  | HTTPS    |
| AWS SDK             | 443  | HTTPS    |

For
TLS connections, Amazon Keyspaces uses certificates issued under Amazon Trust Services (Amazon Root CAs 1–4) to authenticate against the server. For
more information, see [How to manually configure
cqlsh connections for TLS](programmatic.md#encrypt_using_tls "programmatic.md#encrypt_using_tls") or the [Before you begin](using_java_driver.md#using_java_driver.BeforeYouBegin "using_java_driver.md#using_java_driver.BeforeYouBegin") section of your
driver in the [Using a Cassandra client driver to access
Amazon Keyspaces programmatically](programmatic.md "programmatic.md") chapter.

## Global endpoints

Amazon Keyspaces supports both IPv4 and IPv6 public endpoints. You can choose between IPv4
endpoints and dual-stack endpoints. The endpoints use the following naming convention,
where you can replace `us-east-1` with another available AWS Region from the table.

- **IPv4 endpoints** – `cassandra.`us-east-1`.amazonaws.com`
- **Dual-stack endpoints** – `cassandra.`us-east-1`.api.aws`

For more information about dual-stack endpoints and how to configure connections, see
[Connecting to dual-stack endpoints](dualstack_endpoints.md "dualstack_endpoints.md").

Amazon Keyspaces is available in the following Regions.

| Region Name               | Region         | Endpoint                                                                                                                                       | Protocol                                                         |
| ------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| US East (Ohio)            | us-east-2      | cassandra.us-east-2.amazonaws.com<br>cassandra.us-east-2.api.aws                                                                               | HTTPS and TLS<br>HTTPS and TLS                                   |
| US East (N. Virginia)     | us-east-1      | cassandra.us-east-1.amazonaws.com<br>cassandra-fips.us-east-1.api.aws<br>cassandra-fips.us-east-1.amazonaws.com<br>cassandra.us-east-1.api.aws | HTTPS and TLS<br>HTTPS and TLS<br>HTTPS and TLS<br>HTTPS and TLS |
| US West (N. California)   | us-west-1      | cassandra.us-west-1.amazonaws.com<br>cassandra.us-west-1.api.aws                                                                               | HTTPS and TLS<br>HTTPS and TLS                                   |
| US West (Oregon)          | us-west-2      | cassandra.us-west-2.amazonaws.com<br>cassandra-fips.us-west-2.api.aws<br>cassandra-fips.us-west-2.amazonaws.com<br>cassandra.us-west-2.api.aws | HTTPS and TLS<br>HTTPS and TLS<br>HTTPS and TLS<br>HTTPS and TLS |
| Africa (Cape Town)        | af-south-1     | cassandra.af-south-1.amazonaws.com<br>cassandra.af-south-1.api.aws                                                                             | HTTPS and TLS<br>HTTPS and TLS                                   |
| Asia Pacific (Hong Kong)  | ap-east-1      | cassandra.ap-east-1.amazonaws.com<br>cassandra.ap-east-1.api.aws                                                                               | HTTPS and TLS<br>HTTPS and TLS                                   |
| Asia Pacific (Mumbai)     | ap-south-1     | cassandra.ap-south-1.amazonaws.com<br>cassandra.ap-south-1.api.aws                                                                             | HTTPS and TLS<br>HTTPS and TLS                                   |
| Asia Pacific (Seoul)      | ap-northeast-2 | cassandra.ap-northeast-2.amazonaws.com<br>cassandra.ap-northeast-2.api.aws                                                                     | HTTPS and TLS<br>HTTPS and TLS                                   |
| Asia Pacific (Singapore)  | ap-southeast-1 | cassandra.ap-southeast-1.amazonaws.com<br>cassandra.ap-southeast-1.api.aws                                                                     | HTTPS and TLS<br>HTTPS and TLS                                   |
| Asia Pacific (Sydney)     | ap-southeast-2 | cassandra.ap-southeast-2.amazonaws.com<br>cassandra.ap-southeast-2.api.aws                                                                     | HTTPS and TLS<br>HTTPS and TLS                                   |
| Asia Pacific (Tokyo)      | ap-northeast-1 | cassandra.ap-northeast-1.amazonaws.com<br>cassandra.ap-northeast-1.api.aws                                                                     | HTTPS and TLS<br>HTTPS and TLS                                   |
| Canada (Central)          | ca-central-1   | cassandra.ca-central-1.amazonaws.com<br>cassandra.ca-central-1.api.aws                                                                         | HTTPS and TLS<br>HTTPS and TLS                                   |
| Europe (Frankfurt)        | eu-central-1   | cassandra.eu-central-1.amazonaws.com<br>cassandra.eu-central-1.api.aws                                                                         | HTTPS and TLS<br>HTTPS and TLS                                   |
| Europe (Ireland)          | eu-west-1      | cassandra.eu-west-1.amazonaws.com<br>cassandra.eu-west-1.api.aws                                                                               | HTTPS and TLS<br>HTTPS and TLS                                   |
| Europe (London)           | eu-west-2      | cassandra.eu-west-2.amazonaws.com<br>cassandra.eu-west-2.api.aws                                                                               | HTTPS and TLS<br>HTTPS and TLS                                   |
| Europe (Paris)            | eu-west-3      | cassandra.eu-west-3.amazonaws.com<br>cassandra.eu-west-3.api.aws                                                                               | HTTPS and TLS<br>HTTPS and TLS                                   |
| Europe (Stockholm)        | eu-north-1     | cassandra.eu-north-1.amazonaws.com<br>cassandra.eu-north-1.api.aws                                                                             | HTTPS and TLS<br>HTTPS and TLS                                   |
| Middle East (Bahrain)     | me-south-1     | cassandra.me-south-1.amazonaws.com<br>cassandra.me-south-1.api.aws                                                                             | HTTPS and TLS<br>HTTPS and TLS                                   |
| Middle East (UAE)         | me-central-1   | cassandra.me-central-1.amazonaws.com<br>cassandra.me-central-1.api.aws                                                                         | HTTPS and TLS<br>HTTPS and TLS                                   |
| South America (São Paulo) | sa-east-1      | cassandra.sa-east-1.amazonaws.com<br>cassandra.sa-east-1.api.aws                                                                               | HTTPS and TLS<br>HTTPS and TLS                                   |
| AWS GovCloud (US-East)    | us-gov-east-1  | cassandra.us-gov-east-1.amazonaws.com<br>cassandra.us-gov-east-1.api.aws                                                                       | HTTPS and TLS<br>HTTPS and TLS                                   |
| AWS GovCloud (US-West)    | us-gov-west-1  | cassandra.us-gov-west-1.amazonaws.com<br>cassandra.us-gov-west-1.api.aws                                                                       | HTTPS and TLS<br>HTTPS and TLS                                   |

## AWS GovCloud (US) Region FIPS endpoints

Available FIPS endpoints in the AWS GovCloud (US) Region. Amazon Keyspaces supports both IPv4 and IPv6 FIPS endpoints. You can choose between IPv4
endpoints and dual-stack endpoints. For more information, see [Amazon Keyspaces in the
_AWS GovCloud (US) User Guide_](../../../govcloud-us/latest/UserGuide/govcloud-keyspaces.md "../../../govcloud-us/latest/UserGuide/govcloud-keyspaces.md").

| Region name            | Region        | FIPS endpoint IPv4                    | FIPS endpoint dual-stack        | Protocol      |
| ---------------------- | ------------- | ------------------------------------- | ------------------------------- | ------------- |
| AWS GovCloud (US-East) | us-gov-east-1 | cassandra.us-gov-east-1.amazonaws.com | cassandra.us-gov-east-1.api.aws | HTTPS and TLS |
| AWS GovCloud (US-West) | us-gov-west-1 | cassandra.us-gov-west-1.amazonaws.com | cassandra.us-gov-west-1.api.aws | HTTPS and TLS |

## China Regions endpoints

Amazon Keyspaces supports IPv4 endpoints in the AWS China Regions.

To access
these endpoints, you have to sign up for a separate set of account credentials unique to the China Regions.
For more information, see [China Signup, Accounts, and Credentials](https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html "https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html").

| Region name     | Region         | Endpoint                                  | Protocol      |
| --------------- | -------------- | ----------------------------------------- | ------------- |
| China (Beijing) | cn-north-1     | cassandra.cn-north-1.amazonaws.com.cn     | HTTPS and TLS |
| China (Ningxia) | cn-northwest-1 | cassandra.cn-northwest-1.amazonaws.com.cn | HTTPS and TLS |

## Streams endpoints

Amazon Keyspaces CDC streams is available in the following AWS Regions. This table shows the available
dual-stack service endpoint for each Region. For more information about Amazon Keyspaces CDC streams, see
[How to access CDC stream endpoints in
Amazon Keyspaces](CDC_access-endpoints.md "CDC_access-endpoints.md").

| Region Name               | Region         | Endpoint                                 | Protocol |
| ------------------------- | -------------- | ---------------------------------------- | -------- |
| US East (Ohio)            | us-east-2      | cassandra-streams.us-east-2.api.aws      | HTTPS    |
| US East (N. Virginia)     | us-east-1      | cassandra-streams.us-east-1.api.aws      | HTTPS    |
| US West (N. California)   | us-west-1      | cassandra-streams.us-west-1.api.aws      | HTTPS    |
| US West (Oregon)          | us-west-2      | cassandra-streams.us-west-2.api.aws      | HTTPS    |
| Africa (Cape Town)        | af-south-1     | cassandra-streams.af-south-1.api.aws     | HTTPS    |
| Asia Pacific (Hong Kong)  | ap-east-1      | cassandra-streams.ap-east-1.api.aws      | HTTPS    |
| Asia Pacific (Mumbai)     | ap-south-1     | cassandra-streams.ap-south-1.api.aws     | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | cassandra-streams.ap-northeast-2.api.aws | HTTPS    |
| Asia Pacific (Singapore)  | ap-southeast-1 | cassandra-streams.ap-southeast-1.api.aws | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | cassandra-streams.ap-southeast-2.api.aws | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | cassandra-streams.ap-northeast-1.api.aws | HTTPS    |
| Canada (Central)          | ca-central-1   | cassandra-streams.ca-central-1.api.aws   | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | cassandra-streams.eu-central-1.api.aws   | HTTPS    |
| Europe (Ireland)          | eu-west-1      | cassandra-streams.eu-west-1.api.aws      | HTTPS    |
| Europe (London)           | eu-west-2      | cassandra-streams.eu-west-2.api.aws      | HTTPS    |
| Europe (Paris)            | eu-west-3      | cassandra-streams.eu-west-3.api.aws      | HTTPS    |
| Europe (Stockholm)        | eu-north-1     | cassandra-streams.eu-north-1.api.aws     | HTTPS    |
| Middle East (Bahrain)     | me-south-1     | cassandra-streams.me-south-1.api.aws     | HTTPS    |
| Middle East (UAE)         | me-central-1   | cassandra-streams.me-central-1.api.aws   | HTTPS    |
| South America (São Paulo) | sa-east-1      | cassandra-streams.sa-east-1.api.aws      | HTTPS    |
| AWS GovCloud (US-East)    | us-gov-east-1  | cassandra-streams.us-gov-east-1.api.aws  | HTTPS    |
| AWS GovCloud (US-West)    | us-gov-west-1  | cassandra-streams.us-gov-west-1.api.aws  | HTTPS    |
