# AWS Clean Rooms Differential Privacy

AWS Clean Rooms Differential Privacy helps you protect the privacy of your users with a
mathematically-backed technique that is implemented with intuitive controls in a few clicks. As
a fully managed capability, no prior differential privacy experience is needed to help you
prevent the re-identification of your users. AWS Clean Rooms automatically adds a carefully calibrated
amount of noise to query results at runtime in order to help protect your individual-level
data.

AWS Clean Rooms Differential Privacy supports a wide range of analytical queries and is a good fit for
a wide variety of use cases, where a small amount of error in the query results will not
compromise the usefulness of your analysis. With it, your partners can generate
business-critical insights about advertising campaigns, investment decisions, clinical research,
and more, all without requiring any additional setup from your partners.

AWS Clean Rooms Differential Privacy protects against overflow or invalid cast errors that make use of
scalar functions or math operator symbols in a malicious manner.

For more information about AWS Clean Rooms Differential Privacy, see the following topics.

###### Topics

- [Differential privacy](#dp-overview "#dp-overview")
- [How Differential Privacy in AWS Clean Rooms works](#dp-how-it-works "#dp-how-it-works")
- [Differential privacy policy](dp-settings.md "dp-settings.md")
- [SQL capabilities of AWS Clean Rooms Differential Privacy](dp-sql-capabilities.md "dp-sql-capabilities.md")
- [Differential Privacy query tips and examples](dp-query-tips-examples.md "dp-query-tips-examples.md")
- [Limitations of AWS Clean Rooms Differential Privacy](dp-limitations.md "dp-limitations.md")

## Differential privacy

Differential privacy allows only aggregated insights and obfuscates the contribution of
any individual's data in those insights. Differential privacy protects the collaboration data
from the member who can receive results learning about a specific individual. Without
differential privacy, the member who can receive results can attempt to infer individual user
data by adding or removing records about an individual and observing the difference in query
results.

When differential privacy is turned on, a specified amount of noise is added to the query
results to obfuscate the contribution of individual users. If the member who can receive
results tries to observe the difference in query results after removing records about an
individual from their dataset, the variability in the query result helps prevent the
identification of the individual's data. AWS Clean Rooms Differential Privacy uses the [SampCert](https://github.com/leanprover/SampCert "https://github.com/leanprover/SampCert") sampler, a proven correct
sampler implementation developed by AWS.

## How Differential Privacy in AWS Clean Rooms works

The workflow to turn on differential privacy in AWS Clean Rooms requires the following
additional steps when [completing the
workflow for AWS Clean Rooms](what-is.md#how-it-works "what-is.md#how-it-works"):

1. You turn on differential privacy when adding a [custom analysis rule](analysis-rules-custom.md "analysis-rules-custom.md").
2. [You configure the differential privacy
   policy for the collaboration](configure-differential-privacy.md "configure-differential-privacy.md") to make your data tables protected with differential
   privacy available for querying.

After you complete these steps, the member who can query can start running queries on
differential privacy protected data. AWS Clean Rooms returns results that comply with the differential
privacy policy. AWS Clean Rooms Differential Privacy tracks the estimated number of remaining queries
that you can run, similar to the gas gauge in a car that shows you the car's current fuel
level. The number of queries that the member who can query can run is limited by the
**Privacy budget** and **Noise added per query**
parameters that are set in the [Differential privacy policy](dp-settings.md "dp-settings.md").

### Considerations

When using differential privacy in AWS Clean Rooms, consider the following:

- The member who can receive results can't use differential privacy. They will
  configure a custom analysis rule with differential privacy turned off for their
  configured tables.
- The member who can query can't join tables from two or more data providers when both
  have differential privacy turned on.
