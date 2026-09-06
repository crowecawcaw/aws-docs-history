

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Understanding and managing Verified Amazon Q Apps
<a name="verfied-apps-management"></a>

The Verified Q Apps feature empowers administrators to endorse published Amazon Q Apps. The goal is to enhance governance and provide a clear signal to end-users about which Q Apps are recommended for use within their organization. By labeling apps as *Verified*, admins can help improve trust and adoption of the most valuable, high-quality Q Apps created by employees.

Admins can easily endorse published Q Apps by updating their status from *Default* to *Verified* directly within the Amazon Q Business console. The idea is that admins would work closely with their business stakeholders to determine the criteria for verifying apps, based on their organization's specific needs and policies. This admin-led labeling capability is a reactive approach to endorsing published apps, without gating the publishing process for app creators.

When users access the Amazon Q Apps Library, they will see a distinct blue checkmark icon on any apps that have been marked as *Verified* by administrators. Additionally verified apps are automatically surfaced to the top of the app list within each category, making them easily discoverable. Users can also filter the library to view only Verified apps.

**Note**  
If a Amazon Q App is unpublished and then re-published, or if changes are made to a *Verified* app, the verified label will be removed until the administrator re-applies it.

**Topics**
+ [Considerations for verifying Amazon Q Apps](#verified-apps-considersations)
+ [Verifying Amazon Q Apps](#verified-apps-update)
+ [Restoring Amazon Q Apps to the default state](#default-apps-update)

## Considerations for verifying Amazon Q Apps
<a name="verified-apps-considersations"></a>

To start using the Verified Apps feature in Amazon Q Apps, consider the following: 
+ **Determine Verification Criteria:** Work with business stakeholders to establish the criteria for verifying Q Apps. This could include factors like content quality, alignment with organizational policies, and user feedback.
+ **Review Published Apps:** Review the list of published apps against your criteria. This can be accessed from the Amazon Q Business console or API.

## Verifying Amazon Q Apps
<a name="verified-apps-update"></a>

To update an app state to verified you can use the console; or the [UpdateLibraryItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateLibraryItem.html) API operation. The following tabs provide a procedure for the console and code examples for the AWS CLI.

------
#### [ Console ]

**To verify Amazon Q Apps**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, select the name of your application environment from the list of applications.

1. From the left navigation menu, choose **Enhancements**, and then choose **Amazon Q Apps**.

1. In the **Amazon Q Apps in library** section, choose the Q Apps that you want to verify, and then choose **Update state**.

1. From the **Update state** drop down, choose **Verified**.

------
#### [ AWS CLI ]

**To verify Amazon Q Apps**

```
// to add the verified label
                        aws qapps update-library-item-metadata \
                        --instance-id  {{instanceId}} \
                        --library-item-id  {{libraryItemId}} \
                        --is-verified \
```

------

## Restoring Amazon Q Apps to the default state
<a name="default-apps-update"></a>

All Amazon Q Apps are always in a *Default* state when they are first published or updated. To remove an Amazon Q App verified state and change it back to default you can use the console; or the [UpdateLibraryItem](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateLibraryItem.html) API operation. The following tabs provide a procedure for the console and code examples for the AWS CLI.

------
#### [ Console ]

**To restore Amazon Q Apps state to default**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. In **Applications**, select the name of your application environment from the list of applications.

1. From the left navigation menu, choose **Enhancements**, and then choose **Amazon Q Apps**.

1. In the **Amazon Q Apps in library** section, choose the Q Apps that you want to verify, and then choose **Update state**.

1. From the **Update state** drop down, choose **Default**.

------
#### [ AWS CLI ]

**To restore Amazon Q Apps state to default**

```
// to add the verified label
                        aws qapps update-library-item-metadata \
                        --instance-id  {{instanceId}} \
                        --library-item-id  {{libraryItemId}} \
                        --no-is-verified \
```

------