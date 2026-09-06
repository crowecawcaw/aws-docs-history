

# Attach a Git Repository from the SageMaker AI Console for Amazon SageMaker Studio Classic
<a name="studio-git-attach-console"></a>

**Note**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).  
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

The following topic shows how to associate a Git repository URL from the Amazon SageMaker AI console to clone it in your Studio Classic environment. After you associate the Git repository URL, you can clone it by following the steps in [Clone a Git Repository in Amazon SageMaker Studio Classic](studio-tasks-git.md).

## Prerequisites
<a name="studio-git-attach-console-prerequisites"></a>

Before you can begin this tutorial, you must onboard to Amazon SageMaker AI domain. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).

## Attach the Git repo to a domain or user profile
<a name="studio-git-attach-console-attach"></a>

Git repo URLs associated at the domain level are inherited by all users. However, Git repo URL that are associated at the user profile level are scoped to a specific user. 

The following sections show how to attach a Git repo URL to a domain and user profile.

### Attach to a domain
<a name="studio-git-attach-console-attach-domain"></a>

**To attach a Git repo URL to an existing domain**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **domains**. 

1. Select the domain to attach the Git repo to.

1. On the **domain details** page, choose the **Environment** tab.

1. On the **Suggested code repositories for the domain** tab, choose **Attach**.

1. Under **Source**, enter the Git repository URL.

1. Select **Attach to domain**.

### Attach to a user profile
<a name="studio-git-attach-console-attach-userprofile"></a>

The following shows how to attach a Git repository URL to an existing user profile.

**To attach a Git repository URL to a user profile**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **domains**. 

1. Select the domain that includes the user profile to attach the Git repo to.

1. On the **domain details** page, choose the **User profiles** tab.

1. Select the user profile to attach the Git repo URL to.

1. On the **User details** page, choose **Edit**.

1. On the **Studio settings** page, choose **Attach** from the **Suggested code repositories for the user** section.

1. Under **Source**, enter the Git repository URL.

1. Choose **Attach to user**.