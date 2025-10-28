# Activate

dynamic playlist input

In the specified event (which must be currently running),
activate the specified dynamic playlist input either at the
specified time or immediately.

The input being prepared must not be already Active.

## HTTP request and response

### HTTP URL

```
POST http://<Live IP address>/live_events/<event ID>/activate_input
```

### Body of HTTP

XML content consisting of one of the following:

- One input_id tag that contains the ID of the
  input to activate.

Or

- One input_label tag that contains the
  input_label of the input to activate.

Or

- One activate_input element that
  contains:
  - One input_id tag that contains the ID
    of the input to prepare or one
    input_label tag that contains the
    input_label of the input to
    prepare.
  - One utc_time tag that contains the
    time at which to activate the input, in
    UTC time, down to the seconds and
    (optionally) fractional seconds.

### Response

The entire <input> element for the specified
input.

## Example

1

### Request

In the event with the ID 31, activate the input with
the input_label “syndicated_show_231”.

```
POST http://10.4.136.92/live_events/31/activate_input
----------------------------------------------------
<input_label>syndicated_show_231</input_label>

```

### Response

The response returns the entire <input> element. In
this example, this input has the ID 64.

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

In the event with the ID 31, activate the input with the
ID 103 and activate the input at 2015123T235959.999:

```
<activate_input>
  <input_id>103</input_id>
  <utc_time>2015123T235959.999</utc_time>
</activate_input>

```
