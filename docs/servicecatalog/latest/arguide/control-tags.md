# Controlling the resources associated to applications

This topic includes policy templates that you can use to control how tag key-value pairs are associated to applications.

The following policy templates are organized by scenario and include values that can be replaced with your information.

**Sample policy: Stack only association**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:*",
 "cloudformation:DescribeStacks",
 "resource-groups:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "servicecatalog:AssociateResource",
 "Resource": "arn:aws:servicecatalog:*:*:*",
 "Condition": {
 "StringNotEquals": {
 "servicecatalog:ResourceType": "`CFN_STACK`"
 }
 }
 }
 ]
}`

```

**Sample policy: Stack association that allows a specific stack name**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:*",
 "cloudformation:DescribeStacks",
 "resource-groups:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "servicecatalog:AssociateResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "servicecatalog:ResourceType": "`CFN_STACK`"
 }
 }
 }
 ]
}`

```

**Sample policy: Stack association that allows multiple specific stack names**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:*",
 "cloudformation:DescribeStacks",
 "resource-groups:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "servicecatalog:AssociateResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "servicecatalog:ResourceType": "`CFN_STACK`"
 }
 }
 }
 ]
}`

```

**Sample policy: Tag value association that denies a specific tag query value while allowing other tag queries**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:*",
 "cloudformation:DescribeStacks",
 "resource-groups:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "servicecatalog:AssociateResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "servicecatalog:ResourceType": "`TAG_QUERY`"
 }
 }
 }
 ]
}`

```

**Sample policy: Allow tag query association only**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:*",
 "cloudformation:DescribeStacks",
 "resource-groups:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "servicecatalog:AssociateResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "servicecatalog:ResourceType": "`TAG_QUERY`"
 }
 }
 }
 ]
}`

```

**Sample policy: Allow tag query association/deny specific tag query values**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:*",
 "cloudformation:DescribeStacks",
 "resource-groups:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "servicecatalog:AssociateResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "servicecatalog:ResourceType": "`CFN_STACK`"
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "servicecatalog:AssociateResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "servicecatalog:ResourceType": ["`TAG_QUERY`"]
 }
 }
 }
 ]
}`

```

**Sample policy: Allow specific tag query value and specific stack**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "servicecatalog:*",
 "cloudformation:DescribeStacks",
 "resource-groups:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "servicecatalog:AssociateResource"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "servicecatalog:AssociateResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "servicecatalog:ResourceType": "`CFN_STACK`"
 }
 }
 }
 ]
}`

```
