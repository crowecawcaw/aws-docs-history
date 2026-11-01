

# Input settings—Network input settings
<a name="input-network-input"></a>

The fields in the Network input settings section apply only to HLS inputs and multicast inputs. 
+ For HLS inputs, all the fields except **Multicast settings** apply.
+ For multicast inputs, only the **Multicast settings** apply. The **Source IP address** field filters the multicast group by the sender's address, for source-specific multicast (SSM).

  If the multicast input has a secondary source, leave this field empty. MediaLive rejects the channel if you set this field for an input that has a secondary source. If you use SSM, set the source IP addresses on the input instead, one for each copy of the stream (**Multicast source IP** and **Secondary source IP**). For more information, see [SMPTE 2022-7 seamless protection switching for multicast inputs](multicast-2022-7.md).