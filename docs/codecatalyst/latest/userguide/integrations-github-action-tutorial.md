

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Tutorial: Lint code using a GitHub Action
<a name="integrations-github-action-tutorial"></a>

In this tutorial, you add the [Super-Linter GitHub Action](https://github.com/marketplace/actions/super-linter) to an Amazon CodeCatalyst workflow. The Super-Linter action inspects code, finds areas where the code has errors, formatting issues, and suspicious constructs, and then outputs the results to the CodeCatalyst console). After adding the linter to your workflow, you run the workflow to lint a sample Node.js application (`app.js`). You then fix the reported problems and run the workflow again to see if the fixes worked.

**Tip**  
Consider using Super-Linter to lint YAML files, such as [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html).

**Topics**
+ [Prerequisites](#integrations-github-action-tutorial-prereqs)
+ [Step 1: Create a source repository](#integrations-github-action-tutorial-create-source-repo)
+ [Step 2: Add an app.js file](#integrations-github-action-tutorial-add-appjs)
+ [Step 3: Create a workflow that runs the Super-Linter action](#integrations-github-action-tutorial-create-workflow)
+ [Step 4: Fix problems that the Super-Linter found](#integrations-github-action-tutorial-fix-probs)
+ [Clean up](#integrations-github-action-tutorial-cleanup)

## Prerequisites
<a name="integrations-github-action-tutorial-prereqs"></a>

Before you begin, you'll need:
+ A CodeCatalyst **space** with a connected AWS account. For more information, see [Creating a space](spaces-create.md).
+ An empty project in your CodeCatalyst space called `codecatalyst-linter-project`. Choose the **Start from scratch** option to create this project.

  ```
  ```

  For more information, see [Creating an empty project in Amazon CodeCatalyst](projects-create.md#projects-create-empty).

## Step 1: Create a source repository
<a name="integrations-github-action-tutorial-create-source-repo"></a>

In this step, you create a source repository in CodeCatalyst. You'll use this repository to store the sample application source file, `app.js`, for this tutorial.

For more information about source repositories, see [Creating a source repository](source-repositories-create.md).

**To create a source repository**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your project, `codecatalyst-linter-project`.

1. In the navigation pane, choose **Code**, and then choose **Source repositories**. 

1. Choose **Add repository**, and then choose **Create repository**.

1. In **Repository name**, enter:

   ```
   codecatalyst-linter-source-repository
   ```

1. Choose **Create**.

## Step 2: Add an app.js file
<a name="integrations-github-action-tutorial-add-appjs"></a>

In this step, you add an `app.js` file to your source repository. The `app.js` contains function code that has a few mistakes that the linter will find.

**To add the app.js file**

1. In the CodeCatalyst console, choose your project, `codecatalyst-linter-project`.

1. In the navigation pane, choose **Code**, and then choose **Source repositories**.

1. From the list of source repositories, choose your repository, `codecatalyst-linter-source-repository`.

1. In **Files**, choose **Create file**.

1. In the text box, enter the following code:

   ```
   // const axios = require('axios')
   // const url = 'http://checkip.amazonaws.com/';
   let response;
   /**
    *
    * Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
    * @param {Object} event - API Gateway Lambda Proxy Input Format
    *
    * Context doc: https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-context.html 
    * @param {Object} context
    *
    * Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    * @returns {Object} object - API Gateway Lambda Proxy Output Format
    *
    */
   exports.lambdaHandler = async (event, context) => {
     try {
       // const ret = await axios(url);
       response = {
         statusCode: 200,
         'body': JSON.stringify({
           message: 'hello world'
           // location: ret.data.trim()
         })
       }
     } catch (err) {
       console.log(err)
       return err
     }
   
       return response
   }
   ```

1. For **File name**, enter `app.js`. Keep the other default options.

1. Choose **Commit**.

   You have now created a file called `app.js`.

## Step 3: Create a workflow that runs the Super-Linter action
<a name="integrations-github-action-tutorial-create-workflow"></a>

In this step, you create a workflow that runs the Super-Linter action when you push code to your source repository. The workflow consists of the following building blocks, which you define in a YAML file:
+ **A trigger** – This trigger starts the workflow run automatically when you push a change to your source repository. For more information about triggers, see [Starting a workflow run automatically using triggers](workflows-add-trigger.md).
+ **A 'GitHub Actions' action** – On trigger, the **GitHub Actions** action runs the Super-Linter action, which in turn inspects all files in your source repository. If the linter finds an issue, the workflow action fails. 

**To create a workflow that runs the Super-Linter action**

1. In the CodeCatalyst console, choose your project, `codecatalyst-linter-project`.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**. 

1. Choose **Create workflow**.

1. For **Source repository**, choose `codecatalyst-linter-source-repository`.

1. For **Branch**, choose `main`.

1. Choose **Create**.

1. Delete the YAML sample code.

1. Add the following YAML:

   ```
   Name: codecatalyst-linter-workflow
   SchemaVersion: "1.0"
   Triggers:
     - Type: PUSH
       Branches:
         - main
   Actions:
     SuperLinterAction:
       Identifier: aws/github-actions-runner@v1
       Configuration:
         Steps:
           {{github-action-code}}
   ```

   In the preceding code, replace {{github-action-code}} with the Super-Linter action code, as instructed in the following steps of this procedure.

1. Go to the [Super-Linter page](https://github.com/marketplace/actions/super-linter) in the GitHub Marketplace.

1. Under `steps:`(lowercase), find the code and paste it into the CodeCatalyst workflow under `Steps:` (uppercase).

   Adjust the GitHub Action code to conform to CodeCatalyst standards, as shown in the following code.

   Your CodeCatalyst workflow now looks like this:

   ```
   Name: codecatalyst-linter-workflow
   SchemaVersion: "1.0"
   Triggers:
     - Type: PUSH
       Branches:
         - main
   Actions:
     SuperLinterAction:
       Identifier: aws/github-actions-runner@v1
       Configuration:
         Steps:
           - name: Lint Code Base
             uses: github/super-linter@v4
             env:
               VALIDATE_ALL_CODEBASE: "true"
               DEFAULT_BRANCH: main
   ```

1. (Optional) Choose **Validate** to make sure the YAML code is valid before committing.

1. Choose **Commit**, enter a **Commit message**, select your `codecatalyst-linter-source-repository` **Repository**, and choose **Commit** again.

   You have now created a workflow. A workflow run starts automatically because of the trigger defined at the top of the workflow.

**To view the workflow run in progress**

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the workflow you just created: `codecatalyst-linter-workflow`.

1. In the workflow diagram, choose **SuperLinterAction**.

1. Wait for the action to fail. This failure is expected because the linter found problems in the code.

1. Leave the CodeCatalyst console open and go to [Step 4: Fix problems that the Super-Linter found](#integrations-github-action-tutorial-fix-probs).

## Step 4: Fix problems that the Super-Linter found
<a name="integrations-github-action-tutorial-fix-probs"></a>

The Super-Linter should have found problems in the `app.js` code, as well as the `README.md` file included in your source repository.

**To fix the problems the linter found**

1. In the CodeCatalyst console, choose the **Logs** tab, and then choose **Lint Code Base**.

   The logs that the Super-Linter action generated are displayed.

1. In the Super-Linter logs, scroll down to around line 90, where you find the start of the problems. They look similar to the following: 

   ```
   /github/workspace/hello-world/app.js:3:13: Extra semicolon.
   /github/workspace/hello-world/app.js:9:92: Trailing spaces not allowed.
   /github/workspace/hello-world/app.js:21:7: Unnecessarily quoted property 'body' found.
   /github/workspace/hello-world/app.js:31:1: Expected indentation of 2 spaces but found 4.
   /github/workspace/hello-world/app.js:32:2: Newline required at end of file but not found.
   ```

1. Fix `app.js` and `README.md` in your source repository and commit your changes. 
**Tip**  
To fix the `README.md`, add `markdown` to the code block, like this:  

   ```
   ```markdown
   Setup examples:
   ...
   ```
   ```

   Your changes start another workflow run automatically. Wait for the workflow to finish. If you fixed all the problems, the workflow should succeed.

## Clean up
<a name="integrations-github-action-tutorial-cleanup"></a>

Clean up in CodeCatalyst to remove traces of this tutorial from your environment.

**To clean up in CodeCatalyst**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Delete `codecatalyst-linter-source-repository`.

1. Delete `codecatalyst-linter-workflow`.

In this tutorial, you learned how to add the Super-Linter GitHub Action to a CodeCatalyst workflow in order to lint some code.