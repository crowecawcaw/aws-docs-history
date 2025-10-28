# Create a business glossary in

Amazon SageMaker Unified Studio

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
2. Navigate to the **Discover** menu in the top navigation bar.
3. Choose **Glossaries**, and then choose
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
   To disable or enable a business glossary, complete the following steps:

7. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
8. Navigate to the **Discover** menu in the top navigation bar.
9. Choose **Glossaries**.
10. Select the
    business glossary that you want to disable or enable.
11. On the glossary details page, locate the **Enabled** toggle
    and use it to enable or disable your selected glossary.

###### Note

Disabling a glossary also disables all the terms that it contains.
