# diff

Compares the log events found in your requested time period with the log
events from a previous time period of equal length. This way, you can look
for trends and find whether specific log events are new.

Add a modifier to the `diff` command to specify the time period
that you want to compare with:

- `diff` compares the log events in the currently
  selected time range to the log events of the immediately preceding
  time range.
- `diff previousDay` compares the log events in the
  currently selected time range to the log events from the same time
  the preceding day.
- `diff previousWeek` compares the log events in the
  currently selected time range to the log events from the same time
  the preceding week.
- `diff previousMonth` compares the log events in the
  currently selected time range to the log events from the same time
  the preceding month.
  For more information, see [Compare (diff) with previous time ranges](CWL_AnalyzeLogData_Compare.md "CWL_AnalyzeLogData_Compare.md").
