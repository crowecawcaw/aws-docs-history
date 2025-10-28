# Testing and troubleshooting compatibility with Proton for Amazon GameLift Streams

If your Amazon GameLift Streams application runs on a Proton runtime environment, this section can help you troubleshoot compatibility issues between your
application and the Proton layer. These instructions include a set of scripts that installs Proton to your own machine, simulating the
environment that Amazon GameLift Streams would use. By troubleshooting without the Amazon GameLift Streams service, you can focus on troubleshooting issues specific to your
application and the runtime environment.

## High-level steps to test and troubleshoot

1. Acquire an Ubuntu 22.04 LTS machine. You can use either a local machine or an Amazon EC2 cloud-based desktop. Choose from
   the following topics for instructions:
   - [Set up a local machine](troubleshoot-compatibility-setup-local.md "troubleshoot-compatibility-setup-local.md")
   - [Set up a remote machine](troubleshoot-compatibility-setup-remote.md "troubleshoot-compatibility-setup-remote.md")

2. Install the Proton runtime environment to test and debug your application. Refer to [Troubleshoot on Proton](troubleshoot-compatibility-wp-proton.md "troubleshoot-compatibility-wp-proton.md") for
   guidance.

## Known issues with Proton

Refer to the [Proton GitHub wiki](https://github.com/ValveSoftware/Proton/wiki "https://github.com/ValveSoftware/Proton/wiki") for the latest compatibility and
troubleshooting resources. You can also search for issues in the Proton GitHub [issue tracker](https://github.com/ValveSoftware/Proton/issues "https://github.com/ValveSoftware/Proton/issues"). Following are some specific issues to be aware of that our customers have encountered when running Windows
applications on Proton:

**Godot applications on Proton**

- Godot-based applications running on Proton might encounter a black screen if the Amazon Vulkan capture layer is enabled. To
  mitigate this issue, disable shared textures when streaming by setting the environment variable
  `VK_LAYER_AMZN_BLITSURFACE_SHARED_TEXTURES=0`.

**Unreal Engine applications on Proton**

- If you run into problems on Proton 8.x with Electra Media Player, (an Unreal Engine plugin) we recommend using the fixes found in [https://github.com/ValveSoftware/wine/pull/257](https://github.com/ValveSoftware/wine/pull/257 "https://github.com/ValveSoftware/wine/pull/257").
