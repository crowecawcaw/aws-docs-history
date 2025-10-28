# Promote a canary release

When you promote a canary release, the canary release replaces the current stage settings. Promoting a canary
release does not disable the canary on the stage. To disable a canary, you must remove the canary settings on the
stage. To promote a canary, do the following.

- Reset the [deployment
  ID](../api/API_Stage.md#deploymentId "../api/API_Stage.md#deploymentId") of the stage with the [deployment ID](../api/API_Stage.md#canarySettings "../api/API_Stage.md#canarySettings")
  settings of the canary. This updates the API snapshot of the stage with the
  snapshot of the canary, making the test version the production release as
  well.
- Update stage variables with canary stage variables, if any. This updates the
  API execution context of the stage with that of the canary. Without this update,
  the new API version may produce unexpected results if the test version uses
  different stage variables or different values of existing stage
  variables.
- Set the percentage of canary traffic to 0.0%.

###### Topics

- [Promote a canary release
  using the API Gateway console](#promote-canary-release-deployment-console "#promote-canary-release-deployment-console")
- [Promote a canary release using the
  AWS CLI](#promote-canary-release-cli "#promote-canary-release-cli")

## Promote a canary release

using the API Gateway console

To use the API Gateway console to promote a canary release deployment, do the
following:

###### To promote a canary release deployment

1. Sign in to the API Gateway console and choose an existing API in the primary
   navigation pane.
2. In the main navigation pane, choose **Stages**, and then choose an existing stage.
3. Choose the **Canary** tab.
4. Choose **Promote canary**.
5. Confirm changes to be made and choose **Promote canary**.

After the promotion, the production release references the same API version
(**deploymentId**) as the canary release. You can verify this
using the AWS CLI. For example, see [Promote a canary release using the
AWS CLI](#promote-canary-release-cli "#promote-canary-release-cli").

## Promote a canary release using the

AWS CLI

To promote a canary release to the production release using the AWS CLI commands,
call the `update-stage` command to copy the canary-associated
`deploymentId` to the stage-associated `deploymentId`, to
reset the canary traffic percentage to zero (`0.0`), and, to copy any
canary-bound stage variables to the corresponding stage-bound ones.

Suppose we have a canary release deployment, described by a stage similar to the
following:

```
{
    "_links": {
        ...
    },
    "accessLogSettings": {
        ...
    },
    "cacheClusterEnabled": false,
    "cacheClusterStatus": "NOT_AVAILABLE",
    "canarySettings": {
        "deploymentId": "eh1sby",
        "useStageCache": false,
        "stageVariableOverrides": {
            "sv2": "val3",
            "sv1": "val2"
        },
        "percentTraffic": 10.5
    },
    "createdDate": "2017-11-20T04:42:19Z",
    "deploymentId": "nfcn0x",
    "lastUpdatedDate": "2017-11-22T00:54:28Z",
    "methodSettings": {
        ...
    },
    "stageName": "prod",
    "variables": {
        "sv1": "val1"
    }
}
```

Use the following [update-stage](../../../cli/latest/reference/apigateway/update-stage.md "../../../cli/latest/reference/apigateway/update-stage.md") command to
promote the canary:

```
aws apigateway update-stage  \
    --rest-api-id {rest-api-id}  \
    --stage-name '{stage-name}'  \
    --patch-operations '[{
        "op": "replace",
        "value": "0.0",
        "path": "/canarySettings/percentTraffic"
      }, {
        "op": "copy",
        "from": "/canarySettings/stageVariableOverrides",
        "path": "/variables"
      }, {
        "op": "copy",
        "from": "/canarySettings/deploymentId",
        "path": "/deploymentId"
      }]'
```

The output will look like the following:

```
{
    "_links": {
        ...
    },
    "accessLogSettings": {
        ...
    },
    "cacheClusterEnabled": false,
    "cacheClusterStatus": "NOT_AVAILABLE",
    "canarySettings": {
        "deploymentId": "eh1sby",
        "useStageCache": false,
        "stageVariableOverrides": {
            "sv2": "val3",
            "sv1": "val2"
        },
        "percentTraffic": 0
    },
    "createdDate": "2017-11-20T04:42:19Z",
    "deploymentId": "eh1sby",
    "lastUpdatedDate": "2017-11-22T05:29:47Z",
    "methodSettings": {
        ...
    },
    "stageName": "prod",
    "variables": {
        "sv2": "val3",
        "sv1": "val2"
    }
}
```

Promoting a canary release to the stage does not disable the
canary and the deployment remains to be a canary release deployment. To make it a
regular production release deployment, you must disable the canary settings. For
more information about how to disable a canary release deployment, see [Turn off a canary release](delete-canary-deployment.md "delete-canary-deployment.md").
