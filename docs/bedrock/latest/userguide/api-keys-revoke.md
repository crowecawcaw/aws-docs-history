# Handle compromised long-term and short-term Amazon Bedrock API keys

If your API key becomes compromised, you should revoke permissions to use it. There are various methods that you can use to revoke permissions for an Amazon Bedrock API key:

- For long-term Amazon Bedrock API keys, you can use the [UpdateServiceSpecificCredential](../../../IAM/latest/APIReference/API_UpdateServiceSpecificCredential.html.md "../../../IAM/latest/APIReference/API_UpdateServiceSpecificCredential.html.md"), [ResetServiceSpecificCredential](../../../IAM/latest/APIReference/API_ResetServiceSpecificCredential.html.md "../../../IAM/latest/APIReference/API_ResetServiceSpecificCredential.html.md"), or [DeleteServiceSpecificCredential](../../../IAM/latest/APIReference/API_DeleteServiceSpecificCredential.html.md "../../../IAM/latest/APIReference/API_DeleteServiceSpecificCredential.html.md") to revoke permissions in the following ways:

  - Set the status of the key to inactive. You can reactivate the key later.
  - Reset the key. This action generates a new password for the key.
  - Delete the key permanently.

###### Note

To carry out these actions through the API, you must authenticate with AWS credentials and not with an Amazon Bedrock API key.

- For both long-term and short-term Amazon Bedrock API keys, you can attach IAM policies to revoke permissions.

###### Note

You can't deactivate, reset, or delete an individual short-term Amazon Bedrock API key. The Amazon Bedrock console doesn't list short-term keys after you generate them or provide revocation actions for them. A short-term key is a pre-signed URL that inherits the credentials and expiration of the session that generated it. To prevent use before the key expires, see [Invalidate an IAM session](#api-keys-iam-policies-invalidate-session "#api-keys-iam-policies-invalidate-session") or [Deny an identity the ability to make calls with an Amazon Bedrock API key](#api-keys-iam-policies-deny-call-with-bearer-token "#api-keys-iam-policies-deny-call-with-bearer-token"). These controls affect the generating session or identity, not only one short-term key.

###### Topics

- [Change the status of a long-term Amazon Bedrock API key](#api-keys-change-status "#api-keys-change-status")
- [Reset a long-term Amazon Bedrock API key](#api-keys-reset "#api-keys-reset")
- [Delete a long-term Amazon Bedrock API key](#api-keys-delete "#api-keys-delete")
- [Attach IAM policies to remove permissions for using an Amazon Bedrock API key](#api-keys-iam-policies "#api-keys-iam-policies")

## Change the status of a long-term Amazon Bedrock API key

If you need to prevent a key from being used temporarily, deactivate it. After you're ready for it to be used again, reactivate it.

Choose the tab for your preferred method, and then follow the steps:

Console

###### To deactivate a key

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, select **API keys**.
3. In the **Long-term API keys** section, choose a key whose **Status** is **Inactive**.
4. Choose **Actions**.
5. Select **Deactivate**.
6. To confirm, select **Deactivate API key**. The **Status** of the key becomes **Inactive**.

###### To reactivate a key

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, select **API keys**.
3. In the **Long-term API keys** section, choose a key whose **Status** is **Inactive**.
4. Choose **Actions**.
5. Select **Activate**.
6. To confirm, select **Activate API key**. The **Status** of the key becomes **Active**.

Python
To deactivate a key using the API, send an [UpdateServiceSpecificCredential](../../../IAM/latest/APIReference/API_UpdateServiceSpecificCredential.html.md "../../../IAM/latest/APIReference/API_UpdateServiceSpecificCredential.html.md") request with an [IAM endpoint](../../../general/latest/gr/iam-service.md "../../../general/latest/gr/iam-service.md") and specify the `Status` as `Inactive`. You can use the following code snippet to deactivate a key, replacing `${ServiceSpecificCredentialId}` with the value returned when you created the key.

```
import boto3

iam_client = boto3.client("iam")

iam_client.update_service_specific_credential(
    service_specific_credential_id=`${ServiceSpecificCredentialId}`,
    status="Inactive"
)
```

To reactivate a key using the API, send an [UpdateServiceSpecificCredential](../../../IAM/latest/APIReference/API_UpdateServiceSpecificCredential.html.md "../../../IAM/latest/APIReference/API_UpdateServiceSpecificCredential.html.md") request with an [IAM endpoint](../../../general/latest/gr/iam-service.md "../../../general/latest/gr/iam-service.md") and specify the `Status` as `Active`. You can use the following code snippet to reactivate a key, replacing `${ServiceSpecificCredentialId}` with the value returned when you created the key.

```
import boto3

iam_client = boto3.client("iam")

iam_client.update_service_specific_credential(
    service_specific_credential_id=`${ServiceSpecificCredentialId}`,
    status="Active"
)
```

## Reset a long-term Amazon Bedrock API key

If the value of your key has been compromised or you no longer have it, reset it. The key must not have expired yet. If it's already expired, delete the key and create a new one.

Choose the tab for your preferred method, and then follow the steps:

Console

###### To reset a key

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, select **API keys**.
3. In the **Long-term API keys** section, choose a key.
4. Choose **Actions**.
5. Select **Reset key**.
6. Select **Next**.

Python
To reset a key using the API, send a [ResetServiceSpecificCredential](../../../IAM/latest/APIReference/API_ResetServiceSpecificCredential.html.md "../../../IAM/latest/APIReference/API_ResetServiceSpecificCredential.html.md") request with an [IAM endpoint](../../../general/latest/gr/iam-service.md "../../../general/latest/gr/iam-service.md"). You can use the following code snippet to reset a key, replacing `${ServiceSpecificCredentialId}` with the value returned when you created the key.

```
import boto3

iam_client = boto3.client("iam")

iam_client.reset_service_specific_credential(
    service_specific_credential_id=`${ServiceSpecificCredentialId}`
)
```

## Delete a long-term Amazon Bedrock API key

If you no longer need a key or it has expired, delete it.

Choose the tab for your preferred method, and then follow the steps:

Console

###### To delete a key

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, select **API keys**.
3. In the **Long-term API keys** section, choose a key.
4. Choose **Actions**.
5. Select **Delete**.
6. Confirm the deletion.

###### An API key is linked with an IAM user

Deleting this API key doesn't delete the IAM user which was created with this key as the owner. You can delete the IAM user from IAM console in the next step.

Python
To delete a key using the API, send a [DeleteServiceSpecificCredential](../../../IAM/latest/APIReference/API_DeleteServiceSpecificCredential.html.md "../../../IAM/latest/APIReference/API_DeleteServiceSpecificCredential.html.md") request with an [IAM endpoint](../../../general/latest/gr/iam-service.md "../../../general/latest/gr/iam-service.md"). You can use the following code snippet to delete a key, replacing `${ServiceSpecificCredentialId}` with the value returned when you created the key.

```
import boto3

iam_client = boto3.client("iam")

iam_client.delete_service_specific_credential(
    service_specific_credential_id=`${ServiceSpecificCredentialId}`
)
```

## Attach IAM policies to remove permissions for using an Amazon Bedrock API key

This section provides some IAM policies that you can use to restrict access to an Amazon Bedrock API key.

### Deny an identity the ability to make calls with an Amazon Bedrock API key

To fully prevent an identity from making calls with an Amazon Bedrock API key, you must deny both of the following actions:

- `bedrock:CallWithBearerToken` – Controls API key usage through the Amazon Bedrock endpoint.
- `bedrock-mantle:CallWithBearerToken` – Controls API key usage through the Amazon Bedrock Mantle endpoint.

###### Important

Denying only `bedrock:CallWithBearerToken` does **not** prevent API key usage through the Mantle endpoint. You must also deny `bedrock-mantle:CallWithBearerToken` to completely block API key usage.

To prevent an identity from making calls with an API key, attach an IAM policy on the identity depending on the type of key:

- **Long-term key** – Attach the policy to the IAM user associated with the key.
- **Short-term key** – Attach the policy to the IAM identity used to generate the key.

The IAM policy that you can attach to the IAM identity is as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Deny",
 "Action": [
 "bedrock:CallWithBearerToken",
 "bedrock-mantle:CallWithBearerToken"
 ],
 "Resource": "*"
 }
}`

```

### Invalidate an IAM session

If a short-term key becomes compromised, you can prevent its usage by invalidating the session that was used to generate the key. To invalidate the session, attach the following policy to the IAM identity that generated the key. Replace `2014-05-07T23:47:00Z` with the time after which you want the session to be invalidated.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "DateLessThan": {"aws:TokenIssueTime": "`2014-05-07T23:47:00Z`"}
 }
 }
}`

```
