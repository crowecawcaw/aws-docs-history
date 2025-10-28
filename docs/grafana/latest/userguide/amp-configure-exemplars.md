# Configure exemplars

###### Note

This feature requires Prometheus version 2.26 or later.

Exemplars are not supported in Amazon Managed Service for Prometheus.

You can show exemplars data alongside a metric both in Explore and Dashboards.
Exemplars associate higher-cardinality metadata from a specific event with
traditional time series data.

You can configure exemplars in the data source settings by adding links to
your exemplars. You can use macros in your URL. For example, you could create a
URL such as `https://example.com/${__value.raw}`.
