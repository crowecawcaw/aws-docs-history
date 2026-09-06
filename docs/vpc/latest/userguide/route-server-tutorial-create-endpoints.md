

# Step 4: Create route server endpoints
<a name="route-server-tutorial-create-endpoints"></a>

Complete the steps in this section to create route server endpoints. Create two endpoints per subnet for redundancy.

A route server endpoint is an AWS-managed component inside a subnet that helps [BGP (Border Gateway Protocol)](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) connections between your route server and your BGP peers. 

Route server endpoints are the "contact points" where your network devices establish BGP sessions with the route server. They're the components that actually handle the BGP connections, while the route server itself manages the routing decisions and route propagation.

**Note**  
Route server endpoints are charged $0.75 per hour.

------
#### [ AWS Management Console ]

**To create route server endpoints**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Virtual private cloud**, choose **Route servers**.

1. Select the route server for which you want to create endpoints.

1. In the lower pane, choose the **Route server endpoints** tab.

1. Choose **Create route server endpoint**.

1. On the **Create route server endpoint** page, configure the following settings:
   + For **Name**, enter a descriptive name for your endpoint.
   + For **Route server**, confirm that the correct route server is selected.
   + For **Subnet**, select the subnet in which you want to create the endpoint.

1. (Optional) To add tags to your route server endpoint, scroll down to the **Tags - optional** section and choose **Add new tag**. Enter a key and an optional value for each tag.

1. Review your settings and choose **Create route server endpoint**.

1. Wait for the endpoint to be created. Once complete, you will see a success message.

1. Repeat steps 5-9 to create a second endpoint in the same subnet, using a different name.

1. Repeat steps 5-10 for each subnet where you need route server endpoints.

1. After creating the endpoints, return to the **Route server endpoints** tab for your route server.

1. Verify that you see two endpoints listed for each subnet.

1. Check that the **State** for each endpoint is *Available*.

------
#### [ Command line ]

Use the following procedure to create a route server endpoint.

1. Command:

   ```
   aws ec2 create-route-server-endpoint --route-server-id rs-1 --subnet-id subnet-1
   ```

   Response:

   ```
   {
       "RouteServerEndpoint": {
           "RouteServerId": "rs-1",
           "RouteServerEndpointId": "rse-1",
           "VpcId": "vpc-1",
           "SubnetId": "subnet-1",
           "State": "pending"
       }
   }
   ```

1. You may need to wait a few minutes for the endpoints to become fully available after creation.

   Command:

   ```
   aws ec2 describe-route-server-endpoints
   ```

   Response:

   ```
   {
       "RouteServerEndpoint": {
           "RouteServerId": "rs-1",
           "RouteServerEndpointId": "rse-1",
           "VpcId": "vpc-1",
           "SubnetId": "subnet-1",
           "EniId": "eni-123",
           "EniAddress": "10.1.2.3",
           "State": "available"
       }
   }
   ```

Repeat the steps to create a second endpoint in the same subnet using a different name and create endpoints for each subnet where you need route server endpoints.

------