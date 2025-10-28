# Associating an IP access setting with a web portal in Amazon WorkSpaces Secure Browser

###### Important

IP access controls only support IPv4. Users connecting from IPv6-only networks will be blocked.

To associate an IP access control group with an existing web portal, follow these
steps.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/ "https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/").
2. In the navigation pane, choose **Web portals**.
3. Select the web portal, and choose **Edit**.
4. Under **IP access control group,** and select the IP access control
   groups for the web portal.
5. Choose **Save**.
   To associate an IP access control group when creating a new web portal, follow these steps.

6. Complete steps 1 through 4 in [Configuring portal settings for Amazon WorkSpaces Secure Browser](portal-settings.md "portal-settings.md") to access **IP
   Access Control (optional)**.
7. Choose **Create IP access controls**.
8. In the **Create IP Group** dialog box, enter a name (required) and
   description (optional) for the group.
9. Enter the IP address or CIDR IP range that will be associated to
   **Source**, and a **Description** (optional).
10. Under **Tags**, choose whether to tag a key value pair for each IP
    access control group.
11. When you are done adding rules and tags, choose **Create IP access
    control**.
12. Your IP access control group will be associated to this web portal when launched.
