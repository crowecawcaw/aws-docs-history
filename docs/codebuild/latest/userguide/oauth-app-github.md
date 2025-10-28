# GitHub OAuth app

## Connect GitHub using OAuth

(console)

To use the console to connect your project to GitHub using an OAuth app, do the
following when you create a project. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console").

1. For **Source provider**, choose
   **GitHub**.
2. For **Credential**, do one of the following:
   - Choose to use account credentials to apply your account's default source credential to all projects.
     1. If you aren't connected to GitHub, choose **Manage account credential**.
     2. For **Credential type**, choose **OAuth app**.

   - If you chose to use account level credentials for **Service**, choose which service you'd like to use to store your token and do the following:
     1. If you choose to use **Secrets Manager**, you can choose to use an existing secret connection or create a new secret, and then choose **Save**.
        For more information how to create a new secret, see [Create and store a token in a Secrets Manager secret](asm-create-secret.md "asm-create-secret.md").
     2. If you choose to use **CodeBuild** and then choose **Save**.

   - Select **Use override credentials for this project only** to use a custom source credential to override your account's credential settings.
     1. From the populated credential list, choose one of the options under **OAuth app**.
     2. You can also create new OAuth app token by selecting **create a new Oauth app token connection** in the description.

To review your authorized OAuth apps, navigate to [Applications](https://github.com/settings/applications "https://github.com/settings/applications") on GitHub,
and verify that an application named `AWS CodeBuild (`region`)` owned by
[aws-codesuite](https://github.com/aws-codesuite "https://github.com/aws-codesuite") is listed.
