

# Retrieving user metadata and attributes using userID in an identity store
<a name="query-session-data-map-userid"></a>

**Note**  
This procedure also applies to the `createdBy` field returned by the [SearchJobs](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchJobs.html) API, which uses the same user ID format.

The `userId` field in session statistics contains one of the following values:
+ An AWS Identity and Access Management (IAM) role ARN, for example: `arn:aws:sts::123456789012:assumed-role/Admin/user-Isengard`.
+ An IAM Identity Center user ID (UUID), for example: `f9c1f3f0-1031-70dc-4d25-30d7225b04a0`.

For IAM role ARNs, the username is visible in the ARN itself. For IAM Identity Center user IDs, you can look up the username using the IAM Identity Center Identity Store API.

To identify the username associated with an IAM Identity Center user ID, use the following procedure. Before you begin, get the Identity Store ID from your IAM Identity Center settings. For more information, see [Finding your Identity Store ID](#query-session-data-find-identity-store-id).

## To map a user ID
<a name="query-session-data-map-userid-cli"></a>

1. Run the following command, replacing {{IdentityStoreId}} with your Identity Store ID and {{userUUID}} with the `userId` from the session statistics response:

   ```
   aws identitystore describe-user \
       --identity-store-id {{IdentityStoreId}} \
       --user-id {{userUUID}}
   ```

1. Review the response, which includes the username:

   ```
   {
       "UserName": "jdoe",
       "UserId": "f9c1f3f0-1031-70dc-4d25-30d7225b04a0",
       "Name": {
           "FamilyName": "Doe",
           "GivenName": "Jane"
       },
       "DisplayName": "Jane Doe",
       "Emails": [{
           "Value": "jdoe@example.com",
           "Type": "work",
           "Primary": true
       }],
       "IdentityStoreId": "d-xxxxxxxxxx"
   }
   ```

## Finding your Identity Store ID
<a name="query-session-data-find-identity-store-id"></a>

To map user IDs to usernames, you need the Identity Store ID. You can find the Identity Store ID using the IAM Identity Center console or the AWS CLI.

**Console**  
To find your Identity Store ID using the console, use the following procedure.

1. Sign in to the AWS Management Console and open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/home).

1. In the navigation pane, choose **Settings**.

1. Copy the **IAM Identity Center Identity Store ID** value. The format is `d-xxxxxxxxxx`.

**AWS CLI**  


Run the following command, replacing {{region-name}} with the Region where your IAM Identity Center instance is configured:

```
aws sso-admin list-instances --region {{region-name}}
```

The response includes the `IdentityStoreId`:

```
{
    "Instances": [
        {
            "CreatedDate": "2025-11-19T15:45:55.160000-08:00",
            "IdentityStoreId": "d-xxxxxxxxxx",
            "InstanceArn": "arn:aws:sso:::instance/ssoins-xxxxxxxxxxxxxxxx",
            "OwnerAccountId": "123456789012",
            "Status": "ACTIVE"
        }
    ]
}
```

## Verifying the user mapping
<a name="query-session-data-verify-user"></a>

After you map a user ID to a username, you can verify in the IAM Identity Center console that the user ID matches the expected user. To verify the user mapping, use the following procedure.

1. Sign in to the AWS Management Console and open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/home).

1. In the navigation pane, choose **Users**.

1. Choose the username from the AWS CLI response.

1. In the **General information** section, verify that the **User ID** matches the `userId` from your session statistics.

## Additional resources
<a name="query-session-data-additional-resources"></a>
+ [IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
+ [IAM Identity Center Identity Store API Reference](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html)