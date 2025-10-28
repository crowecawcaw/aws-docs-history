# Install Windows Subsystem for Linux on your EC2 Windows instance

The Windows Subsystem for Linux (WSL) is a feature of Microsoft Windows. By installing WSL
on your EC2 Windows instance, you can run native Linux command line tools directly on your
Windows instance.

There are two versions of Windows Subsystem for Linux (WSL): WSL 1 and WSL 2. For more information, see
[Windows Subsystem for Linux Documentation](https://learn.microsoft.com/en-us/windows/wsl/ "https://learn.microsoft.com/en-us/windows/wsl/")
on the Microsoft website.

###### Requirements

- The operating system must be Windows Server 2019 or later.
- You must install WSL 1 on virtualized Windows instances (the instance size is not `.metal`).
- You can install either WSL 1 or WSL 2 on bare metal instances (the instance size is `.metal`).
  Bare metal instances provide the required support for nested virtualization.

## Install WSL on your Windows instance

###### To install WSL 1

1. Install WSL. The process that you'll use depends on the version of Windows Server
   running on the instance.
   - Windows Server 2022 and later - Run the
     following standard installation command on your EC2 instance.

   ```
   wsl --install --enable-wsl1 --no-launch
   ```

   - Windows Server 2019 - Enable WSL and then
     install WSL as described in [Install WSL on previous versions of Windows Server](https://learn.microsoft.com/en-us/windows/wsl/install-on-server#install-wsl-on-previous-versions-of-windows-server "https://learn.microsoft.com/en-us/windows/wsl/install-on-server#install-wsl-on-previous-versions-of-windows-server") on the Microsoft website.

2. Restart your EC2 instance.

```
shutdown -r -t 20
```

3. To configure WSL to use WSL 1, run the following command on your instance. This step
   is required for virtualized instances (the instance size is not `.metal`).

```
wsl --set-default-version 1
```

4. Install the default distribution.

```
wsl --install
```

###### To install WSL 2 (bare metal instances only)

Run the following standard installation command on your EC2 instance. By default,
WSL 2 is installed.

```
wsl --install
```
