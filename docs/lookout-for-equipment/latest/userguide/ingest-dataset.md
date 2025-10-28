On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Adding your dataset

###### Note

You can also [add a dataset to your project](SDK-examples.md#ingest-sensor-py-sdk "SDK-examples.md#ingest-sensor-py-sdk")
or [manage your dataset](SDK-examples.md#manage-sdk "SDK-examples.md#manage-sdk") using the SDK.

You've [created a project](create-project.md "create-project.md") and you've uploaded your [properly
formatted](formatting-data.md "formatting-data.md") data to Amazon S3. Now it's time to add the data to the
project.

## Setting your permissions

Lookout for Equipment requires permissions to access your data in Amazon S3, and to publish your ingestion
logs to CloudWatch Logs.

On the **Ingest dataset** page, under **Data source
details,** under **IAM role**, select your preferred
method of giving Lookout for Equipment the appropriate permissions.

- **Create an IAM role** is the default. If you select this
  option. Lookout for Equipment will create a role for you with the appropriate permissions.
- **Use an existing role**. If you have previously created an
  IAM role that you want to use with this dataset, you can select it here.
- **Enter a custom IAM role ARN**. This is another way to
  choose an existing role.

## Choosing your schema

You have multiple options in how to structure your data in Amazon S3. Your choice of those
options should be guided by one of two approaches.

_Approach A:_ Your data is already organized in a
particular way, and you prefer to keep it that way. In this case, choose the option
below that best matches the way your data is currently organized.

_Approach B:_ You haven’t yet organized your data.
In that case, examine the options below, and choose one that looks easier to implement.
Then organize your data according to that option.

Before you proceed, be sure your data is [formatted
correctly](formatting-data.md "formatting-data.md").

###### Note

The following options assume that your files and folders have been organized by asset, which is what we recommend.

However, organizing them by sensor, according to the same pattern, is also possible.

- **Option 1 (by filename):**

      + The name of the asset is the complete name of the CSV file.
      + All sensors from that asset are represented in that one CSV
       file.
      + The rest of the hierarchy of your Amazon S3 bucket doesn’t affect the
       ingestion of data for this asset.
      + You can place multiple asset files into one folder.
      + There is one CSV file per asset.

  This is a good option if you have a small set of files, each named after a
  specific asset.

- **Option 2 (by part of filename):**

      + The name of the asset is part of the name of the CSV file.
       (Specifically, it's the part of the filename that precedes the
       delimiter.)
      + The rest of the hierarchy of your Amazon S3 bucket doesn’t affect the
       ingestion of data for this asset.
      + There are multiple CSV files per asset.

  This is a good option if you have to break up large files and give the smaller
  files similar names, such as pump1_january.csv and pump1_february.csv.

If you choose this option, then you must choose a delimiter. The delimiter
indicates which character you are using, within the filename, to separate the
name of the asset from the name of the sensor.

If applicable, select your delimiter from the dropdown menu at the bottom of
the console window.

- **Option 3 (by folder name):**

      + The name of the asset is the complete name of the folder containing
       one or more CSV files.
      + The hierarchy in Amazon S3 is as follows:




      	- Inside the Amazon S3 bucket is the folder you select when you
      	 specify the Amazon S3 location of your data source. Within that folder
      	 is a folder named after the asset.
      	- Inside that folder are all the CSV files for that
      	 asset.
      + There can be multiple CSV files per asset.

  This is a good option if you have many files with long or inconsistent names,
  or a custom folder heirarchy that you want to retain.

## Uploading your data to Amazon S3

You have organized the .csv files that contain your data. Now,
the next step is to upload those files to Amazon S3.

Moving your data to Amazon S3 is a prerequisite to [ingesting your data](ingest-dataset.md "ingest-dataset.md").

1. [Open the Amazon S3 console.](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/")
2. Choose **Create bucket**
3. Under **Bucket name**, enter the name of your bucket. It might be useful to give your bucket the same name as your project, but that's optional.
4. Choose **Create bucket**
5. On the page with the list of buckets, choose your new bucket.
6. Choose **Create folder**.
7. Name your folder.
   - If you chose to use one file for each asset, then the folder should be named after the facility.
   - If you chose to use one file for each sensor, then the folder should be named after the asset.

8. Choose **Create folder**.
9. Choose the folder you created.
10. Choose one of the **Upload** buttons.
11. On the **Upload** page, choose **Add files**.
12. Add the appropriate files from your computer.
13. Choose **Upload**.
14. Return to the Lookout for Equipment console.
15. On the **Ingest dataset** page, under **Data source details**, indicate the location of the files you uploaded to Amazon S3.

So far, you've [created your project](create-project.md "create-project.md"), and (on this page) you've uploaded your well-organized data. Now it's time to integrate those steps by [adding your uploaded data to your project](ingest-dataset.md "ingest-dataset.md").

## Instructing Lookout for Equipment to ingest your data

You've set your permissions, chosen your schema, and (if applicable) chosen your delimiter. Now it is time for Lookout for Equipment to ingest your data.

1. Return to the **Ingest dataset** page.
2. Choose **Ingest dataset**.

You've ingested your data, but it's possible that there was an issue with the files,
the sensors, or the ingestion job as a whole. To find out, you must now [review data ingestion](understanding-ingestion-validation.md "understanding-ingestion-validation.md").
