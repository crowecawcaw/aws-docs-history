# Get information about a

single on-premises instance

You can get information about a single on-premises instance by following the instructions
in [View CodeDeploy deployment details](deployments-view-details.md "deployments-view-details.md") . You
can use the AWS CLI or the CodeDeploy console to get more information about a single on-premises
instance.

###### To get information about a single on-premises instance (CLI)

- Call the [get-on-premises-instance](../../../cli/latest/reference/deploy/get-on-premises-instance.md "../../../cli/latest/reference/deploy/get-on-premises-instance.md") command, specifying the name that
  uniquely identifies the on-premises instance (with the `--instance-name`
  option):

```
aws deploy get-on-premises-instance --instance-name AssetTag12010298EX
```

###### To get information about a single on-premises instance (console)

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy "https://console.aws.amazon.com/codedeploy").

###### Note

Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md "getting-started-codedeploy.md"). 2. In the navigation pane, expand **Deploy**, and choose **On-premises instances**. 3. In the list of on-premises instances, choose the name of an on-premises instance to
view its detail.
