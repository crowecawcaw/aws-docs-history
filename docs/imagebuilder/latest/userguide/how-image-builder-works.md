# How EC2 Image Builder works

When you use the EC2 Image Builder console to create a custom image pipeline, the system
guides you through the following steps.

1. **Specify pipeline details** – Enter
   information about your pipeline, such as a name, description, tags, and a schedule
   to run automated builds. You can choose manual builds, if you prefer.
2. **Choose recipe** – Choose between building an
   AMI, or building a container image. For both types of output images, you enter a
   name and version for your recipe, select a base image, and choose components to
   add for building and testing. You can also choose automatic versioning, to ensure
   that you always use the latest available Operating System (OS) version for your
   base image. Container recipes additionally define Dockerfiles, and the target
   Amazon ECR repository for your output Docker container image.

###### Note

Components are the building blocks that are consumed by an image
recipe or a container recipe. For example, packages for installation,
security hardening steps, and tests. The selected base image and
components make up an image recipe. 3. **Define infrastructure configuration** – Image Builder
launches EC2 instances in your account to customize images and run validation
tests. The Infrastructure configuration settings specify infrastructure details for
the instances that will run in your AWS account during the build process. 4. **Define distribution settings** – Choose the
AWS Regions to distribute your image to after the build is complete and has passed
all its tests. The pipeline automatically distributes your image to the Region where
it runs the build, and you can add image distribution for other Regions.
The images that you build from your custom base image are in your AWS account. You can
configure your image pipeline to produce updated and patched versions of your image by
entering a build schedule. When the build is complete, you can receive notification through
[Amazon Simple Notification
Service (SNS)](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md"). In addition to producing a final image, the Image Builder console wizard
generates a recipe that can be used with existing version control systems and continuous
integration/continuous deployment (CI/CD) pipelines for repeatable automation. You can share
and create new versions of your recipe.

###### Section contents

- [AMI elements](#ami-image-elements "#ami-image-elements")
- [Component management](#ibhow-component-management "#ibhow-component-management")
- [Resources created](#image-builder-resources "#image-builder-resources")
- [Distribution](#image-builder-distribution "#image-builder-distribution")
- [Sharing Resources](#ibhow-sharing "#ibhow-sharing")
- [Compliance](#ibhow-compliance "#ibhow-compliance")

## AMI elements

An Amazon Machine Image (AMI) is a preconfigured virtual machine (VM) image that
contains the OS and software to deploy EC2 instances.

An AMI includes the following elements:

- A template for the root volume of the VM. When you launch an Amazon EC2 VM, the root
  device volume contains the image to boot the instance. When instance store is
  used, the root device is an instance store volume created from a template in
  Amazon S3. For more information, see [Amazon EC2
  Root Device Volume](../../../AWSEC2/latest/UserGuide/RootDeviceStorage.md "../../../AWSEC2/latest/UserGuide/RootDeviceStorage.md").
- When Amazon EBS is used, the root device is an EBS volume created from an [EBS
  snapshot](../../../ebs/latest/userguide/ebs-snapshots.md "../../../ebs/latest/userguide/ebs-snapshots.md").
- Launch permissions that determine the AWS accounts that can launch VMs with
  the AMI.
- [Block device mapping](../../../AWSEC2/latest/UserGuide/block-device-mapping-concepts.md "../../../AWSEC2/latest/UserGuide/block-device-mapping-concepts.md") data that specifies the volumes to attach to
  the instance after launch.
- A unique [resource
  identifier](../../../AWSEC2/latest/UserGuide/resource-ids.md "../../../AWSEC2/latest/UserGuide/resource-ids.md") for each Region, for each account.
- [Metadata](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md") payloads such as tags, and properties, such as Region,
  operating system, architecture, root device type, provider, launch permissions,
  storage for the root device, and signing status.
- An AMI signature for Windows images to protect against unauthorized tampering. For more
  information, see [Instance Identity Documents](../../../AWSEC2/latest/WindowsGuide/instance-identity-documents.md "../../../AWSEC2/latest/WindowsGuide/instance-identity-documents.md").

## Component management

EC2 Image Builder uses a component management application AWS Task Orchestrator and Executor (AWSTOE) that helps you orchestrate
complex workflows, modify system configurations, and test your systems with YAML-based
script components. Because AWSTOE is a standalone application, it does not require any
additional setup. It can run on any cloud infrastructure and on premises. To get started
using AWSTOE as a standalone application, see [Manual set up to develop custom components with AWSTOE](toe-get-started.md "toe-get-started.md").

Image Builder uses AWSTOE to perform all on-instance activities. These include building and validating
your image before taking a snapshot, and testing the snapshot to ensure that it functions as
expected before creating the final image. For more information about how Image Builder uses AWSTOE to
manage its components, see [Use components to customize your Image Builder image](manage-components.md "manage-components.md"). For more information about creating components with
AWSTOE, see [How Image Builder uses the AWS Task Orchestrator and Executor application to manage components](toe-component-manager.md "toe-component-manager.md").

### Image testing

You can use AWSTOE test components to validate your image, and ensure that it
functions as expected, prior to creating the final image.

Generally, each test component consists of a YAML document that contains a test script, a
test binary, and test metadata. The test script contains the orchestration commands to
start the test binary, which can be written in any language supported by the OS. Exit
status codes indicate the test outcome. Test metadata describes the test and its
behavior; for example, the name, description, paths to test binary, and expected
duration.

## Resources created

When you create a pipeline, no resources external to Image Builder are created, unless the
following is true:

- When an image is created through the pipeline schedule
- When you choose **Run Pipeline**
  from the **Actions** menu in the Image Builder console
- When you run either of these commands from the API or AWS CLI:
  **StartImagePipelineExecution** or
  **CreateImage**

The following resources are created during the image build process:

###### AMI image pipelines

- EC2 instance (_temporary_)
- Systems Manager Inventory Association (through Systems Manager State Manager if
  `EnhancedImageMetadata` is Enabled) on the EC2 instance
- Amazon EC2 AMI
- The Amazon EBS Snapshot associated with Amazon EC2 AMI

###### Container image pipelines

- Docker container running on an EC2 instance
  (_temporary_)
- Systems Manager Inventory Association (through Systems Manager State Manager)
  `EnhancedImageMetadata` is Enabled) on the EC2 instance
- Docker container image
- Dockerfile

After the image has been created, all of the temporary
resources are deleted.

## Distribution

EC2 Image Builder can distribute AMIs or container images to any AWS Region. The image is
copied to each Region that you specify in the account used to build the image.

For AMI output images, you can define AMI launch permissions to control
which AWS accounts are permitted to launch EC2 instances with the
created AMI. For example, you can make the image private, public, or share
with specific accounts. If you both distribute the AMI to other Regions, and
define launch permissions for other accounts, the launch permissions are
propagated to the AMIs in all of the Regions in which the AMI is distributed.

You can also use your AWS Organizations account to enforce
limitations on member accounts to launch instances only with approved and
compliant AMIs. For more information, see [Managing the AWS accounts in Your Organization](../../../organizations/latest/userguide/orgs_manage_accounts.md "../../../organizations/latest/userguide/orgs_manage_accounts.md").

To update your distribution settings using the Image Builder console, follow the steps to
[Create a new image recipe version from the console](create-image-recipes.md#create-image-recipe-version-console "create-image-recipes.md#create-image-recipe-version-console"), or
[Create a new container recipe version
with the console](create-container-recipes.md#create-container-recipe-version "create-container-recipes.md#create-container-recipe-version").

## Sharing Resources

To share components, recipes, or images with other accounts or within AWS Organizations,
see [Share Image Builder resources with AWS RAM](manage-shared-resources.md "manage-shared-resources.md").

## Compliance

For Center for Internet Security (CIS) Benchmarks, EC2 Image Builder uses Amazon Inspector to perform
assessments for exposure, vulnerabilities, and
deviations from best practices and compliance standards. For example, Image Builder assesses
unintended network accessibility, unpatched CVEs, public internet connectivity, and
remote root login activation. Amazon Inspector is offered as a test component that you can choose
to add to your image recipe. For more information about Amazon Inspector, see
the _[Amazon Inspector](../../../inspector/v1/userguide/inspector_introduction.md "../../../inspector/v1/userguide/inspector_introduction.md") User
Guide_. For
more information, see [Center for
Internet Security (CIS) Benchmarks](../../../inspector/latest/userguide/inspector_cis.md "../../../inspector/latest/userguide/inspector_cis.md").

Image Builder provides STIG hardening components to help you more efficiently build compliant images
for baseline STIG standards. These STIG components scan for misconfigurations and run a remediation
script. There are no additional charges for using STIG-compliant components. For a
complete list of STIG components available through Image Builder, see [Amazon managed STIG hardening components for Image Builder](ib-stig.md "ib-stig.md").
