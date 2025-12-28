# Integrate application with Amazon Connect

Agent Workspace contact data

To integrate your application with contact data from the Amazon Connect
agent workspace, instantiate
the contact client as follows:

```

import { ContactClient } from "@amazon-connect/contact";

const contactClient = new ContactClient({ provider });

```

###### Note

You must first instantiate the [AmazonConnectApp](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which initializes the default AmazonConnectProvider and
returns `{ provider }` . This is the recommended option.

Alternatively, see the [API
reference](api-reference-3P-apps-contact-client.md "api-reference-3P-apps-contact-client.md") to customize your client’s configuration.

Once the contact client is instantiated, you can use it to subscribe to events and
make requests.

## Contact scope

All ContactClient methods include an optional `contactId` parameter. If no value is provided, the client automatically defaults to the contact context from which the app was launched. Note that this requires the app to be opened within a contact's context.

- **Applications configured with Per Contact scope**

For Per Contact scoped applications, the `contactId` of the current
contact is provided in the `AppCreateEvent` which is supplied
in the `onCreate` callback.

```

const provider =  AmazonConnectApp.init({

    onCreate: async (event: AppCreateEvent) => {
        // Check if scope is defined and has contactId before accessing it
        if (event.context.scope && "contactId" in event.context.scope) {
            let contactId = event.context.scope.contactId;
            console.log("App launched for the contactId", contactId);
        }
    },

    onDestroy: async (event: AppDestroyEvent) => {
        console.log("App destroyed:", event);
    },

});

```

- **Applications configured with Cross Contact scope**

Cross Contact scoped applications can retrieve the `contactId` by
subscribing to any of the contact events like `onConnected` or `onIncomming`

```

const handler: ContactIncomingHandler = async (data: ContactIncoming) => {
    console.log("Contact incoming occurred! " + data);
    let contactId = data.contactId;
};

contactClient.onIncoming(handler);

```

## Example contact

event

The following code sample subscribes a callback to the connected event topic.
Whenever a contact is connected to the agent, the agent workspace will invoke
your
provided callback, passing in the event data payload for your function to
operate on. In this example, it logs the event data to the console.

```

import {
    ContactClient,
    ContactConnected,
    ContactConnectedHandler
} from "@amazon-connect/contact";

// A simple callback that just console logs the contact connected event data
// returned by the workspace whenever the current contact is connected
const handler: ContactConnectedHandler = async (data: ContactConnected) => {
    console.log(data);
};

// Subscribe to the contact connected topic using the above handler
contactClient.onConnected(handler, contactId);

```

## Example contact

request

The following code sample submits a `getQueue` request and then
logs the returned data to the console.

```

import { ContactClient } from "@amazon-connect/contact";

const queue = await contact.getQueue(contactId);

console.log(`Got the queue: ${queue}`);

```

The above contact event and request are non-exhaustive. For a full list of
available contact events and requests, see the [API
Reference](api-reference-3P-apps-events-and-requests.md "api-reference-3P-apps-events-and-requests.md").
