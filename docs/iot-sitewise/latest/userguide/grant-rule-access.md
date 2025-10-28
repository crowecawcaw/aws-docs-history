# Grant AWS IoT the required access

You use IAM roles to control the AWS resources to which each rule has access. Before
you create a rule, you must create an IAM role with a policy that allows the rule to perform actions on the
required AWS resource. AWS IoT assumes this role when running a rule.

If you create the rule action in the AWS IoT console, you can choose a root asset to
create a role that has access to a selected asset hierarchy. For more information about how
to manually define a role for a rule, see [Granting AWS IoT the required
access](../../../iot/latest/developerguide/iot-create-role.md "../../../iot/latest/developerguide/iot-create-role.md") and [Pass role permissions](../../../iot/latest/developerguide/pass-role.md "../../../iot/latest/developerguide/pass-role.md") in the
_AWS IoT Developer Guide_.

For the AWS IoT SiteWise rule action, you must define a role that allows
`iotsitewise:BatchPutAssetPropertyValue` access to the asset properties to
which the rule sends data. To improve security, you can specify an AWS IoT SiteWise asset hierarchy
path in the `Condition` property.

The following example trust policy allows access to a specific asset and its
children.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iotsitewise:BatchPutAssetPropertyValue",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iotsitewise:assetHierarchyPath": [
 "/`root node asset ID`",
 "/`root node asset ID`/*"
 ]
 }
 }
 }
 ]
}`

```

Remove the `Condition` from the policy to allow access to all of your
assets. The following example trust policy allows access to all of your assets in the
current Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iotsitewise:BatchPutAssetPropertyValue",
 "Resource": "*"
 }
 ]
}`

```
