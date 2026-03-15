# Configure cross-account access in Global Accelerator

By using cross-account support, you can use AWS Global Accelerator as a fixed entry point to your application that accesses
resources in multiple accounts, or choose IP addresses for your accelerator from shared CIDR blocks.
Using cross-account permissions for allowing access to resources in different
accounts is an AWS best practice. With cross-account support for bring your own IP (BYOIP) address CIDR
blocks, you can use the same address pool for accelerators in different accounts in your organization. You can
also organize AWS resources under one account that controls internet access to your applications, which can
simplify monitoring and security, as well as provide visibility to inbound connections.

Cross-account support in Global Accelerator enables you to do the following:

- Add endpoints, such as Network Load Balancers, from other accounts to an accelerator.
- Choose a BYOIP address pool for IP addresses, and then select IP addresses from the
  pool for accelerators in different accounts. By sharing a BYOIP address pool, you can use more addresses from
  the same CIDR block, reducing the number of CIDR blocks that you require.
  You can work with cross-account attachments and resources in the Global Accelerator console, or by using Global Accelerator API operations
  with the AWS Command Line Interface (AWS CLI) or an AWS SDK. For example, as a principal, you can use the
  [UpdateEndpoints](../api/API_AddEndpoints.md "../api/API_AddEndpoints.md")
  operation to add a cross-account resource as an endpoint for an accelerator. When you use the API operation, you specify
  the cross-account attachment ARN and the endpoint ID. For more information, see the
  [AWS Global Accelerator API Reference Guide](../api/Welcome.md "../api/Welcome.md").

###### Contents

- [How cross-account works](cross-account-resources.md "cross-account-resources.md")
- [Work with cross-account attachments](cross-account-resources.md "cross-account-resources.md")
- [Work with cross-account resources](cross-account-resources.md "cross-account-resources.md")
- [Identify cross-account resources](cross-account-resources.md "cross-account-resources.md")
- [Responsibilities and permissions](cross-account-resources-endpoints.md "cross-account-resources-endpoints.md")
- [Billing costs](cross-account-resources-endpoints.md "cross-account-resources-endpoints.md")
- [Quotas](cross-account-resources-endpoints.md "cross-account-resources-endpoints.md")
