

# Enabling and viewing thumbnails in the console
<a name="thumbnails-enable-view-console"></a>

You enable thumbnails separately in each flow. You can enable thumbnails when you are creating the flow, or you can enable them in an existing flow. 

After you have enabled thumbnails, MediaConnect automatically starts to generate them whenever the flow is active.

## Enabling when you create a flow
<a name="thumbnails-enable-on-create"></a>

In the flow that you are creating, go to the **Source monitor configuration** section, and move the **Thumbnails state** slider to **Enabled**. 

When you start the new flow, MediaConnect will start to generate thumbnails.

## Enabling in an existing flow
<a name="thumbnails-enable-existing"></a>

1. On the left navigation bar, choose **Flows**. Select the flow by its name. 

1. On the flow **Details** page, choose the **Sources** tab. In the **Source monitoring configuration** section, choose **Edit**. 

1. Move the **Thumbnails state** slider to **Enabled**, then choose **Update**.

If the flow is currently active, MediaConnect starts to generate thumbnails. You can enable and disable the thumbnails as often as you want, when the flow is active or inactive. 

## Viewing thumbnails
<a name="thumbnails-view-console"></a>

When thumbnails are enabled in an active flow, MediaConnect automatically generates thumbnails and displays them in the flow **Details** page, in the **Preview** section.

If the flow becomes inactive, the thumbnail preview stops refreshing. After a few seconds, the preview is replaced by a message.

**Viewing thumbnails on several flows**

You might open several instances of the MediaConnect console, one instance for each active flow. You can do this, but if you enable thumbnails in all the instances, there might be issues with displaying thumbnails in one or more of the instances.

We recommend that you enable thumbnails on only one active flow at a time, and disable it on other active flows. 

## Disabling thumbnails
<a name="thumbnails-disable-console"></a>

You can disable thumbnails on an active or inactive flow. If the flow is active, you don't have to stop it first.

Go to the flow **Details** page, choose the **Sources** tab, and move the **Thumbnails state** slider to **Disabled**. Then choose **Update**.