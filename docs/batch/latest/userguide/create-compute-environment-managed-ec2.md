# Tutorial: Create a managed compute

environment using Amazon EC2 resources

Complete the following steps to create a managed compute environment using Amazon Elastic Compute Cloud
(Amazon EC2) resources.

1.  Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2.  From the navigation bar, select the AWS Region to use.
3.  In the navigation pane, choose **Environments**.
4.  Choose **Create environment** and then **Compute
    environment**.
5.  Configure the environment.
    1. For **Compute environment configuration**, choose
       **Amazon Elastic Compute Cloud (Amazon EC2)**.
    2. For **Orchestration type**, choose
       **Managed**.
    3. For **Name**, specify a unique name for your compute environment.
       The name can contain up to 128 characters in length. It can contain uppercase and
       lowercase letters, numbers, hyphens (-), and underscores (\_).
    4. For **Service role**, choose service-linked role that lets the
       AWS Batch service make calls to the required AWS API operations on your behalf. For
       example, choose **AWSServiceRoleForBatch**. For more information, see
       [Using service-linked roles for
       AWS Batch](using-service-linked-roles.md "using-service-linked-roles.md").
    5. For **Instance role**, choose to create a new instance profile or
       use an existing instance profile that has the required IAM permissions attached. This
       instance profile allows the Amazon ECS container instances that are created for your
       compute environment to make calls to the required AWS API operations on your behalf.
       For more information, see [Amazon ECS instance role](instance_IAM_role.md "instance_IAM_role.md"). If you choose to create a new instance profile, the
       required role (`ecsInstanceRole`) is created for you.
    6. (Optional) Expand **Tags**.
       1. (Optional) For **EC2 tags**, choose **Add tag**
          to add a tag to resources that are launched in the compute environment. Then, enter a
          **Key** name and optional **Value**. Choose
          **Add tag**.
       2. (Optional) For **Tags**, choose **Add tag**.
          Then, enter a **Key** name and optional **Value**.
          Choose **Add tag**.

       For more information, see [Tag your AWS Batch resources](using-tags.md "using-tags.md").

    7. Choose **Next**.

6.  In the **Instance configuration** section:
    1. (Optional) For **Enable using Spot instances**, turn on Spot. For
       more information, see [Spot Instances](../../../AWSEC2/latest/UserGuide/using-spot-instances.md "../../../AWSEC2/latest/UserGuide/using-spot-instances.md").
    2. (Spot only) For **Maximum % on-demand price**, choose the maximum
       percentage that a Spot Instance price can be when compared with the On-Demand price
       for that instance type before instances are launched. For example, if your maximum
       price is 20%, then the Spot price must be less than 20% of the current On-Demand price
       for that EC2 instance. You always pay the lowest (market) price and never more than
       your maximum percentage. If you leave this field empty, the default value is 100% of
       the On-Demand price.
    3. (Spot only) For **Spot fleet role**, choose an existing Amazon EC2
       Spot Fleet IAM role to apply to your Spot compute environment. If you don't already
       have an existing Amazon EC2 Spot Fleet IAM role, you must create one first. For more
       information, see [Amazon EC2 spot fleet role](spot_fleet_IAM_role.md "spot_fleet_IAM_role.md").

    ###### Important

    To tag your Spot Instances on creation, your Amazon EC2 Spot Fleet IAM role must
    use the newer **AmazonEC2SpotFleetTaggingRole** managed policy. The
    **AmazonEC2SpotFleetRole** managed policy doesn't have the
    required permissions to tag Spot Instances. For more information, see [Spot Instances not tagged on creation](spot-instance-no-tag.md "spot-instance-no-tag.md") and [Tag your resources](tag-resources.md "tag-resources.md"). 4. For **Minimum vCPUs**, choose the minimum number of vCPUs that
    your compute environment maintains, regardless of job queue demand. 5. For **Desired vCPUs**, choose the number of vCPUs that your
    compute environment launches with. As your job queue demand increases, AWS Batch can
    increase the desired number of vCPUs in your compute environment and add EC2
    instances, up to the maximum vCPUs. As demand decreases, AWS Batch can decrease the
    desired number of vCPUs in your compute environment and remove instances, down to the
    minimum vCPUs. 6. For **Maximum vCPUs**, choose the maximum number of vCPUs that
    your compute environment can scale out to, regardless of job queue demand. 7. For **Allowed instance types**, choose the Amazon EC2 instance types
    that can be launched. You can specify instance families to launch any instance type
    within those families (for example, `c5`, `c5n`, or
    `p3`). Or, you can specify specific sizes within a family (such as
    `c5.8xlarge`). Metal instance types aren't in the instance families. For
    example, `c5` doesn't include `c5.metal`.

    AWS Batch can select the instance type for you if you choose one of the following:

        * `optimal` to select instance types (from the `c4`, `m4`,
         `r4`, `c5`, `m5`, and `r5`
         instance families) that match the demand of your job queues.
        * `default_x86_64` to choose x86 based instance types (from the m6i,
         c6i, r6i, and c7i instance families)
         that matches the resource demands of the job queue.
        * `default_arm64` to choose x86 based instance types (from the m6g,
         c6g, r6g, and c7g instance families)
         that matches the resource demands of the job queue.

    ###### Note

    Starting on 11/01/2025 the behavior of `optimal` is going to be changed
    to match `default_x86_64`. During the change your instance families could
    be updated to a newer generation. You do not need to perform any actions for the
    upgrade to happen. For more information about change, see .

    ###### Note

        * Instance family availability varies by AWS Region. For example, some AWS Regions may not
         have any fourth generation instance families but have fifth and sixth generation
         instance families.
        * When using `default_x86_64` or `default_arm64` instance bundles, AWS Batch
         selects instance families based on a balance of cost-effectiveness and
         performance. While newer generation instances often provide better
         price-performance, AWS Batch may choose an earlier generation instance family if
         it provides the optimal combination of availability, cost, and performance for
         your workload. For example, in an AWS Region where both c6i and c7i instances
         are available, AWS Batch might select c6i instances if they offer better
         cost-effectiveness for your specific job requirements. For more information on
         AWS Batch instance types and AWS Region availability, see [Instance type compute
         table](instance-type-compute-table.md#instance-type-compute-table.title "instance-type-compute-table.md#instance-type-compute-table.title").
        * AWS Batch periodically updates your instances in default bundles to newer, more cost-effective
         options. Updates happen automatically without requiring any action from you. Your
         workloads continue running during updates with no interruption.

    ###### Note

    When you create a compute environment, the instance types that you select for the compute environment must share
    the same architecture. For example, you can't mix x86 and ARM instances in the same compute environment.

    ###### Note

    AWS Batch will scale GPUs based on the required amount in your job queues. To use
    GPU scheduling, the compute environment must include instance types from the
    `p3`, `p4`, `p5`, `p6`, `g3`, `g3s`,
    `g4`, `g5`, or `g6` families. 8. For **Allocation strategy**, choose the allocation strategy to
    use when selecting instance types from the list of allowed instance types.
    **BEST_FIT_PROGRESSIVE** is usually the better choice for EC2
    On-Demand compute environments, **SPOT_CAPACITY_OPTIMIZED**, and
    **SPOT_PRICE_CAPACITY_OPTIMIZED** for EC2 Spot compute
    environments. For more information, see [Instance type allocation strategies for AWS Batch](allocation-strategies.md "allocation-strategies.md"). 9. Expand **Additional configuration**.

        1. (Optional) For **Placement group**, enter a placement group name
         to group resources in the compute environment.
        2. (Optional) For **EC2 key pair**, choose a public
         and private key pair as security credentials when you connect to the instance. For
         more information about Amazon EC2 key pairs, see [Amazon EC2 key pairs and Linux
         instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md").
        3. (Optional) For **EC2 configuration** choose **Image
         type** and **Image ID override** values to provide
         information for AWS Batch to select Amazon Machine Images (AMIs) for instances in the
         compute environment. If the **Image ID override** isn't specified for
         each **Image type**, AWS Batch selects a recent [Amazon ECS optimized AMI](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md"). If no **Image type** is specified,
         the default is a **Amazon Linux 2** for non-GPU, non AWS Graviton
         instance.


        ###### Important

        To use a custom AMI, choose the image type and then enter the custom AMI ID
         in the **Image ID override** box.




        [Amazon Linux
         2](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#al2ami "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#al2ami")

         Default for all AWS Graviton-based instance families (for example,
         `C6g`, `M6g`, `R6g`, and `T4g`)
         and can be used for all non-GPU instance types.



        [Amazon Linux
         2 (GPU)](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#gpuami "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#gpuami")

        Default for all GPU instance families (for example `P4` and
         `G4`) and can be used for all non AWS Graviton-based instance
         types.



        [Amazon Linux 2023](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md")

        AWS Batch
         supports Amazon Linux 2023.


        ###### Note

        Amazon Linux 2023 does not support `A1` instances.



        [Amazon Linux 2023
         (GPU)](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#gpuami "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#gpuami")

        Default for all GPU instance families (for example `P4` and
         `G4`) and can be used for all non AWS Graviton-based instance types.




        ###### Note

        The AMI that you choose for a compute environment must match the architecture of the instance types that
         you intend to use for that compute environment. For example, if your compute environment uses A1 instance types,
         the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the
         Amazon ECS optimized Amazon Linux 2 AMI. For more information, see [Amazon ECS optimized Amazon Linux 2 AMI](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#ecs-optimized-ami-linux-variants.html "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#ecs-optimized-ami-linux-variants.html")
         in the *Amazon Elastic Container Service Developer Guide*.

    10. (Optional) Expand **Launch templates**
        1. For **Default launch template**, select an existing Amazon EC2
           launch template to configure your compute resources. The default version of the
           template is automatically populated. For more information, see [Use Amazon EC2 launch templates with AWS Batch](launch-templates.md "launch-templates.md").

        ###### Note

        In a launch template, you can specify a custom AMI that you created. 2. (Optional) For **Default version**, enter
        `$Default`, `$Latest`, or a specific version number to
        use.

        ###### Note

        Note: If you use either substitution variable ($Default or $Latest), they will
        apply the current default or latest version number at the time that this
        configuration is saved. If the default or latest version changes in the future, you
        must update the information - it won't automatically update.

        ###### Important

        If the version parameter of the launch template is `$Default` or
        `$Latest`, the default or latest version of the specified launch
        template is evaluated during an infrastructure update. If a different AMI ID is
        selected by the default or the latest version of the launch template is selected,
        that AMI ID is used in the update. For more information, see [AMI selection during infrastructure updates](infrastructure-updates.md#updating-compute-environments-ami "infrastructure-updates.md#updating-compute-environments-ami"). 3. (Optional) For **Override launch template** choose **Add override launch template**

            1. (Optional) For **Launch template**, select an existing Amazon EC2
             launch template to use for specific instance types and families.
            2. (Optional) For **Default version**, enter a specific version
             number to use, `$Default`, or `$Latest`.


            ###### Note

            If you use either the `$Default` or `$Latest` variable,
             AWS Batch will apply the current information at the time that the compute environment
             is created. If the default or latest version changes in the future, you must update
             the information through [UpdateComputeEnvironment](../APIReference/API_UpdateComputeEnvironment.md "../APIReference/API_UpdateComputeEnvironment.md") or through the AWS Management Console - AWS Batch.
            3. (Optional) For **Target instance types**, select the instance
             type or family that you want to apply the override launch template.


            ###### Note

            If you specify an override launch template, **Target instance
             types** is required. For more information, see [LaunchTemplateSpecificationOverride.targetInstanceTypes](../APIReference/API_LaunchTemplateSpecificationOverride.md#Batch-Type-LaunchTemplateSpecificationOverride-targetInstanceTypes "../APIReference/API_LaunchTemplateSpecificationOverride.md#Batch-Type-LaunchTemplateSpecificationOverride-targetInstanceTypes").


            ###### Note

            If the instance type or family that you want to select doesn't appear in this
             list, review the selections you made in `Allowed instance types`.

    11. Choose **Next**.

7.  In the **Network configuration** section:

###### Important

Compute resources need access to communicate with the Amazon ECS
service endpoint. This can be through an interface VPC endpoint or through your
compute resources having public IP addresses.

For more information about interface VPC endpoints, see [Amazon ECS Interface
VPC Endpoints (AWS PrivateLink)](../../../AmazonECS/latest/developerguide/vpc-endpoints.md "../../../AmazonECS/latest/developerguide/vpc-endpoints.md") in the
_Amazon Elastic Container Service Developer Guide_.

If you do not have an interface VPC endpoint configured and your compute
resources do not have public IP addresses, then they must use
network address translation (NAT) to provide this access. For more information,
see [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in the
_Amazon VPC User Guide_. For more information, see
[Create a VPC](create-a-vpc.md "create-a-vpc.md").

    1. For **Virtual Private Cloud (VPC) ID**, choose a VPC where to
     launch your instances.
    2. For **Subnets**, choose the subnets to use. By default, all
     subnets within the selected VPC are available.


    ###### Note

    AWS Batch on Amazon EC2 supports Local Zones. For more information, see  [Local Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-local-zones "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-local-zones") in the *Amazon EC2 User Guide* and  [Amazon ECS clusters in Local Zones, Wavelength Zones, and AWS Outposts](../../../AmazonECS/latest/developerguide/cluster-regions-zones.md#clusters-local-zones "../../../AmazonECS/latest/developerguide/cluster-regions-zones.md#clusters-local-zones") in the
     *Amazon Elastic Container Service Developer Guide*.
    3. (Optional) For **Security groups**, choose a security group to
     attach to your instances. By default, the default security group for your VPC is
     chosen.


    ###### Note

    Note: If you use either substitution variable ($Default or $Latest), they will
     apply the current default or latest version number at the time that this
     configuration is saved. If the default or latest version changes in the future, you
     must update the information - it won't automatically update.

8. Choose **Next page**.
9. For **Review**, review the configuration steps. If you
   need to make changes, choose **Edit**. When you're finished,
   choose **Create compute environment**.
