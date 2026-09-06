

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Create an auto-approval policy for just-in-time node access
<a name="systems-manager-just-in-time-node-access-create-auto-approval-policies"></a>

Auto-approval policies use the Cedar policy language to define which users can automatically connect to the specified nodes without manual approval. An auto-approval policy contains multiple `permit` statements specifying the `principal` and `resource`. Each statement includes a `when` clause defining the conditions for automatic approval.

The following is an example auto-approval policy.

```
permit (
    principal in AWS::IdentityStore::Group::"e8c17310-e011-7089-d989-10da1EXAMPLE",
    action == AWS::SSM::Action::"getTokenForInstanceAccess",
    resource
)
when {
    principal has costCenter && resource.hasTag("CostCenter") && principal.costCenter == resource.getTag("CostCenter")
};

permit (
    principal in AWS::IdentityStore::Group::"d4q81745-r081-7079-d789-14da1EXAMPLE",
    action == AWS::SSM::Action::"getTokenForInstanceAccess",
    resource
)
when {
    principal has organization && resource.hasTag("Engineering") && resource.hasTag("Production") && principal.organization == "Platform"
};

permit (
    principal,
    action == AWS::SSM::Action::"getTokenForInstanceAccess",
    resource
)
when {
    principal has employeeNumber && principal.employeeNumber like "E-1*" && resource.hasTag("Purpose") && resource.getTag("Purpose") == "Testing"
};
```

The following procedure describes how to create an auto-approval policy for just-in-time node acces. The access duration for an access request that is automatically approved is 1 hour. This value can't be changed. You can only have one auto-approval policy per AWS account and AWS Region. For more information about how to construct policy statements, see [Statement structure and built-in operators for auto-approval and deny-access policies](auto-approval-deny-access-policy-statement-structure.md).

**To create an auto-approval policy**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. Select **Manage node access** in the navigation pane.

1. In the **Approval policies** tab, select **Create an auto-approval policy**.

1. Enter your policy statement for the auto-approval policy in the **Policy statement** section. You can use the **Sample statements** provided to help you create your policy.

1. Select **Create auto-approval policy**.