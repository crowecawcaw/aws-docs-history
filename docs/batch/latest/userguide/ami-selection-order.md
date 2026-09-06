

# AMI selection order
<a name="ami-selection-order"></a>

AWS Batch determines the Amazon Machine Image (AMI) for compute resources using the following priority order. Understanding this order helps you understand why AWS Batch chose a particular AMI for your compute environment:

1. **Launch template override AMI** - If a launch template override for the launched instance has an image, then its image is used.

1. **Compute resources image ID (deprecated)** - If set, this compute environment AMI is used. *Note: Deprecated field; use ec2Configuration.imageIdOverride instead.*

1. **EC2 configuration image ID override** - If specified, the image in this field is used.

1. **Launch template AMI** - If the compute environment has an associated launch template with an image, then this image will be used.

1. **AWS default AMI** - If none of the above are configured, AWS Batch selects a default AMI based on the specified imageType in the ec2Configuration.

**Note**  
The ec2Configuration parameter is optional. When omitted, AWS Batch automatically selects an appropriate ec2Configuration and default AMI based on the instance types launched in the compute environment.

**Note**  
This AMI selection order does not apply to Fargate compute environments.

## AMI selection order from highest to lowest priority
<a name="ami-order"></a>

1. **Launch template override AMI** (highest precedence)

   **API field:** `overrides[].launchTemplateId` with target instance types

   **Reference:** [LaunchTemplateSpecification](https://docs.aws.amazon.com/batch/latest/APIReference/API_LaunchTemplateSpecification.html)

   Override templates target specific instance types and provide more granular control than the default launch template. They take precedence over all other AMI specifications for matching instance types.

   ```
   {
     "computeResources": {
       "launchTemplate": {
         "launchTemplateId": "lt-default",
         "overrides": [
           {
             "launchTemplateId": "lt-gpu-optimized",
             "targetInstanceTypes": ["p3.2xlarge", "g4dn.xlarge"]
           }
         ]
       }
     }
   }
   ```

1. **Compute resources image ID**

   **API field:** `computeResources.imageId`

   **Reference:** [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html)

   You can specify an AMI directly at the compute environment level. This takes precedence over EC2 configuration overrides and launch templates (except override templates).

   In a compute environment with multiple EC2 configurations (e.g. for `ECS_AL2023` and `ECS_AL2023_NVIDIA`), the AMI ID specified here is used for all EC2 configurations.
**Important**  
The `imageId` field is deprecated. Please use `ec2Configuration.imageIdOverride` instead.

   ```
   {
     "computeResources": {
       "imageId": "ami-12345678",
       "instanceTypes": ["m5.large", "m5.xlarge"]
     }
   }
   ```

1. **EC2 configuration image ID override**

   **API field:** `computeResources.ec2Configuration[].imageIdOverride`

   **Reference:** [Ec2Configuration](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html)

   EC2 configuration provides image type-specific overrides. This setting overrides the default AMI selection and launch template AMI for the specified image type.

   ```
   {
     "computeResources": {
       "ec2Configuration": [
         {
           "imageType": "ECS_AL2",
           "imageIdOverride": "ami-87654321"
         }
       ]
     }
   }
   ```

1. **Launch template AMI**

   **API field:** `ImageId` in the Amazon EC2 launch template

   **Reference:** [Use Amazon EC2 launch templates with AWS Batch](launch-templates.md)

   When you specify an AMI in the launch template, it takes precedence over the default AMI selection but is overridden by higher precedence settings.

   ```
   // EC2 Launch Template content
   {
     "LaunchTemplateName": "my-batch-template",
     "LaunchTemplateData": {
       "ImageId": "ami-12345678"
     }
   }
   ```

   Referenced by the AWS Batch launch template:

   ```
   // Batch Launch Template content
   {
     "computeResources": {
       "launchTemplate": {
         "launchTemplateName": "my-batch-template",
         "version": "$Latest"
       }
     }
   }
   ```

1. **AWS default AMI** (lowest precedence)

   **API field:** Determined by `computeResources.ec2Configuration[].imageType`

   **Reference:** [Ec2Configuration imageType](https://docs.aws.amazon.com/batch/latest/APIReference/API_Ec2Configuration.html)

   When no custom AMI is specified, AWS Batch automatically selects the latest approved Amazon Amazon ECS-optimized AMI based on the image type.
**Note**  
The `ec2Configuration` is optional. AWS Batch will select an appropriate default AMI if no `ec2Configuration` is specified.

   ```
   {
     "computeResources": {
       "ec2Configuration": [
         {
           "imageType": "ECS_AL2023"
         }
       ]
     }
   }
   ```