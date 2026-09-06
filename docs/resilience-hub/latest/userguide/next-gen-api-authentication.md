

# Making API requests and authentication
<a name="next-gen-api-authentication"></a>

**Endpoint**

```
https://resiliencehub.{region}.amazonaws.com
```

**API version**

Next generation Resilience Hub APIs use the `/v3` path prefix. All requests must be signed with AWS Signature Version 4 (SigV4).

**Authentication**

All API calls require valid AWS credentials. Next generation Resilience Hub uses AWS IAM for authorization. Ensure your IAM policy grants the necessary `resiliencehub:*` actions.