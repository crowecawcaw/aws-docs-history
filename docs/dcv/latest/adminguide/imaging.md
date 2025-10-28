# Step 3: Set up Amazon DCV Server imaging (Optional)

After customizing an [Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") instance, you can capture those changes as an [Amazon Machine Image](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") (AMI). This feature allows you
to launch multiple instances from a single AMI, all with the same configuration, when needed. When you have a requirement to securely stream with a high-performance remote
display protocol, you can add Amazon DCV to your operating system before taking an image of the Amazon EC2 instance. The Amazon DCV configuration is included in your image, allowing you
to separate business units at the image level or set specific DCV configurations on a deployed instance.

For example, if you are deploying several Amazon EC2 instances from a single AMI, you can use automatic console creation for a local user account and delegate Amazon DCV permissions
to the end users. Alternatively, you can also use a Broker, like [Amazon DCV Session Manager](../sm-admin/what-is-sm.md "../sm-admin/what-is-sm.md"), to manage Amazon DCV session creation at scale.

Creating a Amazon DCV AMI can be performed in one of the following two ways:

## Building a Amazon DCV image

First, you must have Amazon DCV installed on your system. If you do not, ensure your system is [supported by Amazon DCV](servers.md#requirements "servers.md#requirements") then follow
the [Installing](setting-up-installing.md "setting-up-installing.md") instructions. Once Amazon DCV is installed and
[configured](manage.md "manage.md"), take an
[AMI](../../../toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.md "../../../toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.md") of the instance.

Alternatively, if you have the Amazon DCV prerequisites met for [Windows](setting-up-installing-winprereq.md "setting-up-installing-winprereq.md")
or [Linux](setting-up-installing-linux-prereq.md "setting-up-installing-linux-prereq.md"), you can run the Amazon-managed Image Builder Amazon DCV
component to install and configure Amazon DCV. The component can be retrieved by performing the following:

1. Navigate to the components page within the [Amazon EC2 Image Builder console](https://console.aws.amazon.com/imagebuilder/home?#/viewComponents "https://console.aws.amazon.com/imagebuilder/home?#/viewComponents").
2. Select the **Filter owner** drop-down menu and select **Quick start (Amazon-managed)**.
3. Use the filter textbox to search for `dcv-server-windows` or `dcv-server-linux`.
4. Select the component’s hyperlink.
5. On the Amazon DCV component page, retrieve the component contents from the **Content** section.
6. Use the [AWS Task Orchestrator and Executor](../../../imagebuilder/latest/userguide/toe-component-manager.md "../../../imagebuilder/latest/userguide/toe-component-manager.md") (AWSTOE) to run the
   component locally on the instance.

###### Note

For more information, see [Get started with AWSTOE](../../../imagebuilder/latest/userguide/toe-get-started.md "../../../imagebuilder/latest/userguide/toe-get-started.md").

For parameter usage within the components, see the section below.

## Adding Amazon DCV to an Image Pipeline

An [EC2 Image Builder recipe](../../../imagebuilder/latest/userguide/manage-recipes.md "../../../imagebuilder/latest/userguide/manage-recipes.md") defines the base image to use as a starting point to create
a new image, along with the set of components that you add to customize the image and verify that everything works as expected. Within this recipe, select the `dcv-server-windows`
or `dcv-server-linux` component to automate the installation of Amazon DCV within your pipeline. When selecting one of these components, you can fine tune the parameters to meet your requirements.

###### Note

For Linux, all [prerequisites](../../../en_us/dcv/latest/adminguide/setting-up-installing-linux-prereq.md "../../../en_us/dcv/latest/adminguide/setting-up-installing-linux-prereq.md")
need to be met. This can be done on the base AMI or in preceding Image Builder components.

### Parameters

###### Windows

- `sessionOwner`—Sets the default owner of the automatically created session. If not specified, automatic console creation will be disabled. For more information,
  see the [Enabling Automatic Console Sessions](managing-sessions-start.md#managing-sessions-start-auto "managing-sessions-start.md#managing-sessions-start-auto") in the Amazon DCV Administration Guide.
- `dcvPermissions`—Sets the Amazon DCV permissions of your session. For more information, see [Working with permissions files](security-authorization-file-create.md "security-authorization-file-create.md")
  in the DCV Administration Guide.

###### Linux

- `SessionOwner`—Sets the default owner of the automatically created session. If not specified, automatic console creation will be disabled. For more information,
  see the [Enabling Automatic Console Sessions](managing-sessions-start.md#managing-sessions-start-auto "managing-sessions-start.md#managing-sessions-start-auto") in the Amazon DCV Administration Guide.
- `Packages`—Defines the Amazon DCV packages that will be installed. If empty, all available Amazon DCV packages are installed. For more information, see the
  [Install the Amazon DCV Server on Linux](setting-up-installing-linux-server.md "setting-up-installing-linux-server.md") in the Amazon DCV Administration Guide.

If you would like to modify the component, you may [create a new component](../../../imagebuilder/latest/userguide/create-component-console.md "../../../imagebuilder/latest/userguide/create-component-console.md") version.
