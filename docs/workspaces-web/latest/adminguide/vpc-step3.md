# Adding a second private subnet

In the previous step, you created a VPC with one public subnet and one private
subnet. Complete the following steps to add a second private subnet to your VPC. We
recommend that you add a second private subnet in a different Availability Zone than
your first private subnet.

###### To add a second private subnet

1. In the navigation pane, choose **Subnets**.
2. Select the first private subnet that you created in the previous step. On the
   **Description** tab, below the list of subnets, make a note of
   the Availability Zone for this subnet.
3. On the upper left of the subnets pane, choose **Create
   Subnet**.
4. For **Name tag**, enter a name for the private subnet. For
   example, `WorkSpaces Secure Browser Private Subnet2`.
5. For **VPC**, select the VPC that you created in the previous
   step.
6. For **Availability Zone**, select an Availability Zone other
   than the one you're using for your first private subnet. Selecting a different
   Availability Zone increases fault tolerance and helps prevent insufficient capacity
   errors.
7. For **IPv4 CIDR block**, specify a unique CIDR block range for
   the new subnet. For example, if your first private subnet has an IPv4 CIDR block
   range of `10.0.1.0/24`, you could specify a CIDR block range of
   `10.0.2.0/24` for the second private subnet.
8. Choose **Create**.
9. After your subnet is created, choose **Close**.
