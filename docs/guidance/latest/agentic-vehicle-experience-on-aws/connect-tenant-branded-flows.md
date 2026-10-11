

# Tenant-branded contact flows
<a name="connect-tenant-branded-flows"></a>

Every tenant operates its own set of Amazon Connect contact flows. Tenancy is first-class: one Connect instance, multiple contact flows differentiated by tenant configuration. `/escalate` resolves the tenant from the caller’s verified `custom:tenantId` claim and reads that tenant’s Connect settings.


| Contact flow element | Tenant-specific configuration | 
| --- | --- | 
| Greeting prompt | Text or audio prompt personalized with the tenant’s brand voice. Stored in Connect prompts library, referenced by prompt name from the tenant config record. | 
| Nova 2 Sonic voice profile | Each tenant selects a Nova 2 Sonic voice ID that matches its brand — conversational for consumer contexts, professional for fleet and commercial contexts. | 
| Hours of operation | Connect Hours of Operation block configured per tenant. Outside-hours routing sends the caller to a voicemail queue or a partner roadside-assistance line rather than an AVX agent session. | 
| Escalation queues | One chat queue for every human handoff (`escalation.tier2QueueArn`), named per tenant convention (for example, `<tenant>-fleet-support`). The chat contact flow reads the `severity` contact attribute and sends P0 to a high-priority branch of that queue. A tenant that offers the P0 callback also names a callback contact flow and a callback queue, or a claimed number, as caller ID (`escalation.callback`). The tenant config record in DynamoDB (`vsa-tenant-config`) stores both. | 
| Language and locale | Nova 2 Sonic supports multiple languages natively. The tenant config sets the default locale; the contact flow passes it as a session attribute so the supervisor system prompt and Nova 2 Sonic voice are locale-matched from the first utterance. | 
| Custom prompts | Consent recordings, privacy disclosures, and brand-specific transition phrases are stored as Connect prompts and referenced from the contact flow by logical name. | 

## Wiring tenant config to Connect
<a name="wiring-tenant-config-to-connect"></a>

The script `scripts/wire-connect-to-tenant.py` reads the outputs of the deployed `cvx-{stage}-connect` stack and writes the Connect instance, the chat contact flow and the queue ARNs into the tenant’s active config version. Run it once after deploying a new tenant’s Connect resources:

```
VSA_STAGE=staging VSA_TENANT_ID=<tenant-id> AWS_REGION=us-east-1 \
  python3 scripts/wire-connect-to-tenant.py
```

After the script completes, the `vsa-tenant-config` entry for the tenant holds the Connect identifiers `/escalate` needs, with no hard-coded values in application code. The P0 callback is configured by hand, in a new config version: see [P0 callback](connect-escalation-queues.md#connect-p0-callback).

**Note**  
The Connect instance ID is a deployment-time value obtained from the AWS Management Console or from `aws connect list-instances`. Do not embed it in source code or configuration files committed to version control; reference it via the environment variable `CONNECT_INSTANCE_ID` or the CDK stack output for your deployment.