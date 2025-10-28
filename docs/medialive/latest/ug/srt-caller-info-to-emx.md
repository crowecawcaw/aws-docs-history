# Provide information to the downstream

system

The downstream system might need the source IP addresses of the one or two MediaLive
streams, so that they can allow these addresses to connect to them. If the downstream
system is MediaConnect, it definitely needs this information.

**On an AWS Cloud channel**

Read this information if your organization doesn't deploy MediaLive Anywhere.

- After you have created the channel, select the channel by its name. The
  channel details appear.

In the **Destinations** tab, find the **Egress
endpoints** section. Copy the one or two IP addresses. There is one
set of addresses for the channel, not one set for each output.

- Make a note of the IP addresses and label them correctly as pipeline 0 and
  pipeline 1. Give them to the downstream operator.
  **On a MediaLive Anywhere channel**

Read this information if your channel is a MediaLive Anywhere channel, which means that it is
running on an on-premises hardware, not in the AWS Cloud.

- Obtain the IP address of the Gateway into the network. You might need to speak
  to the network administrator in your organization. Give this address
  to the downstream operator.
