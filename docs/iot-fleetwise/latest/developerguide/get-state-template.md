# Get AWS IoT FleetWise state template information

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can use the [GetStateTemplate](../APIReference/API_GetStateTemplate.md "../APIReference/API_GetStateTemplate.md") API operation to retrieve information about a
state template. The following example uses the AWS CLI.

Replace `identifier` with the name of the state template.

```
aws iotfleetwise get-state-template \
    --identifier `idenitfier`
```

You can use the [ListStateTemplates](../APIReference/API_ListStateTemplates.md "../APIReference/API_ListStateTemplates.md") API operation to retrieve a list of your created state templates. The following example uses the AWS CLI.

```
aws iotfleetwise list-state-templates
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `GetStateTemplate` or `ListStateTemplates` API operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS_KEY_ID`"
 ]
 }
 ]
}`

```
