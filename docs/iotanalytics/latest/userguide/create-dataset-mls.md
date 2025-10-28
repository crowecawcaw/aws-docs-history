End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Create an AWS IoT Analytics dataset with AWS IoT SiteWise data

An AWS IoT Analytics dataset contains SQL statements and expressions that you use to query data in your data store along with an optional schedule that repeats the query at a day and time that you specify. You can use expressions similar to [Amazon CloudWatch schedule expressions](../../../AmazonCloudWatch/latest/events/ScheduledEvents.md "../../../AmazonCloudWatch/latest/events/ScheduledEvents.md") to create the optional schedules.

###### Note

A dataset is typically a collection of data that might or might not be organized in tabular form. In contrast, AWS IoT Analytics creates your dataset by applying a SQL query to data in your data store.

Follow these steps to get started with creating a dataset for your AWS IoT SiteWise data.

###### Topics

- [Create a dataset with AWS IoT SiteWise data (Console)](create-dataset-itsw-console.md "create-dataset-itsw-console.md")
- [Create a dataset with AWS IoT SiteWise data (AWS CLI)](create-dataset-itsw-cli.md "create-dataset-itsw-cli.md")
