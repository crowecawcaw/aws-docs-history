# Update the WorkSpaces Applications Agent Software by Using

Managed WorkSpaces Applications Agent Versions

WorkSpaces Applications provides an automated way to update your image builder with newer WorkSpaces Applications agent
software. Doing so enables you to create a new image whenever a new version of the agent
is released. You can then test the image before updating your production fleets. For more information about how to manage the
WorkSpaces Applications agent software, see [Manage WorkSpaces Applications Agent Versions](base-images-agent.md "base-images-agent.md").

###### Note

You're responsible for installing and maintaining the updates for the Windows operating
system, your applications, and their dependencies.

To
keep your WorkSpaces Applications image updated with the latest Windows operating system updates, do one
of the following:

- Install your applications on the latest base image each time a new image is released.
- Install the updates for the Windows operating system, your applications, and their dependencies on an existing image builder.
- Install the updates for the Windows operating system, your applications, and their dependencies on a new image builder from an existing image.
  After you create a new image with the latest Windows operating system, applications and their dependencies, and the WorkSpaces Applications agent software, test the image on a development fleet. After you verify that your applications work as expected, update your production fleet with the new image.
