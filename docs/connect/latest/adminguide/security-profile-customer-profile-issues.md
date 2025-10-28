# Assign new Customer Profiles

permissions in case of error

1. In order to update permissions in case of a 403 forbidden call error for
   any of the backend APIs, navigate to the domain section of the Amazon Connect Customer Profiles console and choose **View details**.

![The domain section of the Amazon Connect Customer Profiles console.](images/security-profile-customer-profile-issues-403-1.png) 2. Choose **Update Permissions** in the view domain details
section.

![Update permissions button appears here if any outstanding permissions need to be updated.](images/security-profile-customer-profile-issues-403-2.png) 3. After this is done, the permissions will be successfully updated and the
**Update Permissions** button will no longer be visible
in the domain details section. This will mitigate the 403 forbidden error
issue and you will be able to make API calls successfully.

![Update permissions button disappears after the action has completed successfully.](images/security-profile-customer-profile-issues-403-3.png)
