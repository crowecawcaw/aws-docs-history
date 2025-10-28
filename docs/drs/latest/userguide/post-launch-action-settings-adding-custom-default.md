# Adding custom actions

AWS Elastic Disaster Recovery (AWS DRS) allows you to run any SSM document that you like – public SSM documents or ones you created and uploaded to your account.
You can configure a custom action to run any SSM document that is available in your account.
To be able to create, edit or delete a default custom action, make sure the post-launch actions are activated in the default settings.

## Create a custom action

Adding a custom action through the default settings adds it to newly added
servers. To add a custom action to an existing source server use the **Post-launch settings** tab in the source server details
page. To add a new custom action to the default post-launch action settings, go
to **Settings → Default post-launch actions**. If
the default post-launch actions settings is **Active**, you can create new custom actions by selecting **Add action**.

The **Add action** page includes these parameters:

**Action name** – The name of the action in AWS DRS, which should be intuitive, meaningful and unique in this AWS account and region.

**Activate this action** – Use this checkbox to
activate or deactivate the action by default. Newly added source servers have
the action set to active or not active according to the value this field had
when the source server was added.

**Mark launch as successful only if this action finishes
running successfully** – This checkbox dictates whether or not the
launch is marked as successful, based on the successful run of this action.
Instance launches still progress normally regardless of the success of the
action.

**System Manager document name** – Select any Systems Manager document that is available to be used in this account.

**System Manager document name** – Select any Systems Manager document that is available to be used in this account.

**View in Systems Manager** – select to open
**System Managers** and view additional
information about the document.

**Description** – Add a description or keep the default.

**Document version** – Select which SSM document version to run. AWS DRS can run a default version, the latest version, or a specific version, according to your preferences.

**Category** – Select from various available categories including monitoring, validation, security and more.

**Order** – Specify the order in which the
actions are executed. The lower the number, the earlier the action is executed.
Values allowed are between 2 and 10,000. The numbers must be unique but don’t
need to be consecutive.

**Platform** – Taken from the SSM document and reports which Operating System platform (Windows/Linux) is supported by the action.

**Creator** – Who created the action. For custom actions, the default is always **This account**.

The **Action parameters** change according to
the specific SSM document that is selected. Note that for the instance ID
parameter, you can choose to use the launch instance ID, in which case, AWS DRS
dynamically populates the value.

###### Note

AWS Elastic Disaster Recovery (AWS DRS) places **AWSElasticDisasterRecoveryRecoveryInstanceWithLaunchActionsRole** instance profile on the launch instance if post-launch actions is active for the source server.
If you add an SSM command action that requires additional permissions in the launch instance,
you must ensure that the instance profile has the right policies or the right permissions.
In order to do so, create a role that has the required permissions as per the policies above or has a policy or policies with those permissions attached to it.
Go to **Launch settings** > **EC2 launch template** > **Modify** > **Advance** > **IAM instance profile**.
Use an existing profile or create a new one using the **Create new IAM profile** link.

###### Note

Only trusted, authorized users should have access to the parameter store. For enhanced security, ensure that users who do not have permissions to execute SSM documents / commands,
do not have access to parameter store. [Learn more about restricting access to Systems Manager parameters](../../../systems-manager/latest/userguide/sysman-paramstore-access.md "../../../systems-manager/latest/userguide/sysman-paramstore-access.md"). Action parameters are stored in the SSM parameter store as regular strings.
Changing parameters in the SSM Parameter store may impact the post launch action run on target instances. We recommend to consider security implications, when choosing to use parameters that
contain scripts or sensitive information, such as API keys and database passwords.
