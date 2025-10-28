# Creating an initial SaaS product page on AWS Marketplace

You can use your software as a service (SaaS) application metadata to create an initial
SaaS product page in the AWS Marketplace catalog, using the AWS Marketplace Management Portal. You can then also add product
information, product deployment details, and public offer details. Optionally, you
can add accounts to the allowlist to test the
product. For more information see the following procedure.

###### To create an initial SaaS product page

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/homepage "https://aws.amazon.com/marketplace/management/homepage").
2. Choose **Create SaaS product**, and then choose **SaaS
   product**.
3. Generate a SaaS product ID and code. You can also add optional tags to support
   tag-based authorization.

###### Note

For information about tag-based authorization, see [Controlling access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources") in the
_AWS Identity and Access Management User Guide_. 4. Use the self-service experience to create the AWS Marketplace listing. Add product
information, product deployment details, and public offer details. Optionally, you
can also add accounts to the allowlist to test the product.

###### Note

If you need to end your session before finishing the steps, choose the
**Save and exit** option to save your current selections to
the staging area. This option creates a request to validate the information that
you provided. While your request is being validated, you can't edit the product.
If your request is successful, you can continue creating your product by
choosing **Resume product creation**.

If your request isn't successful, it's because of a validation error, which is
visible on the product request log. Select the request to view the error, and
choose **Copy to new** under **Actions** to
correct the error and resubmit the request. To update previous steps, open the
product detail page and submit a change request.

###### Note

Your price will default to $0.001 per dimension during testing. This price
allows you to test your product in the **Limited** state
without incurring a large bill. You'll provide your actual price when making
your product public. 5. Choose **Submit**. Then, AWS Marketplace validates the information. If the
validation succeeds, AWS Marketplace releases the product in a **Limited**
status. After the validation succeeds, you can preview, integrate, and test your
product.

###### Note

While the validation is in progress, you can't edit the product. When your
product is initially published, it's only accessible for the AWS account used
to create the product and the AWS Marketplace Seller Operations team's test account. If
you view the product from the **SaaS products** page, you can
choose **View on AWS Marketplace** to view the product details as they
will appear in AWS Marketplace for buyers. This detail listing isn't visible to other
AWS Marketplace users.
