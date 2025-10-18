# How CloudWatch Evidently collects and stores data

###### Important

End of support notice: On October 16, 2025, AWS 
 will discontinue support for CloudWatch Evidently. After October 16, 2025, you will 
 no longer be able to access the Evidently console or Evidently resources. 
 

Amazon CloudWatch Evidently collects and stores data related to project configurations so that 
 customers can run experiments and launches. The data includes the following:


* Metadata about projects, features, launches, and experiments
* Metric events
* Evaluation data
Resource metadata is stored in Amazon DynamoDB. The data is encrypted at rest by
 default, using AWS owned keys. These keys are a collection of AWS KMS keys that an
 AWS service owns and manages for use in multiple AWS accounts. Customers can’t view,
 manage, or audit the use of these keys. Customers are also not required to take action
 or change programs to protect the keys that encrypt their data.

For more information, see 
 [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk") in the AWS Key Management Service Developer Guide.

Evidently metric events and evaluation events are delivered directly to customer-owned
 locations.

 Data in transit is automatically
 encrypted with HTTPS. This data will be delivered to customer-owned locations.

You can also choose to store evaluation events in Amazon Simple Storage Service or Amazon CloudWatch Logs. For more information about 
 how you can secure your data in these services, see
 [Enabling Amazon S3 default bucket encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html") and [Encrypting log data in CloudWatch Logs using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html").

**Retrieving data**

You can retrieve your data using CloudWatch Evidently APIs. To retrieve project 
 data, use [GetProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetProject.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetProject.html")
 or [ListProjects](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListProjects.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListProjects.html").

To retrieve feature 
 data, use [GetFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetFeature.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetFeature.html")
 or [ListFeatures](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListFeature.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListFeature.html").

To retrieve launch 
 data, use [GetLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetLaunch.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetLaunch.html")
 or [ListLaunches](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListLaunches.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListLaunches.html").

To retrieve experiment 
 data, use [GetExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetExperiment.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetExperiment.html"),
 [ListExperiments](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListExperiments.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListExperiments.html"), 
 or [GetExperimentResults](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetExperimentResults.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetExperimentResults.html").

**Modifying and deleting data**

You can modify and delete your data using CloudWatch Evidently APIs. For project 
 data, use [UpdateProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateProject.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateProject.html")
 or [DeleteProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteProject.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteProject.html").

For feature 
 data, use [UpdateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateFeature.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateFeature.html")
 or [DeleteFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteFeature.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteFeature.html").

For launch 
 data, use [UpdateLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateLaunch.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateLaunch.html")
 or [DeleteLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteLaunch.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteLaunch.html").

For experiment 
 data, use [UpdateExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateExperiment.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateExperiment.html") or
 [DeleteExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteExperiment.html "https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteExperiment.html").
