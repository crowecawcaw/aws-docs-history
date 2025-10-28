# Using plugins in Amazon Q Apps

If [plugins](plugins.md "plugins.md") are configured for your Amazon Q Business application environment you
can add these to a Amazon Q Apps you're creating. Once you add a plugin to your Q Apps,
your app users will be able to perform plugin actions from within your Q Apps.

All plugins (new and legacy built-in plugins, and custom plugins) configured in the
Amazon Q Business console will be available for Q App creators to use.

###### Important

You can add only one action per plugin card.

The following section outlines how to add plugins to your Q Apps using both the
AWS Management Console and the AWS CLI.

###### Topics

- [Prerequisites for adding
  plugins](#qapps-plugins-prerequisites "#qapps-plugins-prerequisites")
- [Adding plugins in Amazon Q Apps](#qapps-plugins-add "#qapps-plugins-add")
- [Using plugins in Amazon Q Apps](#qapps-plugins-use "#qapps-plugins-use")

## Prerequisites for adding

plugins

Before your web experience users can create and use plugins, the web experience
IAM role for your application environment must have the correct permissions to perform the
necessary actions. We recommend updating your web experience IAM policy following
the steps outlined in [Prerequisites for configuring Amazon Q Business
built-in plugins](basic-plugins-prereqs.md "basic-plugins-prereqs.md").

## Adding plugins in Amazon Q Apps

To add a plugin to your Q App you can use either the AWS Management Console or the [CreateQApp](../api-reference/API_qapps_CreateQApp.md "../api-reference/API_qapps_CreateQApp.md") API operation. The
following tabs provide a procedure for the console and code examples for the
AWS CLI.

###### Note

You can also add a plugin to your Q App through your Amazon Q Business
web experience URL.

Console
**To add a plugin card to an
Q App**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In **Applications**, select the name of your
   application environment from the list of applications.
3. From the left navigation menu, choose
   **Enhancements**, and then choose
   **Amazon Q Apps**.
4. In the **Amazon Q Apps in library** section,
   choose the Q Apps that you want to add a plugin card to, and
   then select the web experience URL for that Q Apps.
5. From the Q Apps **App library** navigate to
   your app and select **Open**.
6. On the Q App page that opens, select **Add
   card**, and then select
   **Actions**.
7. From the **Actions** menu that opens up on
   the right, do the following:
   - For **Title** – Add a title
     for the card.
   - For **Plugin** – Select the
     plugin you want to add.
     Then, choose the actions you want your plugin to be able
     to perform.

   ###### Note

   You can only add one action per plugin
   card.
   - For **Prompt** – In the prompt
     section, you get a dropdown of actions for the plugin
     you select. Once you select an action in the dropdown,
     your prompt will be populated with a recommended
     template that you can use for configuration. We
     recommend that Q App creators follow the generated
     prompt when writing their own prompts to achieve better
     results.

8. Select **Save**.

AWS CLI
**To add a plugin to an Q App**

```
// Create an app with a single plugin card
aws qapps create-q-app \
--title `appTitle` \
--instance-id `qBusinessApplicationId` \
--description `pluginDescription` \
--app-definition '{"cards":[{"qPlugin":{"type":"q-plugin","title":"Action Card","id":"`cardUUID`","pluginId":"`QBusinessPluginId`","actionIdentifier":"`pa:jira:999.0_0:/rest/api/2/issue:POST`","prompt":"`Create a task in my project`"}}]}'
```

## Using plugins in Amazon Q Apps

To use a plugin within a Q App you can use either the Amazon Q Business web
experience URL or the [StartQAppSession](../api-reference/API_qapps_StartQAppSession.md "../api-reference/API_qapps_StartQAppSession.md") API operation. The
following tabs provide a procedure for the console and code examples for the
AWS CLI.

Web experience
**To use a plugin in an Q App**

1. From your **Q App** with plugins, select
   **Run**.

A window will open up asking you to log in to your
third party plugin
account. 2. After you login, Q Apps displays a dialog box asking you to
grant your Q App permission to access your
third party plugin account. From the
box, select **Allow**.

###### Note

If there are multiple plugins configured for a Q App, the
authentication flow for the second app occurs after the
first one. 3. After a successful connection, your plugin card will display a
form where you can fill in the details for the action you are
taking. 4. After filling in the details needed, select
**Create**.

Your plugin card displays a success message when your action
completes successfully.

AWS CLI
**To use a plugin in an Q App**

```

// start execution of an app

aws qapps start-q-app-session \
--app-id `fill in from create or get q app response` \
--app-version `fill in from create or get q app response` \
--instance-id `qBusinessApplicationId` \


// If you have input cards that should be passed to the plugin:

aws qapps start-q-app-session \
--app-id `fill in from create or get q app response` \
--app-version `fill in from create or get q app response` \
--initial-values '{"cardId":"`fill in from create q app input or get q app response`","value":"`fill in`"}' \
--instance-id `qBusinessApplicationId` \


// To get the status of an app, and results (if any):

aws qapps get-q-app-session \
--session-id `fill in from StartQAppSession response` \
--instance-id `qBusinessApplicationId` \

//To provide follow up messages to an app that is waiting for additional input:

aws qapps update-q-app-session \
--session-id `fill in from StartQAppSession response` \
-- values '{"cardId":"`fill in`","value":"`fill in`"}'
--instance-id `qBusinessApplicationId` \


```
