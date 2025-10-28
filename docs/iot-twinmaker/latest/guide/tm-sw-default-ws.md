# Using the IoTSiteWiseDefaultWorkspace

When you opt in to the [AWS IoT SiteWiseAWS IoT TwinMaker
integration](../../../iot-sitewise/latest/userguide/integrate-tm.md "../../../iot-sitewise/latest/userguide/integrate-tm.md"), a default workspace named
`IoTSiteWiseDefaultWorkspace` is created and automatically synced
with AWS IoT SiteWise.

You can also use the AWS IoT TwinMaker `CreateWorkspace` API to create a
workspace named `IoTSiteWiseDefaultWorkspace`.

## Prerequisites

Before creating `IoTSiteWiseDefaultWorkspace`, make sure you have
done the following:

- Create an AWS IoT TwinMaker service-linked role. See [Using service-linked roles for
  AWS IoT TwinMaker](using-service-linked-roles.md "using-service-linked-roles.md")
  for more information.
- Open the IAM console at
  [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

Review the role or user and verify that it has permission to
`iotsitewise:EnableSiteWiseIntegration`.

If needed, add permission to the role or user:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iotsitewise:EnableSiteWiseIntegration",
 "Resource": "*"
 }
 ]
}`

```
