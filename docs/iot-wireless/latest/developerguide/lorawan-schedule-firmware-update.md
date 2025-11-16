# Schedule and run gateway firmware

update task

If you have the firmware update file and signature, you can schedule and run the
task definition to update the gateway firmware, as described in this page. If you
don't have the firmware update files, see [(Optional) Generate the firmware
update file and signature](lorawan-script-fwupdate-sigkey.md "lorawan-script-fwupdate-sigkey.md") for an example that you can use
to adapt to your application.

The following steps show you how to create a wireless gateway task definition to
update the gateway firmware.

###### Topics

- [What's a wireless gateway
  task definition?](#lorawan-firmware-task-definition "#lorawan-firmware-task-definition")
- [Get the current firmware
  version running on your gateway](#lorawan-gateway-current-version "#lorawan-gateway-current-version")
- [Schedule gateway firmware
  update using a task definition](#lorawan-create-task-definition "#lorawan-create-task-definition")
- [Run the firmware update task and
  track progress](#lorawan-run-fwupdate-task "#lorawan-run-fwupdate-task")

## What's a wireless gateway

task definition?

To update the gateway firmware, you create a task definition. You can use the
task definition to include details about the firmware update and define the
update. AWS IoT Core for LoRaWAN provides a firmware update based on information from the
following three fields associated with the gateway.

- ###### LoRa Basics Station

The version and build time of the Basics Station software. To
identify this information, you can also generate it by using the
Basics Station software that is being run by your gateway (for
example, `2.0.5(rpi/std) 2021-03-09 03:45:09`).

- ###### Package version

The firmware version, specified by the file
`version.txt` in the gateway. While this information
might not be present in the gateway, you must specify this field as
it provides a way to define your firmware version (for example,
`1.0.0`).

- ###### Gateway platform model

The platform or model that is being used by the gateway (for
example, Linux).

## Get the current firmware

version running on your gateway

To determine your gateway's eligibility for a firmware update, the CUPS server
checks all three fields, **LoRa Basics Station**,
**Package version**, and **Gateway platform
model**, for a match when the gateway presents them during a CUPS
request. These fields are stored as part of the current version of a wireless
gateway task definition.

You can determine the current firmware version running on the gateway from the
console or the CLI.

When you use the AWS Management Console, you can obtain the firmware version from
the details page of the gateway for which you're retrieving this
information.

1. Go to the [Gateways hub](https://console.aws.amazon.com/iot/home#/wireless/gateways "https://console.aws.amazon.com/iot/home#/wireless/gateways") page
   of the AWS IoT console and choose the gateway for which you're
   retrieving this information.
2. Go to the **Firmware** tab in the details
   page of the gateway to see the current firmware version and the
   status information that indicates whether a firmware update is
   pending.
   When you use the AWS IoT Wireless API or the AWS CLI, you can obtain
   this information using the `CurrentVersion` field that's
   stored as part of the task definition. The following steps use the CLI
   to demonstrate how you can get this information.

3. ###### Obtain wireless gateway ID

First, obtain the unique identifier of the gateway for which
you want to retrieve the current firmware version. If you've
already provisioned a gateway, you can get information about the
gateway using the [`GetWirelessGateway`](../apireference/API_GetWirelessGateway.md "../apireference/API_GetWirelessGateway.md") API operation
or the [`get-wireless-gateway`](../../../cli/latest/reference/iotwireless/get-wireless-gateway.md "../../../cli/latest/reference/iotwireless/get-wireless-gateway.md") CLI
command.

```
aws iotwireless get-wireless-gateway \
    --identifier 5a11b0a85a11b0a8 \
        --identifier-type GatewayEui
```

Following shows a sample output for the command.

```
{
    "Name": "Raspberry pi",
    "Id": "1352172b-0602-4b40-896f-54da9ed16b57",
    "Description": "Raspberry pi",
    "LoRaWAN": {
        "GatewayEui": "5a11b0a85a11b0a8",
        "RfRegion": "US915"
    },
    "Arn": "arn:aws:iotwireless:us-east-1:231894231068:WirelessGateway/1352172b-0602-4b40-896f-54da9ed16b57"
}
```

2. ###### Get gateway firmware version

Using the wireless gateway ID reported by the
`get-wireless-gateway` command, you can use the
[get-wireless-gateway-firmware-information](../../../cli/latest/reference/iotwireless/get-wireless-gateway-firmware-information.md "../../../cli/latest/reference/iotwireless/get-wireless-gateway-firmware-information.md") command
to get the `CurrentVersion`.

```
aws iotwireless get-wireless-gateway-firmware-information \
    --id "3039b406-5cc9-4307-925b-9948c63da25b"
```

Following shows a sample output for the command, with
information from all three fields displayed by the
`CurrentVersion`.

```
{
    "LoRaWAN": {
        "CurrentVersion": {
            "PackageVersion": "1.0.0",
            "Model": "rpi",
            "Station": "2.0.5(rpi/std) 2021-03-09 03:45:09"
        }
    }
}
```

## Schedule gateway firmware

update using a task definition

Now that you've verified the eligibility of the firmware update, you can
schedule a firmware update task using a wireless gateway task definition and
then run the update.

To update the gateway firmware, you'll need a wireless gateway task
definition. You can use the AWS IoT console or the AWS CLI to update the gateway
firmware.

To schedule a firmware update task from the console:

1. Go to the [Gateways hub](https://console.aws.amazon.com/iot/home#/wireless/gateways "https://console.aws.amazon.com/iot/home#/wireless/gateways") page
   of the AWS IoT console and choose the gateway for which you're
   updating the firmware.
2. Go to the **Firmware** tab in the details
   page of the gateway and choose **Update
   firmware**.
3. Create a wireless gateway task, or choose an existing task
   definition if you have already created one.

If you have already created a task definition, choose
**Use an existing task**. Information
about the task definition will appear here, such as the
**Package version**, the location for the
firmware file in Amazon S3, and the status of the update. You can
review the information and then choose **Update
firmware**.

#### Create a

gateway task definition

If you're creating a new task definition, you'll need to perform
the steps described below to specify the location to your firmware
file in Amazon S3, and the IAM role that grants AWS IoT Core for LoRaWAN
permission to access the file and perform the update.

In the **Update firmware** page of the console,
choose **Create a new task**, and then perform
the following steps.

1. ###### Specify firmware file and location in Amazon S3

You can use an Amazon Simple Storage Service bucket to store the firmware
update files. Specify the location to your firmware file in
Amazon S3, and provide the IAM role that grants AWS IoT Core for LoRaWAN
permission to access the file and perform the update.

    * If you have already uploaded the file to Amazon S3,
     choose **Select an existing firmware
     file**. You can then **Browse
     S3** and provide the S3 URI to the
     file.
    * If you haven't already uploaded the file to Amazon S3,
     choose **Upload a new firmware
     file**. You can then upload the firmware
     file and **Browse S3** to choose
     the Amazon S3 bucket where the file will be
     uploaded.

2. ###### (Optional) Provide additional firmware verification
   settings

Optionally, if your firmware update was signed, you can
use the additional settings to specify the update signature
and CRC. These settings can be used to verify the
authenticity and integrity of the signed update. It also
ensures that the code was not corrupted or altered, and the
devices run code that's published only by trusted authors.
The update signature and CRC will be passed to AWS IoT Core for LoRaWAN
when updating the firmware using CUPS. 3. ###### (Optional) Provide additional setting to automatically
create update tasks

Optionally, we recommend that you choose to specify
automatic creation of tasks for all gateways by using the
`Auto create tasks and update all like
 gateways` parameter. This parameter applies to any
gateway that has a match for all three parameters mentioned
previously in [What's a wireless gateway
task definition?](#lorawan-firmware-task-definition "#lorawan-firmware-task-definition"). If
this parameter is disabled, the parameters have to be
manually assigned to the gateway. 4. ###### Permissions to access the bucket

You can either create a new service role or choose an
existing role to allow AWS IoT Core for LoRaWAN to access the firmware
update file in the Amazon S3 bucket on your behalf.

To create a new role, you can enter a role name or leave
it blank for a random name to be generated automatically. To
view the policy permissions that grant access to the Amazon S3
bucket, choose **View policy
permissions**.

You can create the wireless gateway task definition by using the
AWS IoT Wireless API or the AWS CLI. The following steps show how to
create the task definition using the CLI.

###### Note

When you create the task definition, we recommend that you specify
automatic creation of tasks by using the
`AutoCreateTasks` parameter. This parameter applies
to any gateway that has a match for all three parameters mentioned
previously in [What's a wireless gateway
task definition?](#lorawan-firmware-task-definition "#lorawan-firmware-task-definition"). If this
parameter is disabled, the parameters have to be manually assigned
to the gateway.

#### Pre-requisites

Before you use the AWS CLI to update the firmware, you must have
uploaded the firmware file to an Amazon S3 bucket, and created an IAM
role that grants AWS IoT Core for LoRaWAN permission to access the file in the
Amazon S3 bucket for performing the update. If you've already uploaded
the firmware file and the IAM role, proceed to [Run
firmware update task](#lorawan-create-task-definition-cli-run "#lorawan-create-task-definition-cli-run") to run
the firmware update task.

If you haven't already uploaded the firmware file and specified
the IAM role, perform the steps described in [Upload the firmware file to an
Amazon S3 bucket and add an IAM role](lorawan-upload-firmware-s3bucket.md "lorawan-upload-firmware-s3bucket.md")8 and then run
the firmware update task.

#### Run

firmware update task

To run the firmware update task, perform the following
steps.

1. ###### Specify the input parameters for the update task

Create a file, `input.json`, that'll contain
the information to pass to the
`CreateWirelessGatewayTaskDefinition` API. In
the `input.json` file, provide the following
information that you obtained earlier:

    * ###### UpdateDataSource


    Provide the link to your object containing the
     firmware update file that you uploaded to the S3
     bucket. (for example,
     `s3://iotwirelessfwupdate/fwstation`.
    * ###### UpdateDataRole


    Provide the link to the Role ARN for the IAM
     role that you created, which provides permissions
     to read the S3 bucket. (for example,
     `arn:aws:iam::123456789012:role/IoTWirelessFwUpdateRole`.
    * ###### SigKeyCRC and UpdateSignature


    This information might be provided by your
     gateway manufacturer, but if you followed the
     procedure described in [(Optional) Generate the firmware
     update file and signature](lorawan-script-fwupdate-sigkey.md "lorawan-script-fwupdate-sigkey.md"),
     you'll find this information when generating the
     signature.
    * ###### CurrentVersion


    Provide the `CurrentVersion` output
     that you obtained previously by running the
     `get-wireless-gateway-firmware-information`  command.



    ```
    cat input.json
    ```

    Following shows the contents of the
     `input.json` file.



    ```
    {
        "AutoCreateTasks": true,
        "Name": "FirmwareUpdate",
        "Update":
        {
            "UpdateDataSource" : "s3://iotwirelessfwupdate/fwstation",
            "UpdateDataRole" : "arn:aws:iam::123456789012:role/IoTWirelessFwUpdateRole",
            "LoRaWAN" :
            {
                "SigKeyCrc": 3434210794,
                "UpdateSignature": "MEQCIDPY/p2ssgXIPNCOgZr+NzeTLpX+WfBo5tYWbh5pQWN3AiBROen+XlIdMScvAsfVfU/ZScJCalkVNZh4esyS8mNIgA==",
                "CurrentVersion" :
                {
                "PackageVersion": "1.0.0",
                "Model": "rpi",
                "Station": "2.0.5(rpi/std) 2021-03-09 03:45:09"
                }
            }
        }
    }
    ```

2. ###### Create the gateway task definition

Pass the `input.json` file to the [create-wireless-gateway-task-definition](../../../cli/latest/reference/iotwireless/get-wireless-gateway-task-definition.md "../../../cli/latest/reference/iotwireless/get-wireless-gateway-task-definition.md") command
to create the task definition.

```
aws iotwireless create-wireless-gateway-task-definition \
    --cli-input-json file://input.json
```

Following shows the output of the command.

```
{
    "Id": "4ac46ff4-efc5-44fd-9def-e8517077bb12",
    "Arn": "arn:aws:iotwireless:us-east-1:231894231068:WirelessGatewayTaskDefinition/4ac46ff4-efc5-44fd-9def-e8517077bb12"
}
```

## Run the firmware update task and

track progress

The gateway is ready to receive the firmware update and, once powered on, it
connects to the CUPS server. When the CUPS server finds a match in the version
of the gateway, it schedules a firmware update.

A task is a task definition in process. The firmware update task starts as
soon as a matching gateway for the update is found by the CUPS server. You can
track the progress of the update task on the gateway from the console or the
CLI.

When you use the AWS Management Console, you can track the progress of the firmware
update from the details page of the gateway for which you're retrieving
this information. Go to the [Gateways hub](https://console.aws.amazon.com/iot/home#/wireless/gateways "https://console.aws.amazon.com/iot/home#/wireless/gateways") page, choose
the gateway for which you're tracking the update, and then go to the
**Firmware** tab to see the update status.

If the firmware update fails the first time, you'll see a status of
**Retrying**, and the gateway sends
the same request. If the CUPS server is unable to connect to the gateway
after a second retry, it will show a status of **FAILED**.

You can track the progress of the task by using the
`GetWirelessGatewayTask` API. When you run the [get-wireless-gateway-task](../../../cli/latest/reference/iotwireless/get-wireless-gateway-task.md "../../../cli/latest/reference/iotwireless/get-wireless-gateway-task.md") command the
first time, it will show the task status as
`IN_PROGRESS`.

```
aws iotwireless get-wireless-gateway-task \
    --id 1352172b-0602-4b40-896f-54da9ed16b57
```

Following shows the output of the command.

```
{
    "WirelessGatewayId": "1352172b-0602-4b40-896f-54da9ed16b57",
    "WirelessGatewayTaskDefinitionId": "ec11f9e7-b037-4fcc-aa60-a43b839f5de3",
    "LastUplinkReceivedAt": "2021-03-12T09:56:12.047Z",
    "TaskCreatedAt": "2021-03-12T09:56:12.047Z",
    "Status": "IN_PROGRESS"
}
```

When you run the command the next time, if the firmware update takes
effect, it will show the updated fields, `Package`,
`Version`, and `Model` and the task status
changes to `COMPLETED`.

```
aws iotwireless get-wireless-gateway-task \
    --id 1352172b-0602-4b40-896f-54da9ed16b57
```

Following shows the output of the command.

```
{
    "WirelessGatewayId": "1352172b-0602-4b40-896f-54da9ed16b57",
    "WirelessGatewayTaskDefinitionId": "ec11f9e7-b037-4fcc-aa60-a43b839f5de3",
    "LastUplinkReceivedAt": "2021-03-12T09:56:12.047Z",
    "TaskCreatedAt": "2021-03-12T09:56:12.047Z",
    "Status": "COMPLETED"
}
```

In this example, we showed you the firmware update using the Raspberry
Pi based RAKWireless gateway. The firmware update script stops the
running BasicStation to store the updated `Package`,
`Version`, and `Model` fields so BasicStation
will have to be restarted.

```
2021-03-12 09:56:13.108 [CUP:INFO] CUPS provided update.bin
2021-03-12 09:56:13.108 [CUP:INFO] CUPS provided signature len=70 keycrc=37316C36
2021-03-12 09:56:13.148 [CUP:INFO] ECDSA key#0 -> VERIFIED
2021-03-12 09:56:13.148 [CUP:INFO] Running update.bin as background process
2021-03-12 09:56:13.149 [SYS:VERB] /tmp/update.bin: Forked, waiting...
2021-03-12 09:56:13.151 [SYS:INFO] Process /tmp/update.bin (pid=6873) completed
2021-03-12 09:56:13.152 [CUP:INFO] Interaction with CUPS done - next regular check in 10s
```

If the firmware update fails, you see a status of
`FIRST_RETRY` from the CUPS server, and the gateway sends
the same request. If the CUPS server is unable to connect to the gateway
after a `SECOND_RETRY`, it will show a status of
`FAILED`.

After the previous task was `COMPLETED` or
`FAILED`, delete the old task by using the [delete-wireless-gateway-task](../../../cli/latest/reference/iotwireless/delete-wireless-gateway-task.md "../../../cli/latest/reference/iotwireless/delete-wireless-gateway-task.md") command
before starting a new one.

```
aws iotwireless delete-wireless-gateway-task \
    --id 1352172b-0602-4b40-896f-54da9ed16b57
```
