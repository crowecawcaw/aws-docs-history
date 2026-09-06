

# Creating an incoming webhook to start a build
<a name="create-incoming-webhook"></a>

Set up an incoming webhook in the Amplify console to start a build without committing code to your Git repository. You can use webhooks with headless CMS tools (such as Contentful or GraphCMS) to start a build whenever content changes, or to perform daily builds using services such as Zapier.

**To create an incoming webhook**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. Choose the app that you want to create a webhook for.

1. In the navigation pane, choose **Hosting**, then **Build settings**.

1. On the **Build settings** page, scroll down to the **Incoming webhooks** section and choose **Create webhook**.

1. In the **Create webhook** dialog box, do the following:

   1. For **Webhook name** enter a name for the webhook.

   1. For **Branch to build**, select the branch to build on incoming webhook requests.

   1. Choose **Create webhook**.

1. In the **Incoming webhooks** section, do one of the following:
   + Copy the webhook URL and provide it to a headless CMS tool or other service to initiate builds.
   + Run the curl command in a terminal window to start a new build.