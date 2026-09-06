

# Monitor collectors
<a name="managed-prometheus-collectors-monitor"></a>

Amazon CloudWatch managed Prometheus collectors automatically vend logs to CloudWatch Logs so you can monitor scraper health, diagnose connectivity issues, and track scraping activity. These logs include information about target discovery, scrape successes and failures, and configuration errors. For more information about collector logging, see [Logging for managed collectors](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-logging.html) in the *Amazon Managed Service for Prometheus User Guide*.

## List scrapers
<a name="managed-prometheus-collectors-monitor-list"></a>

Use the following command to list all scrapers in your account and Region:

```
aws amp list-scrapers
```

To filter scrapers by alias:

```
aws amp list-scrapers --filters alias={{my-scraper-alias}}
```

## Describe a scraper
<a name="managed-prometheus-collectors-monitor-describe"></a>

To view the details and current status of a specific scraper:

```
aws amp describe-scraper --scraper-id {{scraper-id}}
```

## Delete a scraper
<a name="managed-prometheus-collectors-monitor-delete"></a>

To delete a scraper that is no longer needed:

```
aws amp delete-scraper --scraper-id {{scraper-id}}
```

**Note**  
Deleting a scraper removes the ENIs that the collector created in your VPC. Allow a few minutes for the deletion to complete and for CloudWatch to clean up all associated resources.