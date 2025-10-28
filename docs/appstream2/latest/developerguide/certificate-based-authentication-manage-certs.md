# End User

Certificates

End user certificates issued by AWS Private CA for AppStream 2.0 certificate-based
authentication don't require renewal or revocation. These certificates are
short-lived. AppStream 2.0 automatically issues a new certificate for each new session,
or every 24 hours for sessions with a long duration. The AppStream 2.0 session governs
the use of these end user certificates. If you end a session, AppStream 2.0 stops using
that certificate. These end user certificates have a shorter validity period
than a typical AWS Private CA CRL distribution. As a result, end user
certificates don't need to be revoked and won't appear in a CRL.
