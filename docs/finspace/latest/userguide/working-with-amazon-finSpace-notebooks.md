After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Working with Amazon FinSpace notebooks

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

Amazon FinSpace notebook provides an Integrated Development Environment (IDE) that lets you access data from the FinSpace Data Catalog to perform data
preparation and analysis. FinSpace simplifies the use of Apache Spark providing access to fully managed Spark Clusters using easy to launch cluster templates. For more information, see [Apache Spark](https://spark.apache.org/ "https://spark.apache.org/").

###### Note

- In order to use notebooks and Spark clusters, you must be a superuser or a member of a group with necessary permissions - **Access Notebooks, Manage Clusters**.
- The Spark clusters are terminated daily at midnight US Eastern time.
  FinSpace notebooks are programmed using Python. Python and Spark integration is achieved using the PySpark library. For more information, see [PySpark](https://spark.apache.org/docs/latest/api/python/ "https://spark.apache.org/docs/latest/api/python/").

######

Topics

- [Opening the notebook environment](opening-the-notebook-environment.md "opening-the-notebook-environment.md")
- [Working in the notebook environment](working-in-the-notebook-environment.md "working-in-the-notebook-environment.md")
- [Access datasets from a notebook](access-datasets-notebook.md "access-datasets-notebook.md")
- [Example notebooks](example-notebook.md "example-notebook.md")
