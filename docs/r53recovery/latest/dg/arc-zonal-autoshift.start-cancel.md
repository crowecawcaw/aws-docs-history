# Enabling and working with zonal autoshift

This section provides procedures for working with zonal autoshifts in Amazon Application Recovery Controller (ARC). After you enable zonal autoshift,
you can make changes to practice run configurations, start an on-demand practice run, cancel an in-progress shift,
including practice runs, or enable autoshift observer notifications.

## Enabling or disabling zonal autoshift

The steps here explain how to enable or disable zonal autoshift on the Amazon Application Recovery Controller (ARC) console.
To work with zonal autoshift programmatically, see the [Zonal Shift and Zonal Autoshift API Reference Guide](../../../arc-zonal-shift/latest/api/Welcome.md "../../../arc-zonal-shift/latest/api/Welcome.md").

When zonal autoshift is enabled, you authorize AWS to shift away application resource traffic from an Availability Zone
during events, on your behalf, to help reduce your time to recovery.

## To enable or disable zonal autoshift

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift](https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift "https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift").
2. Under **Resource zonal autoshift configurations**, choose a resource.
3. In the **Actions** menu, choose **Enable zonal autoshift**,
   then follow the steps to complete the update.

If the resource doesn't have a practice run configuration, **Enable zonal autoshift** is
not available. To configure a practice run configuration and enable zonal autoshift, choose **Configure zonal autoshift**.

###### Contents

- [Configuring, editing, or deleting a practice run configuration](arc-zonal-autoshift.edit-delete-practice-run.md "arc-zonal-autoshift.edit-delete-practice-run.md")
- [Canceling a zonal autoshift](arc-zonal-autoshift.canceling-an-autoshift.md "arc-zonal-autoshift.canceling-an-autoshift.md")
- [Starting a practice run zonal shift](arc-zonal-autoshift.start-practice-run.md "arc-zonal-autoshift.start-practice-run.md")
- [Canceling a practice run zonal shift](arc-zonal-autoshift.cancel-practice-run.md "arc-zonal-autoshift.cancel-practice-run.md")
- [Enabling or disabling autoshift observer notification](arc-zonal-autoshift.enable-autoshift-observer.md "arc-zonal-autoshift.enable-autoshift-observer.md")
