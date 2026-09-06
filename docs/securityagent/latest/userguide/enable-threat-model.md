

# Enable threat modeling
<a name="enable-threat-model"></a>

Configure your Agent Space to enable threat modeling by connecting source code repositories and configuring AWS resources. Threat modeling analyzes your application’s architecture and identifies security threats from source code, design documents, or both.

Setting up threat modeling configurations is an Agent Space-wide operation. The integrations and S3 buckets you connect are shared across capabilities, including threat modeling, code review, and penetration testing.

After completing setup, users can create and run threat models in the AWS Security Agent web application.

**Note**  
If you already have repositories or S3 buckets connected to your Agent Space (for example, through code review or penetration testing setup), threat modeling may already be enabled. You can go directly to the web application to create a threat model. See [Create a threat model](perform-threat-model.md).

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, ensure you have:
+ An Agent Space created in the AWS Management Console (see [Create an Agent Space](create-agent-space.md))
+ Permissions to configure integrations for your Agent Space
+ (Optional) A GitHub, GitLab, or Bitbucket organization with the AWS Security Agent app installed (see [Connect AWS Security Agent to GitHub repositories](connect-github.md), [Connect AWS Security Agent to GitLab repositories](connect-gitlab.md), or [Connect AWS Security Agent to Bitbucket repositories](connect-bitbucket.md))

## Access the threat modeling setup wizard
<a name="_access_the_threat_modeling_setup_wizard"></a>

Navigate to the threat modeling configuration for your Agent Space.

1. In the AWS Security Agent console, select your Agent Space.

1. Choose **Configure threat model** from the **Threat model** card, or from the **Threat model** tab.

You are directed to the **Configure threat model** wizard, which has two optional steps.

## Step 1: Connect source code repositories (optional)
<a name="_step_1_connect_source_code_repositories_optional"></a>

Connect the GitHub, GitLab, or Bitbucket repositories you want to enable threat modeling for. Threat models themselves are created and viewed in the web application.

**Important**  
Integrations configured here are shared across your Agent Space. Changes apply to threat modeling, code review, and penetration testing capabilities.

### Connect repositories
<a name="_connect_repositories"></a>

1. In the **Connected integrations** section, choose **Add**.

1. Select the registration that contains the repositories you want to use.

1. Select the checkbox for each repository you want to connect.

1. Choose **Save** to apply your selections.

**Note**  
If you haven’t registered an integration yet, choose **Settings** to navigate to the Integrations page where you can authorize the AWS Security Agent app. For more information, see [Connect AWS Security Agent to GitHub repositories](connect-github.md), [Connect AWS Security Agent to GitLab repositories](connect-gitlab.md), or [Connect AWS Security Agent to Bitbucket repositories](connect-bitbucket.md).

1. Choose **Next** to proceed to optional configurations.

## Step 2: Optional configurations
<a name="_step_2_optional_configurations"></a>

Configure S3 buckets, CloudWatch logging, and service access settings for your threat modeling environment. These settings are shared with other capabilities on your Agent Space.

### S3 buckets (optional)
<a name="_s3_buckets_optional"></a>

Add S3 buckets containing source code you want the agent to use as context during threat modeling.

1. In the **S3 buckets** section, choose **Add S3 resource**.

1. Enter the S3 URI for the bucket or prefix.

1. Choose **Add**.

**Note**  
You can add up to 10 S3 resources.

### CloudWatch logs (optional)
<a name="_cloudwatch_logs_optional"></a>

Configure CloudWatch log groups to capture and analyze application behavior during threat model runs.

1. In the **CloudWatch logs** section, select one or more existing CloudWatch log groups from your AWS account.

### Service access
<a name="_service_access"></a>

Configure the IAM service role that AWS Security Agent uses to access your AWS resources such as S3 buckets and CloudWatch logs for threat modeling. A service role is required to enable threat modeling.

1. In the **Service access** section, select an existing IAM service role from the dropdown, or leave it empty to have a service role automatically created.

**Note**  
A service role will be automatically created if you don’t select an existing role.

1. Choose **Save** to complete the configuration.

## After setup
<a name="_after_setup"></a>

After completing the threat modeling configuration:
+ The **Threat model** card on your Agent Space page shows a **Ready** status.
+ Users can launch the web application and create threat models from connected source code, uploaded scope docs, Confluence pages, or a combination of these inputs.

## Next steps
<a name="_next_steps"></a>

After enabling threat modeling:
+ Launch the web application to create and run threat models (see [Create a threat model](perform-threat-model.md))
+ Connect additional repositories or S3 buckets as your codebase grows
+ Connect Confluence to enable selecting pages as scope documents (see [Connect AWS Security Agent to Confluence](connect-confluence.md))