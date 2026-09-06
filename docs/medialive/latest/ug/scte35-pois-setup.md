

# Setting up for POIS signal conditioning
<a name="scte35-pois-setup"></a>

With POIS signal conditioning, the MediaLive channel and the POIS server must be set up with identical information.

## Required information
<a name="scte35-pois-get-ready"></a>

Obtain the following information from the POIS operator:
+ The *POIS server endpoint*. This is the URL of the POIS server that MediaLive will send events to. The URL must be reachable by MediaLive.
+ The *Acquisition point identity* and the *Zone identity* (optional). These two fields ensure that MediaLive and the POIS server have a common identifier for the channel.
+ POIS endpoint credentials, if the POIS server requires credentials.

## Set up the channel
<a name="scte35-pois-setup-procedure"></a>

You must configure the channel with information about the POIS server.

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. Display the details for the channel. In the **General settings** section, expand **Avail Configuration**.

1. Complete the fields as follows:
   + **Avail Settings**: **ESAM**
   + **POIS Endpoint**: The URL that you obtained from the POIS operator.
   + **Acquisition Point Identity**: The value that you obtained from the POIS operator.
   + **Zone Identity**: The value that you obtained from the POIS operator.
   + **Ad Avail Offset**: Enter 0 unless the POIS operator tells you to enter a different value. 
   + **POIS Endpoint Credentials** (optional): Complete these fields if your POIS server requires a username and password.