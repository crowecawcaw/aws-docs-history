# Contact-scoped applications

Contact-scoped applications are tied to specific customer interactions (contacts).
They are essential for scenarios where agents handle multiple contacts simultaneously
and need isolated application contexts for each contact. The following behaviors apply
to contact-scoped applications:

- They can only access data for their specific contact.
- They are automatically destroyed by AppManager when the associated contact
  ends. You will receive `onDestroying` and `onDestroyed`
  lifecycle events, allowing you to clean up the user interface.

###### Note

Contact-scoped applications require the
`@amazon-connect/app-manager-agent` package. See
[Step 1: Install required packages](integrate-aws-managed-apps-implementation.md#integrate-aws-managed-apps-step1 "integrate-aws-managed-apps-implementation.md#integrate-aws-managed-apps-step1") for installation
instructions.

## Launch a contact-scoped application

To launch an application scoped to a specific contact, provide a
`scope` object in the `AppLaunchOptions` parameter of
`launchApp`. The `scope` object requires the `contact` type
and the contact ID of the active contact:

```

const launchOptions: AppLaunchOptions = {
    scope: {
        type: "contact",
        contactId: contactId  // The ID of the contact to scope this application to
    }
};

// Launch the application scoped to the specified contact
const appHost = await appManager.launchApp(app.arn, launchOptions);

// Create and configure the iframe for the application
const appIframe = document.createElement("iframe");
appHost.setIFrame(appIframe);

// Optionally indicate in the UI which contact this app belongs to
appIframe.setAttribute("data-contact-id", contactId);
```

## Manage the active contact

When agents handle multiple contacts simultaneously, you must inform AppManager
which contact is currently active. This ensures the correct contact context is used
when launching applications without an explicit `contactId` in the
`scope` option. Use `setActiveContact` to update the active
contact in AppManager:

```

// Update AppManager with the currently active contact
await appManager.setActiveContact(contactId);
```

To keep AppManager automatically in sync with the contact the agent is currently
viewing, subscribe to the `connect.core.onViewContact` event and call
`setActiveContact` when the active contact changes:

```

// Listen for contact selection events from the CCP
connect.core.onViewContact((event) => {
    const contactId = event.contactId;
    if (contactId) {
        // Keep AppManager in sync with the currently viewed contact
        appManager.setActiveContact(contactId).catch((error) => {
            console.error("Failed to set active contact:", error);
        });
    }
});
```

###### Note

The subscription to `connect.core.onViewContact` that invokes `appManager.setActiveContact` should be done after CCP initialization and
before launching any contact-scoped applications to ensure the correct contact
context is always available.
