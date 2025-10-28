# Authenticate when using the AMS API/CLI

When you use the AMS API/CLI, you must authenticate with temporary credentials.
To request temporary security credentials for federated users, cal
[GetFederationToken](../../../STS/latest/UsingSTS/CreatingFedTokens.md "../../../STS/latest/UsingSTS/CreatingFedTokens.md"),
[AssumeRole](../../../STS/latest/UsingSTS/sts_delegate.md "../../../STS/latest/UsingSTS/sts_delegate.md"),
[AssumeRoleWithSAML](../../../IAM/latest/UserGuide/id_credentials_temp_request.md#api_assumerolewithsaml "../../../IAM/latest/UserGuide/id_credentials_temp_request.md#api_assumerolewithsaml"), or
[AssumeRoleWithWebIdentity](../../../IAM/latest/UserGuide/id_credentials_temp_request.md#api_assumerolewithwebidentity "../../../IAM/latest/UserGuide/id_credentials_temp_request.md#api_assumerolewithwebidentity") AWS security token service (STS) APIs.

A common choice is SAML. After set up, you add an argument to
each operation that you call. For example:
`aws --profile saml amscm list-change-type-categories`.

A shortcut for SAML 2.0 profiles is to set the profile variable at the start
of each API/CLI with `set AWS_DEFAULT_PROFILE=saml` (for Windows; for
Linux it would be `export AWS_DEFAULT_PROFILE=saml`). For information
about setting CLI environment variables, see
[Configuring the AWS Command Line Interface, Environment Variables](../../../cli/latest/userguide/cli-chap-getting-started.md#cli-environment "../../../cli/latest/userguide/cli-chap-getting-started.md#cli-environment").
