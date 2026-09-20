

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


<table>
<thead>
  <tr><th>Parameter</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>CKN length</td><td>This is a 64 hexadecimal character (0–9, A–E) string. Use the full length to maximize cross-platform compatibility.</td></tr>
  <tr><td>CAK length</td><td>This is a 64 hexadecimal character (0–9, A–E) string. Use the full length to maximize cross-platform compatibility.</td></tr>
  <tr><td>Cryptographic algorithm</td><td>AES_256_CMAC</td></tr>
  <tr><td>SAK Cipher Suite</td><td> <ul><li> For 100 Gbps connections: GCM_AES_XPN_256  </li><li> For 10 Gbps connections: GCM_AES_XPN_256 or GCM_AES _256 </li></ul> </td></tr>
  <tr><td>Key Cipher Suite</td><td>16</td></tr>
  <tr><td>Confidentiality Offset</td><td>0</td></tr>
  <tr><td>ICV Indicator</td><td>No</td></tr>
  <tr><td>SAK Rekey Time</td><td>PN Rollover&gt;</td></tr>
</tbody>
</table>
