# Granting IAM

permissions to your Kantar credentials

When you use AWS Elemental MediaConvert, you specify an IAM service role that grants
permissions to the service to access the resources it needs to run your job. For
example, your MediaConvert service role grants MediaConvert permissions to read your
job input files from Amazon S3. For information about setting up that service role, see [Setting up IAM permissions](iam-role.md "iam-role.md") .

To encode Kantar watermarks, add permissions to this service role to grant
MediaConvert access to read the AWS Secrets Manager secret that holds your Kantar
credentials.

###### To grant MediaConvert permission to read your Kantar credentials

1. Create a policy that grants permission to read your Secrets Manager secret.
   1. Make sure that you have the ARN to the Secrets Manager secret that you created
      in the previous topic.
   2. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   3. In the navigation pane on the left, under **Access
      management**, choose **Policies**.
   4. Choose **Create policy**.
   5. On the **Create policy** page, next to
      **Service**, choose **Choose a
      service**.
   6. In the search field, type `secrets` and then
      choose **Secrets Manager** from the results.
   7. In the **Filter actions** search field, type
      `GetSecretValue` and then choose
      **GetSecretValue** from the results.
   8. In the **Resources** section, next to
      **Secret**, choose **Add
      ARN**.
   9. On the **Add ARN(s)** page, next to **Specify
      ARN for Secret**, choose **List ARNs
      manually**.
   10. In the **Type or paste a list of ARNs** section,
       paste the ARN for your Kantar credentials secret that you copied at the
       end of the procedure in the previous topic.
   11. Choose **Add**.
   12. At the bottom of the **Create policy** page, choose
       **Next: Tags**.
   13. Choose **Next: Review**.
   14. Under **Review policy**, for
       **Name** type a name that will help you remember
       the purpose of this policy, such as
       `GetKantarCreds`.
   15. Optionally, for **Description**, jot a note to
       yourself for later. For example, you might write "This provides
       MediaConvert permission to read my Kantar credentials."
   16. Choose **Create policy**.

2. Attach the policy to your MediaConvert role.
   1. In the navigation pane on the left, under **Access
      management**, choose **Roles**.
   2. From the list of roles, choose the name of the role that you use with
      your MediaConvert job. This role is often
      **MediaConvert_Default_Role**.
   3. On the role **Summary** page, on the
      **Permissions** tab, choose **Attach
      policies**.
   4. In the search field, type the name of the policy you created, such as
      `GetKantarCreds`.
   5. In the results list, choose the check box next to the policy
      name.
   6. Choose **Attach policy**.
   7. On the **Summary** page for the role, review the list
      of policies and confirm that your policy that grants permission to get
      your Kantar credentials appears there.
