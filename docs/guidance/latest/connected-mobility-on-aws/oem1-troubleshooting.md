

# OEM1 fleet lifecycle troubleshooting
<a name="oem1-troubleshooting"></a>

## Problem: OEM1 admin Lambda returns 4xx on enrollment or unenrollment
<a name="problem-oem1-admin-lambda-4xx"></a>

Calls to `/admin/oem1/bulk-enroll`, `/admin/oem1/bulk-unenroll`, or `/admin/oem1/enroll-quota` return HTTP 400 or 403. CloudWatch logs show either an authorization failure or a quota-exceeded message.

### Diagnosis
<a name="diagnosis-3"></a>

1. Check the Lambda logs for the root cause:

   ```
   STAGE=staging
   aws logs tail /aws/lambda/cms-$STAGE-connector-oem1-admin-bulk-enroll \
     --since 15m --filter-pattern "?ERROR ?Unauthorized ?quota"
   ```

1. Verify the calling user belongs to the `platform-admin` or `fleet-operator` Cognito group:

   ```
   USER_POOL_ID=$(aws cloudformation describe-stacks \
     --stack-name cms-$STAGE-ui \
     --query "Stacks[0].Outputs[?OutputKey=='UserPoolId'].OutputValue" \
     --output text)
   aws cognito-idp admin-list-groups-for-user \
     --user-pool-id $USER_POOL_ID \
     --username <user-email>
   ```

1. Check remaining hourly enrollment quota:

   ```
   # Query the quota endpoint directly
   aws lambda invoke \
     --function-name cms-$STAGE-connector-oem1-admin-enroll-quota \
     --payload '{}' /tmp/quota-response.json && cat /tmp/quota-response.json
   ```

### Resolution
<a name="resolution-21"></a>

 **If the error is 403 — user not in required group:** 

The `/admin/oem1/*` routes require the caller to be in the `platform-admin` group (cross-fleet authority) or the `fleet-operator` group (per-fleet authority via the `custom:fleetIds` claim). Add the user to the appropriate group:

```
STAGE=staging
USER_POOL_ID=$(aws cloudformation describe-stacks \
  --stack-name cms-$STAGE-ui \
  --query "Stacks[0].Outputs[?OutputKey=='UserPoolId'].OutputValue" \
  --output text)

# Add to platform-admin for cross-fleet admin authority
aws cognito-idp admin-add-user-to-group \
  --user-pool-id $USER_POOL_ID \
  --username <user-email> \
  --group-name platform-admin
```

The user must sign out and sign back in for the new group claim to take effect in their JWT.

 **If the error is 400 — enrollment quota exceeded (4 enrollments per hour):** 

The OEM1 connector enforces a rolling hourly enrollment quota of four enrollments per hour per fleet. This quota is tracked in DynamoDB. Wait until the quota window resets, or check the `enroll-quota` endpoint to see when the window expires:

```
aws lambda invoke \
  --function-name cms-$STAGE-connector-oem1-admin-enroll-quota \
  --payload '{"fleet_id": "<fleet-id>"}' /tmp/quota.json && cat /tmp/quota.json
```

Spread enrollment requests across multiple hourly windows if you need to enroll more than four vehicles.

 **If the error is 400 — credential not consented:** 

The OEM1 OAuth credentials may not have been granted admin consent in the identity provider. Verify that the application registration has admin consent for the required API scopes. Consult your OEM1 account manager to confirm consent status and re-grant if necessary.