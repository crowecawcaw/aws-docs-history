# AWS CloudHSM Client SDK 5 configuration syntax

The following table illustrates the syntax for AWS CloudHSM configuration files for Client SDK 5. For more
information about the parameters, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").

PKCS #11

```
Usage: configure-pkcs11[ .exe ] [OPTIONS]

Options:
      --disable-certificate-storage
          Disables Certificate Storage
      --enable-certificate-storage
          Enables Certificate Storage
  -a <HSM ENI IP>...
          The address of the HSM instance
      --cluster-id <CLUSTER ID>
          The id of the cluster containing the HSM instance(s)
      --disable-key-availability-check
          Disables key availability check during key use
      --enable-key-availability-check
          Enables key availability check during key use
      --disable-validate-key-at-init
          Disables parameter validation during initialization of crypto operations
      --enable-validate-key-at-init
          Enables parameter validation during initialization of crypto operations
      --endpoint <ENDPOINT>
          Specify the AWS CloudHSM API Endpoint
      --region <REGION>
          The region of the cluster
      --hsm-ca-cert <HSM CA CERTIFICATE FILE>
          The HSM CA certificate file
      --log-type <LOG TYPE>
          The log type [possible values: term, file]
      --log-file <LOG FILE>
          The log file
      --log-level <LOG LEVEL>
          The logging level [possible values: error, warn, info, debug, trace]
      --log-rotation <LOG ROTATION>
          The log rotation interval [possible values: never, hourly, daily]
      --default-retry-mode <RETRY MODE>
          The default method of retry to use for certain non-terminal failures [possible values: off, standard]
      --client-cert-hsm-tls-file <CLIENT CERTIFICATE HSM TLS FILE>
          The client certificate used for TLS client-hsm mutual authentication
      --client-key-hsm-tls-file <CLIENT KEY HSM TLS FILE>
          The client private key used for TLS client-hsm mutual authentication
  -h, --help
          Print help
```

OpenSSL

```
Usage: configure-dyn[ .exe ] [OPTIONS]

Options:
  -a <HSM ENI IP>...
          The address of the HSM instance
      --cluster-id <CLUSTER ID>
          The id of the cluster containing the HSM instance(s)
      --disable-key-availability-check
          Disables key availability check during key use
      --enable-key-availability-check
          Enables key availability check during key use
      --disable-validate-key-at-init
          Disables parameter validation during initialization of crypto operations
      --enable-validate-key-at-init
          Enables parameter validation during initialization of crypto operations
      --endpoint <ENDPOINT>
          Specify the AWS CloudHSM API Endpoint
      --region <REGION>
          The region of the cluster
      --hsm-ca-cert <HSM CA CERTIFICATE FILE>
          The HSM CA certificate file
      --log-type <LOG TYPE>
          The log type [possible values: term, file]
      --log-file <LOG FILE>
          The log file
      --log-level <LOG LEVEL>
          The logging level [possible values: error, warn, info, debug, trace]
      --log-rotation <LOG ROTATION>
          The log rotation interval [possible values: never, hourly, daily]
      --default-retry-mode <RETRY MODE>
          The default method of retry to use for certain non-terminal failures [possible values: off, standard]
      --client-cert-hsm-tls-file <CLIENT CERTIFICATE HSM TLS FILE>
          The client certificate used for TLS client-hsm mutual authentication
      --client-key-hsm-tls-file <CLIENT KEY HSM TLS FILE>
          The client private key used for TLS client-hsm mutual authentication
  -h, --help
          Print help
```

KSP

```
Usage: configure-ksp.exe [OPTIONS]

Options:
  -a <HSM ENI IP>...
          The address of the HSM instance
      --server-client-cert-file <CLIENT CERTIFICATE FILE>
          The client certificate used for TLS client-server mutual authentication
      --server-client-key-file <CLIENT KEY FILE>
          The client private key used for TLS client-server mutual authentication
      --cluster-id <CLUSTER ID>
          The id of the cluster containing the HSM instance(s)
      --disable-key-availability-check
          Disables key availability check during key use
      --enable-key-availability-check
          Enables key availability check during key use
      --disable-validate-key-at-init
          Disables parameter validation during initialization of crypto operations
      --enable-validate-key-at-init
          Enables parameter validation during initialization of crypto operations
      --endpoint <ENDPOINT>
          Specify the AWS CloudHSM API Endpoint
      --region <REGION>
          The region of the cluster
      --hsm-ca-cert <HSM CA CERTIFICATE FILE>
          The HSM CA certificate file
      --log-type <LOG TYPE>
          The log type [possible values: term, file]
      --log-file <LOG FILE>
          The log file
      --log-level <LOG LEVEL>
          The logging level [possible values: error, warn, info, debug, trace]
      --log-rotation <LOG ROTATION>
          The log rotation interval [possible values: never, hourly, daily]
      --default-retry-mode <RETRY MODE>
          The default method of retry to use for certain non-terminal failures [possible values: off, standard]
      --client-cert-hsm-tls-file <CLIENT CERTIFICATE HSM TLS FILE>
          The client certificate used for TLS client-hsm mutual authentication
      --client-key-hsm-tls-file <CLIENT KEY HSM TLS FILE>
          The client private key used for TLS client-hsm mutual authentication
      --enable-sdk3-compatibility-mode
          Enables key file usage for KSP
      --disable-sdk3-compatibility-mode
          Disables key file usage for KSP
  -h, --help
          Print help
```

JCE

```
Usage: configure-jce[ .exe ] [OPTIONS]

Options:
  -a <HSM ENI IP>...
          The address of the HSM instance
      --cluster-id <CLUSTER ID>
          The id of the cluster containing the HSM instance(s)
      --disable-key-availability-check
          Disables key availability check during key use
      --enable-key-availability-check
          Enables key availability check during key use
      --disable-validate-key-at-init
          Disables parameter validation during initialization of crypto operations
      --enable-validate-key-at-init
          Enables parameter validation during initialization of crypto operations
      --endpoint <ENDPOINT>
          Specify the AWS CloudHSM API Endpoint
      --region <REGION>
          The region of the cluster
      --hsm-ca-cert <HSM CA CERTIFICATE FILE>
          The HSM CA certificate file
      --log-type <LOG TYPE>
          The log type [possible values: term, file]
      --log-file <LOG FILE>
          The log file
      --log-level <LOG LEVEL>
          The logging level [possible values: error, warn, info, debug, trace]
      --log-rotation <LOG ROTATION>
          The log rotation interval [possible values: never, hourly, daily]
      --default-retry-mode <RETRY MODE>
          The default method of retry to use for certain non-terminal failures [possible values: off, standard]
      --client-cert-hsm-tls-file <CLIENT CERTIFICATE HSM TLS FILE>
          The client certificate used for TLS client-hsm mutual authentication
      --client-key-hsm-tls-file <CLIENT KEY HSM TLS FILE>
          The client private key used for TLS client-hsm mutual authentication
  -h, --help
          Print help
```

CloudHSM CLI

```
Usage: configure-cli[ .exe ] [OPTIONS]

Options:
  -a <HSM ENI IP>...
          The address of the HSM instance
      --cluster-id <CLUSTER ID>
          The id of the cluster containing the HSM instance(s)
      --disable-key-availability-check
          Disables key availability check during key use
      --enable-key-availability-check
          Enables key availability check during key use
      --disable-validate-key-at-init
          Disables parameter validation during initialization of crypto operations
      --enable-validate-key-at-init
          Enables parameter validation during initialization of crypto operations
      --endpoint <ENDPOINT>
          Specify the AWS CloudHSM API Endpoint
      --region <REGION>
          The region of the cluster
      --hsm-ca-cert <HSM CA CERTIFICATE FILE>
          The HSM CA certificate file
      --log-type <LOG TYPE>
          The log type [possible values: term, file]
      --log-file <LOG FILE>
          The log file
      --log-level <LOG LEVEL>
          The logging level [possible values: error, warn, info, debug, trace]
      --log-rotation <LOG ROTATION>
          The log rotation interval [possible values: never, hourly, daily]
      --default-retry-mode <RETRY MODE>
          The default method of retry to use for certain non-terminal failures [possible values: off, standard]
      --client-cert-hsm-tls-file <CLIENT CERTIFICATE HSM TLS FILE>
          The client certificate used for TLS client-hsm mutual authentication
      --client-key-hsm-tls-file <CLIENT KEY HSM TLS FILE>
          The client private key used for TLS client-hsm mutual authentication
  -h, --help
          Print help
```

OpenSSL Provider

```
Usage: configure-openssl-provider[ .exe ] [OPTIONS]

Options:
  -a <HSM ENI IP>...
          The address of the HSM instance
      --cluster-id <CLUSTER ID>
          The id of the cluster containing the HSM instance(s)
      --disable-key-availability-check
          Disables key availability check during key use
      --enable-key-availability-check
          Enables key availability check during key use
      --disable-validate-key-at-init
          Disables parameter validation during initialization of crypto operations
      --enable-validate-key-at-init
          Enables parameter validation during initialization of crypto operations
      --endpoint <ENDPOINT>
          Specify the AWS CloudHSM API Endpoint
      --region <REGION>
          The region of the cluster
      --hsm-ca-cert <HSM CA CERTIFICATE FILE>
          The HSM CA certificate file
      --log-type <LOG TYPE>
          The log type [possible values: term, file]
      --log-file <LOG FILE>
          The log file
      --log-level <LOG LEVEL>
          The logging level [possible values: error, warn, info, debug, trace]
      --log-rotation <LOG ROTATION>
          The log rotation interval [possible values: never, hourly, daily]
      --default-retry-mode <RETRY MODE>
          The default method of retry to use for certain non-terminal failures [possible values: off, standard]
      --client-cert-hsm-tls-file <CLIENT CERTIFICATE HSM TLS FILE>
          The client certificate used for TLS client-hsm mutual authentication
      --client-key-hsm-tls-file <CLIENT KEY HSM TLS FILE>
          The client private key used for TLS client-hsm mutual authentication
  -h, --help
          Print help
```
