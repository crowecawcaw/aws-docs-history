

# Configure the PKCS \#11 library for multi-slot functionality for AWS CloudHSM
<a name="pkcs11-multi-slot-config-run"></a>

To configure your PKCS \#11 library for multi-slot functionality for AWS CloudHSM, follow these steps:

1. Identify the clusters you want to connect to using multi-slot functionality.

1. Add these clusters to your PKCS \#11 configuration by following the instructions in [Add a cluster with multi-slot functionality for AWS CloudHSM](pkcs11-multi-slot-add-cluster.md)

1. The next time your PKCS\#11 application runs, it will have multi-slot functionality.