

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Installing an extension in a space
<a name="install-extension"></a>

You can install extensions for your CodeCatalyst space that add functionality to projects in that space. You can view the CodeCatalyst catalog by choosing the **Catalog** icon ![The CodeCatalyst catalog icon in the top navigation bar in CodeCatalyst.](http://docs.aws.amazon.com/codecatalyst/latest/userguide/images/integrations/marketplace-icon.png). To learn more about the extensions and their functionalities, see [Available third-party extensions](extensions.md#extensions-types). 

**Important**  
To install an extension, you must be signed in with an account that has the **Space administrator** role in the space.

**Important**  
After you install a repository extension, any repositories you link to CodeCatalyst will have their code indexed and stored in CodeCatalyst. This will make the code searchable in CodeCatalyst. To better understand the data protection for your code when using linked repositories in CodeCatalyst, see [Data protection](https://docs.aws.amazon.com/codecatalyst/latest/userguide/data-protection.html) in the *Amazon CodeCatalyst User Guide*.

**To install an extension from the CodeCatalyst catalog**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your CodeCatalyst space.

1. Navigate to the CodeCatalyst catalog by choosing the **Catalog** icon ![The CodeCatalyst catalog icon in the top navigation bar in CodeCatalyst.](http://docs.aws.amazon.com/codecatalyst/latest/userguide/images/integrations/marketplace-icon.png) in the top menu. You can search for **GitHub repositories**, **Bitbucket repositories**, **GitLab repositories**, or **Jira Software**. You can also filter extensions based on categories.

1. (Optional) Choose the name of the extension to see more details about the extension, such as the permissions the extension will have.

1. Choose **Install**. Review the permissions required by the extension, and if you want to continue, choose **Install** again.

After installing an extension, you will see the details page for the installed extension. Browse the tabs for more information about the extension. The details page is also where you will perform further configuration of the extension if needed.