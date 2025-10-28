# Adding filter controls to analysis sheets

When you're designing an analysis, you can add a filter to the analysis sheet near the
visuals that you want to filter. It appears in the sheet as a control that dashboard viewers
can use when you publish the analysis as a dashboard. The control uses the analysis theme
settings so it looks like it's part of the sheet.

Filter controls share some settings with their filters. They apply to one, some, or all of
the objects on the same sheet.

Use the following sections add and customize filter controls to an analysis. To learn how
to add cross-sheet controls, see [Controls](cross-sheet-filters.md#cross-sheet-controls "cross-sheet-filters.md#cross-sheet-controls").

###### Topics

- [Adding filter controls](#filter-controls-add "#filter-controls-add")
- [Pinning filter controls to the top of a
  sheet](#filter-controls-pin "#filter-controls-pin")
- [Customizing filter controls](#filter-controls-customize "#filter-controls-customize")
- [Cascading filter controls](#cascading-controls "#cascading-controls")

## Adding filter controls

Use the following procedure to add a filter control.

###### To add a filter control

1. Open the [Quick Suite console](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
2. From the Quick Suite homepage, choose **Analyses**, and
   then choose the analysis that you want to work with.
3. In the analysis, choose **Filter**.
4. If you don't already have some filters available, create one. For more
   information about creating filters, see [Adding filters](add-a-filter-data-prep.md "add-a-filter-data-prep.md").
5. In the **Filters** pane, choose the three dots to the right
   of the filter that you want to add a control for, and choose **Add to
   sheet**.

The filter control is added to the sheet, usually at the bottom. You can
resize it or drag it to different positions on the sheet. You can also customize
how it appears and how dashboard viewers can interact with it. For more
information about customizing filter controls, see the following
sections.

## Pinning filter controls to the top of a

sheet

Use the following procedure to pin filter controls to the top of a sheet.

###### To pin a control to the top of a sheet

1. On the filter control that you want to move, choose the three dots next to the
   pencil icon and choose **Pin to top**.

The filter is pinned to the top of the sheet and is collapsed. You can click
it to expand it. 2. (Optional) To unpin the control, expand it and hover over it at the top of the
sheet until three dots appear. Choose the three dots, and then choose
**Move to sheet**.

## Customizing filter controls

Depending on the data type of the field and the type of filter, filter controls have
different settings available. You can customize how they appear in the sheet and how
dashboard viewers can interact with them.

###### To customize a filter control

1. Choose the filter control in the sheet.
2. On the filter control, choose the pencil icon.

If the filter control is pinned to the top of the sheet, expand it and hover
your cursor over it until the three dots appear. Choose the three dots, and then
choose **Edit**. 3. In the **Format control** pane that opens, do the
following:

    1. For **Display name**, enter a name for the filter
     control.
    2. (Optional) To hide the display name from the filter control, clear the
     check box for **Show title**.
    3. For **Title font size**, choose the title font size
     that you want to use. The options range from extra small to extra large.
     The default setting is medium.

The remaining steps depend on the type of field the control is referencing. For
options by filter type, see the following sections.

### Date filters

If your filter control is from a date filter, use the following procedure to
customize the remaining options.

###### To customize further options for a date filter

1.  In the **Format control** pane, for
    **Style**, choose one of the following options:

        * **Date picker – range** – Displays
         a set of two fields to define a time range. You can enter a date or
         time, or you can choose a date from the calendar control. You can
         also customize how you want the dates to appear in the control by
         entering a date token for **Date format**. For more
         information, see [Customizing date formats
         in Quick Suite](format-visual-date-controls.md "format-visual-date-controls.md").
        * **Date picker – relative** –
         Displays settings like the time period, its relation to the current
         date and time, and the option to exclude time periods. You can also
         customize how you want the dates to appear in the control by
         entering a date token for **Date format**. For more
         information, see [Customizing date formats
         in Quick Suite](format-visual-date-controls.md "format-visual-date-controls.md").
        * **Text field** – Displays a box where you
         can enter the top or bottom *N*
         date.


        Helper text is included in the text field control by default, but
         you can choose to remove it by clearing the **Show helper
         text in control** option.

    By default, Quick Suite visuals are reloaded whenever a change is
    made to a control. For Calendar and Relative date picker controls, authors
    can add an **Apply** button to a control that delays visual
    reload until the user chooses **Apply**. This allows users
    to make multiple changes at a time without additional queries. This setting
    can be configured with the **Show an apply button**
    checkbox in the **Control options** section of the
    **Format control** pane.

2.  When finished, choose **Apply**.

### Text filters

If your filter control is from a text filter, for example dimensions, categories,
or labels, use the following procedure to customize the remaining options.

###### To customize further options for a text filter

1.  In the **Format control** pane, for
    **Style**, choose one of the following options:
    - **Dropdown** – Displays a dropdown list
      with buttons that you can use to select a single value.

    When you select this option, you can choose the following options
    for **Values**:

        + **Filter** – Displays all the
         values that are available in the filter.
        + **Specific values** – Enables you
         to enter the values to display, one entry per line.

    You can also choose to **Hide Select all option from the
    control values**. This removes the option to select or
    clear the selection of all values in the filter control.
    - **Dropdown - multiselect** – Displays a
      dropdown list with boxes that you can use to select multiple values.

    When you select this option, you can choose the following options
    for **Values**:

        + **Filter** – Displays all the
         values that are available in the filter.
        + **Specific values** – Enables you
         to enter the values to display, one entry per line.

    By default, Quick Suite visuals are reloaded whenever a
    change is made to a control. For Multiselect dropdown controls,
    authors can add an **Apply** button to a control
    that delays visual reload until the user chooses
    **Apply**. This allows users to make multiple
    changes at a time without additional queries. This setting can be
    configured with the **Show an apply button**
    checkbox in the **Control options** section of the
    **Format control** pane.
    - **List** – Displays a list with buttons
      that you can use to select a single value.

    When you select this option, you can choose the following options
    for **Values**:

        + **Filter** – Displays all the
         values that are available in the filter.
        + **Specific values** – Enables you
         to enter the values to display, one entry per line.

    You can also choose the following:

        + **Hide search bar when control is on
         sheet** – Hides the search bar in the
         filter control, so users can't search for specific
         values.
        + **Hide Select all option from the control
         values** – Removes the option to select
         or clear the selection of all values in the filter
         control.

    - **List - multiselect** – Displays a list
      with boxes that you can use to select multiple values.

    When you select this option, you can choose the following options
    for **Values**:

        + **Filter** – Displays all the
         values that are available in the filter.
        + **Specific values** – Enables you
         to enter the values to display, one entry per line.

    You can also choose the following:

        + **Hide search bar when control is on
         sheet** – Hides the search bar in the
         filter control, so users can't search for specific
         values.
        + **Hide Select all option from the control
         values** – Removes the option to select
         or clear the selection of all values in the filter
         control.

    - **Text field** – Displays a text box where
      you can enter a single entry. Text fields support up to 79950
      characters.

    When you select this option, you can choose the following:

        + **Show helper text in control** –
         Removes the helper text in text fields.

    - **Text field - multiline** – Displays a
      text box where you can enter multiple entries. Multiline text fields
      support up to 79950 characters across all entries.

    When you select this option, you can choose the following:

        + For **Separate values by**, choose how
         you want to separate values you enter into the filter
         control. You can choose to separate values by a line break,
         comma, pipe (|), or semicolon.
        + **Show helper text in control** –
         Removes the helper text in text fields.

2.  When finished, choose **Apply**.

### Numeric filters

If your filter control is from a numeric filter, use the following procedure to
customize the remaining options.

###### To customize further options for a numeric filter

1.  In the **Format control** pane, for
    **Style**, choose one of the following options:
    - **Dropdown** – Displays a list where you
      can select a single value.

    When you select this option, you can choose the following options
    for **Values**:

        + **Filter** – Displays all the
         values that are available in the filter.
        + **Specific values** – Enables you
         to enter the values to display, one entry per line.

    You can also choose to **Hide Select all option from the
    control values**. This removes the option to select or
    clear the selection of all values in the filter control.

        + **Filter** – Displays all the
         values that are available in the filter.
        + **Specific values** – Enables you
         to enter the values to display, one entry per line.
        + **Hide Select all option from the control
         values** – Removes the option to select
         or clear the selection of all values in the filter
         control.

    - **List** – Displays a list with buttons
      that enable selecting a single value.

    When you select this option, you can choose the following options
    for **Values**:

        + **Filter** – Displays all the
         values that are available in the filter.
        + **Specific values** – Enables you
         to enter the values to display, one entry per line.

    You can also choose the following:

        + **Hide search bar when control is on
         sheet** – Hides the search bar in the
         filter control, so users can't search for specific
         values.
        + **Hide Select all option from the control
         values** – Removes the option to select
         or clear the selection of all values in the filter
         control.

    - **Slider** – Displays a horizontal bar
      with a toggle that you can slide to change the value. If you have a
      ranged filter for values between a minimum and a maximum, the slider
      provides a toggle for each number. For sliders, you can specify the
      following options:
      - **Minimum value** – Displays the
        smaller value at the left of the slider.
      - **Maximum value** – Displays the
        larger value at the right of the slider.
      - **Step size** – Enables you to set
        the number of increments that the bar is divided
        into.

    - **Text box** – Displays a box where you
      can enter the value. When you select this option, you can choose the
      following:
      - **Show helper text in control** –
        Removes the helper text in text fields.

2.  When finished, choose **Apply**.

## Cascading filter controls

You can limit the values displayed in the control, so they only show values that are
valid for what is selected in other controls. This is called a cascading control.

###### When creating cascading controls, the following limitations apply:

1. Cascading controls must be tied to dataset columns from the same
   dataset.
2. The child control must be a dropdown or list control.
3. For parameter controls, the child control must be linked to a dataset
   column.
4. For filter controls, the child control must be linked to a filter (instead of
   showing only specific values).
5. The parent control must be one of the following:
   1. A string, integer, or numeric parameter control.
   2. A string filter control (excluding top-bottom filters).
   3. A non-aggregated numeric filter control.
   4. A date filter control (excluding top-bottom filters).

###### To create a cascading control

1. Choose **Show relevant values only.** Note that this option
   might not be available for all filter control types.
2. In the **Show relevant values only** pane that opens, choose
   one or more controls from the available list.
3. Choose a field to match the value to.
4. Choose **Update**.
