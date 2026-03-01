# Service-specific permissions

In addition to the destination-specific permissions listed in the previous sections,
some services require explicit authorization that customers are allowed to send logs
from their resources, as an additional layer of security. It authorizes the
`AllowVendedLogDeliveryForResource` action for resources that vend logs
within that service. For these services, use the following policy and replace
`service` and `resource-type` with
the appropriate values. For the service-specific values for these fields, see those
services' documentation page for vended logs. In the following example, the policy has
been updated to enable vended logs from Amazon SES.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ServiceLevelAccessForLogDelivery",
 "Effect": "Allow",
 "Action": [
 "`ses`:AllowVendedLogDeliveryForResource"
 ],
 "Resource": "arn:aws:`ses`:`us-east-1`:`123456789012`:`resource-type`/*"
 }
 ]
}`

```
