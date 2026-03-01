# Using the framework library to manage frameworks in AWS Audit Manager

You can find and manage frameworks in the framework library in AWS Audit Manager.

A framework determines which controls are tested in an environment over a period of time. It
defines the controls and their data source mappings for a given compliance standard or
regulation. It's also used to structure and automate Audit Manager assessments. You can use frameworks as
a starting point to audit your AWS service usage and start automating evidence
collection.

## Key points

In the framework library, frameworks are organized into the following categories.

- **Standard frameworks** are prebuilt frameworks that
  AWS provides. These frameworks are based on AWS best practices for different
  compliance standards and regulations, such as GDPR and HIPAA. Standard frameworks include
  controls that are organized into control sets based on the compliance standard or
  regulation that the framework supports.

You can view the contents of standard frameworks, but you can't edit or delete them.
However, you can make an editable copy of any standard framework to create a new one to
meet your specific requirements.

- **Custom frameworks** are frameworks that you create. You
  can create a custom framework from scratch, or by making an editable copy of an existing
  framework. You can use custom frameworks to organize controls into control sets in a way
  that meets your specific requirements.

You can create an assessment from a standard framework or a custom framework.

###### Note

AWS Audit Manager assists in collecting evidence that's relevant for verifying compliance with
specific compliance standards and regulations. However, it doesn't assess your compliance
itself. The evidence that's collected through AWS Audit Manager therefore might not include all the
information about your AWS usage that's needed for audits. AWS Audit Manager isn't a substitute for
legal counsel or compliance experts.

## Additional resources

To create and manage frameworks in Audit Manager, follow the procedures that are outlined
here.

- [Finding the available frameworks in AWS Audit Manager](access-frameworks.md "access-frameworks.md")
- [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md")
- [Creating a custom framework in AWS Audit Manager](custom-frameworks.md "custom-frameworks.md")
  - [Creating a custom framework from scratch in AWS Audit Manager](create-custom-frameworks-from-scratch.md "create-custom-frameworks-from-scratch.md")
  - [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md")

- [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md "edit-custom-frameworks.md")
- [Deleting a custom framework in AWS Audit Manager](delete-custom-framework.md "delete-custom-framework.md")
- [Sharing a custom framework in AWS Audit Manager](share-custom-framework.md "share-custom-framework.md")
  - [Framework sharing concepts and terminology](share-custom-framework-concepts-and-terminology.md "share-custom-framework-concepts-and-terminology.md")
  - [Sending request to share a custom framework in AWS Audit Manager](framework-sharing.md "framework-sharing.md")
  - [Responding to share requests in AWS Audit Manager](responding-to-shared-framework-requests.md "responding-to-shared-framework-requests.md")
  - [Deleting share requests in AWS Audit Manager](deleting-shared-framework-requests.md "deleting-shared-framework-requests.md")

- [Supported frameworks in AWS Audit Manager](framework-overviews.md "framework-overviews.md")
