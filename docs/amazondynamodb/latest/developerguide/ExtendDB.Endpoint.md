

# Connecting your application

Set the endpoint URL to `http://localhost:18080` and set any AWS Region. The following example lists the tables in `extenddb-dev` with the AWS CLI:

```
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE \
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY \
aws dynamodb list-tables --region us-east-1 --endpoint-url http://localhost:18080
```

In the preceding command:

`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`  
The seeded AWS example credential.

`--region`  
Can be any value, because `extenddb-dev` does not validate the Region.

`--endpoint-url`  
The local endpoint, `http://localhost:18080`.

For AWS SDK code examples that use an endpoint override, see [Running the code examples in this Developer Guide](CodeSamples.md). Replace the localhost port in each example with `18080`, and use a credential that `extenddb-dev` accepts.