# Prepare dynamic

playlist input

In the specified event (which must be currently running),
manually prepare the specified dynamic playlist input either at
the specified time or immediately.

The input being prepared must not be already Active.

## HTTP Request and Response

### HTTP

URL

```
POST http://<Live IP address>/live_events/<event ID>/prepare_input
```

### Body of HTTP

XML content consisting of one of the following:

- One input_id tag that contains the ID of the
  input to prepare.

Or

- One input_label tag that contains the
  input_label of the input to prepare.

Or

- One prepare_input element that
  contains:
  - One input_id tag that contains the ID
    of the input to prepare or one
    input_label tag that contains the
    input_label of the input to
    prepare.
  - One utc_time tag that contains the
    time at which to prepare the input, in
    UTC time, down to the seconds and
    (optionally) fractional seconds.

### Response

The entire <input> element for the specified
input.

## Example

1

### Request

In the event with the ID 31, prepare the input with
the label “live_news_feed”.

```
POST http://10.4.136.92/live_events/31/prepare_input
----------------------------------------------------
<input_id>live_news_feed</input_id>

```

### Response

The response returns the entire <input> element. In
this example, this input has the ID 194.

```
<?xml version="1.0" encoding="UTF-8"?>
  <input>
    <active>true</active>
    <id>194</id>
    <input_label>live_news_feed</input_label>
    <loop_source>false</loop_source>
    <status>pending</status>
    .
    .
    .
    <network_input>
      <id>296</id>
      <uri>udp://10.255.10.41:5001</uri>
    </network_input>
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

## Example

2

In the event with the ID 31, prepare the input with the ID
103 and activate the input at 2015123T235959.999:

```
<prepare_input>
  <input_id>103</input_id>
  <utc_time>2015123T235959.999</utc_time>
</prepare_input>

```
