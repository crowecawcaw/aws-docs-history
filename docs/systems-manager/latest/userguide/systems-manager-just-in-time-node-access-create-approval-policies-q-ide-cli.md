• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Create approval policies for just-in-time node access with Amazon Q

Using Amazon Q Developer for command line provides guidance and support across various
aspects of software development. For just-in-time node access, Amazon Q helps you
create approval policies by generating and updating the code for the policies,
analyzing policy statements, and more. The following information describes how
to create approval policies using Amazon Q for command line.

## Identify your use case

The first step in creating approval policies is clearly defining your use
case. For example, in your organization you might want to automatically
approve access requests to nodes with an `Environment:Testing`
tag. You might also want to explicitly deny auto-approvals to nodes with an
`Environment:Production` tag if an employee ID begins with
`TEMP`. For nodes with a `Tier:Database` tag, you
might want to require two levels of manual approvals.

In any given scenario, you might prefer one policy or condition, over
another. Therefore, we recommend that you clearly define the policy
behaviors you want to determine which statements best fit your use case and
preferences.

## Set up your development

environment

Install Amazon Q for command line where you want to develop your approval
policies. For information about installing Amazon Q for the command line, see
[Installing Amazon Q for command line](../../../amazonq/latest/qdeveloper-ug/command-line-installing.md "../../../amazonq/latest/qdeveloper-ug/command-line-installing.md") in the _Amazon Q Developer
User Guide_.

We also recommend installing the MCP server for AWS documentation. This
MCP server connects Amazon Q for command line to the most current
documentation resources. For information about using MCP with Amazon Q for the
command line, see [Using MCP with
Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/command-line-mcp.md "../../../amazonq/latest/qdeveloper-ug/command-line-mcp.md") in the _Amazon Q Developer User Guide_.

For more information about the AWS Documentation MCP server see [AWS Documentation MCP Server](https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server/ "https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server/").

Install and configure the AWS CLI, if you have not already. For information,
see [Installing or
updating the latest version of the AWS CLI.](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")

## Develop approval policy content

With your use case identified and environment set up, you're ready to
develop the content for your policies. Your use case and preferences will
largely dictate the types of approval policies and statements you
use.

If you're unsure how to use a particular policy or need more information
about the schema for a policy, see [Create
approval policies for your nodes](systems-manager-just-in-time-node-access-approval-policies.md "systems-manager-just-in-time-node-access-approval-policies.md") and the subsequent topics. These topics explain in detail how policies
are evaluated and provide working example statements.

The following procedure describes how to create approval policies with Amazon Q
for command line.

###### Note

Amazon Q Developer uses generative AI. You may need to verify responses. See the
[AWS
Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/ "https://aws.amazon.com/ai/responsible-ai/policy/").

###### To create a approval policies using Amazon Q for command line

1. Open your terminal and start a session with Amazon Q.

```
$ q chat
```

2. Enter a prompt and describe what kind of policy statement you want to
   create. For example, using the earlier scenario for an approval policy,
   you could enter the following prompt:

```
Create a Cedar policy statement that allows a principal to use the “getTokenForInstanceAccess" action for a resource
that has a tag key “Environment” and tag value of “Testing”. Use the following example statement for reference to verify the syntax.

permit (
    principal in AWS::IdentityStore::Group::"e8c17310-e011-7089-d989-10da1EXAMPLE",
    action == AWS::SSM::Action::"getTokenForInstanceAccess",
    resource
)
when {
    principal has organization && resource.hasTag("Engineering") && resource.hasTag("Production") && principal.organization == "Platform"
};

The Cedar policy statement you create must be valid. Validate the Cedar statement using the AWS documentation provided for just-in-time node access policy statement structure and make sure you abide by the schema.
```

3. Entering this example prompt resulted in the following output:

```
Based on the AWS documentation for Cedar policy statements and the examples provided, I'll create a valid Cedar policy
statement that allows a principal to use the "getTokenForInstanceAccess" action for resources with the tag key "Environment" and tag value "Testing".

Here's the Cedar policy statement:

permit (
    principal,
    action == AWS::SSM::Action::"getTokenForInstanceAccess",
    resource
)
when {
    resource.hasTag("Environment") &&
    resource.getTag("Environment") == "Testing"
};


This policy statement:
1. Uses the permit effect to allow access
2. Applies to any principal (since no specific principal is defined)
3. Specifically targets the "getTokenForInstanceAccess" action
4. Applies to resources that have a tag with key "Environment" and value "Testing"
5. Uses the proper syntax for the condition clause with the hasTag() and getTag() operators

The statement follows the Cedar policy language structure as documented in the AWS Systems Manager documentation for just-in-time node access policies.
```

4. Paste the policy statement into a new Cedar file to validate the
   syntax. You can also validate the statement using the [Cedar
   playground](https://www.cedarpolicy.com/en/playground "https://www.cedarpolicy.com/en/playground").
5. After validating the statement, save the Cedar file.
6. From your terminal, run the following AWS CLI command to create an SSM
   document using your policy content. Before using approval policies in a
   production environment, test your approval policies with a subset of
   identities and nodes in an AWS account and AWS Region.

###### Note

For an auto-approval policy, the document name must be
`SSM-JustInTimeAccessAutoApprovalPolicy`. There can
only be one auto-approval policy per AWS account and AWS Region.
For a deny-access policy, the document name must be
`SSM-JustInTimeAccessDenyAccessOrgPolicy`. There can
only be one deny-access policy per AWS Organizations organization, and the
policy must be created in the delegated administrator account for
Systems Manager. The naming constraints for manual approval policies are the
same as other SSM documents. For more information, see [CreateDocument](../APIReference/API_CreateDocument.md#systemsmanager-CreateDocument-request-Name "../APIReference/API_CreateDocument.md#systemsmanager-CreateDocument-request-Name").

Linux & macOS

```
aws ssm create-document \
    --content file://`path`/`to`/`file`/`policyContent`.cedar \
    --name "`SSM-JustInTimeAccessAutoApprovalPolicy`" \
    --document-type "AutoApproval"
```

Windows

```
aws ssm create-document ^
    --content file://C:\`path`\`to`\`file`\`policyContent`.cedar ^
    --name "`SSM-JustInTimeAccessAutoApprovalPolicy`" ^
    --document-type "AutoApproval"
```

PowerShell

```
$cedar = Get-Content -Path "C:\`path`\`to`\`file`\`policyContent`.cedar" | Out-String
New-SSMDocument `
    -Content $cedar `
    -Name "`SSM-JustInTimeAccessAutoApprovalPolicy`" `
    -DocumentType "AutoApproval"
```
