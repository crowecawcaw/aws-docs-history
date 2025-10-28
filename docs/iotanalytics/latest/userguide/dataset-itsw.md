End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Working with AWS IoT SiteWise data

AWS IoT SiteWise is a managed service that you can use to collect,
model, analyze, and visualize data from industrial equipment at scale. The service provides
an asset modeling framework for building representations of your industrial devices,
processes, and facilities.

With AWS IoT SiteWise asset models, you can define what industrial equipment data to consume and how
to process your data into complex metrics. You can configure asset models to collect and
process data in the AWS Cloud. For more information, see the [AWS IoT SiteWise](../../../iot-sitewise/latest/userguide/what-is-sitewise.md "../../../iot-sitewise/latest/userguide/what-is-sitewise.md") User
Guide.

AWS IoT Analytics integrates with AWS IoT SiteWise so you can run and schedule SQL queries on AWS IoT SiteWise data. To
start querying your AWS IoT SiteWise data, create a data store by following the procedures in [Configure storage settings](../../../iot-sitewise/latest/userguide/configure-storage.md "../../../iot-sitewise/latest/userguide/configure-storage.md") in the
_AWS IoT SiteWise User Guide_. Then, follow the steps in [Create a dataset with AWS IoT SiteWise data (Console)](create-dataset-itsw-console.md "create-dataset-itsw-console.md") or
in [Create a dataset with AWS IoT SiteWise data (AWS CLI)](create-dataset-itsw-cli.md "create-dataset-itsw-cli.md") to
create an AWS IoT Analytics dataset and run a SQL query on your industrial data.

###### Topics

- [Create an AWS IoT Analytics dataset with AWS IoT SiteWise data](create-dataset-mls.md "create-dataset-mls.md")
- [Access dataset contents](dataset-results-itsw.md "dataset-results-itsw.md")
- [Tutorial: Query AWS IoT SiteWise data in AWS IoT Analytics](tutorial-query-mls.md "tutorial-query-mls.md")
