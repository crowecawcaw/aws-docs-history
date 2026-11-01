

# Updates and maintenance
<a name="updating"></a>

You update AWS Coding Plugin for SAP ABAP ("Coding Plugin") through Eclipse, from the same update site you installed it from. The plug-in and Kiro CLI update on two independent tracks: Eclipse updates the plug-in when you run Help > Check for Updates, and Kiro CLI updates itself separately. Updating one does not update the other.

## Check for plug-in updates
<a name="updating-check-for-updates"></a>

Eclipse checks the update sites already configured for your installation, including the Coding Plugin update site, and offers any newer version it finds.

**To update Coding Plugin**

1. In Eclipse, choose **Help**, **Check for Updates**.

1. If a newer version is available, choose AWS Coding Plugin for SAP ABAP in the **Available Updates** list, then choose **Next**.

1. Review the update details, then choose **Next**.

1. Accept the license terms, then choose **Finish**.

1. When Eclipse prompts you to restart, choose **Restart Now**.

After Eclipse restarts, the new version of the plug-in is running.

## Review release notes
<a name="updating-release-notes"></a>

When the plug-in’s version changes, the What’s New window opens automatically after Eclipse restarts and summarizes what changed in that release.

## Uninstall AWS Coding Plugin for SAP ABAP
<a name="updating-uninstall"></a>

Uninstalling removes the plug-in from Eclipse. Your SAP system, your ABAP Development Tools (ADT) connection, and Kiro CLI are not affected.

**To uninstall Coding Plugin**

1. Choose **Help**, **About Eclipse** (macOS: **Eclipse**, **About Eclipse**).

1. Choose **Installation Details**.

1. On the **Installed Software** tab, choose AWS Coding Plugin for SAP ABAP.

1. Choose **Uninstall**.

1. Follow the prompts to finish, then restart Eclipse when prompted.

After Eclipse restarts, the plug-in’s chat window and editor integration no longer appear. To install the plug-in again, choose **Help**, **Install New Software** and enter the update site `https://downloads.aws.com/sap/aws-coding-plugin-for-sap-abap/current`.