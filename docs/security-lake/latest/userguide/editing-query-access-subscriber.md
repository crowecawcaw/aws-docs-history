

# Editing a subscriber with query access in Security Lake
<a name="editing-query-access-subscriber"></a>

Security Lake supports making edits to a subscriber with query access. You can edit the subscriber's name, description, external ID, principal (AWS account ID), and the log sources that the subscriber is able to consume. Choose your preferred method, and follow the steps to edit a subscriber with query access in the current AWS Region.

**Note**  
Security Lake does not support Lake Formation cross-account data sharing version 1. You must update Lake Formation cross-account data sharing to version 2 or version 3. For the steps to update **Cross account version settings** through the AWS Lake Formation console or the AWS CLI, see [To enable the new version](https://docs.aws.amazon.com/lake-formation/latest/dg/optimize-ram.html#version-update-steps) in the *AWS Lake Formation Developer Guide*.

------
#### [ Console ]

Based on the details that you want to edit, follow the steps provided for that action only.

**To edit subscriber name**  

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/).

   Sign in to the delegated administrator account.

1. By using the AWS Region selector in the upper-right corner of the page, select the Region where you want to edit the subscriber details.

1. In the navigation pane, choose **Subscribers**.

1. On the **Subscribers** page, use the radio button to select the subscriber that you want to edit. The **Data access method** for the selected subscriber must be **LAKEFORMATION**.

1. Choose **Edit**.

1. Enter the new **Subscriber name**, and choose **Save**.

**To edit subscriber description**  

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/).

   Sign in to the delegated administrator account.

1. By using the AWS Region selector in the upper-right corner of the page, select the Region where you want to edit the subscriber.

1. In the navigation pane, choose **Subscribers**.

1. On the **Subscribers** page, use the radio button to select the subscriber that you want to edit. The **Data access method** for the selected subscriber must be **LAKEFORMATION**.

1. Choose **Edit**.

1. Enter the new description for the subscriber, and choose **Save**.

**To edit external ID**  

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/).

   Sign in to the delegated administrator account.

1. By using the AWS Region selector in the upper-right corner of the page, select the Region where you want to edit the subscriber details.

1. In the navigation pane, choose **Subscribers**.

1. On the **Subscribers** page, use the radio button to select the subscriber that you want to edit. The **Data access method** for the selected subscriber must be **LAKEFORMATION**.

1. Choose **Edit**.

1. Enter the new **External ID** that the subscriber has provided, and choose **Save**.

   Saving the new external ID automatically removes the previous AWS RAM resource share and creates a new resource share for the subscriber.

1. The subscriber must accept the new resource share by following step 1 in [Setting up cross-account table sharing (subscriber step)](create-query-subscriber-procedures.md#grant-query-access-subscriber). Make sure the Amazon Resource Name (ARN) that appears in subscriber details is the same as in the Lake Formation console. The resource link to the shared tables remains as is, so the subscriber doesn't have to create a new resource link.

**To edit principal (AWS account ID)**  

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/).

   Sign in to the delegated administrator account.

1. By using the AWS Region selector in the upper-right corner of the page, select the Region where you want to edit the subscriber details.

1. In the navigation pane, choose **Subscribers**.

1. On the **Subscribers** page, use the radio button to select the subscriber that you want to edit. The **Data access method** for the selected subscriber must be **LAKEFORMATION**.

1. Choose **Edit**.

1. Enter the new **AWS account ID** of the subscriber, and choose **Save**.

   Saving the new account ID automatically removes the previous AWS RAM resource share so the previous principal can't consume the log and event sources. Security Lake creates a new resource share.

1. Using the credentials of the new principal, the subscriber must accept the new resource share and create a resource link to the shared tables. This gives the new principal access to the shared resources. For instructions, see steps 1 and 2 in [Setting up cross-account table sharing (subscriber step)](create-query-subscriber-procedures.md#grant-query-access-subscriber). Make sure the ARN that appears in the subscriber details is the same as in the Lake Formation console. 

**To edit log and event sources**  

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/).

   Sign in to the delegated administrator account.

1. By using the AWS Region selector in the upper-right corner of the page, select the Region where you want to edit the subscriber details.

1. In the navigation pane, choose **Subscribers**.

1. On the **Subscribers** page, use the radio button to select the subscriber that you want to edit. The **Data access method** for the selected subscriber must be **LAKEFORMATION**.

1. Choose **Edit**.

1. Deselect existing sources or select sources that you want to add. If you deselect a source, no further action is required from your end. If you select to add a source, no new resource share invitation is created. However, Security Lake updates the shared Lake Formation tables based on the added sources. The subscriber must create a resource link to the updated shared tables so that they can query the source data. For instructions, see step 2 in [Setting up cross-account table sharing (subscriber step)](create-query-subscriber-procedures.md#grant-query-access-subscriber).

1. Choose **Save**.

------
#### [ API ]

To edit a subscriber with query access programmatically, use the [UpdateSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateSubscriber.html) operation of the Security Lake API. If you're using the AWS Command Line Interface (AWS CLI), run the [update-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-subscriber.html) command. In your request, use the supported parameters to specify the following settings for the subscriber:
+ For `subscriberName`, specify the new subscriber name.
+ For `subscriberDescription`, specify the new description.
+ For `subscriberIdentity`, specify the principal (AWS account ID) and external ID that the subscriber will use to query source data. You must provide both the principal and external ID. If you want to keep one of these values the same, pass in the current value.
  + **Updating only external ID** – This action removes the previous AWS RAM resource share and creates a new resource share for the subscriber. The subscriber must accept the new resource share by following step 1 in [Setting up cross-account table sharing (subscriber step)](create-query-subscriber-procedures.md#grant-query-access-subscriber). The resource link to the shared tables remains as is, so the subscriber doesn't have to create a new resource link.
  + **Updating only principal** – This action removes the previous AWS RAM resource share so the previous principal can't consume the log and event sources. Security Lake creates a new resource share. Using the credentials of the new principal, the subscriber must accept the new resource share and create a resource link to the shared tables. This gives the new principal access to the shared resources. For instructions, see steps 1 and 2 in [Setting up cross-account table sharing (subscriber step)](create-query-subscriber-procedures.md#grant-query-access-subscriber).

  To update the external ID *and* principal, follow steps 1 and 2 in [Setting up cross-account table sharing (subscriber step)](create-query-subscriber-procedures.md#grant-query-access-subscriber).
+ For `sources`, remove existing sources or specify sources that you want to add. If you remove a source, no further action is required from your end. If you add a source, no new resource share invitation is created. However, Security Lake updates the shared Lake Formation tables based on the added sources. The subscriber must create a resource link to the updated shared tables so that they can query the source data. For instructions, see step 2 in [Setting up cross-account table sharing (subscriber step)](create-query-subscriber-procedures.md#grant-query-access-subscriber).

------