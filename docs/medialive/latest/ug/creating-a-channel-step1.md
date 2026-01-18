# Complete channel and input details

The **Channel and input details** section of the **Create
channel** page lets you do the following in the MediaLive that you are
creating:

- Select the IAM role that AWS Elemental MediaLive will use to access the channel when the
  channel is running (started).
- Optionally select a template to use.
- Select the channel class.
- Complete input specification information.
- Set up tagging.

###### To provide channel and input details

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. Before creating a channel, make sure that you have [created the inputs](creating-input.md "creating-input.md") that you will attach to
   the channel.
3. On the MediaLive home page, choose **Create channel**, and in the
   navigation pane, choose **Channels**.

If you've created a channel before, you won't see the home page. In that case,
in the MediaLive navigation pane, choose **Channels**, and then
choose **Create channel**. 4. On the **Create channel** page, choose **Channel and
input details**. 5. Complete the sections:

    * In **General info**, for **Channel
     name**, type a name for your channel.
    * In **General info**, complete **IAM
     role**. See [IAM role and ARN](role-and-remember-arn.md "role-and-remember-arn.md").
    * You can optionally configure the channel by selecting and loading a
     channel template. For information about the **Channel
     template** section, see [Creating a channel from a
     template](creating-channel-template.md "creating-channel-template.md").
    * Your organization might have deployed a MediaLive Anywhere cluster, in order to
     run channels on on-premises hardware. In this case, complete the MediaLive Anywhere
     settings. You must specify the channel placement group that the channel
     belongs to, and the cluster that this channel placement group belongs
     to.


    If you were involved in [designing the MediaLive Anywhere clusters](emla-deploy-design-cluster.md "emla-deploy-design-cluster.md") in your organization, you
     should know which is the appropriate channel placement group and
     cluster. If you weren't involved in this design, you must obtain this
     information from the video engineer who was involved.


    ###### Warning

    Don't arbitrarily choose a channel placement group and cluster. If
     you do, it's possible that the channel won't run because it will be
     assigned to a node that can't handle this type of input, or that
     future channels won't run, because you have overloaded the channel
     placement group.
    * In **Channel class**, choose the class. See [Channel class](channel-class.md "channel-class.md").


    With a regular MediaLive channel, you can set up the channel as a standard
     channel or a single-pipeline channel.


    With a MediaLive Anywhere channel, you must set up the channel as a
     single-pipeline channel.
    * If you selected **SINGLE\_PIPELINE** for channel
     class, you can optionally configure **Linked channel
     settings** to set up this channel as a primary or follower
     channel for pipeline locking. See
     [Linked channels for single-pipeline
     channels](channel-class.md#linked-channels "channel-class.md#linked-channels").
    * In **Input specifications** and **CDI input
     specifications**, complete the fields to match your input.
     See [Input specifications settings](input-specification.md "input-specification.md").
    * In **Output delivery**, set up the channel to deliver
     output via the public internet or your Amazon VPC.


    With a regular MediaLive channel, you can set up in either way. For
     information about delivering via Amazon VPC, see [Delivering outputs via your VPC](delivery-out-vpc.md "delivery-out-vpc.md").


    With a MediaLive Anywhere channel, you must set up the channel to use the public
     internet.
    * In the **Tags** section, create tags if you want to
     associate tags with this channel. For more information, see [Tagging resources](tagging.md "tagging.md").

6. When ready, go to the [next
   section](creating-a-channel-step2.md "creating-a-channel-step2.md").
