

# Test your application for Connect Customer agent workspace locally
<a name="getting-started-testing"></a>

Once you have a minimal version of the app that you want to use in the Connect Customer agent workspace with the Connect Customer SDK that you want to test in the agent workspace, run your app locally and create an application in the AWS console with an * AccessUrl* using the localhost endpoint, like `http://localhost:3000` .

## Creating an application and associating to your instance
<a name="getting-started-testing-create-an-application"></a>

**Note**  
Detailed steps for creating and managing applications can be found in the admin guide under [Integrate third-party applications in the agent workspace](https://docs.aws.amazon.com/connect/latest/adminguide/3p-apps.html).

1. Run your application locally.

1. Create an integration whose access URL is your localhost endpoint, for example `http://localhost:3000`. For the procedure, see [Integrate third-party applications in the agent workspace](https://docs.aws.amazon.com/connect/latest/adminguide/3p-apps.html) in the *Connect Customer Administrator Guide*.

1. Associate the integration with the Connect Customer instance that you are testing with.

1. Grant your user the `View` permission for the application in a security profile. See [Assign permissions](https://docs.aws.amazon.com/connect/latest/adminguide/assign-security-profile-3p-apps.html) in the *Connect Customer Administrator Guide*.

1. Open the agent workspace at `/agent-app-v2`, and open your application from the **Apps** launcher.

After following these steps you will have your app loaded from your local machine into the workspace. This will only work when loading the agent workspace on your local machine that has the app running on it. If you want to be able to load your app from any browser / computer, then you must deploy your app somewhere that is internet accessible.

Assuming the logging was included from the code snippet above, you should see the following in the console log of your browser’s dev tools when you open your app in the workspace.

```
App initialized:  00420d405e    
```

When your app is closed, for example, by closing the tab in the agent workspace, you should see the following series of logs entries.

```
> App destroyed: begin
> App being destroyed
> App destroyed
> App destroyed: end
```

If you see these, then your app correctly integrates with the *Connect Customer SDK* and the [The create event in Connect Customer agent workspace](integrating-with-agent-workspace-lifecycle-events-create.md) / [The destroy event in Connect Customer agent workspace](integrating-with-agent-workspace-lifecycle-events-destroy.md)destroy lifecycle events.