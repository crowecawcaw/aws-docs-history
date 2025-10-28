# `AWS::CodeDeploy::BlueGreen` hook

syntax

The following syntax describes the structure of an `AWS::CodeDeploy::BlueGreen`
hook for ECS blue/green deployments.

## Syntax

```
"Hooks": {
  "`Logical ID`": {
    "Type": "AWS::CodeDeploy::BlueGreen",
    "Properties": {
      "TrafficRoutingConfig": {
        "Type": "`Traffic routing type`",
        "TimeBasedCanary": {
          "StepPercentage": `Integer`,
          "BakeTimeMins": `Integer`
        },
        "TimeBasedLinear": {
          "StepPercentage": `Integer`,
          "BakeTimeMins": `Integer`
        }
      },
      "AdditionalOptions": {"TerminationWaitTimeInMinutes": `Integer`},
      "LifecycleEventHooks": {
        "BeforeInstall": "`FunctionName`",
        "AfterInstall": "`FunctionName`",
        "AfterAllowTestTraffic": "`FunctionName`",
        "BeforeAllowTraffic": "`FunctionName`",
        "AfterAllowTraffic": "`FunctionName`"
      },
      "ServiceRole": "`CodeDeployServiceRoleName`",
      "Applications": [
        {
          "Target": {
            "Type": "AWS::ECS::Service",
            "LogicalID": "`Logical ID of AWS::ECS::Service`"
          },
          "ECSAttributes": {
            "TaskDefinitions": [
              "`Logical ID of AWS::ECS::TaskDefinition (Blue)`",
              "`Logical ID of AWS::ECS::TaskDefinition (Green)`"
            ],
            "TaskSets": [
              "`Logical ID of AWS::ECS::TaskSet (Blue)`",
              "`Logical ID of AWS::ECS::TaskSet (Green)`"
            ],
            "TrafficRouting": {
              "ProdTrafficRoute": {
                "Type": "AWS::ElasticLoadBalancingV2::Listener",
                "LogicalID": "`Logical ID of AWS::ElasticLoadBalancingV2::Listener (Production)`"
              },
              "TestTrafficRoute": {
                "Type": "AWS::ElasticLoadBalancingV2::Listener",
                "LogicalID": "`Logical ID of AWS::ElasticLoadBalancingV2::Listener (Test)`"
              },
              "TargetGroups": [
                "`Logical ID of AWS::ElasticLoadBalancingV2::TargetGroup (Blue)`",
                "`Logical ID of AWS::ElasticLoadBalancingV2::TargetGroup (Green)`"
              ]
            }
          }
        }
      ]
    }
  }
}
```

## Properties

Logical ID (also called _logical name_)

The logical ID of a hook declared in the `Hooks` section of the
template. The logical ID must be alphanumeric (A-Za-z0-9) and unique within the
template.

_Required_: Yes

`Type`

The type of hook. `AWS::CodeDeploy::BlueGreen`

_Required_: Yes

`Properties`

Properties of the hook.

_Required_: Yes

`TrafficRoutingConfig`

Traffic routing configuration settings.

_Required_: No

The default configuration is time-based canary traffic shifting, with
a 15% step percentage and a five minute bake time.

`Type`

The type of traffic shifting used by the deployment
configuration.

Valid values: AllAtOnce | TimeBasedCanary |
TimeBasedLinear

_Required_: Yes

`TimeBasedCanary`

Specifies a configuration that shifts traffic from one
version of the deployment to another in two increments.

_Required_: Conditional: If you specify
`TimeBasedCanary` as the traffic routing type,
you must include the `TimeBasedCanary`
parameter.

`StepPercentage`

The percentage of traffic to shift in the first
increment of a `TimeBasedCanary` deployment.
The step percentage must be 14% or greater.

_Required_: No

`BakeTimeMins`

The number of minutes between the first and second
traffic shifts of a `TimeBasedCanary`
deployment.

_Required_: No

`TimeBasedLinear`

Specifies a configuration that shifts traffic from one
version of the deployment to another in equal increments, with
an equal number of minutes between each increment.

_Required_: Conditional: If you specify
`TimeBasedLinear` as the traffic routing type,
you must include the `TimeBasedLinear`
parameter.

`StepPercentage`

The percentage of traffic that's shifted at the
start of each increment of a
`TimeBasedLinear` deployment. The step
percentage must be 14% or greater.

_Required_: No

`BakeTimeMins`

The number of minutes between each incremental
traffic shift of a `TimeBasedLinear`
deployment.

_Required_: No

`AdditionalOptions`

Additional options for the blue/green deployment.

_Required_: No

`TerminationWaitTimeInMinutes`

Specifies time to wait, in minutes, before terminating the blue
resources.

_Required_: No

`LifecycleEventHooks`

Use lifecycle event hooks to specify a Lambda function that CodeDeploy can
call to validate a deployment. You can use the same function or a
different one for deployment lifecyle events. Following completion of the
validation tests, the Lambda `AfterAllowTraffic` function calls
back CodeDeploy and delivers a result of `Succeeded` or
`Failed`. For more information, see [AppSpec 'hooks' section](../../../codedeploy/latest/userguide/reference-appspec-file-structure-hooks.md "../../../codedeploy/latest/userguide/reference-appspec-file-structure-hooks.md") in the _AWS CodeDeploy User
Guide._

_Required_: No

`BeforeInstall`

Function to use to run tasks before the replacement task set is
created.

_Required_: No

`AfterInstall`

Function to use to run tasks after the replacement task set is
created and one of the target groups is associated with it.

_Required_: No

`AfterAllowTestTraffic`

Function to use to run tasks after the test listener serves
traffic to the replacement task set.

_Required_: No

`BeforeAllowTraffic`

Function to use to run tasks after the second target group is
associated with the replacement task set, but before traffic is
shifted to the replacement task set.

_Required_: No

`AfterAllowTraffic`

Function to use to run tasks after the second target group
serves traffic to the replacement task set.

_Required_: No

`ServiceRole`

The execution role for CloudFormation to use to perform the blue-green
deployments. For a list of the necessary permissions, see [IAM permissions for blue/green deployments](about-blue-green-deployments.md#blue-green-iam "about-blue-green-deployments.md#blue-green-iam").

_Required_: No

`Applications`

Specifies properties of the Amazon ECS application.

_Required_: Yes

`Target`

_Required_: Yes

`Type`

The type of the resource.

_Required_: Yes

`LogicalID`

The logical id of the resource.

_Required_: Yes

`ECSAttributes`

The resources that represent the various requirements of your
Amazon ECS application deployment.

_Required_: Yes

`TaskDefinitions`

The logical ID of the [AWS::ECS::TaskDefinition](../TemplateReference/aws-resource-ecs-taskdefinition.md "../TemplateReference/aws-resource-ecs-taskdefinition.md") resource
to run the Docker container that contains your Amazon ECS
application.

_Required_: Yes

`TaskSets`

The logical IDs of the [AWS::ECS::TaskSet](../TemplateReference/aws-resource-ecs-taskset.md "../TemplateReference/aws-resource-ecs-taskset.md") resources to use
as task sets for the application.

_Required_: Yes

`TrafficRouting`

Specifies resources used for traffic routing.

_Required_: Yes

`ProdTrafficRoute`

The listener to be used by your load balancer to
direct traffic to your target groups.

_Required_: Yes

`Type`

The type of the resource.
`AWS::ElasticLoadBalancingV2::Listener`

_Required_: Yes

`LogicalID`

The logical ID of the resource.

_Required_: Yes

`TestTrafficRoute`

The listener to be used by your load balancer to
direct traffic to your target groups.

_Required_: Yes

`Type`

The type of the resource.
`AWS::ElasticLoadBalancingV2::Listener`

_Required_: Yes

`LogicalID`

The logical ID of the resource.

_Required_: No

`TargetGroups`

Logical ID of resources to use as target groups to
route traffic to the registered target.

_Required_: Yes
