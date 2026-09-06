

# Creating a capacity provider for Amazon ECS Managed Instances
<a name="create-capacity-provider-managed-instances"></a>

Amazon ECS Managed Instances uses capacity providers to manage compute capacity for your workloads. When you create a capacity provider without specifying `instanceRequirements`, Amazon ECS automatically selects the most cost-optimized [general-purpose instance types](https://aws.amazon.com/ec2/instance-types/general-purpose/). You can create capacity providers with `instanceRequirements` to specify instance attributes such as instance types, CPU manufacturers, accelerator types, and other requirements.

Custom capacity providers use attribute-based instance type selection, which allows you to express instance requirements as a set of attributes. These requirements are automatically translated to all matching Amazon EC2 instance types, simplifying the creation and maintenance of instance type configurations. To learn more about instance requirements and attribute-based selection, see the [Amazon EC2 Fleet attribute-based instance type selection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html) documentation in the *Amazon EC2 User Guide*.

## Prerequisites
<a name="create-capacity-provider-managed-instances-prerequisites"></a>

Before you begin, ensure that you have completed the following:
+ Determine what type of monitoring to use. For more information, see [Detailed monitoring for Amazon ECS Managed Instances](monitoring-managed-instances.md#detailed-monitoring-managed-instances).
+ Have an existing cluster or plan to create one. For more information, see [Creating a cluster for Amazon ECS Managed Instances](create-cluster-managed-instances.md).
+ You have the required IAM roles for Amazon ECS Managed Instances. This includes:
  + **Infrastructure role** - Allows Amazon ECS to make calls to AWS services on your behalf to manage Amazon ECS Managed Instances infrastructure.

    For more information, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md).
  + **Instance profile** - Provides permissions for the Amazon ECS container agent and Docker daemon running on managed instances.

    For more information, see [Amazon ECS Managed Instances instance profile](managed-instances-instance-profile.md).

Understand how to choose your instances. For more information, see [Instance selection best practices for Amazon ECS Managed Instances](managed-instances-instance-selection-best-practices.md).

## Console procedure
<a name="create-capacity-provider-managed-instances-console"></a>

**To create a capacity provider for Amazon ECS Managed Instances (Amazon ECS console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. From the navigation bar, select the Region to use.

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, choose your cluster name.

1. On the cluster page, choose the **Infrastructure** tab.

1. In the **Capacity providers** section, choose **Create capacity provider**.

1. Under **Capacity provider configuration**, configure the following:
   + For **Capacity provider name**, enter a unique name for your capacity provider.
   + For **Capacity provider type**, choose **Amazon ECS Managed Instances**.

1. Under **Instance configuration**, configure the following:
   + For **Instance profile**, choose the instance profile role created for Amazon ECS Managed Instances.
   + For **Infrastructure role**, choose the infrastructure role created for Amazon ECS Managed Instances.

1. Under **Instance requirements**, specify the attributes for your instances. You can configure any combination of the following:
   + **vCPU count** - Specify the number of vCPUs (for example, `4` or `8-16` for a range).
   + **Memory (MiB)** - Specify the amount of memory in MiB (for example, `8192` or `16384-32768` for a range).
   + **Instance types** - Specify specific instance types (for example, `m5.large,m5.xlarge,c5.large`).
   + **CPU manufacturers** - Choose from `intel`, `amd`, or `amazon-web-services`.
   + **Accelerator types** - Specify accelerator types such as `gpu`, `fpga`, or `inference`.
   + **Accelerator count** - Specify the number of accelerators (for example, `1` or `2-4` for a range).

1. Under **Advanced configuration**, choose one of the following monitoring options:
   + To have CloudWatch send status-check metrics, choose **Basic**.
   + To have CloudWatch send all metrics metrics, choose **Detailed**.

1. (Optional) To help identify your capacity provider, expand **Tags**, and then configure your tags.

   To enable tag propagation from capacity provider to managed resources such as instances launched from the capacity provider, for **Propagate tags from**, choose **Capacity provider**.

   [Add a tag] Choose **Add tag** and do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

1. Choose **Create**.

## AWS CLI procedure
<a name="create-capacity-provider-managed-instances-cli"></a>

You can create a capacity provider for Amazon ECS Managed Instances using the AWS CLI. Use the latest version of the AWS CLI. For more information on how to upgrade to the latest version, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**To create a capacity provider for Amazon ECS Managed Instances (AWS CLI)**

1. Run the following command:

   ```
   aws ecs create-capacity-provider --cli-input-json file://capacity-provider-definition.json
   ```

   The following `capacity-provider-definition.json` can be used to specify basic instance requirements, instance storage size, and enable tag propagation:

   ```
   {
       "name": "my-managed-instances-provider",
       "cluster": "my-cluster",
       "tags": [ 
           { 
               "key": "version",
               "value": "test"
           }
       ],    
       "managedInstancesProvider": {
           "infrastructureRoleArn": "arn:aws:iam::123456789012:role/ecsInfrastructureRole",
           "instanceLaunchTemplate": {
               "ec2InstanceProfileArn": "arn:aws:iam::123456789012:instance-profile/ecsInstanceRole",
               "instanceRequirements": {
                   "vCpuCount": {
                       "min": 4,
                       "max": 8
                   },
                   "memoryMiB": {
                       "min": 8192,
                       "max": 16384
                   }
               },
               "networkConfiguration": {
                   "subnets": [
                       "subnet-abcdef01234567",
                       "subnet-bcdefa98765432"
                   ],
                   "securityGroups": [
                       "sg-0123456789abcdef"
                   ]
               },
               "storageConfiguration": {
                   "storageSizeGiB": 100
               },
               "monitoring": "basic"
           },
           "propagateTags": "CAPACITY_PROVIDER"
       }
   }
   ```

1. Verify that your capacity provider was created successfully:

   ```
   aws ecs describe-capacity-providers \
       --capacity-providers {{my-managed-instances-provider}}
   ```

## Next steps
<a name="capacity-provider-managed-instances-next-steps"></a>

After creating your capacity provider, you can use it when creating services or running tasks:
+ To use the capacity provider with a service, see [Creating an Amazon ECS rolling update deployment](create-service-console-v2.md).
+ To use the capacity provider with standalone tasks, see [Running an application as an Amazon ECS task](standalone-task-create.md).