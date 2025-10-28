# Configuring the build settings for an Amplify application

When you deploy an application, Amplify automatically detects the frontend framework and
associated build settings by inspecting the app's `package.json` file in your Git
repository. You have the following options for storing your app's build settings:

- Save the build settings in the Amplify console - The Amplify console autodetects
  build settings and saves them so that they can be accessed by the Amplify console.
  Amplify applies these settings to all of your branches unless there is an
  `amplify.yml` file stored in your repository.
- Save the build settings in your repository - Download the
  `amplify.yml` file and add it to the root of your repository.

###### Note

**Build settings** is visible in the Amplify console's
**Hosting** menu only when an app is set up for continuous deployment and
connected to a git repository. For instructions on this type of deployment, see [Getting started](getting-started.md "getting-started.md").
