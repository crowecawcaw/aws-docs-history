# Code examples for Deadline Cloud

The [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples")
GitHub repository contains a collection of working artifacts for AWS Deadline Cloud. The
examples cover job submission, software packaging, infrastructure deployment,
worker configuration, and more. You can submit, deploy, or adapt them for your
own farms.

The following sections describe each category of example and link to
individual topics that explain when to use each one.

**Tutorials**

Complete walkthroughs that take you from prerequisites to a working
result on a real workload. Each tutorial covers prerequisites, step-by-step
instructions, parameter references, and cleanup.

For details, see [Tutorials for Deadline Cloud](examples-tutorials.md "examples-tutorials.md").

**Job bundle examples**

Job bundles define jobs that you submit to a Deadline Cloud queue. The repository
includes job bundles for digital content creation (DCC) renderers such as Maya,
Blender, Houdini, Nuke, 3ds Max, Cinema 4D, KeyShot, and VRED. It also includes
machine learning workloads, multi-step rendering pipelines, and small examples
that demonstrate individual concepts such as job parameters, environments, and
job attachments.

For details, see [Job bundle examples for Deadline Cloud](examples-job-bundles.md "examples-job-bundles.md").

**Conda recipe examples**

Conda recipes build conda packages that supply applications and plugins to
your jobs through a queue environment. The repository includes recipes for many
versions of Maya, Blender, Houdini, Nuke, 3ds Max, Cinema 4D, KeyShot, and
Unreal Engine, along with renderer plugins such as Arnold, V-Ray, and
Redshift.

For details, see [Conda recipe examples for Deadline Cloud](examples-conda-recipes.md "examples-conda-recipes.md").

**CloudFormation template examples**

CloudFormation templates deploy farms and supporting infrastructure. The repository
includes a starter farm template, templates for connecting service-managed
fleets to private VPC resources, and templates for capacity management,
standby scheduling, fleet health checks, and budget notifications.

For details, see [CloudFormation template examples for Deadline Cloud](examples-cloudformation.md "examples-cloudformation.md").

**Host configuration script examples**

Host configuration scripts run with elevated privileges on
service-managed fleet workers to install software, configure GPU runtimes for
containers, install fonts, enable swap, and perform other administrative
tasks. You attach a script to a fleet through the Deadline Cloud console or the
`update-fleet` CLI command.

For details, see [Host configuration script examples for Deadline Cloud](examples-host-config.md "examples-host-config.md").

**Queue environment examples**

Queue environments provide software applications to your jobs. The repository
includes several conda-based queue environments with different performance
trade-offs, a Rez-based queue environment for customer-managed fleets that have
a shared file system, a pip-based queue environment for Python-only packages,
and a queue environment that disconnects usage-based licensing so you can use
a custom license server.

For details, see [Queue environment examples for Deadline Cloud](examples-queue-environments.md "examples-queue-environments.md").

**Other examples**

The repository also includes the following examples:

- [Build a worker-equivalent Amazon Linux 2023 Docker image for Deadline Cloud](examples-container-al2023.md "examples-container-al2023.md") — A Dockerfile that
  replicates the package set of the Deadline Cloud service-managed fleet (SMF) worker
  AMI on Amazon Linux 2023.
- [Build a Blender Docker image for GPU rendering on Deadline Cloud](examples-container-blender.md "examples-container-blender.md") — A Dockerfile that
  packages Blender with the OpenJD adaptor and GPU support for Cycles
  rendering in a container.
- [Upload files to Deadline Cloud job attachments](examples-upload-to-job-attachments.md "examples-upload-to-job-attachments.md") — A script
  that uploads files and directories from your workstation or server to
  Deadline Cloud job attachments storage.
- [Set up a virtual workstation for Deadline Cloud with a script](examples-virtual-workstation.md "examples-virtual-workstation.md") — Scripts
  that turn a fresh Linux or Windows workstation into a Deadline Cloud
  submission machine with a DCC, the submitter, and a pre-configured
  monitor profile.
- [Enforce fixed license limits with a Deadline Cloud submission hook](examples-license-limits-hook.md "examples-license-limits-hook.md") — A submission
  hook that enforces fixed license limits by combining the Deadline Cloud Limits
  feature with a pre-submission hook.
- [AI agent skills for Deadline Cloud](examples-skills.md "examples-skills.md") — Reusable AI agent
  skills that walk an agent through writing job bundles, building
  conda packages, and creating Windows host configuration
  scripts.
  **Additional resources**

The following resources help you author and run your own examples in
Deadline Cloud.

- [Open Job Description (OpenJD) templates for Deadline Cloud](build-job-bundle.md "build-job-bundle.md") — Learn how to author your
  own job bundles for Deadline Cloud.
- [Using AI agents with Deadline Cloud](ai-agents.md "ai-agents.md") — Use AI agents to write job
  bundles, develop conda packages, and troubleshoot jobs.
- [Open
  Job Description specifications](https://github.com/OpenJobDescription/openjd-specifications "https://github.com/OpenJobDescription/openjd-specifications") on GitHub — The schema and
  reference for job templates that Deadline Cloud runs.
- [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples")
  on GitHub — The source repository for all of the examples in this
  chapter.

###### Topics

- [Tutorials for Deadline Cloud](examples-tutorials.md "examples-tutorials.md")
- [Job bundle examples for Deadline Cloud](examples-job-bundles.md "examples-job-bundles.md")
- [Conda recipe examples for Deadline Cloud](examples-conda-recipes.md "examples-conda-recipes.md")
- [CloudFormation template examples for Deadline Cloud](examples-cloudformation.md "examples-cloudformation.md")
- [Deploy Deadline Cloud farms with the AWS CDK](examples-cdk.md "examples-cdk.md")
- [Deploy Deadline Cloud farms with Terraform](examples-terraform.md "examples-terraform.md")
- [Host configuration script examples for Deadline Cloud](examples-host-config.md "examples-host-config.md")
- [Queue environment examples for Deadline Cloud](examples-queue-environments.md "examples-queue-environments.md")
- [Build a worker-equivalent Amazon Linux 2023 Docker image for Deadline Cloud](examples-container-al2023.md "examples-container-al2023.md")
- [Build a Blender Docker image for GPU rendering on Deadline Cloud](examples-container-blender.md "examples-container-blender.md")
- [Upload files to Deadline Cloud job attachments](examples-upload-to-job-attachments.md "examples-upload-to-job-attachments.md")
- [Set up a virtual workstation for Deadline Cloud with a script](examples-virtual-workstation.md "examples-virtual-workstation.md")
- [Enforce fixed license limits with a Deadline Cloud submission hook](examples-license-limits-hook.md "examples-license-limits-hook.md")
- [AI agent skills for Deadline Cloud](examples-skills.md "examples-skills.md")
