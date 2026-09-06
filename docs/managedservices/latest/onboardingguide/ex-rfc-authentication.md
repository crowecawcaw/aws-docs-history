

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Authenticate when using the AMS API/CLI
<a name="ex-rfc-authentication"></a>

When you use the AMS API/CLI, you must authenticate with temporary credentials. To request temporary security credentials for federated users, cal [ GetFederationToken](https://docs.aws.amazon.com/STS/latest/UsingSTS/CreatingFedTokens.html), [AssumeRole](https://docs.aws.amazon.com/STS/latest/UsingSTS/sts_delegate.html), [AssumeRoleWithSAML](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithsaml), or [ AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithwebidentity) AWS security token service (STS) APIs.

A common choice is SAML. After set up, you add an argument to each operation that you call. For example: `aws --profile saml amscm list-change-type-categories`.

A shortcut for SAML 2.0 profiles is to set the profile variable at the start of each API/CLI with `set AWS_DEFAULT_PROFILE=saml` (for Windows; for Linux it would be `export AWS_DEFAULT_PROFILE=saml`). For information about setting CLI environment variables, see [ Configuring the AWS Command Line Interface, Environment Variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-environment).