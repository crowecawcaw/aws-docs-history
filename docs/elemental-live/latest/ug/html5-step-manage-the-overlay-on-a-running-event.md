# Step D: Showing and hiding the motion overlay

If you have configured the motion overlay for [REST control](step-design-controls-html5.md#html5-controls-rest "step-design-controls-html5.md#html5-controls-rest"), start the
event , then enter REST API commands to show and hide the motion
overlay.

If you have configured the motion overlay for authoring system
control or SCTE 35 control, Elemental Live automatically shows and
hides the motion overlay. You don't have to intervene. You can stop
reading this section.

###### To show or hide the motion overlay on a running event

1. Enter a POST command as follows:

```
POST http://<Live IP Address>/live_events/<live event id>/motion_image_inserter
```

2. In the body of the request, include one
   `motion_image_inserter` element that contains
   only the `active` tag. Set the `active`
   to true to show the motion overlay, or set it to
   `false` to hide the motion overlay. See the
   examples after this procedure.
3. The response repeats back the data that you posted with
   `<ID>` tags for
   `motion_image_inserter` and
   `motion_image_inserter_input`.

###### **Example 1**

The following example shows the motion overlay
immediately.

```
POST http://198.51.100.22/live_events/33/motion_image_inserter
-------------------------------------------------------------
<motion_image_inserter>
    <active>true</active>
</motion_image_inserter>
```

###### **Example 2**

The following example hides the motion overlay
immediately.

```
POST http://198.51.100.22/live_events/33/motion_image_inserter
-------------------------------------------------------------
<motion_image_inserter>
    <active>false</active>
</motion_image_inserter>
```
