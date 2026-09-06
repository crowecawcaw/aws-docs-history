

# Migrating from dev endpoints to interactive sessions
<a name="development-migration-checklist"></a>

 Use the following checklist to determine the appropriate method to migrate from dev endpoints to interactive sessions. 

 **Does your script depend on AWS Glue 0.9 or 1.0 specific features (for example, HDFS, YARN, etc.)?** 

 If the answer is yes, see [Migrating AWS Glue for Spark jobs to  AWS Glue version 4.0](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-40.html) to learn how to migrate from Glue 0.9 or 1.0 to Glue 4.0 and later. 

 **Which method do you use to access your dev endpoint?** 


| If you use this method | Then do this | 
| --- | --- | 
| SageMaker AI notebook, Jupyter notebook, or JupyterLab | Migrate to [AWS Glue Studio notebook](https://docs.aws.amazon.com/glue/latest/dg/notebook-getting-started.html) by downloading .ipynb files on Jupyter and create a new AWS Glue Studio notebook job by uploading the  .ipynb file. Alternatively, you can also use [ SageMaker AI Studio](https://aws.amazon.com/blogs/machine-learning/prepare-data-at-scale-in-amazon-sagemaker-studio-using-serverless-aws-glue-interactive-sessions/) and select the AWS Glue kernel.  | 
| Zeppelin notebook | Convert the notebook to a Jupyter notebook manually by copying and pasting code or automatically using a third-party converter such as ze2nb. Then, use the notebook in AWS Glue Studio notebook or SageMaker AI Studio.  | 
| IDE |  See [ Author AWS Glue jobs with PyCharm using AWS Glue interactive sessions](https://aws.amazon.com/blogs/big-data/author-aws-glue-jobs-with-pycharm-using-aws-glue-interactive-sessions/), or [ Using interactive sessions with Microsoft Visual Studio Code](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-vscode.html).  | 
| REPL |  Install the [`aws-glue-session package`](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions.html) locally, then run the following command: +   For Python: `jupyter console --kernal glue_pyspark`  <br />+   For Scala: `jupyter console --kernal glue_spark`   | 
| SSH | No corresponding option on interactive sessions. Alternatively, you can use a Docker image. To learn more, see [Developing using a Docker image](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-libraries.html#develop-local-docker-image).  | 