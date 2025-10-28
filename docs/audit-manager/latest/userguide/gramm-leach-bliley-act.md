# Gramm-Leach-Bliley Act

AWS Audit Manager provides a prebuilt framework that supports the Gramm-Leach-Bliley Act
(GLBA).

###### Topics

- [What is the GLBA?](#what-is-the-gramm-leach-bliley-act "#what-is-the-gramm-leach-bliley-act")
- [Using this framework](#framework-gramm-leach-bliley-act "#framework-gramm-leach-bliley-act")
- [Next steps](#next-steps-glba "#next-steps-glba")

## What is the GLBA?

The GLBA (or the GLB Act), also known as the Financial Service Modernization Act of
1999, is a federal law enacted in the United States to control the ways that financial
institutions deal with the private information of individuals. The Act consists of three
sections. The first is the Financial Privacy Rule, which regulates the collection and
disclosure of private financial information. The second is the Safeguards Rule, which
stipulates that financial institutions must implement security programs to protect such
information. The third is the Pretexting provisions, which prohibit the practice of
pretexting (accessing private information using false pretenses). The Act also requires
financial institutions to give customers written privacy notices that explain their
information-sharing practices.

## Using this framework

You can use the GLBA 2016 framework to help you prepare for audits. This framework
includes a prebuilt collection of controls with descriptions and testing procedures. These
controls are grouped into control sets according to GLBA requirements. You can also
customize this framework and its controls to support internal audits with specific
requirements.

Using the GLBA framework as a starting point, you can create an Audit Manager assessment and
start collecting evidence that’s relevant for a GLBA audit. In your assessment, you can
specify the AWS accounts that you want to include in the scope of your audit. After you
create an assessment, Audit Manager starts to assess your AWS resources. It does this based on
the controls that are defined in the GLBA framework. When it's time for an audit,
you—or a delegate of your choice—can review the evidence that Audit Manager
collected. Either, you can browse the evidence folders in your assessment and choose which
evidence you want to include in your assessment report. Or, if you enabled evidence
finder, you can search for specific evidence and export it in CSV format, or create an
assessment report from your search results. Either way, you can use this assessment report
to show that your controls are working as intended.

The framework details are as follows:

| Framework name in AWS Audit Manager | Number of automated controls | Number of manual controls | Number of control sets |
| ----------------------------------- | ---------------------------- | ------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gramm-Leach-Bliley Act (GLBA)       | 0                            | 120                       | 16                     | The controls in this AWS Audit Manager framework aren't intended to verify if your systems are compliant with the GLBA standard. Moreover, they can't guarantee that you'll pass a GLBA audit. AWS Audit Manager doesn't automatically check procedural controls that require manual evidence collection. ## Next steps For instructions on how to view detailed information about this framework, including the list of standard controls that it contains, see [Reviewing a framework in AWS Audit Manager](review-frameworks.md "review-frameworks.md"). For instructions on how to create an assessment using this framework, see [Creating an assessment in AWS Audit Manager](create-assessments.md "create-assessments.md"). For instructions on how to customize this framework to support your specific requirements, see [Making an editable copy of an existing framework in AWS Audit Manager](create-custom-frameworks-from-existing.md "create-custom-frameworks-from-existing.md"). |
