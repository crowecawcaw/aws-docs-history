After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Step 4: Configuring routes in your VPC route

tables

With a VPC, you must create routes to send traffic to the transit gateway. The following
steps show how you can update your default VPC route tables to have an entry for traffic to
return to FinSpace VPC.

###### To configure route tables

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Route Tables**.
3. Choose the route table for the default VPC ID.
4. Choose **Edit routes**.
5. On **Edit routes** page, choose **Add route** and
   enter _100.64.0.0/26_ as the **Destination**. This value
   is the same as the CIDR range that you added while creating the network connectivity in
   [Step 1: Configuring a network connection to create FinSpace VPC transit gateway attachment](step1-config-ntw.md "step1-config-ntw.md").
6. For **Target** choose **Transit Gateway** and select
   your transit gateway ID.
7. Choose **Save changes**.
