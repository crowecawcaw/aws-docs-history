

# Perform blue/green updates for compute environments
<a name="blue-green-updates"></a>

A blue/green update is an update strategy that reduces downtime and risk by creating a new compute environment (green) alongside your existing compute environment (blue). This approach allows you to gradually transition workloads to the new environment while keeping the existing environment operational. Blue/green updates provide the safest update path and work with any service role type or allocation strategy.

## Overview
<a name="blue-green-overview"></a>

Blue/green updates offer several advantages that make them ideal for production environments. They provide *zero downtime* by keeping your workloads running continuously during the update process. The approach enables *easy rollback* capabilities, allowing you to quickly revert to the original environment if issues arise. You can implement a *gradual transition* strategy, verifying the new environment's performance before fully switching over your production workloads. This method also provides excellent *risk mitigation* since the original environment remains unchanged and operational until you choose to remove it.

### When blue/green updates are required
<a name="blue-green-when-required"></a>

You must use blue/green updates in the following situations:
+ When your compute environment uses `BEST_FIT` allocation strategy (doesn't support infrastructure updates).
+ When your compute environment doesn't use the *AWSServiceRoleForBatch* service-linked role.
+ When you need to transition between different service role types.

### When blue/green updates are recommended
<a name="blue-green-when-recommended"></a>

We recommend blue/green updates for production environments where zero downtime is critical for your workloads. This approach works well when you need to test new configurations before transitioning production workloads, ensuring that changes meet your performance and reliability requirements. Choose blue/green updates when quick rollback capability is important for your operations, especially if you're updating custom AMIs with significant changes. This method is also ideal when you want to validate performance characteristics and behavior before fully committing to changes, providing confidence in your update process.

### Prerequisites
<a name="blue-green-prerequisites"></a>

Before performing a blue/green update, ensure you have:
+ Appropriate [IAM permissions](IAM_policies.md) to create and manage compute environments.
+ Access to view and modify job queue settings.
+ Job retry strategies configured for your job definitions to handle potential failures during the transition. For more information, see [Automated job retries](job_retries.md).
+ The AMI ID for the new compute environment. This can be either:
  + A recent, approved version of the Amazon ECS optimized AMI (used by default).
  + A custom AMI that meets the Amazon ECS container instance AMI specification. When using a custom AMI, you can specify it in one of these ways:
    + Using the **Image ID override** field in the EC2 configuration.
    + Specifying it in a launch template.

    For more information about creating custom AMIs, see [Tutorial: Create a compute resource AMI](create-batch-ami.md).

Before creating the new environment, you need to record the configuration of your existing compute environment. You can do this using either the AWS Management Console or the AWS CLI. 

**Note**  
The following procedures detail how to perform a blue/green update that only changes the AMI. You can update other settings for the new environment.

**Important**  
When you remove the old (blue) compute environment, any currently running jobs on those instances will fail because the instances will be terminated. Configure job retry strategies in your job definitions to handle these failures automatically. For more information, see [Automated job retries](job_retries.md).  
Once you're confident in the new environment:  
Edit the job queue to remove the old compute environment.
Wait for any running jobs in the old environment to complete.
Delete the old compute environment.

------
#### [ Performing blue/green updates using the AWS Management Console ]

1. Clone your current compute environment

   1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

   1. Select the option next to your existing compute environment. You must select a compute environment before the options in the **Actions** menu become available.

   1. Choose **Actions** and then **Clone**.

   1. For **Name**, enter a unique name for your new compute environment. 

   1. Choose **Next**.

   1. In the **Instance configuration** section, update the AMI settings:

      1. Expand **Additional configuration**.

      1. For **EC2 configuration**, specify the new AMI type in **Image type** and AMI ID in the **Image ID override** field.

   1. Choose **Next**.

   1. For **Network configuration** choose **Next**.

   1. Review the other settings which are automatically copied from your existing environment.

   1. Choose **Create compute environment**.

   1. Wait for the new compute environment status to become `VALID`.

1. Change the job queue order

   1. In the navigation pane, choose **Job queues**.

   1. Select the job queue associated with your existing compute environment.

   1. Choose **Edit**.

   1. Under **Connected Compute environment**, add the new compute environment:
      + Add the new compute environment with a higher order number than the existing environment to transition the workload.
      + Once you verify the new environment is working correctly, you can make it the primary environment by giving it a lower order number.

   1. Choose **Update job queue**.

1. Clean up

   1. Monitor job execution in the new environment to ensure everything is working as expected.

   1. Once you're confident in the new environment:

      1. Edit the job queue to remove the old compute environment.

      1. Wait for any running jobs in the old environment to complete.

      1. Delete the old compute environment.

------
#### [ Performing blue/green updates using the AWS CLI ]

1. To get the configuration using the AWS CLI, use the following command:

   ```
   aws batch describe-compute-environments \
     --compute-environments {{your-compute-environment-name}}
   ```

   Save the output for reference when creating the new environment.

1. Create a new compute environment using the configuration from your existing environment, but with the new AMI. Here's an example command structure:

   Replace the example values with your actual configuration from the previous step:

   ```
   cat <<EOF > ./blue-green-compute-environment.json
   {
     "computeEnvironmentName": "{{your-new-compute-environment-name}}",
     "type": "MANAGED",
     "state": "ENABLED",
     "computeResources": {
       "instanceRole": "arn:aws:iam::{{012345678901}}:instance-profile/ecsInstanceRole",
       "type": "EC2",
       "minvCpus": 2,
       "desiredvCpus": 2,
       "maxvCpus": 256,
       "instanceTypes": [
         "optimal"
       ],
       "allocationStrategy": "BEST_FIT_PROGRESSIVE",
       "ec2Configuration": [
         {
           "imageType": "ECS_AL2023",
           "imageIdOverride": "{{ami-0abcdef1234567890}}"
         }
       ],
       "subnets": [,
         "{{subnet-0abcdef1234567890}}"
       ],
       "securityGroupIds": [
         "{{sg-0abcdef1234567890"}}
       ]
     }
   }
   EOF
   ```

   ```
   $ aws batch create-compute-environment --cli-input-json file://./blue-green-compute-environment.json
   ```

1. Wait for the new environment to become available:

   ```
   aws batch describe-compute-environments \
     --compute-environments {{your-new-compute-environment-name}} \
     --query 'computeEnvironments[].status'
   ```

1. Add the new compute environment to your job queue:

   ```
   aws batch update-job-queue \
     --job-queue {{your-job-queue}} \
     --compute-environment-order order=1,computeEnvironment={{your-existing-environment}} \
     order=2,computeEnvironment={{your-new-compute-environment-name}}
   ```

1. Once verified, update again to make the new environment primary:

   ```
   aws batch update-job-queue \
     --job-queue {{your-job-queue}} \
     --compute-environment-order order=1,computeEnvironment={{your-new-compute-environment-name}}
   ```

   After all jobs complete in the old environment, disable and then delete it:

   ```
   aws batch update-compute-environment \
       --compute-environment {{your-existing-environment}} \
       --state DISABLED
   ```

   ```
   aws batch delete-compute-environment \
     --compute-environment {{your-existing-environment}}
   ```

------