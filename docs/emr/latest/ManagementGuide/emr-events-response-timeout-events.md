# Responding to Amazon EMR cluster

instance fleet resize timeout events

## Overview

Amazon EMR clusters emit [events](emr-manage-cloudwatch-events.md#emr-cloudwatch-instance-fleet-resize-events "emr-manage-cloudwatch-events.md#emr-cloudwatch-instance-fleet-resize-events") while executing the resize operation for instance fleet clusters.
The provisioning timeout events are emitted when Amazon EMR stops provisioning Spot or
On-demand capacity for the fleet after the timeout expires. The timeout duration can
be configured by the user as part of the [resize specifications](../APIReference/API_InstanceFleetResizingSpecifications.md "../APIReference/API_InstanceFleetResizingSpecifications.md") for the instance fleets. In scenarios of
consecutive resizes for the same instance fleet, Amazon EMR emits the `Spot
 provisioning timeout - continuing resize` or `On-Demand provisioning
 timeout - continuing resize` events when timeout for the current resize
operation expires. It then starts provisioning capacity for the fleet’s next resize
operation.

## Responding to instance fleet

resize timeout events

We recommend that you respond to a provisioning timeout event in one of the
following ways:

- Revisit the [resize specifications](../APIReference/API_InstanceFleetResizingSpecifications.md "../APIReference/API_InstanceFleetResizingSpecifications.md") and retry the resize operation. As
  capacity shifts frequently, your clusters will successfully resize as soon
  as Amazon EC2 capacity becomes available. We recommend customers to configure
  lower values for the timeout duration for the jobs that require stricter
  SLAs.
- Alternatively, you can either:
  - Launch a new cluster with diversified instance types based on the
    [best practices for instance and Availability
    Zone flexibility](emr-flexibility.md#emr-flexibility-types "emr-flexibility.md#emr-flexibility-types") or
  - Launch a cluster with On-demand capacity

- For the provisioning timeout - continuing resize event, you can
  additionally wait for resize operations to be processed. Amazon EMR will
  continue to sequentially process the resize operations triggered for the
  fleet, respecting the configured resize specifications.

You can also set up rules or automated responses to this event as described in the
next section.

## Automated recovery from a

provisioning timeout event

You can build automation in response to Amazon EMR events with the `Spot
 Provisioning timeout` event code. For example, the following AWS Lambda
function shuts down an EMR cluster with an instance fleet that uses Spot instances
for Task nodes, and then creates a new EMR cluster with an instance fleet that
contains more diversified instance types than the original request. In this example,
the `Spot Provisioning timeout` event emitted for task nodes will trigger
the execution of the Lambda function.

###### Example function to respond to Spot Provisioning timeout event

```
// Lambda code with Python 3.10 and handler is lambda_function.lambda_handler
// Note: related IAM role requires permission to use Amazon EMR

import json
import boto3
import datetime
from datetime import timezone

SPOT_PROVISIONING_TIMEOUT_EXCEPTION_DETAIL_TYPE = "EMR Instance Fleet Resize"
SPOT_PROVISIONING_TIMEOUT_EXCEPTION_EVENT_CODE = (
    "Spot Provisioning timeout"
)

CLIENT = boto3.client("emr", region_name="us-east-1")

# checks if the incoming event is 'EMR Instance Fleet Resize' with eventCode 'Spot provisioning timeout'
def is_spot_provisioning_timeout_event(event):
    if not event["detail"]:
        return False
    else:
        return (
            event["detail-type"] == SPOT_PROVISIONING_TIMEOUT_EXCEPTION_DETAIL_TYPE
            and event["detail"]["eventCode"]
            == SPOT_PROVISIONING_TIMEOUT_EXCEPTION_EVENT_CODE
        )


# checks if the cluster is eligible for termination
def is_cluster_eligible_for_termination(event, describeClusterResponse):
    # instanceFleetType could be CORE, MASTER OR TASK
    instanceFleetType = event["detail"]["instanceFleetType"]

    # Check if instance fleet receiving Spot provisioning timeout event is TASK
    if (instanceFleetType == "TASK"):
        return True
    else:
        return False


# create a new cluster by choosing different InstanceType.
def create_cluster(event):
    # instanceFleetType cloud be CORE, MASTER OR TASK
    instanceFleetType = event["detail"]["instanceFleetType"]

    # the following two lines assumes that the customer that created the cluster already knows which instance types they use in original request
    instanceTypesFromOriginalRequestMaster = "m5.xlarge"
    instanceTypesFromOriginalRequestCore = "m5.xlarge"

    # select new instance types to include in the new createCluster request
    instanceTypesForTask = [
        "m5.xlarge",
        "m5.2xlarge",
        "m5.4xlarge",
        "m5.8xlarge",
        "m5.12xlarge"
    ]

    print("Starting to create cluster...")
    instances = {
        "InstanceFleets": [
            {
                "InstanceFleetType":"MASTER",
                "TargetOnDemandCapacity":1,
                "TargetSpotCapacity":0,
                "InstanceTypeConfigs":[
                    {
                        'InstanceType': instanceTypesFromOriginalRequestMaster,
                        "WeightedCapacity":1,
                    }
                ]
            },
            {
                "InstanceFleetType":"CORE",
                "TargetOnDemandCapacity":1,
                "TargetSpotCapacity":0,
                "InstanceTypeConfigs":[
                    {
                        'InstanceType': instanceTypesFromOriginalRequestCore,
                        "WeightedCapacity":1,
                    }
                ]
            },
            {
                "InstanceFleetType":"TASK",
                "TargetOnDemandCapacity":0,
                "TargetSpotCapacity":100,
                "LaunchSpecifications":{},
                "InstanceTypeConfigs":[
                    {
                        'InstanceType': instanceTypesForTask[0],
                        "WeightedCapacity":1,
                    },
                    {
                        'InstanceType': instanceTypesForTask[1],
                        "WeightedCapacity":2,
                    },
                    {
                        'InstanceType': instanceTypesForTask[2],
                        "WeightedCapacity":4,
                    },
                    {
                        'InstanceType': instanceTypesForTask[3],
                        "WeightedCapacity":8,
                    },
                    {
                        'InstanceType': instanceTypesForTask[4],
                        "WeightedCapacity":12,
                    }
                ],
                "ResizeSpecifications": {
                    "SpotResizeSpecification": {
                        "TimeoutDurationMinutes": 30
                    }
                }
            }
        ]
    }
    response = CLIENT.run_job_flow(
        Name="Test Cluster",
        Instances=instances,
        VisibleToAllUsers=True,
        JobFlowRole="EMR_EC2_DefaultRole",
        ServiceRole="EMR_DefaultRole",
        ReleaseLabel="emr-6.10.0",
    )

    return response["JobFlowId"]


# terminated the cluster using clusterId received in an event
def terminate_cluster(event):
    print("Trying to terminate cluster, clusterId: " + event["detail"]["clusterId"])
    response = CLIENT.terminate_job_flows(JobFlowIds=[event["detail"]["clusterId"]])
    print(f"Terminate cluster response: {response}")


def describe_cluster(event):
    response = CLIENT.describe_cluster(ClusterId=event["detail"]["clusterId"])
    return response


def lambda_handler(event, context):
    if is_spot_provisioning_timeout_event(event):
        print(
            "Received spot provisioning timeout event for instanceFleet, clusterId: "
            + event["detail"]["clusterId"]
        )

        describeClusterResponse = describe_cluster(event)

        shouldTerminateCluster = is_cluster_eligible_for_termination(
            event, describeClusterResponse
        )
        if shouldTerminateCluster:
            terminate_cluster(event)

            clusterId = create_cluster(event)
            print("Created a new cluster, clusterId: " + clusterId)
        else:
            print(
                "Cluster is not eligible for termination, clusterId: "
                + event["detail"]["clusterId"]
            )

    else:
        print("Received event is not spot provisioning timeout event, skipping")
```
