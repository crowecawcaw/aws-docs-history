# Constants, Functions, and Events for Embedded Amazon WorkSpaces Applications Streaming Sessions

The following topics provide reference information for constants, functions, and events that you can use to configure embedded WorkSpaces Applications streaming sessions.

###### Contents

- [Working with HIDDEN_ELEMENTS](#constants-hidden-elements "#constants-hidden-elements")
- [Functions for the AppStream.Embed Object](#functions-embed-object "#functions-embed-object")
- [Events for Embedded WorkSpaces Applications Streaming Sessions](#events-embedded-streaming-sessions "#events-embedded-streaming-sessions")
- [Examples for Adding Event Listeners and Ending an Embedded WorkSpaces Applications Streaming Session](#examples-add-event-listeners-end-embedded-streaming-session "#examples-add-event-listeners-end-embedded-streaming-session")
  The following WorkSpaces Applications user interface elements can be passed into the `HIDDEN_ELEMENTS` configuration option when an embedded WorkSpaces Applications streaming session is initialized.

## Working with `HIDDEN_ELEMENTS`

The following WorkSpaces Applications user interface elements can be passed as constants into the `HIDDEN_ELEMENTS` configuration option when an embedded WorkSpaces Applications streaming session is initialized.

```
AppStream.Embed.Elements.TOOLBAR
AppStream.Embed.Elements.FULLSCREEN_BUTTON
AppStream.Embed.Elements.END_SESSION_BUTTON
AppStream.Embed.Elements.TOOLBAR
AppStream.Embed.Elements.CATALOG_BUTTON
AppStream.Embed.Elements.WINDOW_SWITCHER_BUTTON
AppStream.Embed.Elements.FILES_BUTTON
AppStream.Embed.Elements.CLIPBOARD_BUTTON
AppStream.Embed.Elements.COPY_LOCAL_BUTTON
AppStream.Embed.Elements.PASTE_REMOTE_BUTTON
AppStream.Embed.Elements.SETTINGS_BUTTON
AppStream.Embed.Elements.STREAMING_MODE_BUTTON
AppStream.Embed.Elements.SCREEN_RESOLUTION_BUTTON
AppStream.Embed.Elements.REGIONAL_SETTINGS_BUTTON
AppStream.Embed.Elements.FULLSCREEN_BUTTON
AppStream.Embed.Elements.END_SESSION_BUTTON
```

The following three elements can be passed as strings into HIDDEN_ELEMENTS, rather than as constants.

| String                      | Description                                                                                                                                                                                                                                                          |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `'adminCommandsButton'`     | When you are connected to an WorkSpaces Applications image builder, the **Admin Commands\*<br>• button displays on the top right corner of the WorkSpaces Applications toolbar. Passing this string into `HIDDEN_ELEMENTS` hides the **Admin Commands\*<br>• button. |
| `'softKeyboardButton'`      | During WorkSpaces Applications streaming sessions on touch-enabled devices, users can tap the keyboard icon on the WorkSpaces Applications toolbar to display the on-screen keyboard. Passing this string into `HIDDEN_ELEMENTS` hides the keyboard icon.            |
| `'keyboardShortcutsButton'` | During WorkSpaces Applications streaming sessions on touch-enabled devices, users can tap the Fn icon on the WorkSpaces Applications toolbar to display keyboard shortcuts. Passing this string into `HIDDEN_ELEMENTS` hides the Fn icon.                            |

## Functions for the `AppStream.Embed` Object

The following table lists the functions that can be performed on the `AppStream.Embed` object.

| Function                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AppStream.Embed(containerId:string, options:object)` | The `AppStream.Embed` object constructor. This constructor initializes and communicates with the `AppStream.Embed` object, and it uses a div container ID. The ID is used to inject the iframe. It also injects an object that includes the configuration options for `appstreamOptions` (`sessionURL` and `HIDDEN_ELEMENTS`).                                                                                     |
| `endSession()`                                        | This function ends the streaming session, but does not destroy the iframe. If you specify a redirect URL, the iframe attempts to load the URL. Depending on the CORS headers of the page, the URL may not load.                                                                                                                                                                                                    |
| `launchApp(appId:string)`                             | This function programmatically launches an application with the application ID that was specified during image creation.                                                                                                                                                                                                                                                                                           |
| `launchAppSwitcher()`                                 | This function sends the **AppSwitcher\*<br>• command to the WorkSpaces Applications portal. This triggers the **AppSwitcher\*<br>• command on the instance.                                                                                                                                                                                                                                                        |
| `getSessionState()`                                   | This function returns an object for `sessionStatus`. For more information, see [Events for Embedded WorkSpaces Applications Streaming Sessions](#events-embedded-streaming-sessions "#events-embedded-streaming-sessions").                                                                                                                                                                                        |
| `getUserInterfaceState()`                             | This function returns an object for `UserInterfaceState`. The object contains the key-value pairs for the following:<br>`sessionStatus`: State enumeration<br>`sessionTerminationReason`: String<br>`sessionDisconnectionReason`: String<br>For more information, see [Events for Embedded WorkSpaces Applications Streaming Sessions](#events-embedded-streaming-sessions "#events-embedded-streaming-sessions"). |
| `addEventListener(name, callback)`                    | This function adds a callback function to call when the specified event is triggered. For a list of the events that can be triggered, see [Events for Embedded WorkSpaces Applications Streaming Sessions](#events-embedded-streaming-sessions "#events-embedded-streaming-sessions").                                                                                                                             |
| `removeEventListener(name, callback)`                 | This function removes the callback for the specified events.                                                                                                                                                                                                                                                                                                                                                       |
| `destroy()`                                           | This function deletes the iframe and cleans up resources. This function does not affect streaming sessions that are in progress.                                                                                                                                                                                                                                                                                   |

## Events for Embedded WorkSpaces Applications Streaming Sessions

The following table lists the events that can be triggered during embedded WorkSpaces Applications streaming sessions.

| Event                                                   | Data                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AppStream.Embed.Events.SESSION_STATE_CHANGE`           | `sessionStatus`: `State enumeration`<br>`sessionTerminationReason`: String<br>`sessionDisconnectionReason`: String | This event is triggered when any session state change occurs. The event includes a map of the states that changed. To retrieve the full session state, use the `getSessionState()` function.<br>Following are the session states:<br>`AppStream.Embed.SessionStatus.Unknown` — The session has not started and is not reserved<br>`AppStream.Embed.SessionStatus.Reserved` — The session is reserved but has not started.<br>`AppStream.Embed.SessionStatus.Started` — The user connected to the session and started streaming.<br>`AppStream.Embed.SessionStatus Disconnected` — The user disconnected from the session.<br>`AppStream.Embed.SessionStatus.Ended` — The session was marked as ended or expired. |
| `AppStream.Embed.Events.SESSION_INTERFACE_STATE_CHANGE` | `hiddenElements`: Array of strings<br>`isFullscreen`: Boolean<br>`isSoftKeyboardVisible`: Boolean                  | This event is triggered when any session state change occurs. The event includes a map of the states that changed. To retrieve the full session state, use the `getSessionState()` function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `AppStream.Embed.Events.SESSION_ERROR`                  | `errorCode`: Number<br>`errorMessage`: String                                                                      | This event is triggered when any errors occur during a session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Examples for Adding Event Listeners and Ending an Embedded WorkSpaces Applications Streaming Session

The examples in this section show how to do the following:

- Add event listeners for embedded WorkSpaces Applications streaming sessions.
- Programmatically end an embedded WorkSpaces Applications streaming session.

### Example 1: Add event listeners for embedded WorkSpaces Applications streaming sessions

To add event listeners for session state changes, session interface state changes, and session errors during embedded streaming sessions, use the following code:

```
appstreamEmbed.addEventListener(AppStream.Embed.Events.SESSION_STATE_CHANGE, updateSessionStateCallback);

appstreamEmbed.addEventListener(AppStream.Embed.Events.SESSION_INTERFACE_STATE_CHANGE, updateUserInterfaceStateCallback);

appstreamEmbed.addEventListener(AppStream.Embed.Events.SESSION_ERROR, errorCallback);
```

In this example, `AppStream.Embed.Events.SESSION_STATE_CHANGE`, `AppStream.Embed.Events.SESSION_INTERFACE_STATE_CHANGE`, and `AppStream.Embed.Events.SESSION_ERROR` are event names.

The `updateSessionStateCallback`, `updateUserInterfaceStateCallback`, and `errorCallback` functions are ones that you implement. These functions are passed into the `addEventListener` function and called when an event is triggered.

### Example 2: Programmatically end an embedded WorkSpaces Applications streaming session

To end an embedded WorkSpaces Applications streaming sessions, use the following function:

```
appstreamEmbed.endSession();
```
