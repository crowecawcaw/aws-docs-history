# Configure session timeouts for

AWS IoT SiteWise Edge

SiteWise Edge allows you to configure session timeouts for the SiteWise Edge API. This feature
enhances security by automatically terminating inactive sessions after a specified
time-period. This section guides you through the process of configuring the session
timeout using the AWS IoT SiteWise console.

###### Note

Session timeout configuration is available for version 3.4.0 and later of the
`aws.iot.SiteWiseEdgeProcessor` component. For more information,
see [AWS IoT SiteWise processor](../../../greengrass/v2/developerguide/iotsitewise-processor-component.md "../../../greengrass/v2/developerguide/iotsitewise-processor-component.md") in the
_AWS IoT Greengrass Version 2 Developer Guide_.

###### To configure a session timeout for a SiteWise Edge gateway

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Edge gateways**.
3. Choose the SiteWise Edge gateway where you want to configure the session
   timeout.

###### Note

You can configure the session timeout on the AWS IoT Greengrass V2 deployment
type. 4. In the **Gateway configuration** section, choose the
associated **Greengrass core device**. 5. In the **Deployments** tab, under **Greengrass
devices**, select the appropriate deployment link. 6. Under **Actions** choose **Revise**.
Read the warning, and then choose **Revise
deployment**.

###### Important

Creating a revised session timeout configuration replaces the device's
current configuration. 7. In **Step 1, Specify target**, provide an optional
**Name** to identify the revised deployment, and then
choose **Next**. 8. In **Step 2, Select components - optional**, you can
leave all current selections as-is and choose
**Next**. 9. In **Step 3, Configure components - optional**, select
**aws.iot.SiteWiseEdgeProcessor**, and choose
**Configure component**. 10. In the **Configuration update** section, under
**Configuration to merge**, enter the following
JSON:

```

{
    "AWS_SITEWISE_EDGE_SESSION_TIMEOUT_MINUTES": "240"
}

```

11. Set the value for `AWS_SITEWISE_EDGE_SESSION_TIMEOUT_MINUTES`
    in minutes. Session timeout values can be from 1 minute to 10080 minutes (7
    days). The default value is 240 minutes (4 hours).
12. Choose **Confirm**.
13. Choose **Next** to proceed through remaining steps until
    you arrive at Step 5, **Review**.
14. Review your configuration changes, then choose **Deploy**
    to apply the changes to your SiteWise Edge gateway.

###### Note

Alternatively, you can configure the session timeout by setting the global
environmental variable
**AWS_SITEWISE_EDGE_SESSION_TIMEOUT_MINUTES** to your
desired value (in minutes) on your SiteWise Edge gateway.

After the deployment is complete, the new session timeout configuration is applied
to your SiteWise Edge API.
