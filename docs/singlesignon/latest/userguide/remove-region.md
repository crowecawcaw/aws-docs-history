

# Remove a Region from IAM Identity Center
<a name="remove-region"></a>

 To remove an additional Region from your IAM Identity Center instance, follow these steps: 

## Step 1: Update external IdP configuration (if applicable)
<a name="update-external-idp"></a>

 If you use an external identity provider, you can choose to remove the ACS URL for this Region from your external IdP or keep it in case you want to add this Region again later. We recommend that you remove or hide the bookmark app you might have created for the AWS access portal in this Region. If you use the Identity Center directory as your identity source, proceed to Step 2. 

## Step 2: Remove the Region
<a name="remove-region-step"></a>

------
#### [ Console ]

 **To remove a Region** 

1.  Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/). 

1.  In the navigation pane, choose **Settings**. 

1.  Choose the **Management** tab. 

1.  In the **Regions for IAM Identity Center** section, choose the additional Region you want to remove. 

1.  Choose **Remove**. 

1.  Before confirming removal by choosing **Remove Region**, pay attention to the warning about the potential loss of access to applications that were created in this IAM Identity Center Region. If you're not sure whether you have such applications, choose **Applications** in the navigation pane and confirm the connected Region in the **Created from** column for each AWS managed and customer managed application.
**Note**  
 You may continue incurring charges for deployments of AWS managed applications that are still connected to the removed Region even if you lose access to these applications. To prevent this, you need to remove these AWS managed application deployments through the application console or API before removing the Region in IAM Identity Center. If you already removed the IAM Identity Center Region, you can restore access to applications by adding the Region back. 

1.  In the **Regions for IAM Identity Center** section, monitor the Region status. Use the **Refresh** button (circular arrow) to see the latest Region status as needed. After the Region is removed, the Region no longer appears in the Region list. 

------
#### [ AWS CLI ]

 **To remove a Region** 

```
aws sso-admin remove-region \
    --instance-arn arn:aws:sso:::instance/ssoins-1234567890abcdef \
    --region-name eu-west-1
```

 **To check the current Region status** 

```
aws sso-admin describe-region \
    --instance-arn arn:aws:sso:::instance/ssoins-1234567890abcdef \
    --region-name eu-west-1
```

 When the Region is removed, proceed to Step 3. 

------

## Step 3: Delete the replica key
<a name="remove-kms-key-replica"></a>

 You can choose to remove the replica key from this Region to avoid incurring KMS storage charges. For more information, see [Deleting an AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html). 

**Important**  
 Make sure to delete only the replica key in this specific Region. The other IAM Identity Center Regions continue to rely on the KMS key in the other enabled Regions for normal operations. 