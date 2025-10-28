# Development endpoint workflow

To use an AWS Glue development endpoint, you can follow this workflow:

1. Create a development endpoint using the API. The endpoint is launched in a
   virtual private cloud (VPC) with your defined security groups.
2. The API polls the development endpoint until it is provisioned and ready for work.
   When it's ready, connect to the development endpoint using one of the following methods to
   create and test AWS Glue scripts.
   - Create an SageMaker AI notebook in your account. For more information about how to create
     a notebook, see [Authoring code with AWS Glue Studio notebooks](notebooks-chapter.md "notebooks-chapter.md").
   - Open a terminal window to connect directly to a development endpoint.
   - If you have the professional edition of the JetBrains [PyCharm Python IDE](https://www.jetbrains.com/pycharm/ "https://www.jetbrains.com/pycharm/"), connect it to a
     development endpoint and use it to develop interactively. If you insert `pydevd`
     statements in your script, PyCharm can support remote breakpoints.

3. When you finish debugging and testing on your development endpoint, you can delete
   it.
