# Stop a deployment with CodeDeploy

You can use the CodeDeploy console, the AWS CLI, or the CodeDeploy APIs to stop deployments associated
with your AWS account.

###### Warning

Stopping an EC2/On-Premises deployment can leave some or all of the
instances in your deployment groups in an indeterminate deployment state. For more
information, see [Stopped and failed deployments](deployment-steps-server.md#deployment-stop-fail "deployment-steps-server.md#deployment-stop-fail").

###### You can either stop

a deployment or stop and roll back a deployment.

- [Stop a deployment (console)](#deployments-stop-console "#deployments-stop-console")
- [Stop a deployment (CLI)](#deployments-stop-cli "#deployments-stop-cli")

###### Note

If your deployment is a blue/green deployment through CloudFormation, you cannot perform this task in the CodeDeploy console. Go to the CloudFormation console to perform this task.

## Stop a deployment (console)

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, and then choose **Deployments**.

###### Note

If no entries are displayed, make sure the correct region is selected. On the
navigation bar, in the region selector, choose one of the regions listed in [Region and Endpoints](../../../general/latest/gr/rande.md#codedeploy_region "../../../general/latest/gr/rande.md#codedeploy_region") in the
_AWS General Reference_. CodeDeploy is supported in these regions only. 3. Choose the deployment you want to stop do one of the following:

    1. Choose **Stop deployment** to stop the deployment
     without a rollback.
    2. Choose **Stop and roll back deployment** to stop and
     roll back the deployment

For more information, see [Redeploy and roll back a deployment with
CodeDeploy](deployments-rollback-and-redeploy.md "deployments-rollback-and-redeploy.md").

###### Note

If **Stop deployment** and **Stop and roll back
deployment** are unavailable, the deployment has progressed to
a point where it cannot be stopped.

## Stop a deployment (CLI)

Call the [stop-deployment](../../../cli/latest/reference/deploy/stop-deployment.md "../../../cli/latest/reference/deploy/stop-deployment.md") command, specifying the deployment ID. To view
a list of deployment IDs, call the [list-deployments](../../../cli/latest/reference/deploy/list-deployments.md "../../../cli/latest/reference/deploy/list-deployments.md") command.
