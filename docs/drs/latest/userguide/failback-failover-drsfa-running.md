

# Running the DRSFA client
<a name="failback-failover-drsfa-running"></a>

Navigate to the `drs_failback_automation_client` directory, set the required environment variables, and run the client.

The following table describes the environment variables:


| Variable | Required | Description | 
| --- | --- | --- | 
| AWS\_REGION | Yes | The AWS Region where your Recovery instances are located. | 
| AWS\_ACCESS\_KEY | Yes | The AWS access key for the DRSFA client. | 
| AWS\_SECRET\_ACCESS\_KEY | Yes | The AWS secret access key for the DRSFA client. | 
| AWS\_SESSION\_TOKEN | Conditional | Required when using temporary credentials. | 
| DRS\_FAILBACK\_CLIENT\_PASSWORD | Yes | The password you set in the drs\_failback\_automation\_seed.iso file. | 
| VCENTER\_HOST | Yes | The IP address of the vCenter host. | 
| VCENTER\_PORT | Yes | The vCenter port (usually 443). | 
| VCENTER\_USER | Yes | The vCenter username (for example, admin@vsphere.local). | 
| VCENTER\_PASSWORD | Yes | The vCenter password. | 
| VCENTER\_DATASTORE | Yes | The datastore where the Failback Client ISO and seed ISO are stored. | 
| VCENTER\_FAILBACK\_CLIENT\_PATH | Yes | Path to aws-failback-livecd-64bit.iso in the datastore. | 
| VCENTER\_SEED\_ISO\_PATH | Yes | Path to drs\_failback\_automation\_seed.iso in the datastore. | 
| DISABLE\_SSL\_VERIFICATION | No | Set to true to deactivate SSL verification. Active by default. | 
| THREAD\_POOL\_SIZE | No | Number of servers to process concurrently. Default is 10. | 

You can set the variables inline or export them individually.

**Option 1: Export variables individually**

```
export AWS_REGION=us-west-2
export AWS_ACCESS_KEY=XXXX
export AWS_SECRET_ACCESS_KEY=XXXX
export AWS_SESSION_TOKEN=XXXX
export DRS_FAILBACK_CLIENT_PASSWORD=XXXX
export VCENTER_HOST=10.0.1.100
export VCENTER_PORT=443
export VCENTER_USER=admin@vsphere.local
export VCENTER_PASSWORD=XXXX
export VCENTER_DATASTORE=Datastore1
export VCENTER_FAILBACK_CLIENT_PATH='path/aws-failback-livecd-64bit.iso'
export VCENTER_SEED_ISO_PATH='path/drs_failback_automation_seed.iso'

python3 drs_failback_automation_init.pyc
```

**Option 2: Inline variables**

```
AWS_REGION=us-west-2 AWS_ACCESS_KEY=XXXX AWS_SECRET_ACCESS_KEY=XXXX \
DRS_FAILBACK_CLIENT_PASSWORD=XXXX VCENTER_HOST=10.0.1.100 VCENTER_PORT=443 \
VCENTER_USER=admin@vsphere.local VCENTER_PASSWORD=XXXX \
VCENTER_DATASTORE=Datastore1 \
VCENTER_FAILBACK_CLIENT_PATH='path/aws-failback-livecd-64bit.iso' \
VCENTER_SEED_ISO_PATH='path/drs_failback_automation_seed.iso' \
python3 drs_failback_automation_init.pyc
```