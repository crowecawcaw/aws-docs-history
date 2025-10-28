After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Adding and managing data in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

People with different roles such as Analyst, Data Scientist, Data Engineer, Data Governor, Audit personnel use Amazon FinSpace for data organization, governance, preparation, and analysis.
FinSpace supports data of any file format with additional features for structure data formats such as CSV.

FinSpace represents data in the catalog using a structure called a Dataset. Dataset is a logical container of semantically identical data and schema.

![A diagram that shows the dataset meta model.](images/05-add-and-manage-data/dataset-meta-model.png)
The first step is loading data into FinSpace, often referred to as ingesting data. FinSpace supports loading data in a variety of data formats and sources.
You can load data by connecting in your data feeds or upload ad-hoc data through the web application.

After your data is available in FinSpace, you can do the following:

- Describe datasets to provide business context by using fields specified from Attribute Sets.
- Control who can access the data by assigning permissions to permission groups.
- Create data views that allow users to query data in FinSpace notebooks.
- Using the notebooks, create derived data by joining data and from the results of analysis of a dataset.
- Generate audit report on activity.

######

Topics

- [Loading data into Amazon FinSpace](load-data-into-finspace.md "load-data-into-finspace.md")
- [Supported data types and file formats in Amazon FinSpace](supported-data-types.md "supported-data-types.md")
- [Working with datasets in Amazon FinSpace](working-with-datasets.md "working-with-datasets.md")
