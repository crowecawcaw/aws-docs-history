

# Data Retention for Signer
<a name="retention"></a>

**Signing Profiles **are automatically scheduled for deletion once they are [`canceled`](https://docs.aws.amazon.com/signer/latest/api/API_CancelSigningProfile.html) or [`revoked`](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSigningProfile.html).

 When a signing profile is canceled or revoked, we retain the profile for an additional period of time to ensure that any existing signatures created with that profile have expired before it is deleted. The retention period is equal to the signing profile's signature vailidity period plus 6 months. The default validity period is 135 months, so by default, canceled or revoked profiles are deleted after 141 months. Should you configure a shorter validity period, they will be deleted sooner.

**Note**  
For AWS IoT Device Management, canceled or revoked profiles have a retention period of 20 months.

**Signing Jobs** are automatically deleted 6 months after the generated signature expires.

**Note**  
For AWS IoT Device Management, signing job retention period is 20 months.