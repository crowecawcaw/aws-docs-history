# Delete dynamic

playlist input

In the specified event (which must be currently running),
delete the specified non-Active input from the dynamic playlist.

You can also delete the dynamic playlist using Replace Dynamic
Playlist with an empty inputs in the Body. For more information,
see [Replace dynamic
playlist](replace-dynamic-playlist.md "replace-dynamic-playlist.md").

## HTTP Request and Response

### HTTP

URL

To specify the input by its REST ID:

```
DELETE http://<Live IP address>/live_events/<event ID>/inputs/<input ID>
```

To specify the input by the input label:

```
DELETE http://<Live IP address>/live_events/<event ID>/inputs/by_label/<input label>
```

The input label is the value in the <input_label>;
you may have included this tag when you first created
the input. If you did not specify an input label, you
cannot use this signature to delete.

### Response

200 OK for a successful request.

## Example

### Request

This request deletes the input with the label
“curling_83399” that is in the event with the ID 31.

```
DELETE http://10.4.136.92/live_events/31/inputs/by_label/83399
--------------------------------------------------------------

```
