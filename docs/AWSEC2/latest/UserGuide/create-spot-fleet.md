# Create a Spot Fleet

Using the AWS Management Console, you can quickly create a Spot Fleet request by choosing only an AMI and
your desired total target capacity. Amazon EC2 will configure a fleet that best meets your
needs and follows Spot best practices. Alternatively, you can modify any of the default
settings.

If you want to include On-Demand Instances in your fleet, you must specify a launch template in
your request and specify you desired On-Demand capacity.

The fleet launches On-Demand Instances when capacity is available, and launches Spot Instances when your
maximum price exceeds the Spot price and capacity is available.

If your fleet includes Spot Instances and is of type `maintain`, Amazon EC2 will attempt
to maintain your fleet target capacity when your Spot Instances are interrupted.

###### Required permissions

For more information, see [Spot Fleet permissions](spot-fleet-prerequisites.md "spot-fleet-prerequisites.md").

###### Tasks

- [Quickly create a Spot Fleet request](#create-spot-fleet-quick "#create-spot-fleet-quick")
- [Create a Spot Fleet request using defined
  parameters](#create-spot-fleet-advanced "#create-spot-fleet-advanced")
- [Create a Spot Fleet that replaces unhealthy
  Spot Instances](#spot-fleet-health-checks "#spot-fleet-health-checks")

## Quickly create a Spot Fleet request

Follow these steps to quickly create a Spot Fleet request using the Amazon EC2
console.

###### To create a Spot Fleet request using the recommended settings

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. If you are new to Spot, you see a welcome page; choose **Get
   started**. Otherwise, choose **Create Spot Fleet
   Request**.
4. Under **Launch parameters**, choose **Manually
   configure launch parameters**.
5. For **AMI**, choose an AMI.
6. Under **Target capacity**, for **Total target
   capacity**, specify the number of units to request. For the
   type of unit, you can choose **Instances**,
   **vCPUs**, or **Memory (GiB)**.
7. Under **Your fleet request at a glance**, review your
   fleet configuration, and choose **Launch**.

## Create a Spot Fleet request using defined

parameters

You can create a Spot Fleet by using parameters that you define.

Console

###### To create a Spot Fleet request using defined parameters

1.  Open the Amazon EC2 console at
    [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2.  In the navigation pane, choose **Spot
    Requests**.
3.  If you are new to Spot, you see a welcome page; choose
    **Get started**. Otherwise, choose
    **Create Spot Fleet Request**.
4.  For **Launch parameters**, you can either
    manually configure the launch parameters or you can use a launch
    template, as follows:
    1.  [Manually configure] To define the launch parameters
        in the Amazon EC2 console, choose **Manually
        configure launch parameters**, and then do
        the following:
        1. For **AMI**, choose one of
           the basic AMIs provided by AWS, or choose
           **Search for AMI** to use an AMI
           from our user community, the

        AWS Marketplace, or one of your own.

        ###### Note

        If an AMI specified in the launch parameters
        is deregistered or disabled, no new instances can
        be launched from the AMI. For fleets that are set
        to maintain target capacity, the target capacity
        will not be maintained. 2. (Optional) For **Key pair
        name**, choose an existing key pair or
        create a new one.

        [Existing key pair] Choose the key
        pair.

        [New key pair] Choose **Create new key
        pair** to go the **Key
        pairs** page. When you are done, return
        to the **Spot Requests** page and
        refresh the list. 3. (Optional) Expand **Additional launch
        parameters**, and do the
        following:

            1. (Optional) To enable Amazon EBS optimization, for
             **EBS-optimized**, select
             **Launch EBS-optimized
             instances**.
            2. (Optional) To add temporary block-level
             storage for your instances, for **Instance
             store**, choose **Attach at
             launch**.
            3. (Optional) To add storage, choose
             **Add new volume**, and specify
             additional instance store volumes or Amazon EBS
             volumes, depending on the instance type.
            4. (Optional) By default, basic monitoring is
             enabled for your instances. To enable detailed
             monitoring, for **Monitoring**,
             select **Enable CloudWatch detailed
             monitoring**.
            5. (Optional) To run a Dedicated Spot Instance, for
             **Tenancy**, choose
             **Dedicated - run a dedicated
             instance**.
            6. (Optional) For **Security
             groups**, choose one or more security
             groups or create a new one.


            [Existing security group] Choose one or more
             security groups.


            [New security group] Choose **Create
             new security group** to go the
             **Security Groups** page. When
             you are done, return to the **Spot
             Requests** and refresh the list.
            7. (Optional) To make your instances reachable
             from the internet, for **Auto-assign IPv4
             Public IP**, choose
             **Enable**.
            8. (Optional) To launch your Spot Instances with an
             IAM role, for **IAM instance
             profile**, choose the role.
            9. (Optional) To run a start-up script, copy it
             to **User data**.
            10. (Optional) To add a tag, choose
             **Create tag** and enter the key
             and value for the tag, and choose
             **Create**. Repeat for each
             tag.


            For each tag, to tag the instances and the
             Spot Fleet request with the same tag, ensure that both
             **Instances** and
             **Fleet** are selected. To tag
             only the instances launched by the fleet, clear
             **Fleet**. To tag only the Spot Fleet
             request, clear
             **Instances**.

    2.  [Launch template] To use a configuration you created
        in a launch template, choose **Use a launch
        template**, and for **Launch
        template**, choose a launch
        template.

    ###### Note

    If you want On-Demand capacity in your Spot Fleet, you
    must specify a launch template.

5.  For **Additional request details**, do the
    following:
    1. Review the additional request details. To make
       changes, clear **Apply
       defaults**.
    2. (Optional) For **IAM fleet role**,
       you can use the default role or choose a different role.
       To use the default role after changing the role, choose
       **Use default role**.
    3. (Optional) To create a request that is valid only
       during a specific time period, edit **Request
       valid from** and **Request valid
       until**.
    4. (Optional) By default, Amazon EC2 terminates your Spot Instances
       when the Spot Fleet request expires. To keep them running
       after your request expires, clear **Terminate
       the instances when the request
       expires**.
    5. (Optional) To register your Spot Instances with a load
       balancer, choose **Receive traffic from one or
       more load balancers** and choose one or
       more Classic Load Balancers or target groups.

6.  For **Target capacity**, do the
    following:
    1. For **Total target capacity**,
       specify the number of units to request. For the type of
       unit, you can choose **Instances**,
       **vCPUs**, or **Memory
       (MiB)**. To specify a target capacity of 0
       so that you can add capacity later, you must first
       select **Maintain target
       capacity**.
    2. (Optional) For **Include On-Demand base
       capacity**, specify the number of On-Demand
       units to request. The number must be less than the
       **Total target capacity**. Amazon EC2
       calculates the difference, and allocates the difference
       to Spot units to request.

    ###### Important

    To specify optional On-Demand capacity, you must
    first choose a launch template. 3. (Optional) By default, Amazon EC2 terminates Spot Instances when
    they are interrupted. To maintain the target capacity,
    select **Maintain target capacity**.
    You can then specify that Amazon EC2 terminates, stops, or
    hibernates Spot Instances when they are interrupted. To do so,
    choose the corresponding option from
    **Interruption behavior**.

    ###### Note

    If an AMI specified in the launch parameters is
    deregistered or disabled, no new instances can be
    launched from the AMI. In this case, for fleets that
    are set to maintain target capacity, the target
    capacity will not be maintained. 4. (Optional) To allow Spot Fleet to launch a replacement Spot Instance
    when an instance rebalance notification is emitted for
    an existing Spot Instance in the fleet, select **Capacity
    rebalance**, and then choose an instance
    replacement strategy. If you choose **Launch
    before terminate**, specify the delay (in
    seconds) before Amazon EC2 terminates the old instances. For
    more information, see [Use Capacity Rebalancing in EC2 Fleet and Spot Fleet
    to replace at-risk Spot Instances](ec2-fleet-capacity-rebalance.md "ec2-fleet-capacity-rebalance.md"). 5. (Optional) To control the amount you pay per hour for
    all the Spot Instances in your fleet, select **Set
    maximum cost for Spot Instances** and then enter the
    maximum total amount you're willing to pay per hour.
    When the maximum total amount is reached, Spot Fleet stops
    launching Spot Instances even if it hasn’t met the target
    capacity. For more information, see [Set a spending limit for your EC2 Fleet or
    Spot Fleet](ec2-fleet-control-spending.md "ec2-fleet-control-spending.md").

7.  For **Network**, do the following:
    1. For **Network**, choose an existing
       VPC or create a new one.

    [Existing VPC] Choose the VPC.

    [New VPC] Choose **Create new VPC**
    to go the Amazon VPC console. When you're done, return to
    this screen and refresh the list. 2. (Optional) For **Availability Zone**,
    let Amazon EC2 choose the Availability Zones for your Spot Instances,
    or specify one or more Availability Zones.

    If you have more than one subnet in an Availability
    Zone, choose the appropriate subnet from
    **Subnet**. To add subnets, choose
    **Create new subnet** to go to the
    Amazon VPC console. When you are done, return to this screen
    and refresh the list.

8.  For **Instance type requirements**, you can
    either specify instance attributes and let Amazon EC2 identify the
    optimal instance types with these attributes, or you can specify
    a list of instances. For more information, see [Specify attributes for
    instance type selection for EC2 Fleet or Spot Fleet](ec2-fleet-attribute-based-instance-type-selection.md "ec2-fleet-attribute-based-instance-type-selection.md").
    1. If you choose **Specify instance attributes
       that match your compute requirements**,
       specify your instance attributes as follows:
       1. For **vCPUs**, enter the
          desired minimum and maximum number of vCPUs. To
          specify no limit, select **No
          minimum** or **No
          maximum**, or both.
       2. For **Memory (GiB)**, enter
          the desired minimum and maximum amount of memory.
          To specify no limit, select **No
          minimum** or **No
          maximum**, or both.
       3. (Optional) For **Additional instance
          attribute**, you can optionally specify
          one or more attributes to express your compute
          requirements in more detail. Each additional
          attribute adds a further constraint to your
          request. You can omit the additional attributes;
          when omitted, the default values are used. For a
          description of each attribute and their default
          values, see [get-spot-placement-scores](../../../cli/latest/reference/ec2/get-spot-placement-scores.md "../../../cli/latest/reference/ec2/get-spot-placement-scores.md").
       4. (Optional) To view the instance types with
          your specified attributes, expand
          **Preview matching instance
          types**. To exclude instance types from
          being used in your request, select the instances
          and then choose **Exclude selected
          instance types**.

    2. If you choose **Manually select instance
       types**, Spot Fleet provides a default list of
       instance types. To select more instance types, choose
       **Add instance types**, select the
       instance types to use in your request, and choose
       **Select**. To delete instance
       types, select the instance types and choose
       **Delete**.

9.  For **Allocation strategy**, choose a Spot
    allocation strategy and an On-Demand allocation strategy that
    meets your needs. For more information, see [Use allocation strategies to determine
    how EC2 Fleet or Spot Fleet fulfills Spot and On-Demand capacity](ec2-fleet-allocation-strategy.md "ec2-fleet-allocation-strategy.md").
10. For **Your fleet request at a glance**,
    review your fleet configuration, and make any adjustments if
    necessary.
11. (Optional) To download a copy of the launch configuration for
    use with the AWS CLI, choose **JSON
    config**.
12. When you're ready to launch your Spot Fleet, choose
    **Launch**.

The Spot Fleet request type is `fleet`. When the request
is fulfilled, requests of type `instance` are added,
where the state is `active` and the status is
`fulfilled`.

AWS CLI

###### To create a Spot Fleet request

Use the [request-spot-fleet](../../../cli/latest/reference/ec2/request-spot-fleet.md "../../../cli/latest/reference/ec2/request-spot-fleet.md") command.

```
aws ec2 request-spot-fleet --spot-fleet-request-config file://`config.json`
```

For example configuration files, see [Example CLI configurations Spot Fleet](spot-fleet-examples.md "spot-fleet-examples.md").

PowerShell

###### To create a Spot Fleet request

Use the [Request-EC2SpotFleet](../../../powershell/latest/reference/items/Request-EC2SpotFleet.md "../../../powershell/latest/reference/items/Request-EC2SpotFleet.md") cmdlet. The following example
launches Spot Instances in a capacity-optimized fleet.

```
Request-EC2SpotFleet `
    -SpotFleetRequestConfig_TargetCapacity `50` `
    -SpotFleetRequestConfig_AllocationStrategy "CapacityOptimized" `
    -SpotFleetRequestConfig_IamFleetRole "arn:aws:iam::`123456789012`:role/`my-spot-fleet-role`" `
    -SpotFleetRequestConfig_LaunchTemplateConfig @($launchConfig)
```

Define the launch configuration as follows, setting the launch
template and override properties that you need. For example
configurations, see [Example CLI configurations Spot Fleet](spot-fleet-examples.md "spot-fleet-examples.md").

```
$lcSpec = Amazon.EC2.Model.FleetLaunchTemplateSpecification
# To do - Set FleetLaunchTemplateSpecification properties
$lcOverrides = New-Object Amazon.EC2.Model.LaunchTemplateOverrides
# To do - Set LaunchTemplateOverrides properties
$launchConfig = New-Object Amazon.EC2.Model.LaunchTemplateConfig
$launchConfig.LaunchTemplateSpecification $lcSpec
$launchConfig.Overrides @($lcOverrides)
```

## Create a Spot Fleet that replaces unhealthy

Spot Instances

Spot Fleet checks the health status of the Spot Instances in the fleet every two minutes. The
health status of an instance is either `healthy` or
`unhealthy`.

Spot Fleet determines the health status of an instance by using the status checks
provided by Amazon EC2. An instance is determined as `unhealthy` when the
status of either the instance status check or the system status check is
`impaired` for three consecutive health checks. For more information,
see [Status checks for Amazon EC2
instances](monitoring-system-instance-status-check.md "monitoring-system-instance-status-check.md").

You can configure your fleet to replace unhealthy Spot Instances. After enabling health
check replacement, a Spot Instance is replaced when it is reported as `unhealthy`.
The fleet could go below its target capacity for up to a few minutes while an
unhealthy Spot Instance is being replaced.

###### Requirements

- Health check replacement is supported only for Spot Fleets that maintain a
  target capacity (fleets of type `maintain`), not for one-time
  Spot Fleets (fleets of type `request`).
- Health check replacement is supported only for Spot Instances. This feature is not
  supported for On-Demand Instances.
- You can configure your Spot Fleet to replace unhealthy instances only when you
  create it.
- Users can use health check replacement only if they have permission to
  call the `ec2:DescribeInstanceStatus` action.

Console

###### To configure a Spot Fleet to replace unhealthy Spot Instances

1. Follow the steps for creating a Spot Fleet in [Create a Spot Fleet request using defined
   parameters](#create-spot-fleet-advanced "#create-spot-fleet-advanced").
2. To configure the fleet to replace unhealthy Spot Instances, expand
   **Additional launch parameters**, and under
   **Health check**, select **Replace
   unhealthy instances**. To enable this option, you
   must first choose **Maintain target
   capacity**.

AWS CLI

###### To configure a Spot Fleet to replace unhealthy Spot Instances

Use the [request-spot-fleet](../../../cli/latest/reference/ec2/request-spot-fleet.md "../../../cli/latest/reference/ec2/request-spot-fleet.md") command with the
`ReplaceUnhealthyInstances` property of
`SpotFleetRequestConfig`.

```
{
    "SpotFleetRequestConfig": {
        "AllocationStrategy": "`lowestPrice`",
        "IamFleetRole": "arn:aws:iam::`123456789012`:role/`aws-ec2-spot-fleet-tagging-role`",
        "TargetCapacity": `10`,
        "ReplaceUnhealthyInstances": true
    }
}
```

PowerShell

###### To configure a Spot Fleet request to replace unhealthy Spot Instances

Use the [Request-EC2SpotFleet](../../../powershell/latest/reference/items/Request-EC2SpotFleet.md "../../../powershell/latest/reference/items/Request-EC2SpotFleet.md") cmdlet with the
`-SpotFleetRequestConfig_ReplaceUnhealthyInstance`
parameter.

```
-SpotFleetRequestConfig_ReplaceUnhealthyInstance $true
```
