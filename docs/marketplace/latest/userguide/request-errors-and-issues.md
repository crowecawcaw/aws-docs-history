# Troubleshooting common errors for change

requests on AWS Marketplace

When you make changes to your product's information on AWS Marketplace, you might run into
errors. This topic explains some common errors and provides suggestions for how to fix
them.

- Scanning your AMI – Several issues could
  happen when scanning your AMI:

      + You have not granted AWS Marketplace permissions to scan your AMI. Grant AWS Marketplace
       permissions to access it. Or you have granted permissions, but the
       permissions boundary is too restrictive. For more information, see [Giving AWS Marketplace access to your
       AMI](single-ami-marketplace-ami-access.md "single-ami-marketplace-ami-access.md").
      + If scanning finds security issues or Common Vulnerabilities and Exposures
       (CVEs) in your AMI, make sure you're using the latest patches for the
       operating system in your image. For more information, see [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md "product-and-ami-policies.md").

  For general guidelines about building an AMI, see [Best practices for building AMIs for use with AWS Marketplace](best-practices-for-building-your-amis.md "best-practices-for-building-your-amis.md").

- AWS Marketplace Management Portal fields – Some fields in the
  AWS Marketplace Management Portal require very specific information:

      + If you are unsure about what the field is requesting, try checking the
       details in the console. Most fields have text descriptions above the field,
       and formatting requirements below the field.
      + If you try to submit a form with one or more invalid fields, a list of
       issues is shown. A recommended action is provided to help you fix the
       issue.
      + If you're asked to provide an ARN, you will typically find it elsewhere
       in the console. For example, the ARN for the IAM role that you created to
       give AWS Marketplace access to your AMI is found on the [Roles page](https://console.aws.amazon.com/iam/home?region=us-east-1#/roles "https://console.aws.amazon.com/iam/home?region=us-east-1#/roles") in the IAM console. ARNs all have a similar format.
       For example, an IAM role ARN is in the form
       *arn:aws:iam::123456789012:role/exampleRole*.
      + Your logos and videos must be provided as a URL directly to the content.
       For more information about logo formats, see [Company and product logo requirements](product-submission.md#seller-and-product-logos "product-submission.md#seller-and-product-logos").

  For more information about submitting products and version change requests, see
  [Submitting your product for publication on AWS Marketplace](product-submission.md "product-submission.md").

- Product Load Form (PLF) issues – PLFs
  contain instructions that are included in the spreadsheet. Overall instructions are
  provided in the Instructions table. Each field has instructions for how to fill it
  out—select the field to reveal the instructions.
- Request in Progress – Some requests can't
  happen in parallel. You can only have one request to update specific information in
  progress for a product at a time. You can see all of your requests still under
  review on the **Requests** tab of the **Server
  products** page in AWS Marketplace Management Portal. If you have a pending request that you
  did not intend, you can cancel it and then submit a new request with the change that
  you want to make.
  - You can't update version information when an update (to add or restrict) a
    version is ongoing.
  - If there is a request pending from the AWS Marketplace Seller Operations team, you can't submit any
    new changes.

- Unexplained error – If your submission fails
  with no explanation, try again. Occasionally, server load causes a submission to
  fail.
  If you're still having problems with a change request, contact the [AWS Marketplace Seller Operations](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/")
  team.
