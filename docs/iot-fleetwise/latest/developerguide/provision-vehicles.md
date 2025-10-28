# Provision AWS IoT FleetWise vehicles

The Edge Agent for AWS IoT FleetWise software running in your vehicle collects and transfers data to the cloud.
AWS IoT FleetWise integrates with AWS IoT Core to support secure communication between the Edge
Agent software and the cloud through MQTT. Each vehicle corresponds to an AWS IoT thing.
You can use an existing AWS IoT thing to create a vehicle or set AWS IoT FleetWise to
automatically create an AWS IoT thing for your vehicle. For more information, see [Create an AWS IoT FleetWise vehicle](create-vehicle.md "create-vehicle.md").

AWS IoT Core supports [authentication](../../../iot/latest/developerguide/authentication.md "../../../iot/latest/developerguide/authentication.md") and [authorization](../../../iot/latest/developerguide/iot-authorization.md "../../../iot/latest/developerguide/iot-authorization.md") that help securely control access to AWS IoT FleetWise resources.
Vehicles can use X.509 certificates to get authenticated (signed in) to use AWS IoT FleetWise
and AWS IoT Core policies to get authorized (have permissions) to perform specified
actions.

## Authenticate vehicles

You can create AWS IoT Core policies to authenticate your vehicles.

###### To authenticate your vehicle

- To create an AWS IoT Core policy, run the following command.
  - Replace `policy-name` with the name of
    the policy that you want to create.
  - Replace `file-name` with the name of the
    JSON file that contains the AWS IoT Core policy.

```
aws iot create-policy --policy-name `policy-name` --policy-document file://`file-name`.json
```

Before you use the example policy, do the following:

    + Replace `us-east-1` with the
     AWS Region where you created AWS IoT FleetWise
     resources.
    + Replace `111122223333` with
     your AWS account ID.This example includes topics reserved by AWS IoT FleetWise. You must add the topics to the policy. For more information, see [Reserved topics in AWS IoT FleetWise](reserved-topics.md "reserved-topics.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Connect"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:client/${iot:Connection.Thing.ThingName}"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Publish"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:topic/$aws/iotfleetwise/vehicles/${iot:Connection.Thing.ThingName}/checkins",
 "arn:aws:iot:`us-east-1`:`111122223333`:topic/$aws/iotfleetwise/vehicles/${iot:Connection.Thing.ThingName}/signals"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Subscribe"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:topicfilter/$aws/iotfleetwise/vehicles/${iot:Connection.Thing.ThingName}/collection_schemes",
 "arn:aws:iot:`us-east-1`:`111122223333`:topicfilter/$aws/iotfleetwise/vehicles/${iot:Connection.Thing.ThingName}/decoder_manifests"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Receive"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`111122223333`:topic/$aws/iotfleetwise/vehicles/${iot:Connection.Thing.ThingName}/collection_schemes",
 "arn:aws:iot:`us-east-1`:`111122223333`:topic/$aws/iotfleetwise/vehicles/${iot:Connection.Thing.ThingName}/decoder_manifests"
 ]
 }
 ]
}`

```

## Authorize vehicles

You can create X.509 certificates to authorize your vehicles.

###### To authorize your vehicle

###### Important

We recommend that you create a new certificate for each vehicle.

1. To create an RSA key pair and issue an X.509 certificate, run the
   following command.
   - Replace `cert` with the name of the file
     that saves the command output contents of certificatePem.
   - Replace `public-key` with the name of the
     file that saves the command output contents of
     keyPair.PublicKey.
   - Replace `private-key` with the name of
     the file that saves the command output contents of
     keyPair.PrivateKey.

```
aws iot create-keys-and-certificate \
    --set-as-active \
    --certificate-pem-outfile `cert`.pem \
    --public-key-outfile `public-key`.key" \
    --private-key-outfile  `private-key`.key"
```

2. Copy the Amazon Resource Name (ARN) of the certificate from the
   output.
3. To attach the policy to the certificate, run the following command.
   - Replace `policy-name` with the name of
     the AWS IoT Core policy that you created.
   - Replace `certificate-arn` with the ARN of
     the certificate that you copied.

```
aws iot attach-policy \
    --policy-name `policy-name`\
    --target "`certificate-arn`"
```

4. To attach the certificate to the thing, run the following command.
   - Replace `thing-name` with the name of
     your AWS IoT thing or the ID of your vehicle.
   - Replace `certificate-arn` with the ARN of
     the certificate that you copied.

```
aws iot attach-thing-principal \
    --thing-name `thing-name` \
    --principal "`certificate-arn`"
```
