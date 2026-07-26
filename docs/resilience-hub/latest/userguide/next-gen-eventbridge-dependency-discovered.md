# New dependency discovered event

The following is an example event emitted when dependency discovery identifies a new
dependency for your service. This event is emitted after a stabilization period to reduce
noise during initial discovery.

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "detail-type": "New Dependency Discovered",
  "source": "aws.resiliencehub",
  "account": "111122223333",
  "time": "2026-01-15T10:30:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:resiliencehub:us-east-1:111122223333:service/my-service:abc123"
  ],
  "detail": {
    "dependencyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "dependencyName": "S3",
    "dnsName": "s3.us-east-1.amazonaws.com.",
    "location": "us-east-1",
    "provider": "AWS",
    "sourceRegions": [
      "us-east-1",
      "us-west-2"
    ]
  }
}
```

The `detail` object contains the following fields:

| Field            | Description                                                                 |
| ---------------- | --------------------------------------------------------------------------- |
| `dependencyId`   | The unique identifier of the discovered dependency.                         |
| `dependencyName` | The name of the dependency (for example, the AWS service name).             |
| `dnsName`        | The DNS name used by your service to communicate with the dependency.       |
| `location`       | The AWS Region or location where the dependency is hosted.                  |
| `provider`       | The dependency provider. Values include `AWS`,<br>`ThirdParty`, `Internal`. |
| `sourceRegions`  | The Regions from which your service communicates with this<br>dependency.   |
