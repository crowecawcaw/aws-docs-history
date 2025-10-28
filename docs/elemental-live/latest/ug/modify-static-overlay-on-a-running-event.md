# Modify

static overlay on a running event

In a running event, you can use the REST API to add more static overlays, modify
the behavior of an existing static overlay, or delete an existing static
overlay.

###### Note

Commands sent during an event change the event XML. Therefore, if you export
the XML and create a new event with it, the new event will have any overlays set
up as they were set during the course of the event, not as they were when the
event was created.

## HTTP

request and response

**HTTP URL - one input**

To add, modify, or delete the static overlay in one input element.

```
POST http://<Live IP Address>/live_events/<id>/image_inserter/input/<input id>
```

Where `<input id>` is the unique ID automatically assigned to
this input when the event is created or when the input is added to the event.

or:

```
POST http://<Live IP Address>/live_events/<id>/image_inserter/input/by_label/<input label>
```

Where `<input label>` is the input label you assigned when you
created this event or created this input. Input labels are always optional.

**HTTP URL - all outputs**

To add, modify, or delete the static overlay in all outputs.

```
POST http://<Live IP Address>/live_events/<id>/image_inserter
```

**HTTP URL - one output**

To add, modify, or delete the static overlay in one output.

```
POST http://<Live IP Address>/live_events/<id>/image_inserter/output/<output id>
```

Where `<output id>` is the unique ID automatically assigned to
this output when the event is created.

**HTTP URL - outputs for one stream
assembly**

To add, modify, or delete the static overlay in the outputs associated with a
given stream.

```
POST http://<Live IP Address>/live_events/<id>/image_inserter/output/by_stream/<stream id>
```

Where `<stream id>` is the `<ID>` automatically
assigned to this stream when the event is created. The ID can change while the
event is running (for example, if another stream is deleted), so you may need to
obtain the current ID before sending this command.

**Body of request**

XML content consisting of:

- One or more image_inserter elements that each contains:
  - 1 to 8 <image> elements that each contains the tags in the table
    in the section [Create or modify a non-running event with static graphic
    overlay](create-or-modify-a-non-running-event-with-static-graphic-overlay.md "create-or-modify-a-non-running-event-with-static-graphic-overlay.md").

For information about the tags to include for different actions, see [Types of
changes](step-c-manage-overlays-on-a-running-event.md#static-overlay-types-of-changes "step-c-manage-overlays-on-a-running-event.md#static-overlay-types-of-changes").

**Response**

The response repeats back the data that you posted with `<ID>`
tags for `image_inserter` and each overlay. If the event is not
running, the message “Event <ID> is not running” is returned.

## Example

The following request modifies the overlays in the event with the ID 16. It
modifies the start time on the existing overlay in layer 3.

It also adds one overlay (in layer 4); if an overlay already exists in layer 4,
that overlay is replaced with the new overlay (even if that overlay is currently
running). If an overlay does not exist in layer 4, the overlay is added.

```
POST http://198.51.100.22/live_events/16/image_inserter
```

```
<?xml version="1.0" encoding="UTF-8"?>
  <image_inserter>
    <image>
      <activate>true</activate>
      <layer>3</layer>
      <start_time>17:09:09:10</start_time>
    </image>
    <image>
      <activate>true</activate>
      <duration>30000</duration>
      <fade_in>10</fade_in>
      <fade_out>10</fade_out>
      <height>900</height>
      <left>300</left>
      <top>400</top>
      <layer>4</layer>
      <start_time>16:09:09:10</start_time>
      <width>800</width>
      <image_inserter_input>
        <uri>mnt/storage/logo.bmp</uri>
      </image_inserter_input>
    </image>
  </image_inserter>
```
