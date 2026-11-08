

# Application lifecycle management
<a name="integrate-aws-managed-apps-lifecycle"></a>

Application lifecycle management is essential when adding and removing applications throughout a page's life. If you launch an application once at startup and keep it open, lifecycle management is optional. However, if you launch and close apps as part of the user's workflow, then these lifecycle states help you create a better user experience.

## Managing application lifecycle
<a name="integrate-aws-managed-apps-managing-lifecycle"></a>

Application loading begins after you set an iframe on the `AppHost`. You can subscribe to the `onRunning` event of the `AppHost` to control when the iframe appears to the user, though showing it while the application loads has no functional impact. To read the current state at any time, call `getState()`, which returns the state and a version number. To receive every transition, subscribe to `onStateChanged`.

AppManager handles application state transitions throughout the lifecycle. To close an application, invoke the `destroy` method on the `AppHost` object. The `AppHost` then emits the `onDestroying` and `onDestroyed` lifecycle events. Your web application handles these events to update the user interface accordingly.

The following table describes the application lifecycle states (`ComponentState`) and the `AppHost` event, if any, that is emitted when the application enters each state. `onStateChanged` is emitted for every transition.


| State | Event | Description | 
| --- | --- | --- | 
| pending | None | The launch request is accepted and the application instance is being created. | 
| provisioned | onProvisioned | The application instance exists and its AppHost is available. AppManager also emits onAppHostAdded at this point. Set an iframe on the AppHost to start loading the application. | 
| loading | None | An iframe is set and the application page is loading. | 
| loaded | None | The application page finished loading in the iframe. | 
| connected | None | Secure communication between the application and AppManager is established. | 
| running | onRunning | The application is ready for use, visible, and actively synchronizing data. Calling start() on a stopped application returns it to this state. | 
| stopped | onStopped | The application is not visible and background operations are paused. This state occurs after you invoke stop(). | 
| restarting | onRestarting | The application page reloaded inside the same iframe and communication is being re-established. | 
| destroying | onDestroying | Application cleanup is in progress. The application is no longer usable. This state occurs after you invoke destroy(), or when AppManager destroys the application, for example because its contact ended. | 
| destroyed | onDestroyed | The application is fully destroyed. This state occurs up to 5 seconds following the destroy() method invocation. AppManager also emits onAppHostRemoved. The iframe can be safely removed from the DOM. | 
| error | onError | The application encountered an error. The event payload includes an error property. | 

**Important**  
When destroying an application, do not remove it from the Document Object Model (DOM) until the destruction process completes. You can hide it from users, but premature removal from the DOM might interrupt critical cleanup processes such as flushing log buffers or saving state. The `onDestroyed` event indicates when it's safe to completely remove the application.

 **Application visibility states** 

When managing multiple applications, based on how you arrange them, some applications may not be visible at any given time. When an application is temporarily hidden, it's recommended to notify the application by invoking ` stop()` on `AppHost` and then invoking `start()` when making it visible again.

`start()` moves the application to the `running` state and `stop()` moves it to the `stopped` state. Both resolve with a result object, `{ success: true, state }` when the application is in the requested state, or `{ success: false, reason }` when the transition is not possible. The reason is `appNotFound` if the application instance no longer exists.


| State | Description | 
| --- | --- | 
|  running  | The application is visible and actively synchronizing data. | 
|  stopped  | The application is not visible. Background operations are paused. | 

## Handle lifecycle events
<a name="integrate-aws-managed-apps-lifecycle-events"></a>

Implement application lifecycle event handlers to manage iframe visibility and cleanup operations. In the following example, `appIframe` is the iframe element that you passed to `setIFrame`.

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