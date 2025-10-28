# Troubleshoot AgentCore built-in tools

This section provides solutions to common issues you might encounter when using Amazon Bedrock AgentCore built-in tools.

## Browser tool issues

### Permission denied errors

**Symptom:** Errors mentioning access denied or insufficient permissions.

**Solution:**

- Verify your IAM user or role has the required Browser permissions
- Check your AWS credentials: `aws sts get-caller-identity`
- For recording: Verify the execution role has Amazon S3 write permissions
- For recording: Confirm the trust policy allows `bedrock-agentcore.amazonaws.com` to assume the role

### Model access denied

**Symptom:** Errors about model access or authorization when running agents.

**Solution:**

- Navigate to the Amazon Bedrock console
- Go to **Model access** in the left navigation
- Enable **Anthropic Claude Sonnet 4**
- Verify you're in the correct region (match the region in your code)

### Browser session timeout

**Symptom:** Browser sessions end unexpectedly or timeout errors occur.

**Solution:**

- Check the `sessionTimeoutSeconds` parameter when starting sessions
- Default timeout is 900 seconds (15 minutes)
- Increase timeout for longer sessions: `sessionTimeoutSeconds=1800`
- Sessions automatically stop after the timeout period

### Recording not appearing in Amazon S3

**Symptom:** No recording files in your Amazon S3 bucket after session completes.

**Solution:**

- Verify the execution role has correct Amazon S3 permissions
- Confirm the Amazon S3 bucket name and prefix are correct
- Check the execution role trust policy includes bedrock-agentcore service
- Review CloudWatch Logs for Amazon S3 upload errors
- Ensure the session ran for at least a few seconds (very short sessions may not generate recordings)

### Playwright connection errors

**Symptom:** Cannot connect to browser with Playwright or WebSocket errors.

**Solution:**

- Verify you installed playwright: `pip install playwright`
- Confirm the browser session started successfully before connecting
- Check that the session is still active (not timed out)
- Verify your network allows WebSocket connections

### Agent cannot make progress due to CAPTCHA checks

**Issue:** Your agent gets blocked by CAPTCHA verification when using the Browser tool to interact with websites.

**Cause:** Anti-bot measures on popular websites detect automated browsing and require human verification.

**Solution:** Structure your agent to avoid search engines and implement the following architecture pattern:

- Use the Browser tool only for specific page actions, not general web searching
- Use non-browser MCP tools like Tavily search for general web search operations
- Consider adding a live view feature to your agent application that allows end users to take control and solve CAPTCHAs when needed

### CORS errors when integrating with browser applications

**Issue:** Cross-Origin Resource Sharing (CORS) errors occur when building browser-based web applications that call a custom Amazon Bedrock AgentCore runtime server.

**Cause:** Browser security policies block cross-origin requests to your runtime server during local development or self-hosted deployment.

**Solution:** Add CORS middleware to your BedrockAgentCoreApp to handle cross-origin requests from your frontend:

```

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from fastapi.middleware.cors import CORSMiddleware

app = BedrockAgentCoreApp()

# Add CORS middleware to allow browser requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Customize in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Handle browser preflight requests to /invocations
@app.options("/invocations")
async def options_handler():
    return {"message": "OK"}

@app.entrypoint
def my_agent(payload):
    return {"response": "Hello from agent"}

```

###### Important

In production environments, replace `allow_origins=["*"]` with specific domain origins for better security.

## Code Interpreter issues

For general Code Interpreter troubleshooting, see the specific documentation for [Execute code and analyze data using
Amazon Bedrock AgentCore Code Interpreter](code-interpreter-tool.md "code-interpreter-tool.md").

Common issues with Code Interpreter typically relate to:

- Code execution timeouts
- Memory limitations during data processing
- Package installation restrictions

For detailed troubleshooting steps, refer to the Code Interpreter tool documentation.
