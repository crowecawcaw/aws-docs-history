

# Connect Customer SDK Agent API
<a name="api-reference-3P-apps-agent-client"></a>

The Connect Customer SDK provides an `AgentClient` which serves as an interface that your app in the Connect Customer agent workspace can use to subscribe to agent events and make agent data requests.

To create an `AgentClient`, pass it the `provider` that `AmazonConnectApp.init` returns. For details, see [Initialize the Connect Customer SDK in your application for Connect Customer agent workspace](getting-started-initialize-sdk.md). This is the recommended option.

```
import { AmazonConnectApp } from "@amazon-connect/app";
import { AgentClient } from "@amazon-connect/contact";

const { provider } = AmazonConnectApp.init({
  onCreate: async (event) => {
    // Your app is ready.
  },
});

const agentClient = new AgentClient(provider);
```

The constructor argument has the type `ConnectClientConfig`, which is defined as follows:

```
type ConnectClientConfig =
  | AmazonConnectProvider
  | { context: ModuleContext; provider?: AmazonConnectProvider }
  | { provider: AmazonConnectProvider };
```

You can also pass the provider inside an object, for example `new AgentClient({ provider })`.

The following sections describe API calls for working with the Agent API.

**Topics**
+ [getARN()](3P-apps-agent-requests-getarn.md)
+ [getChannelConcurrency()](3P-apps-agent-requests-getchannelconcurrency.md)
+ [getExtension()](3P-apps-agent-requests-getextension.md)
+ [getName()](3P-apps-agent-requests-getname.md)
+ [getRoutingProfile()](3P-apps-agent-requests-getroutingprofile.md)
+ [listAvailabilityStates()](3P-apps-agent-requests-listavailabilitystates.md)
+ [listQuickConnects()](3P-apps-agent-requests-listquickconnects.md)
+ [offEnabledChannelListChanged()](3P-apps-agent-requests-off-enabledchannellistchanged.md)
+ [offRoutingProfileChanged()](3P-apps-agent-requests-off-routingprofilechanged.md)
+ [onEnabledChannelListChanged()](3P-apps-agent-requests-on-enabledchannellistchanged.md)
+ [onRoutingProfileChanged()](3P-apps-agent-requests-on-routingprofile-changed.md)
+ [setAvailabilityState()](3P-apps-agent-requests-setavailabilitystate.md)
+ [setAvailabilityStateByName()](3P-apps-agent-requests-setavailabilitystatebyname.md)
+ [setOffline()](3P-apps-agent-requests-setoffline.md)
+ [getDefaultOutboundQueue()](3P-apps-agent-requests-getdefaultoutboundqueue.md)
+ [getRoutingProfileQueues()](3P-apps-agent-requests-getroutingprofilequeues.md)
+ [getAvailabilityState()](3P-apps-agent-requests-getavailabilitystate.md)
+ [listSecurityProfilePermissions()](3P-apps-agent-requests-listsecurityprofilepermissions.md)
+ [onAvailabilityStateChanged()](3P-apps-agent-events-availabilitystatechanged-sub.md)
+ [offAvailabilityStateChanged()](3P-apps-agent-events-availabilitystatechanged-unsub.md)
+ [onNextAvailabilityStateChanged()](3P-apps-agent-events-nextavailabilitystatechanged-sub.md)
+ [getNetworkConnectionStatus()](3P-apps-agent-requests-getnetworkconnectionstatus.md)
+ [onNetworkConnectionStatusChanged()](3P-apps-agent-events-networkconnectionstatuschanged-sub.md)
+ [offNetworkConnectionStatusChanged()](3P-apps-agent-events-networkconnectionstatuschanged-unsub.md)
+ [offNextAvailabilityStateChanged()](3P-apps-agent-events-nextavailabilitystatechanged-unsub.md)