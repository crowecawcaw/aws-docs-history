# AWS HealthImaging throttling limits

Your AWS account has throttling limits that apply to AWS HealthImaging API actions. For all
actions, a `ThrottlingException` error is thrown if throttling limits are exceeded. For
more information, see the [_AWS HealthImaging API Reference_](../APIReference.md "../APIReference.md").

###### Note

Throttling limits are adjustable for all HealthImaging API actions. To request a throttling limit
adjustment, contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
To create a case, log in to your AWS account and choose **Create
case**.

The following table lists throttling limits for both [native HealthImaging actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") and
[representations of DICOMweb services](using-dicomweb.md "using-dicomweb.md").

| AWS HealthImaging throttling limits | Action    | Throttle rate | Throttle burst |
| ----------------------------------- | --------- | ------------- | -------------- |
| CreateDatastore                     | 0.085 tps | 1 tps         |
| GetDatastore                        | 10 tps    | 20 tps        |
| ListDatastores                      | 5 tps     | 10 tps        |
| DeleteDatastore                     | 0.085 tps | 1 tps         |
| StartDICOMImportJob                 | 1 tps     | 2 tps         |
| GetDICOMImportJob                   | 25 tps    | 50 tps        |
| ListDICOMImportJobs                 | 10 tps    | 20 tps        |
| SearchImageSets                     | 25 tps    | 50 tps        |
| GetImageSet                         | 25 tps    | 50 tps        |
| GetImageSetMetadata                 | 50 tps    | 100 tps       |
| GetImageFrame                       | 1000 tps  | 2000 tps      |
| ListImageSetVersions                | 25 tps    | 50 tps        |
| UpdateImageSetMetadata              | 0.25 tps  | 1 tps         |
| CopyImageSet                        | 0.25 tps  | 1 tps         |
| DeleteImageSet                      | 0.25 tps  | 1 tps         |
| TagResource                         | 10 tps    | 20 tps        |
| ListTagsForResource                 | 10 tps    | 20 tps        |
| UntagResource                       | 10 tps    | 20 tps        |
| GetDICOMInstance\*                  | 50 tps    | 100 tps       |
| GetDICOMInstanceMetadata\*          | 50 tps    | 100 tps       |
| GetDICOMInstanceFrames\*            | 50 tps    | 100 tps       |
| GetDICOMSeriesMetadata              | 50 tps    | 100 tps       |

\*Representation of a DICOMweb service
