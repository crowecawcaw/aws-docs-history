

# Creating a control panel in ARC
<a name="routing-control.create-control-panel"></a>

A control panel in Amazon Application Recovery Controller (ARC) lets you group together related routing controls. A control panel can have routing controls that represent a microservice within an application, an entire application itself, or a group of applications, depending on the scope of your failover. A benefit of grouping routing controls into a control panel is that you can use safety rules with a control panel to help safeguard traffic routing changes. 

When you create a cluster, ARC creates a default control panel. You can use the default control panel for your routing controls, or you can create one or more control panels to group your routing controls. Note that only ASCII characters are supported for control panel names.

The steps to create a control panel on the ARC console are included in this section. For information about using recovery control configuration API operations with ARC, see the [Routing control API operations](actions.routing-control.md).

# To create a control panel


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Routing control**.

1. On the **Routing control** page, choose **Create**, and then choose a **Control panel**. 

1. Choose a cluster to create the control panel on, and then enter a name for the panel.

1. Choose **Create control panel**.