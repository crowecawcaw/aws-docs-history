# Mouse movement handling

Mouse movement handling is critical for delivering responsive and intuitive user experiences in streamed applications. Amazon GameLift Streams automatically
optimizes mouse input transmission based on your application's cursor behavior, ensuring that mouse movements feel natural whether the cursor
is hidden or visible. Understanding how Amazon GameLift Streams processes mouse events helps you design applications that work seamlessly with the streaming
service and provide the best possible user experience.

## Mouse input modes

Amazon GameLift Streams uses two distinct modes for transmitting mouse events to your application, automatically selecting the appropriate mode based on
cursor visibility:

Relative mode

In relative mode, mouse updates are transmitted as small, incremental differences from the previous position. This mode is
ideal for applications that require precise, continuous mouse movement tracking, such as first-person shooter (FPS) games or
interfaces that use 3D orientation. Amazon GameLift Streams uses relative mode when the operating system cursor is hidden or fully
transparent.

Absolute mode

In absolute mode, the mouse cursor position is transmitted as an exact screen coordinate. This mode works well for
applications that rely on precise cursor positioning, such as point-and-click games or any UI with clickable elements. Amazon GameLift Streams
uses absolute mode when the operating system cursor is visible, even if your application displays a custom cursor
image.

This automatic selection ensures optimal performance for different application types without requiring manual configuration.

## Pointer lock

Pointer lock is a web API feature that captures the mouse cursor within a specific element, hiding the cursor and preventing it from
leaving the designated area. This feature is particularly valuable for games that require unrestricted mouse movement for camera control
or aiming, without the distraction of a visible cursor or the limitation of reaching window edges.

Amazon GameLift Streams provides automatic pointer lock functionality through the `autoPointerLock` property in the Web SDK's
`InputConfiguration` interface. This feature integrates with the [requestPointerLock API](https://developer.mozilla.org/en-US/docs/Web/API/Element/requestPointerLock "https://developer.mozilla.org/en-US/docs/Web/API/Element/requestPointerLock") to provide
intuitive and context-aware mouse capture.

### Automatic pointer lock behavior

Amazon GameLift Streams automatically enables pointer lock when the application is fullscreen and the remote cursor is invisible on the stream
host. This behavior aligns well with common game development patterns:

- **FPS/TPS games and 3D orientation control** - The pointer is automatically locked and the
  cursor is hidden, providing unrestricted camera control essential for FPS gameplay.
- **Point-and-click games and UI control** - When games make the cursor visible for menu
  interactions or strategy gameplay, the pointer remains visible and unlocked, preserving the intended user experience.

### Configuration options

The `autoPointerLock` property accepts the following values:

`true`

The mouse is always captured when the remote cursor is invisible.

`false`

The mouse is never captured, regardless of cursor visibility.

`'fullscreen'` (default)

The mouse is only captured when the video element is in fullscreen mode and the remote cursor is invisible.

###### Important

`autoPointerLock` has no effect in the Safari browser or on iOS platforms due to platform limitations.

## Best practices

To ensure optimal mouse handling in your streamed applications:

- **Always stream fullscreen** - Your application should already be running in fullscreen mode to
  work properly on our service. In addition, we recommend using browser support to make the stream a fullscreen element for the best
  end-user experience. This will help avoid problems such as alignment issues between the system cursor and software cursor.
- **Hide the cursor for relative motion** - If your application expects relative mouse motion (such
  as FPS-style camera controls or drag-based interactions), hide the operating system cursor during those interactions. In some
  scenarios, you might need to hide the cursor on mouse-down and show it again on mouse-up.
- **Show the cursor for absolute positioning** - When your application needs precise cursor
  positioning for UI interactions, ensure the operating system cursor remains visible to enable absolute coordinate mode.
- **Test different input scenarios** - Verify that your application handles both relative and
  absolute mouse modes correctly, as Amazon GameLift Streams may switch between modes based on your cursor visibility changes.
- **Test different window modes** - Test your application's mouse handling in both windowed and
  fullscreen modes, if applicable. Determine which `autoPointerLock` setting is best for your input configuration.
