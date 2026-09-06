

# Configuring additional settings
<a name="configuring-additional-settings"></a>

After enabling basic mutual TLS authentication, you can configure additional settings to customize the authentication behavior for specific use cases and requirements.

## Certificate Authority advertisement
<a name="ca-advertisement"></a>

The AdvertiseTrustStoreCaNames field controls whether CloudFront sends the list of trusted CA names to clients during the TLS handshake, helping clients select the appropriate certificate.

### To configure CA advertisement (Console)
<a name="configure-ca-advertisement-console"></a>

1. In your distribution settings, navigate to the **General** tab, choose **Edit**.

1. Scroll to the **Viewer mutual authentication (mTLS)** section within the **Connectivity** container.

1. Select or de-select the **Advertise trust store CA names** checkbox.

1. Choose **Save changes**.

### To configure CA advertisement (AWS CLI)
<a name="configure-ca-advertisement-cli"></a>

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
<a name="certificate-expiration-handling"></a>

The IgnoreCertificateExpiry property determines how CloudFront responds to expired client certificates. By default, CloudFront rejects expired client certificates, but you can configure it to accept them when necessary. This is typically enabled for devices with expired certificates that cannot be readily updated.

### To configure certificate expiration handling (Console)
<a name="configure-expiration-console"></a>

1. In your distribution settings, navigate to **General** tab, choose **Edit**.

1. Scroll to the **Viewer mutual authentication (mTLS)** section of the **Connectivity** container.

1. Select or deselect the **Ignore certificate expiration date** checkbox.

1. Choose **Save changes**.

### To configure certificate expiration handling (AWS CLI)
<a name="configure-expiration-cli"></a>

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

**Note**  
**IgnoreCertificateExpiry** only applies to the certificates Validity dates. All other certificate validation checks still apply (chain of trust, signature validation).

## Next steps
<a name="additional-settings-next-steps"></a>

After configuring additional settings, you can set up header forwarding to pass certificate information to your origins, implement certificate revocation using Connection Functions and KeyValueStore, and enable connection logs for monitoring. For details on forwarding certificate information to origins, see [Forward Headers to origins](viewer-mtls-headers.md).