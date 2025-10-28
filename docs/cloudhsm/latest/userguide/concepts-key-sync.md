# AWS CloudHSM key concepts

The following are concepts to be aware of when working with keys in AWS CloudHSM.

**Token keys**

Persistent keys that you create during key generate, import or unwrap
operations. AWS CloudHSM synchronizes token keys across a cluster.

**Session keys**

Ephemeral keys that exist only on one hardware security module (HSM) in the
cluster. AWS CloudHSM does _not_ synchronize session
keys across a cluster.

**Client-side key synchronization**

A client-side process that clones token keys you create during key generate,
import or unwrap operations. You can make token keys more durable by running a
cluster with a minimum of two HSMs.

**Server-side key synchronization**

Periodically clones keys to every HSM in the cluster. Requires no
management.

**Client key durability settings**

Settings you configure on the client that impact key durability. These settings work
differently in Client SDK 5 and Client SDK 3.

- In Client SDK 5, use this setting to run a single HSM cluster.
- In Client SDK 3, use this setting to specify the number of HSMs required
  for key creation operations to succeed.
