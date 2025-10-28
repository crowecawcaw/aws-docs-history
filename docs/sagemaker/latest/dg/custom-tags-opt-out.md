# Opt-out of custom tag propagation

The process to opt-out of custom tag propagation differs based on if you are opting-out from
the console or from the AWS CLI.

## Opt-out from the console

The following steps outline how to opt-out of custom tag propagation from the console. You
can only opt-out of custom tag propagation from the console by updating an existing
domain.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation, select **Admin configurations**. Under
   **Admin configurations**, select **Domains**.
3. On the **Domains** page, select the domain that you want to opt-out
   of custom tag propagation for.
4. From the **Domain details** page, select the **Domain
   settings** tab.
5. On the **Domain settings** tab, navigate to **Custom Tag
   Propagation**.
6. Select **Edit**.
7. From the **Edit custom tag propagation** page, select
   **Automatically propagate custom tags**
8. Select **Submit**.

## Opt-out using the AWS CLI

To opt-out of custom tag propagation, set the
`TagPropagation` attribute in the [CreateDomain](../APIReference/API_CreateDomain.md "../APIReference/API_CreateDomain.md") and [UpdateDomain](../APIReference/API_UpdateDomain.md "../APIReference/API_UpdateDomain.md") APIs to `DISABLED` as shown in the following example. By
default, the value of this field is `DISABLED`. An empty value also defaults
to `DISABLED`. 

###### Note

Tag propagation is not automatically turned off for existing applications when
`TagPropagation` is set to `DISABLED`. Applications must be restarted
for opt-out to take effect for existing apps.

```
aws sagemaker update-domain \
--domain-id `domain-id` \
--region `region` \
--tag-propagation DISABLED
```
