# Team

Manage account-level team settings. Each account has a single team resource.

###### Contents

- [GetTeam](#acxd-team-getteam "#acxd-team-getteam")

## GetTeam

Gets the team settings for the authenticated account.

### Input

No parameters.

### Sample Request

```
await client.send(new GetTeamCommand({}));
```

### Output

```
{
  "teamId": "t1a2b3c4-5678-90ab-cdef-1234567890ab",
  "name": "Northwind Corp",
  "createdAt": "2026-07-30T18:39:14.741Z",
  "updatedAt": "2026-07-30T18:39:14.741Z"
}
```

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)
