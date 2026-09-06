

# 6 Configuration Dictionary
<a name="elpg-configuration-dictionary"></a>

The configuration dictionary is a key-value store containing all the options necessary for the proper functioning of ExpressLink modules.

**Note**  
All keys are case sensitive.

Configuration key-value pairs listed in Table 2 are meant to be long lived (persist) throughout the life of the application and so are stored in non-volatile memory. Note that these key-value pairs have factory preset values, and can be read only or write only.


**Table 2 - Configuration Dictionary Persistent Keys**  

| Configuration Parameter | Type | Initial Value | Factory Reset | Buff Size | Description | 
| --- | --- | --- | --- | --- | --- | 
| About | R | Vendor - Model | N | 64 | A concatenation of Vendor name and Model name (also see 11.1.5.3). | 
| Version | R | X.Y.Z<br />[suffix] | N | 32 | The specific module firmware version (also see 11.1.5.3). Note: an optional alphanumeric suffix may be present. | 
| TechSpec | R | TechSpec version | N | 16 | The Technical Specification version this model implements (for example 'v0.6', 'v1.1.2'). | 
| ThingName | R | UID | N | 64 | The UID provided by the HW root of trust and present in the device certificate (also see 11.1.3.1) [12.1.3 ExpressLink Birth Certificate](elpg-provisioning.md#elpg-provisioning-birth-certificate)). | 
| Certificate | R | Device Birth Certificate | N | ≥4KB | Device certificate used to authenticate with AWS cloud, signed by the manufacturer CA (also see [12.1.3 ExpressLink Birth Certificate](elpg-provisioning.md#elpg-provisioning-birth-certificate)). | 
| CustomName | R/W | {empty} | Y | ≥128 | Custom Product Name, can be set by the host. | 
| Endpoint | R/W | Staging account endpoint | Y | ≥128 | The endpoint of the AWS account to which the ExpressLink module connects (also see [21.3.2 ExpressLink onboarding states and transitions](elpg-provisioning.md#elpg-provisioning-onboarding-states)). | 
| RootCA | R/W | AWS root CA | N | ≥4KB | The server root certificate that will be used to authenticate the cloud Endpoint (also see [9.12 Server Root Certificate Update](elpg-ota-updates.md#elpg-server-root-cert)). | 
| ShadowToken | R/W | ExpressLink | Y | 64 | The default client-token that will be used to mark Device Shadow updates. | 
| DefenderPeriod | R/W | 0 | Y | ≥8 | The Device Defender upload period in seconds. (0 indicates the service is disabled.) | 
| HOTAcertificate | R/W | {empty} | Y | ≥4KB | Host OTA certificate (see [9.10 Host OTA Signature Verification](elpg-ota-updates.md#elpg-hota-sig-verification)). | 
| OTAcertificate | W | Vendor OTA Certificate | N | ≥4KB | Module OTA certificate. Vendor and Model specific (see [9.5 Module OTA signature verification](elpg-ota-updates.md#elpg-ota-signature-verification)). (Wi-Fi modules only.) | 
| SSID | R/W | {Empty} | Y | 32 | SSID of local router (Wi-Fi modules only). | 
| Passphrase | W | {Empty} | Y | 64 | Passphrase of local router (Wi-Fi modules only). | 
| APN | R/W | {default} | Y | 128 | Access Point Name (Cellular modules only). | 
| KeepAlive | R/W | {default} | N | >=8 | The MQTT keep alive period in seconds. | 
| LWTConfig | R/W | {default} | N | >=128 | A JSON object describing the configuration of the Last Will and Testament Topic and options in case of unexpected connection loss. Expected keys are: “topic”, “qos”, and “retain”. Example: {“topic”: “abcde”, “qos”:0, “retain”:0} | 
| LWTMessage | R/W | {default} | N | >=128 | Message to publish as Last Will and Testament in case of unexpected connection loss. This can can be any valid MQTT message. | 

The additional configuration parameters in Table 3 are non-persistent. They are re-initialized at power up, and following any reset event. The host processor might have to re-configure them following a reset and (possibly) a *deep sleep* awakening (depending on the implementation).


**Table 3 - Configuration dictionary non-persistent keys**  
<a name="elpg-table3"></a>
<table>
<thead>
  <tr><th>Configuration Parameter</th><th>Type</th><th>Initial Value</th><th>Buff Size</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>QoS</td><td>R/W</td><td>0</td><td>1</td><td>QoS level selected for SEND commands</td></tr>
  <tr><td>Topic1</td><td>R/W</td><td>{Empty}</td><td>≥128</td><td>Custom defined topic 1</td></tr>
  <tr><td>Topic2</td><td>R/W</td><td>{Empty}</td><td></td><td>Custom defined topic 2</td></tr>
  <tr><td>...</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Topic&lt;Max Topic&gt;</td><td>R/W</td><td>{Empty}</td><td></td><td>Custom defined topic MaxTopic</td></tr>
  <tr><td>EnableShadow</td><td>R/W</td><td>0</td><td>1</td><td>0 - disabled, or 1 - enabled</td></tr>
  <tr><td colspan="5">Shadow configuration parameters (required only by modules that support the Shadow feature, see <a href="elpg-iot-services.md#elpg-device-shadow">10.2 AWS IoT Device Shadow</a>) </td></tr>
  <tr><td>Shadow1</td><td>R/W</td><td>{Empty}</td><td>64</td><td>Custom defined named shadow</td></tr>
  <tr><td>...</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>Shadow&lt;MaxShadow&gt;</td><td>R/W</td><td>{Empty}</td><td></td><td>Custom defined named shadow</td></tr>
  <tr><td colspan="5">BLE configuration parameters (required only by modules that support BLE host control, see <a href="elpg-ble.md">13 Bluetooth Low Energy (BLE)</a>) </td></tr>
  <tr><td>BLECentral1</td><td>R/W</td><td>{Empty}</td><td>≥ 128</td><td>GAP Central discovery/connect configurations. </td></tr>
  <tr><td>BLECentral2</td><td>R/W</td><td>{Empty}</td><td>≥ 128</td><td></td></tr>
  <tr><td>...</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>BLECentral&lt;MaxBLECentral&gt;</td><td>R/W</td><td>{Empty}</td><td>≥ 128</td><td></td></tr>
  <tr><td>BLEGATT1</td><td>R/W</td><td>{Empty}</td><td>≥ 128</td><td>GATT Characteristic definitions (JSON). </td></tr>
  <tr><td>BLEGATT2</td><td>R/W</td><td>{Empty}</td><td>≥ 128</td><td></td></tr>
  <tr><td>...</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>BLEGATT&lt;MaxBLEGatt&gt;</td><td>R/W</td><td>{Empty}</td><td>≥ 128</td><td></td></tr>
  <tr><td>BLEPeripheral</td><td>R/W</td><td>{Empty}</td><td>≥ 128</td><td>GAP Peripheral advertising configuration.</td></tr>
  <tr><td>BLEAllowList</td><td>R</td><td>{Empty}</td><td>≥ 128</td><td>BLE Allow list</td></tr>
  <tr><td>BLEBondLIstl</td><td>R</td><td>{Empty}</td><td>≥ 128</td><td>BLE Bonding list</td></tr>
</tbody>
</table>


## 6.1 Data values referenced
<a name="elpg-data-values"></a>

**6.1.1.1**   Maximum key length is 16 characters   
A parameter name (key) can be from 1 to 16 characters.

**6.1.1.2**   `ERR9 INVALID KEY LENGTH`   
If a parameter name (key) exceeds 16 characters, the ExpressLink module returns 'ERR9 INVALID KEY LENGTH'.

**6.1.1.3**   Valid key characters are 0-9, A-Z, a-z   
A parameter name (key) may only contain alphanumeric characters.

**6.1.1.4**   `ERR10 INVALID KEY NAME`   
If a non-alphanumeric character is used in a key name, then the ExpressLink module returns 'ERR10 INVALID KEY NAME'.

**6.1.1.5**   `ERR11 UNKNOWN KEY`   
If the parameter name (key) is not found in [Table 2 - Configuration Dictionary Persistent Keys](#elpg-table2) or [Table 3 - Configuration dictionary non-persistent keys](#elpg-table3), then the module returns 'ERR11 UNKNOWN KEY'.

**6.1.1.6**   `ERR4 PARAMETER ERROR`   
If the parameter (value) length exceeds the buffer size as defined in [Table 2 - Configuration Dictionary Persistent Keys](#elpg-table2) or [Table 3 - Configuration dictionary non-persistent keys](#elpg-table3).

## 6.2 Dictionary data access - CONF command
<a name="elpg-data-accessed-conf"></a>

### 6.2.1 CONF KEY=*{value}*   »Assignment«
<a name="elpg-assignment-conf"></a>

Assign a value to a configuration parameter present in the configuration dictionary. (See [9.11.2 CONF? *{certificate} pem*   »Special certificate output formatting option«](elpg-ota-updates.md#elpg-ota-confq-command)).Returns:

**6.2.1.1**   `OK{EOL}`   
If the write is successful, then the module returns 'OK'.  
Example:  

```
AT+CONF Topic1={EOL}  # Assign the empty string to Topic 1
OK
```

**6.2.1.2**   `ERR9 INVALID KEY LENGTH`   
If the key is too long, then the module returns 'INVALID KEY LENGTH'.

**6.2.1.3**   `ERR10 INVALID KEY NAME`  
If the key uses incorrect characters, then the module returns 'INVALID KEY NAME'.

**6.2.1.4**   `ERR11 UNKNOWN KEY`  
If the key is not present in the dictionary, then the module returns 'UNKNOWN KEY'.  
Example:  

```
AT+CONF VERSION=1.0   # Incorrect capitalization
ERR11 UNKNOWN KEY     # The key is not recognized as spelled
```

**6.2.1.5**   `ERR12 KEY READONLY`  
Some keys are read-only and cannot be written. If the key cannot be written to, then the module returns 'KEY READONLY' (for example, ThingName, Certificate, About).  
Example  

```
AT+CONF Version=1.0   # Attempt to manually modify the Version parameter
ERR12 KEY READONLY
```

**6.2.1.6**   `ERR23 INVALID SIGNATURE`  
When updating a certificate (for example, Certificate, OTAcertificate, HOTAcertificate) if a required signature verification failed, then the module returns 'INVALID SIGNATURE'. (See [9.11 Host OTA certificate update](elpg-ota-updates.md#elpg-hota-cert-update) for more detail on the signature verification rules that apply to different types of certificates.) 

### 6.2.2 CONF? *key*   »Read the value of a configuration parameter«
<a name="elpg-retrieval-conf"></a>Returns:

**6.2.2.1**   `OK {value}`   
If the read is successful, then the module returns 'OK'.

**6.2.2.2**   `ERR9 INVALID KEY LENGTH`   
If the key is too long, then the module returns 'INVALID KEY LENGTH'.

**6.2.2.3**   `ERR10 INVALID KEY NAME`  
If the key uses incorrect characters, then the module returns 'INVALID KEY NAME'.

**6.2.2.4**   `ERR11 UNKNOWN KEY`  
If the key is not present in the system, then the module returns 'UNKNOWN KEY'.

**6.2.2.5**   `ERR13 KEY WRITEONLY`  
Some keys are write-only and cannot be read. If the key cannot be read, then the module returns 'KEY WRITEONLY'.

Example:

```
AT+CONF? Passphrase
ERR13 KEY WRITEONLY
```