# Tag-based authorization guidelines

Tag-based authorization can prevent you from modifying customer resources. This strategy
utilizes IAM tag conditions. You assume a role in your customer’s account, and the role will
have IAM policies based on tag conditions. When you create a resource in your customer’s
account, the policy requires a specific tag to be added. And when you modify a resource in your
customer’s account, the policy ensures that it only allows modification on resources with the
specified tags. You should not have permission to modify or delete tags on a resource. To create a
complete IAM policy for the assume role, the customer can use the following examples.

###### Topics

- [Tag conditions](#tag-conditions "#tag-conditions")
- [Additional examples](#additional-examples "#additional-examples")

## Tag conditions

### TagKeys condition

To ensure that only a specific tag key can be used in a request, use the
`aws:TagKeys` condition key.

### RequestTag condition

To ensure that a specific tag key and value will be put on the resource, use a combination
of the `aws:TagKeys` and `aws:RequestTag` condition keys. This applies to
resource creation API actions, such as CreateWorkspaces.

The following tag keys policy example only allows API actions to use tag keys
“PartnerManaged.”

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "workspaces:CreateWorkspaces"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/PartnerManaged": "true"
 },
 "ForAllValues:StringEquals" : {
 "aws:TagKeys": "PartnerManaged"
 }
 }
 }
 ]
}`

```

### ResourceTag condition

To control access to a customer’s resources based on the tag key and value use a
combination of the `aws:TagKeys` and `aws:ResourceTag` condition keys.
This applies to modifications related to API actions, such as ModifyWorkspaceProperties.

The following resource tag policy example ensures that modifications can only happen on
resources with the tag “Key=PartnerManaged, Value=true”.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "workspaces:ModifyWorkspaceProperties"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/PartnerManaged": "true"
 },
 "ForAllValues:StringEquals" : {
 "aws:TagKeys": "PartnerManaged"
 }
 }
 }
 ]
}`

```

## Additional examples

| API name                                                                                                                                     | Tag condition request | Assumed role policy for UserTag                                                                                                                                                                                                                                                                                                                                      | Note                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [CreateWorkSpaces](../../../workspaces/latest/api/API_CreateWorkspaces.md "../../../workspaces/latest/api/API_CreateWorkspaces.md")          | TagKeys + RequestTag  | JSON<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"workspaces:CreateWorkspaces"<br>],<br>"Resource": "*",<br>"Condition": {<br>"StringEquals": {<br>"aws:RequestTag/PartnerManaged": "true"<br>},<br>"ForAllValues:StringEquals" : {<br>"aws:TagKeys": "PartnerManaged"<br>}<br>}<br>}<br>]<br>}`<br>``     | With this policy, you can only create a workspace if you provide a tag key<br>"PartnerManaged" and value "true" in the request. |
| [TerminateWorkSpaces](../../../workspaces/latest/api/API_TerminateWorkspaces.md "../../../workspaces/latest/api/API_TerminateWorkspaces.md") | TagKeys + RequestTag  | JSON<br>``<br>`{<br>"Version":"2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"workspaces:TerminateWorkspaces"<br>],<br>"Resource": "*",<br>"Condition": {<br>"StringEquals": {<br>"aws:ResourceTag/PartnerManaged": "true"<br>},<br>"ForAllValues:StringEquals" : {<br>"aws:TagKeys": "PartnerManaged"<br>}<br>}<br>}<br>]<br>}`<br>`` | With this policy, you can only terminate a workspace if the workspace has a tag key<br>"PartnerManaged" and value "true".       |
