# Enabling signed or encrypted email

You can use S/MIME to enable users to send signed or encrypted email both inside and
outside of the organization.

###### Note

User certificates in the Global Address List (GAL) are supported only in a
connected Active Directory setup.

###### To enable users to send signed or encrypted emails

1. Set
   up an Active Directory (AD) Connector. Setting up an AD
   Connector with your on-premises directory allows users to continue to use their
   existing corporate credentials.
2. Configure Certificate
   Autoenrollment
   to issue and store user certificates automatically in the Active Directory. Amazon WorkMail
   receives user certificates from the Active Directory and publishes them to the
   GAL. For more information, see [Configure Certificate Autoenrollment](<https://technet.microsoft.com/en-us/library/cc731522(v=ws.11).aspx> "https://technet.microsoft.com/en-us/library/cc731522(v=ws.11).aspx").
3. Distribute
   the generated certificates to users by exporting the certificates from the
   server running Microsoft Exchange and mailing them.
4. Each user installs the certificate to their email program (such as Windows
   Outlook) and mobile devices.
