# AWS Private CA Connector for SCEP

Connector for Simple Certificate Enrollment Protocol (SCEP) links AWS Private Certificate Authority to your SCEP-enabled mobile devices and networking equipment. With Connector for SCEP, you can use AWS Private CA to issue certificates and enroll your SCEP devices. Connector for SCEP is available to use with popular mobile device management (MDM) systems and is designed to work with clients or endpoints that supports SCEP.

###### Topics

- [Features](#features-c4scep "#features-c4scep")
- [How to get started with Connector for SCEP](#how-to-gs-c4scep "#how-to-gs-c4scep")
- [Related services](#related-services-c4scep "#related-services-c4scep")
- [Access Connector for SCEP](#accessing-c4scep "#accessing-c4scep")
- [Pricing](#pricing-c4scep "#pricing-c4scep")
- [Connector for SCEP concepts](c4scep-concepts.md "c4scep-concepts.md")
- [Understand Connector for SCEP considerations and limitations](c4scep-considerations-limitations.md "c4scep-considerations-limitations.md")
- [Set up Connector for SCEP](connector-for-scep-setting-up.md "connector-for-scep-setting-up.md")
- [Get started with
  Connector for SCEP](connector-for-scep-getting-started.md "connector-for-scep-getting-started.md")
- [Configure your MDM system for
  Connector for SCEP](using-connector-for-scep-with-mdm.md "using-connector-for-scep-with-mdm.md")
- [Monitor Connector for SCEP](c4scep-monitoring-overview.md "c4scep-monitoring-overview.md")
- [Troubleshoot AWS Private Certificate Authority Connector for SCEP issues](troubleshoot-connector-scep.md "troubleshoot-connector-scep.md")

## Features

**Support for SCEP protocol** - SCEP is a widely-adopted protocol for getting digital identity certificates from a certificate authority (CA) and distributing them to mobile devices and networking gear. You can use Connector for SCEP to help you enroll your endpoints using SCEP.

**Mobile device enrollment** - You can use Connector for SCEP with popular MDM systems including Microsoft Intune and Jamf Pro.

**Issue certificates at scale** - After you configure your SCEP-enabled devices to request certificates through the connector's SCEP endpoint, your clients can automatically request certificates from AWS Private CA.

## How to get started with Connector for SCEP

To get started, launch the guided wizard from the [Connector for SCEP management console](https://console.aws.amazon.com/pca-connector-scep/home "https://console.aws.amazon.com/pca-connector-scep/home") which helps you create a connector and designate the private CA to use with the connector. After completing these steps, Connector for SCEP provides an endpoint and other configuration parameters that you can enter into your MDM systems or networking equipment. After configuring your MDM systems or networking equipment, your clients will automatically request certificates from AWS Private CA. To learn more about how to get started with Connector for SCEP, see [Get started with
Connector for SCEP](connector-for-scep-getting-started.md "connector-for-scep-getting-started.md").

## Related services

Connector for SCEP is related to the following AWS services.

- **AWS Private Certificate Authority** - AWS Private CA provides you a highly-available private CA service without the upfront investment and ongoing maintenance costs of operating your own private CA.
- **AWS Private CA Connector for Active Directory** - Connector for AD links your Active Directory (AD) to AWS Private CA. The connector brokers the exchange of certificates from AWS Private CA to users and machines managed by your AD.

## Access Connector for SCEP

You can create, access, and manage your Connector for SCEP connectors using any of the following interfaces:

- **AWS Management Console** - Provides a web interface that you can use to access Connector for SCEP. See [Connector for SCEP management console](https://console.aws.amazon.com/pca-connector-scep/home "https://console.aws.amazon.com/pca-connector-scep/home").
- **AWS Command Line Interface** - Provides commands for a broad set of AWS services, including Connector for SCEP. The AWS CLI is supported on Windows, macOS, and Linux. For more information, see [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").
- **AWS SDKs** - Provide language-specific APIs and take care of many of the connection details, such as calculating signatures, handling request retries, and error handling. For more information, see [AWS Command Line Interface](https://aws.amazon.com/developer/tools/#SDKs "https://aws.amazon.com/developer/tools/#SDKs").
- **Connector for SCEP API** - Provides low-level API actions that you call using HTTPS requests. Using the Connector for SCEP API is the most direct way to access the service. However, the Connector for SCEP API requires that your application handle low-level details such as generating the hash to sign the request, and error handling. For more information, see [Connector for SCEP API reference](../../../pca-connector-scep/latest/APIReference/Welcome.md "../../../pca-connector-scep/latest/APIReference/Welcome.md").

## Pricing

Connector for SCEP is offered as a feature of AWS Private CA at no additional cost. You only pay for AWS Private Certificate Authority operations and certificates used to create and update connectors.

For the latest AWS Private CA pricing information, see [AWS Private Certificate Authority Pricing](https://aws.amazon.com/private-ca/pricing/ "https://aws.amazon.com/private-ca/pricing/"). You can also use the [AWS pricing
calculator](https://calculator.aws/#/createCalculator/certificateManager "https://calculator.aws/#/createCalculator/certificateManager") to estimate costs.
