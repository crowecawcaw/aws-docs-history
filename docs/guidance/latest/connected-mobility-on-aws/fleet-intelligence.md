

# Fleet Intelligence
<a name="fleet-intelligence"></a>

Fleet Intelligence is the Tier 1 deterministic replacement for the retired Virtual Fleet Operator (VFO) fleet-view surface. It surfaces cost-per-mile, preventive-maintenance compliance, fleet rebalancing, warranty (read-only recalls and coverage), and per-vehicle sell-timing analysis in the Fleet Manager UI under `/fleet-intelligence/*`. `/fleet-intelligence/lifecycle` is the landing route.

## FleetIntelligenceAnalyticsStack
<a name="fleet-intelligence-analytics-stack"></a>

The stack deploys an Amazon Athena workgroup and a results S3 bucket in `us-east-1`. Fleet Intelligence services in the `us-west-2` deployment region read cross-region against the Automotive Data Platform (ADP) accelerator’s curated products (`service_records`, `charging_sessions`, `energy_usage`) through that workgroup. The stack lives in the `us-east-1` Region so its resources sit adjacent to the ADP data catalog; the CMS Lambda functions reading through it authenticate via Lake Formation grants owned by the ADP producer account plus a cross-account KMS `Decrypt` scoped by `kms:ViaService=s3.us-east-1.amazonaws.com`.

## Fleet Intelligence services
<a name="fleet-intelligence-consumer"></a>

The `services/fleet_intelligence/` module contains the deterministic renderers behind the four fleet-view routes and their supporting Athena reader (`adp_source.py`). Each renderer reads maintenance cost per vehicle per month directly from ADP curated products rather than materializing a Tier 2 artifact. Sell-timing analysis uses a linear-fit of maintenance cost versus straight-line depreciation to compute a crossover month, fit R², and provenance — all deterministic and reproducible for a given `snapshot_date`.