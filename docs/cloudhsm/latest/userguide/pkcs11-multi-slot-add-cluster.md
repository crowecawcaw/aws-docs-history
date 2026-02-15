# Add a cluster with multi-slot functionality for

AWS CloudHSM

When [connecting to multiple slots with
PKCS #11](pkcs11-library-configs-multi-slot.md "pkcs11-library-configs-multi-slot.md") for AWS CloudHSM, use the **configure-pkcs11 add-cluster** command
to add a cluster to your configuration.

## Syntax

```
`configure-pkcs11 add-cluster `[OPTIONS]`
 --cluster-id `<CLUSTER ID>`
 [--region `<REGION>`]
 [--endpoint `<ENDPOINT>`]
 [--hsm-ca-cert `<HSM CA CERTIFICATE FILE>`]
 [--client-cert-hsm-tls-file `<CLIENT CERTIFICATE FILE>`]
 [--client-key-hsm-tls-file `<CLIENT KEY FILE>`]
 [-h, --help]`
```

## Examples

###### Example

Use the **configure-pkcs11 add-cluster** along with the `cluster-id` parameter to add a cluster (with the ID of `cluster-1234567`) to your configuration.

Linux

```
`$` `sudo /opt/cloudhsm/bin/configure-pkcs11 add-cluster --cluster-id `<cluster-1234567>``
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" add-cluster --cluster-id `<cluster-1234567>``
```

###### Tip

If using **configure-pkcs11 add-cluster** with the `cluster-id` parameter doesn't result in the cluster being added, refer to the following example for a longer version
of this command that also requires `--region` and `--endpoint` parameters to identify the cluster being added. If, for example, the region of the cluster is different than the one configured as your AWS CLI default,
you should use the `--region` parameter to use the correct region. Additionally, you have the ability to specify the AWS CloudHSM API endpoint to use for the call, which may be necessary for
various network setups, such as using VPC interface endpoints that don’t use the default DNS hostname for AWS CloudHSM.

###### Example

Use the **configure-pkcs11 add-cluster** along with the `cluster-id`, `endpoint`, and `region` parameters to add a cluster (with the ID of `cluster-1234567`) to your configuration.

Linux

```

`$` `sudo /opt/cloudhsm/bin/configure-pkcs11 add-cluster --cluster-id `<cluster-1234567>` --region `<us-east-1>` --endpoint `<https://cloudhsmv2.us-east-1.amazonaws.com>``

```

Windows

```

`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" add-cluster --cluster-id `<cluster-1234567>`--region `<us-east-1>` --endpoint `<https://cloudhsmv2.us-east-1.amazonaws.com>``

```

For more information about the `--cluster-id`, `--region`,
and `--endpoint` parameters, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").

## Parameters

**--cluster-id `<Cluster ID>`**

Makes a `DescribeClusters` call to find all of the HSM elastic network interface (ENI) IP addresses in the cluster
associated with the cluster ID. The system adds the ENI IP addresses to the AWS CloudHSM configuration files.

###### Note

If you use the `--cluster-id` parameter from an EC2 instance within a VPC that does
not have access to the public internet, then you must create an interface VPC
endpoint to connect with AWS CloudHSM. For more information about VPC endpoints, see [AWS CloudHSM and VPC endpoints](cloudhsm-vpc-endpoint.md "cloudhsm-vpc-endpoint.md").

Required: Yes

**--endpoint `<Endpoint>`**

Specify the AWS CloudHSM API endpoint used for making the `DescribeClusters` call. You must set this option in combination with `--cluster-id`.

Required: No

**--hsm-ca-cert `<HsmCA Certificate Filepath>`**

Specifies the filepath to the HSM CA certificate.

Required: No

**--region `<Region>`**

Specify the region of your cluster. You must set this option in combination with `--cluster-id`.

If you don’t supply the `--region` parameter, the system chooses the region by attempting to read the `AWS_DEFAULT_REGION`
or `AWS_REGION` environment variables. If those variables aren’t set, then the system checks the region associated with your profile in your
AWS config file (typically `~/.aws/config`) unless you specified a different file in the `AWS_CONFIG_FILE` environment variable.
If none of the above are set, the system defaults to the `us-east-1` region.

Required: No

**--client-cert-hsm-tls-file
`<client certificate hsm tls path>`**

Path to the client certificate used for TLS client-HSM mutual authentication.

Only use this option if you have registered at least one trust anchor onto HSM with CloudHSM CLI. You must set this option in combination with
`--client-key-hsm-tls-file`.

Required: No

**--client-key-hsm-tls-file `<client key hsm tls path>`**

Path to the client key used for TLS client-HSM mutual authentication.

Only use this option if you have registered at least one trust anchor onto HSM with CloudHSM CLI. You must set this option in combination with
`--client-cert-hsm-tls-file`.

Required: No
