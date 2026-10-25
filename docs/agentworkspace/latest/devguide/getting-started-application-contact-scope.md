

# Application scoping for Connect Customer applications
<a name="getting-started-application-contact-scope"></a>

Every application built with the Connect Customer SDK runs with a contact scope. The contact scope determines whether the agent receives a separate instance of your application for each contact that they handle, or a single instance that serves all of them. You choose the scope when you design and register your application.

We recommend that you design your application to handle a single contact and register it with the **Per contact** scope. [AppManager](integrate-aws-managed-apps-streams.md#integrate-aws-managed-apps-appmanager-definition) creates a separate instance of your application for each contact that the agent handles, provides that contact's `contactId` to the instance at startup, and destroys the instance when the contact ends. Your application does not track the agent's other contacts, determine which contact the agent is working on, or change its content when the agent moves between contacts. AppManager handles this behavior. When the agent switches contacts, AppManager displays the instance for the newly selected contact and hides the others. A hidden instance retains its state and is not reloaded or reinitialized.

Register the **Cross contacts** scope only when your application's content is session-level rather than contact-level, such as a notes application that an agent uses to record information across all of the contacts that they handle during a shift.

**Important**  
If your application displays contact-specific information but is registered with the **Cross contacts** scope, a single instance is shared across all of the agent's concurrent contacts. That instance receives contact events for every one of those contacts, and your application must determine which contact the content on screen reflects. This can result in data for one contact being displayed while the agent is working on another.  
Your application does not receive an event when the agent switches between contacts. If your application is contact-specific, register it with the **Per contact** scope rather than tracking the active contact in your application.

Contact scoping works the same way in the Connect Customer agent workspace and in a custom agent application that you build with Connect Customer Streams.

## Choose a contact scope
<a name="getting-started-application-contact-scope-choosing"></a>

Use the following table to decide which contact scope to register your application with.


| If your application | Register it with | What AppManager does | 
| --- | --- | --- | 
| Displays, collects, or modifies information that belongs to a single contact, such as a customer record looked up from contact attributes, a wrap-up form, or the order being discussed on the call. Requires a contactId, or calls ContactClient request operations. Displays different content depending on which contact the agent is working on. |  **Per contact** <br /> `PER_CONTACT`  | Creates a separate instance for each contact. Each instance is bound to one contact for its entire lifetime, can access data for that contact only, and is destroyed when that contact ends. | 
| Presents the same session-level content regardless of which contact the agent is handling, and holds state that must outlive any individual contact, such as a notes application that spans a shift. |  **Cross contacts** <br /> `CROSS_CONTACTS`  | Creates a single instance that persists across contacts and is not destroyed when contacts end. The instance receives contact events for every contact that the agent is handling. | 

**Note**  
Registering your application with the **Per contact** scope does not limit its availability to times when the agent is handling a contact. Agents open applications when they choose, including when they have no active contact, and a custom agent application can also launch a per-contact application with the `idle` scope. In both cases the instance runs without being bound to a contact. See [Handle your scope at startup](#getting-started-application-contact-scope-launch).

## Register your application with a contact scope
<a name="getting-started-application-contact-scope-registration"></a>

You set the contact scope when your application is registered as an integration in the Connect Customer console. It is the **Contact scope** field on the **Add integration** page, and its value is a property of the application, exposed to the Connect Customer SDK as `contactHandling.scope`. For the procedure, see [Integrate third-party applications in the agent workspace](https://docs.aws.amazon.com/connect/latest/adminguide/3p-apps.html) in the *Connect Customer Administrator Guide*.

You can change the contact scope of an existing integration at any time. The change takes effect the next time an agent signs in.

The contact scope does not grant your application access to contact data. If your application subscribes to contact events or calls `ContactClient` request operations, grant the corresponding permissions when you register the integration. For more information, see [Events and requests in Connect Customer agent workspace](getting-started-events-and-requests.md).

To register an application with a localhost access URL while you develop it, see [Test your application for Connect Customer agent workspace locally](getting-started-testing.md).

## Handle your scope at startup
<a name="getting-started-application-contact-scope-launch"></a>

The following example is for an application registered with the **Per contact** scope. A per-contact instance learns which contact it belongs to from the scope on its create event, and that value does not change for the life of the instance. Read the scope in `onCreate` rather than assuming a contact is present, because an agent can open your application while they are not handling a contact.

```
import { AmazonConnectApp, AppCreateEvent } from "@amazon-connect/app";
import { ContactClient } from "@amazon-connect/contact";

const { provider } = AmazonConnectApp.init({
    onCreate: async (event: AppCreateEvent) => {
        const { scope } = event.context;

        // This application is registered with the Per contact scope, so the scope is
        // "contact" when the agent has an active contact and "idle" when they do not.
        if (scope?.type !== "contact") {
            renderEmptyState();
            return;
        }

        // This instance handles this contact only, for its entire lifetime.
        const { contactId } = scope;
        const contactClient = new ContactClient({ provider });

        const attributes = await contactClient.getAttributes(contactId, "*");
        renderContactView(contactId, attributes);
        contactClient.onConnected(() => refreshContactView(contactId));
    },

    onDestroy: async () => {
        // The contact that this instance was created for has ended.
    },
});
```

An application registered with the **Per contact** scope starts in one of two states.
+ **`{ type: "contact", contactId }`** – The instance is bound to that contact, can access data for that contact only, and is destroyed when the contact ends. Read the `contactId` once and use it for the lifetime of the instance.
+ **`{ type: "idle" }`** – The agent opened your application while they were not handling a contact. The instance cannot access contact data while it holds this scope. Contact events are not delivered to it, and `ContactClient` request operations fail authorization, including operations that do not identify a specific contact, such as `listContacts`. Render an empty state. This is expected behavior. You do not need to register a second application to handle it.

Pass the `contactId` to the `ContactClient` request operations that require it, such as `getAttributes` and `accept`. For event subscriptions such as `onConnected`, the `contactId` parameter is optional: if you omit it, the instance receives events for the contact that it is scoped to. For more information, see [Integrate application with Connect Customer agent workspace contact data](integrate-with-contact-data.md).

**Note**  
If your application shows contact-specific content but is registered with the **Cross contacts** scope, none of the preceding behavior applies. The instance receives no `scope` value, a single instance is shared across all of the agent's contacts and receives contact events for all of them, and your application must determine which contact its content belongs to. See [Choose a contact scope](#getting-started-application-contact-scope-choosing).

## Design considerations for per-contact applications
<a name="getting-started-application-contact-scope-design"></a>

A per-contact application can run more than once at the same time, and an instance can be destroyed at any time. Consider the following.
+ **Several instances can run at once.** Do not assume that only one instance of your application is running in the browser. Each instance runs in its own frame, with its own document and JavaScript state. If an agent opens the agent application in a second browser tab, a second instance of your application runs in that tab.
+ **Key shared resources by contact.** Instances share only what lies outside their frames, such as browser storage. Key any such resource by `contactId` so that one instance does not overwrite the state of another.
+ **An instance can start with no contact.** Handle the `idle` scope, for example by rendering an empty state, rather than assuming that a contact is present at creation. An instance that is not bound to a contact is not destroyed when contacts end: it persists for the lifetime of the page session rather than the agent's sign-in.
+ **Clean up promptly on destroy.** When the contact ends, AppManager invokes your `onDestroy` callback and waits five seconds for it to report completion. After that the instance is destroyed regardless, and incomplete work is lost. Your application is not displayed while the callback runs, so it cannot prompt the agent to confirm anything. Save data that must persist after the contact ends as it changes, rather than only in the `onDestroy` callback.

## Launch an application with an explicit scope
<a name="getting-started-application-contact-scope-launch-examples"></a>

The agent application that hosts your application launches it with an explicit scope. Your application cannot set its own scope. The host passes a scope in `AppLaunchOptions.scope` when it calls `launchApp`, and that value takes precedence over the scope that you registered. For this reason, read the scope at startup rather than assuming it. The following table describes the scope your application runs with for each combination of registered scope and launch-time scope. An *active contact* exists whenever the agent is handling one or more contacts.



- ** **Per contact** **
  - **Launch-time scope:**  contact  / **Resulting behavior:** AppManager creates one instance per contact and destroys the instance when the contact ends.
  - **Launch-time scope:**  idle  / **Resulting behavior:** The instance is available while the agent is idle and is not destroyed when contacts end. It cannot access contact data while it holds this scope.
  - **Launch-time scope:** Not specified / **Resulting behavior:** Behaves the same as contact if an active contact exists at launch, and the same as idle if the agent is idle. The scope of the launching application does not apply.

- ** **Cross contacts** **
  - **Launch-time scope:** Not specified, launched at the top level / **Resulting behavior:** The instance persists across contacts and is destroyed only when the page session ends or the agent application calls `destroy()`. It receives contact events for every contact the agent is handling and can request data for any of them.<br />This is the configuration that matches the publisher's intent for a cross-contact application.
  - **Launch-time scope:** Not specified, launched from within a scoped application / **Resulting behavior:** The instance inherits the scope of the nearest application above it in the launch chain. Launched from a contact-scoped application, it is bound to that contact and is destroyed when the contact ends. It runs without a scope only when no application in the chain has one.
  - **Launch-time scope:**  idle  / **Resulting behavior:** The instance persists across contacts and is destroyed only when the page session ends or the agent application calls destroy(), but it cannot access contact data while it holds this scope. Omit the scope value instead if your application needs contact data.
  - **Launch-time scope:**  contact  / **Resulting behavior:** The instance can access data for the associated contact only, and AppManager destroys it when that contact ends. This prevents the application from persisting across contacts as the publisher intends.



**Note**  
From within an application that already has a scope, a launch that requests a different scope fails with the `invalidScopeProvided` error. A nested launch can request only the scope of the launching application, or no scope value.

If you are building a custom agent application, or if your application launches other applications, see [Launch-time scope](integrate-aws-managed-apps-contact-scoped.md#integrate-aws-managed-apps-contact-scoped-launch) for how to pass a scope, and [Launch an application with an explicit scope](integrate-aws-managed-apps-contact-scoped.md#integrate-aws-managed-apps-contact-scoped-launch-examples) for code examples.