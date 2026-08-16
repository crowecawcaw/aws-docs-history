# Configure analysis settings

Amazon Quick authors can use the Analysis settings menu to configure the refresh and
date time settings of an analysis. To access the Analysis Settings menu, choose
**Edit**, and then choose **Analysis Settings**.
The following settings can be configured in the Analysis settings menu:

###### Refresh settings

- **Reload visuals every time I switch sheets**
  – Use this setting to reload every visual in a Quick Sight analysis
  whenever the user switches to a different sheet in the analysis.
- **Update visuals manually** – Use this
  setting to only update applicable visuals in an analysis when the user applies
  their changes. When this setting is toggled on, the analysis loads the visuals
  blank by default because the queries won't be fired until the user selects the
  **UPDATE VISUALS** button located in the toolbar or on the
  impacted visuals. The **UPDATE VISUALS** button confirms that
  the user is finished with the filter and control choices that they want to apply
  to the affected visuals. The image below shows the **UPDATE
  VISUALS** button.

When **Update visuals manually** is toggled on, authors can
still add visuals, edit visuals, and edit control selections, but the affected
visuals won't update until the author applies the new changes. This allows
authors to build analyses without increasing their database load and gives
better control over which values are loaded in an analysis.

###### Date and time settings

- **Convert time zone** – Use this setting
  to convert all date field related visualizations, filters, and parameters to
  reflect the chosen time zone. All daylight savings adjustments are made
  automatically. For more information about time zone configuration, see [Customize date and time values of an analysis](analysis-date-time.md "analysis-date-time.md").
- **Start of the week** – Use this setting
  to choose the week start day for an analysis.

###### Interactivity

- Use this setting to highlight specific data points across visuals in a sheet.
  When you select or hover over a data point on a visual, related data across
  other visuals will stand out, while unrelated data is dimmed. Highlighting
  allows you to understand correlations, spot patterns, trends, and outliers, and
  facilitate stronger, more informed analyses. Select either **On
  selection** or **On hover** to turn highlighting
  on, or **No highlight** to turn it off.
- To customize highlighting on a per-sheet level see [Adding and managing sheets](working-with-multiple-sheets.md "working-with-multiple-sheets.md").

###### No data message customization

- Use this setting to control the message displayed when a visual in the
  analysis returns no data. Customizing this can give readers of the dashboards
  reasons why no data is shown and potential fixes. Parameters are supported for
  all text input.
- **Title and subtitle** – Use these
  settings to customize the text shown on the message title or subtitle and to
  toggle visibility of either option.
- **Hyperlink** – Use this setting to
  control the hyperlink displayed at the bottom of the message. The link label
  field controls the displayed text of the hyperlink, while the link URL field
  controls where the user is redirected when clicking the hyperlink text. Only
  http://, https://, and mailto: URL schemas are supported.
- **Pixel-perfect reporting** – In
  pixel-perfect (paginated) report output, hyperlinks are rendered as clickable
  links, not as static display text. To show the full URL in a printed report,
  enter the full URL as the link label so it remains visible in the static
  output.
- **Dataset or data refresh errors** – The
  no data message customization applies only to visuals that return zero rows of
  data. Dataset or data refresh errors are a separate error type and are not
  customizable as part of this feature.
