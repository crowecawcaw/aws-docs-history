

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Approve or reject RFCs
<a name="ex-rfc-approvals"></a>

RFCs submitted with approval-required (manual) CTs must be approved by you or AMS. Pre-approved CTs are automatically processed. For more information, see [CT approval requirements](constrained-unconstrained-ctis.md).

**Note**  
When using manual CTs, AMS recommends that you use the ASAP **Scheduling** option (choose **ASAP** in the console, leave start and end time blank in the API/CLI) as these CTs require an AMS operator to examine the RFC, and possibly communicate with you before it can be approved and run. If you schedule these RFCs, be sure to allow at least 24 hours. If approval does not happen before the scheduled start time, the RFC is rejected automatically.

If an approval-required RFC is successfully submitted by AMS, then it must be explicitly approved by you. Or, iff you submit an approval-required RFC, then it must be approved by AMS. If you're required to approve an RFC that AMS submitted, then an email or other predetermined communication is sent to you requesting the approval. The communication includes the RFC ID. After the communication is sent, do one of the followings:
+ Console Approve or Reject: Use the RFC details page for the relevant RFC:  
![RFC details page.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/AMS_Console-App-Rej.png)
+ API / CLI Approve: [ApproveRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ApproveRfc.html) marks a change as approved. The action must be taken by both the owner and operator, if both are required. The following is an example CLI approve command. In the following example, replace RFC\_ID with the appropriate RFC ID.

  ```
  aws amscm approve-rfc --rfc-id {{RFC_ID}}
  ```
+ API / CLI Reject: [RejectRfc](https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RejectRfc.html) marks a change as rejected. The following is an example CLI reject command. In the following example, replace RFC\_ID with the appropriate RFC ID.

  ```
  aws amscm reject-rfc --rfc-id {{RFC_ID}} --reason "no longer relevant"
  ```