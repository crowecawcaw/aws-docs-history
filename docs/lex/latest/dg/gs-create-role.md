End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 1: Create a Service-Linked Role

(AWS CLI)

Amazon Lex assumes AWS Identity and Access Management service-linked roles to call AWS services on behalf of
your bots. The roles, which are in your account, are linked to Amazon Lex use cases and
have predefined permissions. For more information, see [Using Service-Linked Roles for
Amazon Lex](using-service-linked-roles.md "using-service-linked-roles.md").

If you've already created an Amazon Lex bot using the console, the service-linked role
was created automatically. Skip to [Step 2: Create a Custom Slot Type
(AWS CLI)](gs-create-flower-types.md "gs-create-flower-types.md").

###### To create a service-linked role (AWS CLI)

1. In the AWS CLI, type the following command:

```
aws iam create-service-linked-role --aws-service-name lex.amazonaws.com
```

2. Check the policy using the following command:

```
aws iam get-role --role-name AWSServiceRoleForLexBots
```

The response is:

## Next Step

[Step 2: Create a Custom Slot Type
(AWS CLI)](gs-create-flower-types.md "gs-create-flower-types.md")
