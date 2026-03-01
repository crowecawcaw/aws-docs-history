# Create a backend for a Gen 1 app

In this tutorial, you will set up a fullstack CI/CD workflow with Amplify. You will
deploy a frontend app to Amplify Hosting. Then you will create a backend using
Amplify Studio. Finally, you will connect the cloud backend to the frontend app.

## Prerequisites

Before you begin this tutorial, complete the following prerequisites.

**Sign up for an AWS account**

If you are not already an AWS customer, you need to [create an
AWS account](https://portal.aws.amazon.com/billing/signup#/start/email "https://portal.aws.amazon.com/billing/signup#/start/email") by following the online instructions. Signing up
enables you to access Amplify and other AWS services that you can use with
your application.

**Create a Git repository**

Amplify supports GitHub, Bitbucket, GitLab, and AWS CodeCommit. Push your
application to your Git repository.

**Install the Amplify Command Line Interface (CLI)**

For instructions, see [Install the Amplify
CLI](https://docs.amplify.aws/gen1/react/start/project-setup/prerequisites/#install-the-amplify-cli "https://docs.amplify.aws/gen1/react/start/project-setup/prerequisites/#install-the-amplify-cli") in the _Amplify Framework
Documentation_.

## Step 1: Deploy a frontend

If you have an existing frontend app in a git repository that you want to use for
this example, you can proceed to the instructions for deploying a frontend app.

If you need to create a new frontend app to use for this example, you can follow the
[Create React
App](https://create-react-app.dev/docs/getting-started "https://create-react-app.dev/docs/getting-started") instructions in the _Create React App
documentation_.

###### To deploy a frontend app

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. On the **All apps** page, choose **New app**,
   then **Host web app** in the upper right corner.
3. Select your GitHub, Bitbucket, GitLab, or AWS CodeCommit repository provider and
   then choose **Continue**.
4. Amplify authorizes access to your git repository. For GitHub repositories,
   Amplify now uses the GitHub Apps feature to authorize Amplify access.

For more information about installing and authorizing the GitHub App, see [Setting up Amplify access to GitHub repositories](setting-up-GitHub-access.md "setting-up-GitHub-access.md"). 5. On the **Add repository branch** page do the following:

    1. In the **Recently updated repositories** list, select
     the name of the repository to connect.
    2. In the **Branch** list, select the name of the
     repository branch to connect.
    3. Choose **Next**.

6. On the **Configure build settings** page, choose
   **Next**.
7. On the **Review** page, choose **Save and
   deploy**. When the deployment is complete, you can view your app on
   the `amplifyapp.com` default domain.

###### Note

To augment the security of your Amplify applications, the
_amplifyapp.com_ domain is registered in the [Public Suffix List (PSL)](https://publicsuffix.org/ "https://publicsuffix.org/"). For further
security, we recommend that you use cookies with a `__Host-` prefix if you
ever need to set sensitive cookies in the default domain name for your Amplify
applications. This practice will help to defend your domain against cross-site
request forgery attempts (CSRF). For more information see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the Mozilla Developer Network.

## Step 2: Create a backend

Now that you have deployed a frontend app to Amplify Hosting, you can create a
backend. Use the following instructions to create a backend with a simple database and
GraphQL API endpoint.

###### To create a backend

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. On the **All apps** page, select the app that you created in
   _Step 1_.
3. On the app homepage, choose the **Backend environments** tab,
   then choose **Get started**. This initiates the set up process
   for a default **staging** environment.
4. After the set up finishes, choose **Launch Studio** to access
   the **staging** backend environment in Amplify Studio.

Amplify Studio is a visual interface to create and manage your backend and
accelerate your frontend UI development. For more information about Amplify Studio, see
the [Amplify Studio
documentation](https://docs.amplify.aws/gen1/react/tools/console/ "https://docs.amplify.aws/gen1/react/tools/console/").

Use the following instructions to create a simple database using the Amplify Studio
visual backend builder interface.

###### Create a data model

1. On the home page for your app's **staging** environment,
   choose **Create data model**. This opens the data model
   designer.
2. On the **Data modeling** page, choose **Add
   model**.
3. For the title, enter `Todo`.
4. Choose **Add a field**.
5. For **Field name**, enter
   `Description`.

The following screenshot is an example of how your data model will look in the
designer.

![The Amplify Studio UI for creating a data model.](images/amplify-deploy-backend-1.png) 6. Choose **Save and Deploy**. 7. Return to the Amplify Hosting console and the **staging**
environment deployment will be in progress.

During deployment, Amplify Studio creates all the required AWS resources in the
backend, including an AWS AppSync GraphQL API to access data and an Amazon DynamoDB table to
host the Todo items. Amplify uses CloudFormation to deploy your backend, which enables you to
store your backend definition as infrastructure-as-code.

## Step 3: Connect the backend to the frontend

Now that you have deployed a frontend and created a cloud backend that contains a
data model, you need to connect them. Use the following instructions to pull your
backend definition down to your local app project with the Amplify CLI.

###### To connect a cloud backend to a local frontend

1. Open a terminal window and navigate to the root directory of your local
   project.
2. Run the following command in the terminal window, replacing the red text with
   the unique app ID and backend environment name for your project.

```
amplify pull --appId `abcd1234` --envName `staging`
```

3. Follow the instructions in the terminal window to complete the project set
   up.

Now you can configure the build process to add the backend to the continuous
deployment workflow. Use the following instructions to connect a frontend branch with a
backend in the Amplify Hosting console.

###### To connect a frontend app branch and cloud backend

1. On the app homepage, choose the **Hosting environments**
   tab.
2. Locate the **main** branch and choose
   **Edit**.

![The location of the Edit link for a branch in the Amplify console.](images/amplify_edit_backend_alternate.png) 3. In the **Edit target backend** window, for
**Environment**, select the name of the backend to connect. In
this example, choose the **staging** backend that you created in
_Step 2_.

By default, full-stack CI/CD is enabled. Uncheck this option to turn off
full-stack CI/CD for this backend. Turning off full-stack CI/CD causes the app to
run in _pull only_ mode. At build time, Amplify will
automatically generate the `aws-exports.js` file only, without
modifying your backend environment. 4. Next, you must set up a service role to give Amplify the permissions it
requires to make changes to your app backend. You can either use an existing
service role or create a new one. For instructions, see [Adding a service role with permissions to deploy backend resources](amplify-service-role.md "amplify-service-role.md"). 5. After adding a service role, return to the **Edit target
backend** window and choose **Save**. 6. To finish connecting the **staging** backend to
the **main** branch of the frontend app, perform a
new build of your project.

Do one of the following:

    * From your git repository, push some code to initiate a build in the
     Amplify console.
    * In the Amplify console, navigate to the app's build details page and
     choose **Redeploy this version**.

## Next steps

### Set up feature branch deployments

Follow our recommended workflow to [set up feature branch deployments with multiple backend
environments](multi-environments.md#team-workflows-with-amplify-cli-backend-environments "multi-environments.md#team-workflows-with-amplify-cli-backend-environments").

### Create a frontend UI in Amplify Studio

Use Studio to build your frontend UI with a set of ready-to-use UI
components, and then connect it to your app backend. For more information and
tutorials, see the user guide for [Amplify Studio](https://docs.amplify.aws/gen1/react/tools/console/ "https://docs.amplify.aws/gen1/react/tools/console/") in the _Amplify Framework
Documentation_.
