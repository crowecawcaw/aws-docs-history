

# Distributing content from MediaConnect to MediaLive
<a name="distribution-to-medialive"></a>

You can set up a flow in AWS Elemental MediaConnect so that it can distribute content to AWS Elemental MediaLive. With this setup, your MediaConnect flows can serve as upstream inputs for MediaLive channels, enabling MediaLive to process your video streams.

## Prerequisites
<a name="distribution-to-medialive-prerequisites"></a>

Before you begin, ensure that:
+ You have administrator permissions for MediaConnect
+ You can coordinate with someone who has administrator permissions for MediaLive

**Note**  
This page describes the process from the MediaConnect perspective, assuming coordination with someone managing MediaLive. One person can perform both roles if they have the necessary permissions.

## Procedure
<a name="distribution-to-medialive-procedure"></a>
+ [Step 1: Verify MediaLive permissions](#verify-permissions)
+ [Step 2: Get the MediaLive channel details](#get-channel-details)
+ [Step 3. Set up MediaConnect flows](#set-up-flows)
+ [Step 4: Connect with MediaLive and start your flows](#connect-to-medialive-and-start-flow)
+ [Step 5: Start the MediaLive channels](#start-channels)

### Step 1: Verify MediaLive permissions
<a name="verify-permissions"></a>

To use MediaConnect flows as inputs for MediaLive channels, first ensure MediaLive has the necessary permissions to work with your flows. This is a one-time setup.

**To verify permissions**
+ Check with your MediaLive operator that they’ve set up the necessary permissions for MediaLive to interact with your MediaConnect flows. They can choose their preferred approach:
  + **Simple option (recommended)**

    Use the `MediaLiveAccessRole`, which includes all necessary permissions for MediaLive to work with MediaConnect. For instructions, see [Create the trusted entity - simple option](https://docs.aws.amazon.com/medialive/latest/ug/setup-trusted-entity-simple.html). 
  + **Complex option**

    Create your own IAM policy and role if you need more specific custom permissions. Alternatively, you can add these specific MediaConnect permissions to an existing custom IAM policy and role. For instructions, see [Create the trusted entity - complex option](https://docs.aws.amazon.com/medialive/latest/ug/setup-trusted-entity-complex.html). 

**Result of this step**  
MediaLive now has the permissions needed to work with your flows, including creating and removing outputs and reading flow information. You can reuse this role for multiple channels and flows.

### Step 2: Get the MediaLive channel details
<a name="get-channel-details"></a>

Before you configure your flows, you need specific information about the MediaLive channel they'll connect to. The channel settings determine which AWS Region and Availability Zones you'll use for your flows.

**To get the channel details**

1. Coordinate with your MediaLive operator to get information about their channel. They can either use an existing channel, or [create a new channel](https://docs.aws.amazon.com/medialive/latest/ug/creating-channel-scratch.html) if they don’t have one already.

1. Ask them to provide you with the following information about the channel: 
   + AWS Region
   + Availability Zones
   + Channel type (single-pipeline or dual-pipeline) 

**Result of this step**  
You now have the information needed to create your flows in the correct AWS Region and Availability Zones.

### Step 3. Set up MediaConnect flows
<a name="set-up-flows"></a>

In this step, you create new flows (or identify existing ones) to serve as inputs for the MediaLive channel.

**To set up the flows**

1. Sign into the MediaConnect console.

1. Determine how many flows you need based on the MediaLive channel type:
   + **For a single-pipeline channel**

     You’ll need one flow in the same Availability Zone as the channel. 
   + **For a standard (dual-pipeline) channel**

     You’ll need two flows in different Availability Zones (matching the two MediaLive channel Availability Zones).

1. Decide whether to use existing flows or create new ones.
   + **If you’re using existing flows**

     Check that your flows meet these requirements:
     + They’re in the same Region as the MediaLive channel.
     + They have the correct number and placement of Availability Zones (as determined in step 2).
     + They have sufficient bandwidth capacity.
     + They haven’t reached their maximum number of outputs. (MediaLive automatically creates an output on each flow when you create an input in MediaLive). 

     If these requirements are met, skip to step 4. Otherwise, create new flows.
   + **If you’re creating new flows**

     [Create flows](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-create.html) in the same AWS Region as the MediaLive channel, ensuring the correct Availability Zone placement (as determined in step 2). 
**Tip**  
If you’re creating two flows, use names that are identical except for a suffix. For example, **sports\_event\_A** and **sports\_event\_B**. This will help the MediaLive operator match the flows to the input pipelines in MediaLive.

1. Take note of the Amazon Resource Name (ARN) for your flows, and share this information with the MediaLive operator. The flow ARNs look like this: 
   + `arn:aws:mediaconnect:us-west-1:111122223333:flow:1bgf67:sports_event_A`
   + `arn:aws:mediaconnect:us-west-1:111122223333:flow:9pmlk76:sports_event_B`

**Result of this step**  
Your flows are in the correct Region and Availability Zones, and are ready to connect to MediaLive inputs.

### Step 4: Connect with MediaLive and start your flows
<a name="connect-to-medialive-and-start-flow"></a>

Now that your flows are ready, you can provide their details to MediaLive and start them.

**To connect with MediaLive and start your flows**

1. Coordinate with your MediaLive operator:
   + Provide them the flow ARNs from [Step 3. Set up MediaConnect flows](#set-up-flows).
   + Inform them they can now create a MediaConnect input on the MediaLive channel using these flow ARNs.

1. In MediaConnect, start each flow that you set up in [Step 3. Set up MediaConnect flows](#set-up-flows).

**Note**  
You can start your flows before or after MediaLive creates their input - the order doesn't matter. MediaLive can add outputs to either a running flow or one that hasn't started yet.

**Result of this step**  
MediaLive automatically creates two endpoints on the input (even for single-pipeline channels) and establishes connections to your MediaConnect flows. Your flows are now running and ready to receive content from upstream sources.

### Step 5: Start the MediaLive channels
<a name="start-channels"></a>

After the MediaConnect flow is started, the final step is to start the MediaLive channel.

**To start the MediaLive channel**
+ Inform the MediaLive operator that they can now [start the channel](https://docs.aws.amazon.com/medialive/latest/ug/starting-stopping-deleting-a-channel.html) that’s configured to use the MediaConnect inputs.

**Result of this step**  
The MediaLive channel starts ingesting content from your flows and processing it according to the channel's configuration. 

This completes the setup process. Your MediaConnect flows are now serving as inputs for the MediaLive channel.

## Billing considerations
<a name="distribution-from-medialive-billing"></a>

When using MediaConnect as an input source for MediaLive, keep in mind the following considerations that can impact your costs:

**Billing impact when stopping MediaLive channels**
+ When you stop or pause a MediaLive channel that uses MediaConnect as inputs, the associated MediaConnect outputs don’t automatically stop as well. As a result, even though the MediaLive channel is no longer active, the MediaConnect output attempts to send data to it. This can lead to additional charges on your MediaConnect flows. 

**Mitigating additional charges**
+ To avoid incurring unnecessary charges in this scenario, we recommend that you manually stop your MediaConnect flows whenever the associated MediaLive channels are no longer in use. You can either stop the flows yourself, or work with your MediaLive team to do this.
+ If you work with a separate MediaLive team, we recommend that you have them notify you when they are pausing or stopping a MediaLive channel that uses your MediaConnect flows. That way, you can work together to temporarily stop the associated MediaConnect outputs during those periods, preventing additional charges. This coordination between the MediaLive and MediaConnect teams will help ensure you're only paying for the active usage of the services.

 For more information on the pricing and billing implications of using MediaConnect, see the [Pricing](https://docs.aws.amazon.com/mediaconnect/latest/ug/what-is-pricing.html) section of this guide. 