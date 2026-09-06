

# Browser extension
<a name="browser-extension"></a>

The Amazon Quick browser extension is available within Amazon Quick to all eligible users by default and requires no administrative setup for user access. Users can find the browser extension installation link under **Connections** > **Extensions**. The following procedures are for IT administrators who want to automatically deploy or disable the Amazon Quick browser extension across all browsers in their organization using managed device policies.

**Topics**
+ [Deploy the browser extension](#browser-extension-deployment)
+ [Disable the browser extension](#disable-browser-extension)

## Deploy the browser extension
<a name="browser-extension-deployment"></a>

**Note**  
The following deployment guide applies only when you have a managed device fleet with managed browsers.

To deploy the browser extension to all users in your organization, you can define an **ExtensionSettings** policy and distribute this policy to your managed devices.

**Topics**
+ [Install using ExtensionSettings policy](#install-by-extensionsettings)
+ [Distribute ExtensionSettings policy](#distributing-extensionsettings)

### Install using ExtensionSettings policy
<a name="install-by-extensionsettings"></a>

The **ExtensionSettings** policy is an administrative setting for Chrome, Edge, and Firefox that allows you to manage the installation, permissions, and runtime behavior of specific extensions on managed devices. This policy provides granular control by letting administrators specify custom configurations, such as setting installation modes like force install and restricting or allowing specific site access and permissions for individual extensions or all extensions.

The format of the **ExtensionSettings** policy depends on the operating system where you want to distribute this policy. Windows, Mac, and Linux are supported.

To set the install mode in the **ExtensionSettings** policy, you need the extension identifier and the store URL:
+ **Chrome/Edge**
  + ID: `innkphffipcmiflfibbeghfnkifiokgo`
  + URL: `https://clients2.google.com/service/update2/crx`
+ **Firefox**
  + ID: `quick-browser-extension@amazon.com`
  + URL: `https://addons.mozilla.org/firefox/downloads/latest/amazon-quick/latest.xpi`

### Distribute ExtensionSettings policy
<a name="distributing-extensionsettings"></a>

Distributing the **ExtensionSettings** policy depends on the device and browser management solution used by your organization. You can use managed solutions like **Chrome Enterprise Core** or **Microsoft Edge** management service, or distribute the **ExtensionSettings** policy using **Group Policy**, which differs per operating system.

## Disable the browser extension
<a name="disable-browser-extension"></a>

**Note**  
The following deployment guide applies only when you have a managed device fleet with managed browsers.

To disable the browser extension for all users in your organization, you can define an **ExtensionSettings** policy and distribute this policy to your managed devices.

**Topics**
+ [Disable using ExtensionSettings policy](#disable-by-extensionsettings)
+ [Distribute ExtensionSettings policy](#distributing-extensionsettings-disable)

### Disable using ExtensionSettings policy
<a name="disable-by-extensionsettings"></a>

The **ExtensionSettings** policy is an administrative setting for Chrome, Edge, and Firefox that allows you to manage the installation, permissions, and runtime behavior of specific extensions on managed devices. This policy provides granular control by letting administrators specify custom configurations, such as disabling individual extensions.

The format of the **ExtensionSettings** policy depends on the operating system where you want to distribute this policy. See the documentation for the **ExtensionSettings** policy to determine the format. Windows, Mac, and Linux are supported.

To block the use of the extension in the **ExtensionSettings** policy, you need the extension identifier:
+ **Chrome/Edge**

  ID: `innkphffipcmiflfibbeghfnkifiokgo`
+ **Firefox**

  ID: `quick-browser-extension@amazon.com`

### Distribute ExtensionSettings policy
<a name="distributing-extensionsettings-disable"></a>

Distributing the **ExtensionSettings** policy depends on the device and browser management solution used by your organization. You can use managed solutions like **Chrome Enterprise Core** or **Microsoft Edge** management service, or distribute the **ExtensionSettings** policy using **Group Policy**, which differs per operating system.