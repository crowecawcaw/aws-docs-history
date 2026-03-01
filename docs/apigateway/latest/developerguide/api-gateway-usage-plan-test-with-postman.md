# Test usage plans for REST APIs in API Gateway

As an example, let's use the PetStore API, which was created in [Tutorial: Create a REST API by importing an example](api-gateway-create-api-from-example.md "api-gateway-create-api-from-example.md"). Assume that the API is
configured to use an API key of `Hiorr45VR...c4GJc`. The following steps
describe how to test a usage plan.

###### To test your usage plan

- Make a `GET` request on the Pets resource (`/pets`),
  with the `?type=...&page=...` query parameters, of the API
  (for example, `xbvxlpijch`) in a usage plan:

```
GET /testStage/pets?type=dog&page=1 HTTP/1.1
x-api-key: Hiorr45VR...c4GJc
Content-Type: application/x-www-form-urlencoded
Host: xbvxlpijch.execute-api.ap-southeast-1.amazonaws.com
X-Amz-Date: 20160803T001845Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160803/ap-southeast-1/execute-api/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-api-key, Signature={sigv4_hash}

```

###### Note

You must submit this request to the `execute-api` component
of API Gateway and provide the required API key (for example,
`Hiorr45VR...c4GJc`) in the required
`x-api-key` header.

The successful response returns a `200 OK` status code and a
payload that contains the requested results from the backend. If you forget
to set the `x-api-key` header or set it with an incorrect key,
you get a `403 Forbidden` response. However, if you didn't
configure the method to require an API key, you will likely get a `200
 OK` response whether you set the `x-api-key` header
correctly or not, and the throttle and quota limits of the usage plan are
bypassed.

Occasionally, when an internal error occurs where API Gateway is unable to
enforce usage plan throttling limits or quotas for the request, API Gateway serves
the request without applying the throttling limits or quotas as specified in
the usage plan. But, it logs an error message of `Usage Plan check
 failed due to an internal error` in CloudWatch. You can ignore such
occasional errors.
