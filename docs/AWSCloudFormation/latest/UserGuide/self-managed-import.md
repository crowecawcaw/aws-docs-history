# Self-managed stack import for AWS CloudFormation StackSets

The CloudFormation stack import operation can import existing stacks into new or existing StackSets,
 so that you can migrate existing stacks to a StackSet in one operation. By using stack import,
 you avoid downtime and outages without deleting and recreating those resources. Once the stack is
 imported into a StackSet, the original stack will become a stack instance of the specified stack
 set.


###### Considerations for self-managed stack imports


* The stack import operation requires an administrator account in which you create a StackSet and a target account that contains a stack.
* The target account must have permission to use the `GetTemplate` operation with
 the input of stack ID or ARN. Because of that, your administrator account must be granted
 **AWSCloudFormationStackSetAdministrationRole** or
 **AWSCloudFormationStackSetsExectionRole** permissions.
###### Topics

* [Import an existing stack into a new StackSet
 (console)](#import-stacks-to-stack-set "#import-stacks-to-stack-set")
* [Import an existing stack into an existing
 StackSet (console)](#import-stack-to-existing-stackset "#import-stack-to-existing-stackset")
* [Import a stack into a StackSet
 (AWS CLI)](#importing-stack-to-stackset.cli "#importing-stack-to-stackset.cli")

## Import an existing stack into a new StackSet
 (console)


Before you begin, identify the stack that you want to import.



1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the navigation pane, choose **StackSets**.
3. At the top of the **StackSets** page, choose **Create
 StackSet**.
4. On the **Choose a template** page, specify a template by one of the
 following options and choose **Next**.




	* Choose **Amazon S3 URL** and specify the URL for your template in the text
	 box.


	* Choose **Upload a template file** and browse for your template.


	* Choose **From stack ID** and enter your stack ID.
5. On the **Specify StackSet details** page, enter the name of a StackSet
 you want to create and choose **Next**.


(Optional) Enter a description of the StackSet.
6. On the **Configure StackSet options** page, review your choices and
 choose **Next**.
7. On the **Set deployment options** page, choose **Import stacks
 to stack set**.
8. Enter the stack ID of the stack you want to import in the **Stacks to
 import** field. For example,
 ``arn:aws:cloudformation:us-east-1:123456789012:stack/StackToImport/f449b250-b969-11e0-a185-5081d0136786``.


(Optional) Choose **Add another stack ID** and enter the stack ID of
 another stack you want to import. You may add up to 10 stacks per stack import
 operation.
9. Review your deployment options and choose **Next**.
10. On the **Review** page, review your choices and your StackSet's
 properties. When you are ready to import your stack into your StackSet, choose
 **Submit**.

**Results**: The imported stack is now a stack instance of the
 specified StackSet. To learn more about the stack import status, see [StackSets status codes](stacksets-concepts.md#stackset-status-codes "stacksets-concepts.md#stackset-status-codes").


## Import an existing stack into an existing
 StackSet (console)


Before you begin, identify the stack that you want to import.



1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
 [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the navigation pane, choose **StackSets**.
3. On the **StackSets** page, choose the StackSet that you want to
 import a stack into.
4. With the StackSet selected, choose
 **Add
 stacks to StackSet** from the **Actions**
 menu.
5. On the **Set deployment options** page, choose **Import stacks
 to stack set** and enter the stack ID of the stack you want to import in the
 **Stacks to import** field. For example,
 ``arn:aws:cloudformation:us-east-1:123456789012:stack/StackToImport/f449b250-b969-11e0-a185-5081d0136786``.


(Optional) Choose **Add another stack ID** and enter the stack ID of
 another stack you want to import. You may add up to 10 stacks per stack import
 operation.
6. Choose **Next**.
7. On the **Specify overrides** page, review your choices and choose
 **Next**.
8. On the **Review** page, review your choices and your StackSet's
 properties. When you are ready to create your StackSet, choose
 **Submit**.

**Results**: The imported stack is now a stack instance of the
 specified StackSet. To learn more about the stack import status, see [StackSets status codes](stacksets-concepts.md#stackset-status-codes "stacksets-concepts.md#stackset-status-codes").


## Import a stack into a StackSet
 (AWS CLI)


###### To import an existing stack into a new StackSet


The following `create-stack-set` command creates a StackSet and imports the
 specified stack. The stack to import is identified by its ARN. Replace the placeholder text
 with your own information.



```
aws cloudformation create-stack-set \
  --stack-set-name `MyStackSet` \
  --stack-id `arn:aws:cloudformation:us-east-1:123456789012:stack/StackToImport/466df9e0-0dff-08e3-8e2f-5088487c4896` \
  --administration-role-arn `arn:aws:iam::123456789012:role/AWSCloudFormationStackSetAdministrationRole` \
  --execution-role-name `AWSCloudFormationStackSetExecutionRole`
```

###### To import an existing stack into an existing StackSet


The following `import-stacks-to-stack-sets` command imports the specified stack
 into the `MyStackSet` StackSet. The stack to import is identified by
 its ARN. Replace the placeholder text with your own information.



```
aws cloudformation import-stacks-to-stack-set \
  --stack-set `MyStackSet` \
  --stack-ids `arn:aws:cloudformation:us-east-1:123456789012:stack/StackToImport/f449b250-b969-11e0-a185-5081d0136786`
```

To specify more than one stack, use the following format for the value of the
 `--stack-ids` option.



```
--stack-ids "`arn_1`" "`arn_2`"
```

###### To clone the imported stack into other Regions and accounts


The following `create-stack-instances` command adds stack instances to your
 StackSet. Replace the placeholder text with your own information.



```
aws cloudformation create-stack-instances \
  --stack-set-name `MyStackSet` \
  --accounts '["`account_ID_1`","`account_ID_2`"]' \
  --regions '["`region_1`","`region_2`"]'
```
