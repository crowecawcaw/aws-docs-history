# Add permissions to your IAM Role

All managed integrations APIs require AWS sigV4 authentication to invoke. SigV4 is signing
protocol to authenticate AWS API requests using your AWS account credentials. The
IAM role you use to invoke the managed integrations APIs must have the following permissions
to be able to successfully invoke the APIs:

```
 	"Version": "2012-10-17",
 	"Statement": [
 	{
 		"Sid": "Statement1",
 		"Effect": "Allow",
 		"Action": [
 			"iotmanagedintegrations:`Your-Required-Actions`"
 		],
 		"Resource": [
 			"`Your-Resource`"
 		]
 	}]
}

```

For additional information on adding these permissions, contact Support.

###### Additional resources

To register your C2C connector, you will need the following:

- The Lambda ARN designating the connector you would like to register.
