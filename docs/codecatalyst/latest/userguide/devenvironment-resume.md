Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Resuming a Dev Environment

The `/projects` directory of a Dev Environment stores the files that are pulled
from the source repository and the devfile that is used to configure the Dev Environment. The
`/home` directory, which is empty upon Dev Environment creation, stores the files you
create while using your Dev Environment. Everything in the `/projects` and
`/home` directories of a Dev Environment is stored persistently, so you can stop
working in a Dev Environment if you need to switch to another Dev Environment, repository, or project
and resume working in your Dev Environment at a later time.

A Dev Environment will automatically stop if it is idle for the amount of time that was
selected in the **Timeout** fields during Dev Environment creation. You must
close the AWS Cloud9 browser tab for the Dev Environment to be idle.

###### Note

The Dev Environment is still available and running even if you delete the branch with which
you created the Dev Environment. If you want to resume working in a Dev Environment for which you
deleted the branch, create a new branch and push your changes to it.

###### To resume a Dev Environment from the overview

page

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project where you want to resume a Dev Environment, and navigate to the
   **My Dev Environments** section.
3. Choose **Resume in (IDE)**.
   - For JetBrains IDEs, choose JetBrains Gateway-EAP when prompted to **Choose an
     application to open the JetBrains-gateway link**. Choose **Open
     Link** to confirm when prompted.
   - For the VS Code IDE, choose VS Code when prompted to **Choose an
     application to open the VS Code link**. Choose **Open
     Link** to confirm.

###### To resume a Dev Environment from the source

repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project where you want to resume a Dev Environment.
3. In the navigation pane, choose **Code**.
4. Choose **Source Repositories**.
5. Choose the source repository that contains the Dev Environment you want to resume.
6. Choose the branch name to view a drop-down menu of your branches, then choose your
   branch.
7. Choose **Resume Dev Environment**.
   - For JetBrains IDEs, choose **Open Link** to confirm when prompted
     to **Allow this site to open the JetBrains-gateway link with JetBrains
     Gateway?**.
   - For the VS Code IDE, choose **Open Link** to confirm when
     prompted to **Allow this site to open the VS Code link with Visual Studio
     Code?**.

###### To resume a Dev Environment from the

Dev Environments page

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the project where you want to resume a Dev Environment.
3. In the navigation pane, choose **Code**.
4. Choose **Dev Environments**.
5. From the **IDE** column, choose **Resume in (IDE)**
   for the Dev Environment.
   - For JetBrains IDEs, choose **Open Link** to confirm when prompted
     to **Allow this site to open the JetBrains-gateway link with JetBrains
     Gateway?**.
   - For the VS Code IDE, choose **Open Link** to confirm when
     prompted to **Allow this site to open the VS Code link with Visual Studio
     Code?**.

###### Note

Resuming a Dev Environment may take a few minutes.
