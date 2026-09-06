

# Deleting an auto scaling policy from your Amazon Aurora DB cluster
<a name="Aurora.Integrating.AutoScaling.Delete"></a>

You can delete a scaling policy using the AWS Management Console, the AWS CLI, or the Application Auto Scaling API.

## Console
<a name="Aurora.Integrating.AutoScaling.Delete.Console"></a>

You can delete a scaling policy by using the AWS Management Console.

**To delete an auto scaling policy for an Aurora DB cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**. 

1. Choose the Aurora DB cluster whose auto scaling policy you want to delete.

1. Choose the **Logs & events** tab.

1. In the **Auto scaling policies** section, choose the auto scaling policy, and then choose **Delete**.

## AWS CLI
<a name="Aurora.Integrating.AutoScaling.Delete.CLI"></a>

To delete a scaling policy from your Aurora DB cluster, use the [`delete-scaling-policy`](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/delete-scaling-policy.html) AWS CLI command with the following parameters:
+ `--policy-name` – The name of the scaling policy.
+ `--resource-id` – The resource identifier for the Aurora DB cluster. For this parameter, the resource type is `cluster` and the unique identifier is the name of the Aurora DB cluster, for example `cluster:myscalablecluster`.
+ `--service-namespace` – Set this value to `rds`.
+ `--scalable-dimension` – Set this value to `rds:cluster:ReadReplicaCount`.

**Example**  
In the following example, you delete a target-tracking scaling policy named `myscalablepolicy` from an Aurora DB cluster named `myscalablecluster`.  
For Linux, macOS, or Unix:  

```
aws application-autoscaling delete-scaling-policy \
    --policy-name {{myscalablepolicy}} \
    --resource-id cluster:{{myscalablecluster}} \
    --service-namespace rds \
    --scalable-dimension rds:cluster:ReadReplicaCount \
```
For Windows:  

```
aws application-autoscaling delete-scaling-policy ^
    --policy-name {{myscalablepolicy}} ^
    --resource-id cluster:{{myscalablecluster}} ^
    --service-namespace rds ^
    --scalable-dimension rds:cluster:ReadReplicaCount ^
```

## Application Auto Scaling API
<a name="Aurora.Integrating.AutoScaling.Delete.API"></a>

To delete a scaling policy from your Aurora DB cluster, use the [`DeleteScalingPolicy`](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_DeleteScalingPolicy.html) the Application Auto Scaling API operation with the following parameters:
+ `PolicyName` – The name of the scaling policy.
+ `ServiceNamespace` – Set this value to `rds`.
+ `ResourceID` – The resource identifier for the Aurora DB cluster. For this parameter, the resource type is `cluster` and the unique identifier is the name of the Aurora DB cluster, for example `cluster:myscalablecluster`.
+ `ScalableDimension` – Set this value to `rds:cluster:ReadReplicaCount`.

**Example**  
In the following example, you delete a target-tracking scaling policy named `myscalablepolicy` from an Aurora DB cluster named `myscalablecluster` with the Application Auto Scaling API.  

```
POST / HTTP/1.1
Host: autoscaling.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 219
X-Amz-Target: AnyScaleFrontendService.DeleteScalingPolicy
X-Amz-Date: 20160506T182145Z
User-Agent: aws-cli/1.10.23 Python/2.7.11 Darwin/15.4.0 botocore/1.4.8
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "PolicyName": "{{myscalablepolicy}}",
    "ServiceNamespace": "rds",
    "ResourceId": "cluster:{{myscalablecluster}}",
    "ScalableDimension": "rds:cluster:ReadReplicaCount"
}
```