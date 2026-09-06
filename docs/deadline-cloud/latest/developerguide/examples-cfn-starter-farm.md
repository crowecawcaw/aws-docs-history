

# Deploy a starter Deadline Cloud farm with CloudFormation
<a name="examples-cfn-starter-farm"></a>

The starter\_farm CloudFormation template deploys a Deadline Cloud farm that you can use to run jobs that render images, reconstruct 3D scenes, or transform data. For the template source, see [starter\_farm](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/starter_farm) on the GitHub website. The deployed farm includes:
+ One or more [service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-manage.html) that you select during deployment.
+ A production queue with conda virtual environments for the applications that jobs need.
+ A package build queue that you can use to build conda packages.
+ Two conda channels by default: a private channel on an Amazon S3 bucket you provide and the [deadline-cloud channel](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html#conda-queue-environment), which provides applications such as Blender, Houdini, Maya, and Nuke.

To deploy the template, you need an Amazon S3 bucket to hold job attachments and the conda channel, and a Deadline Cloud monitor with IAM Identity Center to view and manage jobs.

From the CloudFormation console, choose *Create Stack*, upload `deadline-cloud-starter-farm-template.yaml`, enter a stack name and the Amazon S3 bucket name, and proceed through stack creation. To use conda-forge, set the `ProdCondaChannels` parameter to `deadline-cloud conda-forge`. For more information, see [conda-forge](https://conda-forge.org/) on the conda-forge website.