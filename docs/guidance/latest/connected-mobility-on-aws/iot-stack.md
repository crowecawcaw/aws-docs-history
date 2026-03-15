# Vehicle connectivity

The vehicle connectivity layer configures AWS IoT Core for secure vehicle connectivity.

## IoT Core configuration

**Thing types:**

- cms-vehicle: Standard vehicle type
- cms-ev: Electric vehicle type
- cms-commercial: Commercial vehicle type

**IoT policies:**

Policies restrict device permissions to specific MQTT topics.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["iot:Connect"],
      "Resource": "arn:aws:iot:*:*:client/${iot:Connection.Thing.ThingName}"
    },
    {
      "Effect": "Allow",
      "Action": ["iot:Publish"],
      "Resource": "arn:aws:iot:*:*:topic/cms/telemetry/${iot:Connection.Thing.ThingName}"
    }
  ]
}
```

## Certificate management

**Provisioning workflow:**

1. Vehicle requests certificate using claim certificate
2. Pre-provisioning Lambda validates vehicle authorization
3. IoT Core creates thing and activates certificate
4. Post-provisioning Lambda updates DynamoDB
5. Vehicle receives unique certificate and private key

**Certificate rotation:**

- Certificates valid for 365 days
- Automatic rotation 30 days before expiration
- Old certificates deactivated after rotation
