# Types of profile panel visualizations

Profile panel content can take one of the following forms.

| Visualization type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Key-value pairs    | The simplest type of visualization is a set of key-value pairs.<br>A finding or entity information panel is the most common example of a key-value pair<br>panel.<br>Example of a profile panel containing key-value pairs.<br>Key-value pairs can also be used to add additional information to other types of<br>panels.<br>From a key-value pair panel, if a value is an identifier of an entity, then you can<br>pivot to its profile.                                               |
| Table              | A table is a simple multiple-column list of items.<br>Example of a profile panel containing a simple table.<br>You can sort, filter, and page through the table.<br>You can change the number of entries to display on each page. See [Setting the preferences for a profile panel](profile-panel-preferences.md "profile-panel-preferences.md").<br>If a value in the table is an identifier of an entity, then you can pivot to its<br>profile.                                        |
| Timeline           | A timeline visualization shows an aggregated value for defined intervals over<br>time.<br>Example of a profile panel containing timelines.<br>The timeline highlights the current scope time, and includes additional peripheral<br>time before and after the scope time. The peripheral time provides context for the activity<br>in the scope time.<br>Hover over a time interval to display a summary of the data for that time<br>interval.                                          |
| Expandable table   | An expandable table combines tables and timelines.<br>Example of a profile panel containing an expandable table.<br>The visualization starts as a table.<br>You can sort, filter, and page through the table.<br>You can change the number of entries to display on each page. See [Setting the preferences for a profile panel](profile-panel-preferences.md "profile-panel-preferences.md").<br>You can then expand each row to show a timeline visualization specific to that<br>row. |
| Bar chart          | A bar chart shows values based on groupings.<br>Depending on the chart, you might be able to choose a bar to display a timeline of<br>related activity.<br>Example of a profile panel containing a bar chart.                                                                                                                                                                                                                                                                            |
| Geolocation chart  | A geolocation chart displays a map that is marked to highlight data based on<br>geographic location. It may be followed by a table containing details about individual<br>geolocations.<br>Example of a profile panel containing a geolocation chart.<br>Note that when processing incoming geographic data, Detective rounds the latitude and<br>longitude values to a single decimal point.                                                                                            |

## Notes on profile panel content

When viewing the content of a profile panel, be aware of the following items:

\***\*Approximate count data warning\*\***

This warning indicates that items with extremely low counts do not appear due to the
volume of applicable data.

To ensure a completely accurate count, reduce the amount of data. The simplest way to do
that is to reduce the length of the scope time. See [Managing the scope time](scope-time-managing.md "scope-time-managing.md").

\***\*Rounding for geographic locations\*\***

Detective rounds all latitude and longitude values to a single decimal point.

**Changes to how Detective represents API calls**

Beginning on July 14, 2021, Detective tracks the service that made each API call. Whenever
Detective displays an API method, it also displays the associated service. On profile panels that
display information about API calls, the calls are always grouped by the service. For data
that Detective ingested before that date, the service name is listed as **Unknown service**.

Also beginning on July 14, 2021, for accounts and roles, the activity details for the
**Overall API call volume** profile panel no longer show the
AKID of the resource that issued the call. For accounts, Detective displays the identifier of the
principal (user or role) that issued the call. For roles, Detective displays the identifier of
the role session. For data that Detective ingested before July 14, 2021, the identifier is listed
as **Unknown resource**.

For profile panels that display a list of API calls, the associated timeline highlights
the period of time during which this transition occurred. The highlight starts on July 14,
2021, and ends when the update was fully propagated in Detective.
