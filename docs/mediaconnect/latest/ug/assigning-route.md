# Managing routes in MediaConnect

After you've set up your router I/Os, you can control how content flows between them by
assigning and unassigning routes. A route connects an input to one or more outputs,
determining where your content goes. For example, you might route a live sports feed to
multiple regional broadcasters, send a studio production to both transmission and recording,
or direct archive content to specific distribution channels.

All routing happens inside MediaConnect, letting you switch sources immediately and send one
input to multiple outputs. You can manage everything from one place, even across different
AWS Regions, giving you centralized control of your resources.

MediaConnect provides two ways to manage your route assignments:

1. **Router control panel view**

This real-time control interface is ideal for live production. Like a traditional
broadcast router, it lets you make immediate changes and see them take effect immediately.
Visual indicators help you monitor your routes' status during live events. 2. **Router matrix view**

When you need to plan more complex changes, the matrix view lets you set up multiple
route changes at once. You can preview your changes before applying them, making it particularly
useful for scheduled program changes and complex routing scenarios. 3. **Output details page**

For quick changes to individual outputs, you can use the Take Input option on any output
details page. This method lets you select a new input for a single output without opening the
control panel or matrix view.
As you work with routes, remember that outputs are unassigned by default. You can take (assign)
an input from any compatible output, regardless of whether the output is active or in standby.
Taking a new input changes which source signal flows to the destination, similar to using a traditional
switching router. These routing changes don't affect your external endpoint connections between your
source and input, or between your output and destination.

This chapter shows you how to use both the router control panel view and the router matrix view to
manage your route assignments.

###### Topics

- [Using the router control panel view in
  MediaConnect](using-router-control-panel.md "using-router-control-panel.md")
- [Using the router matrix view in MediaConnect](using-router-matrix-editor.md "using-router-matrix-editor.md")
