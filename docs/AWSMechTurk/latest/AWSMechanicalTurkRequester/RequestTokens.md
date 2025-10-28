# Use request tokens

Many of the API operations that have an impact on HITs or the money rewarded to workers,
such as `CreateHIT` and `SendBonus`, can include a
`UniqueRequestToken` attribute. This denotes a unique identifier for the
request that can be used in scenarios where you want to gracefully handle and retry errors
without creating duplicate HITs or payments. This is useful in cases such as network
timeouts, where it is unclear whether or not the call succeeded on the server. If the
operation has already been performed using the same `UniqueRequestToken`,
subsequent calls return an error with a message containing the request ID.

Note that the token must not be longer than 64 characters in length and it is your
responsibility to ensure uniqueness of the token. The unique token expires after 24 hours.
