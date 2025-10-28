# Overview of using notebooks

AWS Glue Studio allows you to interactively author jobs in a notebook interface based on
Jupyter Notebooks.
Through notebooks in AWS Glue Studio, you can edit job scripts and view the output without having
to run a full job, and you can edit data integration code and view the output without having to run a
full job, and you can add markdown and save notebooks as .ipynb files and job scripts. You can start a
notebook without installing software locally or managing servers. When you are satisfied with your code,
AWS Glue Studio can convert your notebook to a Glue job with the click of a button.

Some benefits of using notebooks include:

- No cluster to provision or manage
- No idle clusters to pay for
- No up-front configuration required
- No installation of Jupyter notebooks required
- The same runtime/platform as AWS Glue ETL

When you start a notebook through AWS Glue Studio, all the configuration steps are done for you
so that you can explore your data and start developing your job script after only a few seconds.
AWS Glue Studio configures a Jupyter notebook with the AWS Glue Jupyter kernel.
You don’t have to configure VPCs, network connections, or development endpoints to use this notebook.

To create jobs using the notebook interface:

- configure the necessary IAM permissions.
- start a notebook session to create a job
- write code in the cells in the notebook
- run and test the code to view the output
- save the job

After your notebook is saved, your notebook is a full AWS Glue job. You can manage all aspects of the job,
such as scheduling jobs runs, setting job parameters, and viewing the job run history right along side your notebook.
