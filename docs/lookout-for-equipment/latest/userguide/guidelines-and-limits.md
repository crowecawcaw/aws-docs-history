

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# Quotas for using Lookout for Equipment
<a name="guidelines-and-limits"></a>

## Supported Regions
<a name="limits-regions"></a>

For a list of AWS Regions where Lookout for Equipment is available, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/lookoutequipment.html) in the *AWS General Reference*.

## Quotas
<a name="limits-all"></a>

Service quotas, also referred to as limits, are the maximum number of service resources for your AWS account. For more information, see [AWS Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) in the *AWS General Reference*. 


<table>
<thead>
  <tr><th>Description</th><th>Quota</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"> <b>Data ingestion</b> </td></tr>
  <tr><td>Maximum number of components per dataset </td><td>3,000 </td></tr>
  <tr><td>Maximum number of datasets per account</td><td>15</td></tr>
  <tr><td>Maximum number of pending data ingestion jobs per account</td><td>5</td></tr>
  <tr><td>Maximum number of models per account</td><td>15</td></tr>
  <tr><td>Maximum number of columns across components per dataset (excluding timestamp) </td><td>3,000</td></tr>
  <tr><td>Maximum number of files per component (per dataset) </td><td>1,000</td></tr>
  <tr><td>Maximum length of component name</td><td>200 characters</td></tr>
  <tr><td>Maximum size per dataset</td><td>50 GB</td></tr>
  <tr><td>Maximum size per file</td><td>5 GB</td></tr>
  <tr><td>Maximum number of pending models per account</td><td>5</td></tr>
  <tr><td>Maximum number of inference schedulers per model</td><td>1</td></tr>
  <tr><td colspan="2"> <b>Training and evaluation</b> </td></tr>
  <tr><td>Maximum number of rows in training data (after resampling) </td><td>1.5 million</td></tr>
  <tr><td>Maximum number of rows in evaluation data (after resampling) </td><td>1.5 million</td></tr>
  <tr><td>Maximum number of components in training data</td><td>300</td></tr>
  <tr><td>Maximum number of columns across components in training data (excluding timestamp) </td><td>300</td></tr>
  <tr><td>Minimum timespan of training data</td><td>180 days</td></tr>
  <tr><td colspan="2"> <b>Inference</b> </td></tr>
  <tr><td>Maximum size of raw data in inference input data (5-min scheduling frequency) </td><td>5 MB</td></tr>
  <tr><td>Maximum size of raw data in inference input data (10-min scheduling frequency) </td><td>10 MB</td></tr>
  <tr><td>Maximum size of raw data in inference input data (15-min scheduling frequency) </td><td>15 MB</td></tr>
  <tr><td>Maximum size of raw data in inference input data (30-min scheduling frequency) </td><td>30 MB</td></tr>
  <tr><td>Maximum size of raw data in inference input data (1-hour scheduling frequency) </td><td>60 MB</td></tr>
  <tr><td>Maximum number of rows in inference input data, after resampling (5-min scheduling frequency) </td><td>300</td></tr>
  <tr><td>Maximum number of rows in inference input data, after resampling (10-min scheduling frequency) </td><td>600</td></tr>
  <tr><td>Maximum number of rows in inference input data, after resampling (15-min scheduling frequency) </td><td>900</td></tr>
  <tr><td>Maximum number of rows in inference input data, after resampling (30-min scheduling frequency) </td><td>1,800</td></tr>
  <tr><td>Maximum number of rows in inference input data, after resampling (1-hour scheduling frequency) </td><td>3,600</td></tr>
  <tr><td>Maximum number of files per component (per inference execution) </td><td>60</td></tr>
</tbody>
</table>
