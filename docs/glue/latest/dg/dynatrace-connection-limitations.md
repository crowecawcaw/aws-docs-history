# Dynatrace limitations

The following are limitations or notes for Dynatrace:

- Dynatrace doesn’t support either field based or record based partitioning.
- For the Select All feature, if you provide the "field" in the filter then it will not allow records to be more then 10 per page.
- The maximum page size supported is 500. If you select any of the [`evidenceDetails, impactAnalysis, recentComments`] fields while creating the flow then records per page will be defaulted to 10.
