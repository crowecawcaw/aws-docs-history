**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Where to set the AWS WAF token immunity times

You can set the immunity times in your protection pack (web ACL) and in your rules that use the
Challenge and CAPTCHA rule actions.

For general information about managing a protection pack (web ACL) and its rules, see [Viewing web traffic metrics in AWS WAF](web-acl-working-with.md "web-acl-working-with.md").

###### Where to set the immunity time for a protection pack (web ACL)

- **Console** – When you edit the protection pack (web ACL),
  in the **Rules** tab, edit and change the settings in the
  **protection pack (web ACL) CAPTCHA configuration** and **protection pack (web ACL)
  Challenge configuration** panes. In the console, you can configure
  the protection pack (web ACL) CAPTCHA and challenge immunity times only after you've created the
  protection pack (web ACL).
- **Outside of the console** – The protection pack (web ACL)
  data type has CAPTCHA and challenge configuration parameters, which you can
  configure and provide to your create and update operations on the protection pack (web ACL).

###### Where to set the immunity time for a rule

- **Console** – When you create or edit a
  rule and specify the CAPTCHA or Challenge action, you can modify
  the rule's immunity time setting.
- **Outside of the console** – The rule data
  type has CAPTCHA and challenge configuration parameters, which you can
  configure when you define the rule.
