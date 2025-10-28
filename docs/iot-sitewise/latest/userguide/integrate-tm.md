# Integrate AWS IoT SiteWise and AWS IoT TwinMaker

Integrating with AWS IoT TwinMaker grants access to robust functionality in AWS IoT SiteWise, such as AWS IoT SiteWise data retrieval `ExecuteQuery` API
and advanced asset search in the AWS IoT SiteWise console. To integrate the services and use these features, you must first enable the integration.

###### Topics

- [Enabling the integration](#it-enable "#it-enable")
- [Integrating AWS IoT SiteWise and AWS IoT TwinMaker](#it-integrate "#it-integrate")

## Enabling the integration

Administrators can use AWS JSON policies to specify who has access to what. That is, which _principal_ can perform _actions_ on
what _resources_, and under what _conditions_. The `Action` element of a JSON policy describes the actions that you can use
to allow or deny access in a policy. For more information about AWS IoT SiteWise supported actions, see [Actions defined by AWS IoT SiteWise](../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-actions-as-permissions "../../../service-authorization/latest/reference/list_awsiotsitewise.md#awsiotsitewise-actions-as-permissions") in the
_Service Authorization Reference_.

For more information about AWS IoT TwinMaker service-linked role, see [Service-linked roles for AWS IoT TwinMaker](../../../iot-twinmaker/latest/guide/security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked "../../../iot-twinmaker/latest/guide/security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked") in the _AWS IoT TwinMaker User Guide_.

Before you can integrate AWS IoT SiteWise and AWS IoT TwinMaker, you must grant the following permissions that allow AWS IoT SiteWise to
integrate with an AWS IoT TwinMaker linked workspace:

- `iotsitewise:EnableSiteWiseIntegration` – Allows AWS IoT SiteWise to integrate with a linked
  AWS IoT TwinMaker workspace. This integration allows AWS IoT TwinMaker to read all your modeling information in AWS IoT SiteWise through an
  AWS IoT TwinMaker service-linked role. To enable this permission, add the following policy to your IAM role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iotsitewise:EnableSiteWiseIntegration"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Integrating AWS IoT SiteWise and AWS IoT TwinMaker

To integrate AWS IoT SiteWise and AWS IoT TwinMaker, you must have the following:

- AWS IoT SiteWise service-linked role set up in your account
- AWS IoT TwinMaker service-linked role set up in your account
- AWS IoT TwinMaker workspace with ID `IoTSiteWiseDefaultWorkspace` in your account in the Region.

### To integrate by using the AWS IoT SiteWise console

When you see the **Integration with AWS IoT TwinMaker** banner in the console, choose **Grant
permission**. The prerequisites are created in your account.

### To integrate by using the AWS CLI

To integrate AWS IoT SiteWise and AWS IoT TwinMaker by using the AWS CLI, enter the following commands:

1. Call `CreateServiceLinkedRole` with an `AWSServiceName` of `iotsitewise.amazonaws.com`.

```
aws iam create-service-linked-role --aws-service-name iotsitewise.amazonaws.com
```

2. Call `CreateServiceLinkedRole` with an `AWSServiceName` of `iottwinmaker.amazonaws.com`.

```
aws iam create-service-linked-role --aws-service-name iottwinmaker.amazonaws.com
```

3. Call `CreateWorkspace` with an `ID` of `IoTSiteWiseDefaultWorkspace`.

```
 aws iottwinmaker create-workspace --workspace-id IoTSiteWiseDefaultWorkspace
```
