

# Planning a MediaLive workflow
<a name="container-planning-workflow"></a>

From the point of view of AWS Elemental MediaLive, a live streaming workflow that includes MediaLive involves three systems: 
+ An *upstream system* that provides the video content to MediaLive.
+ MediaLive, which ingests the content and transcodes the content.
+ A *downstream system* that is the destination for the output that MediaLive produces.

You should plan that workflow before you start to create the channel. As the first stage in that planning, you must set up the upstream and downstream systems. As the second stage, you must plan the channel itself—identify the content to extract from the source content, and plan the outputs to produce.

**Important**  
This procedure describes planning the workflow starting from the output and then working back to the input. This is the most effective way to plan a workflow.

**Topics**
+ [Preparing the upstream and downstream systems in a workflow](container-planning-uss-dss.md)
+ [Planning the outputs in the channel](planning-the-channel-in-workflow.md)