# View your Studio running instances,

applications, and spaces

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the updated Studio
experience. For information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

The following topics include information and instructions about how to view your
Studio running instances, applications, and spaces. For more information about
Studio spaces, see [Amazon SageMaker Studio spaces](studio-updated-spaces.md "studio-updated-spaces.md").

## View your Studio running

instances and applications

The **Running instances** page gives information about all running
application instances that were created in Amazon SageMaker Studio by the user, or were shared
with the user.

You can view and stop running instances for all of your applications and spaces. If an
instance is stopped, it does not appear on this page. Stopped instances can be viewed
from the landing page for their respective application types.

You can view a list of running applications and their details in Studio.

###### To view running instances

1. Launch Studio following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. On the left navigation pane, choose **Running instances**.
3. From the **Running instances** page, you can view a list of
   running applications and details about those applications.

To view non-running instances, from the left navigation pane choose, the
relevant application under **Applications**. The non-running
applications will have the **Stopped** status under the
**Status** column.

## View your Studio spaces

The **Spaces** section within your **Domain
details** page gives information about Studio spaces within your
domain. You can view, create, and delete spaces on this page.

The spaces that you can view in the **Spaces** section are running
spaces for the following:

- JupyterLab private space. For information about JupyterLab, see [SageMaker JupyterLab](studio-updated-jl.md "studio-updated-jl.md").
- Code Editor private space. For information about Code Editor, based on Code-OSS, Visual Studio Code - Open Source, see [Code Editor in Amazon SageMaker Studio](code-editor.md "code-editor.md").
- Studio Classic shared space. For information about Studio Classic shared space, see
  [Collaboration with shared spaces](domain-space.md "domain-space.md").

There are no spaces for SageMaker Canvas, Studio Classic (private), or RStudio.

###### View your Studio spaces in a domain

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. From the left navigation pane, expand **Admin
   configurations** and choose **Domains**.
3. Choose the domain where you want to view the spaces.
4. On the **Domain details** page, choose the **Space
   management** tab to open the **Spaces**
   section.

**View your Studio spaces using the AWS CLI**

Use the following command to list all spaces in your domain:

```
aws sagemaker list-spaces --region `us-east-1` --domain-id `domain-id`
```

- `us-east-1` is your
  AWS Region.
- `domain-id` is your domain ID. See [View domains](domain-view.md "domain-view.md") for more
  information.
