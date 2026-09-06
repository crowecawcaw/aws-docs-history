

# UI configuration troubleshooting
<a name="runtimeconfig-troubleshooting"></a>

## Problem: Fleet Manager UI shows missing endpoints after fresh deploy
<a name="problem-runtimeconfig-endpoint-race"></a>

After a fresh deployment, the Fleet Manager UI fails to reach one or more backend services (commands, data processing, simulation, or the conversational assistant). The browser console shows fetch errors against an empty or placeholder URL. The issue occurs because the UI stack is deployed before all sibling stacks are fully provisioned, so the `runtimeConfig.json` file is shipped with empty endpoint fields.

### Diagnosis
<a name="diagnosis-4"></a>

1. Fetch the live `runtimeConfig.json` from the CloudFront distribution:

   ```
   STAGE=staging
   CF_URL=$(aws cloudformation describe-stacks \
     --stack-name cms-$STAGE-ui \
     --query "Stacks[0].Outputs[?OutputKey=='CloudFrontDistributionUrl'].OutputValue" \
     --output text)
   curl -s $CF_URL/runtimeConfig.json | python3 -m json.tool
   ```

1. Look for empty string values for any of these keys: `commandsApiEndpoint`, `dataProcessingApiEndpoint`, `simulationApiEndpoint`, `vsaApiEndpoint`. If a field is empty and the corresponding stack is deployed, the race condition occurred.

### Resolution
<a name="resolution-22"></a>

Run `make regenerate-runtime-config` to re-read all deployed stack outputs and rewrite `runtimeConfig.json` in S3:

```
cd deployment
make regenerate-runtime-config \
  AWS_PROFILE=<profile> \
  AWS_REGION=<region> \
  DEPLOYMENT_STAGE=<stage>
```

After the command completes, perform a hard refresh in the browser (Cmd\+Shift\+R on macOS or Ctrl\+Shift\+R on Windows/Linux) to clear the cached `runtimeConfig.json`. CloudFront invalidation runs automatically as part of the make target; allow 60-120 seconds for the invalidation to propagate before retrying.

If the problem recurs after future deployments of individual stacks, run `make regenerate-runtime-config` after every stack deploy that adds a new backend service. As of v0.2.x, the `phase1`, `deploy-commands`, `deploy-simulation`, `data-processing`, and `deploy-ws-fanout` Makefile targets run this step automatically as a post-deploy soft step.