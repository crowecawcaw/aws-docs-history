

# Amazon GameLift Streams compatible devices and browsers
<a name="compatible-devices-browsers"></a>

With Amazon GameLift Streams, you can stream applications to end users at up to 1080p resolution at 60 frames per second. Streaming uses web browsers and WebView-based clients through WebRTC. Client browsers and runtimes must support WebRTC and Advanced Video Coding (AVC), also known as H.264. Client devices must support OpenGL ES 2.0 or higher.

The following tables show the minimum supported OS versions. Later versions that remain supported by their respective vendors are also supported. Versions that have reached end-of-life from their vendor are not supported.

Overall, we recommend Google Chrome, Microsoft Edge, or a custom Chromium-based desktop application for the best end-user experience and maximum compatibility, particularly with game controllers.

For information about game controller compatibility with web browsers, see the [Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API) on the MDN Web Docs website. Although some guidance might not apply to Amazon GameLift Streams, most game controllers connect successfully through Bluetooth. For Amazon GameLift Streams-specific controller limitations, see [Known issues](#compatible-devices-browsers-known-issues) and [Limitations](#compatible-devices-browsers-limits) in this topic.

## Desktop devices
<a name="compatible-devices-browsers-desktop"></a>

The following table lists supported desktop devices, browsers, and input options.


| Device | Minimum supported OS version | Supported browsers | Input | 
| --- | --- | --- | --- | 
| Windows PC | Windows 11 24H2 or later | Chrome 133\+, Edge 133\+, CEF | Keyboard, mouse, microphone, game controller (including haptic feedback): Xbox (USB or Bluetooth, fully supported), PlayStation 5 DualSense (USB or Bluetooth, partial support through XInput), PlayStation 4 DualShock 4 (USB or Bluetooth) | 
| Windows PC | Windows 11 24H2 or later | Firefox 128 ESR\+ | Keyboard, mouse, microphone, game controller: Xbox (USB or Bluetooth). PlayStation 5 and Luna controllers are not supported in Firefox. | 
| macOS | macOS 15.3 or later | Chrome 133\+, Safari 18.3\+, Edge 133\+, CEF | Keyboard, mouse, microphone, game controller in Bluetooth mode (including haptic feedback): Xbox (fully supported), PlayStation 5 DualSense (partial support through XInput), PlayStation 4 DualShock 4 | 
| macOS | macOS 15.3 or later | Firefox 128 ESR\+ | Keyboard, mouse, microphone | 
| Linux\* | Ubuntu LTS or later | Chrome 133\+, Firefox 128 ESR\+, Edge 133\+, CEF | Keyboard, mouse, game controller: Xbox (USB or Bluetooth, fully supported), PlayStation 5 DualSense (USB or Bluetooth, partial support through XInput; not supported in Firefox), PlayStation 4 DualShock 4 (USB or Bluetooth) | 

\* Supported with caveats. Gamepad is not detected in Firefox on Ubuntu. Use Chrome, Edge, or a Chromium-based application for game controller support on Linux.

## Mobile devices
<a name="compatible-devices-browsers-mobile"></a>

The following table lists supported mobile devices, browsers, and input options.


| Device | Minimum supported OS version | Supported browsers | Input | 
| --- | --- | --- | --- | 
| iPhone | iOS 26.4 or later | Chrome 133\+, Firefox 128 ESR\+, Safari 18.3\+, Edge 133\+, WebView | Touch (virtual gamepad), microphone, game controller: Xbox (Bluetooth, fully supported), PlayStation 5 DualSense (Bluetooth, partial support through XInput; not supported in Firefox). Limited keyboard and mouse. | 
| iPad | iPadOS 18.3.1 or later | Chrome 133\+, Firefox 128 ESR\+, Safari 18.3\+, Edge 133\+, WebView | Touch (virtual gamepad), microphone, game controller: Xbox (Bluetooth, fully supported), PlayStation 5 DualSense (Bluetooth, partial support through XInput; not supported in Firefox). Limited keyboard and mouse. | 
| Android phones and tablets | Android 16 or later | Chrome 133\+, Edge 133\+, WebView | Touch (virtual gamepad), microphone\*, game controller: Xbox (Bluetooth, fully supported), PlayStation 5 DualSense (Bluetooth, partial support through XInput). Limited keyboard and mouse. | 

**Note**  
The virtual gamepad touch overlay is intended for casual interaction and short sessions. For extended gameplay, a Bluetooth game controller provides more responsive and comfortable input.

\* Microphone is not supported on Pixel 9 devices. See [Known issues](#compatible-devices-browsers-known-issues) for details.

## TV devices
<a name="compatible-devices-browsers-tv"></a>

The following table lists supported TV devices, browsers, and input options.


| Device | Minimum supported OS version | Supported browsers | Input | 
| --- | --- | --- | --- | 
| Samsung Smart TV\* (2023 models and later) | Tizen OS 9 or later | Samsung native app (recommended), Samsung Internet browser, WebView | Game controller: Xbox (Bluetooth, fully supported), PlayStation 5 DualSense (Bluetooth, partial support through XInput). Limited keyboard and mouse. | 
| LG Smart TV (2024 models and later) | webOS 25 or later | LG webOS native app, LG TV browser, WebView | Game controller: Xbox (Bluetooth, fully supported), PlayStation 5 DualSense (Bluetooth, partial support through XInput). Limited keyboard and mouse. | 
| Amazon Fire TV Stick 4K Max (1st and 2nd Gen) | Fire TV OS 7.7 or later | Firefox 128 ESR\+ (recommended), WebView | Game controller: Xbox (Bluetooth, fully supported), PlayStation 5 DualSense (Bluetooth, partial support through XInput; WebView only, not supported in Firefox). Limited keyboard and mouse. | 

\* Supported with caveats. On 2025 models, the Samsung native app is recommended for the best experience. The browser and WebView might deliver a reduced frame rate on these models.

## Known issues
<a name="compatible-devices-browsers-known-issues"></a>

Following are known issues with devices, browsers, and input:
+ Safari exits fullscreen immediately whenever `Esc` is pressed. Safari does not allow you to override this behavior.
+ "Embedded" or "in-app" browser views like those inside mobile apps such as LinkedIn, Yelp, Instagram, and others are not supported on iOS. These tend to disable the browser WebRTC support necessary for realtime interactive streaming. We recommend detecting non-standard browser strings and prompting them to open in Safari.
+ If the screen resolution in your application differs from the stream resolution, mouse tracking might not work correctly. When using a non-default resolution, we recommend testing mouse input behavior, disabling windowed mode, and running in full screen.
+ Gamepad input is not fully supported in the default Amazon Silk browser on Fire TV. Use Firefox or a WebView-based application instead.
+ Samsung Smart TV, LG Smart TV, Amazon Fire TV, Pixel 9, and Chromium Embedded Framework (CEF) clients do not support microphone input.

## Limitations
<a name="compatible-devices-browsers-limits"></a>

The following limitations apply to game controller support, haptic feedback, microphone, and input on Amazon GameLift Streams:
+ The PlayStation 5 and Luna game controllers are not supported in Firefox.
+ Haptic feedback support:
  + Haptic feedback is supported on the PlayStation 4 and Xbox Series S/X controllers in Chrome, Edge, and Safari.
  + Haptic feedback on the PlayStation 5 DualSense controller is supported only in the Safari browser.
  + Firefox does not support haptic feedback on any controller.
  + Android and iOS devices do not support haptic feedback on any controller.
+ The **Test stream** feature in the Amazon GameLift Streams console does not support microphones. To test microphone input, use the sample publisher application included in the Web SDK bundle.
+ Keyboard and mouse input on TV and mobile devices works for menu navigation and UI interaction. In-game keyboard and mouse support is limited due to pointer lock restrictions on these platforms. We recommend a game controller for gameplay.
+ For best network performance, use a wired connection or 5 GHz Wi-Fi.

## Runtimes and input support
<a name="compatible-devices-browsers-runtime"></a>

The following table shows input support for each Amazon GameLift Streams runtime environment on the server side. For a list of available runtime environments and their capabilities, see [Runtime environments](configuration-options.md#configuration-options-runtime).


| Runtime environment | Keyboard | Mouse | Microphone | Gamepad | 
| --- | --- | --- | --- | --- | 
| Microsoft Windows Server 2022 Base | Yes | Yes | Yes | Yes | 
| Ubuntu 22.04 LTS | Yes | Yes | No | Yes | 
| Proton runtimes | Yes | Yes | Yes | Yes | 

### Runtime limitations and known issues
<a name="compatible-devices-browsers-runtime-limits"></a>
+ Games running in Proton runtime environments *always* show a game controller as connected, even if the client has no controller plugged in. This supports plug-and-play behavior for game controllers, but can be an issue for games that prompt for controller input even when the controller is idle and unused. We recommend that games show input UI based on the last input method.
+ Ubuntu 22.04 LTS supports gamepad input for applications that use the Simple DirectMedia Layer (SDL) libraries. If your application uses other input libraries, gamepad functionality might not work. If you experience issues, consider using a Proton or Windows runtime environment instead.