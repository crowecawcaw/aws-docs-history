

# Activate dynamic playlist input
<a name="activate-dynamic-playlist-input"></a>

In the specified event (which must be currently running), activate the specified dynamic playlist input either at the specified time or immediately.

The input being prepared must not be already Active.

## HTTP request and response
<a name="activate-dynamic-playlist-http-request-and-response"></a>

### HTTP URL
<a name="activate-dynamic-playlist-http-url"></a>

```
POST http://<Live IP address>/live_events/<event ID>/activate_input
```

### Body of HTTP
<a name="activate-dynamic-playlist-body-of-http"></a>

XML content consisting of one of the following:
+ One input\_id tag that contains the ID of the input to activate.

Or
+ One input\_label tag that contains the input\_label of the input to activate.

Or
+ One activate\_input element that contains:
  + One input\_id tag that contains the ID of the input to prepare or one input\_label tag that contains the input\_label of the input to prepare.
  + One utc\_time tag that contains the time at which to activate the input, in UTC time, down to the seconds and (optionally) fractional seconds.

### Response
<a name="activate-dynamic-playlist-response"></a>

The entire <input> element for the specified input.

## Example 1
<a name="activate-dynamic-playlist-example"></a>

### Request
<a name="activate-dynamic-playlist-example-request"></a>

In the event with the ID 31, activate the input with the input\_label “syndicated\_show\_231”.

```
POST http://10.4.136.92/live_events/31/activate_input
----------------------------------------------------
<input_label>syndicated_show_231</input_label>
```

### Response
<a name="activate-dynamic-playlist-example-response"></a>

The response returns the entire <input> element. In this example, this input has the ID 64.

```
<?xml version="1.0" encoding="UTF-8"?>
  <input>
    <active>true</active>
    <id>64</id>
    <input_label>syndicated_show_231</input_label>
    <loop_source>false</loop_source>
    <status>pending</status>
    .
    .
    .
    <file_input>
      <id>206</id>
      <uri>/data/server/13978.mp4</uri>
    </file_input>
    <video_selector>
      <id>2</id>
      .
      .
      .
    </video_selector>
    <audio_selector>
      <id>2</id>
      .
      .
      .
    </audio_selector>
    <input_info>
      .
      .
      .
    </input_info>
  </input>
```

## Example 2
<a name="activate-dynamic-playlist-example-2"></a>

In the event with the ID 31, activate the input with the ID 103 and activate the input at 2015123T235959.999:

```
<activate_input>
  <input_id>103</input_id>
  <utc_time>2015123T235959.999</utc_time>
</activate_input>
```