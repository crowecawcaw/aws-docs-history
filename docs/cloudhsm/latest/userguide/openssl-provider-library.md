# OpenSSL Provider for AWS CloudHSM Client SDK 5

The AWS CloudHSM OpenSSL Provider allows you to offload TLS cryptographic operations to your
CloudHSM cluster through the OpenSSL Provider API. The Provider interface is the
recommended approach for new deployments using OpenSSL 3.2 and later.

Use the following sections to install and configure the AWS CloudHSM OpenSSL Provider,
using Client SDK 5.

###### Warning

Integration with OpenSSL CLI is not currently supported by AWS CloudHSM OpenSSL Provider. See [AWS CloudHSM SSL/TLS offload on Linux using NGINX or HAProxy with OpenSSL Provider](third-offload-linux-openssl-provider.md "third-offload-linux-openssl-provider.md") for supported integrations.

## Supported platforms

The OpenSSL Provider requires OpenSSL 3.2 or later, available on EL9+, Ubuntu 24.04+, and Amazon Linux 2023+.

Verify compatibility: `openssl version`

###### Topics

- [Install the OpenSSL Provider for AWS CloudHSM
  Client SDK 5](openssl-provider-install.md "openssl-provider-install.md")
- [Supported key types for OpenSSL Provider for AWS CloudHSM Client SDK 5](openssl-provider-key-types.md "openssl-provider-key-types.md")
- [OpenSSL Provider Supported Mechanisms](openssl-provider-mechanisms.md "openssl-provider-mechanisms.md")
- [OpenSSL Provider Advanced Configuration](openssl-provider-advanced-config.md "openssl-provider-advanced-config.md")
