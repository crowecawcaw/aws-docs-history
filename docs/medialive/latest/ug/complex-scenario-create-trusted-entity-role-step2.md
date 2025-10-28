# Create policies

After you have followed [Step A](complex-scenario-create-trusted-entity-role-step1.md "complex-scenario-create-trusted-entity-role-step1.md") to identify the policies that you need, you must create them on the IAM
console.

Follow this procedure for each policy.

1.  Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane on the left, choose **Policies**. Then choose
    **Create policy**. The **Create policy** wizard appears.
    This wizard walks you through the steps, including these key steps:
    - Select a service.
    - Select actions for that service.

    Typically (and by default), you specify the actions that you want to allow.

    But you can also choose the **Switch to deny permissions** button to
    deny the chosen actions instead. We recommend as a security best practice that you deny
    permissions only if you want to override a permission separately allowed by another statement
    or policy. We recommend that you limit the number of deny permissions to a minimum because
    they can increase the difficulty of troubleshooting permissions.
    - [Specify
      resources](../../../IAM/latest/UserGuide/access_controlling.md#access_controlling-resources "../../../IAM/latest/UserGuide/access_controlling.md#access_controlling-resources") for each action (if supported for the action). For example, if you choose
      the MediaLive `DescribeChannel` ARN you can specify the ARNs of specific channels.
    - Specify conditions (optional). For example:

          + You can specify that a user is allowed to perform an actions only when that
           user's request happens within a certain time range.
          + You can specify that the user must use a multi-factor authentication (MFA) device to
           authenticate.
          + You can specify that the request must originate from a range of IP addresses.

      For lists of all of the context keys that you can use in a policy condition, see [Actions,
      resources, and condition keys for AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") in the
      _Service Authorization Reference_.

3.  Choose **Create policy**.
