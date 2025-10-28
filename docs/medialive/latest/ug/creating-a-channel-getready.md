# Getting ready

We recommend that before you start creating the MediaLive channel, you [plan the workflow](container-planning-workflow.md "container-planning-workflow.md"). In both these
planning procedures, you obtain information that you need to create the channel. In
addition, you must create the inputs that you need. You won't be able to create the
channel unless you have created these inputs.

Here is the information that you need, listed in the order in which your will use it
when you create the channel:

- You need to know if you will run the channel in the AWS Cloud or on
  on-premises hardware in a MediaLive Anywhere cluster. Some features and resources are
  available only for one channel mode. For information, see [Running channels in AWS Elemental MediaLive Anywhere](feature-emla.md "feature-emla.md") . For information about deploying a MediaLive Anywhere cluster,
  see [Setting up AWS Elemental MediaLive Anywhere](setup-emla.md "setup-emla.md").
- You will need the following information when you follow the procedure in [Complete channel and input details](creating-a-channel-step1.md "creating-a-channel-step1.md"):
  - Whether you will implement any resiliency features of MediaLive, and
    particularly whether you will create a standard channel or a
    single-pipeline channel. You made these decisions in step 3 of [Preparing the upstream and downstream systems in a workflow](container-planning-uss-dss.md "container-planning-uss-dss.md").

- You will need the following information when you follow the procedure in
  [Attach inputs to the channel](creating-a-channel-step2.md "creating-a-channel-step2.md"):
  - The names of the input or inputs to use in this channel. You created
    the input or inputs in [Setup: Creating inputs](medialive-inputs.md "medialive-inputs.md").

- You will need the following information to create the input selectors, as part
  of the procedure in [Complete the settings for each input](creating-a-channel-step2a.md "creating-a-channel-step2a.md"):
  - The assets to extract from each input. You identified these assets in
    [Map the output encodes
    to the sources](channel-map-output-source.md "channel-map-output-source.md"), as part of planning the
    channel.

- You will need the following information when you follow the procedure in [Configure outputs](creating-a-channel-step4.md "creating-a-channel-step4.md"):
  - The output groups to create. You should have identified these output
    groups in step 1 of [Planning a MediaLive workflow](container-planning-workflow.md "container-planning-workflow.md").
  - The outputs to create. You should have designed the outputs and
    encodes (video, audio,and captions) when you [planned the
    channel](planning-the-channel-in-workflow.md "planning-the-channel-in-workflow.md").
  - Information about the destinations for the outputs of each output
    group. You obtained this information in step 7 of [Planning a MediaLive workflow](container-planning-workflow.md "container-planning-workflow.md").

- You will need the following information when you follow the procedure in the
  three steps that start with [Set up the video encode](creating-a-channel-step6.md "creating-a-channel-step6.md"):
  - Details about the output encodes (video, audio, and captions) to
    create in each output group. You made these decisions in [Planning the outputs in the channel](planning-the-channel-in-workflow.md "planning-the-channel-in-workflow.md").

###### Note

For information about additional steps for setting up a channel for use in a
multiplex program, see [Setting up a multiplex](setting-up-multiplex.md "setting-up-multiplex.md").
