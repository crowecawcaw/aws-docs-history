

# Actions, resources, and condition keys for Amazon FreeRTOS
<a name="list_freertos"></a>

Amazon FreeRTOS (service prefix: `freertos`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/freertos/latest/userguide/what-is-freertos.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/freertos/latest/userguide/what-is-freertos.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/freertos/latest/userguide/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/freertos/freertos.json) for this service.

**Topics**
+ [Actions defined by Amazon FreeRTOS](#list_freertos-actions-as-permissions)
+ [Resource types defined by Amazon FreeRTOS](#list_freertos-resources-for-iam-policies)
+ [Condition keys for Amazon FreeRTOS](#list_freertos-policy-keys)

## Actions defined by Amazon FreeRTOS
<a name="list_freertos-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateSoftwareConfiguration](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to create a software configuration
  - **Resource types (\*required):** [configuration\*](#list_freertos-resource-configuration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_freertos-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_freertos-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_freertos-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSubscription](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html)  **
  - **Description:** Grants permission to create a subscription for FreeRTOS extended maintenance plan (EMP)
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_freertos-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_freertos-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteSoftwareConfiguration](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to delete the software configuration
  - **Resource types (\*required):** [configuration\*](#list_freertos-resource-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_freertos-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeHardwarePlatform](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to describe the hardware platform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSoftwareConfiguration](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to describe the software configuration
  - **Resource types (\*required):** [configuration\*](#list_freertos-resource-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_freertos-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSubscription](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html)  **
  - **Description:** Grants permission to describes the subscription for FreeRTOS extended maintenance plan (EMP)
  - **Resource types (\*required):** [subscription\*](#list_freertos-resource-subscription)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_freertos-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEmpPatchUrl](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html)  **
  - **Description:** Grants permission to get URL for sotware patch-release, patch-diff and release notes under FreeRTOS extended maintenance plan (EMP)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSoftwareURL](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to get the URL for Amazon FreeRTOS software download
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSoftwareURLForConfiguration](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to get the URL for Amazon FreeRTOS software download based on the configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSubscriptionBillingAmount](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html)  **
  - **Description:** Grants permission to fetch the subscription billing amount for FreeRTOS extended maintenance plan (EMP)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListFreeRTOSVersions](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to lists versions of AmazonFreeRTOS
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHardwarePlatforms](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to list the hardware platforms
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHardwareVendors](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to list the hardware vendors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSoftwareConfigurations](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to lists the software configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSoftwarePatches](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html)  **
  - **Description:** Grants permission to list software patches of subscription for FreeRTOS extended maintenance plan (EMP)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscriptionEmails](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html)  **
  - **Description:** Grants permission to list the subscription emails for FreeRTOS extended maintenance plan (EMP)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscriptions](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html)  **
  - **Description:** Grants permission to list the subscriptions for FreeRTOS extended maintenance plan (EMP)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [UpdateEmailRecipients](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html)  **
  - **Description:** Grants permission to update list of subscription email address for FreeRTOS extended maintenance plan (EMP)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSoftwareConfiguration](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  **
  - **Description:** Grants permission to update the software configuration
  - **Resource types (\*required):** [configuration\*](#list_freertos-resource-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_freertos-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VerifyEmail](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html)  **
  - **Description:** Grants permission to verify the email for FreeRTOS extended maintenance plan (EMP)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon FreeRTOS
<a name="list_freertos-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [configuration](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ocw.html)  | arn:${Partition}:freertos:${Region}:${Account}:configuration/${ConfigurationName} | [aws:ResourceTag/${TagKey}](#list_freertos-aws_ResourceTag___TagKey_) | 
|  [subscription](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-emp.html)  | arn:${Partition}:freertos:${Region}:${Account}:subscription/${SubscriptionID} | [aws:ResourceTag/${TagKey}](#list_freertos-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon FreeRTOS
<a name="list_freertos-policy-keys"></a>

Amazon FreeRTOS defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tag key present in the request that the user makes to Amazon FreeRTOS | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key component attached to an Amazon FreeRTOS resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the list of all the tag key names associated with the resource in the request | ArrayOfString | 