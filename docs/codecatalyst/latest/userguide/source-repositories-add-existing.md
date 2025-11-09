Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Cloning an existing Git repository

into a source repository

You can clone an existing Git repository to an empty source repository in Amazon CodeCatalyst.
This is a quick way to get started in CodeCatalyst with code that was previously hosted in
another Git repository provider. You can clone the contents of the repository by
creating a mirror clone and then pushing the mirror to CodeCatalyst. Alternatively, if you
have a local repo of the repository whose contents you want to add to CodeCatalyst, you can
add the CodeCatalyst source repository as another remote to the local repo, and then push to
the empty source repository. Both approaches are equally valid. Using a mirror clone not
only maps branches, it maps all refs. It's a simple and clean way to create a working
copy of the repository in CodeCatalyst. Adding a remote to a local repo that points to an
empty CodeCatalyst source repository will add the repository contents to CodeCatalyst, but it will
also allow you to make pushes from the local repo to both the CodeCatalyst source repository
and the original Git remote repository. This can be useful if you want to maintain the
code in different remote repositories, but can lead to conflicts if other developers are
committing code to only one of the remotes.

The following procedures use basic Git commands to accomplish this task. There are many ways to accomplish tasks in Git, including cloning.
For more information, see the [Git documentation.](https://git-scm.com/docs/git-clone "https://git-scm.com/docs/git-clone")

###### Important

You must create an empty repository in CodeCatalyst before you can clone content to it.
You must also have a personal access token. For more information, see [To create an empty source
repository](source-repositories-create.md#source-repositories-create-empty "source-repositories-create.md#source-repositories-create-empty") and [Create a personal access token](source-setting-up.md#source-setting-up-pat "source-setting-up.md#source-setting-up-pat").

###### To use `git clone --mirror` to clone an existing Git repository into CodeCatalyst

1. In the CodeCatalyst console, navigate to the project where you created an empty repository.
2. On the summary page for your project, choose the empty repository from the
   list, and then choose **View repository**. Alternatively, in
   the navigation pane, choose **Code**, and then choose
   **Source repositories**. Choose the name of the empty
   repository from the list of source repositories for the project.
3. Copy the HTTPS clone URL of the empty repository. You'll need this for pushing
   the mirror clone. For example, if you named the source repository
   MyExampleRepo in the MyExampleProject project in the
   ExampleCorp space, and your user name is LiJuan, your clone URL might
   look like the following:

```
https://`LiJuan`@git.us-west-2.codecatalyst.aws/v1/`ExampleCorp`/`MyExampleProject`/`MyExampleRepo`
```

4. At a command line or terminal window, use the `git clone --mirror`
   command to create a mirror clone of the Git repository you want to clone to
   CodeCatalyst. For example, if you want to create a mirror clone of the
   codecatalyst-blueprints repository in GitHub, you would enter the following
   command:

```
git clone --mirror `https://github.com/aws/codecatalyst-blueprints.git`
```

5. Change directories to the directory where you made the clone.

```
cd `codecatalyst-blueprints.git`
```

6. Run the **git push** command, specifying the URL and name of the destination
   CodeCatalyst source repository and the **--all** option. (This is the
   URL you copied in Step 3.) For example:

```
git push https://`LiJuan`@git.us-west-2.codecatalyst.aws/v1/`ExampleCorp`/`MyExampleProject`/`MyExampleRepo` --all
```

###### To add a remote and push a local repo into CodeCatalyst

1. In the CodeCatalyst console, navigate to the project where you created an empty repository.
2. On the summary page for your project, choose the empty repository from the
   list, and then choose **View repository**. Alternatively, in
   the navigation pane, choose **Code**, and then choose
   **Source repositories**. Choose the name of the empty
   repository from the list of source repositories for the project.
3. Copy the HTTPS clone URL of the empty repository. You'll need this for pushing
   the mirror clone. For example, if you named the source repository
   MyExampleRepo in the MyExampleProject project in the
   ExampleCorp space, and your user name is LiJuan, your clone URL might
   look like the following:

```
https://`LiJuan`@git.us-west-2.codecatalyst.aws/v1/`ExampleCorp`/`MyExampleProject`/`MyExampleRepo`
```

4. At a command line or terminal window, change directories to the local repo you
   want to push to CodeCatalyst.
5. Run the git remote -v command to see the existing remotes for the local
   repository. For example, if you are cloning a local repo of a AWS CodeCommit
   repository named `MyDemoRepo` in the US East (Ohio)
   Region, your command output might look like this:

```
origin  https://git-codecommit.`us-east-2`.amazonaws.com/v1/repos/`MyDemoRepo` (fetch)
origin  https://git-codecommit.`us-east-2`.amazonaws.com/v1/repos/`MyDemoRepo` (push)
```

Copy the remote URL if you want to continue using the repository. 6. Use the `git remote remove` command to remove the CodeCommit repository
URLs for fetch and push for origin:

```
git remote remove origin
```

7. Use the **git remote add** command to add the CodeCatalyst source
   repository URL as the fetch and push remote for your local repo. For
   example:

```
git remote add origin https://`LiJuan`@git.us-west-2.codecatalyst.aws/v1/`ExampleCorp`/`MyExampleProject`/`MyExampleRepo`
```

This replaces the CodeCommit repository push URL with CodeCatalyst source repository
URL, but does not change the fetch URL. So if you run the git remote -v command
again, you'll see that you're now pulling (fetch) code from the CodeCommit remote
repository, but you're configured to push changes from your local repo to the
CodeCatalyst source repository:

```
origin  https://git-codecommit.`us-east-2`.amazonaws.com/v1/repos/`MyDemoRepo` (fetch)
origin  https://LiJuan@git.us-west-2.codecatalyst.aws/v1/ExampleCorp/MyExampleProject/MyExampleRepo (push)
```

You can optionally add back the CodeCommit remote URL if you want to push to both
repositories with the `git remote set-url` command:

```
git remote set-url --add --push origin https://git-codecommit.`us-east-2`.amazonaws.com/v1/repos/`MyDemoRepo`
```

8. Run the `git push` command to push the local repo to all configured push remotes.
   Alternatively, run the **git push -u -origin** command,
   specifying the **--all** option to push the local repo to both
   repositories. For example:

```
git push -u -origin --all
```

###### Tip

Depending on your version of Git, --all might not work to push all branches of the local repo
to the empty repository. You might have to check out and push each branch
separately.
