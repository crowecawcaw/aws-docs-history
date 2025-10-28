# Mount settings used by EFS mount helper

The Amazon EFS mount helper client uses the following mount options that are
optimized for Amazon EFS:

- `nfsvers=4.1` – used when mounting on EC2 Linux
  instances

`nfsvers=4.0` – used when mounting on supported EC2 Mac
instances running macOS Big Sur, Monterey, and Ventura

- `rsize=1048576` – Sets the maximum number of bytes of data that
  the NFS client can receive for each network READ request to 1048576, the largest
  available, to avoid diminished performance.
- `wsize=1048576` – Sets the maximum number of bytes of data that
  the NFS client can send for each network WRITE request to `1048576`, the largest available,
  to avoid diminished performance.
- `hard` – Sets the recovery behavior of the NFS client after an NFS
  request times out, so that NFS requests are retried indefinitely until the server replies,
  to ensure data integrity.
- `timeo=600` – Sets the timeout value that the NFS client uses to
  wait for a response before it retries an NFS request to 600 deciseconds (60 seconds) to
  avoid diminished performance.
- `retrans=2` – Sets to 2 the number of times the NFS client retries
  a request before it attempts further recovery action.
- `noresvport` – Tells the NFS client to use a new non-privileged
  Transmission Control Protocol (TCP) source port when a network connection is
  reestablished. Using the `noresvport` option helps to ensure that your
  EFS file system has uninterrupted availability after a reconnection or
  network recovery event.
- `mountport=2049` – only used when mounting on EC2 Mac instances
  running macOS Big Sur, Monterey, and Ventura.
