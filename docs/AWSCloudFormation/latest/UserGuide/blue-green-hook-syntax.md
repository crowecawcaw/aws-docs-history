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




Logical ID (also called *logical name*)

The logical ID of a hook declared in the `Hooks` section of the
 template. The logical ID must be alphanumeric (A-Za-z0-9) and unique within the
 template.


*Required*: Yes




`Type`

The type of hook. `AWS::CodeDeploy::BlueGreen`


*Required*: Yes



`Properties`

Properties of the hook.


*Required*: Yes




`TrafficRoutingConfig`

Traffic routing configuration settings.


*Required*: No


The default configuration is time-based canary traffic shifting, with
 a 15% step percentage and a five minute bake time.




`Type`

The type of traffic shifting used by the deployment
 configuration.


Valid values: AllAtOnce | TimeBasedCanary |
 TimeBasedLinear


*Required*: Yes




`TimeBasedCanary`

Specifies a configuration that shifts traffic from one
 version of the deployment to another in two increments.


*Required*: Conditional: If you specify
 `TimeBasedCanary` as the traffic routing type,
 you must include the `TimeBasedCanary`
 parameter.




`StepPercentage`

The percentage of traffic to shift in the first
 increment of a `TimeBasedCanary` deployment.
 The step percentage must be 14% or greater.


*Required*: No






`BakeTimeMins`

The number of minutes between the first and second
 traffic shifts of a `TimeBasedCanary`
 deployment.


*Required*: No





`TimeBasedLinear`

Specifies a configuration that shifts traffic from one
 version of the deployment to another in equal increments, with
 an equal number of minutes between each increment.


*Required*: Conditional: If you specify
 `TimeBasedLinear` as the traffic routing type,
 you must include the `TimeBasedLinear`
 parameter.




`StepPercentage`

The percentage of traffic that's shifted at the
 start of each increment of a
 `TimeBasedLinear` deployment. The step
 percentage must be 14% or greater.


*Required*: No






`BakeTimeMins`

The number of minutes between each incremental
 traffic shift of a `TimeBasedLinear`
 deployment.


*Required*: No









`AdditionalOptions`

Additional options for the blue/green deployment.


*Required*: No




`TerminationWaitTimeInMinutes`

Specifies time to wait, in minutes, before terminating the blue
 resources.


*Required*: No





`LifecycleEventHooks`

Use lifecycle event hooks to specify a Lambda function that CodeDeploy can
 call to validate a deployment. You can use the same function or a
 different one for deployment lifecyle events. Following completion of the
 validation tests, the Lambda `AfterAllowTraffic` function calls
 back CodeDeploy and delivers a result of `Succeeded` or
 `Failed`. For more information, see [AppSpec 'hooks' section](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html "https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html") in the *AWS CodeDeploy User
 Guide.*


*Required*: No




`BeforeInstall`

Function to use to run tasks before the replacement task set is
 created.


*Required*: No



`AfterInstall`

Function to use to run tasks after the replacement task set is
 created and one of the target groups is associated with it.


*Required*: No



`AfterAllowTestTraffic`

Function to use to run tasks after the test listener serves
 traffic to the replacement task set.


*Required*: No



`BeforeAllowTraffic`

Function to use to run tasks after the second target group is
 associated with the replacement task set, but before traffic is
 shifted to the replacement task set.


*Required*: No



`AfterAllowTraffic`

Function to use to run tasks after the second target group
 serves traffic to the replacement task set.


*Required*: No





`ServiceRole`

The execution role for CloudFormation to use to perform the blue-green
 deployments. For a list of the necessary permissions, see [IAM permissions for blue/green deployments](about-blue-green-deployments.md#blue-green-iam "about-blue-green-deployments.md#blue-green-iam").


*Required*: No



`Applications`

Specifies properties of the Amazon ECS application.


*Required*: Yes




`Target`


*Required*: Yes




`Type`

The type of the resource.


*Required*: Yes



`LogicalID`

The logical id of the resource.


*Required*: Yes





`ECSAttributes`

The resources that represent the various requirements of your
 Amazon ECS application deployment.


*Required*: Yes




`TaskDefinitions`

The logical ID of the [AWS::ECS::TaskDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html") resource
 to run the Docker container that contains your Amazon ECS
 application.


*Required*: Yes



`TaskSets`

The logical IDs of the [AWS::ECS::TaskSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskset.html") resources to use
 as task sets for the application.


*Required*: Yes



`TrafficRouting`

Specifies resources used for traffic routing.


*Required*: Yes




`ProdTrafficRoute`

The listener to be used by your load balancer to
 direct traffic to your target groups.


*Required*: Yes




`Type`

The type of the resource.
 `AWS::ElasticLoadBalancingV2::Listener`


*Required*: Yes



`LogicalID`

The logical ID of the resource.


*Required*: Yes





`TestTrafficRoute`

The listener to be used by your load balancer to
 direct traffic to your target groups.


*Required*: Yes




`Type`

The type of the resource.
 `AWS::ElasticLoadBalancingV2::Listener`


*Required*: Yes



`LogicalID`

The logical ID of the resource.


*Required*: No





`TargetGroups`

Logical ID of resources to use as target groups to
 route traffic to the registered target.


*Required*: Yes
