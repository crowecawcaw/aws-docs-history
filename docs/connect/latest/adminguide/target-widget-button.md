# Target your Amazon Connect widget button and frame with

CSS/JavaScript

The communication widget renders the open/close widget button and the widget frame
directly on the host website. There are specific selectors that you can use to either
target these elements using CSS or reference them in JavaScript.

###### Tip

To update the colors of the widget button, or the styles of the widget itself, use
the [Amazon Connect admin website](add-chat-to-website.md#customize-chat-widget "add-chat-to-website.md#customize-chat-widget"). For more customizable
styles, you can [pass custom styles](pass-custom-styles.md "pass-custom-styles.md")
directly to the communications widget.

## Widget element IDs and examples

The following images show how the chat widget button appears on the user's screen.
The first image shows Open button to open the chat widget. The second image shows
the Close button to close the chat widget.

![Side-by-side images of the chat widget to open and to close the chat window.](images/widget-elements.png)

1. Open widget button: `#amazon-connect-open-widget-button`
2. Close widget button:
   `#amazon-connect-close-widget-button`
3. Widget frame: `#amazon-connect-widget-frame`
   1. Widget frame while open:
      `#amazon-connect-widget-frame.show`
   2. Widget frame while closed:
      `#amazon-connect-widget-frame:not(.show)`

Following is an example of a CSS style sheet that modifies these elements:

```
/* Target widget button while widget is minimized */
#amazon-connect-open-widget-button {
  ...
}

/* Target widget button while widget is showing */
#amazon-connect-close-widget-button {
  ...
}

/* Target widget frame */
#amazon-connect-widget-frame {
  ...
}

/* Target widget frame while it is showing */
#amazon-connect-widget-frame.show {
  ...
}

/* Target widget frame while it is minimized */
#amazon-connect-widget-frame:not(.show) {
  ...
}
```

Following is an example of referencing these elements using JavaScript:

```
const openWidgetButton = document.getElementById("amazon-connect-open-widget-button");
const closeWidgetButton = document.getElementById("amazon-connect-close-widget-button");

const widgetFrame = document.querySelector("#amazon-connect-widget-frame");
const openWidgetFrame = document.querySelector("#amazon-connect-widget-frame.show");
const hiddenWidgetFrame = document.querySelector("#amazon-connect-widget-frame:not(.show)");
```
