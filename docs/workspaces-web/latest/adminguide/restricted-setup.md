# HTTP outbound proxy for Amazon WorkSpaces Secure Browser

To set up an HTTP outbound proxy for WorkSpaces Secure Browser, follow these steps.

1. To deploy an example outbound proxy to your VPC, follow the steps in [How to set up an outbound VPC proxy with domain whitelisting and content
   filtering](https://aws.amazon.com/blogs/security/how-to-set-up-an-outbound-vpc-proxy-with-domain-whitelisting-and-content-filtering/ "https://aws.amazon.com/blogs/security/how-to-set-up-an-outbound-vpc-proxy-with-domain-whitelisting-and-content-filtering/").
   1. Follow the steps in "Installation (one-time setup)" to deploy the CloudFormation
      template to your account. Make sure to choose the right VPC and subnets as the
      CloudFormation template parameters.
   2. After deployment, find the CloudFormation output parameter
      **OutboundProxyDomain** and
      **OutboundProxyPort**. This is your proxy’s DNS name and
      port.
   3. If you already have your own proxy, skip this step and use your proxy’s DNS
      name and port.

2. In the WorkSpaces Secure Browser, console, select your portal and then choose
   **Edit**.
   1. In the **Network connection details**, choose the VPC and
      private subnets that have access to the proxy.
   2. In the **Policy settings**, add the following ProxySettings
      policy by using a JSON editor. The `ProxyServer` field should be your
      proxy’s DNS name and port. For more details about ProxySettings policy, see
      [ProxySettings](https://chromeenterprise.google/policies/#ProxySettings "https://chromeenterprise.google/policies/#ProxySettings").

   ```
   {
       "chromePolicies":
       {
           ...
           "ProxySettings": {
               "value": {
                   "ProxyMode": "fixed_servers",
                   "ProxyServer": "OutboundProxyLoadBalancer-0a01409a46943c47.elb.us-west-2.amazonaws.com:3128",
                   "ProxyBypassList": "https://www.example1.com,https://www.example2.com,https://internalsite/"
               }
           },
       }
   }
   ```

3. In your WorkSpaces Secure Browser session, you will see the proxy is applied to Chrome setting
   **Chrome is using proxy settings from your
   administrator**.
4. Go to chrome://policy and the **Chrome policy** tab to confirm
   that the policy is applied.
5. Verify that your WorkSpaces Secure Browser session can successfully browse internet content without
   NAT gateway. In the CloudWatch Logs, verify that Squid proxy access logs are recorded.
