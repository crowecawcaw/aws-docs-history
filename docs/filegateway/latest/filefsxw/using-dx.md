Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Using AWS Direct Connect with Storage Gateway

AWS Direct Connect links your internal network to the Amazon Web Services Cloud. By using AWS Direct Connect with
Storage Gateway, you can create a connection for high-throughput workload needs, providing a
dedicated network connection between your on-premises gateway and AWS.

Storage Gateway uses public endpoints. With an AWS Direct Connect connection in place, you can create a
public virtual interface to allow traffic to be routed to the Storage Gateway endpoints. The
public virtual interface bypasses internet service providers in your network path. The
Storage Gateway service public endpoint can be in the same AWS Region as the AWS Direct Connect
location, or it can be in a different AWS Region.

The following illustration shows an example of how AWS Direct Connect works with
Storage Gateway.

![network architecture showing Storage Gateway connected to the cloud using AWS direct connect.](images/DirectConnect3.png)
The following procedure assumes that you have created a functioning gateway.

###### To use AWS Direct Connect with Storage Gateway

1. Create and establish an AWS Direct Connect connection between your on-premises data
   center and your Storage Gateway endpoint. For more information about how to create a
   connection, see [Getting Started
   with AWS Direct Connect](../../../directconnect/latest/UserGuide/getting_started.md "../../../directconnect/latest/UserGuide/getting_started.md") in the _AWS Direct Connect User Guide._
2. Connect your on-premises Storage Gateway appliance to the AWS Direct Connect router.
3. Create a public virtual interface, and configure your on-premises router
   accordingly. For more information, see [Creating a Virtual Interface](../../../directconnect/latest/UserGuide/create-vif.md "../../../directconnect/latest/UserGuide/create-vif.md") in the _AWS Direct Connect User Guide._
   For details about AWS Direct Connect, see [What is
   AWS Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") in the _AWS Direct Connect User Guide_.
