Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Tutorial: Creating and updating a React application

As a blueprint author, you can develop and add custom blueprints to your space's blueprints catalog. These blueprints can
then be used by space members to create new projects or add them to existing projects. You can continue to make changes to your blueprints
that are then made available as updates through pull requests.

This tutorial provides a walkthrough from a blueprint author's perspective and a blueprint user's perspective. The tutorial
shows how to create a React single-page web application blueprint. The blueprint is then used to create a new project. When the blueprint
is updated with changes, the project created from the blueprint incorporates those changes through a pull request.

###### Topics

- [Prerequisites](#blueprint-getting-started-prerequisites "#blueprint-getting-started-prerequisites")
- [Step 1: Create a custom blueprint](#react-bluprint-tutorial-create-bp "#react-bluprint-tutorial-create-bp")
- [Step 2: View release workflow](#blueprint-getting-started-view-workflow "#blueprint-getting-started-view-workflow")
- [Step 3: Add blueprint to catalog](#blueprint-getting-started-add-to-catalog "#blueprint-getting-started-add-to-catalog")
- [Step 4: Create project with blueprint](#blueprint-getting-started-create-project "#blueprint-getting-started-create-project")
- [Step 5: Update blueprint](#blueprint-getting-started-update-blueprint "#blueprint-getting-started-update-blueprint")
- [Step 6: Update the blueprint's published catalog version to the new version](#blueprint-getting-started-update-catalog-version "#blueprint-getting-started-update-catalog-version")
- [Step 7: Update project with new blueprint version](#blueprint-getting-started-update-project "#blueprint-getting-started-update-project")
- [Step 8: View the changes in the project](#blueprint-getting-started-view-changes "#blueprint-getting-started-view-changes")

## Prerequisites

To create and update a custom blueprint, you must have completed the tasks
in [Set up and sign in to CodeCatalyst](setting-up-topnode.md "setting-up-topnode.md") as follows:

- Have an AWS Builder ID for signing in to CodeCatalyst.
- Belong to a space and have the **Space administrator** or
  **Power user** role assigned to you in that space. For more
  information, see [Creating a space](spaces-create.md "spaces-create.md"), [Granting users space permissions](spaces-members.md "spaces-members.md"), and [Space administrator role](ipa-role-types.md#ipa-role-space-admin "ipa-role-types.md#ipa-role-space-admin").

## Step 1: Create a custom blueprint

When you create a custom blueprint, a CodeCatalyst project is created that contains your blueprint source code and development
tools and resources. Your project is where you will develop, test, and publish the blueprint.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the CodeCatalyst console, navigate to the space where you want to create a blueprint.
3. Choose **Settings** to navigate to the space settings.
4. In the **Space settings** tab, choose **Blueprints**
   and choose **Create blueprint**.
5. Update the fields in the blueprint creation wizard with the following values:
   - In **Blueprint name**, enter `react-app-blueprint`.
   - In **Blueprint Display Name**, enter `react-app-blueprint`.

6. Optionally, choose **View code** to preview the blueprint source code for your blueprint.
   Likewise, choose **View workflow** to preview the workflow that will be created in the
   project that builds and publishes the blueprint.
7. Choose **Create blueprint**.
8. Once your blueprint is created, you are taken to the blueprint's project. This project contains the blueprint source code, along with
   the tools and resources you need to develop, test, and publish the blueprint. A release workflow was generated and it automatically published
   your blueprint to the space.
9. Now that your blueprint and blueprint project is created, the next step is to configure it by updating the source code.
   You can use Dev Environments to open and edit your source repository directly in your browser.

In the navigation pane, choose **Code**, and then choose **Dev Environments**. 10. Choose **Create Dev Environment** and then choose **AWS Cloud9 (in browser)**. 11. Keep the default settings and choose **Create**. 12. In the AWS Cloud9 terminal, navigate to your blueprint project directory by running the following command:

```
cd react-app-blueprint
```

13. A `static-assets` folder is created and filled automatically when a blueprint is created. In this tutorial, you will
    delete the default folder and generate a new one for a react app blueprint.

Delete the static-assets folder by running the following command:

```
rm -r static-assets
```

AWS Cloud9 is built on a Linux-based platform. If you're using a Windows operating system, you can use the following command instead:

```
rmdir /s /q static-assets
```

14. Now that the default folder is deleted, create a `static-assets`
    folder for a react-app blueprint by running the following command:

```
npx create-react-app static-assets
```

If prompted, enter `y` to proceed.

A new react application was created in the `static-assets` folder with necessary packages. The changes need to pushed
to your remote CodeCatalyst source repository. 15. Ensure you have the latest changes, and then commit and push the changes to the blueprint's CodeCatalyst source repository by running the following commands:

```
git pull
```

```
git add .
```

```
git commit -m "Add React app to static-assets"
```

```
git push
```

When a change is pushed to the blueprint's source repository, the release workflow is automatically started. This workflow
increments the blueprint version, builds the blueprint, and publishes it to your space. In the next step, you'll navigate
to the release workflow run to see how it's doing.

## Step 2: View release workflow

1. In the CodeCatalyst console, in the navigation pane, choose **CI/CD**, and then choose **Workflows**.
2. Choose the **blueprint-release** workflow.
3. You can see the workflow has actions to build and publish the blueprint.
4. Under **Latest run**, choose the workflow run link to view the run from the code change you made.
5. Once the run is completed, your new blueprint version is published. Published blueprint
   versions can be seen in your space **Settings**, but can't be used in projects until it's added to the space's blueprints
   catalog. In the next step, you'll add the blueprint to the catalog.

## Step 3: Add blueprint to catalog

Adding a blueprint to the space's blueprints catalog makes the blueprint available for use in all projects in a space. Space members
can use the blueprint to create new projects or add them to existing projects.

1. In the CodeCatalyst console, navigate back to the space.
2. Choose **Settings**, and then choose **Blueprints**.
3. Choose **react-app-blueprint**, and then choose **Add to catalog**.
4. Choose **Save**.

## Step 4: Create project with blueprint

Now that the blueprint is added to the catalog, it can be used in projects. In this step, you'll create a project
with the blueprint you just created. In a later step, you'll update this project by updating and publishing a
new version of the blueprint.

1. Choose the **Projects** tab and then choose **Create project**.
2. Choose **Space blueprints**, and then choose **react-app-blueprint**.

###### Note

Once the blueprint is chosen, you can see the contents of the blueprint's `README.md` file. 3. Choose **Next**. 4. ###### Note

The contents of this project creation wizard can be configured in the blueprint.

Enter the project name as a blueprint user. For this tutorial, enter `react-app-project`. For more information,
see [Developing a custom blueprint to meet project requirements](develop-bp.md "develop-bp.md").

Next, you'll make an update to the blueprint and add the new version to the catalog,
which you will use to update this project.

## Step 5: Update blueprint

After a blueprint is used to create a new project or applied to existing projects, you can continue to make updates as a blueprint author. In
this step, you'll make changes to the blueprint and automatically publish a new version to the space. The new version can then be added as the catalog
version.

1. Navigate to the **react-app-blueprint** project created in [Tutorial: Creating and updating a React application](blueprint-getting-started-tutorial.md "blueprint-getting-started-tutorial.md").
2. Open the Dev Environment created in [Tutorial: Creating and updating a React application](blueprint-getting-started-tutorial.md "blueprint-getting-started-tutorial.md").
   1. In the navigation pane, choose **Code**, and then choose **Dev Environments**.
   2. From the table, find the Dev Environment, and then choose **Open in AWS Cloud9 (in browser)**.

3. When the blueprint release workflow was run, it incremented the blueprint version by updating the `package.json` file.
   Pull that change in by running the following command in the AWS Cloud9 terminal:

```
git pull
```

4. Navigate to the `static-assets` folder by running the following command:

```
cd /projects/react-app-blueprint/static-assets
```

5. Create a `hello-world.txt` file in `static-assets` folder by running the following command:

```
touch hello-world.txt
```

AWS Cloud9 is built on a Linux-based platform. If you're using a Windows operating system, you can use the following command instead:

```
echo > hello-world.text
```

6. In the left-hand navigation, double-click the `hello-world.txt` file to open it in the editor,
   and add the following contents:

```
Hello, world!
```

Save the file. 7. Ensure you have the latest changes, and then commit and push the changes to the blueprint's CodeCatalyst source repository by running the following commands:

```
git pull
```

```
git add .
```

```
git commit -m "prettier setup"
```

```
git push
```

Pushing the changes started the release workflow, which will automatically publish the new version of the blueprint to the space.

## Step 6: Update the blueprint's published catalog version to the new version

After a blueprint is used to create a new project or applied to existing projects, you can still update the blueprint as a blueprint author. In
this step, you'll make changes to the blueprint and change the blueprint's catalog version.

1. In the CodeCatalyst console, navigate back to the space.
2. Choose **Settings**, and then choose **Blueprints**.
3. Choose **react-app-blueprint**, and then choose **Manage catalog version**.
4. Choose the new version, and then choose **Save**.

## Step 7: Update project with new blueprint version

A new version is now available in the space's blueprints catalog. As a blueprint user, you can update the version for the project created in
[Step 4: Create project with blueprint](#blueprint-getting-started-create-project "#blueprint-getting-started-create-project"). This ensures you have the latest
changes and fixes needed to meet best practices.

1. In the CodeCatalyst console, navigate to **react-app-project** project created in [Step 4: Create project with blueprint](#blueprint-getting-started-create-project "#blueprint-getting-started-create-project").
2. In the navigation pane, choose **Blueprints**.
3. Choose **Update blueprint** in the info box.
4. In the right-side **Code changes** panel, you can see
   the `hello-world.txt` and `package.json` updates.
5. Choose **Apply update**.

Choosing **Apply update** creates a pull request in the project with the
changes from the updated blueprint version. To make the updates to the project, you must merge
the pull request. For more information, see [Reviewing a pull request](pull-requests-review.md "pull-requests-review.md")
and [Merging a pull request](pull-requests-merge.md "pull-requests-merge.md").

1. In the **Blueprints** table, find the blueprint. In the **Status** column,
   choose **Pending pull request**, and then choose the link to the open pull request.
2. Review the pull request, and then choose **Merge**.
3. Choose **Fast forward merge** to keep the the default values, and then choose **Merge**.

## Step 8: View the changes in the project

Changes to the blueprint are now available in your project after [Step 7: Update project with new blueprint version](#blueprint-getting-started-update-project "#blueprint-getting-started-update-project"). As a blueprint user, you can view the changes in the source repository.

1. In the navigation pane, choose **Source repositories**, and then choose the name of the source repository created when the
   project was created.
2. Under **Files**, you can view the `hello-world.txt` file that was created in [Step 5: Update blueprint](#blueprint-getting-started-update-blueprint "#blueprint-getting-started-update-blueprint").
3. Choose the `hello-world.txt` to view the file's content.

Lifecycle management provides blueprint authors the ability centrally manage the software development lifecycle of every project that contains a particular blueprint. As seen
in this tutorial, you can push updates to the blueprint that can then be incorporated by projects that used the blueprint to create a new project or applied it to an existing
project. For more information, see [Working with lifecycle management as a blueprint author](lifecycle-management-dev.md "lifecycle-management-dev.md").
