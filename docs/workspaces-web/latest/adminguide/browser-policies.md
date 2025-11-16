# Managing browser policy in Amazon WorkSpaces Secure Browser

You can set any custom browser policy using Chrome policies available for the latest stable version to WorkSpaces Secure Browser. When you set a policy in the WorkSpaces Secure Browser portal, the policy will apply to all sessions managed by that web portal.

There are more than 300 policies you can apply to a web portal. For more information, including the complete list of Chrome policies, see [Chrome Enterprise policy list](https://chromeenterprise.google/policies/ "https://chromeenterprise.google/policies/").

You have three ways to set a Chrome policy:

1. Using the visual editor in the web portal

By using the console view to create a web portal, you can apply some of the most common policies in the visual editor:

    * `StartURL`
    * Turning private browsing on and off
    * History deletion
    * Bookmarks and bookmark folders

2. Using the JSON editor in the web portal

You can also directly add or edit policies by using the JSON editor instead of the visual editor.

For the specific format of a policy, please refer to [Chrome Enterprise policy list](https://chromeenterprise.google/policies/ "https://chromeenterprise.google/policies/"). 3. Uploading a JSON file into the web portal

You can also import the Chrome policies used in your organization by uploading a JSON file into the web portal.

For details, please see [Tutorial: Setting a custom browser policy in Amazon WorkSpaces Secure Browser](browser-policies-custom.md "browser-policies-custom.md")
WorkSpaces Secure Browser applies a baseline browser policy configuration to all portals along with any policies
that you specify. You can edit some of these policies with your custom JSON file. For more
information, see [Editing the baseline browser policy in Amazon WorkSpaces Secure Browser](browser-policies-baseline.md "browser-policies-baseline.md").

###### Topics

- [Tutorial: Setting a custom browser policy in Amazon WorkSpaces Secure Browser](browser-policies-custom.md "browser-policies-custom.md")
- [Editing the baseline browser policy in Amazon WorkSpaces Secure Browser](browser-policies-baseline.md "browser-policies-baseline.md")
