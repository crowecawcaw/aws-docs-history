# Programmatically disconnect the chat

session of an Amazon Connect communication widget

You can disconnect the chat session of a communication widget programmatically using
'JavaScript by calling the `disconnect` method stored to the widget's
`iframe`. From the widget's host document, you can reference the
`disconnect` function using the following code snippet:

```
document.getElementById("amazon-connect-chat-widget-iframe").contentWindow.connect.ChatSession.disconnect()
```

You can readily add it to the existing widget script. Following is an example code
snippet:

```
<script type="text/javascript">
  (function(w, d, x, id){
    s=d.createElement('script');
    s.src='https://`your-instance-alias`.my.connect.aws/connectwidget/static/amazon-connect-chat-interface-client.js';
    s.async=1;
    s.id=id;
    d.getElementsByTagName('head')[0].appendChild(s);
    w[x] =  w[x] || function() { (w[x].ac = w[x].ac || []).push(arguments) };
  })(window, document, 'amazon_connect', '...');
  amazon_connect('styles', { iconType: 'CHAT', openChat: { color: '#ffffff', backgroundColor: '#123456' }, closeChat: { color: '#ffffff', backgroundColor: '#123456'} });
  amazon_connect('snippetId', '...');
  amazon_connect('supportedMessagingContentTypes', [ 'text/plain', 'text/markdown', 'application/vnd.amazonaws.connect.message.interactive', 'application/vnd.amazonaws.connect.message.interactive.response' ]);

  // Add disconnect event listener
  window.addEventListener("pagehide", () => {
      document.getElementById("amazon-connect-chat-widget-iframe").contentWindow.connect.ChatSession.disconnect();
  });
</script>
```

## Implementation and use

cases

Calling disconnect programmatically can be useful in multiple cases. It provides
more control on when to terminate the conversation outside of manually clicking the
`End Chat` button. Here are some common use cases for when to call
`disconnect`.

### On close or navigation

A common use case would be to attach the disconnect functionality to events
that fire when the browser or tab context is destroyed. `pagehide`
and `beforeunload` are the common events that are fired when tearing
down the browser. These are triggered when a user refreshes, navigates to a
different URL or closes the tab or browser. Although both events are fired when
the browser context is destroyed, there is no guarantee that the
`disconnect` function can fully execute before the browser’s
resources are cleaned up.

`pagehide` is a more modern page lifecycle event and is supported
across all major browsers and operating systems. `beforeunload` is an
alternative event to try if the `pagehide` event fails to call
disconnect consistently. `beforeunload` is triggered before
`pagehide` which may provide additional reliability if the
`disconnect` function is failing to complete before the browser
is closed. There have been reliability issues regarding
`beforeunload` especially on iOS devices.

Following is an example code snippet:

```
// Call disconnect when `beforeunload` triggers
window.addEventListener("beforeunload", (event) => {
    document.getElementById("amazon-connect-chat-widget-iframe").contentWindow.connect.ChatSession.disconnect();
});

// Call disconnect when `pagehide` triggers
window.addEventListener("pagehide", (event) => {
    document.getElementById("amazon-connect-chat-widget-iframe").contentWindow.connect.ChatSession.disconnect();
});
```

### On context switching

Another use case would be to trigger a disconnect when the user switches
contexts such as when a user switches or minimizes the tab/app or locks their
screen. The `visibilitychange` event can reliably handle these
scenarios where the context is no longer visible.

Following is an example code snippet:

```
window.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "hidden") {
        document.getElementById("amazon-connect-chat-widget-iframe").contentWindow.connect.ChatSession.disconnect();
    } else if (document.visibilityState === "visible") {
        ...
    }
});
```
