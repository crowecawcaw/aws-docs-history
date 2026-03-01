# Create an Image That Always Uses the Latest Version of the WorkSpaces Applications Agent

When your images are configured to always use the latest WorkSpaces Applications agent version, your streaming instances are automatically updated with the latest features, performance improvements, and security updates that are available from AWS when a new agent version is released.

###### Note

In some cases, a new WorkSpaces Applications agent version might conflict with your software. We recommend that you qualify the new WorkSpaces Applications agent version before deploying it to your production fleets.

###### To create an image that always uses the latest version of the WorkSpaces Applications agent

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").
2. Do either of the following:
   - If you have an image builder that you want to use to create the image,
     start the image builder and then connect to it. If the image builder is
     not running the latest version of the WorkSpaces Applications agent, you are prompted to choose whether to start the image builder with the latest
     agent. Make sure that this option is selected, choose
     **Start**, and then connect to the image
     builder.
   - If you do not have an image builder that you want to use to create the
     image, launch a new image builder. In **Step 1: Choose
     Image**, choose an AWS base image or a custom image. In
     **Step 2: Configure Image Builder**, if the image
     that you choose is not running the latest version of the WorkSpaces Applications agent,
     the **WorkSpaces Applications** section displays. In the **Agent
     version** list, select the latest agent version. Complete
     the remaining steps to create the image builder, and then connect to it.
     For more information, see [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md "tutorial-image-builder-create.md").

3. On the image builder desktop, open Image Assistant and follow the steps to create
   your new image. For the **Configure Image** step, make sure that **Always use the latest agent
   version** is selected. For more information, see [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md "tutorial-image-builder.md").

If you decide later to not always use the latest version of the WorkSpaces Applications agent, you must create a new image and clear that option. 4. Create a new fleet or modify an existing one. When you configure the fleet, select the new
image that you created. For more information, see [Create an Amazon WorkSpaces Applications Fleet and Stack](set-up-stacks-fleets.md "set-up-stacks-fleets.md"). 5. Create a new stack or modify an existing one and associate it with your fleet.
