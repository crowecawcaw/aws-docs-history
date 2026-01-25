# Tutorial: Create an image

pipeline with output Docker container image from the Image Builder console wizard

This tutorial walks you through creating an automated pipeline to build and maintain a
customized EC2 Image Builder Docker image using the **Create image pipeline** console
wizard. To help you move through the steps efficiently, default settings are used when they
are available, and optional sections are skipped.

###### Create image pipeline workflow

- [Step 1: Specify pipeline details](#start-build-container-step1 "#start-build-container-step1")
- [Step 2: Choose recipe](#start-build-container-step2 "#start-build-container-step2")
- [Step 3: Define infrastructure configuration - optional](#start-build-container-step3 "#start-build-container-step3")
- [Step 4: Define distribution settings - optional](#start-build-container-step4 "#start-build-container-step4")
- [Step 5: Review](#start-build-container-step5 "#start-build-container-step5")
- [Step 6: Clean up](#start-build-container-cleanup "#start-build-container-cleanup")

## Step 1: Specify pipeline details

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. To begin creating your pipeline, choose
   **Create image pipeline**.
3. In the **General** section, enter your
   **Pipeline name** (_required_).
4. In the **Build schedule** section, you can keep the defaults
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
   **Docker image** option to create a container
   pipeline that will produce a Docker image and distribute it to
   Amazon ECR repositories in target Regions.
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
   list of Amazon Linux 2 container images, managed by Amazon, for you to choose from
   for your base image.
   1. From the **Image name** dropdown, choose an
      image.
   2. Keep the default for **Auto-versioning options**
      (**Use latest available OS version**).

   ###### Note

   This setting ensures that your pipeline uses semantic
   versioning for the base image, to detect dependency
   updates for automatically scheduled jobs. To learn more about semantic versioning for Image Builder resources, see
   [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").

5. In the **Components** section, you can choose to not add any components and proceed. If you want to add components,
   in the **Build components – Amazon Linux** panel, you
   can browse through the components listed on the page. Use the pagination control
   in the upper right corner to navigate through additional components that are
   available for your base image OS. You can also search for specific components,
   or create your own build component using the Component manager.

For this tutorial, choose a component that updates Linux with the latest
security updates, as follows:

    1. Filter the results by entering the word `update` in the
     search bar that's located at the top of the panel.
    2. Select the check box for the `update-linux` build
     component.
    3. Scroll down, and in the upper right corner of the **Selected
     components** list, choose **Expand
     all** .
    4. Keep the default for **Versioning options**
     (**Use latest available component version**).


    ###### Note

    This setting ensures that your pipeline uses semantic
     versioning for the selected component, to detect dependency
     updates for automatically scheduled jobs. To learn more about semantic versioning for Image Builder resources, see
     [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").


    If you had selected a component that has input parameters, you would also
     see the parameters in this area. Parameters are not covered in this
     tutorial. For more information about using input parameters in your
     components, and setting them in your recipes, see [Tutorial: Create a custom component with input parameters](tutorial-component-parameters.md "tutorial-component-parameters.md").###### Reorder components (optional)

If you have chosen more than one component to include in your
image, you can use the drag-and-drop action to rearrange them into
the order in which they should run during the build process.

###### Note

CIS hardening components don't follow the standard component ordering rules in Image Builder
recipes. The CIS hardening components always run last to ensure that the benchmark tests run
against your output image.

    1. Scroll back up to the list of available components.
    2. Select the check box for the `update-linux-kernel-mainline`
     build component (or any other component of your choice).
    3. Scroll down to the **Selected components** list, to
     see that there are at least two results.
    4. Newly added components might not have their versioning
     expanded. To expand **Versioning options**,
     you can either choose the arrow next to **Versioning
     options**, or you can toggle the **Expand
     all** switch off and on to expand
     versioning for all of the selected components.
    5. Choose one of the components, and drag it up or down to change the
     order in which the components will run.
    6. To remove the `update-linux-kernel-mainline` component,
     choose `X` from the upper right corner of the component
     box.
    7. Repeat the previous step to remove any other components you might have
     added, leaving only the `update-linux` component
     selected.

6. In the **Dockerfile template** section, select the
   **Use example** option. In the **Content**
   panel, notice the contextual variables where Image Builder places build information
   or scripts, based on your container image recipe.

By default, Image Builder uses the following contextual variables in your
Dockerfile.

 

**parentImage (required)**

At build time, this variable resolves to the base image for your
recipe.

Example:

```
FROM
{{{ imagebuilder:parentImage }}}
```

**environments (required if components are specified)**

This variable will resolves to a script that runs components.

Example:

```
{{{ imagebuilder:environments }}}
```

**components (optional)**

Image Builder resolves build and test component scripts for the components that
the container recipe includes. This variable can be placed anywhere in the
Dockerfile, after the environments variable.

Example:

```
{{{ imagebuilder:components }}}
```

7. In the **Target repository** section, specify the name
   of the Amazon ECR repository that you created as a prerequisite for this tutorial.
   This repository is used as the default setting for the distribution configuration
   in the Region where the pipeline runs (Region 1).

###### Note

The target repository must exist in Amazon ECR for all target Regions
prior to distribution. 8. Choose **Next** to proceed to the next step.

## Step 3: Define infrastructure configuration - optional

Image Builder launches EC2 instances in your account to customize images and run
validation tests. The Infrastructure configuration settings specify infrastructure
details for the instances that will run in your AWS account during the build
process.

In the **Infrastructure configuration** section, the
**Configuration options** default to `Create infrastructure 
 configuration using service defaults`. This creates an IAM role and associated
instance profile that are used by build instances to configure your container images.
You can also create your own custom infrastructure configuration, or use settings that
you have already created. For more information about infrastructure configuration
settings, see [CreateInfrastructureConfiguration](../APIReference/API_CreateInfrastructureConfiguration.md "../APIReference/API_CreateInfrastructureConfiguration.md")
in the _EC2 Image Builder API Reference_.

For this tutorial, we are using the default settings.

- Choose **Next** to proceed to the next step.

## Step 4: Define distribution settings - optional

Distribution settings consist of the target Regions, and the target Amazon ECR repository
name. Output Docker images are deployed to the named Amazon ECR repository in each Region.

In the **Distribution settings** section, the **Configuration
options** default to `Create distribution settings using service
 defaults`. This option will distribute the output Docker image to the Amazon ECR
repository specified in your container recipe for the Region where your pipeline runs (Region 1).
If you choose `Create new distribution settings`, you can override the
ECR repository for the current Region, and add more Regions for distribution.

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

###### Delete the container recipe

1. To see a list of the container recipes created under your
   account, choose **Container recipes**
   from the navigation pane.
2. Select the check box next to **Recipe name**
   to select the recipe that you want to delete.
3. At the top of the **Container recipes**
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
