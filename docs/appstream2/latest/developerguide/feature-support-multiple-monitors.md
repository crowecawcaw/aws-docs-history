# Multiple Monitors

WorkSpaces Applications supports the use of multiple monitors during streaming sessions, including monitors that have different resolutions. To help ensure an optimal streaming experience, we recommend that users who have monitors with different resolutions set the display scale for their monitors to 100 percent.

###### Note

For WorkSpaces Applications streaming sessions that use [native application mode](feature-support-native-application-mode.md "feature-support-native-application-mode.md"), monitors with up to 4K
resolution are supported. If higher-resolution monitors are used for
streaming sessions, the WorkSpaces Applications client falls back to classic mode. In
this scenario, the WorkSpaces Applications classic mode streaming view occupies 4K of
the screen, and the remaining portion of the screen is black.

## Multiple Monitors (up to 4K Resolution)

**Default behavior:** By default, all
instance types support up to 4 monitors with a maximum display resolution
of 4096x2160 pixels per monitor, except for instances with small or medium
sizes.

**For all instance types with small and medium
sizes:** While we do not recommend using 4K resolution on
small and medium instances due to performance limitations, you can enable
it by making the following changes in your images:

- For Windows: Configure the following registry setting on image
  builder.
  - Using PowerShell:

  ```
  Set-ItemProperty "HKLM:\SOFTWARE\Amazon\AppStream" -Name EnableNonGraphics4K -Value 1
  ```

  - Using registry edit (regedit):
    - Registry path: `HKLM:Software\Amazon\AppStream`
    - Registry value name: `EnableNonGraphics4K`
    - Registry value data: `1`
    - Registry value type: `DWord`

- For Linux: Edit
  `/etc/euc/workspaces-applications.conf` and
  update the following `[display]`
  configuration:

```
EnableNonGraphics4K=1
```

- Create a new image using this setting.
- Use this new image with your fleets.
- Your end users will see a max of 4K resolution on their
  display devices, depending upon the display resolution of their
  devices.

###### Important

High-resolution monitors (such as 4K displays) require significantly
more GPU and encoding resources, with actual performance depending on
display configuration (resolution and number of monitors) and the
compute instance being used. If your users experience suboptimal
performance on 4K monitors, either switch your fleets to more powerful
instances or recommend your users to reduce their display resolution to
improve responsiveness.

Ultrawide monitors with resolutions exceeding 4096 pixels in either
dimension (e.g., 5120x2160) will display black bars on the sides, as
the maximum supported resolution is limited to 4096 pixels per
dimension.

**Disable 4K resolution for non-graphics
instances**

If your users are facing performance issues with 4K monitor resolutions
on instances without graphics hardware, you can follow the steps below to
limit the resolution to 2K (2560x1440).

- For Windows: Configure the following registry setting on image
  builder.
  - Using PowerShell:

  ```
  Set-ItemProperty "HKLM:\SOFTWARE\Amazon\AppStream" -Name EnableNonGraphics4K -Value 0
  ```

  - Using registry edit (regedit):
    - Registry path: `HKLM:Software\Amazon\AppStream`
    - Registry value name: `EnableNonGraphics4K`
    - Registry value data: `0`
    - Registry value type: `DWord`

- For Linux: Edit
  `/etc/euc/workspaces-applications.conf` and
  update the following `[display]`
  configuration:

```
EnableNonGraphics4K=0
```

- Create a new image using this setting.
- Use this new image with your fleets.
- Your end users will see a max of 2K resolution on their
  display devices.
