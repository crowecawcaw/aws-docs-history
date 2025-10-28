# Limitations

The following are limitations for the Adobe Analytics connector:

- Adobe Analytics doesn’t support field based and record-based partitioning. Field based partitioning is not supported as you cannot query fields that you partition.
  Record based partitioning cannot be supported as there is no provision to get ‘offset’ for pagination.
- In the `Report Top Item` entity, the `startDate` and
  `endDate` query parameters are not functioning as expected. The
  response is not being filtered based on these parameters, which is causing
  issues with the filter and incremental flow for this entity.
- For the `Annotation`, `Calculated Metrics`, `Calculated Metrics
Function`, `Date Ranges`, `Dimension`,
  `Metric`, `Project`, `Report Top Items`,
  and `Segment` entities, the `locale` query parameter
  specifies which language is to be used for localized sections of responses and
  does not filter the records. For example, `locale="ja_JP"` will
  display the data in Japanese.
- `Report Top Item` entity – filter on `dateRange` and
  `lookupNoneValues` fields are currently not working.
- `Segment` entity: with filter value `includeType=“templates”`,
  filters on other fields are not working.
- `Date Range` entity – filter on `curatedRsid` field is not
  working.
- `Metric entity` entity – filter on segmentable field with
  “false” value gives result for both true and false value.
