# Enable Internet Access for Your Fleet in Amazon AppStream 2.0

You can enable internet access either when you create the fleet or later.

###### To enable internet access at fleet creation

1. Complete the steps in [Create a Fleet in Amazon AppStream 2.0](set-up-stacks-fleets-create.md "set-up-stacks-fleets-create.md") up to
   **Step 4: Configure Network**.
2. Choose a VPC with a NAT gateway.
3. If the subnet fields are empty, select a private subnet for
   **Subnet 1** and, optionally, another private subnet
   for **Subnet 2**. If you don't already have a private subnet in your
   VPC, you may need to create a second private subnet.
4. Continue with the steps in [Create a Fleet in Amazon AppStream 2.0](set-up-stacks-fleets-create.md "set-up-stacks-fleets-create.md").

###### To enable internet access after fleet creation by using a NAT gateway

1. In the navigation pane, choose **Fleets**.
2. Select a fleet and verify that the state is
   **Stopped**.
3. Choose **Fleet Details**, **Edit**, and
   choose a VPC with a NAT gateway.
4. Choose a private subnet for **Subnet 1** and, optionally,
   another private subnet for **Subnet 2**. If you don't already have a private subnet in your
   VPC, you may need to [create a second private subnet](create-configure-new-vpc-with-private-public-subnets-nat.md#vpc-with-private-and-public-subnets-add-private-subnet-nat "create-configure-new-vpc-with-private-public-subnets-nat.md#vpc-with-private-and-public-subnets-add-private-subnet-nat").
5. Choose **Update**.
   You can test your internet connectivity by starting your fleet, and then
   connecting to your streaming instance and browsing to the internet.
