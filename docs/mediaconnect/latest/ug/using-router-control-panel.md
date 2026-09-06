

# Using the router control panel view in MediaConnect
<a name="using-router-control-panel"></a>

The router control panel view provides an intuitive interface for taking inputs and monitoring your routes in real time, similar to a traditional broadcast router. You can use the control panel to see your current routing assignments at a glance, and make immediate changes.

When routing content through the control panel, remember these key points:
+ Each output can take content from only one input at a time
+ Each input can send content to multiple outputs

**Tip**  
If you need to quickly change just one output, you can also take an input from the output details page. This alternative method works well for individual changes, while the control panel is better suited for managing multiple routes.

## Prerequisites
<a name="control-panel-prerequisites"></a>

Before you get started, ensure the following:
+ You have one or more router inputs
+ You have one or more router outputs
+ The router inputs and outputs are compatible for pairing

**Note**  
Outputs are checked for compatibility with inputs based upon routing scope and maximum bitrate. When the routing scope is set to regional for a router I/O, it is only compatible with I/O resources in the same AWS Region. To enable a router input or output for cross-region operation, set the routing scope to global.   
Also, router outputs are only compatible with router inputs of equal or lesser maximum bitrate. For example, if an input is 20 Mbps, you can't route it to an output that's set up for less than 20 Mbps. 

## Procedure
<a name="control-panel-procedure"></a>

Follow these procedures to review and assign routes in the control panel.<a name="review-control-panel-procedure"></a>

**To review the router control panel**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. Choose **Router control panel**. The control panel displays two main sections:
   + Input tiles represent your available content sources
   + Output tiles represent your available destinations

1. To see all of your router I/Os in the control panel, choose **Auto-select inputs** and **Auto-select outputs**.
   + Alternatively, you can manually select inputs and outputs in the **Configure control panel **pane. This is useful when managing a subset of routes, like those for a particular event or program.

1. (Optional) Customize your control panel experience with these options:
   + Turn on **Abbreviate resource names** to show shortened I/O names.
   + Select **Locked** to prevent accidental routing changes.
   + Select **Real-time control** to enable immediate routing changes.
**Important**  
Be careful when enabling real-time control. All changes take effect immediately, and your output takes the selected input in real time.

The following image shows the control panel with no active routes.

![MediaConnect router control panel showing input tiles and output tiles in the us-east-1 and us-west-2 Regions. All tiles show the I/O state ("Active" or "Standby").](http://docs.aws.amazon.com/mediaconnect/latest/ug/images/router-control-panel-no-active-routes.png)
<a name="make-changes-control-panel-procedure"></a>

**To make changes on the router control panel**

1. In the router control panel, select **Real-time control** to enable immediate routing changes.

1. Select an output to work with.

1. Choose what you want to do:

   1. To set up a new route: Select the input that you want your output to take.

   1. To change an existing route: Select a different input for your output to take.

   1. To remove an existing route: Deselect the current input.

1. Review the outcome:

   1. For a new route: You'll see a success message, and the input tile flashes yellow while the take is in progress. When the take is complete, the input is highlighted blue to indicate the new connection.

   1. For a cleared route: You'll see a success message appears, and the input tile's highlight will disappear.

   1. For a failed change: You'll see an error message explaining the problem, and your route won't change.

1. When you’re done making changes, choose **Locked** to change the control panel to read-only mode and prevent accidental takes.

In the following image, the blue highlight shows an active route between an input (`SportsCam-Main`) and an output (`ControlRoom-Monitor`).

![MediaConnect router control panel showing an active route between an input and output, with the route highlighted in blue.](http://docs.aws.amazon.com/mediaconnect/latest/ug/images/router-control-panel-active-routes.png)
