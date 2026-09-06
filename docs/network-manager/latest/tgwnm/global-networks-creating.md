

# Create a global network using AWS Network Manager
<a name="global-networks-creating"></a>

Create a global network.

**To create a global network**

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. 

   Choose **Create global network**.

1. Enter a **Name** and **Description** for your global network.

1. (Optional) In Additional settings, add **Key** and **Value** tags that further help identify an Network Manager resource. To add multiple tags, choose **Add tag** for each tag you want to add.

1. Choose **Next**.

1. To create a AWS Transit Gateway network only, clear the **Add core network in your global network** check box on the **Create global network - *optional*** page, and then choose **Next**.
**Note**  
Core networks are only used with AWS Cloud WAN. If you're creating global network for AWS Cloud WAN and want to create a core network, see [Create a core network policy](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-create-policy-console.html) in the *AWS Cloud WAN User Guide*.

1. Review the information for the global network you want to create, and then choose **Create global network**.

**To create a global network using the AWS CLI**  
Use the [create-global-network](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/create-global-network.html) command.