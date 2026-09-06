

# Turn on alarms for your portals in AWS IoT SiteWise
<a name="monitor-enable-alarms"></a>

**Note**  
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

**Note**  
End of support notice: AWS ended support for AWS IoT Events. For more information, see [AWS IoT Events end of support](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-end-of-support.html).

You can enable the alarms feature supported by AWS IoT Events for your portals so that portal administrators can create, edit, and delete AWS IoT Events alarm models in your SiteWise Monitor portals. Project owners can configure alarms. Project viewers can view alarm details. This section explains how you can use the AWS IoT SiteWise console to enable the alarms feature for your portals.

**Important**  
You can't create external alarms in your portals.
If you want to send alarm notifications, you must choose IAM Identity Center for the user authentication service.
The alarm notifications feature isn't available in the China (Beijing) AWS Region.

When you configure and create a portal, you can enable alarms and alarm notifications in **Step 2 Additional features**. Based on the user authentication service, choose one of the following options:

------
#### [ IAM Identity Center ]

![Additional features page for enabling alarms for portals.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/portal-create-console-enable-alarms-sso.png)


**To enable alarms for a portal**

1. (Optional) Choose **Enable alarms**.

   1. For **AWS IoT SiteWise access role**, use an existing role or create a role with the required permissions. This role requires the `iotevents:BatchPutMessage` permission and a trust relationship that allows `iot.amazonaws.com` and `iotevents.amazonaws.com` to assume the role.

1. (Optional) Choose **Enable alarm notifications**.

   1. For **Sender**, choose the sender.
**Important**  
You must verify the sender email address in Amazon SES. For more information, see [Verifying email addresses in Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html), in the *Amazon Simple Email Service Developer Guide*.

   1. For **AWS Lambda role**, use an existing role or create a role with the required permissions. This role requires the `lambda:InvokeFunction` and `sso-directory:DescribeUser`permissions and a trust relationship that allows `iotevents.amazonaws.com` and `lambda.amazonaws.com` to assume the role.

   1. For **AWS Lambda functions**, choose an existing Lambda function or create a function that manages alarm notifications. For more information, see [Managing alarm notifications](https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html) in the *AWS IoT Events Developer Guide*.

------
#### [ IAM ]

![Additional features page for enabling alarms for portals.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/portal-create-console-enable-alarms-iam.png)


**To enable alarms for a portal**
+ (Optional) Choose **Enable alarms**.

  1. For **AWS IoT SiteWise access role**, use an existing role or create a role with the required permissions. This role requires the `iotevents:BatchPutMessage` permission and a trust relationship that allows `iot.amazonaws.com` and `iotevents.amazonaws.com` to assume the role.

------

For more information about alarms in SiteWise Monitor, see [Monitoring with alarms](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html) in the *AWS IoT SiteWise Application Guide*.