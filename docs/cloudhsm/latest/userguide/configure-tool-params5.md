# AWS CloudHSM Client SDK 5 configuration parameters

The following is a list of parameters to configure AWS CloudHSM Client SDK 5.



**-a `<ENI IP address>`**

Adds the specified IP address to Client SDK 5 configuration files. Enter any ENI IP
 address of an HSM from the cluster. For more information about how to use this option,
 see [Bootstrap Client SDK 5](cluster-connect.md#sdk8-connect "cluster-connect.md#sdk8-connect").


Required: Yes



**--hsm-ca-cert `<customerCA certificate file path>`**

 Path to the directory storing the certificate authority (CA) certificate use to
 connect EC2 client instances to the cluster. You create this file when you initialize
 the cluster. By default, the system looks for this file in the following location: 


Linux



```
/opt/cloudhsm/etc/`customerCA.crt`
```

Windows



```
C:\ProgramData\Amazon\CloudHSM\`customerCA.crt`
```

For more information about initializing the cluster or placing the certificate,
 see [Place the issuing certificate on each EC2 instance](cluster-connect.md#place-hsm-cert "cluster-connect.md#place-hsm-cert") and [Initialize the cluster in AWS CloudHSM](initialize-cluster.md "initialize-cluster.md").


Required: No



**--cluster-id `<cluster ID>`**


 Makes a `DescribeClusters` call to find all of the HSM elastic network interface (ENI) IP addresses in the cluster
 associated with the cluster ID. The system adds the ENI IP addresses to the AWS CloudHSM configuration files.


###### Note

If you use the `--cluster-id` parameter from an EC2 instance within a VPC that does
 not have access to the public internet, then you must create an interface VPC
 endpoint to connect with AWS CloudHSM. For more information about VPC endpoints, see [AWS CloudHSM and VPC endpoints](cloudhsm-vpc-endpoint.md "cloudhsm-vpc-endpoint.md").


Required: No



**--endpoint `<endpoint>`**

Specify the AWS CloudHSM API endpoint used for making the `DescribeClusters` call. You must set this option in combination with `--cluster-id`.
 


Required: No



**--region `<region>`**

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



**--log-level `<error | warn | info | debug |
 trace>`**

Specifies the minimum logging level the system should write to the log file. Each
 level includes the previous levels, with error as the minimum level and trace the
 maximum level. This means that if you specify errors, the system only writes errors to
 the log. If you specify trace, the system writes errors, warnings, informational
 (info) and debug messages to the log. For more information, see [Client SDK 5 Logging](hsm-client-logs.md#sdk5-logging "hsm-client-logs.md#sdk5-logging").


Required: No



**--log-rotation `<daily | weekly>`**

Specifies the frequency with which the system rotates logs. For more information,
 see [Client SDK 5 Logging](hsm-client-logs.md#sdk5-logging "hsm-client-logs.md#sdk5-logging").


Required: No



**--log-file `<file name with path>`**

Specifies where the system will write the log file. For more information, see
 [Client SDK 5 Logging](hsm-client-logs.md#sdk5-logging "hsm-client-logs.md#sdk5-logging").


Required: No



**--log-type `<term | file>`**

Specifies whether the system will write the log to a file or terminal. For more information, see
 [Client SDK 5 Logging](hsm-client-logs.md#sdk5-logging "hsm-client-logs.md#sdk5-logging").


Required: No



**-h | --help**

Displays help.


Required: No



**--disable-key-availability-check** 

Flag to disable key availability quorum. Use this flag to indicate AWS CloudHSM should
 disable key availability quorum and you can use keys that exist on only one HSM in the
 cluster. For more information about using this flag to set key availability quorum,
 see [Managing client key durability
 settings](working-client-sync.md#setting-file-sdk8 "working-client-sync.md#setting-file-sdk8").


Required: No



**--enable-key-availability-check** 

Flag to enable key availability quorum. Use this flag to indicate AWS CloudHSM should use
 key availability quorum and not allow you to use keys until those keys exist on two
 HSMs in the cluster. For more information about using this flag to set key
 availability quorum, see [Managing client key durability
 settings](working-client-sync.md#setting-file-sdk8 "working-client-sync.md#setting-file-sdk8").


Enabled by default.


Required: No



**--disable-validate-key-at-init** 

Improves performance by specifying that you can skip an initialization call to
 verify permissions on a key for subsequent calls. Use with caution.


Background: Some mechanisms in the PKCS #11 library support multi-part operations where an
 initialization call verifies if you can use the key for subsequent calls. This
 requires a verification call to the HSM, which adds latency to the overall operation.
 This option enables you to disable the subsequent call and potentially improve
 performance.


Required: No



**--enable-validate-key-at-init** 

Specifies that you should use an initialization call to verify permissions on a
 key for subsequent calls. This is the default option. Use
 `enable-validate-key-at-init` to resume these initialization calls after
 you use `disable-validate-key-at-init` to suspend them.


Required: No
