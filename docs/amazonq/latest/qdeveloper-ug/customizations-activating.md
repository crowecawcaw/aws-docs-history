# Activating your Amazon Q

customizations

## Activating a version

This section describes how to activate and deactivate a version of your
customization.

You can activate a new version of a customization, even while developers from your
organization are using the previous version. After you activate the new version, the
developers will seamlessly begin using it, with no adjustments needed on the
development side.

You can also roll your customization back to a previously active state. However,
Amazon Q does not actually re-activate a previously activated version. Instead, it
creates a new version by copying a previous version and then activating the
copy.

For example, suppose that you have three versions: 1, 2, and 3. The active version
is 3. You decide to go back to version 1. But "re-activating" version 1 is actually
just copying version 1 and creating version 4. That's the version you use: version
4, the new copy of the old version.

To activate a version of your customization, follow this procedure:

1. Sign in to the AWS Management Console.
2. Switch to the Amazon Q Developer console.
3. From the navigation pane on the left, choose
   **Customizations**.

The customizations page will appear. 4. Choose the customization you want to activate a version for.

The customization details page will appear. 5. Choose the version you want to activate from the
**Versions** table. 6. Choose **Activate**.

To deactivate a customization, choose **Deactivate** from the
dropdown.
