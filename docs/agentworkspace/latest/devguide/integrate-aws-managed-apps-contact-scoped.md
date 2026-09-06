

# Contact-scoped applications
<a name="integrate-aws-managed-apps-contact-scoped"></a>

This section describes how to manage AWS-managed applications that are tied to specific customer contacts. Contact scoping itself is not specific to AWS-managed applications — for an explanation of the registration-time and launch-time scope settings that determine how any application behaves with respect to contacts, including `contact` and `idle` launch examples, see [Application scoping in Connect Customer agent workspace](getting-started-application-contact-scope.md).

**Note**  
Scoped application launches require the `@amazon-connect/app-manager-agent` package. For installation instructions, see [Step 1: Install required packages](integrate-aws-managed-apps-implementation.md#integrate-aws-managed-apps-step1).

## Manage the active contact
<a name="integrate-aws-managed-apps-contact-scoped-active-contact"></a>

AppManager binds applications to the active contact when no `scope` value is provided at launch. Therefore, when an agent handles multiple contacts simultaneously, you must keep the active contact accurate so that the correct contact context is used when launching applications without an explicit `contactId` in the `scope` option. Use `setActiveContact` to update the active contact in AppManager:

```
// Update AppManager with the currently active contact
await appManager.setActiveContact(contactId);
```

To keep AppManager automatically in sync with the contact the agent is currently viewing, subscribe to the `connect.core.onViewContact` event and call `setActiveContact` when the active contact changes:

```
// Listen for contact selection events from the CCP
connect.core.onViewContact((event) => {
    const contactId = event.contactId;
    if (contactId) {
        // Keep AppManager in sync with the currently viewed contact
        void appManager.setActiveContact(contactId).catch((error) => {
            console.error("Failed to set active contact:", error);
        });
    }
});
```

**Note**  
The subscription to `connect.core.onViewContact` that invokes `appManager.setActiveContact` should be done after CCP initialization and before launching any contact-scoped applications to ensure the correct contact context is always available.