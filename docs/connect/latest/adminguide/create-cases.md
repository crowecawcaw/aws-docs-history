

# Create a case in Connect Customer Cases or a customer profile to document a customer's issue
<a name="create-cases"></a>

You can create a case either by choosing **\+ Case** from the **Cases** page or by choosing **\+ Connect case** directly from a customer profile. If you are not on active contact, you can still create a case directly from the customer profile.

**To create a case while on the **Customer Profile** page**

1. Choose **\+ Profile** to create a customer profile, as shown in the following image.   
![The Profile button on the Customer profile tab.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cm-cases-associated-profile1.png)

1. Choose **\+ Connect Case** to create a case, as shown in the following image.  
![The connect case button on the customer profile page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cm-cases-associated-profile2.png)

1. Complete the required information for the case, and then choose **Save**. A case is created for the customer, as shown in the following image.  
![A case.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cm-cases-associated-profile3.png)

**To create a case while on the **Cases** page**

1. You must be on a contact (call, chat, or task).

   If `customer_id` is included in the template's `requiredFields`, the contact must already be **Associated** with a customer profile. Otherwise, you can create a case without a customer profile.  
![A customer profile with the Associated status in the contact panel.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cm-create-case.png)

1. Choose the **Cases** tab and then choose **\+ Case**, as shown in the following image.  
![The Cases button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cm-create-case1.png)

1. Complete the required information for the case, and then choose **Save**. A case is created for the customer. 

## Customer name
<a name="cm-customername"></a>

Each case that is created is connected to a customer profile from your Connect Customer instance. While viewing the case details page, an agent can choose or tap the customer's name to open the associated Customer Profile in a different tab. Or, the agent can choose **More (...)** to copy the customer name or profile ID to the clipboard. On new case templates, the customer name appears by default on the case details page. You can rearrange this field on your case template, or even remove it entirely.

![The customer name, the more option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/cases-agent-application-customername.png)
