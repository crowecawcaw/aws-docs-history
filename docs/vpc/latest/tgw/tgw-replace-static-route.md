# Replace a static route in AWS Transit Gateway

Replace a static route in a transit gateway route table with a different static
route.

###### To replace a static route using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Choose the route that you want to replace in the route table.
4. In the details section, choose the **Routes** tab.
5. Choose **Actions**, **Replace static
   route**.
6. For the **Type**, choose either **Active**
   or **Blackhole**.
7. From the **Choose attachment** drop-down, choose the transit gateway
   that will replace the current one in the route table.
8. Choose **Replace static route**.

###### To replace a static route using the AWS CLI

Use the [replace-transit-gateway-route](../../../cli/latest/reference/ec2/replace-transit-gateway-route.md "../../../cli/latest/reference/ec2/replace-transit-gateway-route.md") command.
