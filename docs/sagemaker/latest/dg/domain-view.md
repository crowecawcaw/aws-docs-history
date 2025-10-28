# View domains

The following section shows how to view a list of your domains, and details of an
individual domain from the SageMaker AI console or the AWS CLI.

## Console

The console's domain overview page gives information about the structure of a
domain, and it provides a list of your domains. The page's domain structure
diagram describes domain components and how they interact with each other.

The following procedure shows how to view a list of your domains from the SageMaker AI
console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose
   **domains**.

To view the details of the domain, complete the following procedure. This page gives
information about the general settings for the domain, including the name, domain ID,
execution role used to create the domain, and the authentication method of the
domain. 

1. From the list of domains, select the domain for which you want to open the
   **domain settings** page.
2. On the **domain details** page, choose the **domain
   settings** tab.

## AWS CLI

Run the following command from the terminal of your local machine to view a list of
domains from the AWS CLI.

```
aws sagemaker list-domains --region `region`
```
