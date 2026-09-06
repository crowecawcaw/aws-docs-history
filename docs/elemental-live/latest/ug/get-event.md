

# Get event
<a name="get-event"></a>

Get a list of the inputs in the specified event.

There is no explicit command to get the dynamic playlist. But you can get the event in order to get information about the dynamic playlist.

Get Event is useful for obtaining the IDs of the inputs in the dynamic playlist and for parsing for the order in which they are listed in the XML.

Get Event includes the status of each input in these tags:
+ active tag. Possible values are true and false.
+ status tag. Possible values are preprocessing, pending, running, postprocessing, complete.
+ active\_input\_id tag. Only the currently active input has this tag. For that input, the active tag and the input\_ID specify the same value.

Get Event does not provide information about the prepare time or activate time on inputs on which you explicitly called Prepare with Specified Time or Activate with Specified Time. That information cannot be retrieved from Elemental Live; you must maintain the schedule outside of Elemental Live.

## HTTP Request and Response
<a name="get-event-http-request-and-response"></a>

### HTTP URL
<a name="get-event-http-url"></a>

```
GET http://<Live IP address>/live_events/<event ID>
```

### Response
<a name="get-event-response"></a>

XML content consisting of one event element that contains:
+ Various general tags.
+ One or more input elements that each contain:
  + A unique ID tag.
  + A unique input\_label tag (optional).
  + A status tag.
  + An input element: complete network\_input or device\_input or router\_input or file\_input.
  + A video\_selector element.
  + An optional audio\_selector element.
  + An optional caption\_selector element.
+ Other elements relating to input.
+ Other elements relating to outputs.

## Example
<a name="get-event-example"></a>

### Request
<a name="get-event-example-request"></a>

This request gets the event with the ID 31. 

```
GET http://10.4.136.92/live_events/31
```

### Response
<a name="get-event-example-response"></a>

The event contains three inputs, with IDs 64, 98, 99, and with input\_label tags “movie08E45\_section\_1”, “enigmatic\_car\_ad” and “best\_trowel\_ad”. 

```
<?xml version="1.0" encoding="UTF-8"?>
<live_event; href="/live_events/31" product="Elemental Live" version="2.25.0.12345">
  <id>31</id>
  .
  .
  .
  <input>
    <active>false</active>
    <id>64</id>
    <input_label>movie08E45_section_1</input_label>
    <loop_source>false</loop_source>
    <status>pending</status>
    .
    .
    .
    <network_input>
      <id>4</id>
      .
      .
      .
      <uri>udp://10.0.0.1:5005</uri>
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
  <input>
    <active>true</active>
    <id>98</id>
    <input_label>enigmatic_car_ad</input_label>
    <loop_source>false</loop_source>
    <status>pending</status>
    .
    .
    .
  </input>
  <input>
    <active>false</active>
    <id>99</id>
    <input_label>best_trowel_ad</input_label>
    <loop_source>false</loop_source>
    <status>pending</status>
    .
    .
    .
  </input>
  <active_input_id>98</active_input_id>
  <loop_all_inputs>true</loop_all_inputs>
  <status>running</status>
  .
  .
  .
</live_event>
```