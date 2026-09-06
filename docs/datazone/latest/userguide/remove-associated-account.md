

# Remove an associated account in Amazon DataZone
<a name="remove-associated-account"></a>

To remove an associated AWS account in the Amazon DataZone management console, you must assume an IAM role in the account with administrative permissions. [Configure the IAM permissions required to use the Amazon DataZone management console](create-iam-roles.md) to obtain the minimum permissions.

Complete the following procedure to remove an associated account from your domain.

1. Sign in to the AWS Management Console and open the Amazon DataZone management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone).

1. Choose **View Domains** and choose the domain’s name from the list. The name is a hyperlink.

1. Scroll down to the **Associated accounts** tab. Choose the account ID for the AWS account you want to remove.

1. Choose **Disassociate**. Confirm your choice by entering disassociate in the field and choosing **Disassociate**.

1. The account is now removed from your domain and cannot be used by the domain’s users to publish and consume data.