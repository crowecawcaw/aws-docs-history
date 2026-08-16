# Troubleshoot Linux applications for Amazon GameLift Streams

If your Amazon GameLift Streams application runs on an Ubuntu runtime environment, this section can help you troubleshoot issues specific
to running native Linux applications. For general troubleshooting, see [Troubleshooting Amazon GameLift Streams](troubleshoot.md "troubleshoot.md").

## Set up a local machine to test

Before troubleshooting on Amazon GameLift Streams, verify that your application performs correctly on a local Ubuntu 22.04 LTS machine.
For instructions, see [Set up a local machine](troubleshoot-compatibility-setup-local.md "troubleshoot-compatibility-setup-local.md").

## Known issues

### Application renders a black screen

If your application renders a black screen, try one or both of the following:

- Disable shared textures by setting the environment variable
  `VK_LAYER_AMZN_BLITSURFACE_SHARED_TEXTURES=0`.
- Switch to Vulkan rendering. For Unity applications, add `-force-vulkan` to
  your launch parameters, or set Vulkan as the only Graphics API in **Player**

> **Other Settings** > **Graphics APIs**.

### Poor performance with OpenGL

If your application targets OpenGL and you experience poor frame rates or the application appears frozen,
force the NVIDIA implementation by setting the environment variable
`__GLX_VENDOR_LIBRARY_NAME=nvidia`.

### Unity application freezes or pauses

The application window might not receive OS-level focus in the streaming environment. By default, Unity pauses
rendering when unfocused. To resolve this, apply both of the following settings:

1. Set `Application.runInBackground = true` in your application code.
2. If you use the new Input System package, set
   `InputSettings.backgroundBehavior = InputSettings.BackgroundBehavior.IgnoreFocus`.

### Microphone input is not available

Microphone input is not supported on the Ubuntu 22.04 LTS runtime. If your application requires microphone input, use the
Proton or Microsoft Windows Server 2022 Base runtime instead. For more information, see [Amazon GameLift Streams compatible devices and browsers](compatible-devices-browsers.md "compatible-devices-browsers.md").
