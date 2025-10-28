# Turn off a canary release

To turn off a canary release deployment is to set the [`canarySettings`](../api/API_Stage.md#canarySettings "../api/API_Stage.md#canarySettings") to null to remove it from the stage.

You can disable a canary release deployment using the API Gateway console, the AWS CLI, or an AWS
SDK.

###### Topics

- [Turn off a canary release using the
  API Gateway console](#delete-canary-release-console "#delete-canary-release-console")
- [Turn off a canary release using the
  AWS CLI](#delete-canary-release-cli "#delete-canary-release-cli")

## Turn off a canary release using the

API Gateway console

To use the API Gateway console to turn off a canary release deployment, use the following
steps:

###### To turn off a canary release deployment

1. Sign in to the API Gateway console and choose an existing API in the main
   navigation pane.
2. In the main navigation pane, choose **Stages**, and then choose an existing stage.
3. Choose the **Canary** tab.
4. Choose **Delete**.
5. Confirm you want to delete the canary by choosing
   **Delete**.

As a result, the [`canarySettings`](../api/API_Stage.md#canarySettings "../api/API_Stage.md#canarySettings") property becomes `null` and
is removed from the deployment [stage](../api/API_Stage.md "../api/API_Stage.md"). You can verify this using the AWS CLI. For
example, see [Turn off a canary release using the
AWS CLI](#delete-canary-release-cli "#delete-canary-release-cli").

## Turn off a canary release using the

AWS CLI

The following [update-stage](../../../cli/latest/reference/apigateway/update-stage.md "../../../cli/latest/reference/apigateway/update-stage.md") command turns off
the canary release deployment:

```
aws apigateway update-stage \
    --rest-api-id abcd1234 \
    --stage-name canary \
    --patch-operations '[{"op":"remove", "path":"/canarySettings"}]'
```

The output looks like the following:

```
{
    "stageName": "prod",
    "accessLogSettings": {
        ...
    },
    "cacheClusterEnabled": false,
    "cacheClusterStatus": "NOT_AVAILABLE",
    "deploymentId": "nfcn0x",
    "lastUpdatedDate": 1511309280,
    "createdDate": 1511152939,
    "methodSettings": {
        ...
    }
}
```

As shown in the output, the [canarySettings](../api/API_Stage.md#canarySettings "../api/API_Stage.md#canarySettings") property is no longer present in the [stage](../api/API_Stage.md "../api/API_Stage.md") of a canary-disabled
deployment.
