

# Staging environment reference
<a name="deploy-staging-vs-production"></a>

The table below compares staging with a second environment that an operator adds.


| Item | Staging | Second environment | 
| --- | --- | --- | 
| Deploy command |  `VSA_ADP_KB_ID=<kb-id> make deploy-staging`  | Operator-defined (mirror `deploy-staging`) | 
| Region | us-west-2 | Any region where Amazon Nova 2 Sonic is available | 
| CDK stack prefix |  `vsa-staging-*`  |  `vsa-<stage>-*`  | 
| AgentCore voice runtime |  `vsa_supervisor_bidi_staging`  |  `vsa_supervisor_bidi_<stage>`  | 
| AgentCore text runtime |  `vsa_supervisor_text_staging`  |  `vsa_supervisor_text_<stage>` *(configure separately)*  | 
| Nova 2 Sonic region | us-west-2 (native; matches execution-role region) | Must match the execution-role region | 
| Auto-deploy | Yes — GitHub Actions on push to main after Tier 1/2/3 evals pass | Operator-defined | 
| Demo seed | Runs automatically as part of `make deploy-staging`  |  `make seed STAGE=<stage>` after fresh deploy | 

**Note**  
Amazon Nova 2 Sonic voice is available in select regions. The staging environment uses us-west-2 natively; the execution-role region and the Nova 2 Sonic invocation region must match. Cross-region invocations are rejected by the bidirectional stream allowlist. Consult the Amazon Bedrock service documentation for the current Nova 2 Sonic regional availability table before choosing a second-environment region.