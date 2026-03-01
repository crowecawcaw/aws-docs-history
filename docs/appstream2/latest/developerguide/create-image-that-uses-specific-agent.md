# Create an Image That Uses a Specific Version of the WorkSpaces Applications Agent

You may want to control WorkSpaces Applications agent updates rather than always using the latest
version so that you can test for compatibility first. To ensure that the version of the
WorkSpaces Applications agent you use is compatible with your streaming applications, you can create an
image that uses a specific version of the agent software. Then perform your
qualification tests in a separate fleet before deploying to your production fleet.

When you create the image, make sure that the **Always use latest agent
version** option is not selected. Doing so pins your image to the version
of the WorkSpaces Applications agent that you selected when you launched the image builder, rather than
always using the latest version. After you finish your qualification tests, you can
update your production fleet with the image.

###### To create an image that uses a specific version of the WorkSpaces Applications agent

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").
2. Do either of the following:
   - If you have an image builder that you want to use to create the image,
     start the image builder and then connect to it.
   - If you do not have an image builder that you want to use to create the
     image, launch a new image builder. In **Step 1: Choose
     Image**, choose an AWS base image or a custom image. In
     **Step 2: Configure Image Builder**, if the image
     that you choose is not running the latest version of the WorkSpaces Applications agent,
     the **WorkSpaces Applications** section displays. In the **Agent
     version** list, do not select the latest agent version.
     Complete the remaining steps to create the image builder, and then
     connect to it. For more information, see [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md "tutorial-image-builder-create.md").

3. On the image builder desktop, open Image Assistant and follow the steps to create
   your new image. For the **Configure Image** step in Image
   Assistant, make sure that **Always use the latest agent
   version** is not selected. For more information, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md").

If you decide later to always use the latest version of the WorkSpaces Applications agent, you must create a new image and select that option. 4. Create a new fleet or modify an existing one. When you configure the fleet, select the new
image that you created. For more information, see [Create an Amazon WorkSpaces Applications Fleet and Stack](set-up-stacks-fleets.md "set-up-stacks-fleets.md"). 5. Create a new stack or modify an existing one and associate it with your fleet. 6. Connect to your fleet and test your applications for compatibility.
