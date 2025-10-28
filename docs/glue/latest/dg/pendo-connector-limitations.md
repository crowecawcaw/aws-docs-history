# Limitations

The following are limitations for the Pendo connector:

- Pagination is not supported in Pendo.
- Filtration is supported only by the Aggregate API
  objects(`Account`, `Event`, `Feature Event`,
  `Guide Events`, `Page Event`, `Poll Event`,
  `Track Event`, and `Visitor`)
- DateTimeRange is mandatory filter parameter for Aggregate API objects
  (`Event`, `Feature Event`, `Guide Events`,
  `Page Event`, `Poll Event,`
  `Track Event`)
- The dayRange period will be rounded down to the start of the period in the
  time zone. For example, if provided filter is
  `2023-01-12T07:55:27.065Z` then this time period will be rounded
  to the start of period, that is `2023-01-12T00:00:00Z` .
