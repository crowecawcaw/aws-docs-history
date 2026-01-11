# Known issues for the OpenSSL Provider for AWS CloudHSM

These are the known issues for OpenSSL Provider for AWS CloudHSM.

###### Topics

- [Issue: Errors in OpenSSL CLI when used with OpenSSL Provider](#ki-openssl-provider-1 "#ki-openssl-provider-1")

##

Issue: Errors in OpenSSL CLI when used with OpenSSL Provider

- **Impact:**
  Integration with OpenSSL CLI is not currently supported by AWS CloudHSM OpenSSL Provider. See [AWS CloudHSM SSL/TLS offload on Linux using NGINX or HAProxy with OpenSSL Provider](third-offload-linux-openssl-provider.md "third-offload-linux-openssl-provider.md") for supported integrations.
- **Resolution:**
  Use supported integrations listed in [AWS CloudHSM SSL/TLS offload on Linux using NGINX or HAProxy with OpenSSL Provider](third-offload-linux-openssl-provider.md "third-offload-linux-openssl-provider.md"). Any updates to OpenSSL CLI support will be announced on the version history page.
