

# Insert a new splice insert message
<a name="insert-a-new-splice-insert-message"></a>

Inserts a SCTE-35 message of type splice\_insert in the stream either immediately or at a specified time. The command always includes a start time. It can also include a duration (which implies an end time). 

The command does not support inclusion of a segmentation descriptor, which means that the message is always considered to be an “ad avail.”

**HTTP URL**

```
POST <IP address of Live node>/live_events/<ID of event>/cue_point
```

**Body of HTTP**

The XML body contains one cue\_point elements containing the following tags:


<table>
<thead>
  <tr><th>Tag</th><th>Sub-tag</th><th>Type</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>event_id</td><td> </td><td>integer</td><td>Specify an ID for this SCTE-35 request to allow for canceling of the insertion later (<a href="cancel-a-pending-ad-avail.md">Cancel a pending ad avail</a>).<br />Or leave blank, in which case an ID is generated and returned in the response.</td></tr>
  <tr><td>splice_time</td><td> </td><td> </td><td>Include this in order to specify the insertion point relative to the stream timecode. Include either splice_time or splice_offset, not both.<br />See <a href="#splicetime">Specifying Time with splice_time Tag</a> for details.<br />Specify the time by including the hours, minutes, seconds, and frames tags. </td></tr>
  <tr><td> </td><td>hours</td><td>integer</td><td rowspan="3">The start time of the ad avail. All fields are required. <br />Enter the time in 24-hour format.<br />To insert the ad avail immediately (taking into account that there is a small delay while the request is processed), enter 0 in all fields.</td></tr>
  <tr><td> </td><td>minutes</td><td>integer</td></tr>
  <tr><td> </td><td>seconds</td><td>integer</td></tr>
  <tr><td> </td><td>frames</td><td>integer</td><td>The frame within the specified seconds at which to insert the ad avail.<br />If blank, the start time is the first frame in the specified second.</td></tr>
  <tr><td>splice_offset</td><td> </td><td>integer</td><td>The start time of the ad avail. Include either splice_time or splice_offset, not both.<br />Include in order to specify the start time for the ad avail as the specified milliseconds after the request is received. See <a href="#spliceoffset">Specifying Time with splice_offset Tag</a>.<br />Specify the milliseconds. The number cannot be negative.</td></tr>
  <tr><td>duration</td><td> </td><td>integer</td><td>Optional.<br />You can include a duration so that a start time is included and an end time is implied by the length of time for the duration. <br />Or you can omit the duration so that only a start time is included. If you omit the duration, you must enter a separate command for the end time. </td></tr>
</tbody>
</table>


**Specifying time with "splice\_time" tag**  
Use the splice\_offset tag to specify the start time as a specific clock time, for example, at 10:20:33. The time you specify must match the timecode format in the event, as specified by the** Timecode Config Source** field in the event or profile. For example, if you specify 10:20:33 and the event uses system clock, the message is inserted at 10:20:33 UTC. If the event uses local time, the message is inserted at 10:20:33 for the time zone of the node. 

To verify the timecode format in the event, submit a GET live\_events request and (in the response) read the value in the **timecodeconfig** tag.

Splice Time requires either knowing in advance to insert an ad avail at a given time, or obtaining the current time and inserting an offset so that the time is not missed. It is easier to use **Splice Time** when you know start times in advance. You can obtain the timecode of the content currently being encoded; see [Get current time](get-current-time.md).

**Specifying Time with "splice\_offset" Tag**  
You can use the **splice\_offset** tag to specify time as a number of milliseconds into the future from the moment at which the command is performed. This offset can be 0, which means to insert immediately. 

**Time of insertion of the message and time for the ad avail**  
The time the message is inserted and the start time for the ad avail are typically not identical. For example, you insert a message that says “insert an ad avail at 10:35:15:0”. The message is actually inserted in the content close to the moment that you enter the request. The downstream system won't act on the instruction (it won't insert the ad avail) until the specified time. 

So you can insert the message in advance of its targeted start time. In fact, it is a good idea to include some offset. But take care when calculating offset.
+ **Too little offset**: If you do not add enough offset, the specified time might have already passed. The ad avail might still be inserted in the video (at the current frame) but will be inserted too late for Elemental Live to act upon it. 

  For example, the command says “insert an ad avail at 10:35:15.0” but, if that time has passed, the message is inserted at 10:35:40.0 (for example). Elemental Live inserts the message if its request time is less than 1 hour after the targeted time. Otherwise, it discards the message. Note that the message is inserted in the content but it has a start time that has already passed.
+ **Too much offset**: The maximum offset is 6 hours. Within that range, the ad avail will be inserted at a timepoint (for example 10:35:20), and the command is “insert ad avail at 10:36:00.0, that is, in 40 seconds from now.”

**Splice offset and clock changes**

When you use splice offsets in a splice insert, you must restart the event whenever the clocks change to or from Standard Time. If you don’t restart the event, your splice inserts will permanently either be inserted at the wrong time or not be inserted at all.

These rules apply only if the event uses the local system clock, because this is the only type of clock that is affected by the clock change. 

If you don't plan for any splice inserts in the first few minutes after the clocks change, you can simply restart the event as soon as the clocks change in the region and time zone that the Elemental Live appliance is configured for. 

If your workflow does include plans for splice inserts just after the clocks change, follow these steps:
+ Determine the date and time that the clocks change,in the region and time zone that the Elemental Live appliance is configured for.
+ Identify all the splice insert commands that you plan to enter *before* the clocks change, and where the splice insert has an intended start time that is *after* the clocks change. For example, you plan to enter a command at 1:15 a.m. for a splice insert with a start time that is after the clocks change. Don't enter any of these commands.
+ As soon as the clocks change (so at approximately 2:00.01 a.m.), restart the event. Restart each event where the problem scenario applies.
+ After the event restarts, you can insert the splice insert commands that you previously didn’t enter. It's possible that the intended start time of one or more splice inserts has already passed. You might want to reschedule the start time for the splice inserts, or you might want to skip these splice inserts. 
+ You can then continue entering splice insert commands in the usual way.

**Response**

The body of the response is XML content consisting of one **response** element containing the following tags:


<table>
<thead>
  <tr><th>Tag</th><th>Sub-tag</th><th>Sub-sub-tag</th><th>Type</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>event_id</td><td> </td><td> </td><td>integer</td><td>The event ID of this SCTE-35 request. </td></tr>
  <tr><td>splice_time</td><td>hours</td><td> </td><td>integer</td><td rowspan="4">If splice_time was specified, the hour, minutes, seconds and frame at which to insert the ad avail.<br />If splice_offset was specified, all tags specify “0.”</td></tr>
  <tr><td> </td><td>minutes</td><td> </td><td>integer</td></tr>
  <tr><td> </td><td>seconds</td><td> </td><td>integer</td></tr>
  <tr><td> </td><td>frames</td><td> </td><td>integer</td></tr>
  <tr><td>splice_offset</td><td> </td><td> </td><td>integer</td><td>If splice_offset was specified, the time at which to insert the ad avail.<br />If splice_time was specified, this tag has a null value.</td></tr>
  <tr><td>message</td><td> </td><td> </td><td>string</td><td>A description of the action taken.</td></tr>
  <tr><td>errors</td><td> </td><td> </td><td> </td><td>Included only in an error response.</td></tr>
  <tr><td></td><td>error</td><td>code</td><td> </td><td>An error code. </td></tr>
  <tr><td> </td><td>error</td><td>message</td><td>string</td><td>A human-readable error message.</td></tr>
</tbody>
</table>


A success response does not include the <errors> element. A failure response contains only the <event\_id> and <errors> elements. 

**Example Message**  
The following shows an example message:  

```
<message>Inserted event [32] at event time[08:02:38], PTS[00:02:20.982]. Avail time[08:02:38 0f] PTS[08:02:38.023], duration[01:00:00.000]. Current NTP [15:18:05.712]</message>
```


| Data | Description | 
| --- | --- | 
| Inserted event [n] | The event ID for the ad avail request. | 
| event time | The requested start time of the ad avail, as per the original request. | 
| PTS (first occurrence) | The time at which the SCTE-35 message insertion request was received by Elemental Live, in a clock representation of the presentation timestamp (PTS). This PTS is a “timer”, not a clock time. | 
| Avail Time | The requested start time of the ad avail, including the frame. This time is in the timecode specified in the event or profile. For more information, see [About timecode configuration and timers](processing-options.md#about-timecode-configuration-and-timers).<br />This time is in the timecode specified in the event or profile. If the timecode configuration source is Clock time, Local time, and Specified time, this time is a “clock time.” | 
| PTS (second occurrence) | The requested start time of the ad avail (with the frame converted to milliseconds). | 
| duration | The duration of the ad avail, if specified, in 24-hour format. | 
| Current NTP | The network time protocol (NTP) when the SCTE-35 message insertion request was received by Elemental Live. | 

## Splice insert examples
<a name="splice-insert-examples"></a>

**Splice time**  
Insert a message into the event with the ID 3. Insert the message at 10 hours, 32 minutes, and 10 seconds, and give it a duration of 30 seconds. (The implied end time will be 10 hours ,32 minutes, and 40 seconds.) 

```
POST 10.4.136.95/live_events/3/cue_point
----------------------------------------
<cue_point>
<splice_time>	
<hours>10</hours>
<minutes>32</minutes>
	<seconds>10</seconds>
	<frames>0</frames>
</splice_time>
<duration>30</duration>
</cue_point>
```

The following shows a success response where splice\_offset was used in the request. The SCTE-35 request has an ID of 8.

```
<response value="cue_point"> 
  <event_id>8</event_id>
  <splice_time>
    <hours>0</hours>
    <minutes>0</minutes>
    <seconds>0</seconds>
    <frames>0</frames>
  </splice_time>
  <splice_offset>8000</splice_offset>
  <message> Inserted at PTS[1234]. Avail time[00:00:05.000] PTS[2345], duration[30].  
  </message> 
</response>
```

The following shows a failure response:

```
<response value="cue_point">
  <event_id>8</event_id>
  <errors>
    <error>
      <code>1040</code>
      <message>Preroll time must be positive integer</message>
    </error>
  <errors>
</response>
```

**Splice offset**  
Insert a message into the event with the ID 3. Insert the message 8000 milliseconds from the moment the command is performed. The message has a duration of 30 seconds.

```
POST 10.4.136.95/live_events/3/cue_point
----------------------------------------
<cue_point>
<splice_offset>8000</splice_offset>
<duration>30</duration>
</cue_point>
```