# Set certificate validation policy

Amazon DCV uses a secure TLS connection for communication between the server and client. The
certificate validation policy determines how the Amazon DCV client responds when a certificate
can't be verified as trustworthy. Set one of the following options in the connection file:

- `Strict`: Prohibits the connection if there is any problem validating the TLS certificate.
- `Ask user`: Prompts the user to determine whether to trust the certificate when a certificate can't be verified.
- `Accept untrusted`: Connects to the server even if the TLS certificate is self signed and can't be validated by the client.
  For information about editing the connection file, see [Step 4: Create a connection file (optional)](using-connection-file.md "using-connection-file.md").
