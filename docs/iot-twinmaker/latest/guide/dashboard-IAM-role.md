# Creating a dashboard IAM role

With AWS IoT TwinMaker, you can control data access on your Grafana dashboards. Grafana
dashboard users should have different permission scopes to view data, and in some cases, write
data. For example, an alarm operator might not have permission to view videos, while an admin
has permission for all resources. Grafana defines the permissions through datasources, where
credentials and an IAM role are provided. The AWS IoT TwinMaker datasource fetches AWS credentials
with permissions for that role. If an IAM role isn't provided, Grafana uses the scope of the
credentials, which can't be reduced by AWS IoT TwinMaker.

To use your AWS IoT TwinMaker dashboards in Grafana,
you create an IAM role and attach policies.
You can use the following templates to help you create these policies.

## Create an IAM policy

Create an IAM policy called ``YourWorkspaceId`DashboardPolicy` in the
IAM Console. This policy gives your workspaces access to Amazon S3 bucket and AWS IoT TwinMaker
resources. You can also decide to use [AWS IoT Greengrass Edge Connector for
Amazon Kinesis Video Streams](video-integration.md "video-integration.md"), which requires permissions for the Kinesis Video Streams and AWS IoT SiteWise assets configured
for the component. To fit your use case, choose one of the following policy
templates.

**1. No video permissions policy**
If you don't want to use the Grafana [Video Player panel](https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/panels/video-player/README.md "https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/panels/video-player/README.md"), create the policy using the following template.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "arn:aws:s3:::`amzn-s3-demo-bucket`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iottwinmaker:Get*",
 "iottwinmaker:List*"
 ],
 "Resource": [
 "arn:aws:iottwinmaker:us-east-1:`111122223333`:workspace/`workspaceId`",
 "arn:aws:iottwinmaker:us-east-1:`111122223333`:workspace/`workspaceId`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iottwinmaker:ListWorkspaces",
 "Resource": "*"
 }
 ]
}`

```

An Amazon S3 bucket is created for each workspace.
It contains the 3D models and scenes to view on a dashboard.
The [SceneViewer](https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/panels/scene-viewer/README.md "https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/panels/scene-viewer/README.md")
panel loads items from this bucket.

**2. Scoped down video permissions policy**
To limit access on the Video Player panel in Grafana, group your AWS IoT Greengrass Edge Connector for
Amazon Kinesis Video Streams resources by tags. For more information about scoping down permissions for
your video resources, see [Creating an AWS IoT TwinMaker video player policy](tm-video-policy.md "tm-video-policy.md").

**3. All video permissions**
If you don’t want to group your videos, you can make them all accessible from the Grafana
Video Player. Anyone with access to a Grafana workspace is able to play video for any
stream in your account, and have read only access to any AWS IoT SiteWise asset. This includes
any resources that are created in the future.

Create the policy with the following template:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucketName`/*",
 "arn:aws:s3:::`bucketName`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iottwinmaker:Get*",
 "iottwinmaker:List*"
 ],
 "Resource": [
 "arn:aws:iottwinmaker:us-east-1:`111122223333`:workspace/`workspaceId`",
 "arn:aws:iottwinmaker:us-east-1:`111122223333`:workspace/`workspaceId`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iottwinmaker:ListWorkspaces",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesisvideo:GetDataEndpoint",
 "kinesisvideo:GetHLSStreamingSessionURL"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:GetAssetPropertyValue",
 "iotsitewise:GetInterpolatedAssetPropertyValues"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:BatchPutAssetPropertyValue"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/EdgeConnectorForKVS": "*`workspaceId`*"
 }
 }
 }
 ]
}`

```

This policy template provides the following permissions:

- Read only access to an S3 bucket to load a scene.
- Read only access to AWS IoT TwinMaker for all entities and components in a workspace.
- Read only access to stream all Kinesis Video Streams videos in your account.
- Read only access to the property value history of all AWS IoT SiteWise assets in your account.
- Data ingestion into any property of a AWS IoT SiteWise asset tagged with the key
  `EdgeConnectorForKVS` and the value `workspaceId`.

## Tagging your camera AWS IoT SiteWise asset request video upload from edge

Using the Video Player in Grafana , users can manually request that video is
uploaded from the edge cache to Kinesis Video Streams. You can turn on this feature for any AWS IoT SiteWise asset
that's associated with your AWS IoT Greengrass Edge Connector for Amazon Kinesis Video Streams and that is tagged with the
key `EdgeConnectorForKVS`.

The tag value can be a list of workspaceIds delimited by any of the following
characters: `. : + = @ _ / -`. For example, if you want to use an AWS IoT SiteWise asset
associated with an AWS IoT Greengrass Edge Connector for Amazon Kinesis Video Streams across AWS IoT TwinMaker workspaces, you can
use a tag that follows this pattern: `WorkspaceA/WorkspaceB/WorkspaceC`. The
Grafana plugin enforces that the AWS IoT TwinMaker workspaceId is used to group AWS IoT SiteWise asset data
ingestion.

## Add more permissions to your dashboard

policy

The AWS IoT TwinMaker Grafana plugin uses your authentication provider to call AssumeRole on
the dashboard role you create. Internally, the plugin restricts the highest scope of
permissions you have access to by using a session policy in the AssumeRole call. For more
information about session policies, see [Session
policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session").

This is the maximum permissive policy you can have on your dashboard role for an
AWS IoT TwinMaker workspace:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucketName`/*",
 "arn:aws:s3:::`bucketName`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iottwinmaker:Get*",
 "iottwinmaker:List*"
 ],
 "Resource": [
 "arn:aws:iottwinmaker:us-east-1:`111122223333`:workspace/`workspaceId`",
 "arn:aws:iottwinmaker:us-east-1:`111122223333`:workspace/`workspaceId`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iottwinmaker:ListWorkspaces",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesisvideo:GetDataEndpoint",
 "kinesisvideo:GetHLSStreamingSessionURL"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:GetAssetPropertyValue",
 "iotsitewise:GetInterpolatedAssetPropertyValues"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:BatchPutAssetPropertyValue"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/EdgeConnectorForKVS": "*`workspaceId`*"
 }
 }
 }
 ]
}`

```

If you add statements that `Allow` more permissions, they won't work on
the AWS IoT TwinMaker plugin. This is by design to ensure the minimum necessary permissions are used
by the plugin.

However, you can scope down permissions further. For information, see [Creating an AWS IoT TwinMaker video player policy](tm-video-policy.md "tm-video-policy.md").

## Creating the Grafana Dashboard IAM role

In the IAM Console, create an IAM role called
``YourWorkspaceId`DashboardRole`. Attach the
 ``YourWorkspaceId`DashboardPolicy` to the role.

To edit the trust policy of the dashboard role, you must give permission for the
Grafana authentication provider to call `AssumeRole` on the dashboard role.
Update the trust policy with the following template:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "`ARN of Grafana authentication provider`"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For more information about creating a Grafana environment and finding
your authentication provider, see [Setting up your Grafana environment](grafana-environment.md "grafana-environment.md").
