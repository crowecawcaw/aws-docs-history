# Dates

To convert dates to strings, we recommend following the ISO 8601 format, which supports
lexicographical order comparisons.

The following table describes formats for representing date-time values with differing
degrees of granularity. You must use components exactly as they are shown here and with
exactly this punctuation. Note that the "T" appears literally in the string, to indicate the
beginning of the time element, as is specified in ISO 8601.

| Granularity                                                                   | String                                                        |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Year                                                                          | YYYY (e.g., 1997)                                             |
| Year and month                                                                | YYYY-MM (e.g., 1997-07)                                       |
| Complete date                                                                 | YYYY-MM-DD (e.g., 1997-07-16)                                 |
| Complete date plus hours and minutes                                          | YYYY-MM-DDThh:mmTZD (e.g., 1997-07-16T19:20+01:00)            |
| Complete date plus hours, minutes and seconds                                 | YYYY-MM-DDThh:mm:ssTZD (e.g., 1997-07-16T19:20:30+01:00)      |
| Complete date plus hours, minutes, seconds and a decimal fraction of a second | YYYY-MM-DDThh:mm:ss.sTZD (e.g., 1997-07-16T19:20:30.45+01:00) |
