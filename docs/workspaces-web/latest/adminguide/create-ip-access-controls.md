

# Creating an IP access control group in Amazon WorkSpaces Secure Browser
<a name="create-ip-access-controls"></a>

**Important**  
IP access controls only support IPv4. Users connecting from IPv6-only networks will be blocked.

To create an IP access control group, follow these steps.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/).

1. In the navigation pane, choose **IP access controls**.

1. Choose **Create IP access control group**.

1. In the **Create IP access control group** dialog box, enter a name (required) and description (optional) for the group. 

1. Enter the IP address or CIDR IP range that will be associated to **Source**, and a **Description** (optional). 

1. Under **Tags**, choose whether to tag a key value pair for each IP access control group.

1. When you are done adding rules and tags, choose **Save**.