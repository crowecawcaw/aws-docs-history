# Multiple slot configuration with PKCS #11 library for

AWS CloudHSM

A single slot in Client SDK 5 PKCS #11 library represents a single connection to a cluster in AWS CloudHSM.
With Client SDK 5, you can configure your PKCS11 library to allow multiple slots to connect users to multiple CloudHSM clusters from a single PKCS#11 application.

Use the instructions in this topic to make your application use multi-slot functionality to connect with multiple clusters.

###### Topics

- [Multi-slot prerequisites for PKCS #11 library for
  AWS CloudHSM](#pkcs11-multi-slot-prereqs "#pkcs11-multi-slot-prereqs")
- [Configure the PKCS #11 library for multi-slot
  functionality for AWS CloudHSM](pkcs11-multi-slot-config-run.md "pkcs11-multi-slot-config-run.md")
- [Add a cluster with multi-slot functionality for
  AWS CloudHSM](pkcs11-multi-slot-add-cluster.md "pkcs11-multi-slot-add-cluster.md")
- [Remove a cluster with multi-slot
  functionality for AWS CloudHSM](pkcs11-multi-slot-remove-cluster.md "pkcs11-multi-slot-remove-cluster.md")

## Multi-slot prerequisites for PKCS #11 library for

AWS CloudHSM

Before configuring for multiple slots for PKCS #11 library for AWS CloudHSM, complete the following prerequisites.

- Two or more AWS CloudHSM clusters to which you’d like to connect to, along with their cluster certificates.
- An EC2 instance with Security Groups correctly configured to connect to all of the clusters above. For more information about how to set up a cluster and the client instance,
  refer to [Getting started with AWS CloudHSM](getting-started.md "getting-started.md").
- To set up multi-slot functionality, you must have already downloaded and installed the PKCS #11 library. If you have not already done this, refer to the instructions in [Install the PKCS #11 library for AWS CloudHSM Client SDK 5](pkcs11-library-install.md "pkcs11-library-install.md") .
