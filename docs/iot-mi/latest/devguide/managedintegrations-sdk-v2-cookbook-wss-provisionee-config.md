

# Configure provisionees for WiFi Simple Setup
<a name="managedintegrations-sdk-v2-cookbook-wss-provisionee-config"></a>

**On this page:**
+ [Provisionee requirements](#managedintegrations-sdk-v2-cookbook-wss-provisionee-requirements)
+ [Manufacturing requirements](#managedintegrations-sdk-v2-cookbook-wss-manufacturing-requirements)
+ [Enable provisionee capability](#managedintegrations-sdk-v2-cookbook-wss-enable-provisionee)
+ [Barcode scanning workflow](#managedintegrations-sdk-v2-cookbook-wss-barcode-scanning-workflow)
+ [Activation window and timeouts](#managedintegrations-sdk-v2-cookbook-wss-activation-window-timeouts)
+ [Retry WSS setup](#managedintegrations-sdk-v2-cookbook-wss-retry-setup)
+ [Disable provisionee capability](#managedintegrations-sdk-v2-cookbook-wss-disable-provisionee)

## Provisionee requirements
<a name="managedintegrations-sdk-v2-cookbook-wss-provisionee-requirements"></a>

Provisionee devices must meet these requirements to support WiFi Simple Setup.

### Hardware and security
<a name="managedintegrations-sdk-v2-cookbook-wss-provisionee-hardware"></a>
+ Managed integrations End device SDK integration completed with build flag `IOTMI_USE_WSS_PROVISIONEE` enabled
+ Hardware security module (HSM) or Trusted Platform Module (TPM) for secure storage
+ WiFi connectivity capability
+ Sufficient processing power for cryptographic operations (SHA-384, HKDF)

### Authentication materials
<a name="managedintegrations-sdk-v2-cookbook-wss-authentication-materials"></a>
+ Claim certificate and private key stored securely in HSM/TPM
+ Unique Serial Number (SN): 12-50 characters alphanumeric
+ Universal Product Code (UPC): 12 digits OR European Article Number (EAN): 13 digits
+ Barcode labels displaying SN and UPC/EAN (on device or packaging)

**Note**  
**EAN Support:** Provisioners currently support UPC only. EAN support is planned for future releases. Provisionees support both UPC and EAN.

**Important:** SN paired with UPC/EAN must be unique per managed thing within customer AWS account.

### Software components
<a name="managedintegrations-sdk-v2-cookbook-wss-software-components"></a>
+ corePKCS11 Platform Abstraction Layer (PAL) implementation connecting PKCS\#11 API to HSM/TPM
+ TLS 1.2/1.3 client with Pre-Shared Key (PSK) capability (port 4433, cipher suite: TLS\_AES\_256\_GCM\_SHA384 or equivalent)
+ SOCKS5 proxy client support (port 1080)
+ Cryptographic functions for SHA-384 and HKDF

**Note:** corePKCS11 PAL must interface with actual HSM/TPM hardware, not software-only implementation.

## Manufacturing requirements
<a name="managedintegrations-sdk-v2-cookbook-wss-manufacturing-requirements"></a>

Device manufacturers must provision secure materials and identifiers during manufacturing.

### Secure material provisioning
<a name="managedintegrations-sdk-v2-cookbook-wss-secure-material-provisioning"></a>

**Claim certificate and private key:**
+ Generate during manufacturing process
+ Store in HSM or TPM (required for production devices)
+ Never expose private key outside secure storage
+ Access via corePKCS11 PAL interface

**Device identifiers:**
+ Serial Number (SN): 12-50 character unique identifier
+ Universal Product Code (UPC): 12-digit product code OR European Article Number (EAN): 13-digit product code
+ Store securely alongside claim certificate in HSM/TPM

### Barcode requirements
<a name="managedintegrations-sdk-v2-cookbook-wss-barcode-requirements"></a>

**Physical labels must include:**
+ SN barcode on device or packaging (Code 128 format recommended)
+ UPC/EAN barcode on device or packaging (UPC-A or EAN-13 format)
+ Easily scannable labels (well-lit, focused, unobstructed)
+ Labels that survive shipping and handling

### Fleet Provisioning setup
<a name="managedintegrations-sdk-v2-cookbook-wss-fleet-provisioning-setup"></a>

**AWS account configuration:**

1. Create custom endpoint using GetCustomEndpoint API

1. Create provisioning profile using CreateProvisioningProfile API

1. Obtain claim certificate and private key for device family

1. Configure Fleet Provisioning template with required fields:
   + `deviceSerialNumber` (SN)
   + `universalProductCode` (UPC) or `europeanArticleNumber` (EAN)
   + Device certificate generation support
   + Thing registration in AWS IoT Core

## Enable provisionee capability
<a name="managedintegrations-sdk-v2-cookbook-wss-enable-provisionee"></a>

Enable WSS for devices using CreateManagedThing API during account linking.

### Device registration
<a name="managedintegrations-sdk-v2-cookbook-wss-device-registration"></a>

```
{
  "role": "DEVICE",
  "credentialLockerId": "ad5cdc9f786b4dbe9490e57c0b1d900e",
  "authenticationMaterialType": "WIFI_SETUP_QR_BAR_CODE",
  "authenticationMaterial": "SN:123456789331;UPC:123456789331",
  "wiFiSimpleSetupConfiguration": {
    "enableAsProvisionee": true,
    "timeoutInMinutes": 15
  }
}
```

**Parameters:**
+ `role`: Must be "DEVICE" for provisionee devices
+ `credentialLockerId`: Associates device with household (same as provisioner)
+ `authenticationMaterialType`: Use "WIFI\_SETUP\_QR\_BAR\_CODE" for WSS
+ `authenticationMaterial`: SN and UPC/EAN from device barcodes
+ `enableAsProvisionee`: Set to true to activate WSS
+ `timeoutInMinutes`: Activation window duration (5-15 minutes, default 15)

### Retry or reactivate
<a name="managedintegrations-sdk-v2-cookbook-wss-retry-reactivate"></a>

Use UpdateManagedThing to retry after initial failure:

```
{
  "managedThingId": "existing-device-id",
  "wiFiSimpleSetupConfiguration": {
    "enableAsProvisionee": true,
    "timeoutInMinutes": 15
  }
}
```

## Barcode scanning workflow
<a name="managedintegrations-sdk-v2-cookbook-wss-barcode-scanning-workflow"></a>

Complete end-to-end workflow from barcode scanning to device activation.

### Step 1: Preparation
<a name="managedintegrations-sdk-v2-cookbook-wss-preparation"></a>
+ Ensure mobile application installed and authenticated
+ Verify provisioner device (hub) is powered on and connected
+ Have device and packaging accessible for scanning

### Step 2: Scan and register
<a name="managedintegrations-sdk-v2-cookbook-wss-scan-register"></a>

1. Open mobile application and navigate to device setup

1. Scan device Serial Number (SN) barcode

1. Scan Universal Product Code (UPC) or European Article Number (EAN) barcode

1. Mobile app validates scanned data

1. Mobile app calls CreateManagedThing API with scanned data and WSS configuration

**Important**  
**Single provisionee onboarding limitation:** Only one provisionee can be onboarded at a time. If you scan multiple devices simultaneously, only the latest scanned device will be onboarded. To onboard devices that were previously scanned but not activated, you must run `UpdateManagedThing` to reactivate their setup window.

### Step 3: Cloud activation
<a name="managedintegrations-sdk-v2-cookbook-wss-cloud-activation"></a>

Cloud processing automatically:

1. Creates managed thing record with WSS configuration

1. Activates 15-minute setup window

1. Identifies eligible provisioners (same credential locker, `enableAsProvisioner=true`, `supportAsProvisioner=true`)

1. Sends provisioning notifications to all eligible provisioners

1. Provisioners create temporary SoftAPs and prepare for device connection

**GetManagedThing response example:**

```
{
  "managedThingId": "device-id", 
  "role": "DEVICE",
  "credentialLockerId": "ad5cdc9f786b4dbe9490e57c0b1d900e",
  "authenticationMaterialType": "WIFI_SETUP_QR_BAR_CODE",
  "authenticationMaterial": "SN:123456789331;UPC:123456789331",
  "wiFiSimpleSetupConfiguration": {
    "enableAsProvisioner": false,
    "supportAsProvisioner": false,
    "enableAsProvisionee": true,
    "wssExpirationTimeStamp": "2025-06-04T20:22:04.069610Z"
  }
}
```

**Key fields:**
+ `enableAsProvisionee`: Device configured for WSS provisioning
+ `wssExpirationTimeStamp`: Active setup window end time (null if expired)

### Step 4: Device power-on
<a name="managedintegrations-sdk-v2-cookbook-wss-device-power-on"></a>

1. Mobile app displays "Power on your device now" message

1. User powers on provisionee device

1. WSS workflow proceeds automatically:
   + Device discovers provisioner SoftAP
   + Authentication and credential exchange complete
   + Device connects to WiFi
   + Mobile app receives success notification

## Activation window and timeouts
<a name="managedintegrations-sdk-v2-cookbook-wss-activation-window-timeouts"></a>

WSS uses time-limited windows and operation timeouts to enhance security and manage provisioning.

### Activation window
<a name="managedintegrations-sdk-v2-cookbook-wss-activation-window"></a>

**Default:** 15 minutes from barcode scan to device activation

**Configuration:**
+ Set via `timeoutInMinutes` parameter (range: 5-15 minutes)
+ Default: 15 minutes balances convenience and security

**Expiration behavior:**
+ Provisioners remove device from allowlist after timeout
+ Device cannot connect via WSS after expiration
+ User must rescan barcodes or call UpdateManagedThing to reactivate

### Operation timeouts
<a name="managedintegrations-sdk-v2-cookbook-wss-operation-timeouts"></a>


**WSS operation timeouts**  

| Operation | Timeout | Behavior | 
| --- | --- | --- | 
| SoftAP discovery | 30 seconds | Retries up to 5 times, then falls back to User Guided Setup | 
| Fleet Provisioning | 30 seconds | Retries with exponential backoff if fails | 
| WiFi connection | 60 seconds | Reports error and suggests troubleshooting if fails | 

### Best practices
<a name="managedintegrations-sdk-v2-cookbook-wss-best-practices"></a>
+ Power on device within 5 minutes of barcode scan and place the device near provisioner's softap WiFi range
+ Ensure provisioner is powered on and connected before scanning
+ Use default 15-minute timeout unless specific requirements dictate otherwise

## Retry WSS setup
<a name="managedintegrations-sdk-v2-cookbook-wss-retry-setup"></a>

If initial WSS setup fails, retry using UpdateManagedThing API.

### Retry workflow
<a name="managedintegrations-sdk-v2-cookbook-wss-retry-workflow"></a>

**Step 1: Identify failure**
+ Mobile app receives WSS failure notification
+ Timeout expires without successful activation
+ User sees "Setup failed" or "Try again" message

**Step 2: Retry via UpdateManagedThing**

```
{
  "managedThingId": "device-managed-thing-id",
  "wiFiSimpleSetupConfiguration": {
    "enableAsProvisionee": true,
    "timeoutInMinutes": 15
  }
}
```

**Step 3: Reactivation**
+ Cloud reactivates 15-minute setup window
+ Provisioners recreate SoftAP and allowlist entry
+ User powers on device (if not already powered on)
+ WSS workflow proceeds

### Common retry scenarios
<a name="managedintegrations-sdk-v2-cookbook-wss-retry-scenarios"></a>


**WSS retry scenarios**  

| Scenario | Solution | 
| --- | --- | 
| Device not powered on in time | Call UpdateManagedThing and power on device promptly | 
| Provisioner unavailable | Ensure hub online, then retry | 
| Network connectivity issues | Verify network stable, then retry | 
| User error | Retry with correct device | 

**Important:** Each UpdateManagedThing call creates a new 15-minute window. After 3-4 failures, consider checking provisioner status, verifying device functionality, or using User Guided Setup.

## Disable provisionee capability
<a name="managedintegrations-sdk-v2-cookbook-wss-disable-provisionee"></a>

Disable or permanently remove WSS for a provisionee device.

### Using UpdateManagedThing API
<a name="managedintegrations-sdk-v2-cookbook-wss-using-update"></a>

```
{
  "managedThingId": "device-managed-thing-id",
  "wiFiSimpleSetupConfiguration": {
    "enableAsProvisionee": false
  }
}
```

### Using DeleteManagedThing API
<a name="managedintegrations-sdk-v2-cookbook-wss-using-delete"></a>

```
{
  "managedThingId": "device-managed-thing-id"
}
```

### Comparison
<a name="managedintegrations-sdk-v2-cookbook-wss-comparison"></a>


**Disable vs Delete comparison**  

| Action | UpdateManagedThing | DeleteManagedThing | 
| --- | --- | --- | 
| Device record | Retained in cloud | Permanently removed | 
| Device status | Changed to disabled | No longer exists | 
| Reactivation | Re-enable WSS anytime | Must re-register device | 
| Use case | Temporary disable, testing | Device retired, security incident | 

### Security considerations
<a name="managedintegrations-sdk-v2-cookbook-wss-security-considerations"></a>

Use disable/delete when:
+ Suspicious activity detected
+ Device reported stolen
+ Security incident investigation required
+ Device decommissioned or returned

After disabling/deleting, consider:
+ Changing WiFi password if credentials may have been compromised
+ Reviewing security notifications for unusual activity
+ Checking other devices in household for similar issues