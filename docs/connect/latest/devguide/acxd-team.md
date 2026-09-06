

# Team
<a name="acxd-team"></a>

Manage account-level team settings. Each account has a single team resource.

**Topics**
+ [GetTeam](#acxd-team-getteam)

## GetTeam
<a name="acxd-team-getteam"></a>

Gets the team settings for the authenticated account.

### Input
<a name="acxd-team-getteam-input"></a>

No parameters.

### Sample Request
<a name="acxd-team-getteam-sample-request"></a>

```
await client.send(new GetTeamCommand({}));
```

### Output
<a name="acxd-team-getteam-output"></a>

```
{
  "teamId": "t1a2b3c4-5678-90ab-cdef-1234567890ab",
  "name": "Northwind Corp",
  "createdAt": "2026-07-30T18:39:14.741Z",
  "updatedAt": "2026-07-30T18:39:14.741Z"
}
```

### Errors
<a name="acxd-team-getteam-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)