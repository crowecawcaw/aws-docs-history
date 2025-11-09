# Customize widget launch behavior and button

icon for your website hosted in Amazon Connect

To further customize how your website renders and launches the hosted widget icon, you
can configure the launch behavior and hide the default icon. For example, you can
programmatically launch the widget from a **Chat with us** button
element that is rendered on your website.

###### Contents

- [How to configure custom launch
  behavior for the widget](#config-widget-launch "#config-widget-launch")
- [Supported options and
  constraints](#launch-options-constraints "#launch-options-constraints")
- [Configure widget launch for custom use
  cases](#launch-usage "#launch-usage")
- [Enable chat session
  persistence across tabs](#chat-persistence-across-tabs "#chat-persistence-across-tabs")

## How to configure custom launch behavior for

the widget

To pass custom launch behavior, use the following example code block and embed it
in your widget. All of the fields shown in the following example are optional and
any combination can be used.

```
amazon_connect('customLaunchBehavior', {
    skipIconButtonAndAutoLaunch: true,
    alwaysHideWidgetButton: true,
    programmaticLaunch: (function(launchCallback) {
        var launchWidgetBtn = document.getElementById('launch-widget-btn');
        if (launchWidgetBtn) {
            launchWidgetBtn.addEventListener('click', launchCallback);
            window.onunload = function() {
            launchWidgetBtn.removeEventListener('click', launchCallback);
            return;
            }
        }
    })
});
```

## Supported options and

constraints

The following table lists the supported custom launch behavior options. Fields are
optional and any combination can be used.

| Option name                   | Type     | Description                                                                                                  | Default value |
| ----------------------------- | -------- | ------------------------------------------------------------------------------------------------------------ | ------------- |
| `skipIconButtonAndAutoLaunch` | Boolean  | A flag to enable/disable the automatic launch of the widget<br>without the user clicking on the page load.   | undefined     |
| `alwaysHideWidgetButton`      | Boolean  | A flag to enable/disable the widget icon button from rendering<br>(unless there is an ongoing chat session). | undefined     |
| `programmaticLaunch`          | Function |                                                                                                              | undefined     |

## Configure widget launch for custom use cases

### Custom widget launch button

The following example shows changes you would need to make in the widget to
configure programmatic launch to open only when the user chooses a custom button
element rendered anywhere on your website. For example, they may choose a button
named **Contact Us** or **Chat With Us**.
Optionally, you can hide the default Amazon Connect widget icon until the widget has been
opened.

```
<button id="launch-widget-btn">Chat With Us</button>
```

```
<script type="text/javascript">
 (function(w, d, x, id){
    s=d.createElement("script");
    s.src="./amazon-connect-chat-interface-client.js"
    s.async=1;
    s.id=id;
    d.getElementsByTagName("head")[0].appendChild(s);
    w[x] =  w[x] || function() { (w[x].ac = w[x].ac || []).push(arguments) };
  })(window, document, 'amazon_connect', 'asfd-asdf-asfd-asdf-asdf');
  amazon_connect('styles', { openChat: { color: '#000', backgroundColor: '#3498fe'}, closeChat: { color: '#fff', backgroundColor: '#123456'} });
  amazon_connect('snippetId', "QVFJREFsdafsdfsadfsdafasdfasdfsdafasdfz0=")
  amazon_connect('customLaunchBehavior', {
        skipIconButtonAndAutoLaunch: true,
        alwaysHideWidgetButton: true,
        programmaticLaunch: (function(launchCallback) {
            var launchWidgetBtn = document.getElementById('launch-widget-btn');
            if (launchWidgetBtn) {
                launchWidgetBtn.addEventListener('click', launchCallback);
                window.onunload = function() {
                launchWidgetBtn.removeEventListener('click', launchCallback);
                return;
                }
            }
        }),
    });
</script>
```

### Hyperlink support

The following example shows changes you would need to make in the widget
configure `auto-launch`, which opens the widget without waiting for
the user to click. You can deploy to a page that hosted by your website to
create a shareable hyperlink.

```
https://example.com/contact-us?autoLaunchMyWidget=true
```

```
<script type="text/javascript">
 (function(w, d, x, id){
    s=d.createElement("script");
    s.src="./amazon-connect-chat-interface-client.js"
    s.async=1;
    s.id=id;
    d.getElementsByTagName("head")[0].appendChild(s);
    w[x] =  w[x] || function() { (w[x].ac = w[x].ac || []).push(arguments) };
  })(window, document, 'amazon_connect', 'asfd-asdf-asfd-asdf-asdf');
  amazon_connect('styles', { openChat: { color: '#000', backgroundColor: '#3498fe'}, closeChat: { color: '#fff', backgroundColor: '#123456'} });
  amazon_connect('snippetId', "QVFJREFsdafsdfsadfsdafasdfasdfsdafasdfz0=")
  amazon_connect('customLaunchBehavior', {
        skipIconButtonAndAutoLaunch: true
    });
</script>
```

### Load widget assets when button is clicked

The following example shows changes you would need to make in the widget to
make your website page load faster by fetching the widget's static assets when a
user clicks the **Chat With Us** button. Typically, only small
percentage of customers visiting a **Contact Us** page open the
Amazon Connect widget. The widget could be adding latency on page load by fetching files
from CDN, even though customers never open the widget.

An alternative solution is to run the snippet code asynchronously (or never)
on button click.

```
<button id="launch-widget-btn">Chat With Us</button>
```

```
var buttonElem = document.getElementById('launch-widget-btn');

buttonElem.addEventListener('click', function() {
    (function(w, d, x, id){
        s=d.createElement("script");
        s.src="./amazon-connect-chat-interface-client.js"
        s.async=1;
        s.id=id;
        d.getElementsByTagName("head")[0].appendChild(s);
        w[x] =  w[x] || function() { (w[x].ac = w[x].ac || []).push(arguments) };
    })(window, document, 'amazon_connect', 'asfd-asdf-asfd-asdf-asdf');
    amazon_connect('styles', { openChat: { color: '#000', backgroundColor: '#3498fe'}, closeChat: { color: '#fff', backgroundColor: '#123456'} });
    amazon_connect('snippetId', "QVFJREFsdafsdfsadfsdafasdfasdfsdafasdfz0=")
    amazon_connect('customLaunchBehavior', {
        skipIconButtonAndAutoLaunch: true
    });
});
```

### Launch a new chat in a browser

window

The following example shows changes you would need to make in the widget to
launch a new browser window and auto-launch chat in a full screen.

```
<button id="openChatWindowButton">Launch a Chat</button>
```

```
<script> // Function to open a new browser window with specified URL and dimensions
    function openNewWindow() {
        var url = 'https://mycompany.com/support?autoLaunchChat=true';

        // Define the width and height
        var width = 300;
        var height = 540;

        // Calculate the left and top position to center the window
        var left = (window.innerWidth - width) / 2;
        var top = (window.innerHeight - height) / 2;

        // Open the new window with the specified URL, dimensions, and position
        var newWindow = window.open(url, '', 'width=${width}, height=${height}, left=${left}, top=${top}');
    }

    // Attach a click event listener to the button
    document.getElementById('openChatWindowButton').addEventListener('click', openNewWindow);
</script>
```

## Enable chat session persistence

across tabs

By default if a chat is opened in one tab and then the user opens a new tab and
starts another chat, a new chat will start instead of connecting to the existing
chat. You can enable chat session persistence across tabs if you want the user to
connect to the existing chat that was started in the initial tab.

The chat session is stored in session storage on the browser in the variable
`persistedChatSession`. You need to copy this value into the session
storage of the new tab when the widget is first initialized. Following are
instructions.

To connect to the same chat session when user navigates to different subdomains,
you can set the domain property of the cookie. For example, you own two subdomains:
`domain1.example.com` and `domain2.example.com`. You can
add the property `domain=.example.com` so that the cookie can be accessed
from all subdomains.

1. Copy the following code next to the other amazon_connect functions in the
   hosted widget snippet. This uses the `registerCallback` event
   handlers to store the `persistedChatSession` as a cookie so it
   can be accessed in the new tab. It also cleans up the cookie when the chat
   ends.

```
amazon_connect('registerCallback', {
'CONNECTION_ESTABLISHED': (eventName, { chatDetails, data }) => {
 document.cookie = `activeChat=${sessionStorage.getItem("persistedChatSession")}; SameSite=None; Secure`;
},
'CHAT_ENDED': () => {
  document.cookie = "activeChat=; SameSite=None; Secure";
}
});
```

2. Retrieve the cookie value if it exists and set the session storage value
   in the new tab.

```
const cookie = document.cookie.split('; ').find(c => c.startsWith('activeChat='));
if (cookie) {
  const activeChatValue = cookie.split('=')[1];
  sessionStorage.setItem('persistedChatSession', activeChatValue);
}

//Your hosted widget snippet should be on this page
```
