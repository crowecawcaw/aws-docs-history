# Customize stream appearance

## Loading screen

When a customer opens a web browser to view a stream, the web client starts establishing a connection to the Amazon GameLift Streams stream session.
While the stream session loads, you can display a custom background and logo to the customer's screen.

The Amazon GameLift Streams Web SDK sample client, in the
`GameLiftStreamsSampleGamePublisherService/public/LoadingScreen/loadingscreen.js` file, demonstrates how you can
implement an animated logo in your front-end web client. The default loading screen consists of 2 images: background and foreground.
The foreground image is positioned in the middle and has a pulse animation. The animation plays only while the stream session is
connecting.

###### To enable a loading screen

1. In the Amazon GameLift Streams Web SDK sample client, navigate to the
   `GameLiftStreamsSampleGamePublisherService/public/LoadingScreen/` folder.
2. Add your background and foreground images using the default names, `Background.png` and
   `LoadingLogo.png`. If you want to rename them or use a different image format, you must update the code in
   `GameLiftStreamsSampleGamePublisherService/public/loadingscreen.js`.
3. (Optional) In `GameLiftStreamsSampleGamePublisherService/public/loadingscreen.js`, update the JavaScript code to
   implement different animations.
