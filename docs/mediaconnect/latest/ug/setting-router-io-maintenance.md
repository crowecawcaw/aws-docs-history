

# Setting router I/O maintenance windows
<a name="setting-router-io-maintenance"></a>

You can configure a maintenance window for a router I/O when you create it, or update the window later. When creating a router I/O, you can specify a preferred day and time, or choose the default option to let MediaConnect select a schedule automatically.

**Note**  
You cannot change the maintenance schedule for a router I/O while it is active. You must stop the I/O first (placing it in Standby state) before you can update its maintenance configuration. After the I/O starts, the maintenance schedule is locked until the I/O is stopped again.

**To set or update a router I/O maintenance window (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. In the navigation pane, under **Global routing**, choose **Router inputs** or **Router outputs**.

1. Choose the input or output name to open its details page.

1. Choose **Edit**.

1. In the **Maintenance configuration** section, for **Maintenance type**, choose one of the following options:
   + **Default** – Let MediaConnect select maintenance scheduling preferences on your behalf.
   + **Preferred day and time** – Set a preferred day and time for scheduled maintenance.

1. If you chose **Preferred day and time**, specify the **Maintenance day** and **Maintenance time** (UTC).

1. Choose **Save changes**.

**To create a router I/O with a preferred maintenance window (AWS CLI)**  
Use the `create-router-input` or `create-router-output` command with the `--maintenance-configuration` parameter to specify a preferred day and time for maintenance.

The following example creates a router input with a preferred maintenance window of Sunday at 04:00 UTC:

```
aws mediaconnect create-router-input \
  --name StudioCam1 \
  --maximum-bitrate 50000000 \
  --routing-scope REGIONAL \
  --tier INPUT_50 \
  --configuration '{"Standard":{"NetworkInterfaceArn":"arn:aws:mediaconnect:us-east-1:111122223333:routerNetworkInterface:a1b2c3d4e5f6","ProtocolConfiguration":{"SrtListener":{"Port":5000,"MinimumLatencyMilliseconds":100}}}}' \
  --maintenance-configuration '{"PreferredDayTime":{"Day":"SUNDAY","Time":"04:00"}}'
```

The response includes the maintenance configuration:

```
{
    "RouterInput": {
        "Name": "StudioCam1",
        "Arn": "arn:aws:mediaconnect:us-east-1:111122223333:routerInput:a1b2c3d4e5f6",
        "State": "STANDBY",
        ...
        "MaintenanceType": "PREFERRED_DAY_TIME",
        "MaintenanceConfiguration": {
            "PreferredDayTime": {
                "Day": "SUNDAY",
                "Time": "04:00:00Z"
            }
        }
    }
}
```

**To create a router I/O with default maintenance (AWS CLI)**  
Use the `create-router-input` or `create-router-output` command with `--maintenance-configuration '{"Default":{}}'` to let MediaConnect select a maintenance schedule automatically.

The following example creates a router input with the default maintenance configuration:

```
aws mediaconnect create-router-input \
  --name StudioCam2 \
  --maximum-bitrate 50000000 \
  --routing-scope REGIONAL \
  --tier INPUT_50 \
  --configuration '{"Standard":{"NetworkInterfaceArn":"arn:aws:mediaconnect:us-east-1:111122223333:routerNetworkInterface:a1b2c3d4e5f6","ProtocolConfiguration":{"SrtListener":{"Port":5001,"MinimumLatencyMilliseconds":100}}}}' \
  --maintenance-configuration '{"Default":{}}'
```

The response includes the maintenance configuration:

```
{
    "RouterInput": {
        "Name": "StudioCam2",
        "Arn": "arn:aws:mediaconnect:us-east-1:111122223333:routerInput:g7h8i9j0k1l2",
        "State": "STANDBY",
        ...
        "MaintenanceType": "DEFAULT",
        "MaintenanceConfiguration": {
            "Default": {}
        }
    }
}
```

**To update a router I/O maintenance window (AWS CLI)**  
Use the `update-router-input` or `update-router-output` command with the `--maintenance-configuration` parameter to change the maintenance window. The I/O must be in Standby state.

The following example updates the maintenance window for a router input to Wednesday at 02:00 UTC:

```
aws mediaconnect update-router-input \
  --arn arn:aws:mediaconnect:us-east-1:111122223333:routerInput:a1b2c3d4e5f6 \
  --maintenance-configuration '{"PreferredDayTime":{"Day":"WEDNESDAY","Time":"02:00"}}'
```