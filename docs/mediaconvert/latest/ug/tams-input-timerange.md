# Time range format

TAMS inputs use a specific time range format that provides nanosecond precision for content selection. The format follows the pattern `[start:nanoseconds_end:nanoseconds)`, where brackets indicate whether the boundary is inclusive or exclusive.

The time range format consists of the following components:

- `[` or `(` – Opening bracket indicates inclusive `[` or exclusive `(` start boundary
- `start:nanoseconds` – Start time in seconds and nanoseconds
- `_` – Separator between start and end times
- `end:nanoseconds` – End time in seconds and nanoseconds
- `]` or `)` – Closing bracket indicates inclusive `]` or exclusive `)` end boundary
  The following examples show typical time range formats:

- `[15:0_35:0)` – From 15.0 seconds (inclusive) to 35.0 seconds (exclusive)
- `[0:500000000_10:0]` – From 0.5 seconds (inclusive) to 10.0 seconds (inclusive)
- `[3600:0_7200:0)` – From 1 hour (inclusive) to 2 hours (exclusive)
  MediaConvert automatically calculates precise clipping parameters when your requested time range extends beyond the available segment boundaries. This ensures your output contains exactly the content you specified with nanosecond precision.

###### Note

The end time must be later than the start time. MediaConvert validates the time range format before processing begins.
