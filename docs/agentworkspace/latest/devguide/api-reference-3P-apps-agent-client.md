# Amazon Connect Agent Workspace Agent API

The Amazon Connect SDK provides an `AgentClient` which serves as an interface that your app in the
Amazon Connect agent workspace can use to subscribe to agent events and make agent data requests.

The `AgentClient` accepts an optional constructor argument, `ConnectClientConfig` which itself is defined as:

```

export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};

```

If you do not provide a value for this config, then the client will default to using the **AmazonConnectProvider** set in the global provider scope. You can also manually
configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```

import { AgentClient } from "@amazon-connect/contact";

const agentClient = new AgentClient({ provider });

```

###### Note

You must first instantiate the [AmazonConnectApp](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which initializes the default AmazonConnectProvider and returns `{ provider }` . This is the recommended option.

Alternatively, providing a constructor argument:

```

import { AgentClient } from "@amazon-connect/contact";

const agentClient = new AgentClient({
    context: sampleContext,
    provider: sampleProvider
});

```

The following sections describe API calls for working with the Agent API.

###### Contents

- [getARN()](3P-apps-agent-requests-getarn.md "3P-apps-agent-requests-getarn.md")
- [getChannelConcurrency()](3P-apps-agent-requests-getchannelconcurrency.md "3P-apps-agent-requests-getchannelconcurrency.md")
- [getExtension()](3P-apps-agent-requests-getextension.md "3P-apps-agent-requests-getextension.md")
- [getName()](3P-apps-agent-requests-getname.md "3P-apps-agent-requests-getname.md")
- [getRoutingProfile()](3P-apps-agent-requests-getroutingprofile.md "3P-apps-agent-requests-getroutingprofile.md")
- [getState()](3P-apps-agent-requests-getstate.md "3P-apps-agent-requests-getstate.md")
- [listAvailabilityStates()](3P-apps-agent-requests-listavailabilitystates.md "3P-apps-agent-requests-listavailabilitystates.md")
- [listQuickConnects()](3P-apps-agent-requests-listquickconnects.md "3P-apps-agent-requests-listquickconnects.md")
- [offEnabledChannelListChanged()](3P-apps-agent-requests-off-enabledchannellistchanged.md "3P-apps-agent-requests-off-enabledchannellistchanged.md")
- [offRoutingProfileChanged()](3P-apps-agent-requests-off-routingprofilechanged.md "3P-apps-agent-requests-off-routingprofilechanged.md")
- [onEnabledChannelListChanged()](3P-apps-agent-requests-on-enabledchannellistchanged.md "3P-apps-agent-requests-on-enabledchannellistchanged.md")
- [onRoutingProfileChanged()](3P-apps-agent-requests-on-routingprofile-changed.md "3P-apps-agent-requests-on-routingprofile-changed.md")
- [setAvailabilityState()](3P-apps-agent-requests-setavailabilitystate.md "3P-apps-agent-requests-setavailabilitystate.md")
- [setAvailabilityStateByName()](3P-apps-agent-requests-setavailabilitystatebyname.md "3P-apps-agent-requests-setavailabilitystatebyname.md")
- [setOffline()](3P-apps-agent-requests-setoffline.md "3P-apps-agent-requests-setoffline.md")
- [onStateChanged()](3P-apps-agent-events-statechanged-sub.md "3P-apps-agent-events-statechanged-sub.md")
- [offStateChanged()](3P-apps-agent-events-statechanged-unsub.md "3P-apps-agent-events-statechanged-unsub.md")
