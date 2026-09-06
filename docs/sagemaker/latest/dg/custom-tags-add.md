

# Add custom tags to resources
<a name="custom-tags-add"></a>

 The following page demonstrates the steps needed to use custom tag propagation. Custom tag propagation requires the following steps: 
+  Opt-in to custom tag propagation 
+  Add custom tags to resources 

 When you activate custom tag propagation in an existing domain, tag propagation does not work for existing applications until the application is restarted. Similarly, tags are not updated on an existing resource when new custom tags are added. For example, assume a domain has two tags and a user creates a resource in that domain. The resource then has two tags. If a new tag is added to the domain, then that new tag is not added to the existing resource. However, any new resource created will have the new tag attached to the resource.

## Prerequisites
<a name="custom-tags-add-prereq"></a>
+  Users must have the `sagemaker:AddTags` permission for any resource creation. 
  +  For new domains created with the `SageMakerFullAccess` managed policy or using the SageMaker Role Manager, the `sagemaker:AddTags` permission is pre-populated. 
  +  For existing domains using custom AWS Identity and Access Management policies, you must update the policies to include the `sagemaker:AddTags` permission to allow users to create resources.

## Opt-in to custom tag propagation
<a name="custom-tags-add-opt-in"></a>

The process to opt-in to custom tag propagation differs based on if you are opting-in from the console or from the AWS CLI. From the console, you can only opt-in to custom tag propagation by updating an existing domain. From the AWS CLI, you can opt-in to custom tag propagation when creating a domain or updating an existing domain.



### Opt-in from the console
<a name="custom-tags-add-opt-in-console"></a>

The following steps outline how to opt-in to custom tag propagation from the console. You can only opt-in to custom tag propagation from the console by updating an existing domain.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation, select **Admin configurations**. Under **Admin configurations**, select **Domains**.

1. On the **Domains** page, select the domain that you want to activate custom tag propagation for.

1. From the **Domain details** page, select the **Domain settings** tab.

1. On the **Domain settings** tab, navigate to **Custom Tag Propagation**.

1. Select **Edit**.

1. From the **Edit custom tag propagation** page, select **Automatically propagate custom tags**

1. Select **Submit**.

### Opt-in using the AWS CLI
<a name="custom-tags-add-opt-in-cli"></a>

 To opt-in to custom tag propagation using the AWS CLI, use the `TagPropagation` attribute in the [CreateDomain](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateDomain.html) and [UpdateDomain](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateDomain.html) APIs. By default, the value of this field is `DISABLED`. An empty value also defaults to `DISABLED`. The following example shows how to activate custom tag propagation. 

```
aws sagemaker update-domain \
--domain-id {{domain-id}} \
--region {{region}} \
--tag-propagation ENABLED
```

## Add custom tags
<a name="custom-tags-add-tags"></a>

The process to add custom tags propagation differs based on if you are adding them from the console or from the AWS CLI.

### Add from the console
<a name="custom-tags-add-tags-console"></a>

The following steps outline how to add custom tags to a domain from the console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation, select **Admin configurations**. Under **Admin configurations**, select **Domains**.

1. On the **Domains** page, select the domain that you want to add custom tags to.

1. From the **Domain details** page, select the **Domain settings** tab.

1. On the **Domain settings** tab, navigate to **Tags**.

1. Select **Edit**.

1. From the **Tags** page, select **Add tag**. Add a key and value pair for the custom tag.

1. Select **Save**. This custom tag is now propagated to the SageMaker AI resources created in the domain.

The following steps outline how to add custom tags to a user profile from the console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the left navigation, select **Admin configurations**. Under **Admin configurations**, select **Domains**.

1. On the **Domains** page, select the domain containing the user profile that you want to add custom tags to.

1. From the **Domain details** page, select the **User profiles** tab.

1. On the **User profiles** tab, select the user profile you want to add custom tags to.

1. On the **User Details** tab, navigate to the **Details** section.

1. Select **Edit**.

1. From the **Tags** section, select **Add tag**. Add a key and value pair for the custom tag.

1. Select **Submit**. This custom tag is now propagated to the SageMaker AI resources created in the domain.

### Add using the AWS CLI
<a name="custom-tags-add-tags-cli"></a>

 After you have activated custom tag propagation, you can add custom tags using the AWS CLI at the domain, user profile, or space level during creation or update. The method to add custom tags differs depending on you are creating a new resource or adding tags to an existing resource.

 The following example shows how to add custom tags at the domain level during creation. 

```
aws sagemaker create-domain \
    --domain-name {{domain-id}} \
    --auth-mode IAM \
    --default-user-settings '{"ExecutionRole": "{{execution-role}}"}' \
    --subnet-ids {{subnet-id}} \
    --vpc-id {{vpc-id}} \
    --tags Key={{key}},Value={{value}} \
    --tag-propagation ENABLED
```

 You must use the [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) API to add custom tags for existing domain, user profile, and spaces as follows. 

```
aws sagemaker add-tags \
--resource-arn {{resource-arn-to-attach-tags}} \
--tags Key={{key}}, Value={{value}}
```