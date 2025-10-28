# Using a custom SSM document instead of the default

To replace the SSM document AWS Resilience Hub suggested for your SOP with a custom document you've
created, work directly in your code base. In addition to adding your new custom SSM automation
document, you'll also:

1. Add the IAM permissions required to run the automation.
2. Add an AWS FIS experiment to test your SSM document.
3. Add an SSM parameter that points to the automation document you want to use as the SOP.
   Generally, it's most efficient to work with the suggested default values in AWS Resilience Hub and
   customize them as necessary. For example, add or remove permissions as necessary for the IAM
   role, change the AWS FIS experiment setup to point to the new SSM document, or change the SSM
   parameter to point to your new SSM document.
