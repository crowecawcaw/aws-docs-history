Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Testing your gateway's

network connectivity

You can use your gateway's local console to test your network connectivity. This test
can be useful when you are troubleshooting network issues with your gateway.

###### To test your gateway's connectivity

1. Log in to your gateway's local console. For instructions, see [Logging in to your Amazon EC2 gateway
   local console](EC2_MaintenanceConsoleWindow-fgw.md "EC2_MaintenanceConsoleWindow-fgw.md").
2. From the **AWS Appliance Activation - Configuration** main
   menu, enter the corresponding numeral to select **Test Network
   Connectivity**.

If your gateway has already been activated, the connectivity test begins
immediately. For gateways that have not yet been activated, you must specify the
endpoint type and AWS Region as described in the following steps. 3. If your gateway is not yet activated, enter the corresponding numeral to
select the endpoint type for your gateway. 4. If you selected the public endpoint type, enter the corresponding numeral to
select the AWS Region that you want to test. For supported AWS Regions and a
list of AWS service endpoints you can use with Storage Gateway, see [AWS Storage Gateway endpoints
and quotas](../../../general/latest/gr/sg.md "../../../general/latest/gr/sg.md") in the _AWS General Reference_.
As the test progresses, each endpoint displays either **[PASSED]** or
**[FAILED]**, indicating the status of the connection as
follows:

| Message      | Description                                         |
| ------------ | --------------------------------------------------- |
| **[PASSED]** | Storage Gateway has network connectivity.           |
| **[FAILED]** | Storage Gateway does not have network connectivity. |
