# New dependency discovered events

The following is an example event emitted when dependency discovery identifies a
previously unseen dependency.

```

{
  "source": "aws.resiliencehub",
  "detail-type": "New Dependency Discovered",
  "detail": {
    "serviceArn": "arn:aws:resiliencehub:us-east-1:123456789012:service/checkout:abc123",
    "dependencyName": "api.stripe.com",
    "dependencyLocation": "third-party",
    "discoveredAt": "2026-05-12T10:30:00Z"
  }
}
```
