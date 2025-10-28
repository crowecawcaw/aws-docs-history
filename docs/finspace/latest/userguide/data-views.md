After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Data views for querying data

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

Data views provide you access to the data stored in Amazon FinSpace to perform queries. Each
data view represents a picture of the content of a dataset at a given point in time. A data
view can be historically created from a specified data, or can be auto-updated as new data
is ingested for the dataset via changeset. Multiple views can be created from a dataset
with different dates or with different partitions and column sorting.

######

Topics

- [Data view concepts](data-view-concepts.md "data-view-concepts.md")
- [Create data view](create-data-view.md "create-data-view.md")
- [Sharing data views in Amazon FinSpace](data-sharing-lake-formation.md "data-sharing-lake-formation.md")
