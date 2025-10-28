# Create a deployment configuration with

CodeDeploy

If you don't want to use one of the default deployment configurations provided with CodeDeploy,
you can create your own using the following instructions.

You can use the CodeDeploy console, AWS CLI, the CodeDeploy APIs, or an AWS CloudFormation template to create
custom deployment configurations.

For information about using an AWS CloudFormation template to create a deployment configuration, see
[AWS CloudFormation templates for CodeDeploy
reference](reference-cloudformation-templates.md "reference-cloudformation-templates.md").

###### Topics

- [Creating a deployment
  configuration (console)](#deployment-configurations-create-console "#deployment-configurations-create-console")
- [Creating a deployment
  configuration with CodeDeploy (AWS CLI)](#deployment-configurations-create-cli "#deployment-configurations-create-cli")

## Creating a deployment

configuration (console)

Use the following instructions to create a deployment configuration using the AWS
console.

###### To create a deployment configuration in CodeDeploy using the console

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, choose **Deployment
configurations**.

A list of built-in deployment configurations appears. 3. Choose **Create deployment configuration**. 4. In **Deployment configuration name**, enter a name for the
deployment configuration. For example,
`my-deployment-config`. 5. Under **Compute platform**, choose one of the
following:

    * **EC2/On-premises**
    * **AWS Lambda**
    * **Amazon ECS**

6.  Do one of the following:
    - If you chose **EC2/On-premises**:
      1. Under **Minimum healthy hosts**, specify the
         number or percentage of instances that must remain available at
         any time during a deployment. For more information about how
         CodeDeploy monitors and evaluates instance health during a
         deployment, see [Instance Health](instances-health.md "instances-health.md").
      2. (Optional) Under **Zonal configuration**,
         select **Enable zonal configuration** to have
         CodeDeploy deploy your application to one [Availability Zone](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-availability-zones "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-availability-zones") at a time, within an AWS
         Region. By deploying to one Availability Zone at a time, you can
         expose your deployment to a progressively larger audience as
         confidence in the deployment's performance and viability grows.
         If you don't enable a zonal configuration, CodeDeploy deploys your
         application to a random selection of hosts across a
         Region.

      If you enable the zonal configuration feature, note the
      following:

          + The zonal configuration feature is only supported with
           in-place deployments to Amazon EC2 instances. (Blue/green
           deployments and on-premises instances are not
           supported.) For more information about in-place
           deployments, see [Deployment type](primary-components.md#primary-components-deployment-type "primary-components.md#primary-components-deployment-type").
          + The zonal configuration feature is not supported with
           [predefined deployment configurations](deployment-configurations.md#deployment-configurations-predefined "deployment-configurations.md#deployment-configurations-predefined"). To use
           a zonal configuration, you must create a custom
           deployment configuration, as described here.
          + If CodeDeploy needs to roll back a deployment, CodeDeploy will
           perform the rollback operations on random hosts. (CodeDeploy
           will not roll back one zone at a time, as you might
           expect.) This rollback behavior was chosen for
           performance reasons. For more information about
           rollbacks, see [Redeploy and roll back a deployment with
           CodeDeploy](deployments-rollback-and-redeploy.md "deployments-rollback-and-redeploy.md").

      3. If you selected the **Enable zonal
         configuration** check box, optionally specify the
         following options:
         - (Optional) In **Monitor duration**,
           specify the period of time, in seconds, that CodeDeploy must
           wait after completing a deployment to an Availability
           Zone. CodeDeploy will wait this amount of time before
           starting a deployment to the next Availability Zone.
           Consider adding a monitor duration to give the
           deployment some time to prove itself (or 'bake') in one
           Availability Zone before it is released in the next
           zone. If you don't specify a monitor duration, then
           CodeDeploy starts deploying to the next Availability Zone
           immediately. For more information about how the
           **Monitor duration** setting works,
           see [About the minimum number of healthy instances per
           Availability Zone](instances-health.md#minimum-healthy-hosts-az "instances-health.md#minimum-healthy-hosts-az").
         - (Optional) Select **Add a monitor duration for
           the first zone** to set a monitor duration
           that only applies to the first Availability Zone. You
           might set this option if you want to allow extra bake
           time for the first Availability Zone. If you don't
           specify a value in **Add a first zone monitor
           duration**, then CodeDeploy uses the
           **Monitor duration** value for the
           first Availability Zone.
         - (Optional) Under **Minimum healthy hosts per
           zone**, specify the number or percentage of
           instances that must remain available per Availability
           Zone during a deployment. Choose
           **FLEET_PERCENT** to specify a
           percentage, or **HOST_COUNT** to
           specify a number. This field works in conjunction with
           the **Minimum healthy hosts** field.
           For more information, see [About the minimum number of healthy instances per
           Availability Zone](instances-health.md#minimum-healthy-hosts-az "instances-health.md#minimum-healthy-hosts-az").

         If you don't specify a value under **Minimum
         healthy hosts per zone**, then CodeDeploy uses a
         default value of `0` percent.

    - If you chose **AWS Lambda** or
      **Amazon ECS**:
      1. For **Type**, choose
         **Linear** or
         **Canary**.
      2. In the **Step** and
         **Interval** fields, do one of the
         following:
         - If you chose **Canary**, for
           **Step**, enter a percentage of
           traffic, between 1 and 99, to be shifted. This is the
           percentage of traffic that is shifted in the first
           increment. The remaining traffic is shifted after the
           selected interval in the second increment.

         For **Interval**, enter the number of
         minutes between the first and second traffic
         shift.
         - If you chose **Linear**, for
           **Step**, enter a percentage of
           traffic, between 1 and 99, to be shifted. This is the
           percentage of traffic that is shifted at the start of
           each interval.

         For **Interval**, enter the number of
         minutes between each incremental shift.

7.  Choose **Create deployment configuration**.

You now have a deployment configuration that you can associate with a
deployment group.

## Creating a deployment

configuration with CodeDeploy (AWS CLI)

To use the AWS CLI to create a deployment configuration, call the
[create-deployment-config](../../../cli/latest/reference/deploy/create-deployment-config.md "../../../cli/latest/reference/deploy/create-deployment-config.md") command.

The following example creates an EC2/On-Premises deployment configuration
named `ThreeQuartersHealthy` that requires 75% of target instances to remain
healthy during a deployment:

```
aws deploy create-deployment-config --deployment-config-name ThreeQuartersHealthy --minimum-healthy-hosts type=FLEET_PERCENT,value=75
```

The following example creates an EC2/On-Premises deployment configuration
named `300Total50PerAZ` that requires 300 target instances to remain healthy
in total per deployment, and 50 to remain healthy per Availability Zone. It also sets a
monitor duration of 1 hour.

```
aws deploy create-deployment-config --deployment-config-name 300Total50PerAZ --minimum-healthy-hosts type=HOST_COUNT,value=300 --zonal-config '{"monitorDurationInSeconds":3600,"minimumHealthyHostsPerZone":{"type":"HOST_COUNT","value":50}}'
```

The following example creates an AWS Lambda deployment configuration
named `Canary25Percent45Minutes`. It uses canary traffic shifting to shift 25
percent of traffic in the first increment. The remaining 75 percent shifted 45 minutes
later:

```
aws deploy create-deployment-config --deployment-config-name Canary25Percent45Minutes --traffic-routing-config "type="TimeBasedCanary",timeBasedCanary={canaryPercentage=25,canaryInterval=45}" --compute-platform Lambda
```

The following example creates an Amazon ECS deployment configuration named
`Canary25Percent45Minutes`. It uses canary traffic shifting to shift 25
percent of traffic in the first increment. The remaining 75 percent shifted 45 minutes
later:

```
aws deploy create-deployment-config --deployment-config-name Canary25Percent45Minutes --traffic-routing-config "type="TimeBasedCanary",timeBasedCanary={canaryPercentage=25,canaryInterval=45}" --compute-platform ECS
```
