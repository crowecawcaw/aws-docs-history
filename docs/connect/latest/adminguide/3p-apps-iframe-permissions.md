# Iframe permissions when granting

third-party applications access to Amazon Connect

When configuring third-party applications through either the AWS Console's
`onboarding` UI or API, you have the ability to specify
`iframe` permission settings. These permissions can be modified even
after the application has been set up.

By default, all third-party applications are granted four basic
`iframe` permissions: `allow-forms`,
`allow-popups`, `allow-same-origin`, and
`allow-scripts`. Since some applications may require enhanced
functionality, additional `iframe` permissions can be requested during
the application registration process.

###### Note

The browser compatibility for the following permissions could vary by
different browser implementations.

| Permission                              | Description                                                                                                                                                                                                                            |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Allow**                               |                                                                                                                                                                                                                                        |
| clipboard-read                          | Controls whether the application is allowed to read data from the clipboard. Its currently supported by Chrome, but not by Firefox and Safari.                                                                                         |
| clipboard-write                         | Controls whether the application is allowed to write data to the clipboard. Its currently supported by Chrome, but not by Firefox and Safari.                                                                                          |
| microphone                              | Controls whether the application is allowed to use audio input devices.                                                                                                                                                                |
| camera                                  | Controls whether the application is allowed to use video input devices.                                                                                                                                                                |
| **Sandbox**                             |                                                                                                                                                                                                                                        |
| allow-forms                             | Allows the page to submit forms. Its supported by default.                                                                                                                                                                             |
| allow-popups                            | Allows the application to open popups. Its supported by default.                                                                                                                                                                       |
| allow-same-origin                       | If this token is not used, the resource is treated as being from a special origin that always fails the same-origin policy (potentially preventing access to data storage/cookies and some JavaScript APIs). Its supported by default. |
| allow-scripts                           | Allows the page to run scripts. Its supported by default.                                                                                                                                                                              |
| allow-downloads                         | Allows downloading files through an <a> or <area> element with the download attribute, as well as through the navigation that leads to a download of a file                                                                            |
| allow-modal                             | Allows the page to open modal windows by Window.alert(), Window.confirm(), Window.print() and Window.prompt(), while opening a <dialog> is allowed regardless of this keyword                                                          |
| allow-storage-access-by-user-activation | Allows to use the Storage Access API to request access to unpartitioned cookies.                                                                                                                                                       |
| allow-popups-to-escape-sandbox          | Allows to open a new browsing context without forcing the sandboxing flags upon it                                                                                                                                                     | ## Sample Configuration Iframe permissions can be configured using a similar template to the following. For example, to grant clipboard permissions: `{ "IframeConfig": { "Allow": [ "clipboard-read", "clipboard-write" ], "Sandbox": [ "allow-forms", "allow-popups", "allow-same-origin", "allow-scripts" ] } }` ###### Important Notes 1. By default, if the iframe configuration field is left blank or set to empty curly braces {}, the following sandbox permissions are automatically granted: <br>• allow-forms <br>• allow-popups <br>• allow-same-origin <br>• allow-scripts `{ "IframeConfig": { "Allow": [], "Sandbox": ["allow-forms", "allow-popups", "allow-same-origin", "allow-scripts"] } }` 2. To explicitly configure an application with no permissions, you must set empty arrays for both `Allow` and `Sandbox`: `{ "IframeConfig": { "Allow": [], "Sandbox": [] } }` |
