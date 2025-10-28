# Update the RStudio Package Manager URL

RStudio Package Manager is a repository management server used to organize and centralize
packages across your organization. For more information on RStudio Package Manager, see [RStudio Package Manager](https://www.rstudio.com/products/package-manager/ "https://www.rstudio.com/products/package-manager/"). If
you don't supply your own Package Manager URL, Amazon SageMaker AI domain uses the default Package Manager
repository when you onboard RStudio following the steps in [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md"). For more information, see [Host RStudio Connect and Package Manager for ML development in RStudio on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/host-rstudio-connect-and-package-manager-for-ml-development-in-rstudio-on-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/host-rstudio-connect-and-package-manager-for-ml-development-in-rstudio-on-amazon-sagemaker/").
The following procedure shows how to update the Package Manager URL.

**Update Package Manager URL**

You can update the Package Manager URL used for your RStudio-enabled domain as
follows.

1. Navigate to the **domains** page.
2. Select the desired domain.
3. Choose **domain Settings**.
4. Under **General Settings**, select **Edit**.
5. From the new page, select **RStudio Settings** on the left side.
6. Under **RStudio Package Manager**, enter your RStudio Package Manager
   URL.
7. Select **Submit**.

**CLI**

The only way to update your Package Manager URL from the AWS CLI is to delete your domain
and create a new one with the updated Package Manager URL.
