# Create a term in a glossary in Amazon DataZone

In Amazon DataZone, a business glossary is a collection of business terms that may be
associated with assets (data). For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md"). To create, edit, or delete terms in a glossary in your
Amazon DataZone domain, you must be the member of the owning project with the right permissions for
that domain.

In Amazon DataZone, business glossary terms can have close descriptions. To set the context of
a particular term, you can specify relationships among terms. When you define a relationship
for a term, it is automatically added to the definition of the related term. The glossary term
relationships available in Amazon DataZone include the following:

- **Is a Type of** - indicates that the current term is a type of the
  identified term. Indicates that the identified term is a parent to the current
  term.
- **Has Types** - indicates that the current term is a generic term for
  the indicated specific term or terms. This relationship can denote child terms for the
  generic term.
  To create a new term, complete the following steps:

1. Navigate to the Amazon DataZone data portal using the data portal URL and log in using your
   SSO or AWS credentials. If you’re an Amazon DataZone administrator, you can obtain the data
   portal URL by accessing the Amazon DataZone console at https://console.aws.amazon.com/datazone
   in the AWS account where the Amazon DataZone domain was created.
2. Navigate to the **Catalog** menu in the top navigation bar next to
   **Search**.
3. In the Amazon DataZone Data Portal, choose **Glossaries**, and then choose
   the glossary where you want to create the new term.
4. Specify a name, description, owner for the term and then choose
   **Create term**.
5. Enable the new term by choosing the **Enabled** toggle.
6. To add **Readme**, navigate to the term details page, and then you
   can choose **Create readme** to add some additional information about
   this glossary.
7. To add relationships, navigate to the term details page, choose **Term
   Relationships** section, and then choose **Add Glossary
   Terms**. In the dialog, choose the relationship and the terms you want to
   relate, and then choose **Close** to add a term to the appropriate
   relationship type. This relationship is also added to all the terms you made
   related.
