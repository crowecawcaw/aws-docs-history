

# Step 6: Smoke tests
<a name="deploy-step6-smoke-tests"></a>

Run the smoke tests after every deploy to verify the full stack is operational. Each test must exit zero.

```
# Text-mode agent (AgentCore HTTP path — no voice)
python3 scripts/smoke-test-agentcore.py

# Voice agent — single-turn (requires RUNTIME_ID)
python3 scripts/smoke-test-voice.py

# Cross-account KB Retrieve (requires VSA_ADP_KB_ID)
python3 scripts/smoke-test-kb-retrieve.py --stage <stage>

# Web UI /assistant/chat route (requires VSA_API_URL)
VSA_API_URL=https://<rest-api-id>.execute-api.<region>.amazonaws.com/<stage> \
  python3 scripts/smoke-test-assistant-chat.py
```

For staging, the `make demo-preflight` target bundles all pre-flight checks — CloudFormation stack status, runtime readiness, KB retrieval validation, and the per-persona Tier 3 smoke — in a single non-interactive command:

```
VSA_ADP_KB_ID=<adp-kb-id> make demo-preflight
```

## Eval pipeline
<a name="eval-pipeline"></a>

The tiered eval pipeline validates agent behavior before promoting a deploy:

```
make eval-tier1   # tool unit evals — fast, no live AWS calls (<2s)
make eval-tier2   # mocked-Nova conversation evals — fast (<2s)
make eval-tier3   # real AgentCore E2E — requires RUNTIME_ID; ~10 min; ~$1/run
make eval-all     # all three tiers sequentially
```

Tier 1 and Tier 2 evals run on every pull request via the GitHub Actions workflow. Tier 3 runs nightly and as a gate before the `deploy-staging` job in the workflow. See `docs/EVAL.md` for the full runbook.