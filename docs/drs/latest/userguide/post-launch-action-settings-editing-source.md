# Activating,

deactivating, and editing predefined or custom actions

You can activate, deactivate and edit actions available for this source server.
Activating an action ensures it runs after launching a recovery instance. Likewise,
deactivating it, prevents it from being run after launching a recovery instance. The
default settings are not affected by activating, deactivating or editing an action for a
source server. Editing an action for a source server updates it for that source server.
These changes are not reflected on the action, if it exists in the default post-launch
actions settings. Changes to actions in the default settings, as to apply to newly added
source servers, can be done from the **Settings → Default post-launch
actions** page.

To be able to activate, create, deactivate, edit, or delete a custom action and to activate, deactivate or edit predefined actions for a source server, make sure the post-launch actions are activated for that source server.

## Activating, deactivating and editing predefined or custom actions

To activate, deactivate or edit a post launch action in the default post-launch actions settings, go to **Source server details** page, and visit the **Post-launch settings** tab.
If **Post-launch actions settings** shows **Post-launch actions** to be **Active**, you can edit any action defined for the source server.

Locate the action you want to edit in the **Actions** card view, or use the search field to filter the actions by name.

Choose the action’s card to select it, and then choose the **Edit** button.

To activate the action, make sure the **Activate this action setting** is checked and click the **Save** button.
To deactivate, make sure the **Activate this action** setting is un-checked and click the **Save** button.

The edit page allow you to change the value of some of the parameters for
both pre-defined actions and custom actions. Some parameters can only be edited if the
action is a custom action. See below for specific information.

The parameters that appear on the edit page:

- **Action name** – Editable for custom actions. The name of the action in AWS DRS, which should be intuitive, meaningful and unique in this AWS account and region.
- **Activate this action** – Use this checkbox to
  activate or deactivate the action for this source server. Only active actions run after
  the launch of a recovery instance.
- **Mark launch as successful only if this action finishes
  running successfully** – This checkbox dictates whether or not the launch is
  marked as successful, based on the successful run of this action. Instances launches
  progress normally regardless of the success of the action.
- **System Manager document name** – Editable for custom actions. Select any Systems Manager document that is available to be used in this account.
- **View in Systems Manager** – Click to open **System Managers** and view additional information about the document.
- **Description** – Editable for custom actions. Add a description or keep the default.
- **Document version** – Editable for custom actions. Select which SSM document version to run. AWS DRS can run a default version, the latest version, or a specific version, according to your preferences.
- **Category** – Editable for custom actions. Select from various available categories including monitoring, validation, security and more.
- **Order** – Specify the order in which the
  actions run. The lower the number, the earlier the action runs. Values allowed are
  between 2 and 10,000. The numbers must be unique but don’t need to be
  consecutive.
- **Platform** – Not editable. Taken from the SSM document and reports which Operating System platform (Windows/Linux) is supported by the action.
- **Creator** – Not editable. Who created the action. For custom actions, the default is always **This account**.

The **Action parameters** change according to
the specific SSM document that is selected. Note that for the instance ID parameter, you
can choose to use the launch instance ID, in which case, AWS DRS dynamically populates
the value. Some predefined actions, where applicable allow to use a dynamically
populated value for the volumes. This value is dynamically populated by AWS DRS with the
volumes of the instance being launched.

After making the required changes, click **Save**, to save the changes and **Cancel** to abort them.
