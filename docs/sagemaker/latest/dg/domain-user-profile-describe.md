

# View user profile details
<a name="domain-user-profile-describe"></a>

The following section describes how to view the details of a user profile from the SageMaker AI console or the AWS CLI. 

## View user profile details from the console
<a name="domain-user-profile-describe-console"></a>

 Complete the following procedure to view the details of a user profile from the SageMaker AI console. 

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation pane, choose **Admin configurations**.

1. Under **Admin configurations**, choose **domains**. 

1.  From the list of domains, select the domain that you want to view a list of user profiles for. 

1. On the **domain details** page, choose the **User profiles** tab. 

1.  Select the user profile that you want to view details for. 

## View user profile details from the AWS CLI
<a name="domain-user-profile-describe-cli"></a>

To describe a user profile from the AWS CLI, run the following command from the terminal of your local machine.

```
aws sagemaker describe-user-profile \
--region {{region}} \
--domain-id {{domain-id}} \
--user-profile-name {{user-name}}
```