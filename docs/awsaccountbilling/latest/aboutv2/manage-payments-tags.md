# Manage payment method access using tags

You can use attribute-based access control (ABAC) to manage access to your purchase methods. When you create your payment methods, you can tags with key-value pairs. You can then create IAM policies and specify the tags. For example, if you add the `project` key and assign it a value of `test`, your IAM policies can explicitly allow or deny access to any payment instruments that has this tag.

To add tags to new payment instruments or update existing ones, see [Managing credit card and ACH direct debit](manage-cc.md "manage-cc.md").

###### Example Use tags to allow access

The following policy allows the IAM entity to access payment instruments that have the `creditcard` key and a value of visa.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "payments:ListPaymentInstruments",
 "payments:GetPaymentInstrument",
 "payments:ListTagsForResource"
 ],
 "Resource": "arn:aws:payments::123456789012:payment-instrument/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/creditcard": "visa"
 }
 }
 }]
}`

```

###### Example Use tags to deny access

The following policy denies the IAM entity from completing any payment action on payment methods that have the `creditcard` key and a value of `visa`.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "payments:*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "payments:GetPaymentInstrument",
 "Resource": "arn:aws:payments::123456789012:payment-instrument:*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/creditcard": "visa"
 }
 }
 }]
}`

```

For more information, see the following topics in the _IAM User Guide_:

- [What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")
- [Controlling access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md")
