

# Updating the flow size
<a name="flows-update-size"></a>

Updating the flow size allows you to modify the processing capacity and feature set that's available for your MediaConnect flow. 

**Important**  
You can only update **Medium** flows to **Large** or **Large** flows to **Medium**. 

## Prerequisites
<a name="flows-update-size-prerequsites"></a>
+  The following procedure assumes that you’ve already created a flow. 
+  The flow must be inactive. If the flow is active, you must [stop the flow first](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-stop.html). 
+  If you are updating the flow size from **Large** to **Medium** and the flow has an NDI® source or output, you must [update the source](source-update.md) to a standard source, [remove the NDI output](outputs-remove.md) (if exists), and [disable the NDI configuration](flows-update-ndi-configuration.md) before updating the flow size. 

## Procedure
<a name="flows-update-size-procedure"></a>

**To update the flow size of an existing flow (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. On the **Flows** page, choose the name of the flow that you want to update.

   The details page for that flow appears.

1. In the **Details** section, choose **Flow actions** and then choose **Update flow size**. 

1. Select the flow size. 

1. Choose **Update**.