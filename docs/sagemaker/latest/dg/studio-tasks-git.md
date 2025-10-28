# Clone a Git Repository in Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

Amazon SageMaker Studio Classic can only connect only to a local Git repository (repo). This means
that you must clone the Git repo from within Studio Classic to access the files in the repo.
Studio Classic offers a Git extension for you to enter the URL of a Git repo, clone it into your
environment, push changes, and view commit history. If the repo is private and requires
credentials to access, then you are prompted to enter your user credentials. This includes
your username and personal access token. For more information about personal access tokens,
see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens").

Admins can also attach suggested Git repository URLs at the Amazon SageMaker AI domain or user
profile level. Users can then select the repo URL from the list of suggestions and clone that
into Studio Classic. For more information about attaching suggested repos, see [Attach Suggested Git Repos to Amazon SageMaker Studio Classic](studio-git-attach.md "studio-git-attach.md").

The following procedure shows how to clone a GitHub repo from Studio Classic.

###### To clone the repo

1. In the left sidebar, choose the **Git** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/git.png)
   ).
2. Choose **Clone a Repository**. This opens a new window.
3. In the **Clone Git Repository** window, enter the URL in the
   following format for the Git repo that you want to clone or select a repository from the
   list of **Suggested repositories**.

```
https://github.com/`path-to-git-repo`/`repo`.git
```

4. If you entered the URL of the Git repo manually, select **Clone
   "`git-url`"** from the dropdown menu.
5. Under **Project directory to clone into**, enter the path to the
   local directory that you want to clone the Git repo into. If this value is left empty,
   Studio Classic clones the repo into JupyterLab's root directory.
6. Choose **Clone**. This opens a new terminal window.
7. If the repo requires credentials, you are prompted to enter your username and personal
   access token. This prompt does not accept passwords, you must use a personal access token.
   For more information about personal access tokens, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens "https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens").
8. Wait for the download to finish. After the repo has been cloned, the **File
   Browser** opens to display the cloned repo.
9. Double click the repo to open it.
10. Choose the **Git** icon to view the Git user interface which now
    tracks the repo.
11. To track a different repo, open the repo in the file browser and then choose the
    **Git** icon.
