This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Migration to disable certificate pinning

###### Important

Do not disable certificate pinning if you are using a self-signed certificate.

You may want to disable certificate pinning to avoid losing the ability to respond to
certificate issues. For example, if the certificates are rotated on a regular basis, the
application needs to also be updated regularly. During certificate rotation, the current
certificate expires and a new certificate must be regenerated, if you have certificate pinning
enabled.

When a new certificate is generated and pushed down to all clients/devices using the Push
config option, only the active clients/devices can get the updated certificate. If you have
devices that are not active (switched off or app killed), they won’t get the updated new
certificates. Later, when they become available, the devices won’t receive the push config, which
leads to a bad state for your Wickr app (expired certificates). The only way to reactivate the
Wickr app is by resetting the app, which can be avoided if you disable certificate
pinning.

**To disable certificate pinning:**

1. In the navigation pane, choose **Network Settings**, and then choose
   **Security Group**.
2. Choose **Details**.
3. On the security group page, select the **Push Config** tab, then choose
   **Edit** in the **Certificate Pinning** section.
4. Deselect **Use Certificate Pinning**, and then choose
   **Save**.
