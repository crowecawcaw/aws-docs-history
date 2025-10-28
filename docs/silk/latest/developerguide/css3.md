# CSS3 support in Amazon Silk

Amazon Silk supports basic CSS3 features like backgrounds, opacity, rounded corners, and text
effects, as well as other features. Though not intended to be comprehensive, this page describes
supported features and notes Amazon Silk-specific implementation details, where applicable.

## Media Queries

###### Topics

Media queries provide a way to apply style rules based on particular media features like
width, height, and resolution. Using media queries, you can deliver layouts that, in effect,
respond to the form factor of the user agent.

Media queries are a key component of [Learn about responsive web design](responsive-design.md "responsive-design.md"). You can use media queries to create a fluid grid that
responds to changes in viewport size. (For more on the viewport, see [viewport Meta Element](#viewport "#viewport")). You can also tailor the user experience to device orientation,
so that your layout changes as the user goes from portrait to landscape mode.

To learn more about media queries, see the following resources:

- [W3C Media Queries
  specification](http://www.w3.org/TR/css3-mediaqueries/ "http://www.w3.org/TR/css3-mediaqueries/")
- [Media Queries](http://mediaqueri.es/ "http://mediaqueri.es/")

## Transform Property (2D)

The CSS3 `transform` property can be used to rotate, scale, skew, and otherwise
alter an element. You can use the `transform` property to make a web page more
interactive.

For more information, see [CSS3 transform
Property](http://www.w3schools.com/cssref/css3_pr_transform.asp "http://www.w3schools.com/cssref/css3_pr_transform.asp").

## Transitions

Using a CSS3 `transition`, you can add an effect to a property change, without
employing JavaScript. The result is an element that changes from one style to another, like an
animation.

For more information, see the W3C specification [CSS Transitions](http://www.w3.org/TR/css3-transitions/ "http://www.w3.org/TR/css3-transitions/").

## viewport Meta Element

The viewport represents the display area available to the browser. The viewport can be
bigger or smaller than the physical screen of the device, and it doesn't include browser
chrome (the browser borders and controls). For some calculations, it may be useful to
differentiate between a visual viewport (the dimensions of the area visible on the screen) and
a layout viewport (the dimensions of the entire display area). For more on the visual and
layout viewports, see Peter-Paul Koch's [A tale of two viewports — part
two](http://www.quirksmode.org/mobile/viewports2.html "http://www.quirksmode.org/mobile/viewports2.html").

For more information on the `viewport` meta element, see the following
resources:

- [Learn about responsive web design](responsive-design.md "responsive-design.md")
- [W3C:
  Viewport META Element](http://www.w3.org/TR/css-device-adapt/#viewport-meta-element "http://www.w3.org/TR/css-device-adapt/#viewport-meta-element")
