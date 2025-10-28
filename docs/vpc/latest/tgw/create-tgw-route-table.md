# Create a transit gateway route table in AWS Transit Gateway

###### To create a transit gateway route table using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Choose **Create transit gateway route table**.
4. (Optional) For **Name tag**, type a name for the transit gateway route table.
   This creates a tag with the tag key "Name", where the tag value is the name that you
   specify.
5. For **Transit gateway ID**, select the transit gateway for the route
   table.
6. Choose **Create transit gateway route table**.

###### To create a transit gateway route table using the AWS CLI

Use the [create-transit-gateway-route-table](../../../cli/latest/reference/ec2/create-transit-gateway-route-table.md "../../../cli/latest/reference/ec2/create-transit-gateway-route-table.md") command.
