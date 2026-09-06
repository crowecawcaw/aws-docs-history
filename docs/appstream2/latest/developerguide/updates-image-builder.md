# Update license-included applications

Updates for license-included applications are disabled by default. You can enable and
perform updates for these applications on an image builder that includes one or more of
them or perform the updates using Managed Image Updates. Updates on fleet instances
remain disabled to prevent installation during session setup.

There are three options for updating Office applications:

- Enable and perform updates from the application menu on an image
  builder
- Enable and perform updates manually with PowerShell on an image builder
- Use Managed Image Updates
  After updates complete, snapshot the image and use the new image for your fleets to
  continue using the updated applications.

## Option 1: Enable and perform updates from the application menu

To enable updates for license-included applications from within an Office
application, do the following:

1. On the image builder, open any license-included application (for example,
   Word or Excel).
2. Choose **File**, **Account**,
   **Update Options**, **Enable Updates**.
3. Once updates are enabled, choose **Update Options**,
   **Update Now** to start the updates.

## Option 2: Enable and perform updates manually with PowerShell

To enable updates for license-included applications by using PowerShell, do
the following:

1. On the image builder, open PowerShell as an administrator.
2. Enable updates through Click-to-Run:

`Set-ItemProperty -Path
 "HKLM:\SOFTWARE\Microsoft\Office\ClickToRun\Configuration" -Name UpdatesEnabled
 -Value True` 3. Run the update:

`Start-Process -FilePath "C:\Program Files\Common Files\Microsoft
 Shared\ClickToRun\OfficeC2RClient.exe" -ArgumentList "/update user" -Wait
 -PassThru`

The update can take several minutes to complete. A pop-up window displays the
update status.

## Option 3: Enable updates by using Managed Image Updates

You can also receive updates for Microsoft license-included applications through
Managed Image Updates. For more information, see [Update an Image by Using Managed WorkSpaces Applications Image Updates](keep-image-updated-managed-image-updates.md "keep-image-updated-managed-image-updates.md").
