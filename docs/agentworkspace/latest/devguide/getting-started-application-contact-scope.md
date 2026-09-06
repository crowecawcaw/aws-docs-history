

# Application scoping in Connect Customer agent workspace
<a name="getting-started-application-contact-scope"></a>

Every application has two scope settings that together determine how the application behaves with respect to contacts:
+ A **registration-time scope**, selected by the application publisher when the application integration is registered with Amazon Connect.
+ A **launch-time scope**, passed by the agent application in `AppLaunchOptions.scope` when it calls `launchApp`.

**The launch-time scope always takes precedence.** It is the value that AppManager uses to determine the lifecycle of the application instance, regardless of the registration-time scope. The registration-time scope is advisory: it indicates the launch-time scope that the publisher recommends for typical use of the application, but the agent application is free to launch the application with a different scope. For example, a registration-time "Cross contacts" application launched with `scope.type: "contact"` is destroyed when the associated contact ends.

## Registration-time contact handling scope
<a name="getting-started-application-contact-scope-registration"></a>

The contact handling scope is selected by the application publisher when the application integration is registered with Amazon Connect. It is a property of the application and cannot be changed by the agent application at launch time. The following values are supported.


| Scope | Description | 
| --- | --- | 
|  Per contact  | AppManager maintains a separate application instance for each contact. Each instance's data access is scoped to its associated contact, and the instance is destroyed when that contact ends. To launch the application with this behavior, set the launch-time scope to `contact`. | 
|  Cross contacts  | AppManager maintains a single application instance that persists across contacts for the lifetime of the browser session. The instance is not bound to any specific contact and is not destroyed when contacts end. This scope is suitable for utilities, knowledge bases, dashboards, and other applications whose content is session-level rather than contact-level. To launch the application with this behavior, set the launch-time scope to `idle`. | 

## Launch-time scope
<a name="getting-started-application-contact-scope-launch"></a>

The launch-time scope is the value that the agent application passes in `AppLaunchOptions.scope` when calling `launchApp`. It applies to both per-contact and cross-contact applications and determines the lifecycle of the resulting application instance. The following values are supported.
+ **`contact`** – The application instance is bound to a single contact and can access data only for that contact. AppManager automatically destroys the instance when the associated contact ends, and emits the `onDestroying` and `onDestroyed` lifecycle events so that the agent application can clean up the user interface. This behavior applies regardless of the application's registration-time scope. A cross-contact application launched with the `contact` scope is destroyed when the associated contact ends.
+ **`idle`** – The *idle* state refers to the period when the agent is not handling any contact. An application launched with the `idle` scope is not bound to any contact, does not have access to contact data, and persists for the lifetime of the page or until the agent application calls `destroy()`. Use this scope for cross-contact applications that must remain open across contacts, and for per-contact applications that must remain available when the agent is not handling a contact.

The following table describes the launch-time scope to use for each registration-time scope, including the default behavior when the agent application does not pass a `scope` value at launch. An *active contact* exists whenever the agent is handling one or more contacts; the *idle* state is the period when the agent is not handling any contact.



- ** **Per contact** **
  - **Launch-time scope:**  contact  / **Resulting behavior:** AppManager creates one instance per contact and automatically destroys the instance when the contact ends.
  - **Launch-time scope:**  idle  / **Resulting behavior:** The application is available when the agent is idle and is not destroyed when contacts end. The application cannot access contact data.
  - **Launch-time scope:** Not specified / **Resulting behavior:** If an active contact exists at launch, behaves the same as contact. If the agent is idle at launch, behaves the same as idle.

- ** **Cross contacts** **
  - **Launch-time scope:**  idle  / **Resulting behavior:** The application persists across contacts and is destroyed only when the page session ends or the agent application calls destroy().
  - **Launch-time scope:**  contact  / **Resulting behavior:** The application can access contact data, but AppManager destroys the instance when the associated contact ends. This prevents the application from persisting across contacts as the publisher intends.
  - **Launch-time scope:** Not specified / **Resulting behavior:** If an active contact exists at launch, behaves the same as contact. If the agent is idle at launch, behaves the same as idle.



**Note**  
The registration-time scope is **not** used as the implicit default when no launch-time scope is provided. To guarantee a specific behavior regardless of whether an active contact exists at launch time, set `scope.type` explicitly to `"contact"` or `"idle"`.

## Launch an application with an explicit scope
<a name="getting-started-application-contact-scope-launch-examples"></a>

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