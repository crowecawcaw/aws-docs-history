# Notebook editor components

The notebook editor interface has the following main sections.

- Notebook interface (main panel) and toolbar
- Job editing tabs

## The notebook editor

The AWS Glue Studio notebook editor is based on the Jupyter Notebook Application.
The AWS Glue Studio notebook interface is similar to that provided by Juypter Notebooks, which is
described in the section
[Notebook user interface](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html?highlight=toolbar#notebook-user-interface "https://jupyter-notebook.readthedocs.io/en/stable/notebook.html?highlight=toolbar#notebook-user-interface") .
The notebook used by interactive sessions is a Jupyter Notebook.

Although the AWS Glue Studio notebook is similar to Juptyer Notebooks, it differs in a few key ways:

- currently, the AWS Glue Studio notebook cannot install extensions
- you cannot use multiple tabs; there is a 1:1 relationship between a job and a notebook
- the AWS Glue Studio notebook does not have the same top file menu that exists in Jupyter Notebooks
- currently, the AWS Glue Studio notebook only runs with the AWS Glue kernel. Note that you cannot update the kernel on your own.

## AWS Glue Studio job editing tabs

The tabs that you use to interact with the ETL job are at the top of the notebook page. They
are similar to tabs that appear in the visual job editor of AWS Glue Studio, and they
perform the same actions.

- **Notebook** – Use this tab to view the job
  script using the notebook interface.
- **Job details** – Configure the
  environment and properties for the job runs.
- **Runs** – View information about
  previous runs of this job.
- **Schedules** – Configure a schedule
  for running your job at specific times.
