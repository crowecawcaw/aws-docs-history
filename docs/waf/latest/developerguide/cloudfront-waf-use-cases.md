**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Common use cases for protecting CloudFront distributions with AWS WAF

The following AWS WAF features work the same way for all CloudFront distributions.
Considerations for multi-tenant distributions are listed following each feature scenario.

## Using AWS WAF with CloudFront custom error pages

By default, when AWS WAF blocks a web request based on the criteria that you specify, it returns HTTP status code `403 (Forbidden)` to CloudFront, and CloudFront returns that status code to the viewer. The viewer then displays a brief and sparsely formatted default message similar to the following:

```
Forbidden: You don't have permission to access /myfilename.html on this server.
```

You can override this behavior in your AWS WAF protection pack (web ACL) rules by defining custom responses. For more information about customizing response behavior using AWS WAF rules, see [Sending custom responses for Block
actions](customizing-the-response-for-blocked-requests.md "customizing-the-response-for-blocked-requests.md").

###### Note

Responses that you customize using AWS WAF rules take precedence over any response specifications that you define in CloudFront custom error pages.

If you'd rather display a custom error message through CloudFront, possibly using the same formatting as the rest of your website, you can configure CloudFront to return to the viewer an object (for example, an HTML file) that contains your custom error message.

###### Note

CloudFront can't distinguish between an HTTP status code 403 that is returned by your origin and one that is returned by AWS WAF when a request is blocked. This means that you can't return different custom error pages based on the different causes of an HTTP status code 403.

For more information about CloudFront custom error pages, see [Generating custom error responses](../../../AmazonCloudFront/latest/DeveloperGuide/GeneratingCustomErrorResponses.md "../../../AmazonCloudFront/latest/DeveloperGuide/GeneratingCustomErrorResponses.md") in the _Amazon CloudFront Developer Guide_.

### Custom error pages in multi-tenant distributions

For CloudFront multi-tenant distributions, you can configure custom error pages in the following ways:

- At the multi-tenant level - These settings apply to all tenant distributions that use the multi-tenant distribution template
- Through AWS WAF rules - Custom responses defined in protection packs (web ACLs) take precedence over both multi-tenant distribution and tenant-level custom error pages

## Using AWS WAF with CloudFront for applications running on your own HTTP server

When you use AWS WAF with CloudFront, you can protect your applications running on any HTTP webserver, whether it's a webserver that's running in Amazon Elastic Compute Cloud (Amazon EC2) or a webserver that you manage privately. You can also configure CloudFront to require HTTPS between CloudFront and your own webserver, as well as between viewers and CloudFront.

###### Requiring HTTPS between CloudFront and your own webserver

To require HTTPS between CloudFront and your own webserver, you can use the CloudFront custom origin feature and configure the **Origin Protocol Policy** and the **Origin Domain Name** settings for specific origins. In your CloudFront configuration, you can specify the DNS name of the server along with the port and the protocol that you want CloudFront to use when fetching objects from your origin. You should also ensure that the SSL/TLS certificate on your custom origin server matches the origin domain name you've configured. When you use your own HTTP webserver outside of AWS, you must use a certificate that is signed by a trusted third-party certificate authority (CA), for example, Comodo, DigiCert, or Symantec. For more information about requiring HTTPS for communication between CloudFront and your own webserver, see the topic [Requiring HTTPS for Communication Between CloudFront and Your Custom Origin](../../../AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.md "../../../AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.md") in the _Amazon CloudFront Developer Guide_.

###### Requiring HTTPS between a viewer and CloudFront

To require HTTPS between viewers and CloudFront, you can change the **Viewer Protocol Policy** for one or more cache behaviors in your CloudFront distribution. For more information about using HTTPS between viewers and CloudFront, see the topic [Requiring HTTPS for Communication Between Viewers and CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.md "../../../AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.md") in the _Amazon CloudFront Developer Guide_. You can also bring your own SSL certificate so viewers can connect to your CloudFront distribution over HTTPS using your own domain name, for example *https://www.mysite.com*. For more information, see the topic [Configuring Alternate Domain Names and HTTPS](../../../AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-procedures.md "../../../AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-procedures.md") in the _Amazon CloudFront Developer Guide_.

For multi-tenant distributions, HTTP method configurations follow this hierarchy:

- Template-level settings define the baseline HTTP methods allowed for all tenant distributions
- Tenant distributions can override these settings to:
  - Allow fewer methods than the multi-tenant distribution (using AWS WAF rules to block additional methods)
  - Allow more methods if the multi-tenant distribution is configured to support them

- AWS WAF rules at both multi-tenant distribution and tenant levels can further restrict HTTP methods regardless of the CloudFront configuration

## Choosing the HTTP methods that CloudFront responds to

When you create an Amazon CloudFront web distribution, you choose the HTTP methods that you want CloudFront to process and forward to your origin. You can choose from the following options:

- **`GET`, `HEAD`** – You can use CloudFront only to get objects from your origin or to get object headers.
- **`GET`, `HEAD`, `OPTIONS`** – You can use CloudFront only to get objects from your origin, get object headers, or retrieve a list of the options that your origin server supports.
- **`GET`, `HEAD`, `OPTIONS`, `PUT`, `POST`, `PATCH`, `DELETE`** – You can use CloudFront to get, add, update, and delete objects, and to get object headers. In addition, you can perform other `POST` operations such as submitting data from a web form.

You also can use AWS WAF byte match rule statements to allow or block requests based on the HTTP method, as described in [String match rule
statement](waf-rule-statement-type-string-match.md "waf-rule-statement-type-string-match.md"). If you want to use a combination of methods that CloudFront supports, such as `GET` and `HEAD`, then you don't need to configure AWS WAF to block requests that use the other methods. If you want to allow a combination of methods that CloudFront doesn't support, such as `GET`, `HEAD`, and `POST`, you can configure CloudFront to respond to all methods, and then use AWS WAF to block requests that use other methods.

For more information about choosing the methods that CloudFront responds to, see [Allowed HTTP Methods](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesAllowedHTTPMethods "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md#DownloadDistValuesAllowedHTTPMethods") in the topic [Values that You Specify When You Create or Update a Web Distribution](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md") in the _Amazon CloudFront Developer Guide_.

###### Allowed HTTP method configurations in multi-tenant distributions

For multi-tenant distributions, HTTP method configurations set at the multi-tenant distribution level apply to all tenant distributions by default. Tenant distributions can override these settings if needed.

- If you want to use a combination of methods that CloudFront supports, such as `GET` and `HEAD`, you don't need to configure AWS WAF to block requests that use other methods.
- If you want to allow a combination of methods that CloudFront doesn't support by default, such as `GET`, `HEAD`, and `POST`, you can configure CloudFront to respond to all methods, and then use AWS WAF to block requests that use other methods.

When implementing security headers in multi-tenant distributions, consider the following:

- Template-level security headers provide baseline protection across all tenant distributions
- Tenant distributions can:
  - Add new security headers not defined in the multi-tenant distribution
  - Modify values for tenant-specific headers
  - Cannot remove or override security headers set at the multi-tenant distribution level

- Consider using multi-tenant distribution-level headers for critical security controls that should apply to all tenants

## Logging considerations

Both standard and multi-tenant distributions support AWS WAF logging, but there are important differences in how logs are structured and managed:

| Logging comparison                     | Standard distributions                                                       | Multi-tenant distributions |
| -------------------------------------- | ---------------------------------------------------------------------------- | -------------------------- |
| One log configuration per distribution | Template and tenant-level logging options                                    |
| Standard log fields                    | Additional tenant identifier fields                                          |
| Single destination per distribution    | Separate destinations possible for multi-tenant distribution and tenant logs |

## Additional resources

- To learn more about multi-tenant distributions, see
  [Configure distributions](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.md")
  in the _Amazon CloudFront Developer Guide_.
- To learn more about using AWS WAF with CloudFront, see
  [Using AWS WAF protection](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.md")
  in the _Amazon CloudFront Developer Guide_.
- To learn more about AWS WAF logs, see [Log fields for protection pack (web ACL) traffic](logging-fields.md "logging-fields.md").
