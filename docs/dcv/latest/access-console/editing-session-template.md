

# Editing a session template
<a name="editing-session-template"></a>

If you need to adjust any sessions details, you can edit the parameters of an existing session template.

**Note**  
Editing an existing template could affect users already assigned to it. Any changes you make will not affect the sessions already created. However, it will affect users the next time they create a session using the modified template. If you do not want to affect users who already have this template assigned to them, [Duplicating a session template](duplicating-session-template.md) may be a better option.

1. Select the session template that you want to edit. 

1. Click on the **Actions** button.

1. Select **Edit** from the drop-down menu. This will take you to the **Configure template details** page.  
![Session templates interface showing list of templates with options to edit or delete.](http://docs.aws.amazon.com/dcv/latest/access-console/images/session-templates-actions-edit.png)

1. Change any of the information in the **Configure template details** page.

   This page chooses the parameters of your session template. These parameters define the details of the session and create boundaries for what kind of hosts a session can be created on. See [Session template details](session-templates.md#session-template-details) for more information.

1. Assign users or user groups to the session template.

   You can assign a session template for existing users or groups to use when creating sessions. You can do this either during template creation or after a template has already been created. For more information, see [Assigning a session template to users or groups](assigning-session-template.md).

1. Select the **Update template** button.