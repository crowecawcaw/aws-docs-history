# Certification Authority Authorization (CAA) problems

You can use CAA DNS records to specify that the Amazon certificate authority (CA) can
issue ACM certificates for your domain or subdomain. If you receive an error during
certificate issuance that says **One or more domain names have failed
validation due to a Certification Authority Authorization (CAA) error**, check
your CAA DNS records. If you receive this error after your ACM certificate request has
been successfully validated, you must update your CAA records and request a certificate
again. The **value** field in your CAA record must contain one
of the following domain names:

- amazon.com
- amazontrust.com
- awstrust.com
- amazonaws.com
  For more information about creating a CAA record, see [(Optional) Configure a CAA record](setup.md#setup-caa "setup.md#setup-caa").

###### Note

You can choose to not configure a CAA record for your domain if you do not want to
enable CAA checking.
