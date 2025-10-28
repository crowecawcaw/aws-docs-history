# Delete traffic distribution groups in Amazon Connect

Use the [DeleteTrafficDistributionGroup](../APIReference/API_DeleteTrafficDistributionGroup.md "../APIReference/API_DeleteTrafficDistributionGroup.md") API to delete a traffic distribution group that is no longer
needed.

###### Note

You cannot delete a traffic distribution group if phone numbers are claimed to
it. You must first release phone numbers from the traffic distribution group by
using the [ReleasePhoneNumber](../APIReference/API_ReleasePhoneNumber.md "../APIReference/API_ReleasePhoneNumber.md") API. After that, you can delete the
traffic distribution group.

You cannot release numbers from a traffic distribution group by using the
Amazon Connect console.

Your [DeleteTrafficDistributionGroup](../APIReference/API_DeleteTrafficDistributionGroup.md "../APIReference/API_DeleteTrafficDistributionGroup.md") API call will fail with an
`ResourceInUseException` if phone numbers are still claimed to the
traffic distribution group.
