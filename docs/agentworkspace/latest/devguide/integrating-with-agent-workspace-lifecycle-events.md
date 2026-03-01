# Application lifecycle events in Amazon Connect Agent Workspace

There are lifecycle states that an app can move between from when the app is
initially opened to when it is closed in the Amazon Connect agent workspace. This
includes the initialization handshake that the app goes through with the agent
workspace after it has loaded to establish the communication channel between the
two. There is another handshake between the agent workspace and the application when
the app will be shutdown. An application can hook into `onCreate` and `onDestroy` when calling `AmazonConnectApp.init()`.

The following section describe the create and destroy events in the Amazon Connect
agent workspace.

###### Topics

- [Create
  event](integrating-with-agent-workspace-lifecycle-events-create.md "integrating-with-agent-workspace-lifecycle-events-create.md")
- [Destroy
  event](integrating-with-agent-workspace-lifecycle-events-destroy.md "integrating-with-agent-workspace-lifecycle-events-destroy.md")
