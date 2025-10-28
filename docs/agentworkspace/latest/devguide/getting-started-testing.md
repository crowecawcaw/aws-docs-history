# Test your application for Amazon Connect Agent Workspace

locally

Once you have a minimal version of the app that you want to use in Amazon Connect Agent Workspace
with the SDK that you want to test in the agent workspace, run your app locally and
create an application in the AWS console with an _AccessUrl_ using
the localhost endpoint, like `http://localhost:3000`.

## Creating an

application and associating to your instance

###### Note

Detailed steps for creating and managing applications can be found in the
admin guide under [Third-party applications (3p
apps) in the agent workspace (Preview)](../../../connect/latest/adminguide/3p-apps.md "../../../connect/latest/adminguide/3p-apps.md").

1. Open the Amazon Connect
   [console](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/")
   (https://console.aws.amazon.com/connect/).
2. Navigate to **Third-party applications** in the left hand
   panel.
3. Choose **Add application**.
4. Fill out the necessary required information:
   1. **Name**: The name of the application
      is what will show up to agents in the app launcher in the agent
      workspace.
   2. **Namespace**: Namespace must be
      unique per application and, in the future, allow for applications to
      support custom events. Once an app is created, its namespace cannot
      be updated.
   3. **AccessUrl**: Set to the localhost
      url for your application.
   4. **Permissions**: A list of allowed
      functions that grants your application the ability to subscribe to
      agent/contact events that occur in the agent workspace or make
      requests for agent/contact workspace data.

5. Select the Amazon Connect instance you are testing with to associate
   the app with that instance.
6. Choose **Add application** to finish creating your
   app.
7. Log into your test instance as an admin user.
8. Navigate to **Security profiles** and select the
   `Admin` security profile.
9. Under **Agent applications** find your application and
   make sure the `View` permission is selected.
   1. Open the agent application `/agent-app-v2`

10. Open your app by choosing the app launcher and selecting your application.
    Your app will be opened in a new application tab.

After following these steps you will have your app loaded from your local machine
into the workspace. This will only work when loading the agent workspace on your
local machine that has the app running on it. If you want to be able to load your
app from any browser / computer, then you must deploy your app somewhere that is
internet accessible.

Assuming the logging was included from the code snippet above, you should see the
following in the console log of your browser’s dev tools when you open your app in
the workspace.

```

App initialized:  00420d405e

```

When your app is closed, for example, by closing the tab in the agent workspace,
you should see the following series of logs entries.

```

> App destroyed: begin
> App being destroyed
> App destroyed
> App destroyed: end

```

If you see these, then your app correctly integrates with the _Amazon Connect SDK_ and the [The
create event in Amazon Connect Agent Workspace](integrating-with-agent-workspace-lifecycle-events-create.md "integrating-with-agent-workspace-lifecycle-events-create.md") /
[The
destroy event in Amazon Connect Agent Workspace](integrating-with-agent-workspace-lifecycle-events-destroy.md "integrating-with-agent-workspace-lifecycle-events-destroy.md")destroy lifecycle events.
