# Step 4. Configure Your Website for Integration with Amazon AppStream 2.0

The following sections provide information about how to configure your webpage to host embedded AppStream 2.0 streaming sessions.

###### Contents

- [Import the appstream-embed JavaScript File](#import-embed-javascript-file "#import-embed-javascript-file")
- [Initialize and Configure the AppStream.Embed Interface Object](#initialize-configure-embed-interface-object "#initialize-configure-embed-interface-object")
- [Examples for Hiding Items in the AppStream 2.0 User Interface](#examples-hiding-user-interface-items "#examples-hiding-user-interface-items")

## Import the appstream-embed JavaScript File

1. On the webpage where you plan to embed the AppStream 2.0 streaming session, import the **appstream-embed.js** file into the webpage by adding the following code:

```
<script type="text/javascript" src="./appstream_embed.js"> </script>
```

2. Next, create an empty container div. The ID of the div that you set is passed into the AppStream 2.0 embed constructor. It's then used to inject an iframe for the streaming session. To create the div, add the following code:

```
<div id="appstream-container"> </div>
```

## Initialize and Configure the `AppStream.Embed` Interface Object

To initialize the `AppStream.Embed` interface object in JavaScript, you must add code that creates an `AppStream.Embed` object with options for the streaming URL and user interface configuration. These options, and the div ID that you created, are stored in an object called `appstreamOptions`.

The following example code shows how to initialize the `AppStream.Embed` interface object.

```
var appstreamOptions = {
     sessionURL: '`https://appstream2.``region``.aws.amazon.com/authenticate?parameters=``authenticationcode`...',
     userInterfaceConfig:{[AppStream.Embed.Options.HIDDEN_ELEMENTS]:[AppStream.Embed.Elements.TOOLBAR]}
 };
 appstreamEmbed = new AppStream.Embed("appstream-container", appstreamOptions);

```

In the code, replace `sessionURL` and `userInterfaceConfig` with your own values.

###### Note

The value specified for `userInterfaceConfig` hides the entire AppStream 2.0 toolbar. This value, which is included as an example, is optional.

**`sessionUrl`**

The streaming URL that you created by using the AppStream 2.0 console, the [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md") API action, or the [create-streaming-url](../../../cli/latest/reference/appstream/create-streaming-url.md "../../../cli/latest/reference/appstream/create-streaming-url.md") AWS CLI command. This parameter is case-sensitive.

**Type**: String

**Required**: Yes

**`userInterfaceConfig`**

The configuration that generates the initial state of the user interface elements. The configuration is a key-value pair.

The key, `AppStream.Embed.Options.HIDDEN_ELEMENTS`, specifies the user interface objects that are initially hidden when the embedded AppStream 2.0 streaming session is initialized. Later, you can return both hidden and visible objects by using the `getInterfaceState` parameter.

The value is an array of constants (toolbar buttons). For a list of constants that you can use, see [Working with HIDDEN_ELEMENTS](constants-functions-events-embedded-sessions.md#constants-hidden-elements "constants-functions-events-embedded-sessions.md#constants-hidden-elements").

**Type**: Map (`key`:`value`)

**Required**: No

## Examples for Hiding Items in the AppStream 2.0 User Interface

The examples in this section show how to hide items in the AppStream 2.0 user interface from users during their embedded AppStream 2.0 streaming sessions.

###### Examples

- [Example 1: Hide the entire AppStream 2.0 toolbar](#example-hide-the-entire-tooolbar "#example-hide-the-entire-tooolbar")
- [Example 2: Hide a specific button on the AppStream 2.0 toolbar](#example-hide-a-specific-toolbar-button "#example-hide-a-specific-toolbar-button")
- [Example 3: Hide multiple buttons on the AppStream 2.0 toolbar](#example-hide-multiple-toolbar-buttons "#example-hide-multiple-toolbar-buttons")

### Example 1: Hide the entire AppStream 2.0 toolbar

To prevent users from accessing any button on the AppStream 2.0 toolbar during embedded streaming sessions, use the `AppStream.Embed.Elements.TOOLBAR` constant. This constant lets you hide all AppStream 2.0 toolbar buttons.

```
var appstreamOptions = {
     sessionURL: '`https://appstream2.``region``.aws.amazon.com/authenticate?parameters=``authenticationcode`...',
     userInterfaceConfig:{[AppStream.Embed.Options.HIDDEN_ELEMENTS]:[AppStream.Embed.Elements.TOOLBAR]}
 };
```

### Example 2: Hide a specific button on the AppStream 2.0 toolbar

You can display the AppStream 2.0 toolbar, while preventing users from accessing a specific toolbar button during embedded streaming sessions. To do so, specify the constant for the button that you want to hide. The following code uses the `AppStream.Embed.Elements.FILES_BUTTON` constant to hide the **My Files** button. This prevents users from accessing persistent storage options during embedded streaming sessions.

```
var appstreamOptions = {
     sessionURL: '`https://appstream2.``region``.aws.amazon.com/authenticate?parameters=``authenticationcode`...',
     userInterfaceConfig:{[AppStream.Embed.Options.HIDDEN_ELEMENTS]:[AppStream.Embed.Elements.FILES_BUTTON]}
 };
```

### Example 3: Hide multiple buttons on the AppStream 2.0 toolbar

You can display the AppStream 2.0 toolbar, while preventing users from accessing more than one toolbar button during embedded streaming sessions. To do so, specify the constants for the buttons that you want to hide. The following code uses the `AppStream.Embed.Elements.END_SESSION_BUTTON` and `AppStream.Embed.Elements.FULLSCREEN_BUTTON` constants to hide the **End Session** and **Fullscreen** buttons.

###### Note

Separate each constant with a comma, with no preceding or following space.

```
var appstreamOptions = {
     sessionURL: '`https://appstream2.``region``.aws.amazon.com/authenticate?parameters=``authenticationcode`... `(https://appstream2.``region``.aws.amazon.com/#/)`',
     userInterfaceConfig:{[AppStream.Embed.Options.HIDDEN_ELEMENTS]:[AppStream.Embed.Elements.END_SESSION_BUTTON,AppStream.Embed.Elements.FULLSCREEN_BUTTON]}
 };
```
