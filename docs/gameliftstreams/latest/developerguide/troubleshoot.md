# Troubleshooting Amazon GameLift Streams

## Access denied when making a request to Amazon GameLift Streams service

If you encounter AccessDenied exceptions when making calls to Amazon GameLift Streams APIs or working with resources in the console, your AWS Identity and Access Management (IAM) role might
have insufficient permissions for Amazon GameLift Streams. Check the following:

- If the IAM role has an explicit "deny-all" policy, you must explicitly list Amazon GameLift Streams as an exception to that policy by adding
  `"gameliftstreams:*"` to the [NotAction](../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md "../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md") element. For example:

```
{
    "Sid": "DenyAllExceptListedIfNoMFA",
    "Effect": "Deny",
    "NotAction": [
        "iam:CreateVirtualMFADevice",
        "iam:EnableMFADevice",
        "iam:GetUser",
        "iam:ListMFADevices",
        "iam:ListVirtualMFADevices",
        "iam:ResyncMFADevice",
        "sts:GetSessionToken",
        "gameliftstreams:*"                    // Add this
    ],
    "Resource": "*",
    "Condition": {
        "BoolIfExists": {"aws:MultiFactorAuthPresent": "false"}
    }
}
```

- For more information, see [Identity and Access Management for Amazon GameLift Streams](security-iam.md "security-iam.md") in the Security chapter, and review [Troubleshooting access denied error
  messages](../../../IAM/latest/UserGuide/troubleshoot_access-denied.md "../../../IAM/latest/UserGuide/troubleshoot_access-denied.md") in the _IAM User Guide_.

## Application issues

This section identifies potential causes for issues that prevent applications from running or cause them to appear differently on
Amazon GameLift Streams.

### Preliminary checks

- Run your application on a different machine to verify that it's correctly packaged. This confirms that your application
  content doesn't contain any hardcoded paths, missing assets, libraries, or binaries that might not work on other
  devices.

### Proton issues

- **Verify that your application is compatible with Proton.** Test your application on a local
  environment without the Amazon GameLift Streams server to verify that it's compatible with Proton. For instructions, see [Testing and troubleshooting compatibility with Proton for Amazon GameLift Streams](troubleshoot-compatibility-wp.md "troubleshoot-compatibility-wp.md").

### Application issues due to screen resolution

Applications might freeze, crash, or render incorrectly if you attempt to use a full-screen resolution that is not 1920x1080. We
recommend that you use a borderless fullscreen window to run your application and do not attempt to change the resolution.

### Application terminates at start of stream session

If your application terminates immediately when a stream session starts, review the following for potential causes and
solutions:

- **Verify runtime.** In the Amazon GameLift Streams application configuration, confirm that the file you
  specified in the **Executable launch path** is an executable file or script and is correct for the runtime
  environment that you selected. Windows applications should have a file type of ".exe", ".bat", or ".cmd" and target either of
  the Windows or Proton runtimes. Native Linux applications should be executable files that target the Ubuntu 22.04 LTS
  runtime.
- **Verify required DLLs.** Your Windows application might be missing required DLLs. For example,
  if your application is a debug build, then it requires the debug version of the Microsoft C and C++ (MSVC) runtime libraries.
  To resolve this, we recommend that you package your build and DLLs side-by-side. For instructions, refer to [Prepare a test
  machine to run a debug executable](https://learn.microsoft.com/en-us/cpp/windows/preparing-a-test-machine-to-run-a-debug-executable "https://learn.microsoft.com/en-us/cpp/windows/preparing-a-test-machine-to-run-a-debug-executable") by Microsoft.

In general, we recommend that you test your build on a clean machine first, before trying on Amazon GameLift Streams. For instructions about
testing on an Amazon EC2 instance, refer to [Set up a remote machine](troubleshoot-compatibility-setup-remote.md "troubleshoot-compatibility-setup-remote.md").

### Unreal Engine application crashes or requires additional dependencies

If your Unreal Engine application fails to start, crashes, or requires you to install additional dependencies, such as the Microsoft
C and C++ (MSVC) runtime, try the following:

- **Use the correct executable.** For your application to work correctly with Amazon GameLift Streams, set the
  application path to the full executable that's located in the `Binaries/Win64/` (or similar) subfolder. Unreal
  Engine produces two executables: a small bootstrap executable at the root of the folder, and a platform target executable in
  the `Binaries/Win64/` subfolder. The bootstrap executable at the root attempts to validate pre-conditions are
  correct and can create false positives on Amazon GameLift Streams that prevent application launch. If the platform target executable is
  missing, the application might not have been built correctly. For example, see the following folder structure of a sample
  Unreal application:

```

BuildApp
|-> MyUnrealApp.exe
|-> MyUnrealApp
            |-> Binaries
                    |-> Win64
                            |-> MyUnrealApp.exe
```

- **Turn off Unreal Engine Asserts.** Disable the `check`, `verify`, and
  `ensure` macros. They can prevent the application from creating crash dumps. For more
  information, see [Asserts in
  Unreal Engine documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/asserts-in-unreal-engine "https://dev.epicgames.com/documentation/en-us/unreal-engine/asserts-in-unreal-engine").
  - Define `USE_CHECKS_IN_SHIPPING=0` in your build to disable `check` and `verify`
    macros.
  - Use `-handleensurepercent=0` command-line argument to disable `ensure` macros.

## Performance issues

This section identifies potential causes for game performance issues when running on Amazon GameLift Streams, and offers suggestions for optimizing your
streams on the service.

### Game performance is reduced when streaming on Amazon GameLift Streams

If your game runs well on your own machine but experiences performance issues when you stream it on Amazon GameLift Streams, consider the following:

- Your machine might have more powerful hardware than Amazon GameLift Streams. Make sure to test the application on a machine with similar
  performance to the hardware that Amazon GameLift Streams uses:
  - gen4n: comparable to NVIDIA RTX 2060 GPU
  - gen5n: comparable to NVIDIA RTX 3080 GPU
  - gen6n: comparable to NVIDIA RTX 4060 GPU
    This verifies that your application's rendering settings are
    compatible with the GPU and that the performance meets your expectations.

- The problem might be due to your network connection or Amazon GameLift Streams's settings. Try the troubleshooting tips in the [Stream connectivity issues](#troubleshoot-stream-connectivity "#troubleshoot-stream-connectivity") section.

If your game is slow even when running locally, you'll need to optimize its performance. The best optimization methods will depend
on the specific engine or framework you're using.

- For Unreal Engine games, refer to [Profiling Unreal Engine performance](profiling-ue.md "profiling-ue.md").

### Windows applications experience slow load times or stuttering issues

If your game is experiencing long load times or stuttering behavior, we recommend the following course of action:

1. Ensure your application is packaged and optimized for loading performance using your engine vendor’s guidance around
   optimizing content and shader performance.
2. Ensure your application is set to be the [default application](multi-apps.md#multi-apps-about-linking "multi-apps.md#multi-apps-about-linking") in a stream
   group.
3. Optimize application first launch on the service by caching shaders as part of your application packaging.

There are two approaches to enabling shader caching:

- **Driver-based caching** – This approach is specific to the runtime environment GPU and
  driver version. This option can be applied to all applications and is therefore the default recommended approach. The steps
  for this approach will need to be replicated for every GPU/driver combination.
- **Engine-based caching** – This approach enables shader caching through the game engine,
  if available. It places the burden of creating a pre-baked pipeline state object (PSO) cache on the developer. It also assumes
  that the engine is capable of handling cache support for different drivers on the same GPU hardware.

As a best practice, we recommend implementing driver-based caching first, because it does not require deep understanding of how PSO
caching is implemented for the given engine.

With these implementations, shader files can be exported and packaged with your application so that they don't have to be generated
with every new stream start.

###### To implement a driver-based caching fix for a Windows runtime application

1. Start streaming your default application and play it extensively to generate shaders for the application.

###### Important

Be sure to visit all the areas or levels of the environment to generate as many shaders as possible. 2. _Before_ closing the stream, enable the export feature in your active stream session. For details, see
[Export stream session files](stream-sessions-export-files.md "stream-sessions-export-files.md"). 3. Download the stream session export .zip file from the Amazon S3 bucket you specified in the previous step. You can find a
download link on the Amazon GameLift Streams console on the **Sessions** page. 4. Locate the shaders folder within the stream session export. It's usually saved to this location:
`AppData\Local\NVIDIA\DXCache`. Upload the generated shader files (`*.nvph`) to your application's
Amazon S3 bucket. 5. Create a `.bat` file that will copy the shader files into the NVIDIA caching folder at runtime. This folder is
usually located at: `C:\Users\Administrator\AppData\Local\NVIDIA\DXCache`. Upload the `.bat` file to the
Amazon S3 application bucket. 6. Create a new Amazon GameLift Streams application with the `.bat` file as the executable path.

When your application starts streaming, your `.bat` file will copy the pre-generated shaders to the shader cache before
launching the application, improving the stream loading performance.

###### Note

You might need to repeat these steps whenever you update your application or link the Amazon GameLift Streams application to a new stream group. Newer
stream groups can contain updated GPU drivers from the service.

The following example `.bat` file assumes that the shader files are stored under the Amazon S3 bucket prefix
`Shaders\`. You can use a different folder structure.

```
@echo off
set CURRENT_PATH=%cd%
set DXCACHE_DIR=%CURRENT_PATH%\`Shaders`
set NVIDIA_DXCACHE_DIR=C:\Users\Administrator\AppData\Local\NVIDIA\DXCache

if not exist "%NVIDIA_DXCACHE_DIR%" (
    mkdir "%NVIDIA_DXCACHE_DIR%"
)

xcopy /s /f "%DXCACHE_DIR%" "%NVIDIA_DXCACHE_DIR%"

start %CURRENT_PATH%\`app.exe`

```

###### To implement a driver-based caching fix for a Proton runtime application

1. Start streaming your default application with the following environment variable override:

```
"__GL_SHADER_DISK_CACHE_PATH" : "/home/unpriv/games"
```

2. Play application extensively to generate shaders.

###### Important

Be sure to visit all the areas or levels of the environment to generate as many shaders as possible. 3. _Before_ closing the stream, enable the export feature in your active stream session. For details, see
[Export stream session files](stream-sessions-export-files.md "stream-sessions-export-files.md"). 4. Download the stream session export .zip file from the Amazon S3 bucket you specified in the previous step. You can find a
download link on the Amazon GameLift Streams console on the **Sessions** page. 5. Locate the shaders folders and files within the stream session export:

    1. `application\GLCache` folder
    2. if application uses DX11: `application\`path-to-exe\exe-name`.dxvk-cache`
     file
    3. if application uses DX12: `application\`path-to-exe`\vkd3d-proton.cache.write`
     file

6. Upload the generated shader files to your application's Amazon S3 bucket:
   1. Copy the `GLCache` folder into the root directory of your application.
   2. If available, copy the `.dxvk-cache` or `vkd3d-proton.cache.write` cache file to the folder
      containing the application executable.

7. Create a new Amazon GameLift Streams application with the same Proton configuration.
8. Run the application with the same environment variable override:

```
"__GL_SHADER_DISK_CACHE_PATH" : "/home/unpriv/games"
```

When your application starts streaming, it will use the pre-generated shaders, improving the stream loading performance.

###### Note

You might need to repeat these steps whenever you update your application or link the Amazon GameLift Streams application to a new stream group. Newer
stream groups can contain updated GPU drivers from the service.

###### To implement an engine-based caching fix for an application using Unreal Engine

For this approach, you can use Unreal Engine features to create a pipeline state object (PSO) cache for your Amazon GameLift Streams
application. A PSO cache lets you deliver pre-compiled graphics pipeline states with decreased runtime compilation times, which
can reduce hitches during loading and rendering. This requires advanced knowledge of Unreal Engine, and therefore we will not
cover all the engine-specific details here. For additional instructions, refer to the guidance from Unreal Engine in [Creating a Bundled PSO Cache](https://dev.epicgames.com/documentation/en-us/unreal-engine/manually-creating-bundled-pso-caches-in-unreal-engine "https://dev.epicgames.com/documentation/en-us/unreal-engine/manually-creating-bundled-pso-caches-in-unreal-engine"), "Collection Flow" section.

1. Generate shaders for your application that has PSO logging enabled.
   1. Create a new Amazon GameLift Streams application using the packaged build with the PSO-enabled application.
   2. Start a stream with `-logPSO` command in your PSO logging app. You can use the command-line arguments
      option on the **Test stream** configuration page in the Amazon GameLift Streams console.

   ###### Important

   Be sure to visit all the areas or levels of the environment to generate as many shaders as possible. 3. _Before_ closing the stream, enable the export feature in your active stream session. For details, see [Export stream session files](stream-sessions-export-files.md "stream-sessions-export-files.md"). 4. Quit the application from the menu or by using Unreal shutdown commands. If you close the stream directly, the
   Unreal shaders pipeline file won’t be generated. 5. Download the stream session export .zip file from the Amazon S3 bucket you specified in the export step. You can find a
   download link on the Amazon GameLift Streams console on the **Sessions** page.

2. Package the Unreal shaders pipeline file into your Amazon GameLift Streams application.
   1. Locate the recorded PSO files (`rec.pipelinecache`) in the stream session export under
      `Saved/CollectedPSOs`. Unpack the PSO files using Unreal commands.
   2. Package a new Unreal build with the generated output from the unpacking. Follow the Unreal guidance, sections [Converting PSO caches](https://dev.epicgames.com/documentation/en-us/unreal-engine/manually-creating-bundled-pso-caches-in-unreal-engine#convertingpsocaches "https://dev.epicgames.com/documentation/en-us/unreal-engine/manually-creating-bundled-pso-caches-in-unreal-engine#convertingpsocaches") and [Including PSO caches in your Application](https://dev.epicgames.com/documentation/en-us/unreal-engine/manually-creating-bundled-pso-caches-in-unreal-engine#includingpsocachesinyourapplication "https://dev.epicgames.com/documentation/en-us/unreal-engine/manually-creating-bundled-pso-caches-in-unreal-engine#includingpsocachesinyourapplication").

   ###### Important

   When running the Unreal command in the "Converting PSO Caches" section, make sure that you use the same driver's
   version input files. For example: for DX12, use only the SM6 files as inputs. Otherwise you’ll get an error when
   packaging the new application. 3. Create a new Amazon GameLift Streams application for the new packaged build with the PSO files. 4. When starting and testing streams, confirm that PSO cache is being loaded. Check the game logs for the following
   line:

   ```
   Opened FPipelineCacheFile: ../../...
   ```

###### Note

You might need to repeat these steps whenever you update your application or link the Amazon GameLift Streams application to a new stream group. Newer
stream groups can contain updated GPU drivers from the service.

## Stream connectivity and network performance issues

When you [set up your Amazon GameLift Streams backend service](sdk.md "sdk.md"), check the following:

- Choose the closest AWS Region possible to the end user. High latency from your clients to the Region hosting your stream can
  impact stream quality. Refer to [AWS Regions and streaming locations supported by
  Amazon GameLift Streams](regions-quotas-rande.md "regions-quotas-rande.md") for a list of
  locations where you can stream from. You can ping AWS console endpoints in the Region to get an approximate latency
  measurement.
- Verify your stream group has capacity for new streams.
- Verify that `ConnectionTimeoutSeconds` is reasonably set to allow end users plenty of time to connect before their
  web client times out.

Advise your end users to check the following:

- Ensure firewalls allow access to UDP port range 33435-33465 to allow streaming from Amazon GameLift Streams. If Amazon GameLift Streams can't reach these ports,
  it can lead to streaming issues, such as a black or grey screen.
- Verify that your internet connection can sustain a connection speed of at least 10 Mbps for a 1080p stream. If you detect
  network issues while playing on Amazon GameLift Streams, your internet speed might be fluctuating and you might not be getting at least 10 Mbps
  consistently. Run an internet speed test and continue through the troubleshooting steps.
- Use a wired network if possible. When using Wi-Fi, move your device close to your router for stronger signal strength.
- If you're using a Wi-Fi router with both 2.4 GHz and 5 GHz bands, try connecting to a different band. If you're unsure how to
  switch your router to a different band, visit the support pages of the manufacturer or provider of your Wi-Fi router. You can also
  contact their customer service.
- Identify if others on the same network (especially when on home Wi-Fi) are running high-bandwidth applications like video
  streaming, downloading, online gaming, or backups.
- Close other applications on your device that take up bandwidth.
- Don't use a VPN or proxy while streaming. They can cause higher latencies and impact gameplay.
- Verify you're using Wi-Fi instead of cellular networks when playing on an iPad or iPhone. Using a cellular network can result in
  connectivity issues.
- MacOS users should disable Location Services as it will cause the Wi-Fi to pause from time to time, which will lead to a poor
  streaming experience.

## Stream input issues

This section identifies potential causes and solutions for issues related to user input in a stream session.

### General input troubleshooting

- Test to see if the issue is browser-specifc. Overall, we recommend Google Chrome, Microsoft Edge, or a custom Chromium-based
  desktop application for the best end-user experience and maximum compatibility, particularly with game controllers.
- Log input events sent from client and received by the application to identify where there is an input mismatch in your front
  end code.
- Be sure to check [Supported browsers and input](sdk-browsers-input.md "sdk-browsers-input.md") for additional information on
  supported browsers and input devices, including known issues and limitations.

### Gamepad and microphone inputs don't work on native Linux applications

Gamepad and microphone inputs are not supported in native Linux applications. See [Supported browsers and input](sdk-browsers-input.md "sdk-browsers-input.md") for additional information on supported input devices, including known issues and
limitations.

### Key input appears stuck on MacOS client

On MacOS clients, keys might suddenly appear to be stuck when the **Command** modifier key and another key are
simultaneously pressed, repeating the key event. For example, the arrow key might get stuck when the **Command** key
is also pressed. In a game, if arrow keys are used to spin the camera, this would make the camera rotate endlessly.

- Issue: The **Command** key on MacOS maps to the **Meta** key event, which maps to the
  **Windows** key on Microsoft Windows. The issue is a [bug](https://issues.chromium.org/issues/40880986 "https://issues.chromium.org/issues/40880986") affecting MacOS browsers when **Command**
  and another key are pressed simultaneously, where the **Meta** key is reset when released but the arrow key
  is not reset because the browser didn't capture a keyup event for the arrow key, so the Web SDK client won't send a keyup
  event to the server and the streaming application would still think the key is being pressed.
- Solution: If you are not using the **Command** key, you can filter it out using the Web SDK keyboard filter
  mechanism (`keyboardFilter`) found in the Web SDK's `InputConfiguration` interface.

### Stuck input when you open OS UI elements

On desktop and mobile browser clients, input events such as key releases are not processed when certain OS-level UI elements have priority.
This can cause characters to move or actions to repeat as if keys are still being held down, even though you have released them.

- Issue: When you open certain OS-level UI elements (such as browser menu bars on desktop, or Control Center and
  Notification Center on iOS), the browser stops firing input events without triggering blur or focus events. This causes the
  server to continue receiving the last input state. This is a browser-level limitation that cannot be reliably detected.
- Solution: Use fullscreen mode on desktop browsers to prevent access to browser menu bars. For iOS users with connected
  keyboards, we recommend creating a native app wrapper with a web view where the native app can better detect and handle
  focus loss, explicitly triggering browser window focus and blur events. Alternatively, use front-end HTML or in-game UI
  elements to inform users that a key is still pressed, and provide information about this iOS limitation.

### Mouse movement behaves differently on Amazon GameLift Streams

If mouse movement behaves differently when streaming with Amazon GameLift Streams, such as moving more quickly than expected, you
might need to adjust the mouse-handling and cursor management logic in your application.

- Issue: Amazon GameLift Streams uses a heuristic to pick whether to transmit mouse events in “relative” or “absolute” mode. In relative mode,
  new mouse updates are provided as small, incremental differences from the previous update. In absolute mode, the mouse cursor
  is continually forced to a screen position that is synchronized with the client. When the operating system cursor is visible
  over the streamed content, the heuristic always picks absolute coordinates. This can cause unexpectedly large movement
  deltas if your application is expecting small, relative updates.
- Solution: If your application expects relative mouse motion (for example, FPS-style camera controls or drag-based
  interactions), hide the operating system cursor during mouse interactions. For instance, hide the cursor on mouse-down and
  show it again on mouse-up. This ensures dragging motions use relative coordinates, with absolute position synchronized only
  when the button is released.

For more information on mouse movement in Amazon GameLift Streams, see [Mouse movement handling](sdk-mouse-movement.md "sdk-mouse-movement.md").

## Stream session issues

This section identifies potential causes and solutions for issues related to a stream session starting or terminating
unexpectedly.

### Stream session does not start

Potential causes:

- Application is hung or crashed. Refer to the [Application issues](#troubleshoot-application "#troubleshoot-application") section for troubleshooting instructions.
- Stream group status is not `Active`. Verify the status of the stream group.
- On-demand capacity is taking longer to spin up than the timeout specified by `ConnectionTimeoutSeconds` in the
  [StartStreamSession](../apireference/API_StartStreamSession.md "../apireference/API_StartStreamSession.md") API. On the
  Windows runtime, the on-demand spin up time can take 5 minutes or more.
- No available capacity in the streaming location. Verify that your allocated capacity is greater than your in-use capacity,
  or that you have on-demand capacity that's not in use (allocated capacity is less than always-on capacity plus on-demand
  capacity). In the console, you can find these values in the list of stream groups or on the stream group detail page. Using
  the service API, you can find these values using [GetStreamGroup](../apireference/API_GetStreamGroup.md "../apireference/API_GetStreamGroup.md"). A few scenarios where available capacity is temporarily at zero include the following:
  - If you just increased always-on capacity in the streaming location, wait a few minutes for the capacity to be
    allocated.
  - If you only have 1 available capacity in the streaming location and your client unexpectedly disconnected, the
    previous session might still be in a disconnected state. Wait a few minutes for the session to timeout and try
    again.
  - If you recently added a location to your stream group and the application did not exist at the location, the
    application might not have finished replicating there. Check the replication status on the stream group details page
    in the console. Alternatively, you can use the [GetApplication](../apireference/API_GetApplication.md "../apireference/API_GetApplication.md") API and check the
    `ReplicationStatuses` value to verify that the `Status` of the desired streaming location is
    `COMPLETED`.

- Network conditions are so poor that frames, especially the first frame, are not being sent. Check network conditions between
  the client and the streaming location and adjust or try a different location.

### Stream session terminated

Stream sessions automatically terminate when an application crashes or quits, or when the client connection is lost. Sessions can
also terminate due to the following timeout values:

- **Placement timeout**: Timeout value for Amazon GameLift Streams to find compute resources to host a stream
  session.
- **Connection timeout**: Timeout value for a client to connect or reconnect to a stream
  session.
- **Idle timeout**: Maximum time that a stream session can be idle with no user input.
- **Session length timeout**: Maximum time for a stream session.

For a detailed explanation of each timeout and its possible values, refer to [Timeout values affecting stream sessions](stream-sessions.md#stream-sessions-lifecycle-timeouts "stream-sessions.md#stream-sessions-lifecycle-timeouts").
