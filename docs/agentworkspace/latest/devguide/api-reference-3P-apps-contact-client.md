# Amazon Connect Agent Workspace Contact API

The Amazon Connect SDK provides an `ContactClient` which serves as an interface that your app
in the Amazon Connect agent workspace can use to subscribe to contact events and make contact data requests.

The `ContactClient` accepts an optional constructor argument, `ConnectClientConfig` which itself is defined as:

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

            import { ContactClient } from "@amazon-connect/contact";
            const contactClient = new ContactClient({ provider });

```

###### Note

You must first instantiate the [AmazonConnectApp](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which initializes the default AmazonConnectProvider and returns `{ provider }` . This is the recommended option.

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

- [accept()](3P-apps-contact-requests-accept.md "3P-apps-contact-requests-accept.md")
- [addParticipant()](3P-apps-contact-requests-addparticipant.md "3P-apps-contact-requests-addparticipant.md")
- [clear()](3P-apps-contact-requests-clear.md "3P-apps-contact-requests-clear.md")
- [onCleared()](3P-apps-contact-requests-clearedsubscribing.md "3P-apps-contact-requests-clearedsubscribing.md")
- [offCleared()](3P-apps-contact-requests-clearedunsubscribing.md "3P-apps-contact-requests-clearedunsubscribing.md")
- [onConnected()](3P-apps-contact-events-connected-sub.md "3P-apps-contact-events-connected-sub.md")
- [offConnected()](3P-apps-contact-events-connected-unsub.md "3P-apps-contact-events-connected-unsub.md")
- [disconnectParticipant()](3P-apps-contact-requests-disconnectparticipant.md "3P-apps-contact-requests-disconnectparticipant.md")
- [engagePreviewContact()](3P-apps-contact-requests-engagepreviewcontact.md "3P-apps-contact-requests-engagepreviewcontact.md")
- [getAttribute()](3P-apps-contact-requests-getattribute.md "3P-apps-contact-requests-getattribute.md")
- [getAttributes()](3P-apps-contact-requests-getattributes.md "3P-apps-contact-requests-getattributes.md")
- [getChannelType()](3P-apps-contact-requests-getchanneltype.md "3P-apps-contact-requests-getchanneltype.md")
- [getContact()](3P-apps-contact-requests-getcontact.md "3P-apps-contact-requests-getcontact.md")
- [getInitialContactId()](3P-apps-contact-requests-getinitialcontactid.md "3P-apps-contact-requests-getinitialcontactid.md")
- [getParticipant()](3P-apps-contact-requests-getparticipant.md "3P-apps-contact-requests-getparticipant.md")
- [getParticipantState()](3P-apps-contact-requests-getparticipantstate.md "3P-apps-contact-requests-getparticipantstate.md")
- [getPreviewConfiguration()](3P-apps-contact-requests-getpreviewconfiguration.md "3P-apps-contact-requests-getpreviewconfiguration.md")
- [getQueue()](3P-apps-contact-requests-getqueue.md "3P-apps-contact-requests-getqueue.md")
- [getQueueTimestamp()](3P-apps-contact-requests-getqueuetimestamp.md "3P-apps-contact-requests-getqueuetimestamp.md")
- [getStateDuration()](3P-apps-contact-requests-getstateduration.md "3P-apps-contact-requests-getstateduration.md")
- [isPreviewMode()](3P-apps-contact-requests-ispreviewmode.md "3P-apps-contact-requests-ispreviewmode.md")
- [listContacts()](3P-apps-contact-requests-listcontacts.md "3P-apps-contact-requests-listcontacts.md")
- [listParticipants()](3P-apps-contact-requests-listparticipants.md "3P-apps-contact-requests-listparticipants.md")
- [onMissed()](3P-apps-contact-events-missed-sub.md "3P-apps-contact-events-missed-sub.md")
- [offMissed()](3P-apps-contact-events-missed-unsub.md "3P-apps-contact-events-missed-unsub.md")
- [offIncoming()](3P-apps-contact-requests-off-incoming.md "3P-apps-contact-requests-off-incoming.md")
- [onIncoming()](3P-apps-contact-requests-on-incoming.md "3P-apps-contact-requests-on-incoming.md")
- [onParticipantAdded()](3P-apps-contact-events-participantadded-sub.md "3P-apps-contact-events-participantadded-sub.md")
- [offParticipantAdded()](3P-apps-contact-events-participantadded-unsub.md "3P-apps-contact-events-participantadded-unsub.md")
- [onParticipantDisconnected()](3P-apps-contact-events-participantdisconnected-sub.md "3P-apps-contact-events-participantdisconnected-sub.md")
- [offParticipantDisconnected()](3P-apps-contact-events-participantdisconnected-unsub.md "3P-apps-contact-events-participantdisconnected-unsub.md")
- [onParticipantStateChanged()](3P-apps-contact-events-participantstatechanged-sub.md "3P-apps-contact-events-participantstatechanged-sub.md")
- [onStartingAcw()](3P-apps-contact-events-startingacw-sub.md "3P-apps-contact-events-startingacw-sub.md")
- [offStartingAcw()](3P-apps-contact-events-startingacw-unsub.md "3P-apps-contact-events-startingacw-unsub.md")
- [transfer()](3P-apps-contact-requests-transfer.md "3P-apps-contact-requests-transfer.md")
