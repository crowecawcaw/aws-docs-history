# Creating an ID namespace

target (provider services method)

This topic describes the process of creating an ID namespace target using the
**Provider services** method. This method uses a provider service called
LiveRamp. LiveRamp translates third-party encoded data from a source to a target during an
ID mapping workflow.

###### To create an ID namespace target (provider services)

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/ "https://console.aws.amazon.com/entityresolution/").
2. In the left navigation pane, under **Data preparation**, choose
   **ID namespaces**.
3. On the **ID namespaces** page, in the upper right corner, choose
   **Create ID namespace**.
4. For **Details**, do the following:
   1. For **ID namespace name**, enter a unique name.
   2. (Optional) For **Description**, enter an optional
      description.
   3. For **ID namespace type**, choose
      **Target**.

5. For **ID namespace method**, choose **Provider
   services**.

###### Note

AWS Entity Resolution currently offers the LiveRamp provider service as an ID namespace
method.

If you have a subscription to LiveRamp, then the status appears as
**Subscribed**.

For more information about how to subscribe to LiveRamp, see [Step 1: Subscribe to a provider service on
AWS Data Exchange](prepare-third-party-input-data.md#subscribe-provider-service "prepare-third-party-input-data.md#subscribe-provider-service"). 6. For **Target domain**, enter the LiveRamp client domain identifier
targeted for transcoding that LiveRamp provides. 7. (Optional) To enable **Tags** for the resource, choose
**Add new tag**, and then enter the **Key** and
**Value** pair. 8. Choose **Create ID namespace**.
The ID namespace target is created. After you create the ID namespaces (source and
target) required for an ID mapping workflow, you're ready to [Create the
ID mapping workflow](create-id-mapping-workflow.md "create-id-mapping-workflow.md").
