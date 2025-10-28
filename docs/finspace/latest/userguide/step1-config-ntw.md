After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Step 1: Configuring a network connection to create FinSpace VPC transit gateway attachment

###### To create a network connection

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, under **Network** tab, choose **Add
   network configuration**.
5. On **Add network configuration** page, enter a transit gateway ID and the CIDR range that will be used for the subnets connecting to your internal network. For more information, see the [_Amazon VPC Transit Gateways User Guide_.](../../../vpc/latest/tgw/tgw-transit-gateways.md#create-tgw "../../../vpc/latest/tgw/tgw-transit-gateways.md#create-tgw")

###### Note

When you add a transit gateway without creating a network ACL, all outbound traffic is allowed by default. 6. (Optional) Add rules to define how you want to manage the outbound traffic from kdb network to
your internal network. Choose **Add new rule** to allow or
deny outbound traffic for each port range and destination.

###### Note

    * When you create a network ACL rule, by default all the other traffic are
     denied.
    * We process the ACL rules according to the rule numbers, in ascending order.

7. Choose **Save**. The connection creation process begins and the environment
   details page opens from where you can check the status under the
   **Network** tab.

###### Note

- When you configure a network connection, make sure that you have a /26 (64) IP
  address range from the _100.64.0.0/10_ range. The CIDR range should
  not be used in your network or any other environments that are connected by this TGW. A
  few valid examples of this CIDR range are _100.64.0.0/26_,
  _100.64.1.0/26_, _100.64.2.0/26_,
  _100.64.3.0/26_. We will pick _100.64.0.0/26_
  for this tutorial.
- This step creates a transit gateway VPC attachment to connect FinSpace environment to
  the transit gateway. After you configure a network, check the
  **Network** tab for details of your network.
