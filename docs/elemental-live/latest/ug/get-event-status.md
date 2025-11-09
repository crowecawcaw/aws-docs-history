# Get event status

Get the status of the inputs in the specified event.

There is no explicit command to get the status of the inputs
in the dynamic playlist. But you can get the event status in
order to get status information about the dynamic
playlist.

Warning: Get Event Status only works with the JSON format.
Therefore, the request header must include Accept:
application/json and Content-type:application/json

## HTTP request and response

### HTTP

URL

```
GET http://<Live IP address>/live_events/<event ID>/status
```

### Response

JSON content consisting of one live_event element that
contains:

- One outputs element and one output_groups
  element that each includes various tags.
- One active_input tag that contains the REST ID
  of the currently Active input.
- One inputs element that lists the inputs. The
  inputs appear in the order in which they were
  originally listed when the dynamic playlist was
  created. The following information appears for
  each input:

| Tag         | Value   | Description                                                                                                                                                                                                                                                                                                                       |
| ----------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id          | Integer | The unique REST ID for this<br>input                                                                                                                                                                                                                                                                                              |
| state       | String  | The state of the input:<br>• clear: The input is Activated or<br>Prepared.<br>• quarantined: The input is either<br>starting or is recovering from a failure<br>condition.<br>• pending: The input is Idle<br>• errored: A failure condition (as<br>defined by the failure_condition tag in<br>the event XML) has been triggered. |
| input_label | String  | The input label, if one was<br>created.                                                                                                                                                                                                                                                                                           |
| uri         | String  | The URI for a file input.                                                                                                                                                                                                                                                                                                         |

### Stage

and state

The state tag and active_input tag can provide some
information about the stage and state of each input:

| State tag   | active_input tag            | Stage and state                                                                                          |
| ----------- | --------------------------- | -------------------------------------------------------------------------------------------------------- |
| pending     | Does not specify this input | The input is one of:<br>• Idle and Unprepared<br>• Next-in-line and Unprepared                           |
| clear       | Does not specify this input | The input is one of:<br>• Idle and Prepared<br>• Active<br>• Next-in-line and Prepared                   |
| clear       | Specifies this input        | The input is:<br>• Active                                                                                |
| quarantined | Specifies this input        | The input is:<br>• Active                                                                                |
| errored     | Specifies this input        | A failure condition (as defined by<br>the failure_condition tag in the event<br>XML) has been triggered. |

Note that you cannot determine whether the input is
Next-in-line from the response to this Get. You must
maintain that information outside of Elemental Live.

## Example

```
GET http://10.4.136.92/live_events/47/status
{
  "live_event": {
    "id": "47",
    "status": "running",
    "outputs": [
      .
      .
      .
    ],
    "output_groups": [
      .
      .
      .
    ],
      .
      .
      .
    "active_input": "533761",
      .
      .
      .
    "inputs": [
      {
        "id": "29",
        "state": "pending",
        "input_label": "live_curling",
      },
      {
        "id": "30",
        "state": "clear",
      .
      .
      .

      },
      {
        "id": "30",
        "state": "pending",
        "input_label": null,
        "uri": "http://10.4.99.22/ads/best_trowel_ad.m3u8?_=0ap3000000580895"
      },
      {
        "id": "31",
        "state": "pending",
        "input_label": null,
        "uri": "http://10.4.99.22/ads/magic_scraper_ad/master.m3u8"
      },
      {
        "id": "32",
        "state": "pending",
        "input_label": null,
        "uri": "http://10.4.99.22/ads/enigmatic_car_ad/master.m3u8"
      },
      {
        "id": "33",
        "state": "pending",
        "input_label": null,
        "uri": "http://10.4.99.22/ads/chouette_toy_ad.m3u8"
      },
      .
      .
      .
    ],
    "alerts": [],
    "audio_level": "-7",
    "elapsed_time_in_words": "01:10:28"
  }
}

```
