# Amazon Connect Agent Workspace Agent API

The SDK provides an `AgentClient` which serves as an interface that your
app in Amazon Connect Agent Workspace can use to subscribe to agent events and make agent data
requests.

The `AgentClient` accepts an optional constructor argument,
`ConnectClientConfig` which itself is defined as:

```

export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};

```

If you do not provide a value for this config, then the client will default to using
the **AmazonConnectProvider** set in the global provider scope. You can
also manually configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```

import { AgentClient } from "@amazon-connect/contact";

const agentClient = new AgentClient();

```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must first
instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which will set up the default AmazonConnectProvider. This is the
recommended option.

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

- [getARN()](3p-apps-agent-requests-getarn.md "3p-apps-agent-requests-getarn.md")
- [getChannelConcurrency()](3p-apps-agent-requests-getchannelconcurrency.md "3p-apps-agent-requests-getchannelconcurrency.md")
- [getDialableCountries() - Deprecated](3p-apps-agent-requests-getdialablecountries.md "3p-apps-agent-requests-getdialablecountries.md")
- [getExtension()](3p-apps-agent-requests-getextension.md "3p-apps-agent-requests-getextension.md")
- [getName()](3p-apps-agent-requests-getname.md "3p-apps-agent-requests-getname.md")
- [getRoutingProfile()](3p-apps-agent-requests-getroutingprofile.md "3p-apps-agent-requests-getroutingprofile.md")
- [getState()](3p-apps-agent-requests-getstate.md "3p-apps-agent-requests-getstate.md")
- [listAvailabilityStates()](3p-apps-agent-requests-listavailabilitystates.md "3p-apps-agent-requests-listavailabilitystates.md")
- [listQuickConnects()](3p-apps-agent-requests-listquickconnects.md "3p-apps-agent-requests-listquickconnects.md")
- [setAvailabilityState()](3p-apps-agent-requests-setavailabilitystate.md "3p-apps-agent-requests-setavailabilitystate.md")
- [setAvailabilityStateByName()](3p-apps-agent-requests-setavailabilitystatebyname.md "3p-apps-agent-requests-setavailabilitystatebyname.md")
- [setOffline()](3p-apps-agent-requests-setoffline.md "3p-apps-agent-requests-setoffline.md")
- [StateChanged
  (Subscribing)](3p-apps-agent-events-statechanged-sub.md "3p-apps-agent-events-statechanged-sub.md")
- [StateChanged
  (Unsubscribing)](3p-apps-agent-events-statechanged-unsub.md "3p-apps-agent-events-statechanged-unsub.md")
