

# Push and pull AWS Cloud inputs
<a name="inputs-push-pull"></a>

When an input is being [deployed in the AWS Cloud](inputs-emla.md), it is categorized in terms of how MediaLive and the upstream system negotiate delivery:
+ Push input with handshake. 
+ Push input without handshake.
+ Pull input. 

There are different [limits](eml-limitations-and-rules.md#limits-inputs) and [charges](pricing.md) for push inputs compared to pull inputs.


<table>
<thead>
  <tr><th>MediaLive input type</th><th colspan="2">Category</th></tr>
</thead>
<tbody>
  <tr><td>CDI</td><td>Push</td><td></td></tr>
  <tr><td>HLS</td><td></td><td>Pull</td></tr>
  <tr><td>Link</td><td>Push</td><td></td></tr>
  <tr><td>MediaConnect</td><td>Push </td><td></td></tr>
  <tr><td>MediaConnect Router</td><td>Push </td><td></td></tr>
  <tr><td>MP4</td><td></td><td>Pull</td></tr>
  <tr><td>RTMP Pull</td><td></td><td>Pull</td></tr>
  <tr><td>RTMP Push</td><td>Push. See the note below</td><td></td></tr>
  <tr><td>RTP</td><td>Push</td><td></td></tr>
  <tr><td>SRT Caller</td><td></td><td>Pull</td></tr>
  <tr><td>SRT Listener</td><td>Push</td><td></td></tr>
  <tr><td>Transport Stream (TS) file</td><td></td><td>Pull</td></tr>
</tbody>
</table>


**Note about RTMP push inputs**

An RTMP push input works as follows: The source attempts to deliver to an endpoint that is specified in the MediaLive input. There must be a handshake between the source and the MediaLive channel so that the source has information about the status of the input. 

When you start the channel that includes this input, MediaLive responds to the handshake message and ingests it. When the channel is not running, MediaLive does not react; the source goes into a paused state. 