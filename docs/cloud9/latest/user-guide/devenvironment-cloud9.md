AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Dev Environments in Amazon CodeCatalyst

The following sections outline how to create and manage your Dev Environment with CodeCatalyst using the AWS Cloud9 IDE.

- [Creating a Dev Environment](#ide-toolkits-create-cloud9 "#ide-toolkits-create-cloud9")
- [Opening Dev Environment settings](#ide-toolkits-settings-cloud9 "#ide-toolkits-settings-cloud9")
- [Resuming a Dev Environment](#ide-toolkits-resume-cloud9 "#ide-toolkits-resume-cloud9")
- [Deleting a Dev Environment](#ide-toolkits-delete-cloud9 "#ide-toolkits-delete-cloud9")
- [Editing the repository devfile for a
  Dev Environment](#ide-toolkits-edit-devfile-cloud9 "#ide-toolkits-edit-devfile-cloud9")
- [Cloning a repository](#ide-toolkits-clone-cloud9 "#ide-toolkits-clone-cloud9")
- [Troubleshooting a Dev Environment](#cloud9-devenvironment-troubleshoot "#cloud9-devenvironment-troubleshoot")

## Creating a Dev Environment

You can create a Dev Environment in multiple ways:

- Create a Dev Environment in CodeCatalyst with a CodeCatalyst source repository from the
  **Summary**, **Dev Environment**, or
  **Source repositories** pages.
- Create an empty Dev Environment that's not connected to a source repository in CodeCatalyst from
  Dev Environments.
- Create a Dev Environment in your IDE of choice and clone a CodeCatalyst source repository into the Dev Environment.

You can create one Dev Environment for each branch and repository. A project can have
multiple repositories. Your Dev Environments are only associated with your CodeCatalyst
account, and can only be managed by your CodeCatalyst account. You can open the
Dev Environment and work with it with any of the supported IDEs. After you choose a
specific IDE, you can only open that Dev Environment with the chosen IDE. If you
want to use a different IDE, you can either change the IDE by selecting the
Dev Environment in the navigation bar and choosing **Edit**, or by
creating a new Dev Environment. By default, Dev Environments are created with a 2-core
processor, 4 GB of RAM, and 16 GB of persistent storage.

For more information about how to create a Dev Environment in CodeCatalyst, see [Creating a
Dev Environment](../../../codecatalyst/latest/userguide/devenvironment-create.md "../../../codecatalyst/latest/userguide/devenvironment-create.md") in the _Amazon CodeCatalyst guide_.

For information and steps on creating a Dev Environment in CodeCatalyst, see [Creating a Dev Environment](../../../codecatalyst/latest/userguide/devenvironment-create.md "../../../codecatalyst/latest/userguide/devenvironment-create.md") in the _Amazon CodeCatalyst User Guide_.

###### Note

You can now create Dev Environments with third-party source repositories. For
information on linking a third-party source repository to a project within
CodeCatalyst, see [Linking a
source repository](../../../codecatalyst/latest/userguide/source-repositories-link.md "../../../codecatalyst/latest/userguide/source-repositories-link.md") in the _Amazon CodeCatalyst User
Guide_.

## Opening Dev Environment settings

After you create a Dev Environment in the CodeCatalyst console, you can view specific
Dev Environment settings:

1. In the CodeCatalyst console, navigate to your Dev Environment through the
   AWS Cloud9 IDE.
2. Choose **aws-explorer** from the
   AWS Cloud9 sidebar.
3. In the **Developer Tools** navigation pane, expand
   **CodeCatalyst** and choose **Open
   Settings** to open the **Dev Environment
   Settings** view.
4. From the **Dev Environment Settings** view, the following sections contain options for your Dev Environment:
   - **Alias:** View and change the **Alias** that's assigned to
     your Dev Environment.
   - **Status:** View your current Dev Environment status, the project that it's been
     assigned to, and stop your Dev Environment.
   - **Devfile:** View the name and location of the Devfile for
     your Dev Environment. Open your Devfile by the choosing
     **Open in Editor**.
   - **Compute Settings:** Change the size and default **Timeout Length** for your Dev Environment.

###### Note

You can't change the amount of storage space that's assigned to your Dev Environment after it's
created.

###### Note

When using Amazon CodeCatalyst AWS CLI from the terminal, you must ensure you set
_AWS_PROFILE=codecatalyst_ before running any CodeCatalyst commands.

## Resuming a Dev Environment

Everything in the `$HOME` directory of a Dev Environment is stored
persistently. You can stop working in a Dev Environment if necessary, and resume working
in your Dev Environment at a later time. Suppose that a Dev Environment is left idle for
more than the amount of time that was selected in the **Timeout**
fields when the Dev Environment was created. In this case, the session automatically
stops.

You can only resume a Dev Environment from CodeCatalyst. For more information about how to
resume a Dev Environment, see [Resuming a
Dev Environment](../../../codecatalyst/latest/userguide/devenvironment-resume.md "../../../codecatalyst/latest/userguide/devenvironment-resume.md") in the _Amazon CodeCatalyst guide_.

###### Note

Resuming a Dev Environment might take several minutes.

## Deleting a Dev Environment

When you finished working on the content that's stored in your Dev Environment, you can
delete that content. Before you delete a Dev Environment, make sure you commit and push
your code changes to the original source repository. After you delete your
Dev Environment, compute and storage billing for the Dev Environment ends.

You can only delete a Dev Environment from the **Dev Environments** page
in CodeCatalyst. For more information about how to delete a Dev Environment, see [Deleting a
Dev Environment](../../../codecatalyst/latest/userguide/devenvironment-delete.md "../../../codecatalyst/latest/userguide/devenvironment-delete.md") in the _Amazon CodeCatalyst guide_.

## Editing the repository

devfile for a Dev Environment

To change the configuration of a Dev Environment, edit the devfile. You can
usedevfiles to standardize your development Dev Environment across
your team. You can edit the devfile from the root of the source
repository in CodeCatalyst. Alternatively, you can edit the devfile in a
supported IDE. If you edit the devfile in a supported IDE, commit and
push your changes to the source repository or create a pull request. That way, a
team member can review and approve the devfile edits.

###### Note

You can only include public container images in your
devfile.

###### Note

If dependencies are missing, some AWS Cloud9 IDE features might not work in custom
devfile. It might require additional effort to make them work
on some platforms other than Linux x64.

###### To edit the repository

devfile for a Dev Environment in AWS Cloud9

1. In the CodeCatalyst console, navigate to your Dev Environment through the
   AWS Cloud9 IDE.
2. From the AWS Cloud9 sidebar, choose **aws-explorer** .
3. In the **Developer Tools** navigation pane, choose the
   **CodeCatalyst toolkit** menu.
4. Choose **Open Devfile**.
5. Edit the devfile, and save the file.
6. Choose **Source Control**, which is the Git
   extension from the menu side-bar.
7. In the **Message** text field, enter a message before staging
   changes.
8. To prepare for a commit, choose the **Stage All Changes (+)**
   icon.
9. To view Git commands, choose the **menu** icon
   that's next to the repository name.
10. Choose **Commit** and **Push**.
11. Choose **Update Dev Environment** from the
    AWS Toolkit menu.

Choose **Commit** and **Push**. The updated devfile has been saved and the changes have been committed and pushed.

###### Note

Say that the Dev Environment you want to launch using a custom devfile doesn't
work. This might be because the devfile isn't compatible with
AWS Cloud9. To troubleshoot, review the devfile. If the issue
persists, delete it and try creating a new one.

You can also edit the devfile for a Dev Environment through CodeCatalyst. For
more information, see [Configuring your
Dev Environment](../../../codecatalyst/latest/userguide/devenvironment-devfile.md "../../../codecatalyst/latest/userguide/devenvironment-devfile.md") in the _Amazon CodeCatalyst guide_.

## Cloning a repository

To work effectively with multiple files, branches, and commits in source repositories,
you can clone the source repository to your local computer. Then, use a
Git client or an IDE to make changes. From CodeCatalyst, you can use
the AWS Cloud9 IDE Gitextension in the same way as any other
Git host provider and also by using the command line. To learn
how to clone a third-party repository, see [Initialize or clone a
Git repository](using-gitpanel.md "using-gitpanel.md").

For more information about creating a Dev Environment from a source repository and cloning
it with CodeCatalyst, see [Source repository
concepts](../../../codecatalyst/latest/userguide/source-concepts-clone.md "../../../codecatalyst/latest/userguide/source-concepts-clone.md") in the _Amazon CodeCatalyst guide_.

## Troubleshooting a Dev Environment

If you encounter issues with your Dev Environment, see [Troubleshooting problems with Dev Environments](../../../codecatalyst/latest/userguide/troubleshooting-devenvironments.md "../../../codecatalyst/latest/userguide/troubleshooting-devenvironments.md") in the _Amazon CodeCatalyst
guide_.

###### Note

When using Amazon CodeCatalyst AWS CLI from the terminal, you must ensure you set
_AWS_PROFILE=codecatalyst_ before running any CodeCatalyst commands.

If you encounter issues with your Dev Environment, see [Troubleshooting problems with Dev Environments](../../../codecatalyst/latest/userguide/devenvironments-troubleshooting.md "../../../codecatalyst/latest/userguide/devenvironments-troubleshooting.md") in the _Amazon CodeCatalyst guide_.
