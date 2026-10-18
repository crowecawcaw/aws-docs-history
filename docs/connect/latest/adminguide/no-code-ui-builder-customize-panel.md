

# Configure column layouts, colors, and data definitions in a view
<a name="no-code-ui-builder-customize-panel"></a>

The **Customize** panel is on the right side of the UI builder.

![An example of the Customize panel in the UI builder, the global settings icon.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-customize-panel-example.png)


In the **Customize** panel, you configure global settings for the whole view and local settings for each component, including:
+ Column layouts
+ Colors
+ [Dynamic data mapping](no-code-ui-builder-properties-dynamic-fields.md)
+ [Sample data](no-code-ui-builder-sample-data.md)
+ Static data definitions

## Configure global layouts and colors for a view
<a name="no-code-ui-builder-properties-global-settings"></a>

To configure global settings, in the **Customize** panel, choose the global settings icon, as shown in the following image.

![The Customize panel, the global settings icon.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-properties-global-settings-example.png)


You use global settings to set the overall layout and colors of your view:
+ In the **Alignment** section, align components to the left, center, or right of the view.
+ Set three colors:
  + **Primary Color**
  + **Secondary Color**
  + **Neutral Color**

Components use these colors by default. You can override them on any component.

## Configure layout columns
<a name="no-code-ui-builder-properties-layout-columns"></a>

A view uses a 12-column flexbox grid. Components are positioned relative to each other, not by pixel, so the view scales up and down without losing its composition.

In the global settings, you can group the columns. For example, in the **Column** section, you can divide the view into two sections of six columns each, as shown in the following image. 

![A Column section, divided into two sections of six columns each.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-properties-layout-columns-example-1.png)


The following image shows an example of how this layout appears to users.

![A view divided into two sections of six columns, as it appears to users.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-properties-layout-columns-details-example-1.png)


You can also use the **Customize** slider to alter the ratios of these groupings. For example, you can set it so the left side of the view is four columns and the right side is eight, as shown in the following image:

![A layout with four columns on one side and eight on the other.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-properties-layout-columns-example-2.png)


The following image shows an example of how this layout would appear to the user.

![A view of four columns on one side and eight on the other, as it appears to users.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-properties-layout-columns-details-example-2.png)
