# Best practice 3.4 – Identify the source data owners and have them set the data classifications

Identify the owners of the source data, like business data owners, and agree what level of protection is required for the data within the analytics platform.

Data classifications follow the data as it moves throughout
the analytics workﬂow to ensure that the data is protected,
and to determine who and what systems are allowed to access
the data. By following the organization’s classification
policies, the analytics workload should be able to
differentiate the data protection implementations for each
class of data. Because each organization has different kinds
of classification, the analytics workload should provide a
strong logical boundary between processing data of different
sensitivity levels. These classifications include
_restricted_,
_confidential_, and
_sensitive_.

## Suggestion 3.4.1 – Assign owners per each dataset

A dataset, or a table in relational database, is a collection of data. A Data Catalog is a collection of metadata that helps centralize share and search information about the data within your platform. In addition to assigned classifications, this capability allows teams to search for data assets and decide whether the data asset is valuable for their analyze or data science workload.

The administrator of the analytics workload should know who are the owners for each dataset, and should assign the dataset ownership in the Data Catalog.

## Suggestion 3.4.2 – Define attestation scope and reviewer as additional scope for sensitive data

As the owner of the analytics workload, you should know
the data owner for each dataset. For example, when a
dataset classified as highly sensitive has permission
issues within the organization, you might have to talk to
the dataset owners and have them resolve the issues.

## Suggestion 3.4.3 – Set expiry for data ownership and attestation, and have owners reconfirm periodically

As businesses change, the data owners and the data
classifications might change as well. Run campaigns
periodically, such as quarterly or yearly, to request each
of the dataset owners to reconfirm that they are still the
right owners, and that the data classifications are still
accurate.
