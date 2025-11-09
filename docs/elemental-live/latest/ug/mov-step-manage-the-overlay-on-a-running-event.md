# Step C: Manage the motion overlay on a running event

After the event starts, the motion overlay that is configured in
the event runs at the specified time. When the event is running, you
can work with the motion overlay only via the REST API. You can
enter REST API commands to make the following changes:

- A different URL, to specify different content.
- A start time, the new position and size, and the specified
  loop behavior.

###### Note

Commands sent during an event change the event XML. Therefore,
if you export the XML and create a new event with it, the new
event will have any motion overlays set up as they were set
during the course of the event, not as they were when the event
was created.

###### To modify the motion overlay on a running event

1. Decide which fields you want to modify. For information about the types of
   changes that you can make, see the table [later in
   this section](#mov_api_changes "#mov_api_changes").
2. Enter a POST command to modify any of the image overlay
   parameters in the running event:

```
POST http://<Live IP Address>/live_events/<live event id>/motion_image_inserter
```

3. In the body of the request, include one
   `motion_image_inserter` element that contains
   the required tags. For more information about the tags, see
   [Using the REST API](mov-set-up-event-fields-api.md "mov-set-up-event-fields-api.md").
4. The response repeats back the data that you posted with
   `<ID>` tags for
   `motion_image_inserter` and
   `motion_image_inserter_input`.

###### **Example 1**

The following example request modifies the running event with
the ID 33. It sets up the currently defined motion overlay MOV to
run again at 20160102T030405.678Z.

```
POST http://198.51.100.22/live_events/33/motion_image_inserter
-------------------------------------------------------------
<motion_image_inserter>
    <action_time>20160102T030405.678Z</action_time>
    <active>true</active>
</motion_image_inserter>
```

###### **Example 2**

The following example request modifies the running event with
the ID 33. It stops the motion overlay. Notice that you include
**action_time** with an empty value so that
you clear the time currently specified in the XML. If you forget
to do this, Elemental Live might try to apply that time to the
next show/hide request.

```
POST http://198.51.100.22/live_events/33/motion_image_inserter
-------------------------------------------------------------
<motion_image_inserter>
    <action_time></action_time>
    <active>false</active>
</motion_image_inserter>
```

**Types of changes**

This table provides information about some of the changes you can make to a running
event via the REST API:

| State of motion overlay | Desired action                                           | How to use the `motion_image_inserter`<br>command                                                                                                                                                                                                                     | Tags to change                                                                                         |
| ----------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Not running             | Run the motion overlay immediately.                      | Enter the command to set the `active` tag<br>to `true` and set the<br>`<action_time>` tag to empty.                                                                                                                                                                   | `active``action_time`                                                                                  |
| Not running             | Run the motion overlay again at a specified<br>time.     | Enter the command to set the `active` tag<br>to `true` and set the<br>`<action_time>` tag to the desired<br>start time.                                                                                                                                               | `active``action_time`                                                                                  |
| Not running             | Run a different motion overlay of the same file<br>type. | Enter the command to change the motion overlay to<br>point to a different asset.<br>Set the `<active>` tag to<br>`true` and set the<br>`<action_time>` tag to the time you<br>want the start the new motion overlay. Set the<br>`<loop>` tag to `true` or<br>`false`. | All tags that apply to the current motion overlay<br>type.                                             |
| Running                 | Stop the running motion overlay.                         | Just before you want the motion overlay to stop,<br>enter the command to set the `active` tag to<br>`false`.                                                                                                                                                          | `active`                                                                                               |
| Running                 | Start the motion overlay.                                | To start the motion overlay again, enter the<br>command to set the `<active>` tag to<br>`true` and the<br>`<action_time>` tag set to the time<br>you want the motion overlay to begin.                                                                                | `active`                                                                                               |
| Running                 | Change to a different motion overlay.                    | Enter the command to change the motion overlay to a<br>different file.                                                                                                                                                                                                | All tags, not just the ones you want to change. If<br>you exclude a tag, the default value will apply. |
