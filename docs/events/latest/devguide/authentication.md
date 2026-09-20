

# Authentication
<a name="authentication"></a>

 Listing events, and reading the catalog of an event that does not require registration, need no credentials. For everything else the attendee signs in with an AWS Builder ID, the free personal sign-in that AWS uses for its developer tools and events, and your application sends the resulting OAuth 2.0 access token as a bearer token: 

```
curl -H "Authorization: Bearer $ACCESS_TOKEN" \
  https://api.awsevents.com/v1/events/reinvent2026/schedule
```

**Topics**
+ [Access token and event registration](auth-two-requirements.md)
+ [Endpoints and values](auth-endpoints.md)
+ [Signing an attendee in](auth-signing-in.md)
+ [Keeping the attendee signed in](auth-refreshing.md)
+ [Signing an attendee out](auth-signing-out.md)
+ [Handling tokens safely](auth-handling-tokens.md)