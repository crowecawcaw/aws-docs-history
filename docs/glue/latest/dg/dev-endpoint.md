# Developing scripts using development endpoints

###### Note

Development Endpoints are only supported for versions of AWS Glue prior to 2.0. For an interactive environment where you can author and test ETL scripts, use
[Notebooks on AWS Glue Studio](../ug/notebooks-chapter.md "../ug/notebooks-chapter.md").

AWS Glue can create an environment—known as a _development
endpoint_—that you can use to iteratively develop and test your extract, transform,
and load (ETL) scripts. You can create, edit, and delete development endpoints using the
AWS Glue console or API.

## Managing your development environment

When you create a development endpoint, you provide configuration values to provision the
development environment. These values tell AWS Glue how to set up the network so
that you can access the endpoint securely and the endpoint can access your data stores.

You can then create a notebook that connects to the endpoint, and use your notebook to
author and test your ETL script. When you're satisfied with the results of your development
process, you can create an ETL job that runs your script. With this process, you can add
functions and debug your scripts in an interactive manner.

Follow the tutorials in this section to learn how to use your development endpoint with
notebooks.

###### Topics

- [Development endpoint workflow](dev-endpoint-workflow.md "dev-endpoint-workflow.md")
- [How AWS Glue development endpoints
  work with SageMaker notebooks](dev-endpoint-how-it-works.md "dev-endpoint-how-it-works.md")
- [Adding a development endpoint](add-dev-endpoint.md "add-dev-endpoint.md")
- [Accessing your development endpoint](dev-endpoint-elastic-ip.md "dev-endpoint-elastic-ip.md")
- [Tutorial: Set up a Jupyter notebook in JupyterLab to test and debug ETL scripts](dev-endpoint-tutorial-local-jupyter.md "dev-endpoint-tutorial-local-jupyter.md")
- [Tutorial: Use a SageMaker AI notebook with your
  development endpoint](dev-endpoint-tutorial-sage.md "dev-endpoint-tutorial-sage.md")
- [Tutorial: Use a REPL shell with your development endpoint](dev-endpoint-tutorial-repl.md "dev-endpoint-tutorial-repl.md")
- [Tutorial: Set up PyCharm professional with a
  development endpoint](dev-endpoint-tutorial-pycharm.md "dev-endpoint-tutorial-pycharm.md")
- [Advanced configuration: sharing development endpoints
  among multiple users](dev-endpoint-sharing.md "dev-endpoint-sharing.md")
