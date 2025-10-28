# Using the REST API

This description assumes that you are familiar with using the
REST API and with the XML body for a
`live_event`.

###### To configure the event using the REST API

1. Enter a POST or PUT command in the usual way. Use POST
   to create a new event. Use PUT to modify an existing
   event:

```
POST http://<Live IP Address>/live_events
```

```
PUT http://<Live IP Address>/live_events/<live event id>
```

2.  In the body of the request, include one
    `motion_image_inserter` element inside the
    `live_event` tag. You can configure some or
    all the information in the non-running event, but you must
    at least set the following tags:

        * `insertion_mode`
        * `enable_rest`

    Make sure that you configure for the desired motion
    overlay behavior when the event first starts:

        * If you want the motion overlay to appear as soon
         as the event starts, specify all the tags. Make sure
         that you set `active` to
         `true`, and make sure that you leave
         `action_time` empty.
        * If you don't want the motion overlay to appear as
         soon as the event starts, set `active` to
         `false`.

    You can configure the remaining tags after you've
    started the event, when you want to run the first motion
    overlay.

For detailed information about the tags, see [Fields for a PNG asset](png-set-up-event-fields.md "png-set-up-event-fields.md").

```
<motion_image_inserter>
    <action_time>
    <active>
    <enable_rest>
    <duration>
    <framerate_denominator>
    <framerate_numerator>
    <full_frame>
    <image_x>
    <image_y>
    <insertion_mode>
    <loop_input>
    <motion_image_inserter_input>
      <uri>
      <password>
      <username>
    </motion_image_inserter_input>
</motion_image_inserter>
```

3. The response repeats back the data that you posted with
   `<ID>` tags for many elements including
   IDs for the following motion image inserter
   elements:
   - `motion_image_inserter`
   - `motion_image_inserter_input`

###### Example

The following request creates an event with the name
myLiveEvent. The event includes a
`motion_image_inserter` section that inserts the
motion overlay at a specific time:

```
POST http://198.51.100.22/live_events
-----------------------------------
  <?xml version="1.0" encoding="UTF-8"?>
      <live_event>
          <name>myLiveEvent</name>
          . . .
          <motion_image_inserter>
              <action_time>10:16:23:10</action_time>
              <active>true</active>
              <enable_rest>true</enable_rest>
              <framerate_denominator>1001</framerate_denominator>
              <framerate_numerator>30000</framerate_numerator>
              <full_frame>false</full_frame>
              <left>100</left>
              <top>200</top>
              <insertion_mode>png</insertion_mode>
              <loop_input>true</loop_input>
              <motion_image_inserter_input>
                  <uri>/data/logo001.png</uri>
              </motion_image_inserter_input>
          </motion_image_inserter>
      </live_event>

```
