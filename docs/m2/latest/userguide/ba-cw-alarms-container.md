

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Set up Amazon CloudWatch alarms for AWS Transform for mainframe Runtime on container
<a name="ba-cw-alarms-container"></a>

You can set up CloudWatch to have more visible notifications whenever your deployed applications encounter exceptions. This helps you to monitor your application log redirected to CloudWatch, and add an alarm to warn you of possible errors.

## Alarm setup
<a name="alarm-setup"></a>

With CloudWatch logs, you can configure any number of metrics and alarms, depending on your application and your needs.

Specifically, you can set up proactive alarms for usage alerts directly during your cluster creation, so that you get notified when errors occur. To highlight errors in the connection to the AWS Transform for mainframe control system, add a metric concerning the string "Error C" in the logs. You can then define an alarm that reacts to this metric. 