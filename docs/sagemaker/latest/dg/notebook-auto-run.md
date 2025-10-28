# SageMaker Notebook Jobs

You can use Amazon SageMaker AI to interactively build, train, and deploy machine learning models from
your Jupyter notebook in any JupyterLab environment. However, there are various scenarios in
which you might want to run your notebook as a noninteractive, scheduled job. For example, you
might want to create regular audit reports that analyze all training jobs run over a certain
time frame and analyze the business value of deploying those models into production. Or you
might want to scale up a feature engineering job after testing the data transformation logic on
a small subset of data. Other common use cases include:

- Scheduling jobs for model drift monitoring
- Exploring the parameter space for better models
  In these scenarios, you can use SageMaker Notebook Jobs to create a noninteractive job (which
  SageMaker AI runs as an underlying training job) to either run on demand or on a schedule. SageMaker Notebook
  Jobs provides an intuitive user interface so you can schedule your jobs right from JupyterLab by
  choosing the Notebook Jobs widget (
  ![Blue icon of a calendar with a checkmark, representing a scheduled task or event.](images/icons/notebook-schedule.png)
  ) in your notebook. You can also schedule your jobs using the SageMaker AI Python
  SDK, which offers the flexibility of scheduling multiple notebook jobs in a pipeline workflow.
  You can run multiple notebooks in parallel, and parameterize cells in your notebooks to
  customize the input parameters.

This feature leverages the Amazon EventBridge, SageMaker Training and Pipelines services and is available for
use in your Jupyter notebook in any of the following environments:

- Studio, Studio Lab, Studio Classic, or Notebook Instances
- Local setup, such as your local machine, where you run JupyterLab

###### Prerequisites

To schedule a notebook job, make sure you meet the following criteria:

- Ensure your Jupyter notebook and any initialization or startup scripts are self-contained
  with respect to code and software packages. Otherwise, your noninteractive job may incur
  errors.
- Review [Constraints and considerations](notebook-auto-run-constraints.md "notebook-auto-run-constraints.md") to make sure you properly configured your
  Jupyter notebook, network settings, and container settings.
- Ensure your notebook can access needed external resources, such as Amazon EMR
  clusters.
- If you are setting up Notebook Jobs in a local Jupyter notebook, complete the
  installation. For instructions, see [Installation guide](scheduled-notebook-installation.md "scheduled-notebook-installation.md").
- If you connect to an Amazon EMR cluster in your notebook and want to parameterize your Amazon EMR
  connection command, you must apply a workaround using environment variables to pass
  parameters. For details, see [Connect to an Amazon EMR cluster from your
  notebook](scheduled-notebook-connect-emr.md "scheduled-notebook-connect-emr.md").
- If you connect to an Amazon EMR cluster using Kerberos, LDAP, or HTTP Basic Auth
  authentication, you must use the AWS Secrets Manager to pass your security credentials to your Amazon EMR
  connection command. For details, see [Connect to an Amazon EMR cluster from your
  notebook](scheduled-notebook-connect-emr.md "scheduled-notebook-connect-emr.md").
- (optional) If you want the UI to preload a script to run upon notebook startup, your
  admin must install it with a Lifecycle Configuration (LCC). For information about how to use
  a LCC script, see [Customize a Notebook Instance
  Using a Lifecycle Configuration Script](notebook-lifecycle-config.md "notebook-lifecycle-config.md").
