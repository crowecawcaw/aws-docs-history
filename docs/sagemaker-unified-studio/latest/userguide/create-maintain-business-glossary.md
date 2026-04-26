# Create a business glossary in Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, a business glossary is a collection of business terms (words) that may be
associated with assets (data). It provides appropriate vocabularies with a list of business
terms and their definitions for business users to ensure the same definitions are used across
the organization when analyzing data. Business glossaries are created in the catalog domain
and can be applied to assets and columns to help understand key characteristics of that asset
or column. One or more glossary terms can be applied. A business glossary can be a flat list
of terms where any term in the business glossary can be associated with a sublist of other
terms. For more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md"). To create, edit, or delete a glossary in your
Amazon SageMaker Unified Studio domain, you must be a member of the owning project with the right permissions for
that domain.

To create a glossary, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. In the left navigation pane, choose **Catalog**.
3. Choose **View business glossaries**, and then choose
   **Create glossary**.
4. Specify a name, description, and owning project for the glossary and then
   choose **Create glossary**.
5. Optional - if you want to create a [restricted glossary](restricted-asset-classification.md "restricted-asset-classification.md"), then choose **Restrict this glossary for governed
   term use**. And then specify the usage permission by selecting one of the
   following options:
   - All projects - give permissions to all projects in this domain
   - (Default) Owning project - give permissions ONLY to the owning project
   - Selected projects or domain units - give permission to specific projects and/or
     domain units

6. Enable the new glossary by choosing the **Enabled** toggle.

###### Note

After you create and enable a glossary, it is visible to all users in the
domain. Users in other projects can search for, view, and attach the glossary's terms
to their assets. Only members of the project that owns the glossary can edit or
delete it.
To disable or enable a business glossary, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. In the left navigation pane, choose **Catalog**.
3. Choose **View business glossaries**.
4. Select the
   business glossary that you want to disable or enable.
5. On the glossary details page, locate the **Enabled** toggle
   and use it to enable or disable your selected glossary.

###### Note

Disabling a glossary also disables all the terms that it contains.
