

# Signing requests

`extenddb-dev` verifies every request with AWS Signature Version 4 (SigV4). The downloadable version of DynamoDB does not. AWS SDKs and the AWS CLI sign requests automatically after you configure credentials.

On every start, `extenddb-dev` seeds and prints the documented AWS example credential:

```
Access key ID:     AKIAIOSFODNN7EXAMPLE
Secret access key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

Sign requests with this pair. To add one more credential, pass the `EXTENDDB_DEV_ACCESS_KEY_ID` and `EXTENDDB_DEV_SECRET_ACCESS_KEY` environment variables to the container. The access key ID must start with `AKIA`, and the example pair keeps working alongside it.