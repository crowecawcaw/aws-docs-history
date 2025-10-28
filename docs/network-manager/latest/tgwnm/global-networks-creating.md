# Create a global network using AWS Network Manager

Create a global network.

###### To create a global network

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global
   Networks**.
3. Choose **Create global network**.
4. Enter a **Name** and **Description** for
   your global network.
5. (Optional) In Additional settings, add **Key** and
   **Value** tags that further help identify an Network
   Manager resource. To add multiple tags, choose **Add tag**
   for each tag you want to add.
6. Choose **Next**.
7. To create a AWS Transit Gateway network only, clear the **Add core network in
   your global network** check box on the **Create global
   network - _optional_** page, and then choose
   **Next**.

###### Note

Core networks are only used with AWS Cloud WAN. If you're creating global network for AWS Cloud WAN
and want to create a core network, see [Create a core network policy](../cloudwan/cloudwan-create-policy-console.md "../cloudwan/cloudwan-create-policy-console.md")
in the _AWS Cloud WAN User Guide_. 8. Review the information for the global network you want to create, and then choose
**Create global network**.

###### To create a global network using the AWS CLI

Use the [create-global-network](../../../cli/latest/reference/networkmanager/create-global-network.md "../../../cli/latest/reference/networkmanager/create-global-network.md") command.
