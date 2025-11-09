# Configuring TLS settings in domain

configurations

AWS IoT Core provides [predefined security polices](transport-security.md#tls-policy-table "transport-security.md#tls-policy-table") for
you to customize your Transport Layer Security (TLS) settings for [TLS 1.2](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.2 "https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.2")
and [TLS
1.3](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.3 "https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_1.3") in domain configurations. A security policy is a combination of TLS
protocols and their ciphers that determine the supported protocols and ciphers during
TLS negotiations between a client and a server. With the supported security policies,
you can manage your devices' TLS settings with more flexibility, apply the most
up-to-date security measures when connecting new devices, and maintain consistent TLS
configurations for existing devices.

The following table describes the security policies, their TLS versions, and supported
regions:

| Security policy name                | Supported AWS Regions                                                                                                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| IoTSecurityPolicy_TLS13_1_3_2022_10 | All AWS Regions                                                                                                                                                                      |
| IoTSecurityPolicy_TLS13_1_2_2022_10 | All AWS Regions                                                                                                                                                                      |
| IoTSecurityPolicy_TLS12_1_2_2022_10 | All AWS Regions                                                                                                                                                                      |
| IoTSecurityPolicy_TLS12_1_0_2016_01 | ap-east-1, ap-northeast-2, ap-south-1, ap-southeast-2, ca-central-1,<br>cn-north-1, cn-northwest-1, eu-north-1, eu-west-2, eu-west-3,<br>me-south-1, sa-east-1, us-east-2, us-west-1 |
| IoTSecurityPolicy_TLS12_1_0_2015_01 | ap-northeast-1, ap-southeast-1, eu-central-1, eu-west-1, us-east-1,<br>us-west-2                                                                                                     |

The names of the security policies in AWS IoT Core include version information based on the
year and month that they were released. If you create a new domain configuration, the
security policy will default to `IoTSecurityPolicy_TLS13_1_2_2022_10`. For a
complete table of security policies with details of protocols, TCP ports, and ciphers, see
[Security polices](transport-security.md#tls-policy-table "transport-security.md#tls-policy-table"). AWS IoT Core doesn't support
custom security policies. For more information, see [Transport security in AWS IoT Core](transport-security.md "transport-security.md").

To configure TLS settings in domain configurations, you can use the AWS IoT console or
the AWS CLI.

###### Contents

- [Configure TLS settings in domain
  configurations (console)](#custom-tls-console "#custom-tls-console")
- [Configure TLS settings in domain configurations
  (CLI)](#custom-tls-cli "#custom-tls-cli")

## Configure TLS settings in domain

configurations (console)

###### To configure TLS settings using the AWS IoT console

1. Sign in to the AWS Management Console and open the [AWS IoT
   console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home").
2. To configure TLS settings when you create a new domain configuration,
   follow these steps.
   1. In the left navigation pane, choose
      **Settings**, and then, from the
      **Domain configurations** section, choose
      **Create domain configuration**.
   2. In the **Create domain configuration** page,
      in the **Custom domain settings - _optional_** section,
      choose a security policy from **Select security
      policy**.
   3. Follow the widget and complete the rest of the steps. Choose
      **Create domain
      configuration**.

3. To update TLS settings in an existing domain configuration, follow
   these steps.
   1. In the left navigation pane, choose
      **Settings**, and then, under
      **Domain configurations**, choose a domain
      configuration.
   2. In the **Domain configuration details** page,
      choose **Edit**. Then, in the **Custom
      domain settings - _optional_** section, under
      **Select security policy**, choose a
      security policy.
   3. Choose **Update domain
      configuration**.

For more information, see [Create a domain configuration](iot-custom-endpoints-configurable-custom.md#iot-custom-endpoints-configurable-custom-domain-config "iot-custom-endpoints-configurable-custom.md#iot-custom-endpoints-configurable-custom-domain-config") and [Manage domain
configurations](iot-custom-endpoints-managing.md "iot-custom-endpoints-managing.md").

## Configure TLS settings in domain configurations

(CLI)

You can use the [**create-domain-configuration**](../../../cli/latest/reference/iot/create-domain-configuration.md "../../../cli/latest/reference/iot/create-domain-configuration.md") and [**update-domain-configuration**](../../../cli/latest/reference/iot/update-domain-configuration.md "../../../cli/latest/reference/iot/update-domain-configuration.md") CLI commands to
configure your TLS settings in domain configurations.

1. To specify TLS settings using the [**create-domain-configuration**](../../../cli/latest/reference/iot/create-domain-configuration.md "../../../cli/latest/reference/iot/create-domain-configuration.md") CLI
   command:

````
`aws iot create-domain-configuration \
 --domain-configuration-name `domainConfigurationName` \
 `--tls-config securityPolicy=`IoTSecurityPolicy_TLS13_1_2_2022_10```
````

The output of this command can look like the following:

```
{
"domainConfigurationName": "test",
"domainConfigurationArn": "arn:aws:iot:us-west-2:123456789012:domainconfiguration/test/34ga9"
}
```

If you create a new domain configuration without specifying the security
policy, the value will default to:
`IoTSecurityPolicy_TLS13_1_2_2022_10`. 2. To describe TLS settings using the [**describe-domain-configuration**](../../../cli/latest/reference/iot/describe-domain-configuration.md "../../../cli/latest/reference/iot/describe-domain-configuration.md") CLI
command:

```
`aws iot describe-domain-configuration \
 --domain-configuration-name `domainConfigurationName``
```

This command can return the domain configuration details that include the TLS
settings like the following:

```
{
 "tlsConfig": {
 "securityPolicy": "IoTSecurityPolicy_TLS13_1_2_2022_10"
 },
 "domainConfigurationStatus": "ENABLED",
 "serviceType": "DATA",
 "domainType": "AWS_MANAGED",
 "domainName": "d1234567890abcdefghij-ats.iot.us-west-2.amazonaws.com",
 "serverCertificates": [],
 "lastStatusChangeDate": 1678750928.997,
 "domainConfigurationName": "test",
 "domainConfigurationArn": "arn:aws:iot:us-west-2:123456789012:domainconfiguration/test/34ga9"
}
```

3. To update TLS settings using the [**update-domain-configuration**](../../../cli/latest/reference/iot/update-domain-configuration.md "../../../cli/latest/reference/iot/update-domain-configuration.md") CLI
   command:

```
`aws iot update-domain-configuration \
 --domain-configuration-name `domainConfigurationName` \
 --tls-config securityPolicy=`IoTSecurityPolicy_TLS13_1_2_2022_10``
```

The output of this command can look like the following:

```
{
"domainConfigurationName": "test",
"domainConfigurationArn": "arn:aws:iot:us-west-2:123456789012:domainconfiguration/test/34ga9"
}
```

4. To update the TLS settings for your ATS endpoint, run the [**update-domain-configuration**](../../../cli/latest/reference/iot/update-domain-configuration.md "../../../cli/latest/reference/iot/update-domain-configuration.md") CLI command.
   The domain configuration name for your ATS endpoint is
   `iot:Data-ATS`.

````
`aws iot update-domain-configuration \
 --domain-configuration-name "iot:Data-ATS" \
 `--tls-config securityPolicy=`IoTSecurityPolicy_TLS13_1_2_2022_10```
````

The output of the command can look like the following:

```
{
"domainConfigurationName": "iot:Data-ATS",
"domainConfigurationArn": "arn:aws:iot:us-west-2:123456789012:domainconfiguration/iot:Data-ATS"
}
```

For more information, see [CreateDomainConfiguration](../apireference/API_CreateDomainConfiguration.md "../apireference/API_CreateDomainConfiguration.md") and [UpdateDomainConfiguration](../apireference/API_UpdateDomainConfiguration.md "../apireference/API_UpdateDomainConfiguration.md") in the _AWS API
Reference_.
