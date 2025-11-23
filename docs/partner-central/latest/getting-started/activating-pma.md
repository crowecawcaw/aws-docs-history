# Activating a program management account

To activate a PMA, a channel handshake must be accepted by the AWS management account.

**For AWS Partner Central UI users:**

- The channel handshake is automatically created when you create a PMA
- The root email address of the AWS management account receives an request email
- An authorized user must access the invited AWS management account using the unique link provided in the request email
- Within the AWS console of the invited management account, they can accept or reject the request
  **For CLI/SDK users:**

- You must explicitly send a program management account channel handshake request
- The root email address of the AWS management account receives an request email
- The account owner must either access the invited AWS management account and accept/reject through the AWS console using the provided unique link in the request email, or use CLI commands from the invited AWS management account to accept/reject the handshake

###### Important

The handshake request can only be accepted or rejected by signing in to or accessing the invited AWS management account. The partner who created the PMA in Partner Central must have access to this management account to complete the activation process.
