# Permissions for Amazon CloudWatch Logs

Use AWS Identity and Access Management (IAM) to create a role that gives AWS Elemental MediaTailor access to Amazon CloudWatch.
You must perform these steps for CloudWatch Logs to be published for your account. CloudWatch automatically
publishes metrics for your account.

###### To allow MediaTailor access to CloudWatch

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**,
   and then choose **Create role**.
3. Choose the **Another AWS account** role type.
4. For **Account ID**, enter your AWS account ID.
5. Select **Require external ID** and enter
   `Midas`. This option automatically adds a condition to the
   trust policy that allows the service to assume the role only if the request includes
   the correct `sts:ExternalId`.
6. Choose **Next: Permissions**.
7. Add a permissions policy that specifies what actions this role can complete.
   Select from one of the following options, and then choose **Next:
   Review**:
   - **CloudWatchLogsFullAccess** to provide full access to
     Amazon CloudWatch Logs
   - **CloudWatchFullAccess** to provide full access to
     Amazon CloudWatch

8. For **Role name**, enter
   `MediaTailorLogger`, and then choose **Create
   role**.
9. On the **Roles** page, choose the role that you just created.
10. To update the principal, edit the trust relationship:
    1. On the role's **Summary** page, choose the
       **Trust relationship** tab.
    2. Choose **Edit trust relationship**.
    3. In the policy document, change the principal to the MediaTailor service.
       It should look like this:

    ```
    "Principal": {
       "Service": "mediatailor.amazonaws.com"
    },
    ```

    The entire policy should read as follows: 4. Choose **Update Trust Policy**.
