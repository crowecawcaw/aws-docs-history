# Supported browsers and input

The following lists the supported platforms and browsers for viewing Amazon GameLift Streams streams and their compatible input peripherals. Browsers
must also be compatible with advanced video coding (AVC), also known as H.264.

Overall, we recommend Google Chrome, Microsoft Edge, or a custom Chromium-based desktop application for the best end-user experience and
maximum compatibility, particularly with game controllers.

To learn more about which controllers are compatible with which browsers, see the [Web Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API "https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API"). Although some guidance may not apply to
Amazon GameLift Streams, we expect most game controllers to connect successfully via Bluetooth.

| Operating system | Browser                                      | Input                                                                                                                     |
| ---------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Windows          | Chrome, Edge                                 | Keyboard, mouse, microphone, game controller (including haptic feedback)                                                  |
| Firefox          | Keyboard, mouse, microphone, game controller |
| Mac              | Chrome, Edge, Safari                         | Keyboard, mouse, microphone, game controller (in Bluetooth mode) (including haptic feedback)                              |
| Firefox          | Keyboard, mouse, microphone                  |
| Linux            | Chrome, Edge, Firefox                        | Keyboard, mouse                                                                                                           |
| Android          | Chrome, Edge                                 | Simple touch-to-mouse emulation, microphone, external physical mouse, keyboard and game controller (in Bluetooth<br>mode) |
| iOS              | Chrome, Edge, Firefox, Safari                | Simple touch-to-mouse emulation, microphone, external physical mouse, keyboard and game controller (in Bluetooth<br>mode) |

## Known issues

Following are known issues with browsers and input:

- Safari will immediately exit fullscreen whenever `Esc` is pressed. This cannot be overriden.
- “Embedded” or “in-app” browser views like those inside mobile apps such as LinkedIn, Yelp, Instagram, and others are not
  supported on iOS. These tend to disable the browser WebRTC support necessary for realtime interactive streaming. We recommend
  detecting non-standard browser strings and prompting the user to open in Safari.
- If the screen resolution in your application is not set to 1080p, mouse tracking might be impacted. We recommend disabling
  the selection of any other resolution, if possible. We also recommend disabling windowed mode, and only run in full
  screen.
- To support plug and play of game controllers on Proton, despite the lack of support for them in native Linux applications,
  games running in Proton runtime environments will _always_ show a game controller connected, even if none
  are plugged in on the client. This could be an issue for games that prompt for controller input even when the controller is
  idle and unused. We recommend that games show input UI based on the last input method.

## Limitations

- Most runtime environments support game controllers, except for Ubuntu 22.04 LTS. If you need game controller support, consider
  creating the game using another runtime environment. For a list of other runtime environments, refer to [Runtime environments](configuration-options.md#configuration-options-runtime "configuration-options.md#configuration-options-runtime").
- The PlayStation 5 and Luna game controllers are not supported in Firefox.
- Haptic feedback support:
  - Haptic feedback on the PlayStation 4 and Xbox Series S/X controllers are supported in Chrome, Edge, and
    Safari.
  - Haptics on the PlayStation 5 DualSense controller is only supported in the Safari browser.
  - Firefox does not support haptic feedback on any controller.
  - Android and iOS devices do not support haptic feedback on any controller.

- The **Test stream** feature in the Amazon GameLift Streams console does not support microphones.

## IPv6 support

Streaming to IPv6-only clients is supported only with Windows runtime applications.

| Runtime                            | Streaming over IPv4 | Streaming over IPv6 |
| ---------------------------------- | ------------------- | ------------------- |
| Microsoft Windows Server 2022 Base | Yes                 | Yes                 |
| Ubuntu 22.04 LTS                   | Yes                 | No                  |
| Proton runtimes                    | Yes                 | No                  |
