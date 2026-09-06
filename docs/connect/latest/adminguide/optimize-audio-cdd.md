

# Use the agent workspace to optimize audio for Amazon WorkSpaces, Citrix, Omnissa, Azure Virtual Desktop, and Windows 365 cloud desktops
<a name="optimize-audio-cdd"></a>

You can use the Connect Customer agent workspace to simplify the delivery of high-quality voice experiences in Amazon WorkSpaces, Citrix, Omnissa, Azure Virtual Desktop, and Windows 365 Virtual Desktop Infrastructure (VDI) environments. 

Connect Customer supports [audio optimization for Amazon WorkSpaces](using-ccp-vdi-workspaces.md), [Citrix](using-ccp-vdi-citrix-step-by-step.md), [Omnissa](using-ccp-vdi-omnissa-step-by-step.md), and [Azure Virtual Desktop and Windows 365](using-ccp-vdi-azure-step-by-step.md) cloud desktops. This optimization redirects media from an agent's local desktop to Connect Customer. It streamlines the agent experience and improves audio quality by reducing network hops. Your agents can use these audio optimizations in the agent workspace.

## Important things to know
<a name="optimize-audio-cdd-important-notes"></a>
+ For non SSO users, if the agents navigate to the agent workspace from the Connect Customer admin website, there will be a query parameter for referrer already appended to the URL. The format of the URL is `https://{{your-instance-url}}/agent-app-v2?referrer=admin`. To form the VDI platform query parameter, remove the referrer parameter from the URL (for example, you can use Notepad to edit the URL). Append the VDI platform parameter directly to the `/agent-app-v2` path of the URL.
+ For audio optimization inside the VDI environment, always use the bookmarked URL for the agent workspace.
+ If you are not using the agent workspace inside an actual VDI environment, do not append the VDI query parameter.
+ We recommend that agents stay with one media device during an ongoing contact within VDI environments. Because the media device information is relayed at the start of a contact, if an agent were to switch media devices during an ongoing contact, they would not be able to access audio in the updated device.

## How to use audio optimization in the agent workspace
<a name="howto-optimize-audio-cdd"></a>

To use audio optimization in the agent workspace, users need to have a query parameter in the URL with a value for the VDI environment in which the agent workspace is used. This process signals the Contact Control Panel (CCP) to perform WebRTC redirection for the calls from that specific VDI environment to the local device being used by the agent.

Complete the following steps to use a query parameter for the VDI environment.

### Use without SSO based login
<a name="without-sso"></a>

1. Go to the Connect Customer agent workspace, and copy the URL for the agent workspace to Notepad.

1. Append a query parameter with the key `VDIPlatform` and the value equal to the specific VDI environment you have. For example:

   1. For Citrix cloud desktop, the value for the query parameter is `CITRIX_413`. The following code shows an example of the complete URL: 
      + `https://{{your-instance-url}}/agent-app-v2?VDIPlatform=CITRIX_413`

   1. For Amazon WorkSpaces cloud desktop, the value for the query parameter is `AWS_WORKSPACE`. The following code shows an example of the complete URL:
      + `https://{{your-instance-url}}/agent-app-v2?VDIPlatform=AWS_WORKSPACE`

   1. For Omnissa cloud desktop, the value for the query parameter is `OMNISSA`. The following code shows an example of the complete URL:
      + `https://{{your-instance-url}}/agent-app-v2?VDIPlatform=OMNISSA`

   1. For Azure Virtual Desktop or Windows 365 cloud desktop, the value for the query parameter is `AZURE`. The following code shows an example of the complete URL:
      + `https://{{your-instance-url}}/agent-app-v2?VDIPlatform=AZURE`

1. Copy and paste the URL into the agent's browser. 

1. We recommend bookmarking this URL for all the agents. This makes it easy for agents access it in future by just choosing the bookmarked link.

### Use with SSO based login
<a name="with-sso"></a>

1. If you use SSO to directly login into the Connect Customer agent workspace, you need to change the relay state URL of your SSO setup to append the VDI query parameter. Complete the following steps to do this:

   1. Copy and paste the relay state you are using to access the agent workspace in the relay state of your Identity Provider (IdP). 

   1. See [examples of relay state URLs](configure-saml.md#destination-relay). In the examples, ``%2Fagent-app-v2`` is the destination. 

   1. Add the `VDIPlatform` parameter with the appropriate value to this relay state. Using the example from the preceding link, the complete relay state URL for the Connect Customer agent workspace would look like the following:

      1. In Citrix Desktop

         `https://us-east-1.console.aws.amazon.com/connect/federate/instance-id?destination=%2Fagent-app-v2?VDIPlatform=CITRIX_413`

      1. In Amazon WorkSpaces

         `https://us-east-1.console.aws.amazon.com/connect/federate/instance-id?destination=%2Fagent-app-v2?VDIPlatform=AWS_WORKSPACE`

      1. In Omnissa

         `https://us-east-1.console.aws.amazon.com/connect/federate/instance-id?destination=%2Fagent-app-v2?VDIPlatform=OMNISSA`

      1. In Azure Virtual Desktop or Windows 365

         `https://us-east-1.console.aws.amazon.com/connect/federate/instance-id?destination=%2Fagent-app-v2?VDIPlatform=AZURE`

1. Setting `VDIPlatform` in relay state URL automatically sets the audio optimization in the agent workspace for the specific VDI environment being used.

   1. Log in from your IdP, and confirm that ``VDIPlatform`` is present as a query parameter.