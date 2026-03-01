# IAM policy examples for API execution permissions

For permissions model and other background information, see [Control access for invoking an API](api-gateway-control-access-using-iam-policies-to-invoke-api.md "api-gateway-control-access-using-iam-policies-to-invoke-api.md").

The following policy statement gives the user permission to call any POST method along
the path of `mydemoresource`, in the stage of
`test`, for the API with the identifier of `a123456789`, assuming the corresponding API has been deployed to the AWS
region of us-east-1:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "execute-api:Invoke"
 ],
 "Resource": [
 "arn:aws:execute-api:us-east-1:*:a123456789/test/POST/my-demo-resource-path/*"
 ]
 }
 ]
}`

```

The following example policy statement gives the user permission to call any method on
the resource path of `petstorewalkthrough/pets`, in any stage, for the
API with the identifier of `a123456789`, in any AWS
region where the corresponding API has been deployed:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "execute-api:Invoke"
 ],
 "Resource": [
 "arn:aws:execute-api:*:*:a123456789/*/*/petstorewalkthrough/pets"
 ]
 }
 ]
}`

```
