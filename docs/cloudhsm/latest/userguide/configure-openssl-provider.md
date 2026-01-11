# Bootstrap OpenSSL Provider

Use the configure-openssl-provider tool to bootstrap your OpenSSL Provider installation and connect it to your AWS CloudHSM cluster.

###### To bootstrap the OpenSSL Provider

1. Run the configure-openssl-provider command with the IP address of an HSM in your cluster:

```
`$` `sudo /opt/cloudhsm/bin/configure-openssl-provider -a `<HSM IP address>``
```

Replace `<HSM IP address>` with the IP address of any HSM in your cluster. 2. Verify the configuration by checking that the OpenSSL Provider can connect to your cluster:

```
`$` `openssl list -providers -provider-path /opt/cloudhsm/lib -provider cloudhsm`
```

For more information about the configuration parameters, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md "configure-tool-params5.md").
