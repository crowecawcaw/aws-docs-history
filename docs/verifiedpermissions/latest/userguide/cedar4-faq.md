# Amazon Verified Permissions upgrade to Cedar 4 FAQ

Amazon Verified Permissions is upgrading the version of Cedar it uses from version 2 to version 4. Cedar is the open-source language you use to write the policies, policy templates and schemas in your policy stores. With Cedar 4 support in Verified Permissions, you can use new features such as the `is` operator and entity tags to write more expressive policies.

Amazon Verified Permissions is automatically upgrading policy stores to Cedar 4. However, some policies, schemas and authorization requests written for Cedar 2 are incompatible with Cedar 4. If this is the case for your policy store, then we will not upgrade it automatically. You may need to make changes to your policies, policy templates, schemas or application code before you can upgrade to Cedar 4.

###### Topics

- [Why are some policies, policy templates and schemas not compatible with Cedar 4?](#why-are-some-policies-not-compatible-with-cedar-4 "#why-are-some-policies-not-compatible-with-cedar-4")
- [How do I tell whether my policy store is using Cedar 2 or Cedar 4?](#how-do-i-tell-cedar-2-or-cedar-4 "#how-do-i-tell-cedar-2-or-cedar-4")
- [How do I upgrade to Cedar 4?](#how-do-i-upgrade-to-cedar-4 "#how-do-i-upgrade-to-cedar-4")
- [Can I downgrade my policy store from Cedar 4 to Cedar 2?](#can-i-downgrade-from-cedar-4-to-cedar-2 "#can-i-downgrade-from-cedar-4-to-cedar-2")
- [Why am I receiving an error message saying my policy store is configured for Cedar 2?](#why-am-i-receiving-an-error-message-policy-store-configured-for-cedar-4 "#why-am-i-receiving-an-error-message-policy-store-configured-for-cedar-4")
- [How do I make my schema compatible with Cedar 4?](#how-do-i-make-my-schema-compatible "#how-do-i-make-my-schema-compatible")
- [How do I make my policies and templates compatible with Cedar 4?](#how-do-i-make-my-policies-compatible "#how-do-i-make-my-policies-compatible")

##

Why are some policies, policy templates and schemas not compatible with Cedar 4?

The Cedar team has made several backwards-incompatible changes since Cedar 2, to fix bugs and simplify the language. These changes include:

- syntax changes for policies, policy templates and schemas
- a more precise policy validator, which detects more errors
- changes to the behaviour of built-in functions like `isInRange`

For a full list of backwards-incompatible changes, look for items marked with `(*)` in the [Cedar changelog](https://github.com/cedar-policy/cedar/blob/main/cedar-policy/CHANGELOG.md "https://github.com/cedar-policy/cedar/blob/main/cedar-policy/CHANGELOG.md").

##

How do I tell whether my policy store is using Cedar 2 or Cedar 4?

You can check the version of Cedar your policy store uses using the Amazon Verified Permissions console, or using the GetPolicyStore operation.

###### Note

All policy stores in the same AWS account and region use the same version of Cedar.

Console

###### To check the Cedar version of a policy store (console)

1. Sign in to the AWS Management Console and open the Amazon Verified Permissions console at [https://console.aws.amazon.com/verifiedpermissions/](https://console.aws.amazon.com/verifiedpermissions "https://console.aws.amazon.com/verifiedpermissions").
2. From the navigation pane, choose **Policy stores** and then choose the policy store that you want to check.
3. Choose **Settings** in the navigation pane.
4. In the **Details** box, locate the **Cedar version** field.

The field reads `CEDAR_2` if your policy store is using Cedar 2, and `CEDAR_4` if it uses Cedar 4.

CLI

###### To check the Cedar version of a policy store (AWS CLI)

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already. For information, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
2. Use the `get-policy-store` command. In the following example, replace `policy-store-id` with the identifier of your policy store:

```
aws verifiedpermissions get-policy-store \
  --policy-store-id `policy-store-id`
```

The `cedarVersion` field in the output shows which version of Cedar the policy store is using. For example:

```
{
    "policyStoreId": "ABCDEFG12345678abcdefg",
    "arn": "arn:aws:verifiedpermissions::111122223333:policy-store/ABCDEFG12345678abcdefg",
    "validationSettings": {
        "mode": "STRICT"
    },
    "createdDate": "2025-06-03T13:09:47.752255+00:00",
    "lastUpdatedDate": "2025-06-03T13:09:47.752255+00:00",
    "deletionProtection": "ENABLED",
    "cedarVersion": "CEDAR_2"
}
```

The field reads `CEDAR_2` if your policy store is using Cedar 2, and `CEDAR_4` if it uses Cedar 4.

##

How do I upgrade to Cedar 4?

Amazon Verified Permissions has already upgraded most customers to Cedar 4. If you have never created a policy store, then any new policy stores you create will use Cedar 4. If you are an existing customer, then we have likely already upgraded you to Cedar 4. See [How do I tell whether my policy store is using Cedar 2 or Cedar 4?](#how-do-i-tell-cedar-2-or-cedar-4 "#how-do-i-tell-cedar-2-or-cedar-4") to check which version of Cedar your policy stores use.

If you have not been upgraded, then Verified Permissions detected a policy, policy template, schema or authorization request in one of your policy stores which is incompatible with Cedar 4. We will send you an email notification describing which resources are incompatible later in 2025. To upgrade sooner, open a case with Support.

###### Important

All policy stores in the same AWS account use the same version of Cedar. If one policy store in your account is incompatible with Cedar 4, then you can’t use Cedar 4 in any policy store in that account.

##

Can I downgrade my policy store from Cedar 4 to Cedar 2?

No. If you experience issues after your policy store is upgraded to Cedar 4, open a case with Support.

##

Why am I receiving an error message saying my policy store is configured for Cedar 2?

Some features of Amazon Verified Permissions rely on the new features in Cedar 4. If your policy store does not use Cedar 4, then you can’t use the following API fields:

- In the IsAuthorized, BatchIsAuthorized, IsAuthorizedWithToken and BatchIsAuthorizedWithToken operations:
  - `datetime`, `decimal` or `duration` values in the `attributes` or `context` fields

You can’t use syntax or data types in policies, policy templates or schemas introduced after Cedar 2 until your policy store is upgraded.

##

How do I make my schema compatible with Cedar 4?

The Verified Permissions console can automatically fix some compatibility problems in your schema. If your schema cannot be automatically fixed, the console will show a list of errors for you to fix manually.

###### Important

The code editor in the Amazon Verified Permissions console always shows errors and warnings from Cedar 4, even if your policy store uses Cedar 2. You can continue to make schema updates that are not compatible with Cedar 4 using the **Save changes** button, or the Verified Permissions API.

###### To fix a schema using the console

1. Sign in to the AWS Management Console and open the Amazon Verified Permissions console at [verifiedpermissions](https://console.aws.amazon.com/verifiedpermissions "https://console.aws.amazon.com/verifiedpermissions").
2. From the navigation pane, choose **Policy stores** and then choose the policy store you want to check.
3. Choose **Schema** in the navigation pane.
4. If your schema can be fixed automatically, you will see a banner reading “Click ‘Fix’ to preview a compatible version’. Select **Fix**.
5. Review the changes made to your schema, and click **Preview updated schema**.
6. Review the updated schema, and click **Save changes**.

If your schema can’t be fixed automatically, you can see a list of errors to fix yourself in the console.

1. Open the **Edit schema** page as described above.
2. Select **JSON mode**.
3. Hover over the red error icon in the gutter on the left-hand side of the code editor. The error message is displayed in a tooltip.

Here are some common errors you may encounter and how to resolve them:

**failed to parse schema from JSON: `field-name`**

With Cedar 2, you can include arbitrary fields in parts of schemas like type definitions, even if they do not have any meaning as part of a Cedar schema. In Cedar 4, this is no longer permitted. To resolve this error, remove the field called `field-name` from your JSON schema. For a list of valid schema fields, see the [Cedar documentation](https://docs.cedarpolicy.com/schema/json-schema.html "https://docs.cedarpolicy.com/schema/json-schema.html").

**unknown extension type `extension-name`**

In Cedar 2, when you declare an attribute whose `type` is `Extension`, you can specify any value for the `name` field, whether or not the value is a valid extension type name. This is now an error with Cedar 4. To resolve it, replace `extension-name` with a valid extension type name. You can find a list of valid extension type names in the [Cedar documentation](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-extension "https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-extension").

If you are still unsure how to resolve the errors in your schema, contact Support

##

How do I make my policies and templates compatible with Cedar 4?

The Verified Permissions console shows you any errors in your policy or template which make it incompatible with Cedar 4.

###### To view a policy or template’s errors in the console

1. Sign in to the AWS Management Console and open the Amazon Verified Permissions console at [verifiedpermissions](https://console.aws.amazon.com/verifiedpermissions "https://console.aws.amazon.com/verifiedpermissions").
2. From the navigation pane, choose **Policy stores** and then choose the policy store you want to check.
3. Choose **Policies** or **Policy templates** in navigation pane, as appropriate.
4. Select the incompatible policy or template.
5. Select **Edit**
6. Hover over the red error icon in the gutter on the left-hand side of the code editor. The error message is displayed in a tooltip.

Here are some common errors you may encounter and how to resolve them:

**empty set literals are forbidden in policies**

In Cedar 2, you can use the syntax `mySet == []` to check whether a set is empty. With Cedar 4, policies using this syntax no longer validate against a schema. Replace `mySet == []` in your policy with `mySet.isEmpty()`.
