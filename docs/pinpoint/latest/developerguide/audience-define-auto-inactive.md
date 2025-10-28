**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Manage the maximum number of

endpoints in Amazon Pinpoint

Each member of your audience can have a maximum of 15 endpoints associated with their
**UserId**, see [Endpoint quotas](quotas.md#quotas-endpoint "quotas.md#quotas-endpoint"). If you try to add a 16th endpoint then, depending on the **ChannelType**, you will either get **BadRequestException** or it will succeed by removing the endpoint with the oldest **EffectiveDate**.

###### Add a 16th endpoint

- If the new channel type for the endpoint is SMS, PUSH, VOICE, EMAIL, CUSTOM or IN_APP then
  **BadRequestException** is returned because the audience member is
  at their maximum number of endpoints. You need to remove an endpoint associated with the
  audience member and try again, see [Delete endpoints from Amazon Pinpoint programmatically](audience-define-remove.md "audience-define-remove.md").
- If the new channel type for the endpoint is ADM, GCM, APNS, APNS_VOIP, APNS_VOIP_SANDBOX or
  BAIDU:

      + Check that at least one endpoint currently associated with the audience member has a
       **ChannelType** of ADM, GCM, APNS, APNS\_VOICE, APNS\_VOIP\_SANDBOX or BAIDU.
       If there isn't then **BadRequestException** is returned and an
       endpoint needs to be removed before you try again, see [Delete endpoints from Amazon Pinpoint programmatically](audience-define-remove.md "audience-define-remove.md").
      + Otherwise, the endpoint with the oldest **EffectiveDate** is set to
       `INACTIVE` where the **ChannelType** is ADM, GCM, APNS,
       APNS\_VOIP, APNS\_VOIP\_SANDBOX or BAIDU.




      	- The **UserId** from the old endpoint is removed.
      	- The new endpoint is associated to the audience member and they still have the maximum
      	 number of endpoints.

  The endpoint can be re–enabled by setting the **Status** to
  `ACTIVE` and add the **UserId** back to the endpoint.
