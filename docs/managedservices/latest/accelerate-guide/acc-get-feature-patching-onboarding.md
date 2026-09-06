

# Onboarding patching in Accelerate
<a name="acc-get-feature-patching-onboarding"></a>

You need to configure patching to ensure that your software is up-to-date and meets your compliance policies.

**AWS Backup prerequisite: ** To allow creation of a root volume snapshot during the patching maintenance window, ensure that AWS Backup is enabled for each account and region for the *Amazon EBS* resource type by following the steps here: [Getting started 1: Service Opt-in](https://docs.aws.amazon.com/aws-backup/latest/devguide/service-opt-in.html). (You do not need to continue to *Getting started 2: Create an on-demand backup*.) 

**When to patch: ** Patching occurs during a *maintenance window*. You can schedule maintenance windows so that patches are only applied during preset times.

**What to patch: ** You have to associate the Amazon EC2 instances you want to patch with a maintenance window. To associate the instances with a maintenance window, the Amazon EC2 instances must be tagged, and the maintenance window should have those tags as a target.

**Which patches to install**: Using patch baselines, you set rules to auto-approve certain types of patches, such as operating system or high-severity patches. You can also specify exceptions to your rules, for example, lists of patches that are always approved or rejected.

See [Patching recommendations](acc-patching.md#acc-patching-recos) for guidance with Amazon EC2 patch policies. 
+ To start configuring patch management, see [Understand patch management in AMS Accelerate](acc-patching.md)
+ To create a custom patch configuration, see [Custom patch baseline with AMS Accelerate](acc-patch-baseline-custom.md).