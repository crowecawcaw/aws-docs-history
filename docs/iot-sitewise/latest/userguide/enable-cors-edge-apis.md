# Enable CORS on AWS IoT SiteWise Edge APIs

Enabling CORS (Cross-Origin Resource Sharing) on AWS IoT SiteWise Edge APIs allows web
applications to directly communicate with the APIs across different domains. This
enables seamless integration, real-time data exchange, and cross-domain data access
without intermediary servers or workarounds. CORS settings can be configured to
specify allowable origins, ensuring controlled cross-origin access.

###### Note

CORS is available for version 3.3.1 and later of the This feature is available
for version 3.3.1 and later of the `aws.iot.SiteWiseEdgeProcessor`
component. For more information, see [AWS IoT SiteWise processor](../../../greengrass/v2/developerguide/iotsitewise-processor-component.md "../../../greengrass/v2/developerguide/iotsitewise-processor-component.md") in the
_AWS IoT Greengrass Version 2 Developer Guide_.

###### To enable CORS on SiteWise Edge APIs

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Edge gateways**.
3. Select the SiteWise Edge gateway for which you want to enable CORS. You can
   enable CORS on the AWS IoT Greengrass V2 deployment type.
4. In the **Gateway configuration** section, choose the
   associated **Greengrass core device**.
5. In the **Deployments** tab, under **Greengrass
   devices**, select the appropriate deployment link.
6. Under **Actions** choose **Revise**,
   then **Revise deployment**.

###### Important

Creating a revised CORS enabled configuration replaces the device’s
current configuration. 7. In **Step 1, Specify target**, provide an optional
**Name** to identify the deployment. 8. In **Step 2, Select components - optional**, you can
leave all current selections as-is and choose
**Next**. 9. In **Step 3, Configure components - optional**, select
**aws.iot.SiteWiseEdgeProcessor**, and choose
**Configure component**. 10. In the Configuration update section, under Configuration to merge, enter
the following JSON:

```
{
    "AWS_SITEWISE_EDGE_ACCESS_CONTROL_ALLOW_ORIGIN": "*"
}
```

###### Note

Using `*` as the value for
`AWS_SITEWISE_EDGE_ACCESS_CONTROL_ALLOW_ORIGIN` allows
all origins. For production environments, it's recommended to specify
exact origin URLs for better security. 11. Choose **Confirm**. 12. Choose **Next** to proceed through remaining steps until
you arrive at **Step5, Review**. 13. Review your configuration changes, then choose **Deploy**
to apply the changes to your SiteWise Edge gateway.

###### Note

Alternatively, you can enable CORS by setting global the environmental
variable `AWS_SITEWISE_EDGE_ACCESS_CONTROL_ALLOW_ORIGIN` to
`*` on your AWS IoT SiteWise gateway.

###### Note

For authenticated proxy, `userinfo` must be included in the
`url` field in the proxy configuration rather than as a separated
`username` and `password` fields.

After the deployment is complete, CORS is enabled on your SiteWise Edge API, allowing
specified origins to make cross-origin requests to the API.
