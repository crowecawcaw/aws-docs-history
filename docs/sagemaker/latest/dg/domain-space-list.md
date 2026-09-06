

# Get information about shared spaces
<a name="domain-space-list"></a>

**Note**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).  
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

 This guide shows how to access a list of shared spaces in an Amazon SageMaker AI domain with the Amazon SageMaker AI console, Amazon SageMaker Studio, or the AWS CLI. It also shows how to view details of a shared space from the AWS CLI. 

**Topics**
+ [List shared spaces](#domain-space-list-spaces)
+ [View shared space details](#domain-space-describe)

## List shared spaces
<a name="domain-space-list-spaces"></a>

 The following topic describes how to view a list of shared spaces within a domain from the SageMaker AI console or the AWS CLI. 

### List shared spaces from Studio
<a name="domain-space-list-updated"></a>

 Complete the following procedure to view a list of the shared spaces in a domain from Studio.

1. Navigate to Studio following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. From the Studio UI, find the applications pane on the left side.

1. From the applications pane, select **Studio Classic** or **JupyterLab**. You can view the spaces that are being used to run the application type.

### List shared spaces from the console
<a name="domain-space-list-console"></a>

 Complete the following procedure to view a list of the shared spaces in a domain from the SageMaker AI console. 

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **domains**. 

1.  From the list of domains, select the domain that you want to view the list of shared spaces for. 

1.  On the **domain details** page, choose the **Space management** tab. 

### List shared spaces from the AWS CLI
<a name="domain-space-list-cli"></a>

 To list the shared spaces in a domain from the AWS CLI, run the following command from the terminal of your local machine.

```
aws --region {{region}} \
sagemaker list-spaces \
--domain-id {{domain-id}}
```

## View shared space details
<a name="domain-space-describe"></a>

 The following section describes how to view shared space details from the SageMaker AI console, Studio, or the AWS CLI. 

### View shared spaces details from Studio
<a name="domain-space-describe-updated"></a>

 Complete the following procedure to view the details of a shared spaces in a domain from Studio.

1. Navigate to Studio following the steps in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. From the Studio UI, find the applications pane on the left side.

1. From the applications pane, select **Studio Classic** or **JupyterLab**. You can view the spaces that are running the application.

1. Select the name of the space that you want to view more details for.

### View shared space details from the console
<a name="domain-space-describe-console"></a>

 You can view the details of a shared space from the SageMaker AI console using the following procedure. 

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **domains**. 

1.  From the list of domains, select the domain that you want to view the list of shared spaces for. 

1.  On the **domain details** page, choose the **Space management** tab. 

1.  Select the name of the space to open a new page that lists details about the shared space. 

### View shared space details from the AWS CLI
<a name="domain-space-describe-cli"></a>

To view the details of a shared space from the AWS CLI, run the following command from the terminal of your local machine.

```
aws --region {{region}} \
sagemaker describe-space \
--domain-id {{domain-id}} \
--space-name {{space-name}}
```