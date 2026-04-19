# Specifying or changing the Parameter Store default tier using the console

The following procedure shows how to use the Systems Manager console to specify or
change the default parameter tier for the current AWS account and
AWS Region.

###### Tip

If you haven't created a parameter yet, you can use the AWS Command Line Interface
(AWS CLI) or AWS Tools for Windows PowerShell to change the default parameter tier. For
information, see [Specifying or changing the Parameter Store default tier using the AWS CLI](parameter-store-tier-changing-cli.md "parameter-store-tier-changing-cli.md") and [Specifying or changing the Parameter Store default tier (PowerShell)](parameter-store-tier-changing-ps.md "parameter-store-tier-changing-ps.md").

###### To specify or change the Parameter Store default tier

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Parameter Store**.
3. Choose the **Settings** tab.
4. Choose **Manage settings**.
5. In the **Parameter default tier** section, choose an option. For information about these options, see [Specifying a default parameter tier](ps-default-tier.md "ps-default-tier.md").
6. If prompted, select the option to approve the changes and authorize charges. Choose
   **Save settings**.
   If you want to change the default tier setting later, repeat this
   procedure and specify a different default tier option.
