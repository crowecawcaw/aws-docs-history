

# Troubleshoot Linux applications for Amazon GameLift Streams
<a name="troubleshoot-linux"></a>

If your Amazon GameLift Streams application runs on an Ubuntu runtime environment, this section can help you troubleshoot issues specific to running native Linux applications. For general troubleshooting, see [Troubleshooting Amazon GameLift Streams](troubleshoot.md).

## Set up a local machine to test
<a name="troubleshoot-linux-local-test"></a>

Before troubleshooting on Amazon GameLift Streams, verify that your application performs correctly on a local Ubuntu 22.04 LTS machine. For instructions, see [Set up a local machine](troubleshoot-compatibility-setup-local.md).

## Known issues
<a name="troubleshoot-linux-known-issues"></a>

### Application renders a black screen
<a name="troubleshoot-linux-black-screen"></a>

If your application renders a black screen, try one or both of the following:
+ Disable shared textures by setting the environment variable `VK_LAYER_AMZN_BLITSURFACE_SHARED_TEXTURES=0`.
+ Switch to Vulkan rendering. For Unity applications, add `-force-vulkan` to your launch parameters, or set Vulkan as the only Graphics API in **Player** > **Other Settings** > **Graphics APIs**.

### Poor performance with OpenGL
<a name="troubleshoot-linux-opengl-performance"></a>

If your application targets OpenGL and you experience poor frame rates or the application appears frozen, force the NVIDIA implementation by setting the environment variable `__GLX_VENDOR_LIBRARY_NAME=nvidia`.

### Unity application freezes or pauses
<a name="troubleshoot-linux-unity-freeze"></a>

The application window might not receive OS-level focus in the streaming environment. By default, Unity pauses rendering when unfocused. To resolve this, apply both of the following settings:

1. Set `Application.runInBackground = true` in your application code.

1. If you use the new Input System package, set `InputSettings.backgroundBehavior = InputSettings.BackgroundBehavior.IgnoreFocus`.

### Microphone input is not available
<a name="troubleshoot-linux-microphone"></a>

Microphone input is not supported on the Ubuntu 22.04 LTS runtime. If your application requires microphone input, use the Proton or Microsoft Windows Server 2022 Base runtime instead. For more information, see [Amazon GameLift Streams compatible devices and browsers](compatible-devices-browsers.md).