# Integrate application with Amazon Connect

Agent Workspace contact data

To integrate your application with contact data from Amazon Connect Agent Workspace, instantiate
the contact client as follows:

```

import { ContactClient } from "@amazon-connect/contact";

const contactClient = new ContactClient();

```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must
first instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md")
which will set up the default AmazonConnectProvider. This is the recommended
option.

Alternatively, see the [API
reference](api-reference-3p-apps-contact-client.md "api-reference-3p-apps-contact-client.md") to customize your client’s configuration.

Once the contact client is instantiated, you can use it to subscribe to events and
make requests.

## Contact scope

For all ContactClient event methods which have the optional parameter
`contactId` but do not receive an argument for this parameter,
the client will default to using the scope of the contact in which the app was
opened, for example, the _current contact_ from
`AppContactScope`. You can also use `AppContactScope`
_current contact_ value as an argument to the contact request
methods to retrieve data about the contact loaded into the workspace. This
requires the app being opened in the context of a contact.

## Example contact

event

The following code sample subscribes a callback to the connected event topic.
Whenever a contact is connected to the agent, the workspace will invoke your
provided callback, passing in the event data payload for your function to
operate on. In this example, it logs the event data to the console.

```

import {
    ContactClient,
    ContactConnected,
    ContactConnectedHandler
} from "@amazon-connect/contact";
import { AppContactScope } from "@amazon-connect/app";

// A simple callback that just console logs the contact connected event data
// returned by the workspace whenever the current contact is connected
const handler: ContactConnectedHandler = async (data: ContactConnected) => {
    console.log(data);
};

// Subscribe to the contact connected topic using the above handler
contactClient.onConnected(handler, AppContactScope.CurrentContactId);

```

## Example contact

request

The following code sample submits a `getQueue` request and then
logs the returned data to the console.

```

import { ContactClient } from "@amazon-connect/contact";
import { AppContactScope } from "@amazon-connect/app";

const queue = await contact.getQueue(AppContactScope.CurrentContactId);

console.log(`Got the queue: ${queue}`);

```

The above contact event and request are non-exhaustive. For a full list of
available contact events and requests, see the [API
Reference](api-reference-3p-apps-events-and-requests.md "api-reference-3p-apps-events-and-requests.md").
