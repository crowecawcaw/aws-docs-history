# Create an AWS IoT FleetWise vehicle

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can use the AWS IoT FleetWise console or API to create a vehicle.

###### Important

Before you start, check the following:

- You must have a vehicle model and the status of the vehicle model must be
  `ACTIVE`. For more information, see [Manage AWS IoT FleetWise vehicle models](vehicle-models.md "vehicle-models.md").
- Your vehicle model must be associated with a decoder manifest, and the
  status of the decoder manifest must be `ACTIVE`. For more
  information, see [Manage AWS IoT FleetWise decoder manifests](decoder-manifests.md "decoder-manifests.md").

###### Topics

- [Create a vehicle (console)](#create-vehicle-console "#create-vehicle-console")
- [Create a vehicle (AWS CLI)](#create-vehicle-cli "#create-vehicle-cli")

## Create a vehicle (console)

You can use the AWS IoT FleetWise console to create a vehicle.

###### To create a vehicle

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
2. On the navigation pane, choose **Vehicles**.
3. On the vehicle summary page, choose **Create vehicle**,
   and then do the following steps.

###### Topics

- [Step 1: Define vehicle properties](#define-vehicle-properties-console "#define-vehicle-properties-console")
- [Step 2: Configure vehicle certificate](#define-vehicle-certificate-console "#define-vehicle-certificate-console")
- [Step 3: Attach policies to certificate](#attach-vehicle-policy-console "#attach-vehicle-policy-console")
- [Step 4: Review and create](#review-and-create-vehicle-console "#review-and-create-vehicle-console")

### Step 1: Define vehicle properties

In this step, you name the vehicle and associate it with the model manifest and decoder manifest.

1. Enter a unique name for the vehicle.

###### Important

A vehicle corresponds to an AWS IoT thing. If a thing already exists with that name, choose **Associate the vehicle with an IoT thing** to update the thing with the vehicle. Or, choose a different vehicle name and AWS IoT FleetWise will automatically create a new thing for the vehicle. 2. Choose a vehicle model (model manifest) from the list. 3. Choose a decoder manifest from the list. The decoder manifest is associated with the vehicle model. 4. (Optional) To associate vehicle attributes, choose **Add
attributes**. If you skip this step, you must add
attributes after the vehicle is created before you can deploy it to
campaigns. 5. (Optional) To associate tags with the vehicle, choose **Add new
tag**. You can also add tags after the vehicle is
created. 6. Choose **Next**.

### Step 2: Configure vehicle certificate

To use your vehicle as an AWS IoT thing, you must configure a vehicle certificate
with an attached policy. If you skip this step, you must configure a certificate
after the vehicle is created before you can deploy it to campaigns.

1. Choose **Auto-generate a new certificate (recommended)**.
2. Choose **Next**.

### Step 3: Attach policies to certificate

Attach a policy to the certificate you configured in the previous step.

1. For **Policies**, enter an existing policy name. To
   create a new policy, choose **Create policy**.
2. Choose **Next**.

### Step 4: Review and create

Verify the configurations for the vehicle, and then choose
**Create vehicle**.

###### Important

After the vehicle is created, you must download the certificate and keys. You'll use the certificate and private key to connect the vehicle in the Edge Agent for AWS IoT FleetWise software.

## Create a vehicle (AWS CLI)

When you create a vehicle, you must use a vehicle model that is associated with a
decoder manifest. You can use the [CreateVehicle](../APIReference/API_CreateVehicle.md "../APIReference/API_CreateVehicle.md")
API operation to create a vehicle. The following example uses the AWS CLI.

To create a vehicle, run the following command.

Replace `file-name` with the name of the .json file that
contains the vehicle configuration.

```
aws iotfleetwise create-vehicle --cli-input-json file://`file-name`.json
```

###### Example – vehicle configuration

- (Optional) The `associationBehavior` value can be one of the
  following:

      + `CreateIotThing` – When your vehicle is created,
       AWS IoT FleetWise automatically creates an AWS IoT thing with the name of your
       vehicle ID for your vehicle.
      + `ValidateIotThingExists` – Use an existing AWS IoT
       thing to create a vehicle.


      To create an AWS IoT thing, run the following command. Replace
       `thing-name` with the name of the thing
       you want to create.



      ```
      aws iot create-thing --thing-name `thing-name`
      ```

  If it's not specified, AWS IoT FleetWise automatically creates an AWS IoT thing for
  your vehicle.

###### Important

Make sure that the AWS IoT thing is provisioned after the vehicle is
created. For more information, see [Provision AWS IoT FleetWise vehicles](provision-vehicles.md "provision-vehicles.md").

- Replace `vehicle-name` with one of the
  following.
  - The name of your AWS IoT thing if `associationBehavior`
    is configured to `ValidateIotThingExists`.
  - The ID of the vehicle to create if
    `associationBehavior` is configured to
    `CreateIotThing`.

  The vehicle ID can have 1–100 characters. Valid characters:
  a–z, A–Z, 0–9, dash (‐), underscore (\_),
  and colon (:).

- Replace `model-manifest-ARN` with the ARN of your
  vehicle model (model manifest).
- Replace `decoder-manifest-ARN` with the ARN of
  the decoder manifest associated with the specified vehicle model.
- (Optional) You can add additional attributes to distinguish this vehicle
  from other vehicles created from the same vehicle model. For example, if you
  have an electric car, you can specify the following value for an attribute:
  `{"fuelType": "electric"}`.

###### Important

Attributes must be defined in the associated vehicle model before you can add them to
individual vehicles.

```
{
    "associationBehavior": "`associationBehavior`",
    "vehicleName": "`vehicle-name`",
    "modelManifestArn": "`model-manifest-ARN`",
    "decoderManifestArn": "`decoder-manifest-ARN`",
    "attributes": {
        "`key`": "`value`"
    }
}
```

###### Example – associate a state template with the vehicle

You can associate [state templates](state-templates.md "state-templates.md") with
the vehicle to allow collection of state updates from the vehicle in the cloud by using the
`stateTemplates` field.

In this example, `stateTemplateUpdateStrategy`
can be one of:

- `periodic`: allows you to specify a fixed rate at which Edge Agent software
  will send signal updates to the cloud (Edge Agent software will send updates even if the
  signal value hasn't changed between updates).
- `onChange`: Edge Agent software will send signal updates whenever the signal
  changes.

```
aws iotfleetwise create-vehicle --cli-input-json file://`create-vehicle.json`
```

Where the `create-vehicle.json` file contains
(for example):

```
{
    "associationBehavior": "`associationBehavior`",
    "vehicleName": "`vehicle-name`",
    "modelManifestArn": "`model-manifest-ARN`",
    "decoderManifestArn": "`decoder-manifest-ARN`",
    "attributes": {
        "`key`": "`value`"
    },
    "stateTemplates": [
        {
            "identifier": "`state-template-name`",
            "stateTemplateUpdateStrategy": {
                "periodic": {
                    "stateTemplateUpdateRate": {
                        "unit": "`SECOND`",
                        "value": `10`
                    }
                }
            }
        }
    ]
}
```

If you [enabled encryption](key-management.md "key-management.md") using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `CreateVehicle` API operation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey*",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS_KEY_ID`"
 ]
 }
 ]
}`

```
