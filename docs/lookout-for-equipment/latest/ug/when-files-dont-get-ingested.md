On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Checking the files

If Lookout for Equipment fails to ingest a particular file, consider the following
possibilities:

- None of the sensors listed in the file have any data that can be
  ingested.
- The file is not a .csv file, or the file is corrupted, or the file cannot be
  read for some other reason.
  To troubleshoot files that were not ingested:

1. From the **Job details** tab of the main console page for
   your dataset, note the names of any files that failed the ingestion
   process.
2. To address issues with file formatting, see [Formatting your data](formatting-data.md#formatting-data.title "formatting-data.md#formatting-data.title").
3. To address issues with individual sensors, see [Understanding sensor
   quality](reading-details-by-sensor.md#reading-details-by-sensor.title "reading-details-by-sensor.md#reading-details-by-sensor.title").
4. When you’re ready to try again, see [Replacing your dataset](replacing-your-dataset.md#replacing-your-dataset.title "replacing-your-dataset.md#replacing-your-dataset.title").

###### Important

This page is about troubleshooting the ingestion of _specific
files_. You can also read about [why the ingestion of an entire job can
fail](when-ingestion-jobs-fail.md "when-ingestion-jobs-fail.md"), and about [evaluating the
data from specific sensors](reading-details-by-sensor.md "reading-details-by-sensor.md").

## Anticipating schema detection

problems

The following circumstances will lead to the failure of an entire ingestion
job:

- One or more column headers contain one or more invalid characters.

A single invalid character in a single column in a single file is enough
to fail an entire job involving multiple files.

- In a job consisting of a single file, that file has a formatting issue
  that prevents ingestion.
- In a job consisting of multiple files, every single file has a formatting
  issue that prevents ingestion.

The easiest way to prevent problems with file ingestion is to take the following
precautions:

- Make sure your headers don't include any invalid characters, such as
  spaces.

Valid characters are: 0-9, a-z, A-Z, and # $ . \ - (hyphen) \_
(underscore)

- Make sure that the timestamp column is the one furthest to the left in
  your CSV file.
- Make sure that you don't have any duplicated column headers.
