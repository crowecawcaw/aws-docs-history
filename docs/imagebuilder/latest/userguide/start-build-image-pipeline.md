# Tutorial: Create an image

pipeline with output AMI from the Image Builder console wizard

This tutorial walks you through creating an automated pipeline to build and maintain a
customized EC2 Image Builder image using the **Create image pipeline** console
wizard. To help you move through the steps efficiently, default settings are used when they
are available, and optional sections are skipped.

###### Create image pipeline workflow

- [Step 1: Specify pipeline details](#start-build-image-step1 "#start-build-image-step1")
- [Step 2: Choose recipe](#start-build-image-step2 "#start-build-image-step2")
- [Step 3: Define infrastructure configuration - optional](#start-build-image-step3 "#start-build-image-step3")
- [Step 4: Define distribution settings - optional](#start-build-image-step4 "#start-build-image-step4")
- [Step 5: Review](#start-build-image-step5 "#start-build-image-step5")
- [Step 6: Clean up](#start-build-image-cleanup "#start-build-image-cleanup")

## Step 1: Specify pipeline details

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. To begin creating your pipeline, choose
   **Create image pipeline**.
3. In the **General** section, enter your
   **Pipeline name** (_required_).

###### Tip

Enhanced metadata collection is turned on by default. To ensure
compatibility between components and base images, keep it turned on. 4. In the **Build schedule** section, you can keep the defaults
for the **Schedule options**. Note that the **Time
zone** shown for the default schedule is Universal Coordinated Time
(UTC). For more information about UTC time, and to find the offset for your time
zone, see [Time Zone
Abbreviations – Worldwide List](https://www.timeanddate.com/time/zones/ "https://www.timeanddate.com/time/zones/").

For **Dependency update settings**, choose the **Run
pipeline at the scheduled time if there are dependency updates**
option. This setting causes your pipeline to check for updates before starting
the build. If there are no updates, it skips the scheduled pipeline
build.

###### Note

To ensure that your pipeline recognizes dependency updates and builds as
expected, you must use semantic versioning (x.x.x) for your base image and
components. To learn more about semantic versioning for Image Builder resources, see
[Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md"). 5. Choose **Next** to proceed to the next step.

## Step 2: Choose recipe

1. Image Builder defaults to **Use existing recipe** in the
   **Recipe** section. For your first time through,
   choose the **Create new recipe** option.
2. In the **Image type** section, choose the
   **Amazon Machine Image (AMI)** option to create
   an image pipeline that will produce and distribute an AMI.
3. In the **General** section, enter the following required
   boxes:
   - **Name** – your recipe name
   - **Version** – your recipe version
     (use the format _<major>.<minor>.<patch>_,
     where major, minor, and patch are integer values). New recipes
     generally start with `1.0.0`.

4. In the **Source image** section, keep the default values for
   **Select image**, **Image Operating System
   (OS)**, and **Image origin**. This results in a
   list of Linux AMIs that are managed by Amazon. For this tutorial, select the
   `Amazon Linux 2 x86` image.
   1. From the **Image name** dropdown, choose an
      image.
   2. Keep the default for **Auto-versioning options**
      (**Use latest available OS version**).

   ###### Note

   This setting ensures that your pipeline uses semantic
   versioning for the base image, to detect dependency
   updates for automatically scheduled jobs. To learn more about semantic versioning for Image Builder resources, see
   [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").

5. In the **Instance configuration** section, keep the default
   values for the **Systems Manager agent**. This results in Image Builder keeping
   the Systems Manager agent after the build and tests are complete, to include the Systems Manager agent
   in your new image.

Keep **User data** blank for this tutorial. You can use this area
at other times to provide commands, or a command script to run when you launch
your build instance. However, it replaces any commands that Image Builder might have
added to ensure that Systems Manager is installed. When you do use it, make sure that the
Systems Manager agent is preinstalled on your base image, or that you include the install
in your user data. 6. In the **Components** section, you can choose to not add any components and proceed. If you want to add components,
in the **Build components** panel, choose
**Add build components**, and select
`Amazon managed` from the component owner filter list. This opens
a selection panel on the right side of the console interface where you can browse
and filter the components that are available.

For this tutorial, choose a component that updates Linux with the latest
security updates, as follows:

    1. Filter the results by entering the word `update` in the
     search bar that's located at the top of the panel.
    2. Select the check box for the `update-linux` build
     component.
    3. Keep the default for **Versioning options**
     (**Use latest version available**).


    ###### Note

    This setting ensures that your pipeline uses semantic
     versioning for the selected component, to detect dependency
     updates for automatically scheduled jobs. To learn more about semantic versioning for Image Builder resources, see
     [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").
    4. Choose **Add to recipe** to add the component to
     your recipe. This closes the component selection panel.
    5. Back in the **Build components** panel, the component
     that you added is displayed.

7. ###### Reorder components (optional)

If you've chosen more than one component to include in your
image, you can use the drag-and-drop action to rearrange them into
the order in which they should run during the build process.

###### Note

CIS hardening components don't follow the standard component ordering rules in Image Builder
recipes. The CIS hardening components always run last to ensure that the benchmark tests run
against your output image.

    1. Repeat the prior steps to add the `update-linux-kernel-5`
     component to your recipe.
    2. The component you just added has an input parameter for the kernel
     version. To expand settings for **Versioning options**
     or **Input parameters**, you can choose the arrow
     next to the name of the setting. To expand all of the settings for
     all selected components, you can toggle the **Expand all**
     switch off and on. For more information about using
     input parameters in your components, and setting them in your recipes,
     see [Tutorial: Create a custom component with input parameters](tutorial-component-parameters.md "tutorial-component-parameters.md").
    3. Choose one of the components, and drag it up or down to change the
     order in which the components will run.
    4. To remove the `update-linux-kernel-5` component,
     choose `X` from the upper right corner of the component
     box.


    Repeat this step to remove any other components you might have
     added, leaving only the `update-linux` component
     selected.

8. Choose **Next** to proceed to the next step.

## Step 3: Define infrastructure configuration - optional

Image Builder launches EC2 instances in your account to customize images and run
validation tests. The Infrastructure configuration settings specify infrastructure
details for the instances that will run in your AWS account during the build
process.

In the **Infrastructure configuration** section, the
**Configuration options** default to `Create infrastructure 
 configuration using service defaults`. This creates an IAM role and associated
instance profile for the EC2 build and test instances that are used to configure your image.
For more information about infrastructure configuration
settings, see [CreateInfrastructureConfiguration](../APIReference/API_CreateInfrastructureConfiguration.md "../APIReference/API_CreateInfrastructureConfiguration.md")
in the _EC2 Image Builder API Reference_.

For this tutorial, we are using the default settings.

###### Note

To specify a subnet to use for a private VPC, you can create your own
custom infrastructure configuration, or use settings that you have already created.

- Choose **Next** to proceed to the next step.

## Step 4: Define distribution settings - optional

Distribution configurations include the output AMI name, specific Region settings
for encryption, launch permissions, and AWS accounts, organizations, and organizational units (OUs)
that can launch the output AMI, and license configurations.

In the **Distribution settings** section, the **Configuration
options** default to `Create distribution settings using service
 defaults`. This option will distribute the output AMI to the current Region.
For more information about configuring your distribution settings, see [Manage Image Builder distribution settings](manage-distribution-settings.md "manage-distribution-settings.md").

For this tutorial, we are using the default settings.

- Choose **Next** to proceed to the next step.

## Step 5: Review

The **Review** section displays all of the settings
you have configured. To edit information in any given section, choose the
**Edit** button located in the top right corner of the
step section. For example, if you want to change your pipeline name,
choose the **Edit** button in the top right corner
of the **Step 1: Pipeline details** section.

1. When you have reviewed your settings, choose
   **Create pipeline** to create your pipeline.
2. You can see success or failure messages at the top of the
   page, as your resources are created for distribution settings,
   infrastructure configuration, your new recipe, and the pipeline.
   To see details for a resource, including the resource identifier,
   choose **View details**.
3. After you have viewed the details for a resource, you can view details about
   other resources by choosing the resource type from the navigation pane. For
   example, to see details for your new pipeline, choose **Image
   pipelines** from the navigation pane. If your build was
   successful, your new pipeline is displayed in the **Image
   pipelines** list.

## Step 6: Clean up

Your Image Builder environment, just like your home, needs
regular maintenance to help you find what you need, and complete your tasks without
wading through clutter. Make sure to regularly clean up temporary resources that you
created for testing. Otherwise, you might forget about those resources, and then later,
not remember what they were used for. By then, it might not be clear if you can safely get rid of them.

###### Tip

To prevent dependency errors when you delete resources, make sure to delete your
resources in the following order:

1. Image pipeline
2. Image recipe
3. All remaining resources

To clean up the resources that you created for this tutorial, follow these steps:

###### Delete the pipeline

1. To see a list of the build pipelines created under your
   account, choose **Image pipelines**
   from the navigation pane.
2. Select the check box next to **Pipeline name**
   to select the pipeline that you want to delete.
3. At the top of the **Image pipelines**
   panel, on the **Actions** menu, choose
   **Delete**.
4. To confirm the deletion, enter `Delete` in the box,
   and choose **Delete**.

###### Delete the recipe

1. To see a list of the recipes created under your
   account, choose **Image recipes**
   from the navigation pane.
2. Select the check box next to **Recipe name**
   to select the recipe that you want to delete.
3. At the top of the **Image recipes**
   panel, on the **Actions** menu,
   choose **Delete recipe**.
4. To confirm the deletion, enter `Delete` in the box,
   and choose **Delete**.

###### Delete infrastructure configuration

1. To see a list of the infrastructure configurations created
   under your account, choose **Infrastructure
   configuration** from the navigation pane.
2. Select the check box next to **Configuration name**
   to select the infrastructure configuration that you want to delete.
3. At the top of the **Infrastructure configurations**
   panel, choose **Delete**.
4. To confirm the deletion, enter `Delete` in the box,
   and choose **Delete**.

###### Delete distribution settings

1. To see a list of the distribution settings created
   under your account, choose **Distribution
   settings** from the navigation pane.
2. Select the check box next to **Configuration name**
   to select the distribution settings that you created
   for this tutorial.
3. At the top of the **Distribution settings**
   panel, choose **Delete**.
4. To confirm the deletion, enter `Delete` in the box,
   and choose **Delete**.

###### Delete the image

Follow these steps to verify that you have deleted any image
that was created from the tutorial pipeline. This tutorial is not
likely to create an image unless enough time has elapsed since you
created your pipeline that it runs, according to the build schedule.

1. To see a list of the images created under your account,
   choose **Images** from the
   navigation pane.
2. Choose the image **Version** for
   the image that you want to remove. This opens the
   **Image build versions** page.
3. Select the check box next to the **Version**
   for any image that you want to delete. You can select more than one
   image version at a time.
4. At the top of the **Image build versions**
   panel, choose **Delete version**.
5. To confirm the deletion, enter `Delete` in the box,
   and choose **Delete**.
