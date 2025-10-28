Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Tutorial: Pull from a package repository

In this tutorial, you learn how to create a workflow that runs an application whose
dependencies are pulled from a [CodeCatalyst package
repository](packages-concepts.md#packages-concepts-repository "packages-concepts.md#packages-concepts-repository"). The application is a simple Node.js app that prints a 'Hello World' message
to the CodeCatalyst logs. The application has a single dependency: the [lodash](https://www.npmjs.com/package/lodash "https://www.npmjs.com/package/lodash") npm package. The `lodash`
package is used to transform a `hello-world` string to `Hello World`. You
will use version 4.17.20 of this package.

After setting up your application and workflow, you configure CodeCatalyst to block additional
versions of `lodash` from being imported into the CodeCatalyst package repository from the
public external registry ([npmjs.com](https://www.npmjs.com/ "https://www.npmjs.com/")). You then test
that additional versions of `lodash` are blocked successfully.

By the end of this tutorial, you should have a good understanding of how a workflow
interacts with package repositories, both inside and outside CodeCatalyst, in order to retrieve
packages. You should also understand the behind-the-scenes interactions that occur between npm,
your package repository, your workflow, and your application's `package.json`
file.

###### Topics

- [Prerequisites](#packages-tutorial-prereqs "#packages-tutorial-prereqs")
- [Step 1: Create a source repository](#packages-tutorial-source-repo "#packages-tutorial-source-repo")
- [Step 2: Create the CodeCatalyst and gateway package
  repositories](#packages-tutorial-package-repo "#packages-tutorial-package-repo")
- [Step 3: Create the 'Hello World'
  application](#packages-tutorial-create-app "#packages-tutorial-create-app")
- [Step 4: Create a workflow that runs 'Hello
  World'](#packages-tutorial-create-workflow "#packages-tutorial-create-workflow")
- [Step 5: Verify the workflow](#packages-tutorial-verify "#packages-tutorial-verify")
- [Step 6: Block imports from npmjs.com](#packages-tutorial-block "#packages-tutorial-block")
- [Step 7: Test the blocking feature](#packages-tutorial-test-block "#packages-tutorial-test-block")
- [Clean up](#packages-tutorial-cleanup "#packages-tutorial-cleanup")

## Prerequisites

Before you begin:

- You need a CodeCatalyst **Space**. For more
  information, see [Creating a space](spaces-create.md "spaces-create.md").
- In your CodeCatalyst space, you need an empty project called:

```
codecatalyst-package-project
```

Use the **Start from scratch** option to create this project.

For more information, see [Creating an empty project in Amazon CodeCatalyst](projects-create.md#projects-create-empty "projects-create.md#projects-create-empty").

## Step 1: Create a source repository

In this step, you create a source repository in CodeCatalyst. This repository stores the
tutorial's source files, such as the `index.js` and
`package.json` files.

For more information about source repositories, see [Creating a source repository](source-repositories-create.md "source-repositories-create.md").

###### To create a source repository

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your project, `codecatalyst-package-project`.
3. In the navigation pane, choose **Code**, and then choose
   **Source repositories**.
4. Choose **Add repository**, and then choose **Create
   repository**.
5. In **Repository name**, enter:

```
`hello-world-app`
```

6. Choose **Create**.

## Step 2: Create the CodeCatalyst and gateway package

repositories

In this step, you create a package repository in your CodeCatalyst project, and connect it to a
gateway repository, also in your CodeCatalyst project. You later import the tutorial's dependency,
`lodash`, from npmjs.com into both repositories.

The gateway repository is the 'glue' that connects your package repository in CodeCatalyst to
the public npmjs.com.

For more information about package repositories, see [Publish and share software packages in CodeCatalyst](packages.md "packages.md").

###### Note

This tutorial uses the terms _CodeCatalyst package repository_ and
_gateway repository_ to refer to the two repositories that you create
in CodeCatalyst in the following procedure.

###### To create CodeCatalyst package and gateway repositories

1. In the navigation pane, choose **Packages**.
2. Choose **Create package repository**.
3. In **Repository name**, enter:

```
`codecatalyst-package-repository`
```

4. Choose **+ Select upstream repositories**.
5. Choose **Gateway repositories**.
6. In the **npm-public-registry-gateway** box, choose
   **Create**.
7. Choose **Select**.
8. Choose **Create**.

CodeCatalyst creates a package repository called
`codecatalyst-package-repository` which is connected to a gateway
repository. The gateway repository is connected to the npmjs.com registry.

## Step 3: Create the 'Hello World'

application

In this step, you create a 'Hello World' Node.js application and import its dependency
(`lodash`) into your gateway and CodeCatalyst package repositories.

To create the application, you need a development machine with Node.js and the associated
`npm` client installed.

This tutorial assumes you'll be using a CodeCatalyst Dev Environment as your development machine.
Although you don't have to use a CodeCatalyst Dev Environment, it is recommended because it provides a
clean working environment, has Node.js and `npm` preinstalled, and is easy to
delete when you have finished the tutorial. For more information about CodeCatalyst Dev Environments,
see [Creating a Dev Environment](devenvironment-create.md "devenvironment-create.md").

Use the following instructions to launch a CodeCatalyst Dev Environment and use it to create the
'Hello World' application.

###### To launch a CodeCatalyst Dev Environment

1. In the navigation pane, choose **Code**, and then choose
   **Dev Environments**.
2. Near the top choose **Create Dev Environment**, and then choose
   **AWS Cloud9 (in browser)**.
3. Make sure that **Repository** is set to `hello-world-app`
   and **Existing branch** is set to `main`. Choose
   **Create**.

Your Dev Environment launches in a new browser tab, and your repository
(`hello-world-app`) is cloned into it. 4. Leave both CodeCatalyst browser tabs open, and go to the next procedure.

###### To create the 'Hello World' Node.js application

1. Go to your Dev Environment.
2. At the terminal prompt, change to the `hello-world-app` source repository
   root directory:

```
cd hello-world-app
```

3. Initialize a Node.js project:

```
npm init -y
```

The initialization creates a `package.json` file in the root
directory of `hello-world-app`. 4. Connect the npm client in your Dev Environment to your CodeCatalyst package repository:

    1. Switch to the CodeCatalyst console.
    2. In the navigation pane, choose **Packages**.
    3. Choose `codecatalyst-package-repository`.
    4. Choose **Connect to repository**.
    5. Choose **Create token**. A personal access token (PAT) is created
     for you.
    6. Choose **Copy** to copy the commands.
    7. Switch to your Dev Environment.
    8. Make sure you're in the `hello-world-app` directory.
    9. Paste the commands. They look similar to the following:



    ```
    npm set registry=https://packages.us-west-2.codecatalyst.aws/npm/ExampleCompany/codecatalyst-package-project/codecatalyst-package-repository/ --location project
    npm set //packages.us-west-2.codecatalyst.aws/npm/ExampleCompany/codecatalyst-package-project/hello-world-app/:_authToken=`username`:`token-secret`
    ```

5. Import `lodash` version 4.17.20:

```
npm install lodash@v4.17.20 --save --save-exact
```

npm looks for `lodash` version 4.17.20 in the following locations, in the
following order:

    * In the Dev Environment. It can't find it here.
    * In the CodeCatalyst package repository. It can't find it here.
    * In the gateway repository. It can't find it here.
    * In npmjs.com. It finds it here.

npm imports `lodash` into the gateway repository, the CodeCatalyst package
repository, and the Dev Environment.

###### Note

If you had not connected the npm client to your CodeCatalyst package repository in step 4,
then npm would have pulled `lodash` directly from npmjs.com and would not
have imported the package to either repository.

npm also updates your `package.json` file with the
`lodash` dependency, and creates a `node_modules`
directory containing `lodash` and all its dependencies. 6. Test that `lodash` was successfully imported to your Dev Environment.
Enter:

```
npm list
```

The following message appears, indicating a successful import:

```
`-- lodash@4.17.20
```

7. (Optional) Open `hello-world-app/package.json` and verify that the
   lines in **`red bold`** were
   added:

```
{
  "name": "hello-world-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  **`dependencies": {
 "lodash": "4.17.20"`**
  }
}
```

8. In `/hello-world-app`, create a file called `index.js`
   with the following contents:

###### Tip

You can use the side navigation in your Dev Environment to create this file.

```
// Importing lodash library
const _ = require('lodash');

// Input string
const inputString = 'hello-world';

// Transforming the string using lodash
const transformedString = _.startCase(inputString.replace('-', ' '));

// Outputting the transformed string to the console
console.log(transformedString);
```

###### To test that 'lodash' was imported to your gateway and CodeCatalyst package

repositories

1. Switch to the CodeCatalyst console.
2. In the navigation pane, choose **Packages**.
3. Choose **npm-public-registry-gateway**.
4. Make sure `lodash` is displayed. The **Latest version**
   column indicates `4.17.20`.
5. Repeat this procedure for the `codecatalyst-package-repository`. You
   might need to refresh the browser window to see the imported package.

###### To test 'Hello World' in your Dev Environment

1. Switch to your Dev Environment.
2. Make sure you're still in the `hello-world-app` directory, and then
   run the application:

```
node index.js
```

A `Hello World` message appears. Node.js ran the application using the
`lodash` package that you downloaded to your Dev Environment in a previous
step.

###### To ignore the 'node_modules' directory and commit 'Hello World'

1. Ignore the `node_modules` directory. Enter:

```
echo "node_modules/" >> .gitignore
```

It is a best practice to avoid committing this directory. Also, committing this
directory will interfere with later steps in this tutorial. 2. Add, commit, and push:

```
git add .
git commit -m "add the Hello World application"
git push
```

The 'Hello World' application and project files are added to your source
repository.

## Step 4: Create a workflow that runs 'Hello

World'

In this step, you create a workflow that runs the 'Hello World' application using the
`lodash` dependency. The workflow includes a single _action_,
or task, called `RunHelloWorldApp`. The `RunHelloWorldApp` action
includes the following noteworthy commands and sections:

- **`Packages`**

This section indicates the name of the CodeCatalyst package repository that the action must
connect to when running `npm install`.

- **`- Run: npm install`**

This command tells npm to install the dependencies specified in the
`package.json` file. The only dependency specified in the
`package.json` file is `lodash`. npm looks for
`lodash` in the following locations:

    + In the Docker image running the action. It can't find it here.
    + In the CodeCatalyst package repository. It finds it here.

After npm finds `lodash`, it imports it to the Docker image running the
action.

- **`- Run: npm list`**

This command prints out which version of `lodash` was downloaded to the
Docker image running the action.

- **`- Run: node index.js`**

This command runs the 'Hello World' application using the dependency specified in the
`package.json` file.

Notice that the `RunHelloWorldApp` action is a build action, as indicated by
the `aws/build@v1` identifier near the top of the workflow. For more
information about the build action, see [Building with workflows](build-workflow-actions.md "build-workflow-actions.md").

Use the following instructions to create a workflow that pulls the `lodash`
dependency from your CodeCatalyst package repository and then runs your 'Hello World'
application.

###### To create a workflow

1. Switch to the CodeCatalyst console.
2. In the navigation pane, choose **CI/CD**, and then choose
   **Workflows**.
3. Choose **Create workflow**.
4. For **Source repository**, choose
   `hello-world-app`.
5. For **Branch**, choose `main`.

The workflow definition file is will be created in the chosen source repository and
branch. 6. Choose **Create**. 7. Choose **YAML** near the top. 8. Delete the YAML sample code. 9. Add the following YAML code:

```
Name: codecatalyst-package-workflow
SchemaVersion: "1.0"

# Required - Define action configurations.
Actions:
  RunHelloWorldApp:
    # Identifies the action. Do not modify this value.
    Identifier: aws/build@v1
    Compute:
      Type: Lambda
    Inputs:
      Sources:
        - WorkflowSource # This specifies your source repository.
    Configuration:
      Steps:
        - Run: npm install
        - Run: npm list
        - Run: node index.js
      Container: # This specifies the Docker image that runs the action.
        Registry: CODECATALYST
        Image: CodeCatalystLinuxLambda_x86_64:2024_03
    Packages:
      NpmConfiguration:
        PackageRegistries:
          - PackagesRepository: `codecatalyst-package-repository`

```

In the preceding code, replace
`codecatalyst-package-repository` with the name of the
CodeCatalyst package repository that you created in [Step 2: Create the CodeCatalyst and gateway package
repositories](#packages-tutorial-package-repo "#packages-tutorial-package-repo").

For information about the properties in this file, see the [Build and test actions YAML](build-action-ref.md "build-action-ref.md"). 10. (Optional) Choose **Validate** to make sure the YAML code is valid
before committing. 11. Choose **Commit**. 12. On the **Commit workflow** dialog box, enter the following:

    1. For **Workflow file name**, keep the default,
     `codecatalyst-package-workflow`.
    2. For **Commit message**, enter:



    ```
    `add initial workflow file`
    ```
    3. For **Repository**, choose
     **hello-world-app**.
    4. For **Branch name**, choose **main**.
    5. Choose **Commit**.You have now created a workflow.

###### To run the workflow

1. Next to the workflow you just created
   (`codecatalyst-package-workflow`), choose
   **Actions** and then choose **Run**.

A workflow run starts. 2. In the green notification at the top, on the right, choose the link to the run. The
link looks similar to `View Run-1234`.

A workflow diagram appears, showing who started the run and the
**RunHelloWorldApp** action. 3. Choose the **RunHelloWorldApp** action box to watch the action's
progress. 4. When the run finishes, go to [Step 5: Verify the workflow](#packages-tutorial-verify "#packages-tutorial-verify").

## Step 5: Verify the workflow

In this step, you verify that the workflow successfully ran the 'Hello World' application
with its `lodash` dependency.

###### To verify that the 'Hello World' application ran using its dependency

1. In the workflow diagram, choose the **RunHelloWorldApp** box.

A list of log messages appear. 2. Expand the `node index.js` log message.

The following message appears:

```
[Container] 2024/04/24 21:15:41.545650 Running command node index.js
Hello World
```

The appearance of `Hello Word` (instead of `hello-world`)
indicates that the `lodash` dependency was successfully used. 3. Expand the `npm list` log.

A message similar to the following appears:

```
└── lodash@4.17.20
```

This message indicates that `lodash` version 4.17.20 was downloaded to the
Docker image running the workflow action.

## Step 6: Block imports from npmjs.com

Now that `lodash` version 4.17.20 is present in your gateway and CodeCatalyst
package repositories, you can block imports of other versions. Blocking prevents you from
accidentally importing later (or earlier) versions of `lodash`, which might contain
malicious code. For more information, see [Editing package origin controls](package-origin-controls.md "package-origin-controls.md") and [Dependency substitution attacks](package-origin-controls.md#dependency-substitution-attacks "package-origin-controls.md#dependency-substitution-attacks").

Use the following instructions to block imports of `lodash` into your gateway
repository. When you block packages at the gateway, they are also blocked at downstream
locations.

###### To block imports to your gateway repository

1. In the navigation pane, choose **Packages**.
2. Choose **npm-publish-registry-gateway**.
3. Choose `lodash`.
4. Near the top, choose **Origin controls**.
5. Under **Upstream**, choose **Block**.
6. Choose **Save**.

You have now blocked imports into your gateway repository (and downstream repositories
and computers) from npmjs.com.

## Step 7: Test the blocking feature

In this section, you verify that the blocking you set up in [Step 6: Block imports from npmjs.com](#packages-tutorial-block "#packages-tutorial-block") is working. You
start by configuring 'Hello World' to request version 4.17.2**1**
of `lodash` instead of the one available in your gateway repository, which is
4.17.2**0**. You then check that the application cannot pull
version 4.17.21 from nmpjs.com, indicating a successful blockage. As a final test, you unblock
imports to your gateway repository, and check that the application can successfully pull
version 4.17.21 of `lodash`.

Use the following set of procedures to test the blocking feature.

###### Before you begin

1. Switch to your Dev Environment.
2. Pull the `codecatalyst-package-workflow.yaml` file that you
   created using the CodeCatalyst console earlier:

```
git pull
```

###### To configure 'Hello World' to request version 4.17.21 of 'lodash'

1. Open `/hello-world-app/package.json`.
2. Change the `lodash` version to 4.17.21 as shown in **`red bold`**:

```
{
  "name": "hello-world-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "lodash": "**`4.17.21`**"
  }
}
```

There is now a mismatch between the version in the `package.json`
file (4.17.21) and the version in the gateway and CodeCatalyst package repositories
(4.17.20). 3. Add, commit, and push:

```
git add .
git commit -m "update package.json to use lodash 4.17.21"
git push
```

###### To test that 'Hello World' cannot pull version 4.17.21 of 'lodash'

1.  Run the workflow with the version mismatch:
    1. Switch to the CodeCatalyst console.
    2. In the navigation pane, choose **CI/CD**, and then choose
       **Workflows**.
    3. Next to `codecatalyst-package-workflow`, choose
       **Actions**, and then choose **Run.**

    npm looks in `package.json` for dependencies and sees that
    version 4.17.21 of `lodash` is required by 'Hello World'. npm looks for the
    dependency in the following locations, in the following order:

        * In the Docker image running the action. It can't find it here.
        * In the CodeCatalyst package repository. It can't find it here.
        * In the gateway repository. It can't find it here.
        * In npmjs.com. It finds it here.

    After npm finds version 4.17.21 in npmjs.com, it tries to import it into the
    gateway repository, but because you set up the gateway to block imports of
    `lodash`, the import does not occur.

    Because the import does not occur, the workflow fails.

2.  Verify that the workflow failed:
    1. In the green notification at the top, on the right, choose the link to the run.
       The link looks similar to `View Run-2345`.
    2. In the workflow diagram, choose the **RunHelloWorldApp**
       box.
    3. Expand the `npm install` log message.

    The following message appears:

    ```
    [Container] 2024/04/25 17:20:34.995591 Running command npm install
    npm ERR! code ETARGET
    npm ERR! notarget No matching version found for lodash@4.17.21.
    npm ERR! notarget In most cases you or one of your dependencies are requesting
    npm ERR! notarget a package version that doesn't exist.

    npm ERR! A complete log of this run can be found in: /tmp/.npm/_logs/2024-05-08T22_03_26_493Z-debug-0.log
    ```

    The error indicates that version 4.17.21 couldn't be found. This is expected
    because you blocked it.

###### To unblock imports from npmjs.com

1. In the navigation pane, choose **Packages**.
2. Choose **npm-publish-registry-gateway**.
3. Choose `lodash`.
4. Near the top, choose **Origin controls**.
5. Under **Upstream**, choose **Allow**.
6. Choose **Save**.

You have now unblocked imports of `lodash`.

Your workflow can now import version 4.17.21 of `lodash`.

###### To test that imports from npmjs.com are unblocked

1. Run your workflow again. This time the workflow should succeed because the import of
   4.17.21 should now work. To run the workflow again:
   1. Choose **CI/CD** and then choose
      **Workflows**.
   2. Next to `codecatalyst-package-workflow`, choose
      **Actions** and choose **Run**.
   3. In the green notification at the top, on the right, choose the link to the run.
      The link looks similar to `View Run-3456`.

   A workflow diagram appears, showing who started the run and the
   **RunHelloWorldApp** action. 4. Choose the **RunHelloWorldApp** action box to watch the action's
   progress. 5. Expand the `npm list` log message and verify that a message similar to
   the following appears:

   ```
   └── lodash@4.17.21
   ```

   This message indicates that `lodash` version 4.17.21 was
   downloaded.

2. Verify that version 4.17.21 was imported to your CodeCatalyst and gateway
   repositories:
   1. In the navigation pane, choose **Packages**.
   2. Choose **npm-public-registry-gateway**.
   3. Find `lodash` and make sure the version is `4.17.21`.

   ###### Note

   Although version 4.17.20 is not listed on this page, you can find it by choosing
   `lodash` and then choosing **Versions** near the
   top. 4. Repeat these steps to check that version 4.17.21 was imported to
   `codecatalyst-package-repository`.

## Clean up

Clean up the files and services used in this tutorial to avoid being charged for
them.

###### To clean up the packages tutorial

1. Delete the `codecatalyst-package-project`:
   1. In the CodeCatalyst console, nagivate to the
      `codecatalyst-package-project` project if you're not there
      already.
   2. In the navigation pane, choose **Project settings**.
   3. Choose **Delete project**, enter `delete`,
      and choose **Delete project**.

   CodeCatalyst deletes all project resources, including the source, gateway, and CodeCatalyst
   package repositories. The Dev Environment is also deleted.

2. Delete the PAT token:
   1. Choose your username on the right, and then choose **My
      settings**.
   2. Under **Personal access tokens**, choose the token you created in
      this tutorial and choose **Delete**.

In this tutorial, you learned how to create a workflow that runs an application that pulls
its dependencies from a CodeCatalyst package repository. You also learned how to block and unblock
packages from entering your gateway and CodeCatalyst package repositories.
