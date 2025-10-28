# Use Agent Workspace to optimize audio for

Citrix, Amazon WorkSpaces, and Omnissa cloud desktops

You can use Amazon Connect Agent Workspace to simplify the delivery of high-quality voice
experiences in Amazon WorkSpaces, Citrix, and Omnissa Virtual Desktop Infrastructure (VDI)
environments.

Amazon Connect supports [audio optimization for
Amazon WorkSpaces](using-ccp-vdi-workspaces.md "using-ccp-vdi-workspaces.md"), [Citrix](using-ccp-vdi-citrix-step-by-step.md "using-ccp-vdi-citrix-step-by-step.md"), and [Omnissa](using-ccp-vdi-omnissa-step-by-step.md "using-ccp-vdi-omnissa-step-by-step.md") cloud desktops. This optimization redirects media from an
agent's local desktop to Amazon Connect. It streamlines the agent experience and improves
audio quality by reducing network hops. Your agents can leverage these audio
optimizations in the agent workspace.

## Important things to

know

- For non SSO users, if the agents navigate to Agent Workspace from the
  Amazon Connect admin website, there will be a query parameter for referrer already appended to
  the URL. The format of the URL is
  `https://`your-instance-url`/agent-app-v2?referrer=admin`.
  To form the VDI platform query parameter, remove the referrer parameter
  from the URL (for example, you can use Notepad to edit the URL). Append
  the VDI platform parameter directly to the `/agent-app-v2`
  path of the URL.
- For audio optimization inside the VDI environment, always use the
  bookmarked URL for the agent workspace.
- If you are not using the agent workspace inside an actual VDI
  environment, do not append the VDI query parameter.
- We recommend that agents stay with one media device during an ongoing
  contact within VDI environments. Because the media device information is
  relayed at the start of a contact, if an agent were to switch media
  devices during an ongoing contact, they would not be able to access
  audio in the updated device.

## How to use audio optimization in

Agent Workspace

To use audio optimization in Agent Workspace, users need to have a query
parameter in the URL with a value for the VDI environment in which the agent
workspace is used. This process signals the Contact Control Panel (CCP) to
perform WebRTC redirection for the calls from that specific VDI environment to
the local device being used by the agent.

Complete the following steps to use a query parameter for the VDI
environment.

### Use without SSO based login

1. Go to your Amazon Connect Agent Workspace, and copy the URL for the agent
   workspace to Notepad.
2. Append a query parameter with the key `VDIPlatform` and
   the value equal to the specific VDI environment you have. For
   example:
   1. For Citrix cloud desktop, the value for the query
      parameter is `CITRIX`. The following code shows
      an example of the complete URL:
      - `https://`your-instance-url`/agent-app-v2?VDIPlatform=CITRIX`

   2. For Amazon WorkSpaces cloud desktop, the value for the query
      parameter is `AWS_WORKSPACE`. The following code
      shows an example of the complete URL:
      - `https://`your-instance-url`/agent-app-v2?VDIPlatform=AWS_WORKSPACE`

   3. For Omnissa cloud desktop, the value for the query
      parameter is `OMNISSA`. The following code shows
      an example of the complete URL:
      - `https://`your-instance-url`/agent-app-v2?VDIPlatform=OMNISSA`

3. Copy and paste the URL into the agent's browser.
4. We recommend bookmarking this URL for all the agents. This makes
   it easy for agents access it in future by just clicking the
   bookmarked link.

### Use with SSO based login

1. If you use SSO to directly login into Amazon Connect Agent Workspace, you
   need to change the relay state URL of your SSO setup to append the
   VDI query parameter. Complete the following steps to do this:
   1. Copy and paste the relay state you are using to access the
      agent workspace in the relay state of your Identity Provider
      (IdP).
   2. See [examples of relay
      state URLs](configure-saml.md#destination-relay "configure-saml.md#destination-relay"). In the examples,
      `%2Fagent-app-v2` is the destination.
   3. Add the `VDIPlatform` parameter with the
      appropriate value to this relay state. Using the example
      from the above link, the complete relay state URL for the
      Amazon Connect agent workspace would look like the following:
      1. In Citrix Desktop

      `https://us-east-1.console.aws.amazon.com/connect/federate/instance-id?destination=%2Fagent-app-v2?VDIPlatform=CITRIX` 2. In Amazon WorkSpaces

      `https://us-east-1.console.aws.amazon.com/connect/federate/instance-id?destination=%2Fagent-app-v2?VDIPlatform=AWS_WORKSPACE` 3. In Omnissa

      `https://us-east-1.console.aws.amazon.com/connect/federate/instance-id?destination=%2Fagent-app-v2?VDIPlatform=OMNISSA`

2. Setting `VDIPlatform` in relay state URL automatically
   sets the audio optimization in Agent Workspace for the specific VDI
   environment being used.
   1. Log in from your IdP, and confirm that
      `VDIPlatform` is present as a query
      parameter.
