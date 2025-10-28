NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Post-launch settings

Post-launch settings allow you to control and automate actions performed after the
server has been launched in AWS. These settings are created automatically based on the
**Post-launch template**.

To access the template, choose **Post-launch template**
on the left-hand menu.

The settings defined in the template are applied to every newly added server. You can
change the settings for existing and newly added servers individually within the server
details view.

###### Important

To use the post-launch settings feature, you must first activate at the account level. Deactivation is also at the account level.

The **Post-launch template** allows you to control
various post-launch actions, including:

- Deployment of test and cutover instances
- Disaster recovery configuration (installing the AWS Replication Agent for
  Elastic Disaster Recovery and configuring the target disaster recovery AWS Region).
- Operating system conversion on the target machine
- License and subscription changes on the target machine

###### Topics

- [Activating post-launch
  settings](#post-launch-settings-activation "#post-launch-settings-activation")
- [Editing the post-launch settings
  template](#post-launch-settings-editing "#post-launch-settings-editing")
- [Deploying post-launch
  actions](#deploying-post-launch-actions-2022 "#deploying-post-launch-actions-2022")
- [Encrypt post-launch action
  parameters](#encrypt-post-launch-actions-parameters "#encrypt-post-launch-actions-parameters")
- [Post-launch actions table](#post-launch-actions-table "#post-launch-actions-table")
- [Create a custom
  post-launch action](#post-launch-settings-custom-actions-add "#post-launch-settings-custom-actions-add")
- [Edit custom post-launch
  actions](#post-launch-settings-custom-actions-edit "#post-launch-settings-custom-actions-edit")
- [Predefined post-launch actions
  reference](predefined-post-launch-actions.md "predefined-post-launch-actions.md")

## Activating post-launch

settings

To use the post-launch template activate the post-launch actions. This allows
Application Migration Service to:

- Install the [SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") on your servers
- Run the post-launch actions

###### Note

- Installation of the SSM Agent requires a minimum of 200 MB of free disk space and 200 KB of free disk space in the `/var` directory.
- Installation of the SSM Agent is not supported on these operating systems:
  - CentOS 5.x
  - CentOS 6.x
  - RHEL 6.x
  - Oracle 6.x
  - Amazon Linux 1
  - Windows 2008
  - Windows 2008 R2

To activate the post-launch actions:

1. Navigate to **Settings > Post-launch settings
   template**.
2. Choose **Edit**.
3. Toggle the **Install Systems Manager agent and allow
   executing actions on launched servers** option.
4. Choose **Save template**.

The post-launch actions are shown in the \*\*Settings

> Post-launch template\*\* view.

## Editing the post-launch settings

template

Application Migration Service supports post-launch modernization actions, giving you the opportunity to
move and improve. The service provides actions that you can execute on your Amazon EC2 launch
instances and enables you to create your own actions.

The actions described in these sections can be edited within the
post-launch template. Once you have edited your settings, choose **Save template**.

## Deploying post-launch

actions

Use this setting to choose whether to execute the post-launch actions on your
cutover instances, on your test instances, or on both cutover and test instances.

## Encrypt post-launch action

parameters

The post-launch action parameters are stored in SSM [Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") . For enhanced security, ensure that users who do not
have permissions to execute SSM documents, do not have access to the Parameter
Store. For an additional layer of security you can select to encrypt the action
parameters using AWS KMS encryption.

SSM encrypts the parameter value of SecureString parameters type using AWS KMS
with an AWS managed key or with the default AWS KMS key provided by AWS. You can
specify different keys for each parameter, or use the same key for multiple
parameters.

## Post-launch actions table

The post-launch actions table includes both predefined actions and custom actions
that are executed on your new Amazon EC2 instances.

- Predefined post-launch actions are provided out of the box. They are
  prepopulated with the necessary values and only need to be activated or
  deactivated. These actions are based on public SSM documents that cannot
  be changed and have certain unchangeable parameters such as the platform
  name and order.
- Custom post-launch actions are based on SSM documents that you create
  and upload to your account.

Use the **Filter by** options on the left-hand side
to filter the available actions according to your preferences.

Click the settings icon in the right-hand corner of the screen to alternate
between card and list view, according to your preferences.

## Create a custom

post-launch action

AWS Application Migration Service allows you to execute any SSM document that you like – public SSM
document or ones you created and uploaded to your account.

You can configure a custom action to execute any SSM document that is available
in your account.

To add a new customer action, go to the **Post-launch actions
settings** and click **Create
action**.

The page includes these parameters:

- **Action name** – The name of the action in
  Application Migration Service, which should be intuitive and meaningful to your migration
  users.
- **Activate this action** – Use this checkbox
  to activate or deactivate the custom action.
- **This action must be completed successfully before
  finalizing cutover** – This checkbox dictates whether or not the
  script prevents the cutover.
- **System Manager document name** – Select any
  SSM document that is available for the specific account.
- **View in Systems Manager** – Click to open
  **SSM** and view additional information
  about the document.
- **Description** – Add a description or keep
  the default.
- **Document version** – Select which SSM
  document version to run. Application Migration Service can run a default version, the latest
  version, or a specific version, according to your preferences.
- Category – Select from various available categories including disaster
  recovery, security, validation, and more.
- **Order** – Specify the order in which the
  actions is executed. The lower the number, the earlier the action is executed.
  1–1,000 are reserved for predefined actions and 1,001–10,000 for custom actions.
  The numbers must be unique but don’t need to be consecutive.
- **Operating system** – Select the source
  server's operating systems for which the custom action can be configured for.
  Note that if you associate a script with the wrong operating system, it is
  skipped.
- **Creator** – Who created the action. For
  custom actions, the default is always **Me**.

The **Action parameters** change according to the
specific SSM document that is selected.

Note that for the instance ID parameter, you can choose to use the launch instance
ID, in which case, Application Migration Service dynamically populates the value.

###### Note

Only trusted, authorized users should have access to the parameter store. For
enhanced security, ensure that users who do not have permissions to execute
SSM documents / commands, do not have access to parameter store. [Learn more about restricting access to SSM parameters.](../../../systems-manager/latest/userguide/sysman-paramstore-access.md "../../../systems-manager/latest/userguide/sysman-paramstore-access.md") Action
parameters are stored in the SSM parameter store as regular strings. Changing
parameters in the SSM Parameter store may impact the post launch action
execution on target instances. We recommend you consider security implications,
when choosing to use parameters that contain scripts or sensitive information,
such as API keys and database passwords.

Edit each setting as required and then click **Add
action**.

## Edit custom post-launch

actions

AWS Application Migration Service allows you to execute any SSM document that you like – public SSM
document or ones you created and uploaded to your account.

You can configure a custom action to execute any SSM document that is available
in your account.

Use this page to edit the parameters detailed in the **Create
action** section.

Edit each setting as required and then click **Save
action**.
