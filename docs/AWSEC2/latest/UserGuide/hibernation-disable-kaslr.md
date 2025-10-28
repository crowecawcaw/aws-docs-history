# Disable KASLR on an instance (Ubuntu

only)

To run hibernation on a newly launched instance with Ubuntu 16.04 LTS (Xenial Xerus),
Ubuntu 18.04 LTS (Bionic Beaver) released with serial number 20190722.1 or later, or
Ubuntu 20.04 LTS (Focal Fossa) released with serial number 20210820 or later, we
recommend disabling KASLR (Kernel Address Space Layout Randomization). On Ubuntu 16.04
LTS, Ubuntu 18.04 LTS, or Ubuntu 20.04 LTS, KASLR is enabled by default.

KASLR is a standard Linux kernel security feature that helps to mitigate exposure to
and ramifications of yet-undiscovered memory access vulnerabilities by randomizing the
base address value of the kernel. With KASLR enabled, there is a possibility that the
instance might not resume after it has been hibernated.

To learn more about KASLR, see [Ubuntu Features](https://wiki.ubuntu.com/Security/Features "https://wiki.ubuntu.com/Security/Features").

###### To disable KASLR on an instance launched with Ubuntu

1. Connect to your instance using SSH. For more information, see [Connect to your Linux instance using SSH](connect-to-linux-instance.md "connect-to-linux-instance.md").
2. Open the `/etc/default/grub.d/50-cloudimg-settings.cfg` file in
   your editor of choice. Edit the `GRUB_CMDLINE_LINUX_DEFAULT` line to
   append the `nokaslr` option to its end, as shown in the following
   example.

```
GRUB_CMDLINE_LINUX_DEFAULT="console=tty1 console=ttyS0 nvme_core.io_timeout=4294967295 nokaslr"
```

3. Save the file and exit your editor.
4. Run the following command to rebuild the grub configuration.

```
sudo update-grub
```

5. Reboot the instance.

```
sudo reboot
```

6. Run the following command to confirm that `nokaslr` has been
   added.

```
cat /proc/cmdline
```

The output of the command should include the `nokaslr`
option.
