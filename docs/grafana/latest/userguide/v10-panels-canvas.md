# Canvas

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Canvases combine the power of Grafana with the flexibility of custom elements.
Canvases are extensible form-built panels that allow you to explicitly place elements
within static and dynamic layouts. This empowers you to design custom visualizations
and overlay data in ways that aren’t possible with standard Grafana panels, all within
Grafana’s UI. If you’ve used popular UI and web design tools, then designing Canvas
panels will feel very familiar.

## Elements

You can add these elements on your canvas. Adding multiple, and different kinds,
of elements lets you customize a visualization in ways that are not possible with
any other visualization.

**Metric value**

The metric value element lets you easily select the data you want to
display on canvas. This element has a unique _edit_ mode that
can be triggered either through the context menu **Edit** option
or by double-clicking panel. When in edit mode you can select which field data
that you want to display.

**Text**

The text element lets you easily add text to the canvas. The element also
supports an editing mode, triggered via either double-clicking or the edit menu
option in the context menu.

**Ellipse**

The ellipse element lets you add a basic ellipse to the canvas. An ellipse
element can display text (both fixed and field data) and its background color can
be changed based on data thresholds.

**Rectangle**

The rectangle element lets you to add a basic rectangle to the canvas.
A rectangle elements can display text (both fixed and field data) and its
background color can be changed based on data thresholds.

**Icon**

The icon element lets you add a supported icon to the canvas. Icons can have
their color set based on thresholds or value mappings.

**Server**

The server element lets you easily represent a single server, a stack of servers,
a database, or a terminal. Server elements support status color, bulb color, and a
bulb blink rate, all configurable by fixed or field values.

**Button**

The button element lets you add a basic button to the canvas. Button elements
support triggering basic, unauthenticated API calls. API settings are found in the
button element editor. You can also pass template variables in the API editor.

###### Note

Choosing a button will only trigger an API call when inline editing is
disabled. See [Canvas editing](#v10-panels-canvas-editing "#v10-panels-canvas-editing").

## Connections

When building a canvas, you can connect elements together to create more complex
visualizations. You can create connections by dragging from the connection anchor
of one element to the connection anchor of another element. You can also create
connections to the background of the canvas. Connection anchors are displayed when
you hover over an element and inline editing is turned on. To remove a connection,
select the connection and then press `Delete` or
`Backspace`.

You can set both the size and color of connections based on fixed or field
values. To do so, enter into panel edit mode, select the connection, and modify
the connection’s properties in the panel editor.

## Canvas editing

**Inline editor**

You can edit your canvas inline while in the context of dashboard mode.

**Pan and zoom**

You and turn on panning and zooming in a canvas. This allows you to both create
and navigate more complex designs.

###### Note

Pan and zoom is currently in preview by Grafana Labs. Support is
limited, and breaking changes might occur before general availability.

**Context menu**

The context menu lets you perform common tasks quickly and efficiently.
Supported functionality includes opening and closing the inline editor, duplicating
an element, deleting an element, and more.

The context menu is triggered by a right click action (or equivalent) over the
panel or a given canvas element.

When right clicking _the panel_, you are able to
set a background image and easily add elements to the canvas.

When right clicking _an element_, you are able to edit,
delete, and duplicate the element, or modify the element’s layer
positioning.

## Canvas Options

**Inline editing**

The inline editing toggle lets you lock or unlock the canvas panel. When
turned off, the canvas panel becomes _locked_, freezing
elements in place and preventing unintended modifications.

**Data links**

Canvases support [data
links](v10-panels-configure-data-links.md "v10-panels-configure-data-links.md"). You can create a data link for a metric-value element and display it
for all elements that use the field name by following these steps.

###### To create a data link for an element

1. Set an element to be tied to a field value.
2. Turn off the inline editing toggle.
3. Create an override for **Fields with name** and
   select the element field name from the list.
4. Choose the **+ Add override property** button.
5. Select **Datalinks > Datalinks** from the list.
6. Choose **+ Add link**, add a title and URL for the
   data link.
7. Hover over the element to display the data link tooltip.
8. Choose the element to be able to open the data link.

If multiple elements use the same field name, and you want to control which
elements display the data link, you can create a unique field name using the
[Add field from calculation](v10-panels-xform-functions.md#v10-panels-xform-funcs-add "v10-panels-xform-functions.md#v10-panels-xform-funcs-add")
transform. The alias you create in the transform will appear as a field you can
use with an element.
