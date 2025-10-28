# View domain environment details

This page gives information about modifications to the Amazon SageMaker AI domain environment. Complete
the following procedure to view the custom images, lifecycle configurations, and git
repositories attached to a domain environment.

**Open the Environment page**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the list of domains, select a domain to open the
   **Environment** page.
5. On the **domain details** page, choose the
   **Environment** tab.
   For more information about bringing a custom Amazon SageMaker Studio Classic image, see [Bring your own
   SageMaker image](studio-byoi.md "studio-byoi.md").

For more information about bringing a custom
RStudio
image, see [Bring
your own image to RStudio on SageMaker](rstudio-byoi.md "rstudio-byoi.md").

For instructions on using a lifecycle configuration with Studio Classic, see [Use Lifecycle
Configurations with Amazon SageMaker Studio](studio-lcc.md "studio-lcc.md").

For information about attaching a git repository to a domain, see [Attach Suggested Git
Repos to SageMaker AI](studio-git-attach.md "studio-git-attach.md").

These can also be attached to a shared space using the AWS CLI by passing values to the [create-space](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-space.html") command using the `space-settings` parameter.
