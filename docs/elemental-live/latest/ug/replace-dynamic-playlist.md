# Replace dynamic

playlist

In the specified event (which must be currently running),
remove all non-Active inputs from the dynamic playlist and
append the specified file input or inputs. After this command,
only the Active input remains from the original dynamic
playlist; the rest of the dynamic playlist consists of new
inputs.

The dynamic playlist can only consist of file inputs; if you
want to add live inputs or live and file inputs, use Add Dynamic
Playlist Inputs.

There is no maximum to the number of inputs that can be added
using this command, and there is no maximum to the number inputs
that result in the event. For example, you can replace the 15
inputs currently in the event with 900 new inputs. Compare this
lack of restrictions to the restrictions that apply with Add
Dynamic Playlist Inputs.

You can use Replace Dynamic Playlist to clear the dynamic
playlist: create a Body consisting of an empty inputs element.

## HTTP request and response

### HTTP

URL

```
POST http://<Live IP address>/live_events/<event ID>/playlist
```

### Body of HTTP

XML content consisting of:

- One inputs element that contains:
  - One or more input elements that each
    contains one or more of the regular
    input tags. See [Elements and tags in an event
    input XML](elements-and-tags.md "elements-and-tags.md").

### Response

200 OK for a successful request.

## Example

This request specifies two inputs to the event with the ID 31. The first input is a live input, the second is a file
input. This list of inputs will replace the current dynamic
playlist, not including the currently active input.

```
POST http://10.4.136.92/live_events/31/playlist
---------------------------------------------
<inputs>
  <input>
    <input_label>movie08E45_section_1</input_label>
    <loop_source>false</loop_source>
    <network_input>
      <quad>false</quad>
      <uri>udp://10.0.0.1:5005</uri>
    </network_input>
    <audio_selector>
      <default_selection>true</default_selection>
      <track>1</track>
    </audio_selector>
  </input>
  <input>
    <input_label>enigmatic_car_ad</input_label>
    <loop_source></loop_source>
    <file_input>
      <uri>/data/server/ad13978.mp4</uri>
    </file_input>
    <audio_selector>
      <default_selection>true</default_selection>
      <track>1</track>
    </audio_selector>
  </input>
</inputs>

```
