

# Download the Direct Connect router configuration file
<a name="vif-router-config"></a>

After you create the virtual interface and the interface state is up, you can download the router configuration file for your router.

If you use any of the following routers for virtual interfaces that have MACsec turned on, we automatically create the configuration file for your router:
+ Cisco Nexus 9K\+ Series switches running NX-OS 9.3 or later software
+ Juniper Networks M/MX Series Routers running JunOS 9.5 or later software

**To download the router configuration file**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1. Select the virtual interface and then choose **View details**.

1. Choose **Download router configuration**.

1. For **Download router configuration**, do the following:

   1. For **Vendor**, select the manufacturer of your router.

   1. For **Platform**, select the model of your router.

   1. For **Software**, select the software version for your router.

1. Choose **Download**, and then use the appropriate configuration for your router to ensure that you can connect to Direct Connect.

1. If you need to manually configure your router for MACsec, use the following table as a guideline.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/directconnect/latest/UserGuide/vif-router-config.html)