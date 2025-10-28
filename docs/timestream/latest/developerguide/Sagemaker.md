For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Amazon SageMaker AI

You can use Amazon SageMaker Notebooks to integrate your machine learning models with Amazon
Timestream. To help you get started, we have created a sample SageMaker Notebook that processes
data from Timestream. The data is inserted into Timestream from a multi-threaded Python
application continuously sending data. The source code for the sample SageMaker Notebook and the
sample Python application are available in GitHub.

1. Create a database and table following the instructions described in [Create a database](console_timestream.md#console_timestream.db.using-console "console_timestream.md#console_timestream.db.using-console") and [Create a table](console_timestream.md#console_timestream.table.using-console "console_timestream.md#console_timestream.table.using-console").
2. Clone the GitHub repository for the [multi-threaded Python sample application](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/continuous-ingestor "https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/continuous-ingestor") following the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository").
3. Clone the GitHub repository for the [sample Timestream SageMaker Notebook](https://github.com/awslabs/amazon-timestream-tools/blob/master/integrations/sagemaker "https://github.com/awslabs/amazon-timestream-tools/blob/master/integrations/sagemaker") following the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository").
4. Run the application for continuously ingesting data into Timestream following the
   instructions in the [README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/continuous-ingestor/README.md "https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/continuous-ingestor/README.md").
5. Follow the instructions to create an Amazon S3 bucket for Amazon SageMaker as described
   [here](../../../sagemaker/latest/dg/gs-config-permissions.md "../../../sagemaker/latest/dg/gs-config-permissions.md").
6. Create an Amazon SageMaker instance with latest boto3 installed: In addition to the
   instructions described [here](../../../sagemaker/latest/dg/gs-setup-working-env.md "../../../sagemaker/latest/dg/gs-setup-working-env.md"), follow the steps below:
   1. On the **Create notebook** instance page, click on **Additional
      Configuration**
   2. Click on **Lifecycle configuration - _optional_** and
      select **Create a new lifecycle configuration**
   3. On the _Create lifecycle configuration_ wizard box, do the
      following:
      1. Fill in a desired name to the configuration, e.g. `on-start`
      2. In Start Notebook script, copy-paste the script content from [Github](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples/blob/master/scripts/install-pip-package-single-environment/on-start.sh "https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples/blob/master/scripts/install-pip-package-single-environment/on-start.sh")
      3. Replace `PACKAGE=scipy` with `PACKAGE=boto3` in the pasted
         script.

7. Click on **Create configuration**
8. Go to the IAM service in the AWS Management Console and find the newly created SageMaker
   execution role for the notebook instance.
9. Attach the IAM policy for `AmazonTimestreamFullAccess` to the execution
   role.

###### Note

The `AmazonTimestreamFullAccess` IAM policy is not restricted to specific
resources and is unsuitable for production use. For a production system, consider using
policies that restrict access to specific resources. 10. When the status of the notebook instance is **InService**, choose
**Open Jupyter** to launch a SageMaker Notebook for the instance 11. Upload the files `timestreamquery.py` and
`Timestream_SageMaker_Demo.ipynb` into the Notebook by selecting the
**Upload** button 12. Choose `Timestream_SageMaker_Demo.ipynb`

###### Note

If you see a pop up with **Kernel not found**, choose
**conda_python3** and click **Set Kernel**. 13. Modify `DB_NAME`, `TABLE_NAME`, `bucket`, and
`ENDPOINT` to match the database name, table name, S3 bucket name, and region for
the training models. 14. Choose the **play** icon to run the individual cells 15. When you get to the cell `Leverage Timestream to find hosts with average CPU
 utilization across the fleet`, ensure that the output returns at least 2 host
names.

###### Note

If there are less than 2 host names in the output, you may need to rerun the sample Python
application ingesting data into Timestream with a larger number of threads and host-scale. 16. When you get to the cell `Train a Random Cut Forest (RCF) model using the CPU
 utilization history`, change the `train_instance_type` based on the resource
requirements for your training job 17. When you get to the cell `Deploy the model for inference`, change the
`instance_type` based on the resource requirements for your inference job

###### Note

It may take a few minutes to train the model. When the training is complete, you will see
the message **Completed - Training job completed** in the output of the
cell. 18. Run the cell `Stop and delete the endpoint` to clean up resources. You can also
stop and delete the instance from the SageMaker console
