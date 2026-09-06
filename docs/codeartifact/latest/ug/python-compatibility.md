

# Python compatibility
<a name="python-compatibility"></a>

CodeArtifact supports the PyPI Simple Repository API at `/simple/<project>/`, used by `pip`, `twine`, `uv`, and other Python clients. Clients choose between HTML and JSON responses using the `Accept` request header.

## Simple Repository API support
<a name="python-simple-api-support"></a>

CodeArtifact implements version 1.1 of the PyPI Simple Repository API as defined by [PEP 503](https://peps.python.org/pep-0503/), [PEP 691](https://peps.python.org/pep-0691/), and [PEP 700](https://peps.python.org/pep-0700/).

The following `Accept` header content types are supported on the `/simple/<project>/` endpoint:
+ `application/vnd.pypi.simple.v1+json`: JSON response (PEP 691, PEP 700).
+ `application/vnd.pypi.simple.v1+html`: HTML response (PEP 503).
+ `application/vnd.pypi.simple.latest+json`: resolves to the latest supported JSON version.
+ `application/vnd.pypi.simple.latest+html`: resolves to the latest supported HTML version.
+ `text/html`, `*/*`, or no `Accept` header: HTML response (default for backward compatibility).

If a client specifies an `Accept` header that does not include any of the supported content types, CodeArtifact returns `406 Not Acceptable`.

JSON responses include the PEP 700 fields `versions`, `size`, and `upload-time` along with the PEP 691 fields. HTML responses carry the same per-artifact upload time as a `data-upload-time` attribute on each artifact link.

The `size` and `upload-time` fields may be missing for package versions cached before per-asset metadata capture was enabled. When a client requests such a package through the JSON Simple Repository API, CodeArtifact re-fetches the metadata from the upstream registry and populates the missing fields. No customer action is required, and subsequent requests for the same package version return the complete metadata.

`pip` 23.0 and later and `uv` send the JSON `Accept` header by default, so most clients receive JSON without any extra configuration.

### Example: request JSON for a project
<a name="python-simple-api-example"></a>

The following example uses `curl` to fetch the JSON Simple Repository API response for the `requests` project. Get the repository URL from `aws codeartifact get-repository-endpoint`, and the authorization token from `aws codeartifact get-authorization-token`.

```
curl --header "Accept: application/vnd.pypi.simple.v1+json" \
     --header "Authorization: Bearer $CODEARTIFACT_AUTH_TOKEN" \
     "https://{{my_domain}}-{{111122223333}}.d.codeartifact.{{region}}.amazonaws.com/pypi/{{my_repo}}/simple/requests/"
```

**Note**  
The CodeArtifact PyPI endpoint accepts either HTTP Basic authentication (username `aws`, password set to your authorization token) or Bearer token authentication. The `pip` and `twine` configurations shown elsewhere in this guide use HTTP Basic.

The following example shows a typical JSON response (truncated for brevity). The `versions`, `size`, and `upload-time` fields are from PEP 700; the `hashes`, `requires-python`, and `yanked` fields are from PEP 691.

```
{
  "meta": { "api-version": "1.1" },
  "name": "requests",
  "versions": [ "2.31.0", "2.32.0", "2.32.3" ],
  "files": [
    {
      "filename": "requests-2.32.3-py3-none-any.whl",
      "url": "2.32.3/requests-2.32.3-py3-none-any.whl",
      "hashes": {
        "sha256": "70761cfe03c773ceb22aa2f671b4757976145175cdfca038c02654d061d6dcc6",
        "md5": "df6df19f49fc7ae54ee5ff2dd3d22d2c"
      },
      "requires-python": ">=3.8",
      "size": 64928,
      "upload-time": "2024-05-29T15:37:49.123456Z",
      "yanked": false
    }
  ]
}
```

## Unsupported PyPI APIs
<a name="python-unsupported-apis"></a>

CodeArtifact does not support the following PyPI APIs:
+ The PyPI [XML-RPC API](https://github.com/pypi/warehouse/blob/main/docs/dev/api-reference/xml-rpc.rst).
+ The PyPI Warehouse [JSON API](https://github.com/pypi/warehouse/blob/main/docs/dev/api-reference/json.rst), which provides project-level and release-level JSON endpoints under `/pypi/`. This is a separate API from the PEP 691 JSON variant of the Simple Repository API, which CodeArtifact does support.
+ The project list endpoint `/simple/`. Only the project detail endpoint `/simple/<project>/` is supported.

For more information about the PyPI APIs, see the [Legacy API](https://github.com/pypi/warehouse/blob/main/docs/dev/api-reference/legacy.rst) reference on the Python Packaging Authority's GitHub website.

## pip command support
<a name="pip-command-support"></a>

The following sections summarize the pip commands that are supported, by CodeArtifact repositories, in addition to specific commands that are not supported.

**Topics**
+ [Supported commands that interact with a repository](#supported-pip-commands-that-interact-with-a-repository)
+ [Supported client-side commands](#supported-pip-client-side-commands)

### Supported commands that interact with a repository
<a name="supported-pip-commands-that-interact-with-a-repository"></a>

This section lists `pip` commands where the `pip` client makes one or more requests to the registry it's been configured with. These commands have been verified to function correctly when invoked against a CodeArtifact repository.



| Command | Description | 
| --- | --- | 
|  [install](https://pip.pypa.io/en/stable/reference/pip_install/)  | Install packages. | 
|  [download](https://pip.pypa.io/en/stable/reference/pip_download/)  | Download packages. | 

CodeArtifact does not implement `pip search`. If you have configured `pip` with a CodeArtifact repository, running `pip search` will search and show packages from [PyPI](https://pypi.org/).

### Supported client-side commands
<a name="supported-pip-client-side-commands"></a>

These commands don't require any direct interaction with a repository, so CodeArtifact does not need to do anything to support them.



| Command | Description | 
| --- | --- | 
|  [uninstall](https://pip.pypa.io/en/stable/reference/pip_uninstall/)  | Uninstall packages. | 
|  [freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/)  | Output installed packages in requirements format. | 
|  [list](https://pip.pypa.io/en/stable/reference/pip_list/)  | List installed packages. | 
|  [show](https://pip.pypa.io/en/stable/reference/pip_show/)  | Show information about installed packages. | 
|  [check](https://pip.pypa.io/en/stable/reference/pip_check/)  | Verify installed packages have compatible dependencies. | 
|  [config](https://pip.pypa.io/en/stable/reference/pip_config/)  | Manage local and global configuration. | 
|  [wheel](https://pip.pypa.io/en/stable/reference/pip_wheel/)  | Build wheels from your requirements. | 
|  [hash](https://pip.pypa.io/en/stable/reference/pip_hash/)  | Compute hashes of package archives. | 
|  [completion](https://pip.pypa.io/en/stable/user_guide/#command-completion)  | Helps with command completion. | 
|  [debug](https://pip.pypa.io/en/stable/reference/pip_debug/)  | Show information useful for debugging. | 
| help | Show help for commands. | 