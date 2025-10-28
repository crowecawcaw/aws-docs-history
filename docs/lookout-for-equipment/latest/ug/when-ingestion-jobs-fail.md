On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Reviewing the job

Few datasets are perfectly formed. Missing or incorrectly formatted values are common.
Therefore, it's not feasible to fail an ingestion job because of a single error.

Lookout for Equipment operates with a bias toward complete ingestion. In other words, when it
encounters a problem in the ingested data, Lookout for Equipment attempts to fix that problem
automatically. Then it alerts you to whatever issues it encountered, and lets you know
what fixes it implemented.

If your entire job fails, consider the following possibilities:

1. The files are not .csv files, or they are corrupted, or they are unreadable
   for some other reason.
2. The files were not named or organized as explained under Adding your
   data.
3. The files contain no data, or 100% of the data they contain is not formatted
   in a way that Lookout for Equipment recognizes.
   If your ingestion job fails, check the issues above and make the appropriate
   adjustments. When you’re ready to try again, go back to [Adding your dataset](ingest-dataset.md "ingest-dataset.md").

###### Important

This page is about troubleshooting the ingestion of _an entire
job_. You can also read about [why some specific files don't get
ingested](when-files-dont-get-ingested.md "when-files-dont-get-ingested.md"), and about [evaluating
the data from specific sensors](reading-details-by-sensor.md "reading-details-by-sensor.md").

## Checking the logs

If you enabled CloudWatch Logs, then the logs may help you troubleshoot ingestion issues. The published logs may include the following error codes:

- COMPLETE_SENSOR_DATA_MISSING : A sensor has no valid data assosicated with it. The log contains the sensor name and the associated component name.
- DATA_MISSING_IN_COLUMN : Data associated with a sensor is invalid at a particular timestamp. Along with the sensor name and associated component name, the log contains details about the timestamp and the associated file path.
- UNSUPPORTED_DATE_FORMATS : A value in the timestamp column is invalid. The log contains details about the timestamp string, the path of the file, and the associated component name.
- INSUFFICIENT_SENSOR_DATA : A sensor is associated with less than [14 days](formatting-data.md#understanding-date-range "formatting-data.md#understanding-date-range") of data. The log contains the sensor name, the component name, and the date range of data (in days) associated with the sensor.
- DUPLICATE_TIMESTAMPS : A value in the timestamp column of the data is a duplicate entry. The timestamp in question and the associated file path are part of the log.
- FILES_NOT_INGESTED : A file was not ingested during the ingestion workflow. The log contains details about the file's path.
