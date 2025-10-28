# Redirect VPC traffic to a security appliance

The middlebox routing wizard is available in the Amazon VPC console.

###### Contents

- [1. Create routes using the
  middlebox routing wizard](#creating-routing-console "#creating-routing-console")
- [2. Modify middlebox routes](#modify-route "#modify-route")
- [3. Delete the middlebox routing wizard
  configuration](#deleting-routing-console "#deleting-routing-console")

## 1. Create routes using the

middlebox routing wizard

###### To create routes using the middlebox routing wizard

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Your VPCs**.
3. Select your VPC, and then choose **Actions**,
   **Manage middlebox routes**.
4. Choose **Create routes**.
5. On the **Specify routes** page, do the following:
   - For **Source**, choose the source for your traffic.
     If you choose a virtual private gateway, for **Destination
     IPv4 CIDR**, enter the CIDR for the on-premises traffic
     entering the VPC from the virtual private gateway.
   - For **Middlebox**, choose the network interface ID
     that is associated with your middlebox appliance, or when you use a
     Gateway Load Balancer endpoint, choose the VPC endpoint ID.
   - For **Destination subnet**, choose the destination
     subnet.

6. (Optional) To add another destination subnet, choose **Add additional
   subnet**, and then do the following:
   - For **Middlebox**, choose the network interface ID
     that is associated with your middlebox appliance, or when you use a
     Gateway Load Balancer endpoint, choose the VPC endpoint ID.

   You must use the same middlebox appliance for multiple subnets.
   - For **Destination subnet**, choose the destination
     subnet.

7. (Optional) To add another source, choose **Add source**, and
   then repeat the previous steps.
8. Choose **Next**.
9. On the **Review and create** page, verify the routes and then
   choose **Create routes**.

## 2. Modify middlebox routes

You can edit your route configuration by changing the gateway, the middlebox, or
the destination subnet.

When you make any modifications, the middlebox routing wizard automatically perform the
following operations:

- Creates new route tables for the gateway, middlebox, and destination
  subnet.
- Adds the necessary routes to the new route tables.
- Disassociates the current route tables that the middlebox routing wizard associated
  with the resources.
- Associates the new route tables that the middlebox routing wizard creates with the
  resources.

###### To modify middlebox routes using the middlebox routing wizard

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Your VPCs**.
3. Select your VPC, and then choose **Actions**,
   **Manage middlebox routes**.
4. Choose **Edit routes**.
5. To change the gateway, for **Source**, choose the gateway
   through which traffic enters your VPC. If you choose a virtual private
   gateway, for **Destination IPv4 CIDR**, enter the
   destination subnet CIDR.
6. To add another destination subnet, choose **Add additional
   subnet**, and then do the following:
   - For **Middlebox**, choose the network interface
     ID that is associated with your middlebox appliance, or when you use
     a Gateway Load Balancer endpoint, choose the VPC endpoint ID.

   You must use the same middlebox appliance for multiple
   subnets.
   - For **Destination subnet**, choose the
     destination subnet.

7. Choose **Next**.
8. On the **Review and update** page, a list of route tables
   and their routes that will be created by the middlebox routing wizard is displayed.
   Verify the routes, and then in the confirmation dialog box, choose
   **Update routes**.

## 3. Delete the middlebox routing wizard

configuration

If you decide that you no longer want the middlebox routing wizard configuration, you must
manually delete the route tables.

###### To delete the middlebox routing wizard configuration

1. View the middlebox routing wizard route tables.

After you perform the operation, the route tables that the middlebox routing wizard
created are displayed on a separate route table page. 2. Delete each route table that is displayed.
