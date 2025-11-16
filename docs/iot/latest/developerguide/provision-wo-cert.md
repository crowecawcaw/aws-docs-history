# Provisioning devices that don't have device

certificates using fleet provisioning

By using AWS IoT fleet provisioning, AWS IoT can generate and securely deliver device
certificates and private keys to your devices when they connect to AWS IoT for the first
time. AWS IoT provides client certificates that are signed by the Amazon Root certificate
authority (CA).

There are two ways to use fleet provisioning:

- [Provisioning by claim](#claim-based "#claim-based")
- [Provisioning by trusted user](#trusted-user "#trusted-user")

## Provisioning by claim

Devices can be manufactured with a provisioning claim certificate and private key
(which are special purpose credentials) embedded in them. If these certificates are
registered with AWS IoT, the service can exchange them for unique device certificates
that the device can use for regular operations. This process includes the following
steps:

###### Before you deliver the device

1. Call [`CreateProvisioningTemplate`](../apireference/API_CreateProvisioningTemplate.md "../apireference/API_CreateProvisioningTemplate.md") to create a
   provisioning template. This API returns a template ARN. For more
   information, see [Device provisioning MQTT API](fleet-provision-api.md "fleet-provision-api.md").

You can also create a fleet provisioning template in the AWS IoT console.

    1. From the navigation pane, choose the **Connect many
     devices** dropdown. Then, choose **Connect many
     devices**.
    2. Choose **Create provisioning template**.
    3. Choose the **Provisioning scenario** that best
     fits your installation processes. Then, choose
     **Next**.
    4. Complete the template workflow.

2. Create certificates and associated private keys to be used as provisioning
   claim certificates.
3. Register these certificates with AWS IoT and associate an IoT policy that
   restricts the use of the certificates. The following example IoT policy
   restricts the use of the certificate associated with this policy to
   provisioning devices.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Connect"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Publish",
 "iot:Receive"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`123456789012`:topic/$aws/certificates/create/*",
 "arn:aws:iot:`us-east-1`:`123456789012`:topic/$aws/provisioning-templates/`templateName`/provision/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iot:Subscribe",
 "Resource": [
 "arn:aws:iot:`us-east-1`:`123456789012`:topicfilter/$aws/certificates/create/*",
 "arn:aws:iot:`us-east-1`:`123456789012`:topicfilter/$aws/provisioning-templates/`templateName`/provision/*"
 ]
 }
 ]
}`

```

4. Give the AWS IoT service permission to create or update IoT resources such
   as things and certificates in your account when provisioning devices. Do
   this by attaching the `AWSIoTThingsRegistration` managed policy
   to an IAM role (called the provisioning role) that trusts the AWS IoT service
   principal.
5. Manufacture the device with the provisioning claim certificate securely
   embedded in it.

The device is now ready to be delivered to where it will be installed for
use.

###### Important

Provisioning claim private keys should be secured at all times, including on
the device. We recommend that you use AWS IoT CloudWatch metrics and logs to monitor for
indications of misuse. If you detect misuse, turn off the provisioning claim
certificate so it cannot be used for device provisioning.

###### To initialize the device for use

1. The device uses the [AWS IoT Device SDKs, Mobile SDKs, and AWS IoT Device Client](iot-sdks.md "iot-sdks.md") to
   connect to and authenticate with AWS IoT using the provisioning claim
   certificate that is installed on the device.

###### Note

For security, the `certificateOwnershipToken` returned by
`CreateCertificateFromCsr` and `CreateKeysAndCertificate` expires after one hour.
`RegisterThing`
must be called before the `certificateOwnershipToken`
expires. If the certificate created by `CreateCertificateFromCsr`
or `CreateKeysAndCertificate` has not been activated
and has not been attached to a policy or a thing by the time the token
expires, the certificate is deleted. If the token expires, the device
can call `CreateCertificateFromCsr` or `CreateKeysAndCertificate` again to generate a new
certificate. 2. The device obtains a permanent certificate and private key by using one of
these options. The device will use the certificate and key for all future
authentication with AWS IoT.

    1. Call [CreateKeysAndCertificate](fleet-provision-api.md#create-keys-cert "fleet-provision-api.md#create-keys-cert") to create a new
     certificate and private key using the AWS certificate
     authority.


    Or
    2. Call [CreateCertificateFromCsr](fleet-provision-api.md#create-cert-csr "fleet-provision-api.md#create-cert-csr") to generate a
     certificate from a certificate signing request that keeps its
     private key secure.

3. From the device, call [RegisterThing](fleet-provision-api.md#register-thing "fleet-provision-api.md#register-thing") to register the device with AWS IoT
   and create cloud resources.

The Fleet Provisioning service uses a provisioning template to define and
create cloud resources such as IoT things. The template can specify
attributes and groups that the thing belongs to. The thing groups must exist
before the new thing can be added to them. 4. After saving the permanent certificate on the device, the device must
disconnect from the session that it initiated with the provisioning claim
certificate and reconnect using the permanent certificate.

The device is now ready to communicate normally with AWS IoT.

## Provisioning by trusted user

In many cases, a device connects to AWS IoT for the first time when a trusted user,
such as an end user or installation technician, uses a mobile app to configure the
device in its deployed location.

###### Important

You must manage the trusted user's access and permission to perform this
procedure. One way to do this is to provide and maintain an account for the
trusted user that authenticates them and grants them access to the AWS IoT
features and API operations required to perform this procedure.

###### Before you deliver the device

1. Call [`CreateProvisioningTemplate`](../apireference/API_CreateProvisioningTemplate.md "../apireference/API_CreateProvisioningTemplate.md") to create a provisioning
   template and return its `templateArn` and
   `templateName`.
2. Create an IAM role that is used by a trusted user to initiate the
   provisioning process. The provisioning template allows only that user to
   provision a device. For example:

```
{
    "Effect": "Allow",
    "Action": [
        "iot:CreateProvisioningClaim"
    ],
    "Resource": [
        "arn:aws:iot:`aws-region`:`aws-account-id`:provisioningtemplate/`templateName`"
    ]
}
```

3. Give the AWS IoT service permission to create or update IoT resources, such
   as things and certificates in your account when provisioning devices. You do
   this by attaching the `AWSIoTThingsRegistration` managed policy
   to an IAM role (called the _provisioning
   role_) that trusts the AWS IoT service principal.
4. Provide the means to identify your trusted users, such as by providing
   them with an account that can authenticate them and authorize their
   interactions with the AWS API operations necessary to register their
   devices.

###### To initialize the device for use

1. A trusted user signs in to your provisioning mobile app or web
   service.
2. The mobile app or web application uses the IAM role and calls [`CreateProvisioningClaim`](../apireference/API_CreateProvisioningClaim.md "../apireference/API_CreateProvisioningClaim.md") to obtain a temporary
   provisioning claim certificate from AWS IoT.

###### Note

For security, the temporary provisioning claim certificate that
`CreateProvisioningClaim` returns expires after five
minutes. The following steps must successfully return a valid
certificate before the temporary provisioning claim certificate expires.
Temporary provisioning claim certificates do not appear in your
account's list of certificates. 3. The mobile app or web application supplies the temporary provisioning
claim certificate to the device along with any required configuration
information, such as Wi-Fi credentials. 4. The device uses the temporary provisioning claim certificate to connect to
AWS IoT using the [AWS IoT Device SDKs, Mobile SDKs, and AWS IoT Device Client](iot-sdks.md "iot-sdks.md"). 5. The device obtains a permanent certificate and private key by using one of
these options within five minutes of connecting to AWS IoT with the temporary
provisioning claim certificate. The device will use the certificate and key
these options return for all future authentication with AWS IoT.

    1. Call [CreateKeysAndCertificate](fleet-provision-api.md#create-keys-cert "fleet-provision-api.md#create-keys-cert") to create a new
     certificate and private key using the AWS certificate
     authority.


    Or
    2. Call [CreateCertificateFromCsr](fleet-provision-api.md#create-cert-csr "fleet-provision-api.md#create-cert-csr") to generate a
     certificate from a certificate signing request that keeps its
     private key secure.###### Note

Remember [CreateKeysAndCertificate](fleet-provision-api.md#create-keys-cert "fleet-provision-api.md#create-keys-cert") or [CreateCertificateFromCsr](fleet-provision-api.md#create-cert-csr "fleet-provision-api.md#create-cert-csr") must return a valid
certificate within five minutes of connecting to AWS IoT with the
temporary provisioning claim certificate. 6. The device calls [RegisterThing](fleet-provision-api.md#register-thing "fleet-provision-api.md#register-thing") to register the device with AWS IoT and
create cloud resources.

The Fleet Provisioning service uses a provisioning template to define and
create cloud resources such as IoT things. The template can specify
attributes and groups that the thing belongs to. The thing groups must exist
before the new thing can be added to them. 7. After saving the permanent certificate on the device, the device must
disconnect from the session that it initiated with the temporary
provisioning claim certificate and reconnect using the permanent
certificate.

The device is now ready to communicate normally with AWS IoT.

## Using pre-provisioning hooks with the AWS

CLI

The following procedure creates a provisioning template with pre-provisioning
hooks. The Lambda function used here is an example that can be modified.

###### To create and apply a pre-provisioning hook to a provisioning

template

1. Create a Lambda function that has a defined input and output. Lambda
   functions are highly customizable. `allowProvisioning` and
   `parameterOverrides` are required for creating
   pre-provisioning hooks. For more information about creating Lambda functions,
   see [Using AWS Lambda with
   the AWS Command Line Interface](../../../lambda/latest/dg/gettingstarted-awscli.md "../../../lambda/latest/dg/gettingstarted-awscli.md").

The following is an example of a Lambda function output:

```
{
  "allowProvisioning": True,
  "parameterOverrides": {
    "`incomingKey0`": "`incomingValue0`",
    "`incomingKey1`": "`incomingValue1`"
  }
}
```

2. AWS IoT uses resource-based policies to call Lambda, so you must give AWS IoT
   permission to call your Lambda function.

###### Important

Be sure to include the `source-arn` or
`source-account` in the global condition
context keys of the policies attached to your Lambda action to prevent
permission manipulation. For more information about this, see [Cross-service confused deputy
prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

The following is an example using [add-permission](../../../cli/latest/reference/lambda/add-permission.md "../../../cli/latest/reference/lambda/add-permission.md")
give IoT permission to your Lambda.

```
aws lambda add-permission \
    --function-name `myLambdaFunction` \
    --statement-id iot-permission \
    --action lambda:InvokeFunction \
    --principal iot.amazonaws.com
```

3. Add a pre-provisioning hook to a template using either the [create-provisioning-template](../../../cli/latest/reference/iot/create-provisioning-template.md "../../../cli/latest/reference/iot/create-provisioning-template.md") or [update-provisioning-template](../../../cli/latest/reference/iot/update-provisioning-template.md "../../../cli/latest/reference/iot/update-provisioning-template.md") command.

The following CLI example uses the [create-provisioning-template](../../../cli/latest/reference/iot/create-provisioning-template.md "../../../cli/latest/reference/iot/create-provisioning-template.md") to create a provisioning template
that has pre-provisioning hooks:

```
aws iot create-provisioning-template \
    --template-name `myTemplate` \
    --provisioning-role-arn `arn:aws:iam:us-east-1:1234564789012:role/myRole` \
    --template-body `file://template.json` \
    --pre-provisioning-hook `file://hooks.json`
```

The output of this command looks like the following:

```
{
    "templateArn": "`arn:aws:iot:us-east-1:1234564789012:provisioningtemplate/myTemplate`",
    "defaultVersionId": 1,
    "templateName": `myTemplate`
}
```

You can also load a parameter from a file instead of typing it all as a
command line parameter value to save time. For more information, see [Loading AWS CLI
Parameters from a File](../../../cli/latest/userguide/cli-usage-parameters-file.md "../../../cli/latest/userguide/cli-usage-parameters-file.md"). The following shows the
`template` parameter in expanded JSON format:

```
{
    "Parameters" : {
        "DeviceLocation": {
            "Type": "String"
        }
    },
    "Mappings": {
        "LocationTable": {
            "Seattle": {
                "LocationUrl": "https://example.aws"
            }
        }
    },
    "Resources" : {
        "thing" : {
            "Type" : "AWS::IoT::Thing",
            "Properties" : {
                "AttributePayload" : {
                    "version" : "v1",
                    "serialNumber" : "serialNumber"
                },
                "ThingName" : {"Fn::Join":["",["ThingPrefix_",{"Ref":"SerialNumber"}]]},
                "ThingTypeName" : {"Fn::Join":["",["ThingTypePrefix_",{"Ref":"SerialNumber"}]]},
                "ThingGroups" : ["widgets", "WA"],
                "BillingGroup": "BillingGroup"
            },
            "OverrideSettings" : {
                "AttributePayload" : "MERGE",
                "ThingTypeName" : "REPLACE",
                "ThingGroups" : "DO_NOTHING"
            }
        },
        "certificate" : {
            "Type" : "AWS::IoT::Certificate",
            "Properties" : {
                "CertificateId": {"Ref": "AWS::IoT::Certificate::Id"},
                "Status" : "Active",
                "ThingPrincipalType" : "EXCLUSIVE_THING"
            }
        },
        "policy" : {
            "Type" : "AWS::IoT::Policy",
            "Properties" : {
                "PolicyDocument" : {
                    "Version": "2012-10-17",
                    "Statement": [{
                        "Effect": "Allow",
                        "Action":["iot:Publish"],
                        "Resource": ["arn:aws:iot:us-east-1:504350838278:topic/foo/bar"]
                    }]
                }
            }
        }
    },
    "DeviceConfiguration": {
        "FallbackUrl": "https://www.example.com/test-site",
        "LocationUrl": {
            "Fn::FindInMap": ["LocationTable",{"Ref": "DeviceLocation"}, "LocationUrl"]}
    }
}
```

The following shows the `pre-provisioning-hook` parameter in
expanded JSON format:

```
{
     "targetArn" : "`arn:aws:lambda:us-east-1:765219403047:function:pre_provisioning_test`",
     "payloadVersion" : "`2020-04-01`"
}
```
