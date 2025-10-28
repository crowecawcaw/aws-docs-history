# Secure your

Lightsail distribution with minimum TLS protocol version

Amazon Lightsail uses SSL/TLS certificates to validate custom (registered) domains that you
can use with your Lightsail distribution. This guide provides information about the viewer
minimum TLS protocol versions (protocol versions) that you can configure for your SSL/TLS
certificate. For more information about SSL/TLS certificates, see [SSL/TLS certificates in
Lightsail](understanding-tls-ssl-certificates-in-lightsail-https.md "understanding-tls-ssl-certificates-in-lightsail-https.md"). A viewer is an application that makes HTTP requests to the edge
locations that are associated to your Lightsail distribution. For more information about
distributions, see [Content delivery network distributions in Lightsail](amazon-lightsail-content-delivery-network-distributions.md "amazon-lightsail-content-delivery-network-distributions.md").

The `TLSv1.2_2021` protocol version is configured by default when you enable
custom domains for a distribution. You can configure a different protocol version, as
described later in this guide. Lightsail distributions do not support custom TLS protocol
versions.

## Supported protocols

Lightsail distributions can be configured with the following TLS protocols:

- (Recommended) TLSv1.2_2021
- TLSv1.2_2019
- TLSv1.2_2018
- TLSv1.1_2016

## Prerequisites

Complete the following prerequisites if you haven't already:

- [Create a Lightsail content delivery network distribution](amazon-lightsail-creating-content-delivery-network-distribution.md "amazon-lightsail-creating-content-delivery-network-distribution.md")
- [Create
  SSL/TLS certificates for your distribution](amazon-lightsail-create-a-distribution-certificate.md "amazon-lightsail-create-a-distribution-certificate.md")
- [Validate SSL/TLS certificates for your distribution](amazon-lightsail-validating-a-distribution-certificate.md "amazon-lightsail-validating-a-distribution-certificate.md")
- [Enable custom
  domains for your distribution](amazon-lightsail-point-domain-to-distribution.md "amazon-lightsail-point-domain-to-distribution.md")
- [Point your
  domain to the distribution](amazon-lightsail-point-domain-to-distribution.md "amazon-lightsail-point-domain-to-distribution.md")

## Identify the minimum

TLS protocol version for your distribution

Complete the following steps to identify the minimum TLS protocol version for your
Lightsail distribution

###### Note

In this guide, you will use AWS CloudShell to perform the upgrade. CloudShell is a
browser-based, pre-authenticated shell that you can launch directly from the
Lightsail console. With CloudShell, you can run AWS CLI commands using your
preferred shell, such as Bash, PowerShell, or Z shell. You can do this without
downloading or installing command line tools. For more information about how to set
up and use CloudShell, see For more information, see [AWS CloudShell in Lightsail](amazon-lightsail-cloudshell.md "amazon-lightsail-cloudshell.md").

1. Open a Terminal, [AWS CloudShell](amazon-lightsail-cloudshell.md "amazon-lightsail-cloudshell.md"),
   or Command Prompt window.
2. Enter the following command to identify the minimum TLS protocol version for
   your Lightsail distribution.

```
aws lightsail get-distributions --distribution-name `DistributionName` --region us-east-1 | grep "viewerMinimumTlsProtocolVersion"
```

In the command, replace `DistributionName` with the
name of the distribution you want to modify.

**Example**

```
aws lightsail get-distributions --distribution-name `Distribution-1` --region us-east-1 | grep "viewerMinimumTlsProtocolVersion"
```

The command will return the ID of the minimum TLS protocol version for your
distribution.

**Example**

```
"viewerMinimumTlsProtocolVersion": "TLSv1.2_2021"
```

## Configure the minimum TLS

protocol version using the AWS CLI

Complete the following procedure to configure the TLS protocol version using the
AWS Command Line Interface (AWS CLI). You do this by using the `update-distribution` command.
For more information, see the [update-distribution attribute](../../../cli/latest/reference/lightsail/update-distribution.md "../../../cli/latest/reference/lightsail/update-distribution.md") in the _AWS CLI Command
Reference_.

1. Open a Terminal, [AWS CloudShell](amazon-lightsail-cloudshell.md "amazon-lightsail-cloudshell.md"),
   or Command Prompt window.
2. Enter the following command to change the minimum TLS protocol version for
   your distribution.

```
aws lightsail update-distribution --distribution-name `DistributionName` --viewer-minimum-tls-protocol-version `ProtocolVersion`
```

In the command, replace the following example text with your own:

    * `DistributionName` with the name of the
     distribution that you want to update.
    * `ProtocolVersion` with the valid TLS protocol
     version. For example `TLSv1.2_2021` or
     `TLSv1.2_2019`.

Example:

```
aws lightsail update-distribution --distribution-name  `MyDistribution` --viewer-minimum-tls-protocol-version `TLSv1.2_2021`
```

Your change takes a few moments to become effective.
