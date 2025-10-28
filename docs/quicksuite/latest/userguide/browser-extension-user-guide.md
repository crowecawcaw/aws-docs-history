# Amazon Quick Suite browser extension

###### Important

The Amazon Quick Suite browser extension extension doesn't need any admin setup to
install and use.

The Amazon Quick Suite browser extension integrates AI-powered assistance directly into your
web browsing experience. Users can access Quick Suite capabilities within their
browser to enhance productivity, streamline research, and get instant help without
switching between applications.

Key capabilities include:

- Summarize web pages for quick understanding.
- Ask questions about multiple web pages and access organizational knowledge
  from spaces.
- Use actions from [action connectors](action-connectors.md "action-connectors.md") configured in
  Quick Suite.
- Analyze files uploaded to Quick Suite during browsing sessions.
  The AI-powered assistance enables you to maximize reading productivity, streamline
  research and analysis of complex information, and get instant help when creating content
  without context switching during web browsing.

###### Topics

- [Supported browsers](#browser-extension-supported-browsers "#browser-extension-supported-browsers")
- [Browser extension benefits](#browser-extension-benefits "#browser-extension-benefits")
- [Browser extension use cases](#browser-extension-use-cases "#browser-extension-use-cases")
- [Install and configure the browser
  extension](#install-and-configure-browser "#install-and-configure-browser")
- [Deploy the browser extension
  in your organization](#deploy-browser-extension-organization "#deploy-browser-extension-organization")
- [Browser extension usage
  guidelines](#browser-extensions-usage-guidelines "#browser-extensions-usage-guidelines")
- [Browser extension known
  limitations](#browser-extension-known-limitations "#browser-extension-known-limitations")

## Supported browsers

The Quick Suite browser extension is compatible with the following
browsers:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge

## Browser extension benefits

The Quick Suite browser extension provides powerful AI-driven capabilities
that transform how you interact with web content. These key benefits help you work
more efficiently and make better use of information you encounter while browsing,
bringing enterprise knowledge directly into your web research workflows without
requiring application switching.

**Embedded productivity features**

- Summarize a snapshot of any web page for quick understanding and
  analysis.
- Ask questions about one or more web pages using your organizational
  knowledge.
- Analyze both files you upload to Quick Suite and specific spaces it
  can access.
- Execute actions from configured action connectors without leaving your
  browser.

## Browser extension use cases

The following are common use cases that help you make the best use of your
Quick Suite browser extension:

###### Summarize web pages

Use this procedure to quickly understand web page content without reading the
entire page.

1. Open the Quick Suite browser extension.
2. Log in and navigate to the web page you want to summarize.
3. From the chat interface, select **Summarize** for a
   summary of a snapshot of that web page.

Your conversation now contains a snapshot of this web page. You can continue to
chat about the web page and ask follow-up questions.

###### Add individual pages to your conversation scope

Use this procedure to include multiple web pages in your conversation context
for comprehensive analysis.

1. Navigate to the web page you want to add to your conversation.
2. Select the **+** icon to add the page to your
   scope.
3. Navigate from tab to tab and select the **+** icon for
   each page you want to chat about.
4. You can now chat about all the pages you've added to your scope.

This allows you to analyze and compare information across multiple web pages in a
single conversation.

###### Add files to a conversation

Upload files to enhance your conversation with document analysis
capabilities.

1. Select the **paperclip** icon.
2. Select the files to add to the conversation.
3. Select **Add to chat**.

The files are now available to use in the Quick Suite conversation.

###### Add webpages as context to a conversation

Include multiple browser tabs in your conversation for comprehensive web
content analysis.

1. Select **No tabs selected**.
2. From **Add tabs**, choose the tabs you want to include in
   your Quick Suite conversation.
3. Select **Confirm**.

The tabs are now available in your Quick Suite conversation.

###### Reset conversation context

Start fresh when you need to clear your current conversation context.

1. Select the **+ icon inside the bubble** to start a new
   conversation.
2. Alternatively, you can reset your conversation by selecting the
   **X** icon to end the current conversation and then
   open the Quick Suite extension to start a new conversation.

This clears all previous context and allows you to begin with a clean
slate.

###### Use actions in chat

Execute external actions directly from your browser extension
conversation.

1. Ask the chat to perform a specific action.
2. Follow the prompts in the chat and on-screen to complete the
   action.

This enables you to perform tasks in external applications without leaving your
browser.

## Install and configure the browser

extension

As a user, you can install and configure the browser extensions with the following
steps.

- Mozilla based browsers — [Mozilla Firefox Add-ons web store](https://addons.mozilla.org/en-GB/firefox/addon/amazon-quick/ "https://addons.mozilla.org/en-GB/firefox/addon/amazon-quick/")
- Chromium based browsers (including Microsoft Edge) — [Chrome Web Store](https://chromewebstore.google.com/detail/amazon-quick/innkphffipcmiflfibbeghfnkifiokgo "https://chromewebstore.google.com/detail/amazon-quick/innkphffipcmiflfibbeghfnkifiokgo")

Once you have successfully logged on, you can use your Quick Suite browser
extension.

###### Note

You can also **pin** your Quick Suite browser extension
to have it readily accessible while using your browser. Instructions for this
are specific to your browser of choice. The following third-party information
about pinning extensions might be helpful.

- Google Chrome — [https://www.howtogeek.com/683099/how-to-pin-and-unpin-extensions-from-the-chrome-toolbar](https://www.howtogeek.com/683099/how-to-pin-and-unpin-extensions-from-the-chrome-toolbar "https://www.howtogeek.com/683099/how-to-pin-and-unpin-extensions-from-the-chrome-toolbar")
- Mozilla Firefox — [https://support.mozilla.org/en-US/kb/extensions-button#w_manage-pinned-extensions](https://support.mozilla.org/en-US/kb/extensions-button#w_manage-pinned-extensions "https://support.mozilla.org/en-US/kb/extensions-button#w_manage-pinned-extensions")
- Microsoft Edge — [https://www.microsoft.com/en-us/edge/features/pin-to-taskbar](https://www.microsoft.com/en-us/edge/features/pin-to-taskbar "https://www.microsoft.com/en-us/edge/features/pin-to-taskbar")

## Deploy the browser extension

in your organization

As an author, after enabling the browser extension in your Quick Suite
application, you can deploy it across your organization using enterprise management
tools and policies.

For Google Chrome Enterprise environments, you can use
organizational unit policies to manage extension deployment. The Chrome Web
Store for Enterprise provides additional deployment options specifically
designed for organizational use. Mozilla Firefox Enterprise offers
similar capabilities through policy templates and enterprise distribution methods
that allow for automated extension deployment across the organization.
Microsoft Edge Enterprise provides policy settings for managing
extensions through mobile device management (MDM) software.

Policy settings from browser vendors: [Firefox](https://mozilla.github.io/policy-templates/#extensionsettings "https://mozilla.github.io/policy-templates/#extensionsettings"), [Chrome](https://chromeenterprise.google/policies/#ExtensionSettings "https://chromeenterprise.google/policies/#ExtensionSettings"), and [Edge](https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings "https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings").

###### Deploy to Google Chrome Enterprise

Follow these steps to deploy the browser extension across your Chrome
Enterprise environment.

1. Access your Google Admin console and navigate to the
   Chrome management section.
2. Configure extension policies using organizational units to target specific
   user groups or departments.
3. Use the [Chrome extension management guide](https://support.google.com/chrome/a/answer/9296680?hl=en "https://support.google.com/chrome/a/answer/9296680?hl=en") to set up
   automated installation policies.
4. Reference the [Chrome Web Store Enterprise documentation](https://developer.chrome.com/docs/webstore/cws-enterprise "https://developer.chrome.com/docs/webstore/cws-enterprise")
   for advanced deployment configurations.

The extension will now be automatically installed for all users in your Chrome
Enterprise environment.

###### Deploy to Mozilla Firefox Enterprise

Use these steps to deploy the extension across your Firefox Enterprise
environment.

1. Configure Firefox deployment policies using the enterprise
   policy framework.
2. Follow the [Firefox extension deployment guide](https://support.mozilla.org/en-US/kb/deploying-firefox-with-extensions "https://support.mozilla.org/en-US/kb/deploying-firefox-with-extensions") for
   step-by-step instructions.
3. Use the [enterprise distribution documentation](https://extensionworkshop.com/documentation/enterprise/enterprise-distribution/ "https://extensionworkshop.com/documentation/enterprise/enterprise-distribution/") to configure
   organization-wide deployment.
4. Apply extension settings using [Mozilla policy templates](https://mozilla.github.io/policy-templates/#extensionsettings "https://mozilla.github.io/policy-templates/#extensionsettings") for centralized
   configuration management.

The extension is now deployed across your Firefox Enterprise environment with
centralized management.

###### Deploy to Microsoft Edge Enterprise

Deploy the extension to Microsoft Edge Enterprise using these organizational
deployment steps.

1. Install the browser extension for all users using the software deployment
   processes of your organization.
2. Configure extension settings using [Edge policy settings](https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings "https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings") through mobile device
   management (MDM) software.
3. Follow the [Microsoft Edge extension management guide](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide")
   for detailed deployment instructions.

Your Microsoft Edge Enterprise deployment is complete with centralized policy
management.

## Browser extension usage

guidelines

As a user, you are responsible for keeping company information safe. The following
guidelines help you use Quick Suite browser extensions securely while
maintaining data privacy and compliance.

### Using the browser extension

When using the Quick Suite browser extension, users can review past
conversations and attachments to maintain context across browsing
sessions.

### Conversation retention and data

privacy

Amazon Quick Suite maintains strict data privacy through automated retention
policies:

- Amazon Quick Suite automatically deletes conversations and related files
  after 30 days of inactivity.
- Browser extension conversation retention follows your company's
  specific history rules.
- Browser extension retention periods may exceed Amazon Quick Suite's standard
  30-day limit based on organizational policies.

## Browser extension known

limitations

The following are known limitations of the Amazon Quick Suite browser extension:

- The browser extension does not support [flows](flows.md "flows.md").
- The browser extension supports up to a total of 20 web pages and uploaded
  files at a time. For more information, see [Upload files and chat](using-quick-chat.md#file-uploads "using-quick-chat.md#file-uploads").
