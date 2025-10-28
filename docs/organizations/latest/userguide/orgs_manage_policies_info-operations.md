# Getting information about your

organization's policies

This topic describes various ways to get details about the policies in your
organization. These procedures apply to _all_ policy types. You must
enable a policy type on the organization root before you can attach policies of that type to
any entities in that organization root.

###### Topics

- [Listing all policies](#list-all-pols-in-org "#list-all-pols-in-org")
- [Listing attached policies](#list-all-pols-in-entity "#list-all-pols-in-entity")
- [Listing all attachments](#list-all-entities-attached-to-pol "#list-all-entities-attached-to-pol")
- [Getting details about a policy](#get-details-about-pol "#get-details-about-pol")

## Listing all policies

###### Minimum permissions

To list the policies within your organization, you must have the following
permission:

- `organizations:ListPolicies`

You can view the policies in your organization in the AWS Management Console or by using an
AWS Command Line Interface (AWS CLI) command or an AWS SDK operation.

###### To list all of the policies in

your organization

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Policies](https://console.aws.amazon.com/organizations/v2/home/policies "https://console.aws.amazon.com/organizations/v2/home/policies")** page, choose the policy type that you want to
   list.

If the specified policy type is enabled, the console displays a
list of all of the policies of that type that are currently
available in the organization. 3. Return to the **[Policies](https://console.aws.amazon.com/organizations/v2/home/policies "https://console.aws.amazon.com/organizations/v2/home/policies")** page and repeat for each policy
type.

The following code examples show how to use `ListPolicies`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples").

```
    using System;
    using System.Threading.Tasks;
    using Amazon.Organizations;
    using Amazon.Organizations.Model;

    /// <summary>
    /// Shows how to list the AWS Organizations policies associated with an
    /// organization.
    /// </summary>
    public class ListPolicies
    {
        /// <summary>
        /// Initializes an Organizations client object, and then calls its
        /// ListPoliciesAsync method.
        /// </summary>
        public static async Task Main()
        {
            // Create the client object using the default account.
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            // The value for the Filter parameter is required and must must be
            // one of the following:
            //     AISERVICES_OPT_OUT_POLICY
            //     BACKUP_POLICY
            //     SERVICE_CONTROL_POLICY
            //     TAG_POLICY
            var request = new ListPoliciesRequest
            {
                Filter = "SERVICE_CONTROL_POLICY",
                MaxResults = 5,
            };

            var response = new ListPoliciesResponse();
            try
            {
                do
                {
                    response = await client.ListPoliciesAsync(request);
                    response.Policies.ForEach(p => DisplayPolicies(p));
                    if (response.NextToken is not null)
                    {
                        request.NextToken = response.NextToken;
                    }
                }
                while (response.NextToken is not null);
            }
            catch (AWSOrganizationsNotInUseException ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        /// <summary>
        /// Displays information about the Organizations policies associated
        /// with an organization.
        /// </summary>
        /// <param name="policy">An Organizations policy summary to display
        /// information on the console.</param>
        private static void DisplayPolicies(PolicySummary policy)
        {
            string policyInfo = $"{policy.Id} {policy.Name}\t{policy.Description}";

            Console.WriteLine(policyInfo);
        }
    }



```

- For API details, see
  [ListPolicies](../../../goto/DotNetSDKV3/organizations-2016-11-28/ListPolicies.md "../../../goto/DotNetSDKV3/organizations-2016-11-28/ListPolicies.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To retrieve a list of all policies in an organization of a certain type**

The following example shows you how to get a list of SCPs, as specified by the filter parameter:

```
`aws organizations list-policies --filter `SERVICE_CONTROL_POLICY``

```

The output includes a list of policies with summary information:

```
{
        "Policies": [
                {
                        "Type": "SERVICE_CONTROL_POLICY",
                        "Name": "AllowAllS3Actions",
                        "AwsManaged": false,
                        "Id": "p-examplepolicyid111",
                        "Arn": "arn:aws:organizations::111111111111:policy/service_control_policy/p-examplepolicyid111",
                        "Description": "Enables account admins to delegate permissions for any S3 actions to users and roles in their accounts."
                },
                {
                        "Type": "SERVICE_CONTROL_POLICY",
                        "Name": "AllowAllEC2Actions",
                        "AwsManaged": false,
                        "Id": "p-examplepolicyid222",
                        "Arn": "arn:aws:organizations::111111111111:policy/service_control_policy/p-examplepolicyid222",
                        "Description": "Enables account admins to delegate permissions for any EC2 actions to users and roles in their accounts."
                },
                {
                        "AwsManaged": true,
                        "Description": "Allows access to every operation",
                        "Type": "SERVICE_CONTROL_POLICY",
                        "Id": "p-FullAWSAccess",
                        "Arn": "arn:aws:organizations::aws:policy/service_control_policy/p-FullAWSAccess",
                        "Name": "FullAWSAccess"
                }
        ]
}
```

- For API details, see
  [ListPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-policies.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-policies.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples").

```
def list_policies(policy_filter, orgs_client):
    """
    Lists the policies for the account, limited to the specified filter.

    :param policy_filter: The kind of policies to return.
    :param orgs_client: The Boto3 Organizations client.
    :return: The list of policies found.
    """
    try:
        response = orgs_client.list_policies(Filter=policy_filter)
        policies = response["Policies"]
        logger.info("Found %s %s policies.", len(policies), policy_filter)
    except ClientError:
        logger.exception("Couldn't get %s policies.", policy_filter)
        raise
    else:
        return policies




```

- For API details, see
  [ListPolicies](../../../goto/boto3/organizations-2016-11-28/ListPolicies.md "../../../goto/boto3/organizations-2016-11-28/ListPolicies.md")
  in _AWS SDK for Python (Boto3) API Reference_.

## Listing the policies attached to a root, OU,

or account

###### Minimum permissions

To list the policies that are attached to a root, organizational unit (OU), or
account within your organization, you must have the following permission:

- `organizations:ListPoliciesForTarget` with a
  `Resource` element in the same policy statement that includes
  the Amazon Resource Name (ARN) of the specified target (or "\*")

AWS Management Console

###### To list all policies that are attached directly to a specified root,

OU, or account

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, choose the name of the root, OU, or account
   whose policies you want to view. You might have to expand OUs (choose the
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   ) to find the OU that you want.
3. On the Root, OU, or account page, choose the
   **Policies** tab.

The **Policies** tab displays all of the policies
attached to that root, OU, or account, grouped by policy
type.

AWS CLI & AWS SDKs

###### To list all policies that are attached directly to a specified root,

OU, or account

You can use one of the following commands to list policies that are
attached to an entity:

- AWS CLI: [list-policies-for-target](../../../cli/latest/reference/organizations/list-policies-for-target.md "../../../cli/latest/reference/organizations/list-policies-for-target.md")

The following example lists all of the service control policies
attached to the specified OU. You must specify both the ID of the
root, OU, or account, and the type of policy that you want to
list.

```
`$` **aws organizations list-policies-for-target \
 --target-id ou-a1b2-f6g7h222 \
 --filter SERVICE\_CONTROL\_POLICY**`{
 "Policies": [
 {
 "Id": "p-FullAWSAccess",
 "Arn": "arn:aws:organizations::aws:policy/service_control_policy/p-FullAWSAccess",
 "Name": "FullAWSAccess",
 "Description": "Allows access to every operation",
 "Type": "SERVICE_CONTROL_POLICY",
 "AwsManaged": true
 }
 ]
}`
```

- AWS SDKs: [ListPoliciesForTarget](../APIReference/API_ListPoliciesForTarget.md "../APIReference/API_ListPoliciesForTarget.md")

## Listing all roots, OUs, and accounts

that a policy is attached to

###### Minimum permissions

To list the entities that a policy is attached to, you must have the following
permission:

- `organizations:ListTargetsForPolicy` with a
  `Resource` element in the same policy statement that includes
  the ARN of the specified policy (or "\*")

AWS Management Console

###### To list all roots, OUs, and accounts that have a specified policy

attached

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Policies](https://console.aws.amazon.com/organizations/v2/home/policies "https://console.aws.amazon.com/organizations/v2/home/policies")** page, choose the policy type, and then choose the
   name of the policy whose attachments you want to examine.
3. Choose the **Targets** tab, to display a table of
   every root, OU, and account that the chosen policy is attached
   to.

AWS CLI & AWS SDKs

###### To list all roots, OUs, and accounts that have a specified policy

attached

You can use one of the following commands to list entities that have a
policy:

- AWS CLI: [list-targets-for-policy](../../../cli/latest/reference/organizations/list-targets-for-policy.md "../../../cli/latest/reference/organizations/list-targets-for-policy.md")

The following example shows all of the attachments to root, OUs,
and accounts for the specified policy.

```
`$` **aws organizations list-targets-for-policy \
 --policy-id p-FullAWSAccess**`{
 "Targets": [
 {
 "TargetId": "ou-a1b2-f6g7h111",
 "Arn": "arn:aws:organizations::123456789012:ou/o-aa111bb222/ou-a1b2-f6g7h111",
 "Name": "testou2",
 "Type": "ORGANIZATIONAL_UNIT"
 },
 {
 "TargetId": "ou-a1b2-f6g7h222",
 "Arn": "arn:aws:organizations::123456789012:ou/o-aa111bb222/ou-a1b2-f6g7h222",
 "Name": "testou1",
 "Type": "ORGANIZATIONAL_UNIT"
 },
 {
 "TargetId": "123456789012",
 "Arn": "arn:aws:organizations::123456789012:account/o-aa111bb222/123456789012",
 "Name": "My Management Account (bisdavid)",
 "Type": "ACCOUNT"
 },
 {
 "TargetId": "r-a1b2",
 "Arn": "arn:aws:organizations::123456789012:root/o-aa111bb222/r-a1b2",
 "Name": "Root",
 "Type": "ROOT"
 }
 ]
}`
```

- AWS SDKs: [ListTargetsForPolicy](../APIReference/API_ListTargetsForPolicy.md "../APIReference/API_ListTargetsForPolicy.md")

## Getting details about a policy

###### Minimum permissions

To display the details of a policy, you must have the following permission:

- `organizations:DescribePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")

###### To get details about a policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Policies](https://console.aws.amazon.com/organizations/v2/home/policies "https://console.aws.amazon.com/organizations/v2/home/policies")** page, choose the policy type of the policy that
   you want to examine, and then choose the name of the policy.

The policy page displays the available information about the
policy, including its ARN, description, and attached targets.

    * The **Content** tab shows the current
     contents of the policy in JSON format.
    * The **Targets** tab shows a list of the
     roots, OUs, and accounts to which the policy is
     attached.
    * The **Tags** tab shows the tags attached
     to the policy. Note: the Tags tab is not available for AWS
     managed policies.

To edit the policy, choose **Edit policy**.
Because each policy type has different editing requirements, see the
instructions for creating and updating policies of your specified
policy type.

The following code examples show how to use `DescribePolicy`.

CLI

**AWS CLI**

**To get information about a policy**

The following example shows how to request information about a policy:

```
`aws organizations describe-policy --policy-id `p-examplepolicyid111``

```

The output includes a policy object that contains details about the policy:

```
{
        "Policy": {
                "Content": "{\n  \"Version\": \"2012-10-17\",\n  \"Statement\": [\n    {\n      \"Effect\": \"Allow\",\n      \"Action\": \"*\",\n      \"Resource\": \"*\"\n    }\n  ]\n}",
                "PolicySummary": {
                        "Arn": "arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111",
                        "Type": "SERVICE_CONTROL_POLICY",
                        "Id": "p-examplepolicyid111",
                        "AwsManaged": false,
                        "Name": "AllowAllS3Actions",
                        "Description": "Enables admins to delegate S3 permissions"
                }
        }
}
```

- For API details, see
  [DescribePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-policy.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples").

```
def describe_policy(policy_id, orgs_client):
    """
    Describes a policy.

    :param policy_id: The ID of the policy to describe.
    :param orgs_client: The Boto3 Organizations client.
    :return: The description of the policy.
    """
    try:
        response = orgs_client.describe_policy(PolicyId=policy_id)
        policy = response["Policy"]
        logger.info("Got policy %s.", policy_id)
    except ClientError:
        logger.exception("Couldn't get policy %s.", policy_id)
        raise
    else:
        return policy




```

- For API details, see
  [DescribePolicy](../../../goto/boto3/organizations-2016-11-28/DescribePolicy.md "../../../goto/boto3/organizations-2016-11-28/DescribePolicy.md")
  in _AWS SDK for Python (Boto3) API Reference_.
