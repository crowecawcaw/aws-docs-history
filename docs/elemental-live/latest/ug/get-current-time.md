

# Get current time
<a name="get-current-time"></a>

You can obtain the timecode of the frame that is currently being processed in the specified event. Refer to the following tables.

**HTTP URL**

```
POST <IP address of Live node>/live_events/<ID of event>/cue_point
```

**Body of HTTP**

The XML body contains one `cue_point` element containing the following tag:


| Tag | Type | Value | 
| --- | --- | --- | 
| get\_current\_time | Integer | Always 1 | 

**Response**

The body of the response contains one **response** element containing the following tags:


<table>
<thead>
  <tr><th>Tag</th><th>Sub-tag</th><th>Type</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>tag</td><td> </td><td>integer</td><td>A unique ID that could be used in the event_id in a new request to insert a splice_insert. See the explanation below this table.</td></tr>
  <tr><td>splice_time</td><td>hours</td><td>integer</td><td rowspan="4">The time (and frame) associated with the event at the moment that the API request was processed. Time is in 24-hour format. For general information about timecodes in events, see <a href="processing-options.md#about-timecode-configuration-and-timers">About timecode configuration and timers</a>.</td></tr>
  <tr><td> </td><td>minutes</td><td>integer</td></tr>
  <tr><td> </td><td>seconds</td><td>integer</td></tr>
  <tr><td> </td><td>frames</td><td>integer</td></tr>
  <tr><td>message</td><td> </td><td>string</td><td>A description of the time: the presentation timestamp (PTS) of the time and the time in NTP.</td></tr>
  <tr><td>splice_offset</td><td> </td><td> </td><td>Always 0. See the explanation below this table.</td></tr>
  <tr><td>value</td><td> </td><td>string</td><td>Always “cue_point.”</td></tr>
</tbody>
</table>


The response is provided in this format so that you could take the entire response, clean it up a bit (for example, changing the “tag” tag to “event\_id”), and use it as the body of a request to insert a spliceinsert (see [Insert a new splice insert message](insert-a-new-splice-insert-message.md).

## Get current time example
<a name="get-current-time-example"></a>

The following shows a request for the current timecode in the event that has the ID 15:

```
POST 10.4.136.95/live_events/15/cue_point
-----------------------------------
<cue_point>
  <get_current_time>1</get_current_time>
</cue_point>
```

The following shows an example response for the request:

```
<?xml version="1.0" encoding="UTF-8"?>
<response>
  <tag>1</tag>
  <splice_time>
    <hours>0</hours>
    <minutes>0</minutes>
    <seconds>2</seconds>
    <frames>23</frames>
  </splice_time>
  <message>PTS[00:00:02.969]. Current NTP [16:21:23.573].</message>
  <splice_offset>0</splice_offset>
  <value>cue_point</value>
</response>
```