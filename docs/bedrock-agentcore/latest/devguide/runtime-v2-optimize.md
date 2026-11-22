

# Optimize your agent for Amazon Bedrock AgentCore Runtime V2

On platform version V1, AgentCore Runtime starts your container from scratch when a session starts. On platform version V2, AgentCore Runtime prepares your agent once, when you create or update the agent runtime, and takes a snapshot of it. The snapshot includes your agent’s memory and its files. Each session then starts by restoring that snapshot. This has four consequences for how you write your agent:
+  **What your agent holds in memory in the snapshot is ready when a session starts.** Your session code doesn’t have to load it again.
+  **The more your agent holds in memory, the longer each new session takes to start.** A few hundred MiB makes no noticeable difference. Several GiB can add seconds.
+  **Files in the snapshot are slower the first time a session reads them**, such as your code, your Python packages, native libraries, or a headless browser. It’s most noticeable in the first sessions after you create or update your agent.
+  **Values in the snapshot are shared by every session.** A random value, an identifier, or a timestamp that your agent creates before the snapshot is the same in every session.

This topic describes how to prepare your agent so that sessions start fast, and how to handle values that must be unique to each request, such as random values, timestamps, and credentials. For an overview of platform version V2, see [Platform versions](runtime-how-it-works.md#runtime-platform-versions).

## How AgentCore Runtime prepares your agent
<a name="runtime-v2-optimize-lifecycle"></a>

When you create or update an agent runtime, AgentCore Runtime prepares your agent before the runtime reaches `READY`:

1. It starts your container, and your agent starts its server.

1. It waits until your agent’s health check passes, for example when `GET /ping` returns a successful response. If the health check doesn’t pass in time, the create or update fails.

1. It takes a snapshot of your agent, including its memory, its files, and the processes that are still running.

Each session starts from that snapshot. To prepare your agent’s memory before the snapshot and its files after it, configure a build warmup hook. For more information, see [Prepare your agent before sessions start](#runtime-v2-optimize-warmup).

## Prepare your agent before sessions start
<a name="runtime-v2-optimize-warmup"></a>

To make sessions start fast, prepare your agent in three steps. Pass the health check quickly, then use a build warmup hook to load what sessions need into memory before the snapshot, and to make the files that sessions read fast after the snapshot. The hook’s `memory` and `disk` calls share 120 seconds. For how to configure the hook, see [Configure lifecycle hooks](runtime-lifecycle-hooks.md#runtime-lifecycle-hooks-configure).

### Step 1: Pass the health check
<a name="_initialize_once_at_startup"></a>

Before your health check passes, for example before `GET /ping` returns a successful response, do only what your server needs to accept requests, such as your imports and loading static configuration. Then report healthy right away, and do the rest in the warmup hook. If the health check doesn’t pass in time, the create or update fails.

### Step 2: Load what sessions need in the memory call
<a name="runtime-v2-optimize-memory"></a>

Everything that your process holds when the `memory` call returns is in the snapshot, so every session starts with it. Load your model, data, and clients here. If the `memory` call fails, the create or update fails.
+  **Keep what you load.** The snapshot holds only what your process still references when the `memory` call returns, so keep what you load in global variables. Data that you read and discard, such as a file read only to warm it, isn’t in the snapshot.
+  **Check that your model is really in memory.** Some libraries load only an index of the model file and read the weights on first use. Those first reads then happen in sessions.
+  **Load only what sessions need.** Sessions take longer to start the more memory they restore.
+  **Start programs that keep their own random state in the session.** A program that’s still running when the `memory` call returns, such as a headless browser, starts every session with the same random state, including the keys for its TLS connections. For an example, see [Example – Headless browser agent](#runtime-v2-optimize-example).

### Step 3: Run one session’s work in the disk call
<a name="runtime-v2-optimize-disk"></a>

Files in the snapshot are slow the first time a session reads them. In the `disk` call, read the files that a session reads when it starts. AgentCore Runtime uses these reads to make those files fast for new sessions. The simplest way to read the right files is to do once what your agent does on its first request. For example, for an agent that uses a browser, open an HTTPS page in the browser. Loading the page reads the files that the browser uses to make connections and display pages. New sessions then don’t wait for those reads. Keep it short, because the `disk` call shares 120 seconds with the `memory` call.

### Example – Headless browser agent
<a name="runtime-v2-optimize-example"></a>

The following FastAPI application uses a headless browser to return the title of a web page:
+ In the `memory` call, it starts a browser that sessions don’t use. That browser keeps Chromium’s files in memory in the snapshot, so a session launches its own browser in a fraction of a second instead of several seconds. Each session needs its own browser because a browser that’s running at the time of the snapshot has the same random state in every session, including the keys for its TLS connections.
+ In the `disk` call, it opens an HTTPS page, so that the files and the TLS setup that a page load uses are fast for new sessions.
+ Each request opens and closes its own page in the session’s browser. Without the hook, the first request launches the browser, so the application also works without the hook.

In a test with 100 new sessions, the first response in a session took 2.9 seconds at the median and 3.6 seconds at the 90th percentile with the warmup hook, compared with 5.4 and 32.3 seconds without it.

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from playwright.async_api import async_playwright

app = FastAPI()
playwright = None
snapshot_browser = None  # keeps Chromium's files in memory in the snapshot; sessions don't use it
browser = None  # each session launches its own


async def get_browser():
    # Launch this session's own browser. A browser from the snapshot would give
    # every session the same random numbers, including its TLS keys.
    global playwright, browser
    if browser is None or not browser.is_connected():
        playwright = playwright or await async_playwright().start()
        browser = await playwright.chromium.launch()
    return browser


@asynccontextmanager
async def open_page(url):
    # Open the URL in a new page; the page closes when the block ends.
    page = await (await get_browser()).new_page()
    try:
        await page.goto(url)
        yield page
    finally:
        await page.close()


@app.get("/ping")
def ping():
    return {"status": "Healthy"}


@app.post("/warmup")
async def warmup(request: Request):
    global playwright, snapshot_browser
    warmup_type = request.headers.get(
        "X-Amzn-Bedrock-AgentCore-Runtime-Warmup-Type", ""
    ).lower()
    if warmup_type == "memory":
        # Start a browser that sessions don't use. Its files stay in memory in the
        # snapshot, so each session launches its own browser quickly.
        playwright = await async_playwright().start()
        snapshot_browser = await playwright.chromium.launch()
    elif warmup_type == "disk":
        # Open one page, as a session does, so that its files are fast for new sessions.
        async with open_page("https://example.com"):
            pass
    return {"status": "ok"}


@app.post("/invocations")
async def invoke(request: Request):
    payload = await request.json()
    async with open_page(payload["url"]) as page:
        return {"title": await page.title()}
```

The following Dockerfile installs snapshot-safe OpenSSL, Python, and the browser into an Amazon Linux 2023 container image:

```dockerfile
FROM --platform=linux/arm64 public.ecr.aws/amazonlinux/amazonlinux:2023

WORKDIR /app

# Swap in snapshot-safe OpenSSL for Python's ssl module, and install Python 3.11.
RUN dnf swap -y openssl-libs openssl-snapsafe-libs \
    && dnf install -y python3.11 python3.11-pip && dnf clean all
# The Playwright driver needs libatomic on ARM64; Chromium needs the rest.
RUN dnf install -y libatomic alsa-lib at-spi2-atk cups-libs libXcomposite \
    libXdamage libXrandr libxkbcommon mesa-libgbm nss pango && dnf clean all
RUN pip3.11 install --no-cache-dir fastapi==0.162.7 uvicorn==0.54.0 playwright==1.65.1
RUN playwright install chromium

COPY app.py .
EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
```

Create the agent runtime on platform version V2 with a build warmup hook that calls `POST /warmup` on port `8080`. For more information, see [Configure lifecycle hooks](runtime-lifecycle-hooks.md#runtime-lifecycle-hooks-configure).

If you don’t configure a build warmup hook, AgentCore Runtime takes the snapshot as soon as your health check passes. Anything that sessions need in memory must then load before your health check passes, and the first requests of new sessions read their files slowly.

## Considerations for code that runs before the snapshot
<a name="_keep_per_request_state_fresh"></a>

Every session starts from the same snapshot. Any value that your agent creates before the snapshot is the same in every session, and fixed at the time of the snapshot. The following topics describe what to create in your request handler instead.

**Topics**

### Random values, identifiers, and cryptographic libraries
<a name="_use_snapshot_safe_cryptographic_libraries"></a>

Every session starts with the same copy of your agent’s memory, including the state of its random number generators. Python’s `random` module and JavaScript’s `Math.random()` repeat the same sequence in every session.
+ Generate secrets, keys, tokens, and identifiers in your handler, and get random values from the operating system, for example with Python’s `secrets` or `os.urandom()`, Go’s `crypto/rand`, or by reading `/dev/urandom`.
+ Use a snapshot-safe cryptographic library, which reseeds after a restore, such as AWS-LC or the snapshot-safe OpenSSL. Direct code deployments already use the snapshot-safe OpenSSL. In a container image based on Amazon Linux 2023, install it with the following line in your Dockerfile:

  ```dockerfile
  RUN dnf swap -y openssl-libs openssl-snapsafe-libs
  ```

  Other builds of OpenSSL, including ones that libraries bundle, can repeat values across sessions.
+ In Node.js, call `crypto.randomUUID({ disableEntropyCache: true })`. By default, `randomUUID()` caches random data, so a cache filled before the snapshot repeats in every session. If `node -p process.config.variables.node_shared_openssl` prints `false`, your Node.js bundles its own OpenSSL, and all `crypto` random functions can repeat. Read `/dev/urandom` instead.
+ Don’t use the hostname (`localhost`) or PID (`1`) as an identifier. They’re the same in every session.

### Current time and elapsed time
<a name="runtime-v2-optimize-time"></a>

A timestamp that your agent takes before the snapshot is fixed at the time of the snapshot. Read the current time in your handler.

 `time.monotonic()` doesn’t advance across a restore. A duration measured from a reference taken before the snapshot is wrong without looking wrong, so take the reference timestamp in your handler.

### Credentials, clients, and connections
<a name="_networking"></a>

Create reusable clients before the snapshot. The socket that a client opens doesn’t survive a restore. However, the setup that the client library caches around it does survive, such as service-model parsing, endpoint resolution, credential resolution, and the connection pool. The first call after a restore re-establishes the connection.

Credentials that your agent loads before the snapshot can expire before a session starts, and they don’t include the session’s context keys. Refresh credentials when they expire. If your policies use session context keys, create AWS SDK clients in your handler from a new boto3 `Session`. For more information, see [Session context keys](runtime-sessions.md#runtime-session-isolation).

Don’t bind outgoing connections to a fixed source port. A socket that was open at the time of the snapshot still holds its port after a restore, so a new connection that binds the same port fails.

The following code creates a reusable Bedrock client before the snapshot and creates session-specific clients in the request handler:

```python
import boto3
from fastapi import FastAPI, Request

app = FastAPI()

# Created before the snapshot and reused by every session. Its credentials
# don't include session context keys.
bedrock = boto3.client("bedrock-runtime")


@app.post("/invocations")
async def invoke(request: Request):
    session_id = request.headers["X-Amzn-Bedrock-AgentCore-Runtime-Session-Id"]

    # Create clients that need session context keys from a new boto3 Session,
    # so that they load the session's credentials.
    s3 = boto3.Session().client("s3")
    state = s3.get_object(Bucket="amzn-s3-demo-source-bucket", Key=f"sessions/{session_id}/state.json")
    # Handle the request.
```

### Data that can change without an update
<a name="runtime-v2-optimize-changing-data"></a>

Data that your agent fetches before the snapshot is fixed in the snapshot. Every session uses that copy until you update the agent runtime. Fetch data that can change without an update, such as the list of tools from an AgentCore Gateway, for each session or when it can have changed.