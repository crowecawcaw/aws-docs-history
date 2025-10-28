# Integrate application with Amazon Connect

Agent Workspace agent data

To integrate your application with agent data from Amazon Connect Agent Workspace, instantiate
the agent client as follows:

```

import { AgentClient } from "@amazon-connect/contact";

const agentClient = new AgentClient();

```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must
first instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md")
which will set up the default AmazonConnectProvider. This is the recommended
option.

Alternatively, see the [API
reference](api-reference-3p-apps-agent-client.md "api-reference-3p-apps-agent-client.md") to customize your client’s configuration.

Once the agent client is instantiated, you can use it to subscribe to events and
make requests.

## Example agent event

The code sample below subscribes a callback to the state change event topic.
Whenever the agent’s state is modified, the workspace will invoke your provided
callback, passing in the event data payload for your function to operate on. In
this example, it logs the event data to the console.

```

import { AgentStateChanged } from "@amazon-connect/contact";

// A simple callback that just console logs the state change event data
// returned by the workspace whenever the logged-in agent's state changes
const handler = async (data: AgentStateChanged) => {
    console.log(data);
};

// Subscribe to the state change topic using the above handler
agentClient.onStateChanged(handler);

```

## Example agent

request

The following code sample submits a `getARN` request and then logs
the returned data to the console.

```

const arn = await agentClient.getARN();

console.log(`Got the arn value: ${arn}`);

```

The above agent event and request are non-exhaustive. For a full list of
available agent events and requests, see the [API
Reference](api-reference-3p-apps-events-and-requests.md "api-reference-3p-apps-events-and-requests.md").
