# Configuring, editing, or deleting a practice run configuration

The steps in this section explain how to edit or delete a practice run configuration on the Amazon Application Recovery Controller (ARC) console.
To work with zonal autoshift programmatically, including changes to practice run configurations, see the
[Zonal Shift and Zonal Autoshift API Reference Guide](../../../arc-zonal-shift/latest/api/Welcome.md "../../../arc-zonal-shift/latest/api/Welcome.md").

If you delete a practice run configuration in the console, zonal autoshift is disabled.
Before you can delete a practice run configuration with an API operation, you must disable zonal autoshift. You can configure a practice
run without enabling zonal autoshift. However, for zonal autoshift to be enabled for a resource, you are required to have a practice run
configured for the resource.

# To configure a practice run

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift](https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift "https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift").
2. Choose **Configure zonal autoshift**.
3. Choose a resource to configure for zonal autoshift.
4. Choose to disable zonal autoshift if you don't want AWS to start an autoshift for a resource when there's an AWS event.
   You can continue with the wizard to configure a practice run configuration without enabling autoshifts, if you choose.
5. Choose options for practice runs for the resource. For alarms, you can do the following:
   - (Required) Specify at least one outcome alarm to monitor practice runs for this resource.
   - (Optional) Specify one or more blocking alarms for practice runs for this resource.For more information, see the **Alarms that you specify for practice runs** section in
     [Best practices when you configure zonal autoshift](arc-zonal-autoshift.md "arc-zonal-autoshift.md").

6. Optionally, specify blocked windows or allowed windows, to block ARC from starting practice runs or allow
   ARC to start practice runs for this resource. All dates and times are in UTC.
7. Select the check box to confirm that you have read the acknowledgement note.
8. Choose **Create**.

# To edit a practice run configuration

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift](https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift "https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift").
2. Under **Resource zonal autoshift configurations**, choose a resource.
3. In the **Actions** menu, choose **Edit practice run configuration**.
4. Make changes to the practice run configuration, to do one or more of the following:
   - For alarms, you can do the following:
     - For blocking alarms, you can add one or more alarms or delete alarms.
     - For outcome alarms, you can add one or more alarms or delete alarms.
       At least one outcome alarm is required, so you can't delete all of the outcome alarms in a configuration.

   - For blocked windows and allowed windows, you can add new dates or days and times, or you can remove or update
     existing dates or days and times. All dates and times are in UTC.

5. Choose **Save**.

# To delete a practice run configuration

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift](https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift "https://console.aws.amazon.com/route53recovery/zonalshift/home#/autoshift").
2. Under **Resource zonal autoshift configurations**, choose a resource.
3. In the **Actions** menu, choose **Delete practice run configuration**.
4. On the confirmation modal dialog, type `Delete`, and then choose **Delete**.

Note that deleting a practice run configuration in the console also disables zonal autoshift for the resource. Zonal
autoshift requires a practice run to be configured for the resource.
