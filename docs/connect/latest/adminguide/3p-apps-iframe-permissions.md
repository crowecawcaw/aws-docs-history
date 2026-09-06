

# Iframe permissions for third-party applications
<a name="3p-apps-iframe-permissions"></a>

When you configure third-party applications, you can specify `iframe` permission settings. You can change these permissions after creating the application.

By default, Connect Customer grants every third-party application four `iframe` permissions: `allow-forms`, `allow-popups`, `allow-same-origin`, and `allow-scripts`. If an application needs more, you can request additional `iframe` permissions when you register it.

**Note**  
Support for these permissions might vary by browser implementation.


| Permission | Description | 
| --- | --- | 
| Allow |  | 
| clipboard-read | Controls whether the application is allowed to read data from the clipboard. This permission is currently supported by Chrome, but not by Firefox or Safari. | 
| clipboard-write | Controls whether the application is allowed to write data to the clipboard. This permission is currently supported by Chrome, but not by Firefox or Safari. | 
| microphone | Controls whether the application is allowed to use audio input devices. | 
| camera | Controls whether the application is allowed to use video input devices. | 
| Sandbox |  | 
| allow-forms | Allows the page to submit forms. Supported by default. | 
| allow-popups | Allows the application to open popups. Supported by default. | 
| allow-same-origin | If this token is not used, the resource is treated as being from a special origin that always fails the same-origin policy (potentially preventing access to data storage, cookies, and some JavaScript APIs). Supported by default. | 
| allow-scripts | Allows the page to run scripts. Supported by default. | 
| allow-downloads | Allows downloading files through an <a> or <area> element with the download attribute, or through navigation that leads to a file download. | 
| allow-modal | Allows the page to open modal windows with Window.alert(), Window.confirm(), Window.print(), and Window.prompt(). Opening a <dialog> element is allowed regardless of this permission. | 
| allow-storage-access-by-user-activation | Allows the application to use the Storage Access API to request access to unpartitioned cookies. | 
| allow-popups-to-escape-sandbox | Allows the application to open a new browsing context without forcing the sandbox flags upon it. | 

## Sample configuration
<a name="3p-apps-iframe-permissions-sample-configuration"></a>

Configure iframe permissions with a template similar to the following.

For example, to grant clipboard permissions:

```
{
    "IframeConfig": {
        "Allow": [
            "clipboard-read",
            "clipboard-write"
        ],
        "Sandbox": [
            "allow-forms",
            "allow-popups",
            "allow-same-origin",
            "allow-scripts"
        ]
    }
}
```

**Important notes**
+ If you leave the iframe configuration field blank or set it to empty braces (`{}`), Connect Customer grants the following sandbox permissions:
  + allow-forms
  + allow-popups
  + allow-same-origin
  + allow-scripts

  ```
  {
      "IframeConfig": {
          "Allow": [],
          "Sandbox": ["allow-forms", "allow-popups", "allow-same-origin", "allow-scripts"]
      }
  }
  ```
+ To explicitly configure an application with no permissions, you must set empty arrays for both `Allow` and `Sandbox`:

  ```
  {
      "IframeConfig": {
          "Allow": [],
          "Sandbox": []
      }
  }
  ```