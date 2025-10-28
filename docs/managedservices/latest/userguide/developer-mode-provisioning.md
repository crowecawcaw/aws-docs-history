# Provisioning infrastructure in AMS Developer mode

Users that don't have the Developer mode IAM role, `AWSManagedServicesDevelopmentRole`, in
accounts where Developer mode is enabled, are required to follow the AMS Advanced change
management process that leverages AMS Advanced AMIs. Users with correct role (**MALZ**:
`AWSManagedServicesDevelopmentRole`, **SALZ**: `customer_developer_role`)
can use the AMS Advanced change management system and AMS Advanced AMIs but are not required to.

###### Note

An AWS AMI, that has not been processed through AMS Advanced workload ingestion, or created in
an AMS Advanced account, will not include AMS Advanced-required configurations.
