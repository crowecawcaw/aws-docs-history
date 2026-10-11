

# Step 5: Tenant onboarding
<a name="deploy-step5-tenant-onboarding"></a>

## Seed demo data (staging and initial production)
<a name="seed-demo-data-staging-and-initial-production"></a>

After a fresh CDK deploy, seed the demo personas and tenant records. The `seed-staging` Makefile target runs all seed scripts. You can also run the individual scripts directly:

```
# For staging — these are invoked automatically by make deploy-staging
# Replace <stage> and <region> with your target values

# Seed the initial tenant configuration record and demo fleet operator data
STAGE=<stage> AWS_REGION=<region> python3 scripts/seed-meridian-fleet.py

# Create the demo user accounts in Cognito
STAGE=<stage> AWS_REGION=<region> python3 scripts/seed-meridian-fleet-user.py <email>

# Seed all persona demo users (fleet driver, vehicle owner, service advisor, etc.)
STAGE=<stage> AWS_REGION=<region> python3 scripts/seed-persona-users.py

# Seed persona context records into AgentCore Memory
STAGE=<stage> AWS_REGION=<region> python3 scripts/seed-personas.py

# Optionally seed service network fixture data (dealerships, service centers)
STAGE=<stage> AWS_REGION=<region> python3 scripts/seed-service-network.py

# Wire an Amazon Connect instance to the tenant routing record
STAGE=<stage> AWS_REGION=<region> python3 scripts/wire-connect-to-tenant.py
```

**Note**  
Use `make seed-staging` to run all seed scripts in the correct order. For a second environment, run the individual scripts above with the target stage and region values.

For a second environment, substitute `STAGE=<stage> AWS_REGION=<region>` and replace the placeholder credentials with the corresponding values.

## Onboard a new tenant (no code change required)
<a name="onboard-a-new-tenant-no-code-change-required"></a>

AVX multi-tenancy is configuration-driven. Every tenant is represented by a record in the `vsa-<stage>-tenants` DynamoDB table, defined by the schema in `schemas/vsa-tenant-config.schema.json`. To add a new tenant:

1. Write a tenant configuration record to DynamoDB. The record includes the tenant segment type (fleet, rental, or oem), Cognito user pool reference, Amazon Connect contact flow identifiers (using `<placeholder>` values during initial provisioning), and per-tenant feature flags.

1. Create Cognito users for the tenant’s personas via `scripts/seed-persona-users.py` or directly via the Cognito API, assigning the correct `cognito:groups` and `custom:role` attributes so the API Gateway persona inference routes correctly.

1. If the tenant requires Connect escalation, populate the Connect contact flow and queue ARNs in the tenant record after the Connect instance is configured.

No CDK redeploy is required to activate a new tenant. The `tenant-config-loader` Lambda reads the DynamoDB record at API request time and routes accordingly.

For the full tenant configuration schema — field definitions, allowed values, and per-feature toggle semantics — see the `schemas/vsa-tenant-config.schema.json` file in the repository.