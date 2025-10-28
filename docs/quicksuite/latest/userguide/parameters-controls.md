# Using a control with a parameter in

Amazon Quick Suite

In dashboards, parameter controls appear at the top of the data sheet, which contains
a set of visuals. Providing a control allows users to choose a value to use in a
predefined filter or URL action. Dashboard users can use controls
to apply filtering across all visuals datasets on a dashboard, without having to create
the filters themselves.

The following rules apply:

- To create or edit a control for a parameter, make sure that the parameter
  exists.
- Multiselect list controls are compatible with analysis URLs, dashboard URLs,
  custom actions, and custom filters. The filter must be either equal or not equal
  to the values provided. No other comparisons are supported.
- Lists show up to 1,000 values. If there are more than 1,000 distinct values, a
  search box appears so you can filter the list. When the filtered list contains
  less than 1,001 values, the contents of the list appear as line items.
- The **Style** option displays only the style types that are
  appropriate for the parameter's data type and single or multivalue setting.
  If the style that you want to use isn't in the list, recreate your
  parameter with the appropriate settings and try again.
- If your parameter links to a dataset field, it must be an actual field.
  Calculated fields aren't supported.
- The values display alphabetically in the control, unless there are more than
  1,000 distinct values. Then the control displays a search box instead. Each time
  you search for the value you want to use, it initiates a new query. If the
  results contain more than 1,000 values, you can scroll through the values with
  pagination. Wildcard search is supported. To learn more about wildcard search,
  see [Using wildcard search](search-filter.md#search-filter-wildcard "search-filter.md#search-filter-wildcard").
  Use the following procedure to create or edit a control for an existing parameter.

###### To create or edit a control for an existing parameter

1.  Choose an existing parameter's context menu, the `v` icon near
    the parameter name, and choose **Add control**.
2.  Enter a name to give the new control a label. This label appears at the top of
    the workspace, and later at the top of the sheet that a dashboard displays on.
3.  Choose a style for the control from the following:
    - **Text field**

    A text field lets you type in their own value. A text field works with
    numbers and text (strings).
    - **Text field - multiline**

    A multiline text field lets you type in their own values. With this
    option, you can choose to separate values you enter into the parameter
    control by a line break, comma, pipe (|), or semicolon. A text field
    works with numbers and text (strings).
    - **Dropdown**

    A dropdown list control that you can use to select a single value. A
    list control works with numbers and text (strings).
    - **Dropdown multiselect**

    A list control that you can use to select multiple values. A list
    control works with numbers and text (strings).
    - **List**

    A list control that you can use to select a single value. A list
    control works with numbers and text (strings).
    - **List - multiselect**

    A list control that you can use to select multiple values. A list
    control works with numbers and text (strings).
    - **Slider**

    A slider lets you select a numeric value by sliding the control from
    one end of the bar to another. A slider works with numbers.
    - **Date-picker**

    Using a date-picker, you can choose a date from a calendar control.
    When you choose to add a date-picker control, you can customize how to
    format dates in the control. To do so, for **Date
    format**, enter the date format that you want using the
    tokens described in [Customizing date formats
    in Quick Suite](format-visual-date-controls.md "format-visual-date-controls.md").

4.  (Optional) If you choose a dropdown control, the screen expands so you can
    choose the values to display. You can either specify a list of values, or use a
    field in a dataset. Choose one of the following:

        * **Specific values**


        To create a list of specific values, type in one per line, with no
         separating spaces or commas, as shown in the following
         screenshot.


        In the control, the values display alphabetically, not in the order
         that you typed them.
        * **Link to a data set field**


        To link to a field, choose the dataset that contains your field, then
         choose the field from the list.


        If you change the default values in the parameter, choose
         **Reset** on the control to show the new
         values.

    The values that you choose here are unioned with the static default values in
    the parameter settings.

5.  (Optional) Enable the option **Hide [ALL] option from the
    control if the parameter has a default configured**. Doing this
    shows only the data values and removes the option to select all items in the
    control. If you don't configure a static default on the parameter, this
    option doesn't work. You can add a default after adding a control by
    choosing the parameter, and selecting **Edit
    parameter**.
6.  (Optional) You can limit the values displayed in the controls, so they only
    show values that are valid for what is selected in other controls. This is
    called a cascading control.

To create one, choose **Show relevant values only**. Choose
one or more controls that can change what displays in this control.

When creating cascading controls, the following limitations apply.

    * Cascading controls must be tied to dataset columns from the same
     dataset.
    * The child control must be a dropdown or list control.
    * For parameter controls, the child control must be linked to a dataset
     column.
    * For filter controls, the child control must be linked to a filter
     (instead of showing only specific values).
    * The parent control must be one of the following.




    	+ A string, integer, or numeric parameter control.
    	+ A string filter control (EXCLUDING Top-Bottom filters).
    	+ A non-aggregated numeric filter control.
    	+ A date filter control (EXCLUDING Top-Bottom filters).

7. When you finish choosing options for your control, choose
   **Add**.
   The finished control appears at the top of the workspace. The context menu, shaped
   like a `v`, offers four options:

- **Reset** restores the user's selection to its default
  state.
- **Refresh list** applies only to drop-downs that are linked
  to a field in a dataset. Choosing **Refresh list** queries the
  data to check for changes. Data used in the control is cached.
- **Edit** reopens the control creation screen so that you can
  change your settings.

Once you have the **Edit control** pane open, you can click
on different visuals and controls to view formatting data for the specific
visual or control. For more information about formatting a visual, see [Formatting in Amazon Quick Suite](formatting-a-visual.md "formatting-a-visual.md").

- **Delete** removes the control. You can recreate it by
  choosing the parameter context menu.
  In the workspace, you can also resize and rearrange your controls. The dashboard users
  see them as you do, except without being able to edit or delete them.
