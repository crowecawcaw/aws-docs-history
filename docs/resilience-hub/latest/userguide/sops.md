# Managing standard operating procedures

A standard operating procedure (SOP) is a prescriptive set of steps designed to efficiently recover your application in the event of an outage or alarm. Prepare,
test, and measure your SOPs in advance to ensure timely recovery in the event of an operational outage.

Based on your Application Components, AWS Resilience Hub recommends the SOPs you should prepare.
AWS Resilience Hub works with Systems Manager to automate the steps of your SOPs by providing a number of SSM
documents you can use as the basis for those SOPs.

For example, AWS Resilience Hub may recommend an SOP for adding disk space based on an existing SSM Automation document. To run this SSM document, you require a specific IAM role
with the correct permissions. AWS Resilience Hub creates metadata in your application indicating which SSM automation document to run in the case of disk shortage, and which IAM role is
required to run that SSM document. This metadata is then saved in an SSM parameter.

In addition to configuring the SSM automation, it is also best practice to test it with an
AWS FIS experiment. Therefore, AWS Resilience Hub also provides an AWS FIS experiment that calls the SSM
automation document - this way, you can proactively test your application to make sure the SOP
you've created does the intended job.

AWS Resilience Hub provides its recommendations in the form of an CloudFormation template you can add to your application code base. This template provides:

- The IAM role with the permissions required to run the SOP.
- An AWS FIS experiment you can use to test the SOP.
- An SSM parameter that contains application metadata indicating which SSM document and which
  IAM role is to be run as the SOP, and on which resource. For example: `$(DocumentName) for
 SOP $(HandleCrisisA) on $(ResourceA)`.
  Creating an SOP may require some trial and error. Running a resiliency assessment against
  your application and generating an CloudFormation template from the AWS Resilience Hub recommendations is a good
  start. Use the CloudFormation template to generate an CloudFormation stack, then use the SSM parameters and their
  default values in your SOP. Run the SOP and see what refinements you need to make.

Because all applications have differing requirements, the default list of SSM documents that
AWS Resilience Hub provides will not be sufficient for all of your needs. You can, however, copy the default
SSM documents and use them as a basis to create your own custom documents tailored for your
application. You can also create your own entirely new SSM documents. If you create your own SSM
documents instead of modifying the defaults, you must associate them with SSM parameters, so the
correct SSM document is called when the SOP runs.

When you've finalized your SOP by creating the necessary SSM documents and updating the
parameter and document associations as necessary, add the SSM documents directly to your code
base, and make any subsequent changes or customizations there. That way, every time you deploy
your application, you'll also deploy the most up-to-date SOP.

###### Topics

- [Building an SOP based on AWS Resilience Hub recommendations](building-sops.md "building-sops.md")
- [Creating a custom SSM document](create-custom-ssm-doc.md "create-custom-ssm-doc.md")
- [Using a custom SSM document instead of the default](using-different-ssm-doc.md "using-different-ssm-doc.md")
- [Testing SOPs](testing-sops.md "testing-sops.md")
- [Viewing standard operating procedures](view-sops.md "view-sops.md")
