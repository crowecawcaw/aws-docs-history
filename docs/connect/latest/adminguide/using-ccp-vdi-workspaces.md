

# Optimize Connect Customer audio for Amazon WorkSpaces cloud desktops
<a name="using-ccp-vdi-workspaces"></a>

Connect Customer simplifies delivery of high-quality voice experiences for agents operating within Amazon WorkSpaces Virtual Desktop Infrastructure (VDI) environments. By using Amazon WorkSpaces with the WebRTC redirection feature, agents can redirect Connect Customer audio processing to their local devices. This approach results in enhanced audio quality, even over challenging network conditions. To take advantage of this feature, you need to do the following:
+ Use [Connect Customer open source libraries](https://github.com/amazon-connect/amazon-connect-streams) to create a new or update an existing agent user interface, such as a custom Contact Control Panel (CCP). 
+ Configure Amazon WorkSpaces to enable WebRTC redirection.

## System requirements
<a name="using-ccp-vdi-citrix-step-by-step-requirements"></a>

This section describes the system requirements for using Connect Customer with WorkSpaces WebRTC redirection.
+ **WorkSpaces Protocol**

  WorkSpaces needs to use Amazon DCV. For more information, see [What Is Amazon DCV?](https://docs.aws.amazon.com/dcv/latest/adminguide/what-is-dcv.html). 
+ **Client version**

  Users should use WorkSpaces Web Access or WorkSpaces Windows client version 5.21.0 or higher. Complete the [Setup and installation](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-windows-client.html#windows_setup) instructions. 
+ **Group policy**

  WebRTC redirection needs to be enabled in the DCV group policy. In the topic [Manage Group Policy settings for DCV](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#gp_configurations_dcv), open the collapsed section titled **Enable or disable WebRTC redirection for DCV** and complete those instructions.
+ **Networking/firewall configurations**
  + **Workspace VDI configuration**

    The admin needs to allow the Workspaces to access Connect Customer TCP/443 traffic to the domains mentioned in the following diagram. For more information, see [Set up your network](ccp-networking.md).
  + **Agent machine configuration**

    This solution requires a media connection between the agent thin client to Connect Customer. To allow traffic between the agent's machine and Connect Customer Softphone Media UDP Port 3478, see [Set up your network](ccp-networking.md).  
![Workspace VDI and agent machine firewall settings.](http://docs.aws.amazon.com/connect/latest/adminguide/images/vdi-workspaces.png)
+ **Unsupported CCP Deployment**
  + Native CCP

## Confirm media flows between agent machine and Connect Customer during the call
<a name="using-ccp-vdi-citrix-confirm-media-flow"></a>
+ Ensure DCV WebRTC browser extension is enabled and in Ready state.