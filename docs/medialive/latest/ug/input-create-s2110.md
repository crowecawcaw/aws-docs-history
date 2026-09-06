

# Creating a SMPTE 2110 input
<a name="input-create-s2110"></a>

This section describes how to set up the source content on the upstream system, and how to create an SMPTE 2110 input that connects the upstream system to MediaLive. Create the input before you create the channel that ingests the input.

**Note**  
SMPTE 2110 inputs are supported only on AWS Elemental MediaLive Anywhere deployments. For more information about these deployments, see [Setting up AWS Elemental MediaLive Anywhere](setup-emla.md).

With an SMPTE 2110 input, MediaLive connects to the multicast IP address when the channel starts and *pulls* the sources. 

To perform this setup, you must work with the video engineer in your organization who created the SDP files for the SMPTE 2110 source.

**Topics**
+ [Obtain information](setup-s2110-pull-obtain-info.md)
+ [Create a SMPTE 2110 input](setup-input-s2110-pull.md)