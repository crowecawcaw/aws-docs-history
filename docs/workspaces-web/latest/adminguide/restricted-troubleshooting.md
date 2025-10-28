# Troubleshooting restricted internet browsing for Amazon WorkSpaces Secure Browser

After Chrome policy is applied, if your WorkSpaces Secure Browser session still can't access the
internet, follow these steps to try to resolve your issue:

- Verify that the proxy endpoint is accessible from the private subnets where your
  WorkSpaces Secure Browser portal lives. To do you this, create an EC2 instance in the private subnet,
  and test the connection from the private EC2 instance to your proxy endpoint.
- Verify that the proxy has internet access.
- Verify that the Chrome policy is correct.
  - Confirm the following formatting for the `ProxyServer` field of
    the policy: `<Proxy DNS name>:<Proxy port>`. There should be no
    `http://` or `https://` in the prefix.
  - In the WorkSpaces Secure Browser session, use Chrome to navigate to chrome://policy, and make
    sure that the ProxySettings policy is successfully applied.
