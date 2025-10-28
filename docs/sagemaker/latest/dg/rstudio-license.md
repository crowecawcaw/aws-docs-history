# Get an RStudio license

RStudio on Amazon SageMaker AI is a paid product and requires that each user is appropriately licensed.
Licenses for RStudio on Amazon SageMaker AI may be obtained from RStudio PBC directly, or by purchasing a
subscription to Posit Workbench on AWS Marketplace. For existing customers of Posit Workbench
Enterprise, licenses are issued at no additional cost. To use an RStudio license with Amazon SageMaker AI,
you must first have a valid RStudio license registered with AWS License Manager.

For licenses purchased directly through Rstudio PBC, a licenses grant for your AWS Account
must be created. Contact RStudio for direct license purchases or to enable existing licenses in
AWS License Manager. For more information about registering a license with
AWS License Manager, see [Seller issued licenses in AWS License Manager](../../../license-manager/latest/userguide/seller-issued-licenses.md "../../../license-manager/latest/userguide/seller-issued-licenses.md").

The following topics show how to acquire and validate a license granted by RStudio
PBC.

**Get an RStudio license**

1.  If you don't have an RStudio license, you may purchase one from the AWS Marketplace or from RStudio PBC directly.

        * To purchase a subscription from the AWS Marketplace, complete the steps to [subscribe with a SaaS contract](../../../marketplace/latest/buyerguide/buyer-saas-products.md "../../../marketplace/latest/buyerguide/buyer-saas-products.md") by searching for **Posit Platform
         (RStudio on SageMaker)**. To fulfill the license, you will be redirected to
         an external form outside the AWS Marketplace. You must provide additional information,
         including your company name and email address. If you can’t access that form to provide
         a company name and a contact email, create a ticket with Posit Support at [https://support.posit.co/hc/en-us/requests/new](https://support.posit.co/hc/en-us/requests/new "https://support.posit.co/hc/en-us/requests/new") with details about your
         purchase.
        * To purchase from RStudio PBC directly, navigate to [RStudio Pricing](https://www.rstudio.com/pricing/ "https://www.rstudio.com/pricing/") or contact [sales@rstudio.com](mailto:sales@rstudio.com "mailto:sales@rstudio.com"). When buying or updating an
         RStudio license, you must provide the AWS Account that will host your Amazon SageMaker AI domain.

    If you have an existing RStudio license, contact your RStudio Sales representative or
    [sales@rstudio.com](mailto:sales@rstudio.com "mailto:sales@rstudio.com") to add RStudio on Amazon SageMaker AI
    to your existing Posit Workbench Enterprise license, or to convert your Posit Workbench
    Standard license. The RStudio Sales representative will send you the appropriate electronic
    order form.

2.  RStudio grants a Posit Workbench license to your AWS Account through
    AWS License Manager in the US East (N. Virginia) Region. Although the RStudio
    license is granted in the US East (N. Virginia) Region, your license can be consumed in any
    AWS Region that RStudio on Amazon SageMaker AI is supported in. You can expect the license grant
    process to complete within three business days after you share your AWS account ID with
    RStudio.
3.  When this license is granted, you receive an email from
    your RStudio Sales representative with instructions to accept your license grant.

**Validate your RStudio license to be used with Amazon SageMaker AI**

1. Log into the AWS License Manager console in the same region as your
   Amazon SageMaker AI domain. If you are using AWS License Manager for the first time,
   AWS License Manager prompts you to grant permission to use
   AWS License Manager.
2. Select **Start using AWS License manager**.
3. Select `I grant AWS License Manager the required permissions` and select
   **Grant Permissions**.
4. Navigate to **Granted Licenses** on the left panel.
5. Select the license grant with `RSW-SageMaker` as the `Product name` and select **View**.
6. From the license detail page, select **Accept & activate license**.

**RStudio administrative dashboard**

You can use the RStudio administrative dashboard to see the number of users on the license
following the steps in [Use the RStudio administrative dashboard](rstudio-admin.md "rstudio-admin.md").
