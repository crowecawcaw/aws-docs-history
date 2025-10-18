# Best practices for using AWS CloudFormation StackSets

This section describes the best practices for defining a StackSet template, creating or adding
 stacks to a StackSet, or updating a StackSet.

If you are new to CloudFormation, review the [CloudFormation best practices](best-practices.md "best-practices.md") topic for more recommendations that can help you use
 CloudFormation more effectively and securely.

###### Topics

* [Defining the template](#w71aac15c41b9 "#w71aac15c41b9")
* [Creating or adding stacks to the StackSet](#w71aac15c41c11 "#w71aac15c41c11")
* [Updating stacks in a StackSet](#w71aac15c41c13 "#w71aac15c41c13")

## Defining the template



* Define the template that you want to standardize in multiple accounts, within
 multiple regions.
* As you create the template, be sure that global resources (such as IAM roles
 and Amazon S3 buckets) do not have naming conflicts when they are created in more
 than one region in the same account.
* A StackSet has a single template and parameter set. The same stack is created in
 all accounts that are associated with a StackSet. As you author your templates, make
 them granular enough to allow you a good balance of control and standardization.
* We recommend that you store your template in an Amazon S3 bucket.

## Creating or adding stacks to the StackSet



* Verify that adding stack instances to your initial StackSet works before you add
 larger numbers of stack instances to your StackSet.
* Choose the deployment (rollout) options that work for your use case.




	+ For a more conservative deployment, set **Maximum Concurrent
	 Accounts** to 1, and **Failure Tolerance**
	 to 0. Set your lowest-impact region to be first in the **Region
	 Order** list. Start with one region.
	+ For a faster deployment, increase the values of **Maximum
	 Concurrent Accounts** and **Failure
	 Tolerance** as needed.
* Operations on StackSets depend on how many stack instances are involved,
 and can take significant time.

## Updating stacks in a StackSet



* By default, updating a StackSet updates all stack instances. If you have 20
 accounts each in two regions, you will have 40 stack instances, and all will be
 updated when you update the StackSet.


For StackSets with a large number of stack instances, we recommend that to
 test the updated version of a template, you selectively update the stack
 instances in a few test accounts before updating all stack instances.
* To get more granular control over updating individual stacks within your StackSet,
 plan to create multiple StackSets.
* Updating a StackSet that contains a large number of stacks can take significant
 time. In this release, only one operation is permitted at a time on a StackSet. Plan
 your updates so you are not blocked from performing other operations on the
 StackSet.
