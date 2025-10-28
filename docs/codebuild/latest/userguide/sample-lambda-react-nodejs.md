# Create a single page React app with CodeBuild Lambda Node.js

[Create React App](https://create-react-app.dev/ "https://create-react-app.dev/") is a way to create single-page React applications. The following Node.js sample uses Node.js to build the source artifacts from Create React App and returns the build artifacts.

## Set up your source repository and artifacts bucket

Create a source repository for your project using yarn and Create React App.

###### To set up the source repository and artifacts bucket

1. On your local machine, run `yarn create react-app `<app-name>`` to create a simple React app.
2. Upload the React app project folder to a supported source repository. For a list of supported
   source types, see [ProjectSource](../APIReference/API_ProjectSource.md "../APIReference/API_ProjectSource.md").

## Create a CodeBuild Lambda Node.js project

Create an AWS CodeBuild Lambda Node.js project.

###### To create your CodeBuild Lambda Node.js project

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. If a CodeBuild information page is displayed, choose **Create build project**. Otherwise, on the navigation pane, expand **Build**,
   choose **Build projects**, and then choose **Create build project**.
3. In **Project name**, enter
   a name for this build project. Build project names must be unique across each AWS account. You can also include an optional description of the build project to
   help other users understand what this project is used for.
4. In **Source**, select the source repository
   where your AWS SAM project is located.
5. In **Environment**:
   - For **Compute**, select **Lambda**.
   - For **Runtime(s)**, select **Node.js**.
   - For **Image**, select **aws/codebuild/amazonlinux-x86_64-lambda-standard:nodejs20**.

6. In **Artifacts**:
   - For **Type**, select **Amazon S3**.
   - For **Bucket name**, select the project artifacts bucket you created earlier.
   - For **Artifacts packaging**, select **Zip**.

7. Choose **Create build project**.

## Set up the project buildspec

In order to build your React app, CodeBuild reads and executes build commands from a buildspec file.

###### To set up your project buildspec

1. In the CodeBuild console, select your build project, then choose **Edit** and **Buildspec**.
2. In **Buildspec**, choose **Insert build commands** and then **Switch to editor**.
3. Delete the pre-filled build commands and paste in the following buildspec.

```
version: 0.2
phases:
  build:
    commands:
      - yarn
      - yarn add --dev jest-junit @babel/plugin-proposal-private-property-in-object
      - yarn run build
      - yarn run test -- --coverage --watchAll=false --testResultsProcessor="jest-junit" --detectOpenHandles
artifacts:
  name: "build-output"
  files:
    - "**/*"
reports:
  test-report:
    files:
      - 'junit.xml'
    file-format: 'JUNITXML'
  coverage-report:
    files:
      - 'coverage/clover.xml'
    file-format: 'CLOVERXML'
```

4. Choose **Update buildspec**.

## Build and run your React app

Build the React app on CodeBuild Lambda, download the build artifacts, and run the React app locally.

###### To build and run your React app

1. Choose **Start build**.
2. Once the build has finished, navigate to your Amazon S3 project artifacts bucket and download the React app artifact.
3. Unzip the React build artifact and `run npm install -g serve && serve -s build` in the project folder.
4. The `serve` command will serve the static site on a local port and print output to your terminal. You can visit the localhost
   URL under `Local:` in the terminal output to view your React app.

To learn more about how to handle deployment for a React based server, see
[Create React App Deployment](https://create-react-app.dev/docs/deployment/ "https://create-react-app.dev/docs/deployment/").

## Clean up your infrastructure

To avoid further charges for resources you used during this tutorial, delete the resources created for your CodeBuild project.

###### To clean up your infrastructure

1. Delete your project artifacts Amazon S3 bucket
2. Navigate to the CloudWatch console and delete the CloudWatch log groups associated with your CodeBuild project.
3. Navigate to the CodeBuild console and delete your CodeBuild project by choosing **Delete build project**.
