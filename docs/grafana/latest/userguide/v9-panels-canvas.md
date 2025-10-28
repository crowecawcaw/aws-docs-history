# Canvas panel

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Canvas is a new panel that combines the power of Grafana with the
flexibility of custom elements. Canvas visualizations are extensible form-built panels
that allow you to explicitly place elements within static and dynamic layouts. This
empowers you to design custom visualizations and overlay data in ways that aren’t
possible with standard Grafana panels, all within Grafana’s UI. If you’ve used popular
UI and web design tools, then designing Canvas panels will feel very familiar.

## Elements

**Metric value**

The metric value element enables you to easily select the data you want to display
on canvas. This element has a unique “edit” mode that can be triggered either
through the context menu “Edit” option or by double-clicking. When in edit mode you
can select which field data that you want to display.

**Text**

The text element enables you to easily add text to the canvas. The element also
supports an editing mode, triggered via either double-clicking or the edit menu
option in the context menu.

**Rectangle**

The rectangle element enables you to add a basic rectangle to the canvas.
Rectangle elements support displaying text (both fixed and field data) as well
as can change background color based on data thresholds.

**Icon**

The icon element enables you to add a supported icon to the canvas. Icons can have
their color set based on thresholds or value mappings.

## Canvas Editing

**Inline editor**

Canvas introduces a new editing experience. You can now edit your
canvas panel inline while in the context of dashboard mode.

**Context menu**

The context menu gives you access to common tasks. Supported functionality
includes opening and closing the inline editor, duplicating an element, deleting an
element, and more.

The context menu is triggered by a right click action over the panel or a given
canvas element. When right clicking the panel, you are able to set a background
image and easily add elements to the canvas.

When right clicking an element, you are able to edit, delete, and duplicate the
element, or modify the element’s layer positioning.

## Canvas Options

**Inline editing**

The inline editing toggle enables you to lock or unlock the canvas panel. When
turned off the canvas panel becomes _locked_,
freezing elements in place and preventing unintended modifications.
