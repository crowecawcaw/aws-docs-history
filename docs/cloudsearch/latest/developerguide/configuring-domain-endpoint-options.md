# Configuring Domain Endpoint Options in
 Amazon CloudSearch

Amazon CloudSearch domains let you require that all traffic to the domain arrive over HTTPS. This
 security feature helps you block clients that send unencrypted requests to the
 domain.

###### Topics

* [Configuring Domain
 Endpoint Options Using the Amazon CloudSearch Console](#configuring-domain-endpoint-options-console "#configuring-domain-endpoint-options-console")
* [Configuring Domain Endpoint
 Options Using the AWS CLI](#configuring-domain-endpoint-options-cli "#configuring-domain-endpoint-options-cli")
* [Configuring Domain Endpoint
 Options Using the AWS SDKs](#configuring-domain-endpoint-options-api "#configuring-domain-endpoint-options-api")

## Configuring Domain
 Endpoint Options Using the Amazon CloudSearch Console


###### To configure a search domain's endpoint options

1. Within the Amazon CloudSearch console, choose the name of your domain to open its
 settings.
2. Under **Domain configuration**, choose
 **Edit** next to **HTTPS options**.
3. Enable **Toggle HTTPS options**.
4. Choose **Submit**.

## Configuring Domain Endpoint
 Options Using the AWS CLI


Use the `aws cloudsearch update-domain-endpoint-options` command. For more
 information, see the [AWS CLI Command
 Reference](https://docs.aws.amazon.com/cli/latest/reference/cloudsearch/ "https://docs.aws.amazon.com/cli/latest/reference/cloudsearch/").


## Configuring Domain Endpoint
 Options Using the AWS SDKs


The AWS SDKs (except the Android and iOS SDKs) support all of the Amazon CloudSearch actions defined
 in the Amazon CloudSearch Configuration API, including [DescribeDomainEndpointOptions](API_DescribeDomainEndpointOptions.md "API_DescribeDomainEndpointOptions.md") and [UpdateDomainEndpointOptions](API_UpdateDomainEndpointOptions.md "API_UpdateDomainEndpointOptions.md"). For more information about installing
 and using the AWS SDKs, see [AWS Software
 Development Kits](http://aws.amazon.com/code "http://aws.amazon.com/code").
