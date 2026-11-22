

# Troubleshooting

**The website or application never prompts for the security key (Windows fleets)**
+ Confirm that WebAuthn redirection is enabled on the stack associated with the fleet.
+ Confirm that the user started a new session after the stack was updated.
+ Confirm that the process making the request is on the process compatibility list. If you specified a custom list, confirm that it still includes the browser or application in use.
+ Confirm that the user is connecting from a supported Windows or macOS client version. The web client does not support WebAuthn redirection.
+ For Microsoft Teams and Microsoft 365 sign-in, confirm that `Microsoft.AAD.BrokerPlugin.exe` is on the process compatibility list.

**The website never prompts for the security key (Linux fleets)**
+ Confirm that the user is using Google Chrome, Chromium, or Microsoft Edge. Firefox and other browsers are not supported on Linux fleets.
+ Confirm that the fleet has internet access so the browser can download the Amazon DCV WebAuthn redirection extension.
+ In the browser, open the extensions page and confirm that the Amazon DCV WebAuthn redirection extension is installed and enabled. A managed policy installs the extension, and it takes effect the next time the browser starts.
+ If you force-install your own browser extensions with a managed policy, set `PolicyListMultipleSourceMergeList` to include `ExtensionInstallForcelist`. This setting merges your policy with the WorkSpaces Applications policy instead of replacing one with the other.

**The browser reports that the operation timed out or was not allowed**
+ Confirm that the security key is connected to the local device and that the user touched it when prompted. If the website requires user verification, the user must also enter the key's PIN.
+ If the user has more than one authenticator connected, the client prompts them to select one.
+ Try a different browser or authenticator to isolate the issue.

**AssociateFleet or UpdateFleet fails with an incompatible image error**
+ The fleet's image does not support WebAuthn redirection. Use an image with a WorkSpaces Applications agent version released on or after October 20, 2026, or rebuild your image from one.
+ Amazon Linux 2 images are not supported.

**AssociateFleet fails with "ProcessCompatibilityList is not supported on Linux fleets"**
+ If you are using the AWS CLI to configure the feature, do not provide a ProcessCompatibilityList when a Linux fleet is or will be associated.