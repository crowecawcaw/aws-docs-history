# Configure provisioners for WiFi Simple Setup

**On this page:**

- [Provisioner requirements](#managedintegrations-sdk-v2-cookbook-wss-provisioner-requirements "#managedintegrations-sdk-v2-cookbook-wss-provisioner-requirements")
- [Enable provisioner capability](#managedintegrations-sdk-v2-cookbook-wss-enable-provisioner "#managedintegrations-sdk-v2-cookbook-wss-enable-provisioner")
- [Provisioner setup workflow](#managedintegrations-sdk-v2-cookbook-wss-provisioner-setup-workflow "#managedintegrations-sdk-v2-cookbook-wss-provisioner-setup-workflow")
- [WiFi credential access](#managedintegrations-sdk-v2-cookbook-wss-wifi-credential-access "#managedintegrations-sdk-v2-cookbook-wss-wifi-credential-access")
- [Verify provisioner status](#managedintegrations-sdk-v2-cookbook-wss-verify-provisioner-status "#managedintegrations-sdk-v2-cookbook-wss-verify-provisioner-status")
- [Disable provisioner capability](#managedintegrations-sdk-v2-cookbook-wss-disable-provisioner "#managedintegrations-sdk-v2-cookbook-wss-disable-provisioner")

## Provisioner requirements

Provisioner devices must meet these requirements to support WiFi Simple Setup.

### Hardware and connectivity

- Hub SDK integration completed
- WiFi connectivity to network
- Software access point (SoftAP) creation capability
- Sufficient system resources for temporary network services

### Software and security

- Access to local WiFi credentials via customer-provided API
- Ability to create restricted SOCKS5 proxy (port 1080)
- TLS 1.2/1.3 with Pre-Shared Key (PSK) support for credential exchange (port 4433)

### Registration requirements

- Registered as managed integrations CONTROLLER role
- Associated with a credential locker
- Device status: DISCOVERED or ACTIVATED

## Enable provisioner capability

Enable WSS provisioner functionality using CreateManagedThing or UpdateManagedThing APIs.

### For new devices

```

{
  "role": "CONTROLLER",
  "credentialLockerId": "ad5cdc9f786b4dbe9490e57c0b1d900e",
  "authenticationMaterialType": "WIFI_SETUP_QR_BAR_CODE",
  "authenticationMaterial": "SN:12345679012;UPC:987654321012",
  "wiFiSimpleSetupConfiguration": {
    "enableAsProvisioner": true
  }
}

```

### For existing devices

```

{
  "managedThingId": "existing-hub-id",
  "wiFiSimpleSetupConfiguration": {
    "enableAsProvisioner": true
  }
}

```

**Parameters:**

- `enableAsProvisioner`: Boolean flag enabling WSS provisioner capability (default: false)

## Provisioner setup workflow

Configure a hub as WSS provisioner following these steps:

### Step 1: Register and enable

Register hub with CreateManagedThing API:

- Set role as "CONTROLLER"
- Specify credential locker ID for household association
- Include `wiFiSimpleSetupConfiguration` with `enableAsProvisioner: true`
- Or use UpdateManagedThing for existing devices

### Step 2: Configure WiFi credentials path

Configure the path to your WiFi credentials file in iotmi_config.json to enable the provisioner to access WiFi credentials (SSID and password) for sharing with new devices.

Add the `wss_local_wifi_cred_path` parameter to the `ro` (read-only) section of your iotmi_config.json file:

```

{
  "ro": {
    "wss_local_wifi_cred_path": "/etc/wpa_supplicant/wpa_supplicant-wlan0.conf"
  }
}

```

**Parameters:**

- `wss_local_wifi_cred_path`: File path to the wpa_supplicant configuration file containing WiFi credentials

This configuration is required for the Hub SDK to access your WiFi credentials during the provisioning process.

### Step 3: Capability reporting

Hub SDK automatically evaluates and reports capabilities:

- Hub assesses WiFi credential access
- Hub validates SoftAP creation capability
- Hub reports `supportAsProvisioner` status to cloud
- Cloud validates hub can function as provisioner

### Step 4: Activation

Cloud confirms provisioner status:

- Hub becomes ready to receive provisioning requests
- Hub receives notifications for pending devices in same credential locker
- Hub can begin provisioning new devices

## WiFi credential access

Provisioners must provide access to WiFi credentials for sharing with provisionee devices.

### Implementation requirements

Implement a customer API that returns WiFi SSID and password:

- API accessible by Hub SDK components
- Read from system configuration files (e.g., `/etc/wpa_supplicant/wpa_supplicant.conf`)
- Handle appropriate file permissions

### Security controls

**Access restrictions:**

- SSH access from SoftAP disabled by default
- WiFi credentials transmitted only over TLS 1.2/1.3 with PSK (port 4433)
- Session tokens are cryptographically secure (256-bit entropy), device-pair specific, single-use (5-minute validity)
- Session tokens distributed via cloud MQTT messaging for mutual authentication
- Credential access logged for security audit

**Implementation approaches:**

- Direct file system access with appropriate permissions
- System API calls for network configuration
- Custom credential management service with secure retrieval

## Verify provisioner status

Monitor two configuration states to ensure proper provisioner functionality.

### Configuration states

WSS provisioners have two critical state values that determine functionality:

| Provisioner configuration states | State                           | Description                                       | Source                                                      | Purpose |
| -------------------------------- | ------------------------------- | ------------------------------------------------- | ----------------------------------------------------------- | ------- |
| **enableAsProvisioner**          | Customer's configuration intent | Set via CreateManagedThing/UpdateManagedThing API | Enables WSS provisioner role for device                     |
| **supportAsProvisioner**         | Actual device capability        | Self-reported by hub after capability assessment  | Indicates if device can technically function as provisioner |

**Key distinction:**

- `enableAsProvisioner=true` + `supportAsProvisioner=false` = WSS will not work (device configured but incapable)
- `enableAsProvisioner=true` + `supportAsProvisioner=true` = WSS ready and functional
- Both must be true for successful provisioning operations

**Default values:**

- `enableAsProvisioner`: false (must be explicitly enabled)
- `supportAsProvisioner`: true for hub controllers, false for standard WiFi devices (determined by device assessment)

**Troubleshooting:** If `enableAsProvisioner=true` but `supportAsProvisioner=false`, check WiFi credential access and SoftAP capability.

### Status notifications

**Supported:**

```

{
  "notificationType": "WSS_SUPPORTED",
  "managedThingId": "hub-device-id",
  "timestamp": "2025-06-04T20:22:04Z",
  "message": "Device can function as WSS provisioner"
}

```

**Not supported:**

```

{
  "notificationType": "WSS_NOT_SUPPORTED",
  "managedThingId": "hub-device-id",
  "timestamp": "2025-06-04T20:22:04Z",
  "reason": "NO_WIFI_CREDENTIAL_ACCESS",
  "message": "Device cannot function as WSS provisioner"
}

```

### Common unsupported reasons

- No WiFi credential access configured
- Customer WiFi API not implemented
- Cannot create SoftAP
- Ethernet-only connection without WiFi radio
- Insufficient system resources

### Verification steps

1. **Call GetManagedThing API** to check configuration and status:

```

{
  "managedThingId": "hub-device-id",
  "role": "CONTROLLER",
  "credentialLockerId": "ad5cdc9f786b4dbe9490e57c0b1d900e",
  "authenticationMaterialType": "WIFI_SETUP_QR_BAR_CODE",
  "authenticationMaterial": "SN:12345679012;UPC:987654321012",
  "wiFiSimpleSetupConfiguration": {
    "enableAsProvisioner": true,
    "supportAsProvisioner": true,
    "enableAsProvisionee": false,
    "wssExpirationTimeStamp": null
  }
}

```

**Key fields:**

    * `enableAsProvisioner`: Customer configuration setting
    * `supportAsProvisioner`: Device-reported capability status
    * `wssExpirationTimeStamp`: Present only for provisionee devices with active WSS window

2. **Review cloud notifications** for capability reporting
3. **Verify WiFi credential API** returns valid credentials
4. **Check hub logs** for capability assessment details

## Disable provisioner capability

Disable WSS provisioner functionality when no longer needed. Using UpdateManagedThing API.

```

{
  "managedThingId": "hub-device-id",
  "wiFiSimpleSetupConfiguration": {
    "enableAsProvisioner": false
  }
}

```

### Impact of disabling

- Cloud updates `enableAsProvisioner` to false
- Hub stops receiving new provisioning notifications
- Pending provisioning operations cancelled
- Existing connections complete normally
- Hub no longer creates SoftAPs for new devices

### Common use cases

- Security concerns or suspicious activity detected
- Hub being relocated or decommissioned
- Temporary maintenance or troubleshooting
- Customer preference changes

**Note:** Disabling provisioner does not affect hub's other functionality or existing provisionee devices.
