# Tutorial: Setting a custom browser policy in Amazon WorkSpaces Secure Browser

You can set any supported Chrome policy for Linux by uploading a JSON file. To learn more
about Chrome policies, see [Chrome
Enterprise policy list](https://chromeenterprise.google/policies/ "https://chromeenterprise.google/policies/") and select the Linux platform. Then, search and review the
policies for the most recent stable version.

In the following tutorial, you create a web portal with the following policy
controls:

- Set up bookmarks
- Set up default startup pages
- Prevent the user from installing other extensions
- Prevent the user from deleting history
- Prevent the user from accessing incognito mode
- Pre-install the [Okta plug-in](https://help.okta.com/en-us/Content/Topics/Browser-Plugin/silent-install-chrome.htm "https://help.okta.com/en-us/Content/Topics/Browser-Plugin/silent-install-chrome.htm") extension for all sessions.

###### Topics

- [Step 1: Create a web portal](#browser-policies-custom-step1 "#browser-policies-custom-step1")
- [Step 2: Gather policies](#browser-policies-custom-step2 "#browser-policies-custom-step2")
- [Step 3: Create a custom JSON policy
  file](#browser-policies-custom-step3 "#browser-policies-custom-step3")
- [Step 4: Add your policies to the
  template](#browser-policies-custom-step4 "#browser-policies-custom-step4")
- [Step 5: Upload your policy JSON file to your
  web portal](#browser-policies-custom-step5 "#browser-policies-custom-step5")

## Step 1: Create a web portal

In order to upload your Chrome policy JSON file, you must create a WorkSpaces Secure Browser portal. For more
information, see [Creating a web portal for Amazon WorkSpaces Secure Browser](getting-started-step1.md "getting-started-step1.md").

## Step 2: Gather policies

Search for and locate policies you want from Chrome Policy. You then use the policies to
create a JSON file in the next step.

1. Go to [Chrome Enterprise policy
   list](https://chromeenterprise.google/policies/ "https://chromeenterprise.google/policies/").
2. Choose the platform **Linux**, and then choose the most recent Chrome
   version.
3. Search for the policies you want to set. For this example, search for extensions to find
   policies for managing them. Each policy includes a description, Linux preference name, and
   sample value.
4. From the search results, there are 3 policies that meet the business requirements if
   used together:
   - **ExtensionSettings** – Installs an extension at browser
     start.
   - **ExtensionInstallBlocklist** – Prevents specific extensions
     from being installed.
   - **ExtensionInstallAllowlist** – Allows certain extensions to
     be installed.

5. Additional policies satisfy the remaining requirements;
   - **ManagedBookmarks** – Adds bookmarks to webpages.
   - **RestoreOnStartupURLs** – Configures which webpages are
     opened whenever a new browser window is launched.
   - **AllowDeletingBrowserHistory** – Configures whether users can
     delete their browsing history.
   - **IncognitoModeAvailability** – Configures whether users can
     access incognito mode.

## Step 3: Create a custom JSON policy

file

Create a JSON file using a text editor, template, and the policies you found in the
previous step.

1. Open a text editor.
2. Copy and paste the following template into your text editor:

```

{
  "chromePolicies":
    {
        "ManagedBookmarks":
        {
            "value":
            [
                {
                    "name": "Bookmark 1",
                    "url": "`bookmark-url-1`"
                },
                {
                    "name": "Bookmark 2",
                    "url": "`bookmark-url-2`"
                },
            ]
        },
        "RestoreOnStartup":
        {
            "value": 4
        },
        "RestoreOnStartupURLs":
        {
            "value":
            [
                "`startup-url`"
            ]
        },
        "ExtensionInstallBlocklist": {
            "value": [
                "`insert-extensions-value-to-block`",
            ]
        },
        "ExtensionInstallAllowlist": {
            "value": [
                "`insert-extensions-value-to-allow`",
            ]
        },
        "ExtensionSettings":
        {
            "value":
            {
                "`insert-extension-value-to-force-install`":
                {
                    "installation_mode": "force_installed",
                    "update_url": "https://clients2.google.com/service/update2/crx",
                    "toolbar_pin": "force_pinned"
                },
            }
        },
        "AllowDeletingBrowserHistory":
        {
            "value": `should-allow-history-deletion`
        },
        "IncognitoModeAvailability":
        {
            "value": `incognito-mode-availability`
        }
    }
}


```

## Step 4: Add your policies to the

template

Add your custom policies to the template for each business requirement.

1. Set up bookmark URLs.
   1. Under the `value` key, add pairs of `name` and `url`
      keys for each bookmark you want to add.
   2. Set `bookmark-url-1` to `https://www.amazon.com`.
   3. Set `bookmark-url-2` to
      `https://docs.aws.amazon.com/workspaces-web/latest/adminguide/`.

```

    "ManagedBookmarks":
        {
            "value":
            [
                {
                    "name": "`Amazon`",
                    "url": "`https//www.amazon.com`"
                },
                {
                    "name": "`Bookmark 2`",
                    "url": "`https://docs.aws.amazon.com/workspaces-web/latest/adminguide/`"
                },
            ]
        },

```

2. Set up the startup URLs. This policy allows administrators to set the webpages displayed
   when a user launches a new browser window.
   1. Set the `RestoreOnStartup` to `4`. This sets the
      `RestoreOnStartup` action to open a list of URLs . You can also use other
      actions on your startup URLs. For more information, see [Chrome Enterprise policy
      list](https://chromeenterprise.google/policies/ "https://chromeenterprise.google/policies/").
   2. Set `RestoreOnStartupURLs` to https://www.aboutamazon.com/news.

```

     "RestoreOnStartup":
        {
            "value": `4`
        },
    "RestoreOnStartupURLs":
        {
            "value":
            [
                "`https://www.aboutamazon.com/news`"
            ]
        },

```

3. To prevent the user from deleting their browser history, set
   `AllowDeletingBrowserHistory` to `false`.

```

     "AllowDeletingBrowserHistory":
        {
            "value": `false`
        },

```

4. To turn off access to Incognito mode access for your users, set
   `IncognitoModeAvailability` to `1`.

```

     "IncognitoModeAvailability":
        {
            "value": `1`
        }

```

5.  Set and enforce the [Okta plug-in](https://help.okta.com/en-us/Content/Topics/Browser-Plugin/silent-install-chrome.htm "https://help.okta.com/en-us/Content/Topics/Browser-Plugin/silent-install-chrome.htm") with the following policies:

        * `ExtensionSettings` – Installs an extension at browser start. The
         extension value is available from the Okta plug-in help page.
        * `ExtensionInstallBlocklist` – Prevents specific extensions from
         being installed. Use a `*` value to prevent all extensions by default.
         Administrators can control which extensions to allow on the
         `ExtensionInstallAllowlist`.
        * `ExtensionInstallAllowlist` allows you to install certain extensions. Since
         `ExtensionInstallBlocklist` is set to `*`, add the Okta plug-in
         value here to allow it.

    The following shows an example policy to turn on the Okta plug-in:

```

        "ExtensionInstallBlocklist": {
            "value": [
                "`*`",
                ]
        },
        "ExtensionInstallAllowlist": {
            "value": [
                "`glnpjglilkicbckjpbgcfkogebgllemb`",
               ]
        },
        "ExtensionSettings": {
            "value": {
                "`glnpjglilkicbckjpbgcfkogebgllemb`": {
                    "installation_mode": "`force_installed`",
                    "update_url": "`https://clients2.google.com/service/update2/crx`",
                    "toolbar_pin": "`force_pinned`"
            }
        }

```

## Step 5: Upload your policy JSON file to your

web portal

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/ "https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/").
2. Choose **WorkSpaces Secure Browser**, then choose **Web
   portals**.
3. Choose your web portal, and then choose **Edit**.
4. Choose **Policy settings**, then choose **JSON file
   upload**.
5. Choose **Choose File**. Navigate to, select, and upload your JSON
   file.
6. Choose **Save**.
