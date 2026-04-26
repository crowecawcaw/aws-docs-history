# Search for and view assets in the Amazon SageMaker Unified Studio catalog

Amazon SageMaker Unified Studio provides a streamlined way to search for data. Any Amazon SageMaker Unified Studio user with
permissions to access Amazon SageMaker Unified Studio can search for assets in the Amazon SageMaker Unified Studio catalog and view asset
names and the metadata assigned to them. You can take a closer look at an asset by examining
its details page.

###### Note

To view the actual data that an asset contains, you must first subscribe to the asset
and have your subscription request approved and access granted.

###### To search for assets in the catalog

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. In the left navigation pane, choose **Catalog**.
3. Choose **Browse assets**.
4. Find the asset that you want to subscribe to by browsing or entering the name of the asset
   into the search bar. You can apply filters to narrow the results. The filters include
   asset type, source account, the AWS Region to which the asset belongs, date range, and
   custom metadata filters. To add a custom metadata filter, choose
   **Add Filter** at the bottom of the filters panel. You can filter by
   asset name, description, or metadata form fields.

For metadata form filters, select the form, field, and operator
(`contains` for string fields; `equals`,
`greater than`, or `less than` for numeric fields). Enter a
value and choose **Apply**. You can combine multiple custom
filters.

Filter selections persist in your browser by using local storage. Only fields that are marked
as searchable (strings) or sortable (numerics) are available for filtering. 5. To view details about a specific asset, choose the asset to open its details page. The
details page includes the following information:

    * The asset name and type.
    * A description of the asset.
    * The current published revision of the asset, the owner, whether approval is
     required for subscriptions, and update history.
    * A **Business metadata** tab which includes glossary terms and
     metadata forms.
    * A **Subscription requests** tab which includes a list of
     subscribers to the domain.
    * A **Lineage** tab which displays a chart of past revisions of the
     asset.
