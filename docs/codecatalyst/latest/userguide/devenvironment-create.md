Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Creating a Dev Environment

You can create a Dev Environment in multiple ways:

- Create a Dev Environment in CodeCatalyst with a CodeCatalyst source repository or a [linked source repository](source-repositories-link.md "source-repositories-link.md") from the
  **Overview**, **Dev Environments** or **Source
  repositories** pages
- Create an empty Dev Environment in CodeCatalyst that is not connected to a source repository
  from the Dev Environments page
- Create a Dev Environment in your IDE of choice and clone any source repository into the
  Dev Environment

###### Important

Dev Environments aren't available for users in spaces where Active Directory is used as
the identity provider. For more information, see [I can't create a Dev Environment
when I'm signed into CodeCatalyst using a single sign-on account](devenvironments-troubleshooting.md#troubleshoot-create-dev-env-idprovider "devenvironments-troubleshooting.md#troubleshoot-create-dev-env-idprovider").

You can create one Dev Environment per branch of a repository. A project can have multiple
repositories. The Dev Environments you create can only be managed with your CodeCatalyst account, but
you can open the Dev Environment and work in it with any of the supported IDEs. You must have the
AWS Toolkit installed to use Dev Environments in your IDE. For more information, see
[Supported integrated development environments
for Dev Environments](#devenvironment-supported-ide "#devenvironment-supported-ide").
By default, Dev Environments are created with a 2-core processor, 4 GB of RAM, and 16 GB of
persistent storage.

###### Note

If you created a Dev Environment that is associated with a source repository, the
**Resource** column always shows the branch you specified when creating
this Dev Environment. This applies even if you create another branch, switch to
another branch within the Dev Environment, or clone an additional repository. If you created an
empty Dev Environment, the **Resource** column will be blank.

## Supported integrated development environments

for Dev Environments

You can use Dev Environments with the following supported integrated development environments (IDEs):

- [AWS Cloud9](../../../cloud9/latest/user-guide/welcome.md "../../../cloud9/latest/user-guide/welcome.md")
- [JetBrains IDEs](https://www.jetbrains.com/help "https://www.jetbrains.com/help")
  - [IntelliJ
    IDEA Ultimate](https://www.jetbrains.com/help/idea/getting-started.html "https://www.jetbrains.com/help/idea/getting-started.html")
  - [GoLand](https://www.jetbrains.com/help/go/getting-started.html "https://www.jetbrains.com/help/go/getting-started.html")
  - [PyCharm
    Professional](https://www.jetbrains.com/help/pycharm/getting-started.html "https://www.jetbrains.com/help/pycharm/getting-started.html")

- [Visual Studio Code](https://code.visualstudio.com/docs "https://code.visualstudio.com/docs")

## Creating a Dev Environment in CodeCatalyst

To get started working with Dev Environment in CodeCatalyst, authenticate and sign in with
either your [AWS Builder ID](id-how-to-sign-in.md "id-how-to-sign-in.md") or [SSO](sign-in-sso.md "sign-in-sso.md").

###### To create a Dev Environment from a branch

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project where you want to create a Dev Environment.
3. In the navigation pane, do one of the following:
   - Choose **Overview**, and then navigate to the **My Dev Environments** section.
   - Choose **Code**, and then choose **Dev Environments**.
   - Choose **Code**, choose **Source repositories**, and choose the repository for which you want to create a Dev Environment.

4. Choose **Create Dev Environment**.
5. Choose a supported IDE from the drop-down menu. See [Supported integrated development environments
   for Dev Environments](#devenvironment-supported-ide "#devenvironment-supported-ide") for more information.
6. Choose **Clone a repository**.
7. Do one of the following:
   1. Choose the repository to clone, choose **Work in existing branch**, and then choose a branch from the
      **Existing branch** drop-down menu.

   ###### Note

   If you choose a third-party repository, you must work in an existing branch. 2. Choose the repository to clone, choose **Work in new branch**, enter a branch name into the **Branch
   name** field, and choose a branch off of which to create the new
   branch from the **Create branch from** drop-down menu.

   ###### Note

   If you create a Dev Environment from the **Source repositories** page or from a specific source repository, you do not need to choose a repository. The Dev Environment will be created from the source repository you chose from the **Source repositories** page.

8. (Optional) In **Alias - optional**, enter an alias for the Dev Environment.
9. (Optional) Choose the **Dev Environment configuration** edit button to edit the Dev Environment's compute, storage, or timeout configuration.
10. (Optional) In **Amazon Virtual Private Cloud (Amazon VPC) - optional**, select a VPC connection
    that you'd like to associate with your Dev Environment from the drop-down menu.

If a default VPC is set for your space, your Dev Environments will run connected to that VPC. You can override this by
associating a different VPC connection. Also, note that VPC-connected Dev Environments don’t support AWS Toolkit.

If the VPC connection that you want to use is not listed, it might be because it
includes an AWS account connection that's not allowed in your project. For more
information, see [Configuring project-restricted account connections](../adminguide/managing-accounts-restriction.md "../adminguide/managing-accounts-restriction.md") in the _Amazon CodeCatalyst Administrator Guide_.

###### Note

When you create a Dev Environment with a VPC connection, a new network interface is created inside the VPC. CodeCatalyst interacts with this interface using the associated VPC role. Also, make sure that your IPv4 CIDR block is **not** configured to the `172.16.0.0/12` IP address range. 11. Choose **Create**. While your Dev Environment is being created, the Dev Environment status column will display **Starting**, and the status column will display **Running** once the Dev Environment has been created.

###### To create an empty Dev Environment

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project where you want to create a Dev Environment.
3. In the navigation pane, do one of the following:
   - Choose **Overview**, and then navigate to the **My Dev Environments** section.
   - Choose **Code**, and then choose **Dev Environments**.

4. Choose **Create Dev Environment**.
5. Choose a supported IDE from the drop-down menu. See [Supported integrated development environments
   for Dev Environments](#devenvironment-supported-ide "#devenvironment-supported-ide") for more information.
6. Choose **Create an empty Dev Environment**.
7. (Optional) In **Alias - optional**, enter an alias for the Dev Environment.
8. (Optional) Choose the **Dev Environment configuration** edit button to edit the Dev Environment's compute, storage, or timeout configuration.
9. (Optional) In **Amazon Virtual Private Cloud (Amazon VPC) - optional**, select a VPC connection
   that you'd like to associate with your Dev Environment from the drop-down menu.

If a default VPC is set for your space, your Dev Environments will run connected to that VPC. You can override this by
associating a different VPC connection. Also, note that VPC-connected Dev Environments don’t support AWS Toolkit.

If the VPC connection that you want to use is not listed, it might be because it
includes an AWS account connection that's not allowed in your project. For more
information, see [Configuring project-restricted account connections](../adminguide/managing-accounts-restriction.md "../adminguide/managing-accounts-restriction.md") in the _Amazon CodeCatalyst Administrator Guide_.

###### Note

When you create a Dev Environment with a VPC connection, a new network interface is created inside the VPC. CodeCatalyst interacts with this interface using the associated VPC role. Also, make sure that your IPv4 CIDR block is **not** configured to the `172.16.0.0/12` IP address range. 10. Choose **Create**. While your Dev Environment is being created, the Dev Environment status column will display **Starting**, and the status column will display **Running** once the Dev Environment has been created.

###### Note

Creating and opening a Dev Environment for the first time might take one to two
minutes.

###### Note

After the Dev Environment opens in the IDE, you might need to change the directory to the
source repository before you commit and push changes to your code.

## Creating a Dev Environment in an IDE

You can use Dev Environments to quickly work on the code stored in the source repositories of
your project. Dev Environments increase your development velocity because you can start
coding immediately in a project-specific, fully functioning cloud development environment with
a supported integrated development environment (IDE).

For information about working with CodeCatalyst from an IDE, see the following documentation.

- [Amazon CodeCatalyst for JetBrains IDEs](../../../toolkit-for-jetbrains/latest/userguide/codecatalyst-service.md "../../../toolkit-for-jetbrains/latest/userguide/codecatalyst-service.md")
- [Amazon CodeCatalyst for VS Code](../../../toolkit-for-vscode/latest/userguide/codecatalyst-service.md "../../../toolkit-for-vscode/latest/userguide/codecatalyst-service.md")
- [Amazon CodeCatalyst for AWS Cloud9](../../../cloud9/latest/user-guide/ide-toolkits-cloud9.md "../../../cloud9/latest/user-guide/ide-toolkits-cloud9.md")
