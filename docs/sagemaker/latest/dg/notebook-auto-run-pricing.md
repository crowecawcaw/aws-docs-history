# Pricing for SageMaker Notebook Jobs

When you schedule notebook jobs, your Jupyter notebooks run on SageMaker training instances.
After you select an **Image** and **Kernel** in your
**Create Job** form, the form provides a list of available compute types.
You are charged for the compute type you choose, based on the combined duration of use for all
notebook jobs that run from the job definition. If you don’t specify a compute type, SageMaker AI
assigns you a default Amazon EC2 instance type of `ml.m5.large`. For a breakdown of SageMaker AI
pricing by compute type, see [Amazon SageMaker AI
Pricing](https://aws.amazon.com/sagemaker/pricing "https://aws.amazon.com/sagemaker/pricing").
