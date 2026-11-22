

# Prerequisites

To use WebAuthn redirection, you must meet the following requirements:
+ One of the following supported WorkSpaces Applications clients:
  + Windows client version 1.5.0.1071 or later
  + macOS client version 1.6.0.1119 or later
+ A FIDO2 authenticator connected to the user's local device, such as a USB security key.

Windows fleets have the following additional requirements:
+ A streaming instance that runs Windows Server 2019 or later.
+ A WorkSpaces Applications agent released on or after October 20, 2026.

Linux fleets have the following additional requirements:
+ A streaming instance that runs Rocky Linux 8, Red Hat Enterprise Linux 8, or newer. Amazon Linux 2 is not supported.
+ A WorkSpaces Applications managed image released on or after October 20, 2026.
+ Google Chrome, Chromium, or Microsoft Edge installed in the image.
+ A fleet with internet access enabled, so the browser can download the Amazon DCV WebAuthn redirection extension from the Chrome Web Store or Microsoft Edge Add-ons.