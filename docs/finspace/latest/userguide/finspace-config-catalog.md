After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Understanding datasets in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

Datasets are described, organized, and made browsable and searchable in Amazon FinSpace with three constructs:

- **Categories** – Categories allow for cataloging of datasets by commonly used business terms.
  Categories are hierarchical in nature, allowing for each node of the hierarchy to have a name and a description.
  The order of the nodes within a level are defined when you define categories.
  The **Categories** are displayed in the data browser when you choose **Catalog** on the left navigation bar.
- **Controlled Vocabularies** – Controlled Vocabularies are enumeration lists of attributes to describe datasets.
- **Attribute Sets** – Attribute Sets are lists of attributes that can be applied to datasets.
  Attributes are metadata fields used to capture additional business context for each dataset.
  You can then browse and search attributes to find a dataset based on the values assigned to the attributes.
  For information on how to configure your business catalog see [Tutorial: Configuring a business data catalog in Amazon FinSpace](tutorial-build-business-catalog.md "tutorial-build-business-catalog.md").

######

Topics

- [Configuring categories in Amazon FinSpace](categories.md "categories.md")
- [Configuring controlled vocabularies in Amazon FinSpace](controlled-vocabularies.md "controlled-vocabularies.md")
- [Configuring attribute sets in Amazon FinSpace](attribute-sets.md "attribute-sets.md")
- [Tutorial: Configuring a business data catalog in Amazon FinSpace](tutorial-build-business-catalog.md "tutorial-build-business-catalog.md")
