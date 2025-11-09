# End User

Certificates

End user certificates issued by AWS Private CA for WorkSpaces Applications certificate-based
authentication don't require renewal or revocation. These certificates are
short-lived. WorkSpaces Applications automatically issues a new certificate for each new session,
or every 24 hours for sessions with a long duration. The WorkSpaces Applications session governs
the use of these end user certificates. If you end a session, WorkSpaces Applications stops using
that certificate. These end user certificates have a shorter validity period
than a typical AWS Private CA CRL distribution. As a result, end user
certificates don't need to be revoked and won't appear in a CRL.
