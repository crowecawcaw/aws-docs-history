# Edit a field in a metadata

form in Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, metadata forms are simple forms to augment additional business context to
the asset metadata in the catalog. They serve as extensible mechanisms for data owners to
enrich the asset with information that can help data users when they search and find that
data. Metadata forms can also serve an mechanism to enforce consistency to all assets being
published to the Amazon SageMaker Unified Studio catalog.

A metadata form definition is composed of one or more field definitions, with support for
boolean, date, decimal, integer, string, and business glossary field value data types. For
more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md").
To create, edit, or delete fields in metadata forms in your Amazon SageMaker Unified Studio domain, you must be a
member of the owning project who has the right credentials.

To edit a field in a metadata form, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the **Discover** menu in the top navigation bar.
3. Choose **Metadata forms**.
4. Choose the name of the metadata form that contains the field that you want to edit. This takes you to the metadata form details page.
5. On the metadata form details page, choose the field that you want to edit.
6. Expand the **Actions** menu, and then choose **Edit field**.
7. Make your updates to the field name, description, type, and whether it is a required
   field. Make updates to other selections if more are available with the selected field type.
8. Choose **Save**.
