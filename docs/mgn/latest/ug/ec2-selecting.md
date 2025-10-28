NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Selecting the default template

AWS MGN uses the version of the Launch template that is marked as default.

In order to select the default launch template, on the **Modify
template (Create new version)** page, under the **Launch template
name and version description** category, open the **Source
template** menu and choose the EC2 launch template you want to use as the default
template from the drop-down menu.

Every time you modify the Launch template, a new version of the launch template is
created. You are notified that the Launch template has been modified and that a new version
(version number) has been created. Make sure to take note of the version number and the
**Launch template ID** so that you could easily identify your
launch template and version.

###### Note

It's good practice to delete versions of the launch template that you no longer need.

To set the new version of your launch template as the default:

1. Navigate back to the main **EC2 > Launch templates**
   page.
2. Choose your launch template by selecting the toggle to the left of the **Launch template ID**.
3. Open the Actions menu and choose **Set default version**.
4. Select the **Template version** from the drop-down menu and
   then choose **Set as default version**.
   The Amazon EC2 console confirms the version change.
