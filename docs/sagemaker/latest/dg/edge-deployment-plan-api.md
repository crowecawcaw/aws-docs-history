# Deploy the Model Package Directly with SageMaker Edge Manager Deployment API

SageMaker Edge Manager provides a deployment API that you can use to
deploy models to device targets without AWS IoT Greengrass. It is useful in situations
where you want to update models independently of firmware updates or application
deployment mechanisms. You can use the API to integrate your edge
deployments into a CI/CD workflow to automatically deploy models once
you have validated your model for accuracy. The API also has convenient
rollback and staged rollout options for you to ensure models work well
in a particular environment before wider rollout.

To use the Edge Manager deployment API first compile and package
your model. For information on how to compile and package your model,
see [Prepare Your Model for Deployment](edge-getting-started-step2.md "edge-getting-started-step2.md").
The following sections of this guide show how you can create edge
deployments using SageMaker API, after you have compiled and packaged your
models.

###### Topics

- [Create an edge deployment plan](#create-edge-deployment-plan "#create-edge-deployment-plan")
- [Start the edge deployment](#start-edge-deployment-stage "#start-edge-deployment-stage")
- [Check the status of the deployment](#describe-edge-deployment-status "#describe-edge-deployment-status")

## Create an edge deployment plan

You can create an edge deployment plan with the [`CreateEdgeDeploymentPlan`](../APIReference/API_CreateEdgeDeploymentPlan.md "../APIReference/API_CreateEdgeDeploymentPlan.md") API. The deployment plan
can have multiple stages. You can configure each stage to rollout the
deployment to a subset of edge devices (by percentage, or by device
name). You can also configure how rollout failures are handled at each
stage.

The following code snippet shows how you can create an edge
deployment plan with 1 stage to deploy a compiled and package model to
2 specific edge devices:

```

import boto3

client = boto3.client("sagemaker")

client.create_edge_deployment_plan(
    EdgeDeploymentPlanName=`"edge-deployment-plan-name"`,
    DeviceFleetName=`"device-fleet-name"`,
    ModelConfigs=[
        {
            "EdgePackagingJobName": `"edge-packaging-job-name"`,
            "ModelHandle": `"model-handle"`
        }
    ],
    Stages=[
        {
            "StageName": `"stage-name"`,
            "DeviceSelectionConfig": {
                "DeviceSubsetType": "SELECTION",
                "DeviceNames": [`"device-name-1"`, `"device-name-2"`]
            },
            "DeploymentConfig": {
                "FailureHandlingPolicy": "ROLLBACK_ON_FAILURE"
            }
        }
    ]
)

```

Instead of specific devices, if you want to deploy to the model
to a percentage of devices in your fleet, then set the value of
`DeviceSubsetType` to `"PERCENTAGE"` and replace
`"DeviceNames": [`"device-name-1"`, `"device-name-2"`]` with
`"Percentage": `desired-percentage`` in the above example.

Stages can be added after the deployment plan has been created
with the [CreateEdgeDeploymentStage](../APIReference/API_CreateEdgeDeploymentStage.md "../APIReference/API_CreateEdgeDeploymentStage.md")
API, in case you want to start rolling out new stages after validating
your test rollout success. For more information about deployment
stages see [DeploymentStage.](../APIReference/API_DeploymentStage.md "../APIReference/API_DeploymentStage.md")

## Start the edge deployment

After creating the deployment plan and the deployment stages,
you can start the deployment with the [`StartEdgeDeploymentStage`](../APIReference/API_StartEdgeDeploymentStage.md "../APIReference/API_StartEdgeDeploymentStage.md")
API.

```

client.start_edge_deployment_stage(
    EdgeDeploymentPlanName=`"edge-deployment-plan-name"`,
    StageName=`"stage-name"`
)

```

## Check the status of the deployment

You can check the status of the edge deployment with the [DescribeEdgeDeploymentPlan](../APIReference/API_DescribeEdgeDeploymentPlan.md "../APIReference/API_DescribeEdgeDeploymentPlan.md")
API.

```

client.describe_edge_deployment_plan(
    EdgeDeploymentPlanName=`"edge-deployment-plan-name"`
)

```
