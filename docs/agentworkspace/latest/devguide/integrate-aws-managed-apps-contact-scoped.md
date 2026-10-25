

# Contact-scoped applications
<a name="integrate-aws-managed-apps-contact-scoped"></a>

This section describes how to launch and manage AWS managed applications that are tied to specific customer contacts. Contact scoping itself is not specific to AWS managed applications. For the registration-time scope that a publisher selects for an application, and for guidance on designing an application around a single contact, see [Application scoping for Connect Customer applications](getting-started-application-contact-scope.md).

**Note**  
Scoped application launches require the `@amazon-connect/app-manager-agent` package. For installation instructions, see [Step 1: Install required packages](integrate-aws-managed-apps-implementation.md#integrate-aws-managed-apps-step1).

## Launch-time scope
<a name="integrate-aws-managed-apps-contact-scoped-launch"></a>

The launch-time scope is the value that the agent application passes in `AppLaunchOptions.scope` when calling `launchApp`. It applies to both per-contact and cross-contact applications, and it determines the lifecycle of the resulting application instance. The supported values are `contact` and `idle`.

The launch-time scope takes precedence over the registration-time scope, which is advisory: the registration-time scope indicates what the publisher recommends, and the agent application is free to launch with a different scope. For the scope your application runs with for each combination of registration-time and launch-time scope, see [Launch an application with an explicit scope](getting-started-application-contact-scope.md#getting-started-application-contact-scope-launch-examples). For the registration-time scope itself, see [Register your application with a contact scope](getting-started-application-contact-scope.md#getting-started-application-contact-scope-registration).

Consider the following behaviors when you launch an application from your agent application.
+ When AppManager destroys a contact-scoped instance because its contact ended, it emits the `onDestroying` and `onDestroyed` lifecycle events so that your agent application can clean up the user interface. See [Handle lifecycle events](integrate-aws-managed-apps-lifecycle.md#integrate-aws-managed-apps-lifecycle-events).
+ Do not pass the `idle` scope to launch a cross-contact application that needs contact data, because an instance holding that scope cannot access contact data. Omit the `scope` value instead.

**Note**  
When no launch-time scope is provided, the resulting scope depends on the registration-time scope, and for a per-contact application it also depends on whether an active contact exists at launch time. To guarantee a specific behavior when you launch at the top level, set `scope.type` explicitly to `"contact"` or `"idle"`. From inside an application that already has a scope, an explicit scope that does not match fails the launch rather than overriding it, as described in **Nested launches**, following.

**Nested launches**

An application can launch another application by calling `launchApp` on `AppControllerClient`. When it does, the scope of the launching application constrains the scope of the application it launches.
+ If you omit the `scope` value and the application is registered with the **Cross contacts** scope, the new application inherits the scope of the nearest application above it in the launch chain that has one. It runs without a scope only when no application in that chain has a scope. A cross-contact application launched from within a contact-scoped application is therefore bound to that contact, and is destroyed when the contact ends.
+ If you provide a `scope` value that does not match the scope of the nearest application above the new application in the launch chain that has one, `launchApp` fails with the `invalidScopeProvided` error. Launching from within a contact-scoped application, you can pass only that same contact scope, or no `scope` value.

An application registered with the **Per contact** scope is not affected by inheritance. When you omit the `scope` value, the application is bound to the current active contact if one exists, and receives the `idle` scope if the agent is not handling a contact.

## Launch an application with an explicit scope
<a name="integrate-aws-managed-apps-contact-scoped-launch-examples"></a>

To control the scope under which an application runs, provide a `scope` object in the `AppLaunchOptions` parameter of `launchApp`.

 **Launch with `contact` scope:** 

Provide the `contact` type and the ID of the contact to which the application is bound:

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
```

 **Launch with `idle` scope:** 

Provide the `idle` type to launch an application that is not bound to the lifecycle of any contact:

```
const launchOptions: AppLaunchOptions = {
    scope: {
        type: "idle"
    }
};

// Launch an application that does not have access to contact data and
// persists regardless of which contact the agent is handling
const appHost = await appManager.launchApp(app.arn, launchOptions);

// Create and configure the iframe for the application
const appIframe = document.createElement("iframe");
appHost.setIFrame(appIframe);
```

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