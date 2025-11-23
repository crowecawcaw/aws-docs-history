# Revoke Temporary delegation access

Although product provider access sessions are designed to expire automatically after their approved duration, you may need to terminate access immediately in certain situations. Revoking active product provider access provides an emergency control mechanism when security concerns arise, when the product provider's work is completed early, or when business requirements change. Both request initiators and administrators can revoke access to maintain security and operational control.

###### To revoke temporary delegation access

1. Sign in to the AWS Management Console and open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane on the left, choose _Temporary delegation requests_.
3. Locate the request ID for the access session you want to revoke.
4. Choose _Actions_ and then choose _Revoke access_.
5. In the dialog, choose _Revoke access_ to confirm that you want to immediately terminate the access session.
   After revoking access, the product provider will no longer be able to access your AWS resources. The revocation is logged in AWS CloudTrail for audit purposes.

###### Important

Revoking access immediately terminates the product provider access session. Any ongoing work or processes using the access will be interrupted. Ensure that revocation won't disrupt critical operations.

###### Note

You cannot revoke access for requests that were approved using a root user. AWS recommends that you avoid using a root user to approve delegation requests. Use an IAM role with appropriate permissions instead.
