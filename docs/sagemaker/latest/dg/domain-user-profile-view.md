# View user profiles in a domain

The following section describes how to view a list of user profiles in a domain from
the SageMaker AI console or the AWS CLI.

## View user profiles from the console

Complete the following procedure to view a list of user profiles in the domain from
the SageMaker AI console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose
   **domains**.
4. From the list of domains, select the domain that you want to view a list of
   user profiles for.
5. On the **domain details** page, choose the **User
   profiles** tab.

## View user profiles from the AWS CLI

To view the user profiles in a domain from the AWS CLI, run the following command from
the terminal of your local machine.

```
aws sagemaker list-user-profiles \
--region `region` \
--domain-id `domain-id`
```
