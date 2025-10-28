# Edit a term in a glossary in Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, a business glossary is a collection of business terms that may be
associated with assets (data). For more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md"). To create, edit, or delete terms in a glossary in your
Amazon SageMaker Unified Studio domain, you must be a member of the owning project with the right permissions for
that domain.

In Amazon SageMaker Unified Studio, business glossary terms can have close descriptions. To set the context of
a particular term, you can specify relationships among terms. When you define a relationship
for a term, it is automatically added to the definition of the related term. The glossary term
relationships available in Amazon SageMaker Unified Studio include the following:

- **Is a Type of** - indicates that the current term is a type of the
  identified term. Indicates that the identified term is a parent to the current
  term.
- **Has Types** - indicates that the current term is a generic term for
  the indicated specific term or terms. This relationship can denote child terms for the
  generic term.
  To edit a term in a glossary, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the **Discover** menu in the top navigation bar.
3. Choose **Glossaries**.
4. Select the
   glossary that contains the term that you you want to edit.
5. Choose the name of the term to navigate to the term details page.
6. On the term details page, expand **Actions** and then choose
   **Edit** to edit the term.
7. Make your updates to the name and description, and then choose
   **Update term**.
