# Create a site using AWS Network Manager

Create a site to represent the physical location of your network. Location
information is used in the Network Manager transit gateway dashboards.

###### To create a site

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Sites**. Choose
   **Create site**.
5. For **Name** and **Description**, enter
   a name and description for the site.
6. For
   **Address**, enter the physical address of the
   site, for example, `New York, NY 10004`.
7. For **Latitude**, enter the latitude coordinates for the
   site, for example, `40.7128`.
8. For **Longitude**, enter the longitude coordinates for
   the site, for example, `-74.0060`.
9. Choose **Create site**.

###### Creating and viewing a site using the AWS CLI

Use the following commands:

- To create a site: [create-site](../../../cli/latest/reference/networkmanager/create-site.md "../../../cli/latest/reference/networkmanager/create-site.md")
- To view your sites: [get-sites](../../../cli/latest/reference/networkmanager/get-sites.md "../../../cli/latest/reference/networkmanager/get-sites.md")
