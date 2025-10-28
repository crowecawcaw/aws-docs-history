# OpenSSL Dynamic Engine for AWS CloudHSM Client SDK 5

The AWS CloudHSM OpenSSL Dynamic Engine allows you to offload cryptographic operations to your
CloudHSM cluster through the OpenSSL API.

AWS CloudHSM provides an OpenSSL Dynamic Engine, which you can read about in [AWS CloudHSM SSL/TLS offload on Linux using Tomcat with JSSE](third-offload-linux-jsse.md "third-offload-linux-jsse.md") or
[AWS CloudHSM SSL/TLS offload on Linux using NGINX or
Apache with OpenSSL](third-offload-linux-openssl.md "third-offload-linux-openssl.md").
For an example on using AWS CloudHSM with OpenSSL, refer to [this AWS security blog](https://aws.amazon.com/blogs/security/automate-the-deployment-of-an-nginx-web-service-using-amazon-ecs-with-tls-offload-in-cloudhsm/ "https://aws.amazon.com/blogs/security/automate-the-deployment-of-an-nginx-web-service-using-amazon-ecs-with-tls-offload-in-cloudhsm/").
For information about platform support for SDKs, see [AWS CloudHSM Client SDK 5 supported platforms](client-supported-platforms.md "client-supported-platforms.md"). For troubleshooting, see [Known issues for the OpenSSL Dynamic Engine for AWS CloudHSM](ki-openssl-sdk.md "ki-openssl-sdk.md").

Use the following sections to install and configure the AWS CloudHSM dynamic engine for OpenSSL,
using Client SDK 5.

For information on using Client SDK 3, see [Using previous SDK version to work with
AWS CloudHSM](choose-client-sdk.md "choose-client-sdk.md").

###### Topics

- [Install the OpenSSL Dynamic Engine for AWS CloudHSM
  Client SDK 5](openssl5-install.md "openssl5-install.md")
- [Supported key types for OpenSSL Dynamic Engine for AWS CloudHSM
  Client SDK 5](openssl-key-types.md "openssl-key-types.md")
- [Supported mechanisms for OpenSSL Dynamic Engine for AWS CloudHSM
  Client SDK 5](openssl-mechanisms.md "openssl-mechanisms.md")
- [Advanced configurations for OpenSSL for
  AWS CloudHSM](openssl-library-configs.md "openssl-library-configs.md")
