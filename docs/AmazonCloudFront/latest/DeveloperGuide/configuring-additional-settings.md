# Configuring additional settings

After enabling basic mutual TLS authentication, you can configure additional settings to customize the authentication behavior for specific use cases and requirements.

## Client certificate validation Optional mode

CloudFront offers an alternative Optional client certificate validation mode that validates client certificates that are presented but allows access to clients that don't present certificates.

### Optional mode behavior

- Grants connection to clients with valid certificates, (invalid certificates are denied).
- Allows connection to clients without certificates
- Allows mixed client authentication scenarios through a single distribution.

Optional mode is ideal for gradual migration to mTLS authentication, supporting clients with certificates and clients without certificates, or maintaining backward compatibility with legacy clients.

###### Note

In optional mode, Connection Functions are still invoked even when clients don't present certificates. This allows you to implement custom logic such as logging client IP addresses or applying different policies based on whether certificates are presented.

### To configure optional mode (Console)

1. In your distribution settings, navigate to the
   **General** tab, choose
   **Edit**.
2. Scroll to the **Viewer mutual authentication (mTLS)**
   section within the **Connectivity** container.
3. For **Client certificate validation mode**, select **Optional**.
4. Save changes.

### To configure optional mode (AWS CLI)

The following example shows how to configure optional mode:

```

"ViewerMtlsConfig": {
   "Mode": "optional",
   ...other settings
}

```

## Certificate Authority advertisement

The AdvertiseTrustStoreCaNames field controls whether CloudFront sends the list of trusted CA names to clients during the TLS handshake, helping clients select the appropriate certificate.

### To configure CA advertisement (Console)

1. In your distribution settings, navigate to the
   **General** tab, choose
   **Edit**.
2. Scroll to the **Viewer mutual authentication (mTLS)**
   section within the **Connectivity** container.
3. Select or de-select the **Advertise trust store CA names** checkbox.
4. Choose **Save changes**.

### To configure CA advertisement (AWS CLI)

The following example shows how to enable CA advertisement:

```
"ViewerMtlsConfig": {
   "Mode": "required", // or "optional"
   "TrustStoreConfig": {
      "AdvertiseTrustStoreCaNames": true,
      ...other settings
   }
}
```

## Certificate expiration handling

The IgnoreCertificateExpiry property determines how CloudFront responds to expired client certificates. By default, CloudFront rejects expired client certificates, but you can configure it to accept them when necessary. This is typically enabled for devices with expired certificates that cannot be readily updated.

### To configure certificate expiration handling (Console)

1. In your distribution settings, navigate to
   **General** tab, choose
   **Edit**.
2. Scroll to the **Viewer mutual authentication (mTLS)**
   section of the **Connectivity** container.
3. Select or deselect the **Ignore certificate expiration date** checkbox.
4. Choose **Save changes**.

### To configure certificate expiration handling (AWS CLI)

The following example shows how to ignore certificate expiration:

```
"ViewerMtlsConfig": {
  "Mode": "required", // or "optional"
  "TrustStoreConfig": {
     "IgnoreCertificateExpiry": false,
     ...other settings
  }
}
```

###### Note

**IgnoreCertificateExpiry** only applies to the certificates
Validity dates. All other certificate validation checks still apply (chain of
trust, signature validation).

## Next steps

After configuring additional settings, you can set up header forwarding to pass
certificate information to your origins, implement certificate revocation using
Connection Functions and KeyValueStore, and enable connection logs for monitoring.
For details on forwarding certificate information to origins, see [Forward Headers to origins](viewer-mtls-headers.md "viewer-mtls-headers.md").
