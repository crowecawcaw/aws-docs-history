

# Contact record templates in Connect Customer Customer Profiles
<a name="ctr-contact-record-template"></a>

A contact record is a profile object that captures essential metadata from contact events, such as phone calls or chats. Connect Customer Customer Profiles uses contact records to document and analyze your interactions with customers.

Contact records are ingested automatically by the Connect Customer integration when a contact event ends. The contact event's identifier is provided as the `_ctrContactId` key. Because ingestion happens after the contact ends, profile association isn't visible during the live interaction—it appears after the contact record has been processed.

**Note**  
**Assign a contact record to a specific profile**  
You don't have to rely on automatic matching to choose the profile. Call [AddProfileKey](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_AddProfileKey.html) on the profile you want, with `KeyName` set to `_ctrContactId` and the contact's ID as the value. When the contact record is ingested after the contact ends, its `_ctrContactId` key matches the profile you chose, and the record is associated there instead of falling back to `_phone` or creating an inferred profile. Add the key during the contact, while it's still in progress, so it's in place before ingestion. This works with all three templates, because each one evaluates `_ctrContactId` first.

When a contact event occurs, one of three default templates determines how the event is handled. Each template defines specific rules for matching and profile creation, so you can tailor processing to your business needs.

**Topics**
+ [Create inferred profiles and auto-associate profiles (CTR-NoInferred)](#ctr-contact-record-template-no-inferred)
+ [Auto-associate profiles only (CTR-AutoAssociateOnly)](#ctr-contact-record-template-auto-associate)
+ [Create inferred profiles only (CTR)](#ctr-contact-record-template-inferred-only)
+ [Update the contact record type (console)](#ctr-contact-record-template-usage-examples-console)
+ [Update the contact record type (AWS CLI)](#ctr-contact-record-template-usage-examples)
+ [Automatically add names from email contacts to a profile](#add-email-names-to-profile)

## Create inferred profiles and auto-associate profiles (CTR-NoInferred)
<a name="ctr-contact-record-template-no-inferred"></a>

With the CTR-NoInferred template, when a contact event such as a phone call occurs, Customer Profiles first uses the `_ctrContactId` key to search for an existing profile. If a match is found, the contact event is auto-associated with that profile. If not, Customer Profiles searches using the secondary `_phone` key to locate a profile by the caller's phone number, and auto-associates if a match is found.

If neither `_ctrContactId` nor `_phone` finds an existing profile, Customer Profiles creates a new inferred profile and populates it with the contact event metadata.

The CTR-NoInferred behavior is useful for reducing duplicate profiles.

![The Contact Record CTR-NoInferred template diagram.](https://docs.aws.amazon.com/connect/latest/adminguide/images/ctr-contact-record-template-no-inferred.png)


## Auto-associate profiles only (CTR-AutoAssociateOnly)
<a name="ctr-contact-record-template-auto-associate"></a>

CTR-AutoAssociateOnly works like CTR-NoInferred with one important distinction: it doesn't create an inferred profile when no existing profile can be found for auto-association.

It uses `_ctrContactId` first and falls back to `_phone`. If a match is found, the contact event is auto-associated. If no match is found, no inferred profile is created.

Use CTR-AutoAssociateOnly when you want automatic association with existing profiles while maintaining strict control over profile creation.

![The Contact Record CTR-AutoAssociateOnly template diagram.](https://docs.aws.amazon.com/connect/latest/adminguide/images/ctr-contact-record-template-auto-associate.png)


## Create inferred profiles only (CTR)
<a name="ctr-contact-record-template-inferred-only"></a>

The CTR template relies solely on the `_ctrContactId` key. If a match is found, the contact event is associated with that profile. If not, the template creates an inferred profile and populates it with the contact event metadata.

Because this template doesn't fall back to `_phone` for matching, it can create many inferred profiles, which might lead to duplicate profiles. We recommend CTR-NoInferred instead.

![The Contact Record CTR template diagram.](https://docs.aws.amazon.com/connect/latest/adminguide/images/ctr-contact-record-template-inferred-only.png)


## Update the contact record type (console)
<a name="ctr-contact-record-template-usage-examples-console"></a>

1. In the Connect Customer Customer Profiles console, choose **View details** in the **Customer Profiles domain** section.  
![View details in the Customer Profiles domain section.](https://docs.aws.amazon.com/connect/latest/adminguide/images/ctr-contact-record-template-usage-examples-console-1.png)

1. On the **Domain details** page, choose **Edit** in the **Profile creation and auto-association** section.  
![Edit in the Profile creation and auto-association section.](https://docs.aws.amazon.com/connect/latest/adminguide/images/ctr-contact-record-template-usage-examples-console-2.png)

1. Select the contact-record behavior you want and choose **Save**.  
![The desired Contact Record behavior you would like to apply to your Domain and choose Save.](https://docs.aws.amazon.com/connect/latest/adminguide/images/ctr-contact-record-template-usage-examples-console-3.png)

## Update the contact record type (AWS CLI)
<a name="ctr-contact-record-template-usage-examples"></a>
+ CTR-NoInferred:

  ```
  aws customer-profiles put-profile-object-type --domain-name {domain} --object-type-name CTR --description "Creates inferred profiles and auto-associates profiles" --template-id CTR-NoInferred
  ```
+ CTR-AutoAssociateOnly:

  ```
  aws customer-profiles put-profile-object-type --domain-name {domain} --object-type-name CTR --description "Auto-associate with profiles only" --template-id CTR-AutoAssociateOnly
  ```
+ CTR:

  ```
  aws customer-profiles put-profile-object-type --domain-name {domain} --object-type-name CTR --description "Creates inferred profiles only" --template-id CTR
  ```

For information on using the API, see [PutProfileObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutProfileObjectType.html).

## Automatically add names from email contacts to a profile
<a name="add-email-names-to-profile"></a>

You can set up a flow to populate a name from an email contact to the customer's profile. Use the [Customer profiles](customer-profiles-block.md) block, configured to use the [Update profile](customer-profiles-block.md#customer-profiles-block-properties-update-profile) action.