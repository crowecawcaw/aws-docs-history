# Set up a local machine to troubleshoot Proton

Proton is a compatibility layer that enables Windows applications to run on Linux. As such, you must have an Ubuntu machine to test and
troubleshoot with. If you don't have a local Ubuntu machine, you can set up a remote machine using Amazon EC2. To do so, follow the steps in [Set up a remote machine](troubleshoot-compatibility-setup-remote.md "troubleshoot-compatibility-setup-remote.md") instead.

## Prerequisites

- [Ubuntu 22.04 LTS](https://releases.ubuntu.com/jammy/ "https://releases.ubuntu.com/jammy/"). For installation instructions, you can use
  Ubuntu's [Install Ubuntu Desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop "https://ubuntu.com/tutorials/install-ubuntu-desktop") tutorial.
- NVIDIA GPU

## Install GPU drivers

Installing the latest GPU drivers can prevent your application from poor performance and crashes.

**To check what GPU driver your system uses**

1. Run the following command in a terminal:

```
lshw -C display | grep driver
```

2. If the correct drivers are installed, you should see the following output, or similar, where
   `<gpu>` is `nvidia` for NVIDIA: `configuration: driver=<gpu>
latency=0`

**To install the latest NVIDIA GPU drivers**

Follow the instructions in [NVIDIA drivers
installation](https://documentation.ubuntu.com/server/how-to/graphics/install-nvidia-drivers/ "https://documentation.ubuntu.com/server/how-to/graphics/install-nvidia-drivers/").

## Verify GPU drivers

Verify that GPU drivers are installed and working correctly. One way
to verify this is by running the
[vkcube](https://github.com/krh/vkcube "https://github.com/krh/vkcube")
application in a terminal.

1. Install the `vulkan-tools` apt package using the following command.

```
sudo apt install -y vulkan-tools
```

2. Run `vkcube`.
3. Review the output.
   - If your system is properly using the correct GPU, you will
     see output similar to the following, with the name of your
     GPU: `Selected GPU 0: AMD Radeon Pro V520 (RADV NAVI12), type: 2`
   - If your application isn&t able to use the GPU
     correctly, you might see different output similar to the
     following: `Selected GPU 0: llvmpipe (LLVM 15.0.7, 256 bits), type: 4`

   In this case, check the GPU drivers and re-install if needed.

## Next step

With your local Ubuntu machine ready, the next step is to set up Proton. For instructions, refer to [Troubleshoot on Proton](troubleshoot-compatibility-wp-proton.md "troubleshoot-compatibility-wp-proton.md").
