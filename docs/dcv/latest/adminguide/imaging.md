

# Step 3: Set up Amazon DCV Server imaging (Optional)
<a name="imaging"></a>

 After customizing an [Amazon EC2](https://aws.amazon.com/ec2/) instance, you can capture those changes as an [Amazon Machine Image]( https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMI). This feature allows you to launch multiple instances from a single AMI, all with the same configuration, when needed. When you have a requirement to securely stream with a high-performance remote display protocol, you can add Amazon DCV to your operating system before taking an image of the Amazon EC2 instance. The Amazon DCV configuration is included in your image, allowing you to separate business units at the image level or set specific DCV configurations on a deployed instance. 

 For example, if you are deploying several Amazon EC2 instances from a single AMI, you can use automatic console creation for a local user account and delegate Amazon DCV permissions to the end users. Alternatively, you can also use a Broker, like [Amazon DCV Session Manager](https://docs.aws.amazon.com/dcv/latest/sm-admin/what-is-sm.html), to manage Amazon DCV session creation at scale. 

 Creating a Amazon DCV AMI can be performed in one of the following two ways: 

## Building a Amazon DCV image
<a name="building-image"></a>

 First, you must have Amazon DCV installed on your system. If you do not, ensure your system is [supported by Amazon DCV](https://docs.aws.amazon.com/dcv/latest/adminguide/servers.html#requirements) then follow the [Installing](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing.html) instructions. Once Amazon DCV is installed and [configured](https://docs.aws.amazon.com/dcv/latest/adminguide/manage.html), take an [AMI](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html) of the instance. 

 Alternatively, if you have the Amazon DCV prerequisites met for [Windows](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-winprereq.html) or [Linux](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-linux-prereq.html), you can run the Amazon-managed Image Builder Amazon DCV component to install and configure Amazon DCV. The component can be retrieved by performing the following: 

1. Navigate to the components page within the [Amazon EC2 Image Builder console](https://console.aws.amazon.com/imagebuilder/home?#/viewComponents).

1. Select the **Filter owner** drop-down menu and select **Quick start (Amazon-managed)**.

1. Use the filter textbox to search for `dcv-server-windows` or `dcv-server-linux`.

1. Select the component’s hyperlink.

1. On the Amazon DCV component page, retrieve the component contents from the **Content** section.

1. Use the [AWS Task Orchestrator and Executor](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-component-manager.html) (AWSTOE) to run the component locally on the instance.
**Note**  
For more information, see [Get started with AWSTOE](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-get-started.html).

For parameter usage within the components, see the section below.

## Adding Amazon DCV to an Image Pipeline
<a name="adding-image-to-pipeline"></a>

An [EC2 Image Builder recipe](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-recipes.html) defines the base image to use as a starting point to create a new image, along with the set of components that you add to customize the image and verify that everything works as expected. Within this recipe, select the `dcv-server-windows` or `dcv-server-linux` component to automate the installation of Amazon DCV within your pipeline. When selecting one of these components, you can fine tune the parameters to meet your requirements.

**Note**  
For Linux, all [prerequisites](https://docs.aws.amazon.com/en_us/dcv/latest/adminguide/setting-up-installing-linux-prereq.html) need to be met. This can be done on the base AMI or in preceding Image Builder components. 

### Parameters
<a name="imaging-parameters"></a>

**Windows**
+ `sessionOwner`—Sets the default owner of the automatically created session. If not specified, automatic console creation will be disabled. For more information, see the [Enabling Automatic Console Sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-sessions-start.html#managing-sessions-start-auto) in the Amazon DCV Administration Guide.
+ `dcvPermissions`—Sets the Amazon DCV permissions of your session. For more information, see [Working with permissions files](https://docs.aws.amazon.com/dcv/latest/adminguide/security-authorization-file-create.html) in the DCV Administration Guide. 

**Linux**
+ `SessionOwner`—Sets the default owner of the automatically created session. If not specified, automatic console creation will be disabled. For more information, see the [Enabling Automatic Console Sessions](https://docs.aws.amazon.com/dcv/latest/adminguide/managing-sessions-start.html#managing-sessions-start-auto) in the Amazon DCV Administration Guide.
+ `Packages`—Defines the Amazon DCV packages that will be installed. If empty, all available Amazon DCV packages are installed. For more information, see the [Install the Amazon DCV Server on Linux](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-installing-linux-server.html) in the Amazon DCV Administration Guide.

If you would like to modify the component, you may [create a new component](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-component-console.html) version.