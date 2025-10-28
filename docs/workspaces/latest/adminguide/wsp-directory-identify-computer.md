# Identify the computer name for your WorkSpaces Personal directory

The **Computer Name** value shown for a WorkSpace in the Amazon WorkSpaces console
varies, depending on which type of WorkSpace you've launched (Amazon Linux, Ubuntu, or Windows). The computer
name for a WorkSpace can be in one of these formats:

- **Amazon Linux**: A-`xxxxxxxxxxxxx`
- **Red Hat Enterprise Linux**: R-`xxxxxxxxxxxxx`
- **Rocky Linux**: R-`xxxxxxxxxxxxx`
- **Ubuntu**: U-`xxxxxxxxxxxxx`
- **Windows**: IP-C`xxxxxx` or
  WSAMZN-`xxxxxxx` or EC2AMAZ-`xxxxxxx`
  For Windows WorkSpaces, the computer name format is determined by the bundle type, and in the case
  of WorkSpaces created from public bundles or from custom bundles based on public images, by when the
  public images were created.

Starting June 22, 2020, Windows WorkSpaces launched from public bundles have the WSAMZN-`xxxxxxx`
format for their computer names instead of the IP-C`xxxxxx` format.

For custom bundles based on a public image, if the public image was created before June 22, 2020,
the computer names are in the EC2AMAZ-`xxxxxxx` format. If the public image
was created on or after June 22, 2020, the computer names are in the WSAMZN-`xxxxxxx`
format.

For Bring Your Own License (BYOL) bundles, either the DESKTOP-`xxxxxxx` or the
EC2AMAZ-`xxxxxxx` format is used for the computer names by default.

If you've specified a custom format for the computer names in your custom or BYOL bundles, your
custom format overrides these defaults. To specify a custom format, see
[Create a custom WorkSpaces image and bundle for WorkSpaces Personal](create-custom-bundle.md "create-custom-bundle.md").

###### Important

After a WorkSpace is created, you can safely change its computer name. For example, you can execute
a PowerShell script with the command `Rename-Computer` on your WorkSpace or remotely. The updated
computer name value will then be shown for a WorkSpace in the Amazon WorkSpaces console.
