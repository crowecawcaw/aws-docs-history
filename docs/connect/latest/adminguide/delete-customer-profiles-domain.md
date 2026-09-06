

# Delete a Connect Customer Customer Profiles domain
<a name="delete-customer-profiles-domain"></a>

**Select your instance first**  
You must select your Connect Customer instance in the console before the Customer Profiles domain appears in the navigation pane.

Deleting mappings will only delete objects and data associated with that specific mapping. If there are multiple objects associated with a profile, then deleting a specific mapping might not clear the profile data. If you want to delete specific data, you would then delete the mapping, but your profiles might still exist if they contain data from other mappings. This could result in additional charges for the existing profiles. To avoid this from occurring, you can delete your Customer Profiles domain using the Connect Customer console by following these steps.

1. Login to the Connect Customer console and select Customer Profiles from the left navigation pane. Choose your Customer Profiles domain and then choose **View details**.  
![The Connect Customer Customer Profiles delete domain page, the view details domain button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/delete-customer-profiles-domain-step1.png)

1. Choose **Delete domain**.  
![The Connect Customer Customer Profiles delete domain page, the delete domain button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/delete-customer-profiles-domain-step2.png)

1. To delete your domain, enter *confirm* in the box and choose **Delete domain**.  
![The Connect Customer Customer Profiles delete domain page, the delete domain confirmation button after typing in confirm manually.](http://docs.aws.amazon.com/connect/latest/adminguide/images/delete-customer-profiles-domain-step3.png)