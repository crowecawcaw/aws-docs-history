

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Create a deny-access policy for just-in-time node access
<a name="systems-manager-just-in-time-node-access-create-deny-access-policies"></a>

Deny-access policies use the Cedar policy language to define which nodes users can't automatically connect to without manual approval. A deny-access policy contains multiple `forbid` statements specifying the `principal` and `resource`. Each statement includes a `when` clause defining the conditions for explicitly denying automatic approval.

The following is an example deny-access policy.

```
forbid (
    principal in AWS::IdentityStore::Group::"e8c17310-e011-7089-d989-10da1EXAMPLE",
    action == AWS::SSM::Action::"getTokenForInstanceAccess",
    resource
)
when {
    resource.hasTag("Environment") && resource.getTag("Environment") == "Production"
};

forbid (
    principal,
    action == AWS::SSM::Action::"getTokenForInstanceAccess",
    resource
)
when {
    principal has division && principal.division != "Finance" && resource.hasTag("DataClassification") && resource.getTag("DataClassification") == "Financial"
};


forbid (
    principal,
    action == AWS::SSM::Action::"getTokenForInstanceAccess",
    resource
)
when {
    
    principal has employeeNumber && principal.employeeNumber like "TEMP-*" && resource.hasTag("Criticality") && resource.getTag("Criticality") == "High"
};
```

The following procedure describes how to create a deny-access policy for just-in-time node access. For more information about how to construct policy statements, see [Statement structure and built-in operators for auto-approval and deny-access policies](auto-approval-deny-access-policy-statement-structure.md).

**Note**  
Note the following information.  
You can create deny-access policies while logged into the AWS Management account or the delegated administrator account. Your AWS Organizations organization can have only one deny-access policy.
Just-in-time node access uses AWS Resource Access Manager (AWS RAM) to share your deny-access policy with member accounts in your organization. If you would like to share your deny-access policy with the member accounts in your organization, resource sharing must be enabled from the management account of your organization. For more information, see [Enable resource sharing within AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.

**To create a deny-access policy**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. Select **Manage node access** in the navigation pane.

1. In the **Approval policies** tab, select **Create a deny-access policy**.

1. Enter your policy statement for the deny-access policy in the **Policy statement** section. You can use the **Sample statements** provided to help you create your policy.

1. Select **Create deny-access policy**.