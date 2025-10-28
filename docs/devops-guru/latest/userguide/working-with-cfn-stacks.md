# Using AWS CloudFormation stacks to identify resources in your DevOps Guru applications

You can use AWS CloudFormation stacks to specify which AWS resources you want DevOps Guru to analyze. A
stack is a collection of AWS resources that are managed as a single unit. The resources in
the stacks you choose make up your DevOps Guru coverage boundary. For each stack you choose,
operational data in its supported resources are analyzed for anomalous behavior. Those
issues are then grouped into related anomalies to create insights. Each insight includes one
or more recommendations to help you address them. The maximum number of stacks you can
specify is 1000. For more information, see [Working with stacks](../../../AWSCloudFormation/latest/UserGuide/stacks.md "../../../AWSCloudFormation/latest/UserGuide/stacks.md") in the
_AWS CloudFormation User Guide_ and [Updating your AWS analysis coverage in DevOps Guru](update-settings.md#update-coverage "update-settings.md#update-coverage").

After you choose a stack, DevOps Guru immediately starts to analyze any resource you add to it.
If you remove a resource from a stack, it is no longer analyzed.

If you choose to have DevOps Guru analyze all supported resources in your account (this means your
AWS account and Region is your DevOps Guru coverage boundary), then DevOps Guru analyzes and creates
insights for every supported resource in your account, including those in stacks. An insight
created from anomalies in a resource that is not in a stack is grouped at the
_account level_. If an insight is created from anomalies in a
resource that is in a stack,then it is grouped at the _stack level_. For
more information, see [Understanding how anomalous behaviors are
grouped into insights](working-with-insights.md#how-insights-are-grouped "working-with-insights.md#how-insights-are-grouped").

## Choosing stacks for DevOps Guru to analyze

Specify the resources that you want Amazon DevOps Guru to analyze by choosing the AWS CloudFormation stacks
that create them. You can do this using the AWS Management Console or the SDK.

###### Topics

- [Choosing stacks for DevOps Guru to analyze
  (console)](#choose-stacks-console "#choose-stacks-console")
- [Choosing stacks for DevOps Guru to analyze (DevOps Guru
  SDK)](#choose-stacks-sdk "#choose-stacks-sdk")

### Choosing stacks for DevOps Guru to analyze

(console)

You can add AWS CloudFormation stacks using the console.

###### To choose the stacks that contain the resources to analyze

1. Open the Amazon DevOps Guru console at [https://console.aws.amazon.com/devops-guru/](https://console.aws.amazon.com/devops-guru/ "https://console.aws.amazon.com/devops-guru/").
2. Open the navigation pane, then choose **Settings**.
3. In **DevOps Guru analysis coverage**, choose
   **Manage**.
4. Choose **CloudFormation stacks** if you want DevOps Guru to
   analyze the resources that are in stacks you choose, then choose one of
   the following options.
   - **All resources** – All resources that
     are in stacks in your account are analyzed. Resources in each
     stack are grouped into their own application. Any resources in
     your account that are not in a stack are not analyzed.
   - **Select stacks** – Select the stacks
     that you want DevOps Guru to analyze. The resources in each stack you
     select are grouped into their own application. You can enter
     the name of a stack in **Find stacks** to
     quickly locate a specific stack. You can select up to 1,000
     stacks.

5. Choose **Save**.

### Choosing stacks for DevOps Guru to analyze (DevOps Guru

SDK)

To specify AWS CloudFormation stacks using the Amazon DevOps Guru SDK, use the
`UpdateResourceCollection` method. For more information, see [UpdateResourceCollection](../APIReference/API_UpdateResourceCollection.md "../APIReference/API_UpdateResourceCollection.md") in the _Amazon DevOps Guru API
Reference_.
