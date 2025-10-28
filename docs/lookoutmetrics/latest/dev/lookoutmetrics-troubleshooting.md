Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Troubleshooting Lookout for Metrics

The following topics provide troubleshooting information for errors and issues that you might encounter when
using the Amazon Lookout for Metrics console or API. If you find an issue that is not listed here, use the **Provide
feedback** button on this page to report it.

## Data validation

Amazon Lookout for Metrics validates your dataset when you configure metric during [setup](detectors-setup.md "detectors-setup.md"). For an Amazon Simple Storage Service (Amazon S3) datasource, it checks a small sample of files to ensure that the required
fields exist and timestamps are in the right format.

**Error:**
_ValidationException : One of specified bucket in historicalDataPathList is not in same region as this
AWS service API._

An anomaly detector can access only data that is stored in the same AWS Region as the detector. If you can't
create a detector in the same Region as your data, you can use [replication](../../../AmazonS3/latest/userguide/replication.md "../../../AmazonS3/latest/userguide/replication.md") to copy data into the detector's Region. Use the [offset
setting](detectors-setup.md "detectors-setup.md") on the dataset to allow time for replication to complete.

**Error:**
_ValidationException : Timestamp Column values inside file provided in S3 path do not match provided
timestamp format._

This error can occur if you configure the wrong timestamp format, or if the subset of entries used for
validation had errors or missing values. Check the format or try again. Note that `hh` is a 12-hour
format and requires a corresponding AM/PM marker. For example, `yyyy-MM-dd hh:mm:ss a`. For 24-hour
time, use `HH`.

**ConflictException:\***Updating or deleting a resource can cause an inconsistent
state.\*

Amazon Lookout for Metrics requires that your alerts have a unique name. If you delete or update an alert, you might get this error if you try to reuse the name of the alert that was deleted or updates.

## Importing data

At the end of each interval in continuous mode, or at the start of a backtest, a detector imports data from
the datasource into the dataset. In continuous mode, the detector skips the failed interval, records errors in the
[detector log](detectors-manage.md "detectors-manage.md"), and tries again at the end of each interval. In backtest
mode, the test fails. In this case, delete the failed detector, resolve the issue, and try again with a new
detector.

**Error:**
_Insufficient amount of data was found at the source location. Check service limits and
requirements._

The detector couldn't find usable data for the interval or test period. This error can occur if you choose a
field with non-numerical columns as a measure. Measures must have numerical data that can be aggregated (added
together or averaged) for each interval.

**Error:**
_No datapoint was found at the source location for time interval from 2021-02-27T01:30:00.000 to
2021-02-27T01:20:00.000._

This issue can occur if the dataset is configured with the wrong timezone, or if data was written after the
interval ended. If data isn't immediately available in the datasource after an interval ends, use the [offset setting](detectors-setup.md "detectors-setup.md") to make the detector wait before looking for data.
