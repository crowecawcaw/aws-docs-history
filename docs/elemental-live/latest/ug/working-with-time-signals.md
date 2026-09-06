

# Working with time signals
<a name="working-with-time-signals"></a>

Time signals inserted by the REST API can be one of the “ad avail” types, or some other type, depending on what you specify in the segmentation descriptor in the request.

**Effect of creating a time signal**  
Insertion of a time signal modifies the data stream as it is being encoded. 

The effect of time signals on other parts of the content depends on how the event is set up, as described in earlier chapters of this guide. So it depends on the Ad Avail mode, whether manifest decoration is enabled, blanking and blackout are enabled, and whether passthrough is enabled. 

## Insert a new time signal message
<a name="insert-a-new-time-signal-message"></a>

Inserts a SCTE-35 message of type time\_signal in the stream either immediately or at a specified time. The command always includes a start time (in the time tag) and a duration (included in the segmentation descriptor). 

**HTTP URL**

```
POST <IP address of Live node>/live_events/<ID of event>/time_signal
```

**Body of HTTP**

The XML body contains one **time\_signal** element containing the following tags:



- **time **
  - **Sub-tag:**
    - hours
    - minutes
    - seconds
    - frames
  - **Type:** integer 
  - **Value:** The start time. All fields are required. <br />Enter the time in 24-hour format. <br />To insert the message immediately (taking into account that there will be a small delay while the request is processed), enter 0 in all fields.

- **descriptors**
  - **Sub-tag:**  
  - **Type:** string
  - **Value:** Optional. A hexadecimal string containing time signal descriptor data in the form of a binary blob. See the SCTE-35 specification for details on the contents and format.<br />This descriptor includes the time signal duration, segmentation type ID, and other key information.



**Response**

The body of the response is XML content consisting of one **response** element containing the following tags:



- **tag**
  - **Sub-tag:**  
  - **Sub-sub-tag:**  
  - **Type:** integer
  - **Description:** A unique ID

- **signal\_time **
  - **Sub-tag:** hours / **Sub-sub-tag:**   / **Type:** integer
  - **Sub-tag:** minutes / **Sub-sub-tag:**   / **Type:** integer
  - **Sub-tag:** seconds / **Sub-sub-tag:**   / **Type:** integer
  - **Sub-tag:** frames / **Sub-sub-tag:**   / **Type:** integer
  - **Description:** The start time, repeated from the request.

- **message**
  - **Sub-tag:**  
  - **Sub-sub-tag:**  
  - **Type:** string
  - **Description:** A description of the action taken.

- **errors **
  - **Sub-tag:**   / **Sub-sub-tag:**   / **Type:**   / **Description:** Included only in an error response.
  - **Sub-tag:** error / **Sub-sub-tag:** code / **Type:**   / **Description:** An error code. 
  - **Sub-tag:** error / **Sub-sub-tag:** message / **Type:** string / **Description:** A human-readable error message.



A success response does not include the <errors> element. A failure response contains only the <tag> and <errors> elements. 

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
| Avail time | The requested start time of the ad avail, including the frame. This time is in the timecode specified in the event or profile. <br />This time is in the timecode specified in the event or profile. If timecode configuration source is Clock time, Local time, and Specified time, this time is a “clock time.” | 
| PTS (second occurrence) | The requested start time of the ad avail (with the frame converted to milliseconds). | 
| duration | The duration of the ad avail, if specified, in 24-hour format. | 
| Current NTP | The network time protocol (NTP) when the SCTE-35 message insertion request was received by Elemental Live. | 

## Insert a new time signal message example
<a name="insert-a-new-time-signal-example"></a>

The following shows a request to insert a SCTE-35 message immediately into the event that has ID 3. 

```
POST 10.4.136.95/live_events/3/time_signal
----------------------------------------
<time_signal>
  <time>
    <hours>0</hours>
    <minutes>0</minutes>
    <seconds>0</seconds>
    <frames>0</frames>
   </time>
  <descriptors>021B43554549000000027FBF030C54564E413130303030303031300000
  </descriptors>
 </time_signal>
```

The following shows an example success response for the request:

```
<response value="time_signal">
  <message> Inserted time signal at event time[1234], PTS[1234]. Signal time[1234] PTS[1234]. 
  </message> 
  <tag>1</tag> 
  <signal_time>
    <hours>0</hours>
    <minutes>0</minutes>
    <seconds>0</seconds>
  </signal_time> 
</response>
```

The following shows an example failure response for the request:

```
<response value="time_signal">
  <tag>1</tag> 
  <errors>
    <error>
     <code>1040</code>
     <message>Invalid time signal message</message>
    </error>
  </errors>
</response>
```