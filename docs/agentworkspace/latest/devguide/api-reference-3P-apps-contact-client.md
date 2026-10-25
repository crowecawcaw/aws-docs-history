

# Connect Customer SDK Contact API
<a name="api-reference-3P-apps-contact-client"></a>

The Connect Customer SDK provides an `ContactClient` which serves as an interface that your app in the Connect Customer agent workspace can use to subscribe to contact events and make contact data requests.

The `ContactClient` accepts an optional constructor argument, ` ConnectClientConfig` which itself is defined as:

```
            export type ConnectClientConfig = {  
                context?: ModuleContext;  
                provider?: AmazonConnectProvider;
             };
```

If you do not provide a value for this config, then the client will default to using the ** AmazonConnectProvider** set in the global provider scope. You can also manually configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```
            import { ContactClient } from "@amazon-connect/contact";
            const contactClient = new ContactClient({ provider });
```

**Note**  
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md) which initializes the default AmazonConnectProvider and returns ` { provider } `. This is the recommended option.

Alternatively, providing a constructor argument:

```
            import { ContactClient } from "@amazon-connect/contact";
            
            const contactClient = new ContactClient({
                context: sampleContext,  
                provider: sampleProvider
        });
```

The operations that a `ContactClient` can perform depend on the contact scope of the application instance that uses it. Each operation in the following sections states its requirement under **Contact scope**. The following table describes the operations that a `ContactClient` can perform for each contact scope.


| Contact scope of the instance | What the `ContactClient` can do | 
| --- | --- | 
|  { type: "contact", contactId }  | The instance can call request operations for that contactId only. A request that identifies another contact fails authorization, and listContacts() fails regardless of which contact the instance is scoped to. Event subscriptions deliver events for that contact only. | 
|  { type: "idle" }  | The instance cannot call any request operation, including listContacts(), and does not receive contact events while it holds this scope. | 
| No scope value | The instance can call every request operation for any contact that the agent is handling, and receives events for all of those contacts. | 

**Note**  
A cross-contact application does not always run without a scope. When it is launched from within an application that has a scope, it inherits that scope, and the first row of the preceding table applies to it. For more information, see [Launch an application with an explicit scope](getting-started-application-contact-scope.md#getting-started-application-contact-scope-launch-examples).

The following sections describe API calls for working with the Contact API.

**Topics**
+ [accept()](3P-apps-contact-requests-accept.md)
+ [addParticipant()](3P-apps-contact-requests-addparticipant.md)
+ [clear()](3P-apps-contact-requests-clear.md)
+ [onCleared()](3P-apps-contact-requests-clearedsubscribing.md)
+ [offCleared()](3P-apps-contact-requests-clearedunsubscribing.md)
+ [onConnected()](3P-apps-contact-events-connected-sub.md)
+ [offConnected()](3P-apps-contact-events-connected-unsub.md)
+ [disconnectParticipant()](3P-apps-contact-requests-disconnectparticipant.md)
+ [engagePreviewContact()](3P-apps-contact-requests-engagepreviewcontact.md)
+ [getAttribute()](3P-apps-contact-requests-getattribute.md)
+ [getAttributes()](3P-apps-contact-requests-getattributes.md)
+ [getChannelType()](3P-apps-contact-requests-getchanneltype.md)
+ [getContact()](3P-apps-contact-requests-getcontact.md)
+ [getInitialContactId()](3P-apps-contact-requests-getinitialcontactid.md)
+ [getParticipant()](3P-apps-contact-requests-getparticipant.md)
+ [getParticipantState()](3P-apps-contact-requests-getparticipantstate.md)
+ [getPreviewConfiguration()](3P-apps-contact-requests-getpreviewconfiguration.md)
+ [getQueue()](3P-apps-contact-requests-getqueue.md)
+ [getQueueTimestamp()](3P-apps-contact-requests-getqueuetimestamp.md)
+ [getStateDuration()](3P-apps-contact-requests-getstateduration.md)
+ [isPreviewMode()](3P-apps-contact-requests-ispreviewmode.md)
+ [listContacts()](3P-apps-contact-requests-listcontacts.md)
+ [listParticipants()](3P-apps-contact-requests-listparticipants.md)
+ [onMissed()](3P-apps-contact-events-missed-sub.md)
+ [offMissed()](3P-apps-contact-events-missed-unsub.md)
+ [offIncoming()](3P-apps-contact-requests-off-incoming.md)
+ [onIncoming()](3P-apps-contact-requests-on-incoming.md)
+ [onParticipantAdded()](3P-apps-contact-events-participantadded-sub.md)
+ [offParticipantAdded()](3P-apps-contact-events-participantadded-unsub.md)
+ [onParticipantDisconnected()](3P-apps-contact-events-participantdisconnected-sub.md)
+ [offParticipantDisconnected()](3P-apps-contact-events-participantdisconnected-unsub.md)
+ [onParticipantStateChanged()](3P-apps-contact-events-participantstatechanged-sub.md)
+ [onStartingAcw()](3P-apps-contact-events-startingacw-sub.md)
+ [offStartingAcw()](3P-apps-contact-events-startingacw-unsub.md)
+ [transfer()](3P-apps-contact-requests-transfer.md)
+ [reject()](3P-apps-contact-requests-reject.md)
+ [disconnectSelf()](3P-apps-contact-requests-disconnectself.md)
+ [isAutoAcceptEnabled()](3P-apps-contact-requests-isautoacceptenabled.md)
+ [onConnecting()](3P-apps-contact-events-connecting-sub.md)
+ [offConnecting()](3P-apps-contact-events-connecting-unsub.md)
+ [onError()](3P-apps-contact-events-error-sub.md)
+ [offError()](3P-apps-contact-events-error-unsub.md)
+ [onPending()](3P-apps-contact-events-pending-sub.md)
+ [offPending()](3P-apps-contact-events-pending-unsub.md)