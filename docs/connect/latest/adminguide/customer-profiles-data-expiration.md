

# Connect Customer Customer Profiles data expiration
<a name="customer-profiles-data-expiration"></a>

If a profile has not been updated within a specified amount of time, it will expire. This will cause the profile to be cleaned up, and removed from the Customer Profiles domain.

The time for Customer Profiles Data expiry can be broken down into two different categories:

## Profiles created through CreateProfile
<a name="profiles-created-via-createprofile"></a>

Profiles created by using the `CreateProfile` API will expire based on the timestamp assigned by **DefaultExpirationDays** on a Customer Profiles Domain. If no Expiration has been configured it will default to 365 days.

## Profiles created or updated through PutProfileObject
<a name="profiles-created-via-putprofileobject"></a>

Profiles created or updated by using `PutProfileObject` will always respect the **ExpirationDays** defined on the object type associated to them. If no Expiration is defined on the object type, the Customer Profiles domain expiration date will be used. Finally, if neither are provided, the profile or profile object will expire to the default 365 days.

## Mental model visualized
<a name="mental-model-visualized"></a>

![A flowchart showing the expiration logic for Customer Profiles.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-profiles-expiration-model.png)


## Import profile expiration
<a name="import-profile-expiration"></a>

If a profile has been imported into a Customer Profile domain by using Segment Import, its expiry will fall into two different scenarios.

1. **Explicit definition of expiry when calling CreateUploadJob**

   By default profiles imported by using Segment import will expire in 14 days if no updates have been performed. This number [can be defined](customer-segments-imported-files.md#set-profile-expiry) by using the API, or within the Connect Customer admin website during import creation, with a max of 90 days.

1. **Importing profiles that already exist within your Customer Profiles Domain from a previous import job**

   If two import jobs have been ran, and a duplicate profile has been found, Customer profiles will always respect the longest expiry time.