# Nova Act SDK security

Be aware that Nova Act may encounter commands in the content it observes on third party websites, including user-generated content on trusted websites such as social media posts, search results, forum comments, news articles, and document attachments. These unauthorized commands, known as prompt injections, may cause the model to make mistakes or act in a manner that differs from its instructions, such as ignoring your instructions, performing unauthorized actions, or exfiltrating sensitive data.

We have trained Nova Act to deflect these attacks but cannot guarantee all prompt injection attacks will be deflected. To reduce the risks associated with prompt injections, it is important to monitor Nova Act and review its actions, especially when processing untrusted user-contributed content. We also recommend that developers use the following approaches to further reduce their risk wherever possible and appropriate. See below for details.

1. Domain restriction – use SDK state guardrails to enforce an allow/block list of URLs.
2. Tool use restriction – to minimize attack surfaces, only register tools relevant for a given workflow.
3. Local file access restriction - restrict access to `file://` path access unless necessary for a specific workflow. This is blocked by default in the SDK. We recommend developers to allow this capability only for select file-paths to complete a given workflow as needed.

## Nova Act SDK security options

The Nova Act SDK ships with secure default behaviors that should remain enabled unless your use case specifically requires otherwise. Disabling these defaults reduces the security posture of your system.

### Allow navigation to local file:// URLs

To enable local file navigation, define one or more filepath patterns in `SecurityOptions.allowed_file_open_paths`

```
from nova_act import NovaAct, SecurityOptions

NovaAct(starting_page="file://home/nova-act/site/index.html", SecurityOptions(allowed_file_open_paths=['/home/nova-act/site/*']))
```

### Allow file uploads

To allow the agent to upload files to websites, define one or more filepath patterns in `SecurityOptions.allowed_file_upload_paths`.

```
from nova_act import NovaAct, SecurityOptions
NovaAct(starting_page="https://example.com", SecurityOptions(allowed_file_upload_paths=['/home/nova-act/shared/*']))
```

### Filepath structures

The filepath parameters support the following formats:

- `["/home/nova-act/shared/*"]` - Allow from specific directory
- `["/home/nova-act/shared/file.txt"]` - Allow a specific filepath
- `["*"]` - Enable for all paths
- `[]` - Disable the feature (Default)

### State guardrails

State guardrails allow you to control which URLs the agent can visit during execution. You can provide a callback function that inspects the browser state after each observation and decides whether to allow or block continued execution. If blocked, act() will raise ActStateGuardrailError. This is useful for preventing the agent from navigating to unauthorized domains or sensitive pages.

```
from nova_act import NovaAct, GuardrailDecision, GuardrailInputState
from urllib.parse import urlparse
import fnmatch

def url_guardrail(state: GuardrailInputState) -> GuardrailDecision:
    hostname = urlparse(state.browser_url).hostname
    if not hostname:
        return GuardrailDecision.BLOCK

    # Example URL block-list
    blocked = ["*.blocked-domain.com", "*.another-blocked-domain.com"]
    if any(fnmatch.fnmatch(hostname, pattern) for pattern in blocked):
        return GuardrailDecision.BLOCK

    # Example URL allow-list
    allowed = ["allowed-domain.com", "*.another-allowed-domain.com"]
    if any(fnmatch.fnmatch(hostname, pattern) for pattern in allowed):
        return GuardrailDecision.PASS

    return GuardrailDecision.BLOCK

with NovaAct(starting_page="https://allowed-domain.com", state_guardrail=url_guardrail) as nova:
    # The following will be blocked if agent tries to visit a blocklisted domain or leave one of the allowlisted domains
    nova.act("Navigate to the homepage")
```
