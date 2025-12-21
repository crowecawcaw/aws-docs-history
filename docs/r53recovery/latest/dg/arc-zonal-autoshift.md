# Enabling or disabling autoshift observer notification

You can configure zonal autoshift to notify you, through Amazon EventBridge, whenever AWS starts an autoshift to shift
traffic away from a potentially impaired Availability Zone. You must configure this option in each AWS Region that
you want to receive notifications about. You do not have to configure any specific resources with zonal autoshift
to enable these separate notifications. For more information, see [Using zonal autoshift with Amazon EventBridge](eventbridge-zonal-autoshift.md "eventbridge-zonal-autoshift.md").

The steps in this section explain how to enable autoshift observer notification by using the Amazon Application Recovery Controller (ARC) console.
To work with zonal autoshift programmatically, see the [Zonal Shift and Zonal Autoshift API Reference Guide](../../../arc-zonal-shift/latest/api/Welcome.md "../../../arc-zonal-shift/latest/api/Welcome.md").

# To enable or disable autoshift

observer notification

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/](https://console.aws.amazon.com/route53recovery/zonalshift/home#/ "https://console.aws.amazon.com/route53recovery/zonalshift/home#/").
2. Under **Getting started**, choose **Enable autoshift observer notification**.
3. In the confirmation dialog box, choose **Enable observer notification**.
