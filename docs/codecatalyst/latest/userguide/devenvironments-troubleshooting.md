Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Troubleshooting problems with Dev Environments

Consult the following sections to troubleshoot problems related to Dev Environments. For more
information about Dev Environments, see [Write and modify code with Dev Environments in CodeCatalyst](devenvironment.md "devenvironment.md").

###### Topics

- [My Dev Environment creation didn't succeed due to a problem with quotas](#troubleshooting-devenvironments-create "#troubleshooting-devenvironments-create")
- [I can't push changes from my Dev Environment to a specific branch in a repository](#troubleshooting-devenvironments-branchrules "#troubleshooting-devenvironments-branchrules")
- [My Dev Environment didn't
  resume](#troubleshooting-devenvironments-resume "#troubleshooting-devenvironments-resume")
- [My Dev Environment
  disconnected](#troubleshooting-devenvironments-connection "#troubleshooting-devenvironments-connection")
- [My VPC-connected Dev Environment failed](#troubleshooting-devenvironments-vpc "#troubleshooting-devenvironments-vpc")
- [I can't find which directory my project is in](#troubleshooting-devenvironments-projects "#troubleshooting-devenvironments-projects")
- [I'm unable to connect to my Dev Environment via SSH](#troubleshooting-devenvironments-connect-ssh "#troubleshooting-devenvironments-connect-ssh")
- [I'm unable to connect to my Dev Environment via SSH because my local SSH config is missing](#troubleshooting-devenvironments-projects-ssh-config "#troubleshooting-devenvironments-projects-ssh-config")
- [I'm unable to connect to my Dev Environment via SSH because I'm having problems with my AWS Config for
  the codecatalyst profile](#troubleshooting-devenvironments-config-profile "#troubleshooting-devenvironments-config-profile")
- [I can't create a Dev Environment
  when I'm signed into CodeCatalyst using a single sign-on account](#troubleshoot-create-dev-env-idprovider "#troubleshoot-create-dev-env-idprovider")
- [Troubleshooting problems with IDEs](devenvironments-troubleshooting-ides.md "devenvironments-troubleshooting-ides.md")
- [Troubleshooting problems with devfiles](devenvironments-devenvironments-devfile.md "devenvironments-devenvironments-devfile.md")

## My Dev Environment creation didn't succeed due to a problem with quotas

**Problem:** I want to create a Dev Environment in CodeCatalyst, but I see an error.
In the console, I see a message on the Dev Environments page that I have reached the storage limit for the space.

**Possible fixes:** Depending on your role in the project or space,
you can either delete one or more of your own Dev Environments, or if you have the Space administrator role, you can delete unused Dev Environments created
by other users. You can also decide to change the billing tier to one that includes more storage.

- To view the storage limits, view the **Billing** tab of the Amazon CodeCatalyst
  space to see if the **Usage** quotas have reached the
  maximum allowed. If the quotas have reached the maximum, contact someone with
  the Space administrator role to remove unneeded Dev Environments or to consider
  changing the billing tier.
- To remove any Dev Environments you created that you no longer need, see
  [Deleting a Dev Environment](devenvironment-delete.md "devenvironment-delete.md").

If the issue continues and you get an error in your IDE, check that you have a CodeCatalyst role that allows you to create a Dev Environment. The **Space administrator** role, **Project administrator** role,
and **Contributor** role all have permission to create Dev Environments. For more information, see [Granting access with user roles](ipa-roles.md "ipa-roles.md").

## I can't push changes from my Dev Environment to a specific branch in a repository

**Problem:** I want to commit and push code changes in my Dev Environment to a branch in a source repository,
but I see an error.

**Possible fixes:** Depending on your role in the project or space,
you might not have permissions to push code to source repositories in the project. The **Space administrator** role,
**Project administrator** role, and **Contributor** role all have permission to push code
to repositories in the project.

If you have the **Contributor** role but cannot push code to a specific branch, there might be a branch rule
configured for the specific branch that prevents users with that role from pushing code to that particular branch. Try pushing your changes to a different
branch, or create a branch and then push your code to that branch. For more information, see
[Manage allowed actions for a branch with
branch rules](source-branches-branch-rules.md "source-branches-branch-rules.md").

## My Dev Environment didn't

resume

**Problem:** My Dev Environment didn't
resume after I stopped it.

**Possible fixes:** To fix the problem, view the **Billing** tab of the Amazon CodeCatalyst space to see if the **Usage** quotas have reached the maximum limits. If the quotas have reached the maximum limit, contact your Space administrator to raise the billing tier.

## My Dev Environment

disconnected

**Problem:** My Dev Environment disconnected while I was using it.

**Possible fixes:** To fix the problem, check your internet connection.
If you are not connected to the internet, connect and resume working in your Dev Environment.

## My VPC-connected Dev Environment failed

**Problem:** I associated a VPC connection to my Dev Environment and it's running into errors.

**Possible fixes:** Docker uses a link layer device called a
bridge network that enables containers that are connected to the same bridge network to
communicate. The default bridge typically uses the `172.17.0.0/16` subnet
for container networking. If the VPC subnet for your environment's instance uses the same address range that's
already used by Docker, an IP address conflict might occur. To resolve an IP address
conflict that's caused by Amazon VPC and Docker using the same IPv4 CIDR
address block, configure a CIDR block that's different from `172.17.0.0/16`.

###### Note

You can't change the IP address range of an existing VPC or subnet.

## I can't find which directory my project is in

**Problem:** I can't find which directory my project is in.

**Possible fixes:** To locate your project, change directory to `/projects`. This is the directory where you can find your
projects.

## I'm unable to connect to my Dev Environment via SSH

To troubleshoot your connection to your Dev Environment via SSH, you can execute the `ssh` command with `-vvv` option to show more information on how to resolve your issue:

```
ssh -vvv codecatalyst-dev-env=`<space-name>`=`<project-name>`=`<dev-environment-id>`
```

## I'm unable to connect to my Dev Environment via SSH because my local SSH config is missing

If your local SSH config (`~/.ssh/config`) is missing or the contents of `Host codecatalyst-dev-env*` section is out of date, you won’t be able to connect to your Dev Environment via SSH.
To troubleshoot this, delete the `Host codecatalyst-dev-env*` section and execute the first command from the **SSH Access** modal again.
For more information, see [Connecting to a Dev Environment using SSH](devenvironment-connect-ssh.md "devenvironment-connect-ssh.md").

## I'm unable to connect to my Dev Environment via SSH because I'm having problems with my AWS Config for

the `codecatalyst` profile

Make sure your AWS Config (`~/.aws/config`) for the `codecatalyst` profile matches the one described in [Setting up to use the AWS CLI with CodeCatalyst](set-up-cli.md "set-up-cli.md").
If not, delete the profile for `codecatalyst` and execute the first command from the **SSH Access** modal again.
For more information, see [Connecting to a Dev Environment using SSH](devenvironment-connect-ssh.md "devenvironment-connect-ssh.md").

## I can't create a Dev Environment

when I'm signed into CodeCatalyst using a single sign-on account

**Problem:** When I am signed into the CodeCatalyst console as
an SSO user, I receive an unknown exception error when I choose to create a Dev Environment
in the space. When I choose to create a Dev Environment and choose the IDE for access,
such as AWS Cloud9, I experience issues similar to the following:

- The **Dev Environments** page in the CodeCatalyst console shows the
  Dev Environment in the list with a `FAILED` state.
- An error message similar to the following displays:

**`An unknown exception
 happened`**

`We encountered an unknown exception when launching your Dev Environment.
 Mention your Dev Environment id `error_message_ID` if
 you want to report or need any help.`

**Possible fixes:**

Dev Environments aren't available for users in spaces where Active Directory is used
as the identity provider. Administrators for the space can use an alternative
identity provider in order to access Dev Environments, such as IAM Identity Center. For more information
about planning a space that supports identity federation, see [Planning
your space that supports identity federation](../adminguide/setting-up-federation.md#setting-up-planning-federation "../adminguide/setting-up-federation.md#setting-up-planning-federation") in the _CodeCatalyst Administrator Guide_.
