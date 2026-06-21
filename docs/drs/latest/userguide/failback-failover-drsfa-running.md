# Running the DRSFA client

Navigate to the `drs_failback_automation_client` directory, set the
required environment variables, and run the client.

The following table describes the environment variables:

| Variable                       | Required    | Description                                                          |
| ------------------------------ | ----------- | -------------------------------------------------------------------- |
| `AWS_REGION`                   | Yes         | The AWS Region where your Recovery instances are located.            |
| `AWS_ACCESS_KEY`               | Yes         | The AWS access key for the DRSFA client.                             |
| `AWS_SECRET_ACCESS_KEY`        | Yes         | The AWS secret access key for the DRSFA client.                      |
| `AWS_SESSION_TOKEN`            | Conditional | Required when using temporary credentials.                           |
| `DRS_FAILBACK_CLIENT_PASSWORD` | Yes         | The password you set in the `drs_failback_automation_seed.iso` file. |
| `VCENTER_HOST`                 | Yes         | The IP address of the vCenter host.                                  |
| `VCENTER_PORT`                 | Yes         | The vCenter port (usually 443).                                      |
| `VCENTER_USER`                 | Yes         | The vCenter username (for example, `admin@vsphere.local`).           |
| `VCENTER_PASSWORD`             | Yes         | The vCenter password.                                                |
| `VCENTER_DATASTORE`            | Yes         | The datastore where the Failback Client ISO and seed ISO are stored. |
| `VCENTER_FAILBACK_CLIENT_PATH` | Yes         | Path to `aws-failback-livecd-64bit.iso` in the datastore.            |
| `VCENTER_SEED_ISO_PATH`        | Yes         | Path to `drs_failback_automation_seed.iso` in the datastore.         |
| `DISABLE_SSL_VERIFICATION`     | No          | Set to `true` to deactivate SSL verification. Active by default.     |
| `THREAD_POOL_SIZE`             | No          | Number of servers to process concurrently. Default is 10.            |

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
