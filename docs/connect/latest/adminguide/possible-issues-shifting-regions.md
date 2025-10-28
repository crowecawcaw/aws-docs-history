# Tips for avoiding issues when

shifting agents in your Amazon Connect instance across Regions

- Whenever you update the traffic distribution for agents be sure to
  also update the traffic distribution for inbound voice contacts.
  Otherwise, you might end up in a situation where one Region is heavy on
  agents while the other is heavy on telephony traffic.
- Before associating users to a traffic distribution group, make sure
  the same username exists in both the source and replica Amazon Connect instances.
  Otherwise, when you associate a user to a traffic distribution group but
  the user with the username does not exist in the replica Region, you
  will get an `InvalidRequestException` error.
- You must call the [AssociateTrafficDistributionGroupUser](../APIReference/API_AssociateTrafficDistributionGroupUser.md "../APIReference/API_AssociateTrafficDistributionGroupUser.md") API to associate
  agents to a traffic distribution group in the source Region. If you attempt to do this while
  in the replica Region, you will get a
  `ResourceNotFoundException` error.
