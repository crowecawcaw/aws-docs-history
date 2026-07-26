# Monitor collectors

Amazon CloudWatch managed Prometheus collectors automatically vend logs to CloudWatch Logs so you can monitor
scraper health, diagnose connectivity issues, and track scraping activity. These logs
include information about target discovery, scrape successes and failures, and
configuration errors. For more information about collector logging, see [Logging
for managed collectors](../../../prometheus/latest/userguide/AMP-collector-logging.md "../../../prometheus/latest/userguide/AMP-collector-logging.md") in the _Amazon Managed Service for Prometheus User
Guide_.

## List scrapers

Use the following command to list all scrapers in your account and Region:

```
aws amp list-scrapers
```

To filter scrapers by alias:

```
aws amp list-scrapers --filters alias=`my-scraper-alias`
```

## Describe a scraper

To view the details and current status of a specific scraper:

```
aws amp describe-scraper --scraper-id `scraper-id`
```

## Delete a scraper

To delete a scraper that is no longer needed:

```
aws amp delete-scraper --scraper-id `scraper-id`
```

###### Note

Deleting a scraper removes the ENIs that the collector created in your VPC. Allow a
few minutes for the deletion to complete and for CloudWatch to clean up all associated
resources.
