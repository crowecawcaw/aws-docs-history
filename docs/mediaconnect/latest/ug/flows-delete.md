

# Deleting a flow
<a name="flows-delete"></a>

When you delete an active flow, it immediately becomes unavailable to customers who are accessing the output directly from your AWS Elemental MediaConnect flow or through an entitlement. After you delete a flow, you can't recover it.

**Important**  
Some flows have outputs that are [created and managed by a MediaLive channel](https://docs.aws.amazon.com/medialive/latest/ug/input-create-push-mediaconnect.html). When managing this type of flow, keep in mind the following:  
If you **stop** the flow, MediaLive treats this as an input loss and the channel continues to run. 
If you **delete** the flow, MediaLive loses the input configuration, causing the channel to fail—even if the channel isn't currently ingesting the flow outputs.
Recommended action: Before deleting a flow with managed outputs, update the MediaLive channel to remove any references to the flow. This prevents instability or disruption to the channel. For instructions, see [Detaching an input](https://docs.aws.amazon.com/medialive/latest/ug/detach-input.html) in the MediaLive User Guide.

## Prerequisites
<a name="flows-delete-prerequisites"></a>
+ If the flow is active, you must stop the flow before you can delete it. For instructions, see [Stopping a flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-stop.html).

## Procedure
<a name="flows-delete-procedure"></a>

Follow these steps to delete a flow in MediaConnect.

**To delete a flow (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. On the **Flows** page, choose the name of the flow that you want to delete.

   The details page for that flow appears.

1. Review the **Status** field to verify that the flow is in **Standby** mode. 

1. If the flow status is **Active**, choose **Stop**. 

1. Choose **Delete**. 

   A confirmation message appears.

1. Choose **Delete flow**. 

   The flow is no longer viewable to customers who are accessing the output directly from your MediaConnect flow or through an entitlement. It might take up to five minutes for the flow to be deleted entirely.

**To delete a flow (AWS CLI)**
+ In the AWS CLI, use the `delete-flow` command:

  ```
  aws mediaconnect delete-flow --flow-arn {{arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame}} --profile {{PMprofile}}
  ```

  The following example shows the return value:

  ```
  {
    "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
    "Status": "DELETING"
  }
  ```