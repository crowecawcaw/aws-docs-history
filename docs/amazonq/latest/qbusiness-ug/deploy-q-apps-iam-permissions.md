

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# IAM permissions for using Amazon Q Apps
<a name="deploy-q-apps-iam-permissions"></a>

If the users of your deployed web experience want to create lightweight, purpose-built Amazon Q Apps within your broader Amazon Q Business application environment, you must include the following policy permissions. 

**Note**  
This Amazon Q Apps IAM policy released on July 10, 2024 supports the ability for users to view and specify approved *data sources* at the card-level and use other future features. To use these features, you must update all roles for Amazon Q Apps that have been created prior to this date with this new policy.


| Change | Description | Date | 
| --- | --- | --- | 
|  Deprecated some IAM actions related to file upload |  The `qapps:ImportDocumentToQApp`, `qapps:ImportDocumentToQAppSession`, and `qapps:CreatePresignedUrl` IAM actions are deprecated. The `qapps:ImportDocument` action now serves as the single file upload action. |  05/22/2025  | 
|  Added Permission to ` CreatePresignedUrl `  |  This new API allows users to leverage the improved file limits in Amazon Q Apps. You can now upload files with size up to 10MB (per file card). |  11/22/2024  | 
|  Added Permissions to ` DescribeQAppPermissions ` and `UpdateQAppPermissions`  |  These new APIs allows users [privately share Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-private-sharing.html) to leverage the improved file limits in Amazon Q Apps. You can now upload files with size up to 10MB (per file card). |  11/22/2024  | 
|  Added permissions related to management of persistent sessions.  |  These new APIs allows users to start, manage and terminate long running collaborative [data collection sessions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/q-apps-forms.html) to leverage the improved file limits in Amazon Q Apps. You can now upload files with size up to 10MB (per file card). |  11/22/2024  | 

**Topics**
+ [Capabilities available with Amazon Q Apps](#q-apps-actions)
+ [IAM permissions for users to view and specify approved data sources in Amazon Q Apps](#deploy-data-source-iam-permissions)

**If you want to use Amazon Q Apps, your web experience IAM role needs the following additional permissions:**

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "QAppsResourceAgnosticPermissions",
            "Effect": "Allow",
            "Action": [
                "qapps:CreateQApp",
                "qapps:PredictQApp",
                "qapps:PredictProblemStatementFromConversation",
                "qapps:PredictQAppFromProblemStatement",
                "qapps:ListQApps",
                "qapps:ListLibraryItems",
                "qapps:CreateSubscriptionToken"
            ],
            "Resource": "arn:aws:qbusiness:us-east-1:111122223333:application/{{application-id}}"
        },
        {
            "Sid": "QAppsAppUniversalPermissions",
            "Effect": "Allow",
            "Action": [
                "qapps:DisassociateQAppFromUser"
            ],
            "Resource": "arn:aws:qapps:us-east-1:111122223333:application/{{application-id}}/qapp/*"
        },
        {
            "Sid": "QAppsAppOwnerPermissions",
            "Effect": "Allow",
            "Action": [
                "qapps:GetQApp",
                "qapps:CopyQApp",
                "qapps:UpdateQApp",
                "qapps:DeleteQApp",
                "qapps:ImportDocument",
                "qapps:CreateLibraryItem",
                "qapps:UpdateLibraryItem",
                "qapps:StartQAppSession",
                "qapps:DescribeQAppPermissions",
                "qapps:UpdateQAppPermissions"
            ],
            "Resource": "arn:aws:qapps:us-east-1:111122223333:application/{{application-id}}/qapp/*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "qapps:UserIsAppOwner": "true"
                }
            }
        },
        {
            "Sid": "QAppsPublishedAppPermissions",
            "Effect": "Allow",
            "Action": [
                "qapps:GetQApp",
                "qapps:CopyQApp",
                "qapps:AssociateQAppWithUser",
                "qapps:GetLibraryItem",
                "qapps:CreateLibraryItemReview",
                "qapps:AssociateLibraryItemReview",
                "qapps:DisassociateLibraryItemReview",
                "qapps:StartQAppSession",
                "qapps:DescribeQAppPermissions"
            ],
            "Resource": "arn:aws:qapps:us-east-1:111122223333:application/{{application-id}}/qapp/*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "qapps:AppIsPublished": "true"
                }
            }
        },
        {
            "Sid": "QAppsAppSessionModeratorPermissions",
            "Effect": "Allow",
            "Action": [
                "qapps:ImportDocument",
                "qapps:GetQAppSession",
                "qapps:GetQAppSessionMetadata",
                "qapps:UpdateQAppSession",
                "qapps:UpdateQAppSessionMetadata",
                "qapps:StopQAppSession",
                "qapps:ListQAppSessionData",
                "qapps:ExportQAppSessionData"
            ],
            "Resource": "arn:aws:qapps:us-east-1:111122223333:application/{{application-id}}/qapp/*/session/*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "qapps:UserIsSessionModerator": "true"
                }
            }
        },
        {
            "Sid": "QAppsSharedAppSessionPermissions",
            "Effect": "Allow",
            "Action": [
                "qapps:ImportDocument",
                "qapps:GetQAppSession",
                "qapps:GetQAppSessionMetadata",
                "qapps:UpdateQAppSession",
                "qapps:ListQAppSessionData"
            ],
            "Resource": "arn:aws:qapps:us-east-1:111122223333:application/{{application-id}}/qapp/*/session/*",
            "Condition": {
                "StringEqualsIgnoreCase": {
                    "qapps:SessionIsShared": "true"
                }
            }
        }
    ]
}
```

------

## Capabilities available with Amazon Q Apps
<a name="q-apps-actions"></a>

The Amazon Q Apps IAM policy allows your web experience users permissions to do the following:
+ **Amazon Q Apps capabilities:**
  + Create a Q App ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CreateQApp.html))
  + Get the status and other information on a Q App ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetQApp.html))
  + Update a Q App ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQApp.html))
  + List all created Q Apps ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListQApps.html))
  + Delete a Q App ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DeleteQApp.html))
  + Start a Q App run (session) ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_StartQAppSession.html))
  + Stop a Q App run (session) ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_StopQAppSession.html))
  + Upload files to a Q App run (session) ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ImportDocument.html))
  + Converts a conversation into a (*text string*) problem statement ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PredictQApp.html))
  + Convert a problem statement into a proposed Q App ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PredictQApp.html))
+ **Amazon Q Apps library capabilities:**
  + Publish a Q App by adding items to your Q Apps library ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CreateLibraryItem.html))
  + Get the status and other information on a Q App (item) in your Q Apps library ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetLibraryItem.html))
  + Update a published Q App (item) in your Q Apps library ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateLibraryItem.html))
  + List all Q Apps (items) from your Q Apps library ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ListLibraryItems.html))
  + Delete a Q App (item) from your Q Apps library ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DeleteLibraryItem.html))
  + Like (rate) a Q App item from your Q Apps library ([API](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_AssociateLibraryItemReview.html))

## IAM permissions for users to view and specify approved data sources in Amazon Q Apps
<a name="deploy-data-source-iam-permissions"></a>

**(Optional) You must add the following permissions to the Amazon Q Apps policy to allow Q Apps users to view and specify approved data sources** in their app.

**Note**  
If you are using permissions for Amazon Q Apps created prior to July 10, 2024, you must update your role with the new [Amazon Q Apps](#deploy-q-apps-iam-permissions) permissions for your users to have access to use the [permissions to view and specify approved data sources](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/deploy-q-apps-iam-permissions.html#deploy-data-source-iam-permissions) and other future features in Q Apps.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "QBusinessIndexPermission",
            "Effect": "Allow",
            "Action": [
                "qbusiness:ListIndices"
            ],
            "Resource": "arn:aws:qbusiness:us-east-1:111122223333:application/{{application-id}}"
        },
        {
            "Sid": "QBusinessDataSourcePermission",
            "Effect": "Allow",
            "Action": [
                "qbusiness:ListDataSources"
            ],
            "Resource": [
                "arn:aws:qbusiness:us-east-1:111122223333:application/{{application-id}}",
                "arn:aws:qbusiness:us-east-1:111122223333:application/{{application-id}}/index/*"
            ]
        }
    ]
}
```

------

**Note**  
If any of these permissions are removed, then you run the risk of your web experience users not being able to create and run their own Q Apps properly. 