# FIPS Endpoints for Administrative Use

To specify a FIPS endpoint when you run an AWS CLI command for AppStream 2.0, use the `endpoint-url` parameter. The following example uses the AppStream 2.0 FIPS endpoint in the US West (Oregon) Region to retrieve a list of all stacks in the Region:

```
`aws appstream describe-stacks --endpoint-url https://appstream2-fips.us-west-2.amazonaws.com`
```

To specify a FIPS endpoint for AppStream 2.0 API operations, use the procedure in your AWS SDK for specifying a custom endpoint.
