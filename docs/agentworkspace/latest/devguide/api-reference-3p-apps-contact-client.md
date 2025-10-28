# Amazon Connect Agent Workspace Contact

API

The SDK provides an `ContactClient` which serves as an interface that your
app in Amazon Connect Agent Workspace can use to subscribe to contact events and make contact data
requests.

The `ContactClient` accepts an optional constructor argument,
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

            import { ContactClient } from "@amazon-connect/contact";
            const contactClient = new ContactClient();

```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must first
instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which will set up the default AmazonConnectProvider. This is the
recommended option.

Alternatively, providing a constructor argument:

```

            import { ContactClient } from "@amazon-connect/contact";

            const contactClient = new ContactClient({
                context: sampleContext,
                provider: sampleProvider
        });

```

The following sections describe API calls for working with the Contact API.

###### Contents

- [accept()](3p-apps-contact-requests-accept.md "3p-apps-contact-requests-accept.md")
- [addParticipant()](3p-apps-contact-requests-addparticipant.md "3p-apps-contact-requests-addparticipant.md")
- [clear()](3p-apps-contact-requests-clear.md "3p-apps-contact-requests-clear.md")
- [Cleared(Subscribing)](3p-apps-contact-requests-clearedsubscribing.md "3p-apps-contact-requests-clearedsubscribing.md")
- [Cleared(Unsubscribing)](3p-apps-contact-requests-clearedunsubscribing.md "3p-apps-contact-requests-clearedunsubscribing.md")
- [Connected
  (Subscribing)](3p-apps-contact-events-connected-sub.md "3p-apps-contact-events-connected-sub.md")
- [Connected
  (Unsubscribing)](3p-apps-contact-events-connected-unsub.md "3p-apps-contact-events-connected-unsub.md")
- [Destroyed(Subscribing) - Deprecated](3p-apps-contact-requests-destroyedsubscribing-deprecated.md "3p-apps-contact-requests-destroyedsubscribing-deprecated.md")
- [Destroyed(Unsubscribing) - Deprecated](3p-apps-contact-requests-destroyedunsubscribing-deprecated.md "3p-apps-contact-requests-destroyedunsubscribing-deprecated.md")
- [getAttribute()](3p-apps-contact-requests-getattribute.md "3p-apps-contact-requests-getattribute.md")
- [getAttributes()](3p-apps-contact-requests-getattributes.md "3p-apps-contact-requests-getattributes.md")
- [getChannelType()](3p-apps-contact-requests-getchanneltype.md "3p-apps-contact-requests-getchanneltype.md")
- [getInitialContactId()](3p-apps-contact-requests-getinitialcontactid.md "3p-apps-contact-requests-getinitialcontactid.md")
- [getQueue()](3p-apps-contact-requests-getqueue.md "3p-apps-contact-requests-getqueue.md")
- [getQueueTimestamp()](3p-apps-contact-requests-getqueuetimestamp.md "3p-apps-contact-requests-getqueuetimestamp.md")
- [getStateDuration()](3p-apps-contact-requests-getstateduration.md "3p-apps-contact-requests-getstateduration.md")
- [getType() -
  Deprecated](3p-apps-contact-requests-gettype.md "3p-apps-contact-requests-gettype.md")
- [Missed
  (Subscribing)](3p-apps-contact-events-missed-sub.md "3p-apps-contact-events-missed-sub.md")
- [Missed
  (Unsubscribing)](3p-apps-contact-events-missed-unsub.md "3p-apps-contact-events-missed-unsub.md")
- [offCleared(Subscribing)](3p-apps-contact-requests-offcleared-sub.md "3p-apps-contact-requests-offcleared-sub.md")
- [onCleared(Subscribing)](3p-apps-contact-requests-oncleared-sub.md "3p-apps-contact-requests-oncleared-sub.md")
- [StartingAcw
  (Subscribing)](3p-apps-contact-events-startingacw-sub.md "3p-apps-contact-events-startingacw-sub.md")
- [StartingAcw
  (Unsubscribing)](3p-apps-contact-events-startingacw-unsub.md "3p-apps-contact-events-startingacw-unsub.md")
- [transfer()](3p-apps-contact-requests-transfer.md "3p-apps-contact-requests-transfer.md")
