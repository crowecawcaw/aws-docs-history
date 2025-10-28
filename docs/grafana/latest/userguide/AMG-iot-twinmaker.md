# Connect to an AWS IoT TwinMaker data source

###### Note

In workspaces that support version 9 or newer, this data source might require
you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

With Amazon Managed Grafana, you can add AWS IoT TwinMaker, a powerful industrial data analytics service, as
an app and data source in your Grafana workspace. With AWS IoT TwinMaker, you can create end-user
3D digital twin applications to monitor industrial operations. The AWS IoT TwinMaker is a service
that makes it faster for developers to create digital replicas of real-world systems,
helping more customers realize the potential of digital twins to optimize operations. The
AWS IoT TwinMaker for Grafana provides custom panels, dashboard templates, and a data source to
connect to your digital twin data.

## Adding the permission for AWS IoT TwinMaker to your

workspace user role

###### To add permissions for AWS IoT TwinMaker to your workspace user role, assume role

permission between Amazon Managed Grafana workspace and TwinMaker dashboard roles.

1. Go to [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Manually create a dashboard role. For more information about creating a
   dashboard role, see [To manually create a Grafana AWS IoT TwinMaker
   dashboard role](#iot-twinmaker-dashboard-role "#iot-twinmaker-dashboard-role").

## AWS IoT TwinMaker connection details

settings

###### Configure connection details settings

1. In the **Connection Details** menu, select the
   authentication provider (recommended: **Workspace IAM Role**).
2. Choose the **Default Region** you want to query.
3. In the **TwinMaker settings**, enter the AWS IoT TwinMaker
   workspace name.

## To manually create a Grafana AWS IoT TwinMaker

dashboard role

###### To manually create a Grafana AWS IoT TwinMaker dashboard role

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Locate your Amazon Managed Grafana workspace role in the summary. It appears as follows:

```
 AmazonGrafanaServiceRole-`random_ID`
```

3. Add the following inline policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`TwinMakerDashboardRole`"
 }
}`

```

4. Add a new inline policy for each dashboard role. Alternatively, add a list of
   role Amazon Resource Names (ARNs) on the **Resource**
   line.
5. Find your dashboard role in the IAM console. It should have a
   `SceneViewer` policy and, optionally, a `VideoPlayer`
   policy.
6. Choose the **Trust relationship** tab.
7. Choose **Edit trust relationship**.
8. Enter the following policy, replacing
   `AMGWorkspaceRoleArn` with the Arn from your
   account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "`AMGWorkspaceRoleARN`"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Example of an AWS IoT TwinMaker policy

The following is a minimal AWS IoT TwinMaker policy that you can attach to a dashboard
role. You must replace the values for the AWS IoT TwinMaker workspace ARN and ID, as well
as the Amazon S3 bucket ARN, based on your own resources.
