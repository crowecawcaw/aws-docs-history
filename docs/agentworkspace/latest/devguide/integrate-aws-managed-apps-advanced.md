# Advanced configuration

## Prevent duplicate

application instances

When you launch an application multiple times, AppManager creates multiple
application instances by default. You can use launch keys when starting applications
to prevent multiple instances of the same application.

```

const launchOptions: AppLaunchOptions = {
    launchKey: 'Worklist-singleton'
};

// Returns existing instance if launch key matches a running application
const appHost = await appManager.launchApp("Worklist", launchOptions);
```

The launch key is a caller-generated value that prevents duplicate instances. When
an application with a matching launch key is already running, AppManager returns the
existing instance rather than creating a new instance and triggers `onAppHostFocused` event. This event could be leveraged to bring the
application to focus when it's being launched again.

## Dynamic application

launch and management

AppManager provides `onAppHostAdded` and `onAppHostRemoved`
notifications to indicate when a new application is launched or destroyed. These
events could be leveraged to dynamically create and destroy iframes. For an example
implementation, see [Example implementation of
dynamic application management with React](integrate-aws-managed-apps-react-example.md "integrate-aws-managed-apps-react-example.md")
section below.

## Attach metadata to appHost

If you are managing iframes dynamically and want the storage of any application
specific UI state or routing information in the `AppHost`, you can attach
a custom JSON metadata at the time of application launch. This metadata is
accessible in all event callbacks for application state management.

```

const launchOptions: AppLaunchOptions = {
    appManagerData: {
        // Custom JSON data
  }
};

const appHost = await appManager.launchApp("Worklist", launchOptions);

// Access the metadata
console.log("AppManagerData attached to AppHost", appHost.appManagerData);
```

## Support Global

Resiliency

Amazon Connect Global Resiliency features provide automatic failover between AWS
Regions. When your Amazon Connect instance is configured for Global Resiliency, you
should implement the following handlers to ensure agent workspace responsiveness to
failover events:

```

// Handle pending failover events
connect.globalResiliency?.onFailoverPending(() => {
   // Destroy all applications before failover
    appManager.clearAll();
});

// Handle completed failover events
connect.globalResiliency?.onFailoverCompleted(() => {
    // Re-launch necessary applications following failover
    // Implementation depends on your state management approach
});
```

See [Set
up Amazon Connect Global Resiliency](../../../connect/latest/adminguide/setup-connect-global-resiliency.md "../../../connect/latest/adminguide/setup-connect-global-resiliency.md") in the _Amazon Connect
Administrator Guide_.
