

# Configure the process compatibility list (Windows fleets)

On Windows fleets, the process compatibility list controls which processes in the streaming session can make WebAuthn requests that are redirected to the user's device. The list is optional. When you don't specify one, WorkSpaces Applications applies the following default list:
+ `chrome.exe` (Google Chrome)
+ `msedge.exe` (Microsoft Edge)
+ `msedgewebview2.exe` (embedded Microsoft Edge WebView2, used by many desktop applications)
+ `firefox.exe` (Mozilla Firefox)
+ `island.exe` (Island browser)
+ `Microsoft.AAD.BrokerPlugin.exe` (Microsoft sign-in broker, required for Microsoft Teams and Microsoft 365)
+ `dcvwebauthnnativemsghost.exe` (Amazon DCV component)

To add support for another application, add its process image name to the list. Keep the following rules in mind:
+ Enter 1 to 100 process names. Each name must end in `.exe` and can be up to 260 characters. Names are not case-sensitive, and duplicates are rejected.
+ Updating the stack setting replaces the whole setting. If you update the stack and set only **Enable WebAuthn redirection**, any process compatibility list stored earlier is removed and the default list applies again.
+ The process compatibility list is not supported on Linux fleets. If a stack has a process compatibility list, you cannot associate a Linux fleet with it. You also cannot add a list to a stack that already has a Linux fleet associated.