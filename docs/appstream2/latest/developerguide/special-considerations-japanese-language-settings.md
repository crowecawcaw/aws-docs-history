# Special Considerations for Japanese Language Settings

This section describes key points to keep in mind when configuring Japanese language
settings for your WorkSpaces Applications users.

## AWS CLI

Changing the Windows system locale to Japanese requires that your image builder
have AWS Command Line Interface (AWS CLI) version 1.16.30 or later installed. To
update the version of AWS CLI on your image builder, follow the steps in [Installing the
AWS Command Line Interface](../../../cli/latest/userguide/install-windows.md "../../../cli/latest/userguide/install-windows.md").

## Japanese Keyboards

If your image builder input method is set to Japanese when you create an image,
WorkSpaces Applications automatically configures your image to use a Japanese keyboard. Any fleets
that use the image are also automatically configured to use Japanese keyboards.
However, if you want to use a Japanese keyboard within your image builder session,
update the following registry settings for the
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\i8042prt\Parameters registry
key:

| Name                       | Type   | Data        |
| -------------------------- | ------ | ----------- |
| LayerDriver JPN            | REG_SZ | kbd106.dll  |
| OverrideKeyboardIdentifier | REG_SZ | PCAT_106KEY |
| OverrideKeyboardSubtype    | DWORD  | 2           |
| OverrideKeyboardType       | DWORD  | 7           |

After changing these settings, restart your image builder. To do so, choose the
Windows **Start** button, and choose **Windows
PowerShell**. In PowerShell, use the
**restart-computer** cmdlet.
