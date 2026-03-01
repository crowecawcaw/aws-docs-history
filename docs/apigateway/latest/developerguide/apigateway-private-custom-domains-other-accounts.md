# Working with cross-account private custom domain names

This section explains how to work with cross-account private custom domain names. You can provide a private
custom domain name to another AWS account and use another AWS account to invoke a private custom domain
name.

You can share your private custom domain name to another AWS account using AWS Resource Access Manager or API Gateway. AWS Resource Access Manager
(AWS RAM) helps you securely share your resources across AWS accounts and within your organization or organizational
units (OUs). For more information, see
[What is AWS Resource Access Manager](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

For instructions on how to share a private custom domain name with another AWS account using AWS RAM, see [API provider: Share your private custom domain name using AWS RAM](apigateway-private-custom-domains-provider-share.md "apigateway-private-custom-domains-provider-share.md").

For instructions on how to share a private custom domain name with another AWS account using API Gateway, see [API provider: Share your private custom domain name using the API Gateway AWS CLI](apigateway-private-custom-domains-provider-share-cli.md "apigateway-private-custom-domains-provider-share-cli.md").

For instructions on how to consume a private custom domain name in another AWS account, see [API consumer: Associate your VPC endpoint with a private custom domain name shared with you](apigateway-private-custom-domains-consumer-create.md "apigateway-private-custom-domains-consumer-create.md").

## Best practices for working with cross-account private custom domain names

We recommend the following best practices for working with cross-account private custom domain names:

- Use AWS RAM to share your private custom domain names. When you use AWS RAM, you can reduce operational overhead and you don't have to create a
  `managementPolicy` for the Amazon API Gateway Management service.
- Use the `resource-owner` parameter when you list your private custom
  domain names or domain name access associations. Use the `resource-owner` parameter to only list the
  resources owned by you or by other AWS accounts.

The following example shows how to get all domain name access associations that you own:

```
aws apigateway get-domain-name-access-associations --resource-owner SELF
```

Use `--resource-owner OTHER_ACCOUNTS` to list all the domain name access associations that other
accounts have formed with your private custom domain name.
