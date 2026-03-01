# Managing the build configuration for an Amplify application

You can customize the build settings and configuration for your Amplify deployments.
When you deploy an application, Amplify automatically detects the frontend framework and the
associated build settings. You can customize the build settings in the application's build specification (buildspec) to add environment variables, run
build commands, and specify build dependencies.

Amplify's default build image comes with several
packages and dependencies pre-installed, but you can also use the live package updates feature to specify either a
specific version, or ensure that the latest version is always installed. If you have specific dependencies that take a long time to install during a
build using Amplify's default container, you can create your own custom build image. You can also customize the build instance size to provide your application deployment with the CPU, memory, and disk space resources it needs.

Builds are initiated automatically with each commit to your Git repository and with each new
deployment. You can set up the incoming webhooks feature to initiate a build without a commit to
your Git repository.

The build notifications feature allows you to share information with team members about build successes and failures.

###### Topics

- [Configuring the build settings for an Amplify application](build-settings.md "build-settings.md")
- [Customizing the build image](custom-build-image.md "custom-build-image.md")
- [Configuring the build instance for an Amplify application](custom-build-instance.md "custom-build-instance.md")
- [Creating an incoming webhook to start a build](create-incoming-webhook.md "create-incoming-webhook.md")
- [Setting up email notifications for builds](notifications.md "notifications.md")
