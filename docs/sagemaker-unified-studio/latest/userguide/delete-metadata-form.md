# Delete a metadata form in Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, metadata forms are simple forms to augment additional business context to
the asset metadata in the catalog. They serve as extensible mechanisms for data owners to
enrich the asset with information that can help data users when they search and find that
data. Metadata forms can also serve a mechanism to enforce consistency to all assets being
published to the Amazon SageMaker Unified Studio catalog.

A metadata form definition is composed of one or more field definitions, with support for
boolean, date, decimal, integer, string, and business glossary field value data types. For
more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md").
To create, edit, or delete metadata forms in your Amazon SageMaker Unified Studio domain, you must be a member of
the owning project who has the right credentials.

To delete a metadata form, complete the following steps:

###### Note

Before you can delete a metadata form, you must remove it from all asset types or assets
to which it is applied.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the **Discover** menu in the top navigation bar.
3. Choose **Metadata forms**.
4. Choose the name of the metadata form that you want to delete. This takes you to the metadata form details page.
5. If the metadata form that you want to delete is enabled, disable the metadata form by
   choosing the **Enabled** toggle.
6. On the metadata form's details page, expand **Actions**, and then
   choose **Delete**.
7. Confirm deletion by choosing **Delete**.
