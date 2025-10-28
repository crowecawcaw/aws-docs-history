# Amazon Connect Voice ID speaker,

watchlist, and fraudster management APIs

###### Note

End of support notice: On May 20, 2026, AWS will end support for Amazon Connect
Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the
Amazon Connect console, access Voice ID features on the Amazon Connect admin website or Contact Control Panel, or access Voice ID
resources. For more information, visit [Amazon Connect
Voice ID end of support](amazonconnect-voiceid-end-of-support.md "amazonconnect-voiceid-end-of-support.md").

Amazon Connect Voice ID includes APIs to manage speakers enrolled into a Voice ID domain
and fraudsters registered in the domain. All speaker APIs, except
`ListSpeakers`, accept either the `CustomerSpeakerId` or
`GeneratedSpeakerId`.

## Speaker management APIs

1. [DescribeSpeaker](../../../voiceid/latest/APIReference/API_DescribeSpeaker.md "../../../voiceid/latest/APIReference/API_DescribeSpeaker.md"): Describe a speaker's [status in a domain (ENROLLED,
   OPTED_OUT, EXPIRED)](voiceid-domain.md#voiceid-speaker-enrollments "voiceid-domain.md#voiceid-speaker-enrollments"), and to map a
   `GeneratedSpeakerId` to a `CustomerSpeakerId`,
   and vice versa.
2. [DeleteSpeaker](../../../voiceid/latest/APIReference/API_DeleteSpeaker.md "../../../voiceid/latest/APIReference/API_DeleteSpeaker.md"): Completely remove all records for a
   caller/speaker from a Voice ID domain. All voiceprints and enrollment
   status is deleted immediately, and associated audio recordings are
   removed within 24 hours.
3. [ListSpeakers](../../../voiceid/latest/APIReference/API_ListSpeakers.md "../../../voiceid/latest/APIReference/API_ListSpeakers.md"): List all the speakers whose entries are
   present in a Voice ID domain. This API returns both the
   `CustomerSpeakerId` and `GeneratedSpeakerId`
   for a speaker. It returns a paginated output with the page size dictated
   in the API request.
4. [OptOutSpeaker](../../../voiceid/latest/APIReference/API_OptOutSpeaker.md "../../../voiceid/latest/APIReference/API_OptOutSpeaker.md"): Opt out a caller from a Voice ID domain.
   This API doesn't require the speaker to be present in Voice ID. A
   non-existing speaker can be opted-out using this API and Voice ID
   persists the opted out status and rejects future enrollment requests for
   this speaker. Opting out also removes voiceprints and any stored audio
   recordings for this caller.

## Watchlist management APIs

1. [CreateWatchlist](../../../voiceid/latest/APIReference/API_CreateWatchlist.md "../../../voiceid/latest/APIReference/API_CreateWatchlist.md"): Create a watchlist that fraudsters can be
   a part of.
2. [DeleteWatchlist](../../../voiceid/latest/APIReference/API_DeleteWatchlist.md "../../../voiceid/latest/APIReference/API_DeleteWatchlist.md"): Remove a custom fraudster watchlist from
   the Voice ID domain. To delete a watchlist, it must be empty. That is,
   it must not have any fraudsters associated to it. You can use the [DeleteFraudster](../../../voiceid/latest/APIReference/API_DeleteFraudster.md "../../../voiceid/latest/APIReference/API_DeleteFraudster.md") or [DisassociateFraudster](../../../voiceid/latest/APIReference/API_DisassociateFraudster.md "../../../voiceid/latest/APIReference/API_DisassociateFraudster.md") APIs to remove all fraudsters from a
   watchlist.

You cannot delete the default watchlist from a Voice ID
domain. 3. [DescribeWatchlist](../../../voiceid/latest/APIReference/API_DescribeWatchlist.md "../../../voiceid/latest/APIReference/API_DescribeWatchlist.md"): Determine if it is a default fraudster
watchlist, or a custom watchlist that you created, and obtain watchlist
details. 4. [ListWatchlists](../../../voiceid/latest/APIReference/API_ListWatchlists.md "../../../voiceid/latest/APIReference/API_ListWatchlists.md"): List all the watchlists in the Voice ID
domain. 5. [UpdateWatchlist](../../../voiceid/latest/APIReference/API_UpdateWatchlist.md "../../../voiceid/latest/APIReference/API_UpdateWatchlist.md"): Update the name and description of a
custom fraudster watchlist. You cannot modify details of the default
watchlist because it's managed by Voice ID.

## Fraudster management APIs

1. [AssociateFraudster](../../../voiceid/latest/APIReference/API_AssociateFraudster.md "../../../voiceid/latest/APIReference/API_AssociateFraudster.md"): Associate a fraudster to a watchlist in
   the same domain. You can associate a fraudster to multiple watchlists in
   a domain.
2. [DeleteFraudster](../../../voiceid/latest/APIReference/API_DeleteFraudster.md "../../../voiceid/latest/APIReference/API_DeleteFraudster.md"): Delete a fraudster from a Voice ID domain.
   Deleting the fraudster removes the fraudster from all watchlists it is a
   part of. It also deletes all voiceprints and associated audio recordings
   within 24 hours.
3. [DescribeFraudster](../../../voiceid/latest/APIReference/API_DescribeFraudster.md "../../../voiceid/latest/APIReference/API_DescribeFraudster.md"): Describe a fraudster's status in the
   Voice ID domain.
4. [DisassociateFraudster](../../../voiceid/latest/APIReference/API_DisassociateFraudster.md "../../../voiceid/latest/APIReference/API_DisassociateFraudster.md"): Disassociate a fraudsters from the
   watchlist specified. Note that a fraudster always has to be associated
   with at least one fraudster watchlist; an exception is thrown if you try
   to disassociate a fraudster from its only watchlist.

To remove the fraudster completely, use `DeleteFraudster`. 5. [ListFraudsters](../../../voiceid/latest/APIReference/API_ListFraudsters.md "../../../voiceid/latest/APIReference/API_ListFraudsters.md"): List all the fraudsters in a domain or a
specific watchlist. This API also returns the watchlists the fraudster
is a part of. It returns a paginated output with the page size dictated
in the API request.
