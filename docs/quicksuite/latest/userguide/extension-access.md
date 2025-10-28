# Extension access

Extension access connects your Amazon Quick Suite account to third party applications like
Microsoft Teams, Microsoft Outlook, Microsoft
Word, and Slack. Think of it as giving permission for
Amazon Quick Suite to work inside the apps your team already uses, helping them accomplish their
work, assisted by generative AI, and without context switching.

As an admin, you configure extension access. Then, either an admin or an author must
install the extension in the Amazon Quick Suite console to make the extension available to end
users. This default extension is available for use to all users on eligible subscriptions
after setup. Installed extensions are available under **Connections** >
**Extensions** in the Amazon Quick Suite menu for further configuration and
management.

If you're an admin user of Amazon Quick Suite, you configure Amazon Quick Suite access to extensions,
and can also deploy extensions for end user use. As an admin, you can also allow authors to
edit and deploy extensions after you configure access.

User roles and extension permissions work as follows:

- **IAM Administrators:** Can enable/remove extension
  access, create extensions, assign owners, and control extension availability for the
  organization.
- **Authors:** Can create and install extensions using
  administrator-enabled access, and edit/delete extensions they own.
- **Readers (Reader Pro only):** Can use all enabled
  extensions but cannot create or modify them.
  Here's what you need to know about extension access:

- **What it is:** A secure connection between your
  Amazon Quick Suite instance and your organization's account in third-party apps (like your
  Microsoft 365 or Slack workspace).
- **Why it matters:** It gives your Amazon Quick Suite
  instance permission to work within your organization's specific tenant or workspace
  in these apps.
- **Who sets it up:** Only administrators with IAM
  credentials can configure extension access and deploy extensions (or give authors
  permission to edit and deploy extensions) - it's a privileged operation that must be
  done before your team can start using extensions. Note that IAM admin users can
  access the **Extension access** pages from the **Manage
  Quick Suite** menu, but to configure a extension they may need to
  re-log in to the system and select **Connections** >
  **Extensions** from the Amazon Quick Suite menu.

###### Topics

- [Browser extension](browser-extension.md "browser-extension.md")
- [Amazon Quick Suite Microsoft Outlook
  extension](outlook-extension.md "outlook-extension.md")
- [Amazon Quick Suite Slack extension](slack-extension.md "slack-extension.md")
- [Amazon Quick Suite Microsoft Word
  extension](word-extension.md "word-extension.md")
- [Amazon Quick Suite Microsoft Teams
  extension](teams-extension.md "teams-extension.md")
