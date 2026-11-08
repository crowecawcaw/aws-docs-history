

# AppManager and AppHost reference
<a name="integrate-aws-managed-apps-reference"></a>

This section lists AppManager and `AppHost` members that the previous sections do not describe.

## AppManager members
<a name="integrate-aws-managed-apps-reference-appmanager"></a>

The following members are available on `provider.appManager` from the `@amazon-connect/app-manager` package.


| Member | Signature | Description | 
| --- | --- | --- | 
| getAppHost | getAppHost(appInstanceId: string): AppHost \| undefined | Returns the AppHost for an application instance, or undefined if the instance is not known. | 
| listAppHosts | listAppHosts(): AppHost[] | Returns the AppHost objects for all application instances that AppManager tracks. | 
| getAppConfig | getAppConfig(arnOrName: string): Promise<AppConfig> | Returns the configuration of a single application, identified by ARN or name. | 
| destroyInstance | destroyInstance(appInstanceId: string): Promise<void> | Destroys an application instance by ID and resolves when destruction completes. | 
| clearAll | clearAll(): Promise<{ appInstanceIds: string[]; serviceInstanceIds: string[] }> | Destroys all application and service instances, and returns the IDs of the destroyed instances. | 
| destroy | destroy(): void | Starts destroying all instances, as clearAll does, without waiting for the result, and removes the event subscriptions of this AppManager. Call it when you no longer use the AppManager. | 
| onAppHostRemoved, offAppHostRemoved | onAppHostRemoved(handler: AppHostRemovedHandler, appInstanceId?: string): void | Pass appInstanceId to receive the event for a single instance only. Without it, the handler receives the event for every instance. | 
| offAppHostFocused | offAppHostFocused(handler: AppFocusedHandler): void | Removes a handler that you added with onAppHostFocused. The event payload is { host: AppHost; focusRequestTime: number }. | 

## Launch options
<a name="integrate-aws-managed-apps-reference-launch-options"></a>

In addition to `launchKey`, `appManagerData`, and `scope`, `AppLaunchOptions` supports the following properties. The `scope` property is available after you import `@amazon-connect/app-manager-agent`.


| Property | Type | Description | 
| --- | --- | --- | 
| parameters | AppParameters (optional) | JSON data that is passed to the application. Values must be strings, numbers, or Booleans. Nested data is allowed. The application reads it from the parameters field of its context. | 
| openInBackground | boolean (optional) | When true, the newly started application is not focused when it is ready. | 

When `launchKey` matches an existing application instance, all other launch options are ignored.

## AppHost members
<a name="integrate-aws-managed-apps-reference-apphost"></a>

Each lifecycle event has an `on` and an `off` form with the same handler type, for example `onRunning(handler)` and `offRunning(handler)`. Unless noted, the event payload is `{ host: AppHost; state: ComponentState; previous: { state: ComponentState } }`.


| Member | Signature | Description | 
| --- | --- | --- | 
| getState | getState(): Promise<{ state: ComponentState; version: number }> | Returns the current lifecycle state of the instance. | 
| start | start(): Promise<{ success: true; state: "running" } \| { success: false; reason: string }> | Moves the instance to the running state. | 
| stop | stop(): Promise<{ success: true; state: "stopped" } \| { success: false; reason: string }> | Moves the instance to the stopped state. | 
| destroy | destroy(options?: { waitForCompletion?: boolean }): Promise<{ destroyStarted: boolean; destroyCompleted: boolean }> | Destroys the instance. By default, the promise resolves when destruction starts, and destroyCompleted is false. With waitForCompletion: true, the promise resolves when destruction completes, and both values are true. | 
| onStateChanged, offStateChanged | onStateChanged(handler: AppStateChangedHandler): void | Emitted on every state transition. | 
| onProvisioned, offProvisioned | onProvisioned(handler: AppProvisionedHandler): void | Emitted when the instance enters the provisioned state. | 
| onRunning, offRunning | onRunning(handler: AppRunningHandler): void | Emitted when the instance enters the running state. | 
| onStopped, offStopped | onStopped(handler: AppStoppedHandler): void | Emitted when the instance enters the stopped state. | 
| onRestarting, offRestarting | onRestarting(handler: AppRestartingHandler): void | Emitted when the instance enters the restarting state. | 
| offDestroying, offDestroyed | offDestroying(handler: AppDestroyingHandler): void | Remove handlers added with onDestroying and onDestroyed. | 
| onError, offError | onError(handler: AppErrorHandler): void | Emitted when the instance enters the error state. The payload also includes error: unknown. | 
| onFocus, offFocus | onFocus(handler: AppFocusedHandler): void | Emitted when focus is requested for this instance, for example when a launch with a matching launchKey returns it. The payload is { host: AppHost; focusRequestTime: number }. | 

## Contact-scoped AppManager members
<a name="integrate-aws-managed-apps-reference-agent"></a>

Importing the `@amazon-connect/app-manager-agent` package adds the following members to AppManager, in addition to `setActiveContact`. Applications are grouped by scope: an `AppScopeGroup` holds the applications that share one scope, and a `ContactScopeGroup` is an `AppScopeGroup` whose scope is a contact scope.


| Member | Signature | Description | 
| --- | --- | --- | 
| getActiveContact | getActiveContact(): Promise<{ activeContactId: string \| null } \| undefined> | Returns the active contact that AppManager uses for launches without a scope value. activeContactId is null when no contact is active. | 
| onActiveContactChanged, offActiveContactChanged | onActiveContactChanged(handler: ActiveContactChangedHandler): void | Emitted when the active contact changes. The payload is { activeContactId: string \| null }. | 
| getIdleStateGroup | getIdleStateGroup(): Promise<AppScopeGroup> | Returns the group of applications that have the idle scope. | 
| listContactGroups | listContactGroups(): Promise<Record<string, ContactScopeGroup>> | Returns the contact scope groups, keyed by contact ID. | 
| getContactGroup | getContactGroup(contact: string): Promise<ContactScopeGroup \| undefined> | Returns the scope group for one contact ID, or undefined if none exists. | 
| onContactGroupAdded, offContactGroupAdded | onContactGroupAdded(handler: ContactScopeGroupAddedHandler): void | Emitted when a contact scope group is created. The payload is { scopeGroup: ContactScopeGroup }. | 
| onContactGroupDestroying, offContactGroupDestroying | onContactGroupDestroying(handler: ContactScopeGroupDestroyingHandler, contact?: string): void | Emitted when a contact scope group starts being destroyed, for example because the contact ended. The payload is { scopeGroup: ContactScopeGroup; destroyingAppHosts: AppHost[] }. Pass contact to receive the event for one contact only. | 
| onContactGroupRemoved, offContactGroupRemoved | onContactGroupRemoved(handler: ContactScopeGroupRemovedHandler, contact?: string): void | Emitted when a contact scope group is removed. The payload is { scopeGroup: ContactScopeGroup }. Pass contact to receive the event for one contact only. | 
| getActiveAppScopeGroup | getActiveAppScopeGroup(): Promise<AppScopeGroup> | Returns the scope group for the active contact. | 
| onActiveAppScopeGroupChanged, offActiveAppScopeGroupChanged | onActiveAppScopeGroupChanged(handler: ActiveAppScopeGroupChangedHandler): void | Emitted when the active scope group changes. The payload is { scopeGroup: AppScopeGroup }. | 

An `AppScopeGroup` has the following members.


| Member | Signature | Description | 
| --- | --- | --- | 
| scope, key | readonly scope: Readonly<AppScope>, readonly key: AppScopeKey | The scope that the group represents, and its key. | 
| getAppHosts | getAppHosts(options?: { includeDestroying?: boolean }): Promise<AppHost[]> | Returns the AppHost objects in the group, in launch order. Set includeDestroying to include instances that are being destroyed. | 
| onAppHostAdded, onAppHostDestroying, onAppHostRemoved, and their off forms | onAppHostAdded(handler: AppHostInScopeGroupAddedHandler): void | Emitted when an instance is added to, starts being destroyed in, or is removed from the group. The added and destroying payloads are { scopeGroup; appHost }. The removed payload is { scopeGroup; appInstanceId }. | 
| startAll, stopAll | startAll(options?: { includeAppsWithoutScope?: boolean }): Promise<{ startedAppInstanceIds: string[] }> | Starts or stops every instance in the group. stopAll resolves with { stoppedAppInstanceIds: string[] }. Set includeAppsWithoutScope to include instances without a scope. | 