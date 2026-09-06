

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Create an AWS IoT FleetWise vehicle model
<a name="create-vehicle-model"></a>

You can use the AWS IoT FleetWise console or API to create vehicle models. 

**Topics**
+ [Create a vehicle model (console)](#create-vehicle-model-console)
+ [Create a vehicle model (AWS CLI)](#create-vehicle-model-cli)

## Create a vehicle model (console)
<a name="create-vehicle-model-console"></a>

In the AWS IoT FleetWise console, you can create a vehicle model in the following ways:
+ [Use a template provided by AWS](#use-obd-template)
+ [Manually create a vehicle model](#manually-create-vehicle-model)
+ [Duplicate a vehicle model](#duplicate-vehicle-model)

### Use a template provided by AWS
<a name="use-obd-template"></a>

AWS IoT FleetWise provides an On-board Diagnostic (OBD) II, J1979 template that automatically creates a signal catalog, a vehicle model, and a decoder manifest for you. The template also adds OBD network interfaces to the decoder manifest. For more information, see [Manage AWS IoT FleetWise decoder manifests](decoder-manifests.md).

**To create a vehicle model by using a template**

1. <a name="fleetwise-open-console"></a>Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. <a name="choose-vehicle-models"></a>On the navigation pane, choose **Vehicle models**.

1. On the **Vehicle models** page, choose **Add provided template**.

1. Choose **On-board diagnostics (OBD) II**.

1. Enter a name for the OBD network interface that AWS IoT FleetWise is creating.

1. Choose **Add**.

### Manually create a vehicle model
<a name="manually-create-vehicle-model"></a>

You can add signals from the signal catalog or import signals by uploading one or more .dbc files. A .dbc file is a file format that Controller Area Network (CAN bus) databases support.

**Important**  
You can't create a vehicle model with vision system data signals using the AWS IoT FleetWise console. Instead, use the AWS CLI to create a vehicle model.  
Vision system data is in preview release and is subject to change.

**To manually create a vehicle model**

1. <a name="fleetwise-open-console"></a>Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. <a name="choose-vehicle-models"></a>On the navigation pane, choose **Vehicle models**.

1. On the **Vehicle models** page, choose **Create vehicle model**, and then do the following.

**Topics**
+ [Step 1: Configure vehicle model](#configure-vehicle-model-console)
+ [Step 2: Add signals](#add-signals-console)
+ [Step 3: Import signals](#import-signals-console)
+ [(Optional) Step 4: Add attributes](#add-attrobutes-console)
+ [Step 5: Review and create](#review-and-create-vehicle-model)

#### Step 1: Configure vehicle model
<a name="configure-vehicle-model-console"></a>

In **General information**, do the following.

1. Enter a name for the vehicle model.

1. (Optional) Enter a description.

1. Choose **Next**.

#### Step 2: Add signals
<a name="add-signals-console"></a>

**Note**  
If this is the first time you've used AWS IoT FleetWise, this step isn't available until you have a signal catalog. When the first vehicle model is created, AWS IoT FleetWise automatically creates a signal catalog with signals added to the first vehicle model.
If you're experienced with AWS IoT FleetWise, you can add signals to your vehicle model by selecting signals from the signal catalog or uploading .dbc files to import signals.
You must have at least one signal to create a vehicle model.

**To add signals**

1. Choose one or more signals from the signal catalog that you're adding to the vehicle model. You can review selected signals in the right pane.
**Note**  
Only selected signals will be added to the vehicle model.

1. Choose **Next**.

#### Step 3: Import signals
<a name="import-signals-console"></a>

**Note**  
If this is the first time you've used AWS IoT FleetWise, you must upload at least one .dbc file to import signals.
If you're experienced with AWS IoT FleetWise, you can add signals to your vehicle model by selecting signals from the signal catalog or uploading .dbc files to import signals.
You must have at least one signal to create a vehicle model.

**To import signals**

1. Choose **Choose files**.

1. In the dialog box, choose the .dbc file that contains signals. You can upload multiple .dbc files.

1. AWS IoT FleetWise parses your .dbc files to retrieve signals. 

   In the **Signals** section, specify the following metadata for each signal.
   + **Name** – The signal's name.

     The signal name must be unique. The signal name plus the path can have up to 150 characters. Valid characters: a–z, A–Z, 0–9, : (colon), and \_ (underscore).
   + **Data type** – The signal's data type must be one of the following: INT8, UINT8, INT16, UINT16, INT32, UINT32, INT64, UINT64, BOOLEAN, FLOAT, DOUBLE, STRING, UNIX\_TIMESTAMP, INT8\_ARRAY, UINT8\_ARRAY, INT16\_ARRAY, UINT16\_ARRAY, INT32\_ARRAY, UINT32\_ARRAY, INT64\_ARRAY, UINT64\_ARRAY, BOOLEAN\_ARRAY, FLOAT\_ARRAY, DOUBLE\_ARRAY, STRING\_ARRAY, UNIX\_TIMESTAMP\_ARRAY, or UNKNOWN.
   + **Signal type** – The type of the signal, which can be **Sensor** or **Actuator**.
   + (Optional) **Unit** – The scientific unit for the signal, such as km or Celsius.
   + (Optional) **Path** – The path to the signal. Similar to JSONPath, use a dot(.) to refer to a child signal. For example, **Vehicle.Engine.Light**.

     The signal name plus the path can have up to 150 characters. Valid characters: a–z, A–Z, 0–9, : (colon), and \_ (underscore).
   + (Optional) **Min** – The minimum value of the signal.
   + (Optional) **Max** – The maximum value of the signal.
   + (Optional) **Description** – The description for the signal.

     The description can have up to 2048 characters. Valid characters: a–z, A–Z, 0–9, : (colon), \_ (underscore), and - (hyphen).

1. Choose **Next**.

#### (Optional) Step 4: Add attributes
<a name="add-attrobutes-console"></a>

You can add up to 100 attributes, including the existing attributes in the signal catalog.

**To add attributes**

1. In **Add attributes**, specify the following metadata for each attribute.
   + **Name** – The attribute's name.

     The signal name must be unique. The signal name and path can have up to 150 characters. Valid characters: a–z, A–Z, 0–9, : (colon), and \_ (underscore)
   + **Data type** – The attribute's data type must be one of the following: INT8, UINT8, INT16, UINT16, INT32, UINT32, INT64, UINT64, BOOLEAN, FLOAT, DOUBLE, STRING, UNIX\_TIMESTAMP, INT8\_ARRAY, UINT8\_ARRAY, INT16\_ARRAY, UINT16\_ARRAY, INT32\_ARRAY, UINT32\_ARRAY, INT64\_ARRAY, UINT64\_ARRAY, BOOLEAN\_ARRAY, FLOAT\_ARRAY, DOUBLE\_ARRAY, STRING\_ARRAY, UNIX\_TIMESTAMP\_ARRAY, or UNKNOWN
   + (Optional) **Unit** – The scientific unit for the attribute, such as km or Celsius.
   + (Optional) **Path** – The path to the signal. Similar to JSONPath, use a dot(.) to refer to a child signal. For example, **Vehicle.Engine.Light**.

     The signal name plus the path can have up to 150 characters. Valid characters: a–z, A–Z, 0–9, : (colon), and \_ (underscore)
   + (Optional) **Min** – The minimum value of the attribute.
   + (Optional) **Max** – The maximum value of the attribute.
   + (Optional) **Description** – The description for the attribute.

     The description can have up to 2048 characters. Valid characters: a–z, A–Z, 0–9, : (colon), \_ (underscore), and - (hyphen).

1. Choose **Next**.

#### Step 5: Review and create
<a name="review-and-create-vehicle-model"></a>

Verify the configurations for the vehicle model, and then choose **Create**.

### Duplicate a vehicle model
<a name="duplicate-vehicle-model"></a>

AWS IoT FleetWise can copy the configurations of an existing vehicle model to create a new model. Signals specified in the selected vehicle model are copied to the new vehicle model. 

**To duplicate a vehicle model**

1. <a name="fleetwise-open-console"></a>Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise).

1. <a name="choose-vehicle-models"></a>On the navigation pane, choose **Vehicle models**.

1. Choose a model from the vehicle model list, and then choose **Duplicate model**.

To configure the vehicle model, follow the [Manually create a vehicle model](#manually-create-vehicle-model) tutorial.

It can take a few minutes for AWS IoT FleetWise to process your request to create the vehicle model. After the vehicle model is successfully created, on the **Vehicle models** page, the **Status** column shows **ACTIVE**. When the vehicle model becomes active, you can't edit it.

## Create a vehicle model (AWS CLI)
<a name="create-vehicle-model-cli"></a>

You can use the [CreateModelManifest](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateModelManifest.html) API operation to create vehicle models (model manifests). The following example uses the AWS CLI. 

**Important**  
You must have a signal catalog before you can create a vehicle model using the `CreateModelManifest` API operation. For more information about how to create a signal catalog, see [Create an AWS IoT FleetWise signal catalog](create-signal-catalog.md).

To create a vehicle model, run the following command.

Replace {{vehicle-model-configuration}} with the name of the .json file that contains the configuration.

```
aws iotfleetwise create-model-manifest --cli-input-json file://{{vehicle-model-configuration}}.json
```

### Vehicle model configuration
<a name="vehicle-model-configuration"></a>
+ Replace {{vehicle-model-name}} with the name of the vehicle model that you're creating.
+ Replace {{signal-catalog-ARN}} with the Amazon Resource Name (ARN) of the signal catalog.
+ (Optional) Replace {{description}} with a description to help you identify the vehicle model.

For more information about how to configure branches, attributes, sensors, and actuators, see [Configure AWS IoT FleetWise signals](define-signal.md).

```
{
    "name": "{{vehicle-model-name}}",
    "signalCatalogArn": "{{signal-catalog-ARN}}", 
    "description": "{{description}}",
    "nodes": ["Vehicle.Chassis"]
}
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `CreateModelManifest` API operation. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey*",
                "kms:Decrypt"
            ],
            "Resource": [
                "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{KMS_KEY_ID}}"
            ]
        }
    ]
}
```

------