# Learn Quick Setup terminology and details

Quick Setup, a tool in AWS Systems Manager, displays the results of all configuration managers
you've created across all AWS Regions in the **Configuration
managers** table on the Quick Setup home page. From this page, you can
**View details** of each configuration, delete configurations from
the **Actions** drop down, or **Create**
configurations. The **Configuration managers** table contains the
following information:

- **Name** – The name of the configuration manager if
  provided when created.
- **Configuration type** – The configuration type chosen
  when creating the configuration.
- **Version** – The version of the configuration type
  currently deployed.
- **Organizational units** – Displays the organizational
  units (OUs) that the configuration is deployed to if you chose a
  **Custom** set of targets. Organizational units and custom
  targets are only available to the management account of your organization. The
  management account is the account that you use to create an organization in
  AWS Organizations.
- **Deployment type** – Indicates whether the deployment
  applies to the entire organization (`Organizational`) or only your
  account (`Local`).
- **Regions** – The Regions that the configuration is
  deployed to if you chose a **Custom** set of targets or targets
  within your **Current account**.
- **Deployment status** – The deployment status
  indicates if AWS CloudFormation successfully deployed the target or stack instance. The
  target and stack instances contain the configuration options that you chose
  during configuration creation.
- **Association status** – The association status is the
  state of all associations created by the configuration that you created. The
  associations for all targets must run successfully; otherwise, the status is
  **Failed**.

Quick Setup creates and runs a State Manager association for each configuration
target. State Manager is a tool in AWS Systems Manager.
To view configurations deployed to the Region you're currently browsing, select the
**Configurations** tab.

## Configuration details

The **Configuration details** page displays information about the
deployment of the configuration and its related associations. From this page, you
can edit configuration options, update targets, or delete the configuration. You can
also view the details of each configuration deployment to get more information about
the associations.

Depending on the type of configuration, one or more of the following status graphs
are displayed:

**Configuration deployment status**

Displays the number of deployments that have succeeded, failed, or are
running or pending. Deployments occur in the specified target accounts
and Regions that contain nodes affected by the configuration.

**Configuration association status**

Displays the number of State Manager associations that have succeeded,
failed, or are pending. Quick Setup creates an association in each
deployment for the configuration options selected.

**Setup status**

Displays the number of actions performed by the configuration type and
their current statuses.

**Resource compliance**

Displays the number of resources that are compliant to the
configurations specified policy.

The **Configuration details** table displays information about
the deployment of your configuration. You can view more details about each
deployment by selecting the deployment and then choosing **View
details**. The details page of each deployment displays the
associations deployed to the nodes in that deployment.

## Editing and deleting your

configuration

You can edit configuration options of a configuration from the
**Configuration details** page by choosing
**Actions** and then **Edit configuration
options**. When you add new options to the configuration, Quick Setup runs
your deployments and creates new associations. When you remove options from a
configuration, Quick Setup runs your deployments and removes any related
associations.

###### Note

You can edit Quick Setup configurations for your account at anytime. To edit an
**Organization** configuration, the **Configuration
status** must be **Success** or
**Failed**.

You can also update the targets included in your configurations by choosing
**Actions** and **Add OUs**, **Add
Regions**, **Remove OUs**, or **Remove
Regions**. If your account isn't configured as the management account or
you created the configuration for only the current account, you can't update the
target organizational units (OUs). Removing a Region or OU removes the associations
from those Regions or OUs.

Periodically, Quick Setup releases new versions of configurations. You can select the
**Upgrade configuration** option to upgrade your configuration
to the latest version.

You can delete a configuration from Quick Setup by choosing the configuration, then
**Actions**, and then **Delete
configuration**. Or, you can delete the configuration from the
**Configuration details** page under the
**Actions** dropdown and then **Delete
configuration**. Quick Setup then prompts you to **Remove all OUs
and Regions** which might take some time to complete. Deleting a
configuration also deletes all related associations. This two-step deletion process
removes all deployed resources from all accounts and Regions and then deletes the
configuration.

## Configuration compliance

You can view whether your instances are compliant with the associations created by
your configurations in either Explorer or Compliance, which are both tools in
AWS Systems Manager. To learn more about compliance, see [Learn details about Compliance](compliance-about.md "compliance-about.md"). To learn more about viewing compliance in
Explorer, see [AWS Systems Manager Explorer](Explorer.md "Explorer.md").
