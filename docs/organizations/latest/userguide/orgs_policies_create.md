# Creating organization policies with AWS Organizations

After you [enable policies](enable-policy-type.md "enable-policy-type.md") for your organization,
you can create a policy.

This topic describes how to create policies with AWS Organizations. A _policy_
defines the controls that you want to apply to a group of AWS accounts.

###### Topics

- [Create a service control policy (SCP)](#create-an-scp "#create-an-scp")
- [Create a resource control policy (RCP)](#create-an-rcp "#create-an-rcp")
- [Create a declarative
  policy](#create-declarative-policy-procedure "#create-declarative-policy-procedure")
- [Create a backup policy](#create-backup-policy-procedure "#create-backup-policy-procedure")
- [Create a tag policy](#create-tag-policy-procedure "#create-tag-policy-procedure")
- [Create a chat applications
  policy](#create-chatbot-policy-procedure "#create-chatbot-policy-procedure")
- [Create an AI services opt-out
  policy](#create-ai-opt-out-policy-procedure "#create-ai-opt-out-policy-procedure")
- [Create a Security Hub policy](#create-security-hub-policy-procedure "#create-security-hub-policy-procedure")

## Create a service control policy (SCP)

###### Minimum permissions

To create SCPs, you need permission to run the following action:

- `organizations:CreatePolicy`

AWS Management Console

###### To create a service control policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Service control policies](https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy "https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy")** page, choose **Create
   policy**.
3. On the [**Create new service control policy**
   page](https://console.aws.amazon.com/organizations/home/policies/service-control/create "https://console.aws.amazon.com/organizations/home/policies/service-control/create"), enter a **Policy name** and an
   optional **Policy description**.
4. (Optional) Add one or more tags by choosing **Add
   tag** and then entering a key and an optional value.
   Leaving the value blank sets it to an empty string; it isn't
   `null`. You can attach up to 50 tags to a policy. For
   more information, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").

###### Note

In most of the steps that follow, we discuss using the
controls on the right side of the JSON editor to construct the
policy, element by element. Alternatively, you can, at any time,
simply enter text in the JSON editor on the left side of the
window. You can directly type, or use copy and paste. 5. To build the policy, your next steps vary depending on whether you
want to add a statement that [denies](orgs_manage_policies_scps_evaluation.md#how_scps_deny "orgs_manage_policies_scps_evaluation.md#how_scps_deny") or [allows](orgs_manage_policies_scps_evaluation.md#how_scps_allow "orgs_manage_policies_scps_evaluation.md#how_scps_allow")
access. For more information, see [SCP evaluation](orgs_manage_policies_scps_evaluation.md "orgs_manage_policies_scps_evaluation.md"). If you
use `Deny` statements, you have additional control
because you can restrict access to specific resources, define
conditions for when SCPs are in effect, and use the [NotAction](../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md "../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md") element. For details about syntax, see [SCP syntax](orgs_manage_policies_scps_syntax.md "orgs_manage_policies_scps_syntax.md").

To add a statement that _denies_ access:

    1. In the right **Edit statement** pane of
     the editor, under **Add actions**, choose
     an AWS service.


    As you choose options on the right, the JSON editor
     updates to show the corresponding JSON policy on
     left.
    2. After you select a service, a list opens that contains the
     available actions for that service. You can choose
     **All actions**, or choose one or more
     individual actions that you want to deny.


    The JSON on the left updates to include the actions you
     selected.


    ###### Note

    If you select an individual action and then also go
     back and also select **All actions**,
     the expected entry for
     ``servicename`:*`
     is added to the JSON, but the individual actions that
     you previously selected are left in the JSON and not
     removed.
    3. If you want to add actions from additional services, you
     can choose **All services** at the top of
     the **Statement** box, and then repeat the
     previous two steps as needed.
    4. Specify resources to include in the statement.




    	* Next to **Add a resource**,
    	 choose **Add**.
    	* In the **Add resource** dialog,
    	 choose the service whose resources you want to
    	 control from the list. You can select from among
    	 only those services you selected in the previous
    	 step.
    	* Under **Resource type**, choose
    	 the type of resource you want to control.
    	* Finally, complete the Amazon Resource Name (ARN)
    	 in **Resource ARN** to identify the
    	 specific resource to which you want to control
    	 access. You must replace all placeholders that are
    	 surrounded by curly braces `{}`. You can
    	 specify wild cards (`*`) where that
    	 resource type's ARN syntax permits. See the
    	 documentation for a specific resource type for
    	 information about where you can use wild
    	 cards.
    	* Save your addition to the policy by choosing
    	 **Add resource**. The
    	 `Resource` element in the JSON reflects
    	 your additions or changes. The
    	 **Resource** element is required.
    ###### Tip

    If you want to specify all resources for the selected
     service, either choose the **All
     resources** option in the list, or edit the
     `Resource` statement directly in the JSON
     to read `"Resource":"*"`.
    5. (Optional) To specify conditions that limit when a policy
     statement is in effect, next to **Add
     condition**, choose **Add**.




    	* **Condition key** – From
    	 the list you can choose any condition key that is
    	 available for all AWS services (for example,
    	 `aws:SourceIp`) or a service-specific
    	 key for only one of the services that you selected
    	 for this statement.
    	* **Qualifier** – (Optional)
    	 When the request has more than one values for a
    	 multivalued context key, you can specify a [qualifier](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md") for testing requests against
    	 the values. For more information see, [Single-valued vs. multivalued context
    	 keys](reference_policies_condition-single-vs-multi-valued-context-keys.md "reference_policies_condition-single-vs-multi-valued-context-keys.md") in the *IAM User
    	 Guide*. To check if a request can have
    	 multiple values, see the [Actions, resources, and condition keys for
    	 AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") in the *Service
    	 Authorization Reference*.




    		+ **Default** – Tests
    		 a single value in the request against the
    		 condition key value in the policy. The condition
    		 returns true if the value in the request matches
    		 the value in the policy. If the policy specifies
    		 more than one value then they are treated as an
    		 "or" test, and the condition returns true if the
    		 request values matches any of the policy
    		 values.
    		+ **For any value in a
    		 request** – When the request can
    		 have multiple values, this option tests whether
    		 *at least one* of
    		 the request values matches at least one of the
    		 condition key values in the policy. The condition
    		 returns true if any one of the key values in the
    		 request matches any one of the condition values in
    		 the policy. For no matching key or a null dataset,
    		 the condition returns false.
    		+ **For all values in a
    		 request** – When the request can
    		 have multiple values, this option tests whether
    		 *every* request
    		 value matches a condition key value in the policy.
    		 The condition returns true if every key value in
    		 the request matches at least one value in the
    		 policy. It also returns true if there are no keys
    		 in the request, or if the key values resolve to a
    		 null data set, such as an empty string.
    	* **Operator** – The [operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") specifies the type of comparison
    	 to make. The options that are presented depend on
    	 the data type of the condition key. For example, the
    	 `aws:CurrentTime` global condition key
    	 lets you pick from any of the date comparison
    	 operators, or `Null`, which you can use
    	 to test whether the value is present in the
    	 request.


    	For any condition operator except the
    	 `Null` test, you can choose the [IfExists](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IfExists "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IfExists") option.
    	* **Value** – (Optional)
    	 Specify one or more values for which you want to
    	 test the request.
    Choose **Add condition**.


    For more information about condition keys, see [IAM JSON Policy Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the
     *IAM User Guide*.

6. To add a statement that _allows_ access:
   1. In the JSON editor on the left, change the line
      `"Effect": "Deny"` to `"Effect":
"Allow"`.

   As you choose options on the right, the JSON editor
   updates to show the corresponding JSON policy on the
   left. 2. After you select a service, a list opens that contains the
   available actions for that service. You can choose
   **All actions**, or choose one or more
   individual actions that you want to allow.

   The JSON on the left updates to include the actions you
   selected.

   ###### Note

   If you select an individual action and then also go
   back and also select **All actions**,
   the expected entry for
   ``servicename`:\*`
   is added to the JSON, but the individual actions that
   you previously selected are left in the JSON and not
   removed. 3. If you want to add actions from additional services, you
   can choose **All services** at the top of
   the **Statement** box, and then repeat the
   previous two steps as needed.

7. (Optional) To add another statement to the policy, choose
   **Add statement** and use the visual editor to
   build the next statement.
8. When you're finished adding statements, choose **Create
   policy** to save the completed SCP.

Your new SCP appears in the list of the organization's policies. You can
now [attach your SCP to the root, OUs,
or accounts](orgs_policies_attach.md "orgs_policies_attach.md").

AWS CLI & AWS SDKs

###### To create a service control policy

You can use one of the following commands to create an SCP:

- AWS CLI: [create-policy](../../../cli/latest/reference/organizations/create-policy.md "../../../cli/latest/reference/organizations/create-policy.md")

The following example assumes that you have a file named
`Deny-IAM.json` with the JSON policy text in
it. It uses that file to create a new service control policy.

```
`$` **aws organizations create-policy \
 --content file://Deny-IAM.json \
 --description "Deny all IAM actions" \
 --name DenyIAMSCP \
 --type SERVICE\_CONTROL\_POLICY**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/service_control_policy/p-i9j8k7l6m5",
 "Name": "DenyIAMSCP",
 "Description": "Deny all IAM actions",
 "Type": "SERVICE_CONTROL_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"Version\":\"2012-10-17\", \"Statement\":[{\"Sid\":\"Statement1\",\"Effect\":\"Deny\",\"Action\":[\"iam:*\"],\"Resource\":[\"*\"]}]}"
 }
}`
```

- AWS SDKs: [CreatePolicy](../APIReference/API_CreatePolicy.md "../APIReference/API_CreatePolicy.md")

###### Note

SCPs don't take effect on the management account and in a few other situations.
For more information, see [Tasks and entities not restricted by
SCPs](orgs_manage_policies_scps.md#not-restricted-by-scp "orgs_manage_policies_scps.md#not-restricted-by-scp").

## Create a resource control policy (RCP)

###### Minimum permissions

To create RCPs, you need permission to run the following action:

- `organizations:CreatePolicy`

AWS Management Console

###### To create a resource control policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **Resource control policy** page, choose
   **Create policy**.
3. On the [**Create new resource control policy**
   page](https://console.aws.amazon.com/organizations/home/policies/service-control/create "https://console.aws.amazon.com/organizations/home/policies/service-control/create"), enter a **Policy name** and an
   optional **Policy description**.
4. (Optional) Add one or more tags by choosing **Add
   tag** and then entering a key and an optional value.
   Leaving the value blank sets it to an empty string; it isn't
   `null`. You can attach up to 50 tags to a policy. For
   more information, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").

###### Note

In most of the steps that follow, we discuss using the
controls on the right side of the JSON editor to construct the
policy, element by element. Alternatively, you can, at any time,
simply enter text in the JSON editor on the left side of the
window. You can directly type, or use copy and paste. 5. To add a statement:

    1. In the right **Edit statement** pane of
     the editor, under **Add actions**, choose
     an AWS service.


    As you choose options on the right, the JSON editor
     updates to show the corresponding JSON policy on
     left.
    2. After you select a service, a list opens that contains the
     available actions for that service. You can choose
     **All actions**, or choose one or more
     individual actions that you want to deny.


    The JSON on the left updates to include the actions you
     selected.


    ###### Note

    If you select an individual action and then also go
     back and also select **All actions**,
     the expected entry for
     ``servicename`:*`
     is added to the JSON, but the individual actions that
     you previously selected are left in the JSON and not
     removed.
    3. If you want to add actions from additional services, you
     can choose **All services** at the top of
     the **Statement** box, and then repeat the
     previous two steps as needed.
    4. Specify resources to include in the statement.




    	* Next to **Add a resource**,
    	 choose **Add**.
    	* In the **Add resource** dialog,
    	 choose the service whose resources you want to
    	 control from the list. You can select from among
    	 only those services you selected in the previous
    	 step.
    	* Under **Resource type**, choose
    	 the type of resource you want to control.
    	* Complete the Amazon Resource Name (ARN) in
    	 **Resource ARN** to identify the
    	 specific resource to which you want to control
    	 access. You must replace all placeholders that are
    	 surrounded by curly braces `{}`. You can
    	 specify wild cards (`*`) where that
    	 resource type's ARN syntax permits. See the [documentation](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md#reference_policies_elements_resource_wildcards "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md#reference_policies_elements_resource_wildcards") for a specific resource
    	 type for information about where you can use wild
    	 cards.
    	* Save your addition to the policy by choosing
    	 **Add resource**. The
    	 `Resource` element in the JSON reflects
    	 your additions or changes. The
    	 **Resource** element is required.
    ###### Tip

    If you want to specify all resources for the selected
     service, either choose the **All
     resources** option in the list, or edit the
     `Resource` statement directly in the JSON
     to read `"Resource":"*"`.
    5. (Optional) To specify conditions that limit when a policy
     statement is in effect, next to **Add
     condition**, choose **Add**.




    	* **Condition key** – From
    	 the list you can choose any condition key that is
    	 available for all AWS services (for example,
    	 `aws:SourceIp`) or a service-specific
    	 key for only one of the services that you selected
    	 for this statement.
    	* **Qualifier** – (Optional)
    	 When the request has more than one values for a
    	 multivalued context key, you can specify a [qualifier](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md") for testing requests against
    	 the values. For more information see, [Single-valued vs. multivalued context
    	 keys](../../../IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.md") in the *IAM User
    	 Guide*. To check if a request can have
    	 multiple values, see the [Actions, resources, and condition keys for
    	 AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") in the *Service
    	 Authorization Reference*.




    		+ **Default** – Tests
    		 a single value in the request against the
    		 condition key value in the policy. The condition
    		 returns true if the value in the request matches
    		 the value in the policy. If the policy specifies
    		 more than one value then they are treated as an
    		 "or" test, and the condition returns true if the
    		 request values matches any of the policy
    		 values.
    		+ **For any value in a
    		 request** – When the request can
    		 have multiple values, this option tests whether
    		 *at least one* of
    		 the request values matches at least one of the
    		 condition key values in the policy. The condition
    		 returns true if any one of the key values in the
    		 request matches any one of the condition values in
    		 the policy. For no matching key or a null dataset,
    		 the condition returns false.
    		+ **For all values in a
    		 request** – When the request can
    		 have multiple values, this option tests whether
    		 *every* request
    		 value matches a condition key value in the policy.
    		 The condition returns true if every key value in
    		 the request matches at least one value in the
    		 policy. It also returns true if there are no keys
    		 in the request, or if the key values resolve to a
    		 null data set, such as an empty string.
    	* **Operator** – The [operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") specifies the type of comparison
    	 to make. The options that are presented depend on
    	 the data type of the condition key. For example, the
    	 `aws:CurrentTime` global condition key
    	 lets you pick from any of the date comparison
    	 operators, or `Null`, which you can use
    	 to test whether the value is present in the
    	 request.


    	For any condition operator except the
    	 `Null` test, you can choose the [IfExists](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IfExists "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IfExists") option.
    	* **Value** – (Optional)
    	 Specify one or more values for which you want to
    	 test the request.
    Choose **Add condition**.


    For more information about condition keys, see [IAM JSON Policy Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the
     *IAM User Guide*.
    6. (Optional) To use the `NotAction` element to
     deny access to all actions ***except*** those
     specified, replace `Action` in the left pane with
     `NotAction`, just after the `"Effect":
     "Deny",` element. For more information, see [IAM JSON Policy Elements: NotAction](../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md "../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md") in the
     *IAM User Guide*.

6. (Optional) To add another statement to the policy, choose
   **Add statement** and use the visual editor to
   build the next statement.
7. When you're finished adding statements, choose **Create
   policy** to save the completed RCP.

Your new RCP appears in the list of the organization's policies. You can
now [attach your RCP to the root, OUs,
or accounts](orgs_policies_attach.md "orgs_policies_attach.md").

AWS CLI & AWS SDKs

###### To create a resource control policy

You can use one of the following commands to create an RCP:

- AWS CLI: [create-policy](../../../cli/latest/reference/organizations/create-policy.md "../../../cli/latest/reference/organizations/create-policy.md")

The following example assumes that you have a file named
`Deny-IAM.json` with the JSON policy text in
it. It uses that file to create a new resource control
policy.

```
`$` **aws organizations create-policy \
 --content file://Deny-IAM.json \
 --description "Deny all IAM actions" \
 --name DenyIAMRCP \
 --type RESOURCE\_CONTROL\_POLICY**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/resource_control_policy/p-i9j8k7l6m5",
 "Name": "DenyIAMRCP",
 "Description": "Deny all IAM actions",
 "Type": "RESOURCE_CONTROL_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"Version\":\"2012-10-17\", \"Statement\":[{\"Sid\":\"Statement1\",\"Effect\":\"Deny\",\"Action\":[\"iam:*\"],\"Resource\":[\"*\"]}]}"
 }
}`
```

- AWS SDKs: [CreatePolicy](../APIReference/API_CreatePolicy.md "../APIReference/API_CreatePolicy.md")

###### Note

RCPs don't take effect on the management account and in a few other situations.
For more information, see [Resources and entities not restricted by
RCPs](orgs_manage_policies_rcps.md#actions-not-restricted-by-rcps "orgs_manage_policies_rcps.md#actions-not-restricted-by-rcps").

## Create a declarative

policy

###### Minimum permissions

To create a declarative policy, you need permission to run the following
action:

- `organizations:CreatePolicy`

AWS Management Console

###### To create a declarative policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Declarative policies](https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2 "https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2")** page, choose
   **Create policy**.
3. On the [**Create new declarative policy for EC2**
   page](https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2/create "https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2/create"), enter a **Policy name** and an
   optional **Policy description**.
4. (Optional) You can add one or more tags to the policy by choosing
   **Add tag** and then entering a key and an
   optional value. Leaving the value blank sets it to an empty string;
   it isn't `null`. You can attach up to 50 tags to a
   policy. For more information, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").
5. You can build the policy using the **Visual
   editor** as described in this procedure. You can also
   enter or paste policy text in the **JSON** tab. For
   information about declarative policy syntax, see [Declarative policy syntax and
   examples](orgs_manage_policies_declarative_syntax.md "orgs_manage_policies_declarative_syntax.md").

If you choose to use the **Visual editor**,
select the service attribute you want to include in your declarative
policy. For more information, see [Supported
AWS services and attributes](orgs_manage_policies_declarative.md#orgs_manage_policies_declarative-supported-controls "orgs_manage_policies_declarative.md#orgs_manage_policies_declarative-supported-controls"). 6. Choose **Add service attribute**, and configure
the attribute to your specifications. For more detailed information
on the each effect, see [Declarative policy syntax and
examples](orgs_manage_policies_declarative_syntax.md "orgs_manage_policies_declarative_syntax.md"). 7. When you're finished editing your policy, choose **Create
policy** at the lower-right corner of the page.

AWS CLI & AWS SDKs

###### To create a declarative policy

You can use one of the following to create a declarative
policy:

- AWS CLI: [create-policy](../../../cli/latest/reference/organizations/create-policy.md "../../../cli/latest/reference/organizations/create-policy.md")
  1.  Create a declarative policy like the following, and store
      it in a text file.

  ```
  {
      "ec2_attributes": {
          "image_block_public_access": {
              "state": {
                  "@@assign": "block_new_sharing"
              }
          }
      }
  }
  ```

  This declarative policy specifies that all accounts
  affected by the policy are must be configured so that new
  Amazon Machine Images (AMIs) are not publicly sharable. For
  information about declarative policy syntax, see [Declarative policy syntax and
  examples](orgs_manage_policies_declarative_syntax.md "orgs_manage_policies_declarative_syntax.md"). 2. Import the JSON policy file to create a new policy in the
  organization. In this example, the previous JSON file was
  named `policy.json`.

  ```
  `$` **aws organizations create-policy \
   --type DECLARATIVE\_POLICY\_EC2 \
   --name "`MyTestPolicy`" \
   --description "`My test policy`" \
   --content file://`policy.json`**`{
   "Policy": {
   "Content": "{"ec2_attributes":{"image_block_public_access":{"state":{"@@assign":"block_new_sharing"}}}}".
   "PolicySummary": {
   "Id": "p-i9j8k7l6m5"
   "Arn": "arn:aws:organizations::o-aa111bb222:policy/declarative_policy_ec2/p-i9j8k7l6m5",
   "Description": "My test policy",
   "Name": "MyTestPolicy",
   "Type": "DECLARATIVE_POLICY_EC2"
   }
   }
  }`
  ```

- AWS SDKs: [CreatePolicy](../APIReference/API_CreatePolicy.md "../APIReference/API_CreatePolicy.md")

###### What to do next

After you create a declarative policy, assess readiness using the [account status
report](orgs_manage_policies_declarative.md#orgs_manage_policies_declarative-account-status-report "orgs_manage_policies_declarative.md#orgs_manage_policies_declarative-account-status-report"). You can then enforce your baseline configurations. To do that,
you can [attach the policy](orgs_policies_attach.md "orgs_policies_attach.md") to the organization root, organizational units (OUs),
AWS accounts within your organization, or a combination of all of those.

## Create a backup policy

###### Minimum permissions

To create a backup policy, you need permission to run the following action:

- `organizations:CreatePolicy`

AWS Management Console
You can create a backup policy in the AWS Management Console in one of two ways:

- A visual editor that lets you choose options and generates the
  JSON policy text for you.
- A text editor that lets you directly create the JSON policy text
  yourself.

The visual editor makes the process easy, but it limits your flexibility.
It's a great way to create your first policies and get comfortable with
using them. After you understand how they work and have started to be
limited by what the visual editor provides, you can add advanced features to
your policies by editing the JSON policy text yourself. The visual editor
uses only the [@@assign value-setting
operator](policy-operators.md#value-setting-operators "policy-operators.md#value-setting-operators"), and it doesn't provide any access to the [child control operators](policy-operators.md#child-control-operators "policy-operators.md#child-control-operators"). You
can add the child control operators only if you manually edit the JSON
policy text.

###### To create a backup policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Backup policies](https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy "https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy")** page, choose **Create
   policy**.
3. On the **Create policy** page, enter a \***\*Policy name\*\*** and an
   optional **Policy description**.
4. (Optional) You can add one or more tags to the policy by choosing
   **Add tag** and then entering a key and an
   optional value. Leaving the value blank sets it to an empty string;
   it isn't `null`. You can attach up to 50 tags to a
   policy. For more information about tagging, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").
5. You can build the policy using the **Visual
   editor** as described in this procedure. You can also
   enter or paste policy text in the **JSON** tab. For
   information about backup policy syntax, see [Backup policy syntax and
   examples](orgs_manage_policies_backup_syntax.md "orgs_manage_policies_backup_syntax.md").

If you choose to use the **Visual editor**,
select the backup options appropriate for your scenario. A backup
plan consists of three parts. For more information about these
backup plan elements, see [Creating a backup plan](../../../aws-backup/latest/devguide/creating-a-backup-plan.md "../../../aws-backup/latest/devguide/creating-a-backup-plan.md") and [Assigning resources](../../../aws-backup/latest/devguide/assigning-resources.md "../../../aws-backup/latest/devguide/assigning-resources.md") in the _AWS Backup Developer Guide_.

    1. Backup plan general details




    	* The **Backup plan name** can
    	 consist of only alphanumeric, hyphen, and underline
    	 characters.
    	* You must select at least one **Backup plan
    	 region** from the list. The plan can back
    	 up resources in only the selected
    	 AWS Regions.
    2. One or more backup rules that specify how and when AWS Backup
     is to operate. Each backup rule defines the following
     items:




    	* A schedule that includes the frequency of the
    	 backup and the time window in which the backup can
    	 occur.
    	* The name of the backup vault to use. The
    	 **Backup vault name** can consist
    	 of only alphanumeric, hyphen, and underline
    	 characters. The backup vault must exist before the
    	 plan can successfully run. Create the vault using
    	 the AWS Backup console or AWS CLI commands.
    	* (Optional) One or more **Copy to
    	 region** rules to also copy the backup to
    	 vaults in other AWS Regions.
    	* One or more tag key and value pairs to attach to
    	 the backup recovery points created each time this
    	 backup plan runs.
    	* Lifecycle options that specify when the backup
    	 transitions to cold storage, and when the backup
    	 expires.
    Choose **Add rule** to add each rule you
     need to the plan.


    For more information about backup rules, see [Backup Rules](../../../aws-backup/latest/devguide/creating-a-backup-plan.md#backup-rules "../../../aws-backup/latest/devguide/creating-a-backup-plan.md#backup-rules") in the *AWS Backup Developer Guide*.
    3. A resource assignment that specifies which resources that
     AWS Backup should backup with this plan. The assignment is made
     by specifying tag pairs that AWS Backup uses to find and match
     resources




    	* The **Resource assignment name**
    	 can consist of only alphanumeric, hyphen, and
    	 underline characters.
    	* Specify the **IAM role** for
    	 AWS Backup to use to perform the backup by its name.


    	In the console, you don't specify the entire
    	 Amazon Resource Name (ARN). You must include both
    	 the role name and its prefix that specifies the type
    	 of role. The prefixes are typically
    	 `role` or `service-role` ,
    	 and they are separated from the role name by a
    	 forward slash ('/'). For example, you might enter
    	 `role/MyRoleName` or
    	 `service-role/MyManagedRoleName`. This
    	 is converted to a full ARN for you when stored in
    	 the underlying JSON.


    	###### Important

    	The specified IAM role must already exist in
    	 the account the policy is applied to. If it does
    	 not, the backup plan might successfully start
    	 backup jobs, but those backup jobs will
    	 fail.
    	* Specify one or more **Resource tag
    	 key** and **Tag values**
    	 pairs to identify resources that you want backed up.
    	 If there is more than one tag value, separate the
    	 values with commas.
    Choose **Add assignment** to add each
     configured resource assignment to the backup plan.


    For more information, see [Assign Resources to a Backup
     Plan](../../../aws-backup/latest/devguide/create-a-scheduled-backup.md#assign-resources-to-plan "../../../aws-backup/latest/devguide/create-a-scheduled-backup.md#assign-resources-to-plan") in the *AWS Backup Developer Guide*.

6. When you're finished creating your policy, choose **Create
   policy**. The policy appears in your list of available
   backup policies.

AWS CLI & AWS SDKs

###### To create a backup policy

You can use one of the following to create a backup policy:

- AWS CLI: [create-policy](../../../cli/latest/reference/organizations/create-policy.md "../../../cli/latest/reference/organizations/create-policy.md")

Create a backup plan as JSON text similar to the following, and
store it in a text file. For complete rules for the syntax, see
[Backup policy syntax and
examples](orgs_manage_policies_backup_syntax.md "orgs_manage_policies_backup_syntax.md").

```
{
    "plans": {
        "PII_Backup_Plan": {
            "regions": { "@@assign": [ "ap-northeast-2", "us-east-1", "eu-north-1" ] },
            "rules": {
                "Hourly": {
                    "schedule_expression": { "@@assign": "cron(0 5/1 ? * * *)" },
                    "start_backup_window_minutes": { "@@assign": "480" },
                    "complete_backup_window_minutes": { "@@assign": "10080" },
                    "lifecycle": {
                        "move_to_cold_storage_after_days": { "@@assign": "180" },
                        "delete_after_days": { "@@assign": "270" }
                    },
                    "target_backup_vault_name": { "@@assign": "FortKnox" },
                    "copy_actions": {
                        "arn:aws:backup:us-east-1:$account:backup-vault:secondary-vault": {
                            "lifecycle": {
                                "move_to_cold_storage_after_days": { "@@assign": "10" },
                                "delete_after_days": { "@@assign": "100" }
                            }
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "datatype": {
                        "iam_role_arn": { "@@assign": "arn:aws:iam::$account:role/MyIamRole" },
                        "tag_key": { "@@assign": "dataType" },
                        "tag_value": { "@@assign": [ "PII" ] }
                    }
                }
            }
        }
    }
}
```

This backup plan specifies that AWS Backup should back up all
resources in the affected AWS accounts that are in the specified
AWS Regions and that have the tag `dataType` with a
value of `PII`.

Next, import the JSON policy file backup plan to create a new
backup policy in the organization. Note the policy ID at the end of
the policy ARN in the output.

```
`$` **aws organizations create-policy \
 --name "MyBackupPolicy" \
 --type BACKUP\_POLICY \
 --description "My backup policy" \
 --content file://policy.json**`{
 "Policy": {
 "PolicySummary": {
 "Arn": "arn:aws:organizations::o-aa111bb222:policy/backup_policy/p-i9j8k7l6m5",
 "Description": "My backup policy",
 "Name": "MyBackupPolicy",
 "Type": "BACKUP_POLICY"
 }
 "Content": "`...a condensed version of the JSON policy document you provided in the file...`",
 }
}`
```

- AWS SDKs: [CreatePolicy](../APIReference/API_CreatePolicy.md "../APIReference/API_CreatePolicy.md")

## Create a tag policy

###### Minimum permissions

To create tag policies, you need permission to run the following action:

- `organizations:CreatePolicy`

You can create a tag policy in the AWS Management Console in one of two ways:

- A visual editor that lets you choose options and generates the JSON policy
  text for you.
- A text editor that lets you directly create the JSON policy text yourself.

The visual editor makes the process easy, but it limits your flexibility. It's a great
way to create your first policies and get comfortable with using them. After you
understand how they work and have started to be limited by what the visual editor
provides, you can add advanced features to your policies by editing the JSON policy text
yourself. The visual editor uses only the [@@assign value-setting operator](policy-operators.md#value-setting-operators "policy-operators.md#value-setting-operators"), and it doesn't provide any access to the
[child control operators](policy-operators.md#child-control-operators "policy-operators.md#child-control-operators"). You can add
the child control operators only if you manually edit the JSON policy text.

AWS Management Console
You can create a tag policy in the AWS Management Console in one of two ways:

- A visual editor that lets you choose options and generates the
  JSON policy text for you.
- A text editor that lets you directly create the JSON policy text
  yourself.

The visual editor makes the process easy, but it limits your flexibility.
It's a great way to create your first policies and get comfortable with
using them. After you understand how they work and have started to be
limited by what the visual editor provides, you can add advanced features to
your policies by editing the JSON policy text yourself. The visual editor
uses only the [@@assign value-setting
operator](policy-operators.md#value-setting-operators "policy-operators.md#value-setting-operators"), and it doesn't provide any access to the [child control operators](policy-operators.md#child-control-operators "policy-operators.md#child-control-operators"). You
can add the child control operators only if you manually edit the JSON
policy text.

###### To create a tag policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Tag policies](https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy "https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy")** page, choose **Create
   policy**.
3. On the **Create policy** page, enter a \***\*Policy name\*\*** and an
   optional **Policy description**.
4. (Optional) You can add one or more tags to the policy object
   itself. These tags are not part of the policy. To do this, choose
   **Add tag** and then enter a key and an
   optional value. Leaving the value blank sets it to an empty string;
   it isn't `null`. You can attach up to 50 tags to a
   policy. For more information, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").
5. You can build the tag policy using the **Visual
   editor** as described in this procedure. You can also
   type or paste a tag policy in the **JSON** tab. For
   information about tag policy syntax, see [Tag policy syntax](orgs_manage_policies_example-tag-policies.md#tag-policy-syntax-reference "orgs_manage_policies_example-tag-policies.md#tag-policy-syntax-reference").

If you choose to use the **Visual editor**,
specify the following: 6. For **New tag key 1**, specify the name of a tag
key to add. 7. For **Compliance Options** you can select the
following options:

    1. **Use the
     capitalization that you've specified above for the tag
     key** — leave this option cleared (the
     default) to specify that the inherited parent tag policy, if
     any exists, should define the case treatment for the tag
     key.


    Enable this option if you want to mandate a specific
     capitalization for the tag key using this policy. If you
     select this option, the capitalization you specified for
     **Tag Key** overrides the case
     treatment specified in an inherited parent policy.


    If a parent policy doesn't exist and you don't enable this
     option, only tag keys in all lowercase characters are
     considered compliant. For more information about inheritance
     from parent policies, see [Understanding management policy
     inheritance](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md").


    ###### Tip

    Consider using the example tag policy shown in [Example 1: Define organization-wide tag
     key case](orgs_manage_policies_example-tag-policies.md#tag-policy-example-key-case "orgs_manage_policies_example-tag-policies.md#tag-policy-example-key-case") as a guide
     in creating a tag policy that define tag keys and their
     case treatment. Attach it to the organization root.
     Later, you can create and attach additional tag policies
     to OUs or accounts to create additional tagging rules.
    2. **Specify allowed
     values for this tag key** — enable this
     option if you want to add allowed values for this tag key to
     any values inherited from a parent policy.


    By default, this option is cleared, which means that only
     those values defined in and inherited from a parent policy
     are considered compliant. If a parent policy doesn't exist
     and you don't specify tag values then any value (including
     no value at all) is considered compliant.


    To update the list of acceptable tag values, select
     **Specify allowed values for this tag
     key** and then choose **Specify
     values**. When prompted, enter the new values
     (one value per box), and then choose **Save
     changes**.

8. For
   **Resource types to enforce**, you can select
   **Prevent noncompliant operations for this
   tag**.

We recommend that you leave this option cleared (the default)
unless you are experienced with using tag policies. Make sure that
you have reviewed the recommendations in [Understanding
enforcement](orgs_manage_policies_tag-policies-enforcement.md "orgs_manage_policies_tag-policies-enforcement.md"),
and test thoroughly. Otherwise, you could prevent users in your
organization's accounts from tagging the resources they need.

If you do want to enforce compliance with this tag key, select the
check box and then **Specify resource types**. When
prompted, select the resource types to include in the policy. Then
choose **Save changes**.

###### Important

When you select this option, any operations that manipulate
tags for resources of the specified types succeed only if the
operation results in tags that are compliant with the
policy. 9. (Optional) To add another tag key to this tag policy, choose
**Add tag key**. Then perform steps 6–9
to define the tag key. 10. When you're finished building your tag policy, choose
**Save changes**.

AWS CLI & AWS SDKs

###### To create a tag policy

You can use one of the following to create a tag policy:

- AWS CLI: [create-policy](../../../cli/latest/reference/organizations/create-policy.md "../../../cli/latest/reference/organizations/create-policy.md")

You can use any text editor to create a tag policy. Use JSON
syntax and save the tag policy as a file with any name and extension
in a location of your choosing. Tag policies can have a maximum of
2,500 characters, including spaces. For information about tag policy
syntax, see [Tag policy syntax](orgs_manage_policies_example-tag-policies.md#tag-policy-syntax-reference "orgs_manage_policies_example-tag-policies.md#tag-policy-syntax-reference").

###### To create a tag policy

    1. Create a tag policy in a text file that looks similar to
     the following:


    Contents of `testpolicy.json`:



    ```
    {
        "tags": {
            "CostCenter": {
                "tag_key": {
                    "@@assign": "CostCenter"
                }
            }
        }
    }
    ```

    This tag policy defines the `CostCenter` tag
     key. The tag can accept any value or no value. A policy like
     this means that a resource that has the CostCenter tag
     attached with or without a value is compliant.
    2. Create a policy that contains the policy content from the
     file. Extra white space in the output has been truncated for
     readability.



    ```
    `$` **aws organizations create-policy \
     --name "MyTestTagPolicy" \
     --description "My Test policy" \
     --content file://testpolicy.json \
     --type TAG\_POLICY**`{
     "Policy": {
     "PolicySummary": {
     "Id": "p-a1b2c3d4e5",
     "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/tag_policy/p-a1b2c3d4e5",
     "Name": "MyTestTagPolicy",
     "Description": "My Test policy",
     "Type": "TAG_POLICY",
     "AwsManaged": false
     },
     "Content": "{\n\"tags\":{\n\"CostCenter\":{\n\"tag_key\":{\n\"@@assign\":\"CostCenter\"\n}\n}\n}\n}\n\n"
     }
    }`
    ```

- AWS SDKs: [CreatePolicy](../APIReference/API_CreatePolicy.md "../APIReference/API_CreatePolicy.md")

## Create a chat applications

policy

###### Minimum permissions

To create a chat applications policy, you need permission to run the following
action:

- `organizations:CreatePolicy`

AWS Management Console
You can create a chat applications policy in the AWS Management Console in one of two
ways:

- A visual editor that lets you choose options and generates the
  JSON policy text for you.
- A text editor that lets you directly create the JSON policy text
  yourself.

The visual editor makes the process easy, but it limits your flexibility.
It's a great way to create your first policies and get comfortable with
using them. After you understand how they work and have started to be
limited by what the visual editor provides, you can add advanced features to
your policies by editing the JSON policy text yourself. The visual editor
uses only the [@@assign value-setting
operator](policy-operators.md#value-setting-operators "policy-operators.md#value-setting-operators"), and it doesn't provide any access to the [child control operators](policy-operators.md#child-control-operators "policy-operators.md#child-control-operators"). You
can add the child control operators only if you manually edit the JSON
policy text.

###### To create a chat applications policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Chatbot policies](https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy "https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy")** page, choose **Create
   policy**.
3. On the [**Create new chat applications policy**
   page](https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy/create "https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy/create"), enter a **Policy name** and an
   optional **Policy description**.
4. (Optional) You can add one or more tags to the policy by choosing
   **Add tag** and then entering a key and an
   optional value. Leaving the value blank sets it to an empty string;
   it isn't `null`. You can attach up to 50 tags to a
   policy. For more information, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").
5. You can build the policy using the **Visual
   editor** as described in this procedure. You can also
   enter or paste policy text in the **JSON** tab. For
   information about chat applications policy syntax, see [Chat applications policy syntax and
   examples](orgs_manage_policies_chatbot_syntax.md "orgs_manage_policies_chatbot_syntax.md").

If you choose to use the **Visual editor**,
configure your chat applications policy by specifying access
controls for chat clients.

    1. Choose one of the following for **Set Amazon Chime chat
     client access**




    	* Deny chime access.
    	* Allow Chime access.
    2. Choose on the following for **Set Microsoft Teams
     chat client access**




    	* Deny access to all Teams
    	* Allow access to all Teams
    	* Restrict access to named Teams
    3. Choose one of the following for **Set Slack chat
     client access**




    	* Deny access to all Slack workspaces
    	* Allow access to all Slack workspaces
    	* Restrict access to named Slack worksapces
    ###### Note

    In addition, you can select **Limit
     Amazon Q Developer in chat applications usage to only
     private Slack channels**.
    4. Select the following options for **Set IAM
     permissions types**




    	* **Enable Channel level IAM
    	 role** — All channel members
    	 share IAM role permissions to run tasks in a
    	 channel. A channel role is appropriate if channel
    	 members require the same permissions.
    	* **Enable User level IAM
    	 role** — Channel members must
    	 choose an IAM user role to perform actions
    	 (Requires Console access to choose roles). User
    	 roles are apporopriate if channel members require
    	 different permissions and can choose their user
    	 roles.

6. When you're finished creating your policy, choose **Create
   policy**. The policy appears in your list of chatbot
   backup policies.

AWS CLI & AWS SDKs

###### To create a chat applications policy

You can use one of the following to create a chat applications
policy:

- AWS CLI: [create-policy](../../../cli/latest/reference/organizations/create-policy.md "../../../cli/latest/reference/organizations/create-policy.md")

You can use any text editor to create a chat applications policy.
Use JSON syntax and save the chat applications policy as a file with
any name and extension in a location of your choosing. Chat
applications policies can have a maximum of ? characters, including
spaces. For information about tag policy syntax, see [Chat applications policy syntax and
examples](orgs_manage_policies_chatbot_syntax.md "orgs_manage_policies_chatbot_syntax.md").

###### To create a chat applications policy

    1. Create a chat applications policy in a text file that
     looks similar to the following:


    Contents of `testpolicy.json`:



    ```
    {
       "chatbot": {
          "platforms": {
             "slack": {
                "client": {
                   "@@assign": "enabled"
                },
                "workspaces": {
                   "@@assign": [
                      "`Slack-Workspace-Id`"
                   ]
                },
                "default": {
                   "supported_channel_types": {
                      "@@assign": [
                         "private"
                      ]
                   }
                }
             },
             "microsoft_teams": {
                "client": {
                   "@@assign": "disabled"
                }
             }
          }
       }
    }
    ```

    This chat applications policy allows only private Slack
     channels in a specific workspace, disables Microsoft Teams,
     and supports all [role settings](../../../chatbot/latest/adminguide/understanding-permissions.md#role-settings "../../../chatbot/latest/adminguide/understanding-permissions.md#role-settings").
    2. Create a policy that contains the policy content from the
     file. Extra white space in the output has been truncated for
     readability.



    ```
    `$` **aws organizations create-policy \
     --name "MyTestChatbotPolicy" \
     --description "My Test policy" \
     --content file://testpolicy.json \
     --type CHATBOT\_POLICY**`{
     "Policy": {
     "PolicySummary": {
     "Id": "p-a1b2c3d4e5",
     "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/chatbot_policy/p-a1b2c3d4e5",
     "Name": "MyTestChatApplicationsPolicy",
     "Description": "My Test policy",
     "Type": "CHATBOT_POLICY",
     "AwsManaged": false
     },
     "Content": "{"chatbot":{"platforms":{"slack":{"client":{"@@assign":"enabled"},"workspaces":{"@@assign":["`Slack-Workspace-Id`"]},"supported_channel_types":{"@@assign":["private"]}},"microsoft_teams":{"client":{"@@assign":"disabled"}}}}}"
     }
    }`
    ```

- AWS SDKs: [CreatePolicy](../APIReference/API_CreatePolicy.md "../APIReference/API_CreatePolicy.md")

## Create an AI services opt-out

policy

###### Minimum permissions

To create an AI services opt-out policy, you need permission to run the following
action:

- `organizations:CreatePolicy`

AWS Management Console

###### To create an AI services opt-out policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AI services opt-out policies](https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy "https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy")** page, choose **Create
   policy**.
3. On the [**Create new AI services opt-out policy**
   page](https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy/create "https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy/create"), enter a **Policy name** and an
   optional **Policy description**.
4. (Optional) You can add one or more tags to the policy by choosing
   **Add tag** and then entering a key and an
   optional value. Leaving the value blank sets it to an empty string;
   it isn't `null`. You can attach up to 50 tags to a
   policy. For more information, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").
5. Enter or paste the policy text in the **JSON**
   tab. For information about AI services opt-out policy syntax, see [AI services opt-out policy syntax and
   examples](orgs_manage_policies_ai-opt-out_syntax.md "orgs_manage_policies_ai-opt-out_syntax.md"). For example
   policies that you can use as a starting point, see [AI services opt-out policy examples](orgs_manage_policies_ai-opt-out_syntax.md#ai-opt-out-policy-examples "orgs_manage_policies_ai-opt-out_syntax.md#ai-opt-out-policy-examples").
6. When you're finished editing your policy, choose **Create
   policy** at the lower-right corner of the page.

AWS CLI & AWS SDKs

###### To create an AI services opt-out policy

You can use one of the following to create a tag policy:

- AWS CLI: [create-policy](../../../cli/latest/reference/organizations/create-policy.md "../../../cli/latest/reference/organizations/create-policy.md")
  1.  Create an AI services opt-out policy like the following, and
      store it in a text file. Note that "`optOut`" and
      "`optIn`" are case-sensitive.

  ```
  {
      "services": {
          "default": {
              "opt_out_policy": {
                  "@@assign": "optOut"
              }
          },
          "rekognition": {
              "opt_out_policy": {
                  "@@assign": "optIn"
              }
          }
      }
  }
  ```

  This AI services opt-out policy specifies that all accounts
  affected by the policy are opted out of all AI services
  except for Amazon Rekognition. 2. Import the JSON policy file to create a new policy in the
  organization. In this example, the previous JSON file was
  named `policy.json`.

  ```
  `$` **aws organizations create-policy \
   --type AISERVICES\_OPT\_OUT\_POLICY \
   --name "`MyTestPolicy`" \
   --description "`My test policy`" \
   --content file://`policy.json`**`{
   "Policy": {
   "Content": "{\"services\":{\"default\":{\"opt_out_policy\":{\"@@assign\":\"optOut\"}},\"rekognition\":{\"opt_out_policy\":{\"@@assign\":\"optIn\"}}}}",
   "PolicySummary": {
   "Id": "p-i9j8k7l6m5"
   "Arn": "arn:aws:organizations::o-aa111bb222:policy/aiservices_opt_out_policy/p-i9j8k7l6m5",
   "Description": "My test policy",
   "Name": "MyTestPolicy",
   "Type": "AISERVICES_OPT_OUT_POLICY"
   }
   }
  }`
  ```

- AWS SDKs: [CreatePolicy](../APIReference/API_CreatePolicy.md "../APIReference/API_CreatePolicy.md")

## Create a Security Hub policy

###### Minimum permissions

To create a Security Hub policy, you need permission to run the following action:

- `organizations:CreatePolicy`

AWS Management Console

###### To create a Security Hub policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Security Hub policies](https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy "https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy")** page, choose **Create
   policy**.
3. On the [**Create new Security Hub policy** page](https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy/create "https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy/create"),
   enter a **Policy name** and an optional
   **Policy description**.
4. (Optional) You can add one or more tags to the policy by choosing
   **Add tag** and then entering a key and an
   optional value. Leaving the value blank sets it to an empty string;
   it isn't `null`. You can attach up to 50 tags to a
   policy. For more information, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").
5. Enter or paste the policy text in the JSON code box. For
   information about the Security Hub policy syntax, see [Security Hub policy syntax and
   examples](orgs_manage_policies_security_hub_syntax.md "orgs_manage_policies_security_hub_syntax.md"). For
   example policies that you can use as a starting point, see [Security Hub policy examples](orgs_manage_policies_security_hub_syntax.md#security-hub-policy-examples "orgs_manage_policies_security_hub_syntax.md#security-hub-policy-examples").
6. When you're finished editing your policy, choose **Create
   policy** at the lower-right corner of the page.

AWS CLI & AWS SDKs

###### To create an Security Hub policy

You can use one of the following to create a Security Hub policy:

- AWS CLI: [create-policy](../../../cli/latest/reference/organizations/create-policy.md "../../../cli/latest/reference/organizations/create-policy.md")

**Example: Create a policy that enables Security Hub
in all supported Regions**

The following example assumes that you have a file named
`testPolicy_enableAllSupportedRegions.json`
with the JSON policy text in it. It uses that file to create a new
Security Hub policy.

```
`$` **aws organizations create-policy \
 --content file://./testPolicy\_enableAllSupportedRegions.json \
 --name "testPolicy\_enableAllSupportedRegions" \
 --description "Test policy to enable securityhub in ALL\_SUPPORTED Regions" \
 --type SECURITYHUB\_POLICY**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-66ev7hgcvj",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/securityhub_policy/p-66ev7hgcvj",
 "Name": "testPolicy_enableAllSupportedRegions",
 "Description": "Test policy to enable securityhub in ALL_SUPPORTED Regions",
 "Type": "SECURITYHUB_POLICY",
 "AwsManaged": false
 },
 "Content": "{\n \"securityhub\": {\n \"enable_in_regions\": {\n \"@@assign\":[\n \"ALL_SUPPORTED\"\n ]\n },\n \"disable_in_regions\": {\n \"@@assign\":[]\n }\n }\n}\n"
 }
}`
```

**Example: Create a policy that enables Security Hub
in all supported Regions but disable in the us-east-1
Region**

The following example assumes that you have a file named
`testPolicy_enableAllSupportedRegions_Disable_us-east-1.json`
with the JSON policy text in it. It uses that file to create a new
Security Hub policy.

```
`$` **aws organizations create-policy \
 --content file://./testPolicy\_enableAllSupportedRegions\_Disable\_us-east-1.json \
 --name "testPolicy\_enableAllSupportedRegions\_Disable\_us-east-1" \
 --description "Test policy to enable securityhub in ALL\_SUPPORTED Regions but disable in us-east-1 Region" \
 --type SECURITYHUB\_POLICY**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-66217dwpos",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/securityhub_policy/p-66217dwpos",
 "Name": "testPolicy_enableAllSupportedRegions_Disable_us-east-1",
 "Description": "Test policy to enable securityhub in ALL_SUPPORTED Regions but disable in us-east-1 Region",
 "Type": "SECURITYHUB_POLICY",
 "AwsManaged": false
 },
 "Content": "{\n \"securityhub\": {\n \"enable_in_regions\": {\n \"@@assign\":[\n \"ALL_SUPPORTED\"\n ]\n },\n \"disable_in_regions\": {\n \"@@assign\":[\n \"us-east-1\"\n ]\n }\n }\n}\n"
 }
}`
```

- AWS SDKs: [CreatePolicy](../APIReference/API_CreatePolicy.md "../APIReference/API_CreatePolicy.md")
