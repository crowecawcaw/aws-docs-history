# Programming Ray scripts

###### Important

AWS Glue for Ray is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Glue for Ray end of support](awsglue-ray-jobs-availability-change.md "awsglue-ray-jobs-availability-change.md").

AWS Glue makes it easy to write and run Ray scripts. This section describes the supported Ray
capabilities that are available in AWS Glue for Ray. You program Ray scripts in Python.

Your custom script must be compatible with the version of Ray that's defined by the `Runtime`
field in your job definition. For more information about `Runtime` in the Jobs API, see [Jobs](aws-glue-api-jobs-job.md "aws-glue-api-jobs-job.md"). For information about each runtime environment, see [Supported Ray runtime environments](ray-jobs-section.md#author-job-ray-runtimes "ray-jobs-section.md#author-job-ray-runtimes").

###### Topics

- [Tutorial: Writing an ETL script in AWS Glue for Ray](edit-script-ray-intro-tutorial.md "edit-script-ray-intro-tutorial.md")
- [Using Ray Core and Ray Data in AWS Glue for Ray](edit-script-ray-scripting.md "edit-script-ray-scripting.md")
- [Providing files and Python libraries to Ray jobs](edit-script-ray-env-dependencies.md "edit-script-ray-env-dependencies.md")
- [Connecting to data in Ray jobs](edit-script-ray-connections-formats.md "edit-script-ray-connections-formats.md")
