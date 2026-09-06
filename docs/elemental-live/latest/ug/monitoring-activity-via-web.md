

# Monitoring activity through the web interface
<a name="monitoring-activity-via-web"></a>

The operator can monitor dynamic playlist activity through the Elemental Live web interface.

1. On the web interface, display the Event Control tab. 

1. If the blue button specifies Control Panel, then the Details panel is currently displayed. Click the Control Panel button.

1. On the Control Panel, click Input Controls (below the Preview panel) to expand that section. The dynamic playlist appears.

![GUI input controls.](http://docs.aws.amazon.com/elemental-live/latest/ug/images/playlist_GUI_input_controls.png)


## Status information
<a name="status-information"></a>


| Input background | Icon in control column | State | 
| --- | --- | --- | 
| Green | Spinner icon | Active | 
| Green | Arrow icon | Prepared | 
| Brown | Arrow icon | Being prepared | 
| Gray | Arrow icon | Idle | 

The orange numbers down the left side are on-screen numbers, for display purposes only. 

The numbers in the ID column are the REST IDs of the inputs.

## Controls
<a name="controls"></a>

The operator can click the triangle to switch to that input. The input will become Active. Processing will stop on the current Active input.