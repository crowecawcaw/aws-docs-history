# Create CloudFormation StackSets with

self-managed permissions

This topic describes how to create StackSets with
_self-managed_ permissions to deploy stacks across AWS accounts
and Regions.

###### Note

Before you continue, create the IAM service roles required by StackSets to
establish a trusted relationship between the account you're administering the StackSet
from and the account you're deploying stacks to. For more information, see [Grant self-managed permissions](stacksets-prereqs-self-managed.md "stacksets-prereqs-self-managed.md").

###### Topics

- [Create a
  StackSet with self-managed permissions (console)](#stacksets-getting-started-create-self-managed-console "#stacksets-getting-started-create-self-managed-console")
- [Create a StackSet with
  self-managed permissions (AWS CLI)](#stacksets-getting-started-self-managed-cli "#stacksets-getting-started-self-managed-cli")

## Create a

StackSet with self-managed permissions (console)

###### To create a StackSet

1.  Sign in to the AWS Management Console and open the CloudFormation console at
    [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2.  On the navigation bar at the top of the screen, choose the AWS Region
    that you want to manage the StackSet from.
3.  From the navigation pane, choose **StackSets**.
4.  From the top of the **StackSets** page, choose
    **Create StackSet**.
5.  Under **Permissions**, choose **Self-service
    permissions** and choose the IAM roles you created.
6.  Under **Prerequisite - Prepare template**, choose
    **Template is ready**.
7.  Under **Specify template**, choose to either specify the
    URL for the S3 bucket that contains your stack template or upload a stack
    template file. Then, choose **Next**.
8.  On the **Specify StackSet details** page, provide a name
    for the StackSet, specify any parameters, and then choose
    **Next**.
9.  Choose **Next** to continue.
10. On the **Configure StackSet options** page, under
    **Tags**, specify any tags to apply to resources in
    your stack. For more information about how tags are used in AWS, see
    [Organizing
    and tracking costs using AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
    _AWS Billing and Cost Management User Guide_.
11. For **Execution configuration**, choose
    **Active** to enable CloudFormation's optimized operation
    handling:

        * Non-conflicting operations run concurrently for faster deployment
         times.
        * Conflicting operations are automatically queued and processed in
         the order they were requested.

    While operations are running or queued, CloudFormation queues all incoming
    operations even if they're non-conflicting. You can't change execution
    settings during this time.

12. If your template contains IAM resources, for
    **Capabilities**, choose **I acknowledge that
    this template may create IAM resources** to specify that you
    want to use IAM resources in the template. For more information, see [Acknowledging IAM resources in CloudFormation
    templates](control-access-with-iam.md#using-iam-capabilities "control-access-with-iam.md#using-iam-capabilities").
13. Choose **Next**.
14. On the **Set deployment options** page, for **Add
    stacks to StackSet**, choose **Deploy new
    stacks**.
15. For **Accounts**, choose **Deploy stacks in
    accounts**. Paste your target AWS account numbers in the text
    box, separating multiple numbers with commas.

###### Note

You can include your administrator account ID if you want to deploy
stacks in that account as well. 16. Under **Specify regions**, choose the Regions you want to
deploy stacks in. 17. For **Deployment options**, do the following:

    * For **Maximum concurrent accounts**, specify how
     many accounts are processed concurrently.
    * For **Failure tolerance**, specify the maximum
     number of account failures allowed per Region. The operation will
     stop and won't proceed to other Regions once this limit is
     reached.
    * For **Region concurrency**, choose how to process
     Regions: **Sequential** (one Region at a time) or
     **Parallel** (multiple Regions
     concurrently).
    * For **Concurrency mode**, choose how concurrency
     behaves during operation execution.




    	+ **Strict failure tolerance** –
    	 Reduces account concurrency level when failures occur,
    	 staying within **Failure tolerance**
    	 +1.
    	+ **Soft failure tolerance** –
    	 Maintains your specified concurrency level (the value of
    	 **Maximum concurrent accounts**)
    	 regardless of failures.

18. Choose **Next**.
19. On the **Review** page, review your choices. To make
    changes, choose **Edit** on the related section.
20. When you are ready to create your StackSet, choose
    **Submit**.

CloudFormation starts creating your StackSet. View the progress and status of the
creation of the stacks in your StackSet in the StackSet details page that opens when
you choose **Submit**.

## Create a StackSet with

self-managed permissions (AWS CLI)

Follow the steps in this section to use the AWS CLI to:

- Create the StackSet container.
- Deploy stack instances.

###### To create a StackSet

1. Use the [create-stack-set](../../../cli/latest/reference/cloudformation/create-stack-set.md "../../../cli/latest/reference/cloudformation/create-stack-set.md") command to create a new
   StackSet named `my-stackset`. The
   following example uses a template stored in an S3 bucket and includes a
   parameter that sets a `KeyPairName`
   with the value `TestKey`.

```
aws cloudformation create-stack-set \
  --stack-set-name `my-stackset` \
  --template-url `https://s3.region-code.amazonaws.com/amzn-s3-demo-bucket/MyApp.template` \
  --parameters `ParameterKey=KeyPairName,ParameterValue=TestKey`
```

2. After your **create-stack-set** command is finished, run
   the [list-stack-sets](../../../cli/latest/reference/cloudformation/list-stack-sets.md "../../../cli/latest/reference/cloudformation/list-stack-sets.md") command to see that your
   StackSet has been created. You should see your new StackSet in the results.

```
aws cloudformation list-stack-sets
```

3. Use the [create-stack-instances](../../../cli/latest/reference/cloudformation/create-stack-instances.md "../../../cli/latest/reference/cloudformation/create-stack-instances.md") command to deploy
   stacks within your StackSet. The following example deploys stacks in two
   AWS accounts (`account_ID_1` and
   `account_ID_2`) across two
   Regions (`us-west-2` and
   `us-east-1`).

Set concurrent account processing and other deployment preferences using
the `--operation-preferences` option. This example uses
count-based settings. Note that `MaxConcurrentCount` must not
exceed `FailureToleranceCount` + 1. For percentage-based
settings, use `FailureTolerancePercentage` or
`MaxConcurrentPercentage` instead.

```
aws cloudformation create-stack-instances \
  --stack-set-name `my-stackset` \
  --accounts `account_ID_1 account_ID_2` \
  --regions `us-west-2 us-east-1` \
  --operation-preferences `MaxConcurrentCount=1,FailureToleranceCount=0`
```

For more information, see [CreateStackInstances](../APIReference/API_CreateStackInstances.md "../APIReference/API_CreateStackInstances.md") in the
_AWS CloudFormation API Reference_. 4. Use the [describe-stack-set-operation](../../../cli/latest/reference/cloudformation/describe-stack-set-operation.md "../../../cli/latest/reference/cloudformation/describe-stack-set-operation.md") command to
verify that your stacks were created successfully. For the
`--operation-id` option, specify the operation ID that was
returned as part of the **create-stack-instances**
output.

```
aws cloudformation describe-stack-set-operation \
  --stack-set-name `my-stackset` \
  --operation-id `operation_ID`
```
