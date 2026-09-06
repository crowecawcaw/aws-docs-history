

# Voice ID domains in Connect Customer Voice ID
<a name="voiceid-domain"></a>

**Note**  
End of support notice: On May 20, 2026, AWS will end support for Amazon Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Amazon Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [Amazon Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html). 

When you enable Connect Customer Voice ID, you create a Voice ID domain: a container for all Voice ID data, such as speaker identifiers (which serves as the customer identifier), the voiceprints, the customer audio that was used for creating the enrollment voiceprints, and the enrollment statuses (enrolled, opted out) associated with the speaker identifiers. For detection of fraudsters in a watchlist, the Voice ID domain stores the fraudster identifiers, voiceprints, and audio used for creating the voiceprints.

Following are guidelines for creating Voice ID domains: 
+ Each Connect Customer instance can be associated with only one Voice ID domain. 
+ Each Voice ID domain can be associated with multiple Connect Customer instances. With a shared Voice ID domain, you can use the same stored customer data across multiple Connect Customer instances.
+ You can create multiple domains, but they don't share customer data between each other. 
+ We recommend creating a new Voice ID domain to associate with a Connect Customer instance when: 
  + You are enabling Voice ID for the first time on your account in an AWS Region.
  + You want to make sure that you isolate the Voice ID domains used for your test and production environments.
+ We recommend using an existing Voice ID domain when: 
  + You want to use the same set of enrolled callers and fraudsters across different Connect Customer instances (that might belong to different customer service teams) 
  + You want to use the same test environment across different test Connect Customer instances.
**Note**  
Only existing Voice ID domains in the same Region in your Connect Customer account can be shared across Connect Customer instances in that Region.
+ You can change the association of your Connect Customer instance from your current domain to a new domain at any time, by choosing a different domain. 
+ To delete a Voice ID domain, use the [DeleteDomain](https://docs.aws.amazon.com/voiceid/latest/APIReference/API_DeleteDomain.html) Voice ID API. `DeleteDomain` soft deletes the domain. Connect Customer waits 30 days before completely erasing the domain data. During this period, Voice ID; is disabled for all the Connect Customer instances it is associated with. To restore a domain during this window, submit an Support ticket and provide the domain ID. You can find the domain ID on the Voice ID section of the Connect Customer console, as shown in the following example:  
![The Voice ID section of the Connect Customer console displaying the domain ID field which is needed for domain restoration.](http://docs.aws.amazon.com/connect/latest/adminguide/images/voiceid-domain.png)

  Deleting a Voice ID domain deletes all stored customer data, such as audio recordings, voiceprints, and speaker identifiers, as well as any fraudster watchlists that you managed.

## Enrollment status
<a name="voiceid-speaker-enrollments"></a>

Voice ID stores three different enrollment status for a speaker: `ENROLLED`, ` OPTED_OUT` and `EXPIRED`. You can recall these speaker status using [Connect Customer Voice ID APIs](https://docs.aws.amazon.com/voiceid/latest/APIReference/) and using contact flow blocks to take appropriate action.
+ `ENROLLED`: When you enroll a new caller is enrolled into Voice ID, Voice ID creates a new voiceprint and set the speaker status as `ENROLLED`. Even if you re-enroll the same caller into Voice ID, the status stays as `ENROLLED`.
+ `OPTED_OUT`: If a caller does not provide consent to enroll into biometrics, you can opt out the caller (in the Contact Control Panel) or using APIs. Voice ID creates a new entry for this caller and set the speaker's status `OPTED_OUT`. Voice ID does not generate any voiceprint or store any audio recording for the speaker. Future enrollment requests for this speaker is rejected unless their entry is deleted.
+ `EXPIRED`: If a caller's voiceprint has not been accessed or refreshed for 3 years, Voice ID changes the status to `EXPIRED`, and you are no longer able to perform authentications for this caller. You can re-enroll the caller again or delete the caller from Voice ID.

## Expired speakers
<a name="voice-id-expired-speakers"></a>

For BIPA compliance, Voice ID automatically expires speakers that have not been accessed for enrollment, re-enrollment, or successful authentication for three years.

To view a speaker’s last access, look at the `lastAccessedAt` attribute that is returned by the `DescribeSpeaker` and `ListSpeakers` APIs. 

If you try to use the `EvaluateSesssion` API to authenticate an expired speaker, a `SPEAKER_EXPIRED` authentication decision is returned. 

To use the expired speaker again, they must be re-enrolled.

## Speaker and fraudster identifiers
<a name="voiceid-speaker-identifiers"></a>

Voice ID uses speaker identifiers to refer to and retrieve the voiceprints in a Voice ID domain. We recommend that you use identifiers that do not contain an Personally Identifiable Information (PII) in the identifiers. 

Voice ID creates two fields to refer to a caller: 
+ `CustomerSpeakerId`: A identifier provided by the customer. It can be between 1-256 characters and can only contain: **a-z**, **A-Z**, **0-9**, **-** and **\_**
+ `GeneratedSpeakerId`: A unique 22-character alphanumeric string that Voice ID creates and returns at the time of enrollment of the caller.

[Connect Customer Voice ID speaker APIs](https://docs.aws.amazon.com/voiceid/latest/APIReference/Welcome.html) accept either form of speaker identifiers, but only emit `GeneratedSpeakerId` in the Voice ID event streams and contact records. If you want to re-record the caller to redo the voiceprint, you can enroll the caller with the same `CustomerSpeakerId`. 

 Similarly, Voice ID creates unique fraudster identifiers called `GeneratedFraudsterID` for every fraudster that you add to a watchlist in the domain. Voice ID returns the fraudster identifier if a fraudster is detected in a call when performing fraud risk detection. 