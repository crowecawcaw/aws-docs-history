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

2. In the body of the request, include one
   `motion_image_inserter` element inside the
   `live_event` tag. Complete these tags:
   - `insertion_mode`: Set to HTML.
   - `motion_image_inserter_input`: Enter
     the location and file name of the HTML5 asset.

   If access to your local or mounted directory
   requires authentication, enter the user name and
   password.

3. Set the following tags to match the control you are
   using.

| Option for control       | Value for <active>                                                                                  | Value for <enable_rest> | Value for <enable_scte35> |
| ------------------------ | --------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------- |
| Authoring system control | false                                                                                               | false                   | false                     |
| REST API control         | true or false, depending on whether you<br>want the motion overlay to show when the event<br>starts | true                    | false                     |
| SCTE 35 control          | false                                                                                               | false                   | true                      |

For detailed information about the tags, see [Fields for an HTML5 asset](html5-set-up-event-fields.md "html5-set-up-event-fields.md").

```
<motion_image_inserter>
    <active>
    <enable_rest>
    <enable_scte35>
    <insertion_mode>
    <motion_image_inserter_input>
      <uri>
      <password>
      <username>
    </motion_image_inserter_input>
</motion_image_inserter>
```

4. The response repeats back the data that you posted with
   `<ID>` tags for many elements, including
   IDs for the following motion image inserter
   elements:
   - `motion_image_inserter`
   - `motion_image_inserter_input`

###### Example

The following request creates an event with the name
myLiveEvent and turns on the REST API control option.

```
POST http://198.51.100.22/live_events
-----------------------------------
  <?xml version="1.0" encoding="UTF-8"?>
      <live_event>
          <name>myLiveEvent</name>
          . . .
          <motion_image_inserter>
              <active>true</active>
              <enable_rest>true</enable_rest>
              <insertion_mode>html</insertion_mode>
              <motion_image_inserter_input>
                  <uri>http://myAuthorSystem/output/output?aspect=16.9</uri>
              </motion_image_inserter_input>
          </motion_image_inserter>
      </live_event>

```
