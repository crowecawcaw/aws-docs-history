# Create an Interface Endpoint to Access WorkSpaces Applications API Operations and CLI Commands

Perform the following steps to create an interface endpoint.

1.  Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2.  In the navigation pane, choose **Endpoints**, **Create Endpoint**.
3.  Choose **Create Endpoint**.
4.  For **Service category**, ensure that **AWS services** is selected.
5.  For **Service Name**, choose `com.amazonaws.``<AWS Region>``.appstream.api`.
6.  Specify the following information. When you're done, choose **Create endpoint**.

        * For **VPC**, select a VPC in which to create the interface endpoint.
        * For **Subnets**, select the subnets (Availability Zones) in which to create the endpoint network interfaces. We recommend that you choose subnets in at least two Availability Zones.
        * Optionally, you can select the **Enable Private DNS Name** check box.


        ###### Note

        If you select this option, ensure that you configure VPC and DNS as needed to support private DNS. For more information, see [Private DNS](../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns "../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns") in the *Amazon VPC User Guide*.
        * For **Security group**, select the security groups to associate with the endpoint network interfaces.


        ###### Note

        The security groups must provide inbound access to the ports from the IP address range from which your users connect.

    While your interface endpoint is being created, the status of the endpoint in the console
    appears as **Pending**. After your endpoint is created, the
    status changes to **Available.**
