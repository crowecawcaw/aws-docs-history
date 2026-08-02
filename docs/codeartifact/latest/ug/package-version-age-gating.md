# Gating packages on version age

###### Important

Version age gating does not protect against vulnerabilities discovered in existing
versions that have already passed the quarantine window. Use CodeArtifact with Amazon Inspector
for vulnerability scanning of established packages.

When a package version is published to a public registry, the registry records the publish
timestamp. CodeArtifact preserves these original upstream timestamps when it caches packages from
external connections. You can read these timestamps in your CI/CD pipeline and reject versions
that were published too recently.

Most malicious packages are detected and removed within hours of publication. A quarantine
window of 3 to 7 days blocks the majority of supply chain attacks, including dependency
confusion, maintainer account takeover, and typosquatting.

###### Note

The examples in this topic query the CodeArtifact repository URL, which is the same
endpoint your package manager uses to download packages. All requests require
authentication. Pass a valid CodeArtifact authorization token in the
`Authorization: Bearer` header. To get a token, run
`aws codeartifact get-authorization-token` (see the CI/CD example later in
this topic for the full invocation with `--domain` and
`--domain-owner`).

Do not use the `publishedTime` field returned by
`aws codeartifact describe-package-version` for age gating. This field is
populated at ingestion time. For records where the original upstream publish time was
not captured (including packages ingested before per-artifact timestamp capture was
introduced, and certain ingestion paths), it silently falls back to the record's
last-updated time. The API response does not indicate which of the two values you are
reading, so you cannot rely on it as the upstream publish date. Use the per-format
fields described in this topic instead.

The per-format details differ, but the gating pattern is the same for every format: read
the upstream publish timestamp for each resolved version, compare it against your quarantine
cutoff (the current time minus your chosen window), and fail the build if any version is
newer than the cutoff. If you use more than one package format, you apply the same pattern
with the format-specific field shown below.

## npm

CodeArtifact returns the original npmjs.org publish timestamp for every version in the
npm packument `time` field. Many package managers and security tools read
this field natively. These include the Yarn 4 `npmMinimalAgeGate` option,
the Renovate `minimumReleaseAge` setting, and the pnpm
`minimumReleaseAge` setting, all of which work with CodeArtifact without
modification.

**Request:**

```
curl -H "Authorization: Bearer $CODEARTIFACT_AUTH_TOKEN" \
  https://my-domain-111122223333.d.codeartifact.us-east-1.amazonaws.com/npm/my-repo/axios
```

**Response (abbreviated):**

```
{
  "name": "axios",
  "time": {
    "1.6.0": "2023-10-26T21:15:55.685Z",
    "1.6.5": "2024-01-05T19:52:15.051Z",
    "1.7.0": "2024-05-19T20:25:03.615Z",
    "1.7.1": "2024-05-20T13:32:52.757Z",
    "1.7.2": "2024-05-21T16:58:04.163Z"
  }
}
```

**Key field:** `time["<version>"]` —
the value is the original publish date from npmjs.org. For example,
`time["1.7.2"]` returns `2024-05-21T16:58:04.163Z`, which is
the exact timestamp recorded by npmjs.org when that version was published.
To gate on age, compare this value to the current time minus your quarantine window.

## Maven

For Maven artifacts, CodeArtifact returns the original Maven Central publish timestamp in
the `Last-Modified` HTTP response header when you download a file (JAR, POM,
or other artifact).

**Request:**

```
curl -I -H "Authorization: Bearer $CODEARTIFACT_AUTH_TOKEN" \
  https://my-domain-111122223333.d.codeartifact.us-east-1.amazonaws.com/maven/my-repo/\
org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.pom
```

**Response headers:**

```
HTTP/2 200
content-type: application/xml
Last-Modified: Fri, 26 Feb 2021 20:40:52 GMT
content-length: 22672
```

**Key field:** `Last-Modified` header —
this is the original publish date from Maven Central. Compare it to your quarantine
cutoff to determine if the artifact is too new.

###### Note

The `<lastUpdated>` field inside `maven-metadata.xml`
reflects when CodeArtifact last refreshed its cache, not the upstream publish date. Do not
use `maven-metadata.xml` timestamps for age gating.

## NuGet

For NuGet packages, CodeArtifact returns the original nuget.org publish timestamp in the
`published` field of the V3 registration response.

**Request:**

```
curl -H "Authorization: Bearer $CODEARTIFACT_AUTH_TOKEN" \
  https://my-domain-111122223333.d.codeartifact.us-east-1.amazonaws.com/nuget/my-repo/\
v3/registration4/newtonsoft.json/index.json
```

**Response (abbreviated, showing one version):**

```
{
  "items": [{
    "items": [{
      "catalogEntry": {
        "id": "Newtonsoft.Json",
        "version": "13.0.3",
        "published": "2023-03-08T07:42:54.647+00:00",
        "listed": true
      }
    }]
  }]
}
```

**Key field:** `catalogEntry.published` —
this is the original publish date from nuget.org. For example,
`"2023-03-08T07:42:54.647+00:00"` means Newtonsoft.Json 13.0.3 was
published on March 8, 2023.

## Cargo (Rust)

For Cargo crates pulled from crates.io, CodeArtifact preserves the original publish
timestamp in the crates.io V1 API `versions` response. Query the V1 API
endpoint for a crate to read the per-version `created_at` timestamp.

**Request:**

```
curl -H "Authorization: Bearer $CODEARTIFACT_AUTH_TOKEN" \
  https://my-domain-111122223333.d.codeartifact.us-east-1.amazonaws.com/cargo/my-repo/\
api/v1/crates/serde/versions
```

**Key field:** The per-version `created_at`
timestamp in the V1 `versions` response is the original crates.io publish
date.

###### Note

Cargo uses the sparse index protocol
(`<prefix>/<crate>`) for normal dependency resolution. The
sparse index returns `vers`, `cksum`, `yanked`, and
`features` for each version, but it does not include a publish timestamp.
To gate Cargo dependencies on age, query the V1 API shown above in a separate step in
your pipeline. The standard `cargo build` and `cargo update`
commands do not call the V1 API.

## PyPI

For Python packages, CodeArtifact supports PEP 691 (JSON Simple API) and PEP 700, which
include the `upload-time` field for each distribution file.

**Request:**

```
curl -H "Authorization: Bearer $CODEARTIFACT_AUTH_TOKEN" \
  -H "Accept: application/vnd.pypi.simple.v1+json" \
  https://my-domain-111122223333.d.codeartifact.us-east-1.amazonaws.com/pypi/my-repo/simple/requests/
```

**Response (abbreviated):**

```
{
  "files": [{
    "filename": "requests-2.31.0-py3-none-any.whl",
    "upload-time": "2023-05-22T15:12:42.313790Z",
    "size": 62574,
    "url": "../../packages/requests/2.31.0/requests-2.31.0-py3-none-any.whl"
  }]
}
```

**Key field:** `upload-time` —
this is the original publish date from PyPI. Tools such as `uv` support
this natively:

```
# Only install versions published before a specific date
uv pip install --exclude-newer 2026-05-01T00:00:00Z -r requirements.txt
```

###### Note

The PEP 691 JSON API requires the `Accept: application/vnd.pypi.simple.v1+json`
header. The default HTML Simple API does not include timestamps.

For distribution files ingested before per-artifact upload-time capture was
introduced (legacy records), the `upload-time` field may be absent from
entries in `files[]`. Your gating logic should treat a missing
`upload-time` as a version it cannot verify, and decide whether to allow
or block it according to your policy.

## Example: Gating npm packages in CI/CD

The following Python script reads a `package-lock.json` file, queries
CodeArtifact for the publish timestamp of each dependency, and exits with a non-zero status
if any version was published within the quarantine window.

```
#!/usr/bin/env python3
"""
gate_package_age.py - Block npm packages published too recently.

Reads package-lock.json, queries CodeArtifact for each dependency's
publish timestamp, and rejects versions newer than QUARANTINE_HOURS.

Environment variables:
  CODEARTIFACT_AUTH_TOKEN  - from `aws codeartifact get-authorization-token`
  CODEARTIFACT_NPM_ENDPOINT - from `aws codeartifact get-repository-endpoint`
  QUARANTINE_HOURS - minimum version age in hours (default: 72)
"""
import json, os, sys, urllib.request
from datetime import datetime, timezone, timedelta

def get_publish_time(endpoint, token, package, version):
    """Fetch the publish timestamp for a specific version from CodeArtifact."""
    url = f"{endpoint.rstrip('/')}/{package}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    data = json.loads(urllib.request.urlopen(req, timeout=30).read())
    time_str = data.get("time", {}).get(version)
    if not time_str:
        return None
    return datetime.fromisoformat(time_str.replace("Z", "+00:00"))

token = os.environ["CODEARTIFACT_AUTH_TOKEN"]
endpoint = os.environ["CODEARTIFACT_NPM_ENDPOINT"]
quarantine_hours = int(os.environ.get("QUARANTINE_HOURS", "72"))
cutoff = datetime.now(timezone.utc) - timedelta(hours=quarantine_hours)

with open("package-lock.json") as f:
    lockfile = json.load(f)

blocked = []
checked = 0
for path, info in lockfile.get("packages", {}).items():
    if not path.startswith("node_modules/"):
        continue
    name = path.replace("node_modules/", "", 1)
    version = info.get("version")
    if not name or not version:
        continue
    checked += 1
    pub_time = get_publish_time(endpoint, token, name, version)
    if pub_time and pub_time > cutoff:
        age_h = (datetime.now(timezone.utc) - pub_time).total_seconds() / 3600
        blocked.append(f"  {name}@{version} (age: {age_h:.0f}h, published {pub_time.isoformat()})")

if blocked:
    print(f"BLOCKED: {len(blocked)} package(s) newer than {quarantine_hours} hours:")
    print("\n".join(blocked))
    sys.exit(1)
print(f"PASSED: all {checked} packages older than {quarantine_hours} hours.")
```

**CI/CD integration:**

```
# Step 1: Authenticate
export CODEARTIFACT_AUTH_TOKEN=$(aws codeartifact get-authorization-token \
  --domain my-domain --domain-owner 111122223333 \
  --query authorizationToken --output text)

export CODEARTIFACT_NPM_ENDPOINT=$(aws codeartifact get-repository-endpoint \
  --domain my-domain --domain-owner 111122223333 \
  --repository my-repo --format npm \
  --query repositoryEndpoint --output text)

# Step 2: Set quarantine window (72 hours = 3 days)
export QUARANTINE_HOURS=72

# Step 3: Generate lockfile without installing
npm install --package-lock-only

# Step 4: Gate on age — fails if any dependency is too new
python3 gate_package_age.py

# Step 5: If gate passes, install
npm ci
```

**Example output when a package is blocked:**

```
BLOCKED: 1 package(s) newer than 72 hours:
  evil-package@1.0.0 (age: 2h, published 2026-06-03T08:30:00+00:00)
```

**Example output when all packages pass:**

```
PASSED: all 847 packages older than 72 hours.
```

## Attacks mitigated

| Attack type          | How it works                                                                                                           | How age gating helps                                                                                   |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Dependency confusion | Attacker publishes a high-version package with the same name as an<br>internal package to a public registry.           | The malicious version is brand new. Blocked by quarantine window.                                      |
| Account takeover     | Attacker compromises a maintainer's credentials and publishes a<br>malicious update (for example, event-stream).       | The new version is held. Community detects and reverts it within<br>the quarantine period.             |
| Typosquatting        | Attacker publishes a package with a name similar to a popular<br>package (for example, `lodashs` instead of `lodash`). | All versions of the typosquat package are new. Every version is<br>blocked.                            |
| Star-jacking         | Attacker injects malware into a patch release of a legitimate<br>package they control.                                 | The malicious patch is a newly published version. Blocked until<br>it ages past the quarantine window. |

## Supported formats summary

| Format | Where to read publish timestamp           | Key field                | Status    |
| ------ | ----------------------------------------- | ------------------------ | --------- |
| npm    | Packument response (`GET /<package>`)     | `time["<version>"]`      | Available |
| Maven  | HTTP response header on artifact download | `Last-Modified`          | Available |
| NuGet  | V3 registration index                     | `catalogEntry.published` | Available |
| Cargo  | V1 API versions response                  | `created_at`             | Available |
| PyPI   | PEP 691 JSON Simple API                   | `upload-time`            | Available |
