

# Create a site in an AWS Cloud WAN global network
<a name="cloudwan-sites-add"></a>

A site represents the physical location of your network, using location information that you provide. Sites you add to your Cloud WAN global network appear in the geographical map of a Cloud WAN global network dashboard.

**To create a site**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Sites**.

1. Choose **Create site**.

1. For **Name** and **Description**, enter a name and description for the site. 

1. For **Address**, enter the physical address of the site, for example, New York, NY 10004. 

1. For **Latitude**, enter the latitude coordinates for the site (for example, `40.7128`). 

1. For **Longitude**, enter the longitude coordinates for the site (for example, `-74.0060`). 

1. (Optional) Under **Additional settings**, add one or more **Key** and **Value** tags to help identify this site.

1. Choose **Create site**. 

   Sites are created immediately and can be viewed on the global network dashboard. For more information on viewing sites on your global network dashboard, see [Access AWS Cloud WAN global network dashboards](cloudwan-visualize-networks-global.md).