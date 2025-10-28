**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Oversize web request components

in AWS WAF

This section explains how to manage the size limits on inspecting the web request body, headers, and cookies in
AWS WAF.

AWS WAF doesn't support inspecting very large contents for the web request components body,
headers, or cookies. The underlying host service has count and size limits on what it
forwards to AWS WAF for inspection. For example, the host service doesn't send more than 200
headers to AWS WAF, so for a web request with 205 headers, AWS WAF can't inspect the last 5
headers.

When AWS WAF
allows a web request to proceed to your protected resource, the entire web request is sent,
including any contents that are outside of the count and size limits that AWS WAF was able to inspect.

###### Component inspection size limits

The component inspection size limits are as follows:

- **`Body` and `JSON Body`**
  – For Application Load Balancer and AWS AppSync, AWS WAF can inspect the first 8 KB of the body of a request. For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, by default, AWS WAF can inspect the first 16 KB, and
  you can increase the limit up to 64 KB in your protection pack (web ACL) configuration. For more information, see
  [Considerations for managing body inspection in AWS WAF](web-acl-setting-body-inspection-limit.md "web-acl-setting-body-inspection-limit.md").
- **`Headers`** – AWS WAF can inspect at most the first 8 KB (8,192 bytes) of the request headers and at most the first 200 headers. The content is available for inspection by AWS WAF up to the first limit reached.
- **`Cookies`** – AWS WAF can inspect at most the first 8 KB (8,192 bytes) of the request cookies and at most the first 200 cookies. The content is available for inspection by AWS WAF up to the first limit reached.

###### Oversize handling options for your rule statements

When you write a rule statement that inspects one of these request component
types, you specify how to handle oversize components. Oversize handling tells AWS WAF what
to do with a web request when the request component that the rule inspects is over the
size limits.

The options for handling oversize components are as follows:

- **Continue** – Inspect the
  request component normally according to the rule inspection criteria. AWS WAF will
  inspect the request component contents that are within the size limits.
- **Match** – Treat the web request as
  matching the rule statement. AWS WAF applies the rule action to the
  request without evaluating it against the rule's inspection criteria.
- **No match** – Treat the
  web request as not matching the rule statement without evaluating it against the
  rule's inspection criteria. AWS WAF continues its inspection of the web request using
  the rest of the rules in the protection pack (web ACL) like it would do for any non-matching rule.
  In the AWS WAF console, you're required to choose one of these handling options. Outside
  the console, the default option is Continue.

If you use the Match option in a rule that has its action set to
Block, the rule will block a request whose inspected component is oversize. With any
other configuration, the final disposition of the request depends on various factors, such
as the configuration of the other rules in your protection pack (web ACL) and the protection pack (web ACL)'s default action
setting.

###### Oversize handling in rule groups that you don't own

Component size and count limitations apply to all rules that you use in your protection pack (web ACL). This
includes any rules that you use but don't manage, in managed rule groups and in
rule groups that are shared with you by another account.

When you use a rule group that you don't manage, the rule group might have a rule that
inspects a limited request component but that doesn't handle oversized contents the way you
need them to be handled. For information about how AWS Managed Rules manage oversize components, see
[AWS Managed Rules rule groups list](aws-managed-rule-groups-list.md "aws-managed-rule-groups-list.md"). For information about other rule groups,
ask your rule group provider.

###### Guidelines for managing oversize components in your protection pack (web ACL)

The way you handle oversize components in your protection pack (web ACL) can depend on a number of
factors such as the expected size of your request component contents, your protection pack (web ACL)'s
default request handling, and how other rules in your protection pack (web ACL) match and handle requests.

The general guidelines for managing oversized web request components are as follows:

- If you need to allow some requests with oversize component contents, if possible,
  add rules to explicitly allow only those requests. Prioritize those rules so that
  they run before any other rules in the protection pack (web ACL) that inspect the same component
  types. With this approach, you won't be able to use AWS WAF to inspect the entire
  contents of the oversize components that you allow to pass to your protected
  resource.
- For all other requests, you can prevent any additional bytes from passing through
  by blocking requests that go over the limit:
  - **Your rules and rule groups** – In
    your rules that inspect components with size limits, configure oversize
    handling so that you block requests that go over the limit. For example, if
    your rule blocks requests with specific header contents, set the oversize
    handling to match on requests that have oversize header content.
    Alternately, if your protection pack (web ACL) blocks requests by default and your rule allows
    specific header contents, then configure your rule's oversize handling to
    not match on any request that has oversize header content.
  - **Rule groups that you don't manage**
    – To prevent rule groups that you don't manage from allowing oversize
    request components, you can add a separate rule that inspects the request
    component type and blocks requests that go over the limits. Prioritize the
    rule in your protection pack (web ACL) so that it runs before the rule groups. For example,
    you can block requests with oversize body content before any of your body
    inspection rules run in the protection pack (web ACL). The following procedure describes how
    to add this type of rule.

## Blocking oversized web request components

You can add a rule in your protection pack (web ACL) that blocks requests with oversized components.

###### To add a rule that blocks oversized contents

1. When you create or edit your protection pack (web ACL), in the rules settings, choose **Add
   rules**, **Add my own rules and rule groups**,
   **Rule builder**, then **Rule visual editor**.
   For guidance on creating or editing a protection pack (web ACL), see [Viewing web traffic metrics in AWS WAF](web-acl-working-with.md "web-acl-working-with.md").
2. Enter a name for your rule, and leave the **Type** setting at **Regular rule**.
3. Change the following match settings from their defaults:
   1. On **Statement**, for **Inspect**, open
      the dropdown and choose the web request component that you need, either
      **Body**, **Headers**, or
      **Cookies**.
   2. For **Match type**, choose **Size greater than**.
   3. For **Size**, type a number that's at least the
      minimum size for the component type. For headers and cookies, type `8192`. In Application Load Balancer or AWS AppSync protection packs (web ACLs), for bodies, type
      `8192`. For bodies in CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access protection packs (web ACLs),
      if you're using the default body size limit, type `16384`.
      Otherwise, type the body size limit that you've defined for your protection pack (web ACL).
   4. For **Oversize handling**, select
      **Match**.

4. For **Action**, select **Block**.
5. Choose **Add rule**.
6. After you add the rule, on the **Set rule priority** page, move
   it above any rules or rule groups in your protection pack (web ACL) that inspect the same component
   type. This gives the new rule a lower numeric priority setting, which causes AWS WAF to evaluate it first. For
   more information, see [Setting rule priority](web-acl-processing-order.md "web-acl-processing-order.md").
