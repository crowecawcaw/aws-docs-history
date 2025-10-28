After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Using external datasets in Amazon FinSpace

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

External datasets are the datasets that a data connector creates. They refer to the data
that resides outside of FinSpace. You can use external datasets to discover and use data assets
that reside in an external data repository from within FinSpace—without having to copy
the data into a FinSpace environment.

## External datasets in the FinSpace

catalog

You can access the external datasets by using the FinSpace web application. Currently,
FinSpace only supports the Goldman Sachs Financial Cloud for Data as an external datasets source. In the catalog,
these datasets have the _Attribute-set_ label of
**Goldman Sachs Financial Cloud for Data** applied to them.

The external datasets behave like regular datasets, but are different in the
following ways:

- You can't delete external datasets. FinSpace can only remove them as a result of a data connector
  run.
- You can't add data to an external dataset from FinSpace using changesets. For this reason, the
  **Add Data** and **Replace Data** buttons
  aren't visible when you view an external dataset in the FinSpace catalog.
- Each dataset contains a system-generated data view called an _external
  data view_. You can't generate any other additional data
  views.
- You can't add or remove external datasets from the system-generated permission groups where
  they were added by the data connector. To grant users access to external datasets,
  add them to the system-generated permission groups.
- You can't add external datasets to permission groups other than the system-generated one that
  is created by running the data connector.
- You can't remove the system-generated attribute set that is applied to an external
  dataset.

## Browse external datasets

###### To browse external datasets using the FinSpace catalog

1. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
2. On the left navigation bar of the home page, choose
   **Catalog**.
3. From the data browser, choose the **External Data**
   category.
4. Choose the **Goldman Sachs Financial Cloud for Data** category, and then select the
   required dataset. The dataset details page opens, and you can view details about
   the selected dataset.

## Access external datasets from FinSpace

notebook using Spark

The process of accessing external data using a FinSpace notebook is same as accessing any
other datasets. For more information, see [Access datasets from a notebook](access-datasets-notebook.md "access-datasets-notebook.md").

**Specifying additional parameters**

With external datasets, you can also specify additional parameters to pre-filter the
data that returns to a Spark DataFrame. To do this, you use the _partition_filter_ parameter. The parameters that you specify depend on the
particular data provider that you use. For information on the specific parameters for
the Goldman Sachs Financial Cloud for Data, refer to the [Marquee
documentation](https://developer.gs.com/p/docs/services/data/ "https://developer.gs.com/p/docs/services/data/").

The following is an example of specifying additional parameters.

```

        df = analytics.read_data_view( dataset_id="<dataset_id>", data_view_id="<data_view_id>",
partition_filter={
"exchange": ["NASDAQ", "NYSE"],
"symbol": ["AMZN", "GOOG"],
}
)
```

In the preceding example, the <dataset_id> is a FinSpace dataset ID such as
_rgg1nj1_, and <data_view_id> is a FinSpace data
view ID such as _VrvKEKnA1El2nr821BaLTQ_.
