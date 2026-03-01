# Application lifecycle management

Application lifecycle management is essential when adding and removing applications
throughout a page's life. If you launch an application once at startup and keep it open,
lifecycle management is optional. However, if you launch and close apps as part of the
user's workflow, then these lifecycle states help you create a better user experience.

## Managing application lifecycle

Application creation begins after an iframe is set in the AppHost. You can
subscribe to AppHost's `onCreated` event to control when the iframe
appears to the user, though showing it during application creation has no functional
impact.

AppManager handles application state transitions throughout the lifecycle. To
close an application, invoke the `destroy` method on the `AppHost`
object. The `AppHost` then emits lifecycle events (`onDestroying`
, `onDestroyed`). Your web application handles these events to update the
user interface accordingly.

The following table describes the application lifecycle states.

| State        | Description                                                                                                                                                                                           |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Created`    | The application iframe is configured and secure communication is<br>established. The application is ready for use. This state occurs<br>immediately following successful `launchApp()`<br>invocation. |
| `Destroying` | Application cleanup is in progress. The application is no longer<br>usable. This state occurs after you invoke `destroy()`<br>method.                                                                 |
| `Destroyed`  | The application is fully destroyed. This state occurs up to 5<br>seconds following the `destroy()` method invocation. The<br>iframe can be safely removed from the DOM.                               |

###### Important

When destroying an application, do not remove it from the Document Object
Model (DOM) until the destruction process completes. You can hide it from users,
but premature removal from the DOM might interrupt critical cleanup processes
such as flushing log buffers or saving state. The `onDestroyed` event
indicates when it's safe to completely remove the application.

**Application visibility states**

When managing multiple applications, based on how you arrange them, some
applications may not be visible at any given time. When an application is
temporarily hidden, it's recommended to notify the application by invoking `stop()` on `AppHost` and then invoking `start()` when
making it visible again.

| State     | Description                                                       |
| --------- | ----------------------------------------------------------------- |
| `Started` | The application is visible and actively synchronizing data.       |
| `Stopped` | The application is not visible. Background operations are paused. |

## Handle lifecycle events

Implement application lifecycle event handlers to manage iframe visibility and
cleanup operations:

```

// Handle destroying event
appHost.onDestroying((event) => {
    console.log(`Application ${appHost.config.name} is being destroyed`);

    // Hide the iframe as the application is no longer usable
    appIframe.style.display = "none";

    return Promise.resolve();
});

// Handle destroyed event
appHost.onDestroyed((event) => {
    console.log(`Application ${appHost.config.name} has been destroyed`);

    // Remove the iframe from the DOM
    appIframe.remove();

    return Promise.resolve();
});
```
