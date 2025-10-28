# Cross-origin resource sharing (CORS) in Lightsail

Cross-origin resource sharing (CORS) defines a way for client web applications that are loaded in one domain to interact with resources in a different domain. With CORS support, you can build rich client-side web applications with Lightsail object storage and selectively allow cross-origin access to your bucket resources. For more information about CORS, see [What is CORS?](https://aws.amazon.com/what-is/cross-origin-resource-sharing/ "https://aws.amazon.com/what-is/cross-origin-resource-sharing/").

This section shows you how to configure CORS for your Lightsail buckets using the AWS Command Line Interface (AWS CLI). To configure your bucket to allow cross-origin requests, you add a CORS configuration to the bucket using a JSON document that defines rules identifying the origins you will allow to access your bucket, the operations (HTTP methods) supported for each origin, and other operation-specific information.

###### Topics

- [CORS use cases](#cors-use-cases "#cors-use-cases")
- [How Lightsail evaluates CORS configurations](cors-how-evaluation-works.md "cors-how-evaluation-works.md")
- [Configure CORS using the AWS CLI](cors-configuration-cli.md "cors-configuration-cli.md")
- [Troubleshooting CORS](cors-troubleshooting.md "cors-troubleshooting.md")

## CORS use cases

The following example scenario details how you might need to configure CORS with Lightsail buckets.

###### Scenario: Web font hosting

Suppose you want to host web fonts from your Lightsail bucket. Browsers require a CORS check (also called a preflight check) for loading web fonts. You would configure the bucket hosting the web font to allow any origin to make these requests.
