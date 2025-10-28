# Update the AppStream 2.0 Agent Software by Using

Managed AppStream 2.0 Agent Versions

AppStream 2.0 provides an automated way to update your image builder with newer AppStream 2.0 agent
software. Doing so enables you to create a new image whenever a new version of the agent
is released. You can then test the image before updating your production fleets. For more information about how to manage the
AppStream 2.0 agent software, see [Manage AppStream 2.0 Agent Versions](base-images-agent.md "base-images-agent.md").

###### Note

You're responsible for installing and maintaining the updates for the Windows operating
system, your applications, and their dependencies.

To
keep your AppStream 2.0 image updated with the latest Windows operating system updates, do one
of the following:

- Install your applications on the latest base image each time a new image is released.
- Install the updates for the Windows operating system, your applications, and their dependencies on an existing image builder.
- Install the updates for the Windows operating system, your applications, and their dependencies on a new image builder from an existing image.
  After you create a new image with the latest Windows operating system, applications and their dependencies, and the AppStream 2.0 agent software, test the image on a development fleet. After you verify that your applications work as expected, update your production fleet with the new image.
