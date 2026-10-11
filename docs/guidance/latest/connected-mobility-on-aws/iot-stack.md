

# Vehicle connectivity
<a name="iot-stack"></a>

The vehicle connectivity layer configures AWS IoT Core for secure vehicle connectivity.

## IoT Core configuration
<a name="iot-core-configuration"></a>

 **Thing types:** 
+ cms-vehicle: Standard vehicle type
+ cms-ev: Electric vehicle type
+ cms-commercial: Commercial vehicle type

 **IoT policies:** 

Each vehicle certificate carries `CMS-Vehicle-IoT-Policy-Scoped`, which limits the certificate to its own vehicle’s client IDs and topics. The policy uses two thing policy variables: `${iot:Connection.Thing.ThingName}`, which is the VIN, and `${iot:Connection.Thing.Attributes[vehicleId]}`, which is the vehicle ID.
+  **Connect** on `client/<VIN>` and `client/<VIN>-sim`, only when `iot:Connection.Thing.IsAttached` is `true`. The FleetWise Edge Agent connects as `<VIN>` and the simulator, which also hosts the vehicle-side SOVD handlers, connects as `<VIN>-sim` on the same certificate.
+  **Publish** on `cms/fleetwise/vehicles/<VIN>/ `, `cms/commands/things/<VIN>/executions/`, `cms/commands/<vehicleId>/response`, and the stage’s basic-ingest rule topics `$aws/rules/cms_<stage>_iot_msk_rule/<vehicleId>` and `$aws/rules/cms_<stage>_cs_product_meridian_ev_rule/<vehicleId>`.
+  **Subscribe** and **Receive** on `cms/fleetwise/vehicles/<VIN>/ `, `cms/commands/things/<VIN>/executions/`, and `cms/commands/<vehicleId>/request`.

Every resource puts the policy variable at a fixed position after a literal prefix, because ` ` in an IoT policy resource matches across `/` and a wildcard before the vehicle segment would admit another vehicle’s topics. Resources end in `` rather than the MQTT wildcards `#` or `+`, which IoT policies treat as literal characters. The rendered document is about 1,500 characters, under the 2,048-character policy limit. The policy is defined once, in `modules/cms_ui/source/handlers/main_api/iot_device_policy.py`, and every certificate-issuing path uses it.

 **Provisioning:** after minting a certificate, the provisioning path:

1. Checks that no other thing carries the vehicle’s `vehicleId`.

1. Creates the thing, or updates it, with the `vehicleId` attribute, then checks again for a duplicate and removes the attribute if it finds one.

1. Creates `CMS-Vehicle-IoT-Policy-Scoped` for the stage, or republishes it if the deployed version differs.

1. Attaches the certificate to the thing with exclusive association (`EXCLUSIVE_THING`).

1. Attaches the scoped policy to the certificate.

Exclusive association is what makes the binding work for both clients. With the default, non-exclusive association, AWS IoT resolves thing policy variables only when the client ID equals the thing name, so the simulator’s `<VIN>-sim` connection would not resolve. With exclusive association, the certificate alone identifies the thing. One certificate per vehicle therefore serves both the FleetWise Edge Agent and the simulator.

 `deployment/scripts/migrate_iot_vin_binding.py` moves existing things to this binding. It runs as a dry run by default, and has apply, verify, cutover and rollback modes, so each vehicle can be cut over and rolled back on its own.

## Certificate management
<a name="certificate-management"></a>

 **Provisioning workflow:** 

1. Vehicle requests certificate using claim certificate

1. Pre-provisioning Lambda validates vehicle authorization

1. IoT Core creates thing and activates certificate

1. Post-provisioning Lambda updates DynamoDB

1. Vehicle receives unique certificate and private key

 **Certificate rotation:** 
+ Certificates valid for 365 days
+ Automatic rotation 30 days before expiration
+ Old certificates deactivated after rotation