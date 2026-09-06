

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Creating a source repository
<a name="source-repositories-create"></a>

When you create a project using a blueprint in Amazon CodeCatalyst, CodeCatalyst creates a source repository for you. That source repository contains sample code in addition to configuration information for the workflows and other resources created for you. This is the recommended way to get started with repositories in CodeCatalyst. You can choose to create repositories for a project. Those repositories will contain a **README.md** file that you can edit or delete at any time. Depending on your choices when you create a source repository, repositories might also contain a `.gitignore` file.

If you want to clone an existing Git repository into a CodeCatalyst source repository, consider creating an empty repository instead. This repository will be unavailable for use in CodeCatalyst until you add content to it, which you can do with a few simple Git commands. Alternatively, you can add content to the empty repository directly from the CodeCatalyst console. Alternatively, you can link a source repository in a supported Git repository provider. For more information, see [Linking a source repository](source-repositories-link.md).

**To create a source repository**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your project.

1. In the navigation pane, choose **Code**, and then choose **Source repositories**.

1. Choose **Add repository**, and then choose **Create repository**.

1. In **Repository name**, provide a name for the repository. In this guide, we use {{codecatalyst-source-repository}}, but you can choose a different name. Repository names must be unique within a project. For more information about requirements for repository names, see [Quotas for source repositories in CodeCatalyst](source-quotas.md).

1. (Optional) In **Description**, add a description for the repository that will help other users in the project understand what the repository is used for. 

1. Choose **Create repository (default)**. This option creates a repository that includes a default branch and a README.md file. Unlike an empty repository, you can use this repository as soon as it's created.

1. In **Default branch**, leave the name as *main* unless you have a reason to choose a different name. The examples in this guide all use the name *main* for the default branch.

1. (Optional) Add a `.gitignore` file for the type of code you plan to push. 

1. Choose **Create**.
**Note**  
CodeCatalyst adds a `README.md` file to your repository when you create it. CodeCatalyst also creates an initial commit for the repository in a default branch named **main**. You can edit or delete the README.md file, but you can't  delete the default branch.<a name="source-repositories-create-empty"></a>

**To create an empty source repository**

1. In the CodeCatalyst console, navigate to the project where you want to create an empty repository.

1. On the summary page for your project, in **Source repositories**, choose **Add repository**, and then choose **Create repository**. Alternatively, in the navigation pane, choose **Code**, and then choose **Source repositories**. Choose **Add repository**, and then choose **Create repository**. 

1. In **Repository name**, provide a name for the repository. In this guide, we use {{codecatalyst-source-repository}}, but you can choose a different name. Repository names must be unique within a project. For more information about requirements for repository names, see [Quotas for source repositories in CodeCatalyst](source-quotas.md).

1. (Optional) In **Description**, add a description for the repository that will help other users in the project understand what the repository is used for. 

1. Choose **Create empty repository**, and then choose **Create**.