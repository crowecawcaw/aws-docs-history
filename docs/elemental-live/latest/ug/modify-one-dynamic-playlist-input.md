# Modify one

dynamic playlist input

In the specified event (which must be currently running),
modify the specified dynamic playlist input (which must be
non-Active).

The input can be modified in any way, so long as it follows
the rules for inputs in a dynamic playlist, as described in
[Tips for elements and tags](add-dynamic-playlist-inputs.md#add-dynamic-playlist-tips-for-elements-and-tags "add-dynamic-playlist-inputs.md#add-dynamic-playlist-tips-for-elements-and-tags").

## HTTP Request and Response

### HTTP

URL

To specify the input by its REST ID:

```
PUT http://<Live IP address>/live_events/<event ID>/inputs/<input id>
```

To specify the input by the input label:

```
POST http://<Live IP address>/live_events/<event ID>/inputs/by_label/<input_label>
```

The input label is the value in the <input_label>;
you may have included this tag when you first created
the input. If you did not specify an input label, you
cannot use this signature to modify.

### Body of HTTP

XML content consisting of one input element that each
contains only the tags to modify.

### Response

200 OK for a successful request.

## Example

### Request

This request modifies the input with the ID 28 that is
in the event with the ID 31. It modifies the input so to
point to a different asset.

```
PUT http://10.4.136.92/live_events/31/inputs/28
-----------------------------------------------
<input>
  <network_input>
    <uri>udp://10.0.0.1:5005</uri>
  </network_input>
</input>

```
