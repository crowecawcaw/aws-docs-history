# Plugin API reference

Complete API reference for inspector-sbomgen Lua plugins. For a guide on writing plugins, see [Plugin developer guide](sbomgen-plugin-developer-guide.md "sbomgen-plugin-developer-guide.md"). For testing, see [Plugin testing guide](sbomgen-plugin-testing-guide.md "sbomgen-plugin-testing-guide.md").

## Overview

All runtime-provided functions are accessed through the global `sbomgen` table (file I/O, regex, logging, constants, etc.). In addition, each plugin defines a small set of top-level global functions (`discover`, `collect`, `get_scanner_name`, `subscribe_to_event`, and so on) that sbomgen calls at defined points in the plugin lifecycle. These are documented in [Plugin Lifecycle Globals](#sbomgen-plugin-api-reference-plugin-lifecycle-globals "#sbomgen-plugin-api-reference-plugin-lifecycle-globals").

Inside `*_test.lua` files, sbomgen additionally exposes a `testing` global that lets test authors drive the discovery→collection pipeline and make assertions. See [Testing API](#sbomgen-plugin-api-reference-testing-api "#sbomgen-plugin-api-reference-testing-api").

### Sandbox Restrictions

Plugins run in a sandboxed Lua VM with restricted standard library access. The following Lua standard library modules are **available**:

| **Module** | **Notes**                                                                                                                                                                                                  |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `base`     | Core functions (`print`, `type`, `tostring`, `tonumber`, `pairs`, `ipairs`, `pcall`, `error`, `select`, `unpack`, `rawget`, `rawset`, etc.). `dofile`, `loadfile`, and `loadstring` are **removed**.       |
| `string`   | Full string manipulation (`string.match`, `string.find`, `string.format`, `string.gsub`, etc.)                                                                                                             |
| `table`    | Full table manipulation (`table.insert`, `table.remove`, `table.sort`, `table.concat`, etc.)                                                                                                               |
| `math`     | Full math library (`math.floor`, `math.max`, `math.min`, etc.)                                                                                                                                             |
| `package`  | `require()` is available but restricted to modules within the plugin's own directory tree. Parent-directory traversal (`require("../shared")`) is blocked. `package.cpath` and `package.path` are cleared. |

The following standard library modules are **explicitly disallowed** for security and stability:

| **Module**  | **Reason**                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `io`        | Direct filesystem access is blocked. All file operations must go through `sbomgen.*` functions, which route through the artifact interface for consistent behavior across artifact types (directory, container, volume, etc.) and confine reads to the artifact under inventory (see [File access boundary](#sbomgen-plugin-api-reference-file-access-boundary "#sbomgen-plugin-api-reference-file-access-boundary")). |
| `os`        | System-level operations (`os.execute`, `os.remove`, `os.rename`, `os.getenv`, etc.) are blocked to prevent plugins from modifying the host system.                                                                                                                                                                                                                                                                     |
| `debug`     | The debug library is blocked to prevent inspection or modification of the Lua VM internals.                                                                                                                                                                                                                                                                                                                            |
| `coroutine` | Coroutines are not loaded.                                                                                                                                                                                                                                                                                                                                                                                             |

These modules are not in the VM's allowlist and cannot be accessed by plugins.

###### Note

**Important:** All file I/O must go through `sbomgen.*` functions (e.g., `sbomgen.read_file`, `sbomgen.open_file`, `sbomgen.get_file_list`). Using `io.open` or any direct filesystem access will raise a runtime error. The `sbomgen` API ensures plugins interact with the artifact abstraction layer, which provides consistent behavior whether scanning a directory, container image, archive, or volume.

## Plugin Lifecycle Globals

A plugin is a Lua file named `init.lua` that defines certain top-level global functions. These globals are **not** on the `sbomgen` table — they are functions the plugin defines for sbomgen to call. The set of valid globals differs between discovery plugins and collection plugins. For every function below, if the plugin omits it, the default shown in the table is used.

### Discovery plugins

| **Function**                 | **Arity** | **Required** | **Default (when omitted)**                                    | **Description**                                                                                                                                                                                    |
| ---------------------------- | --------- | ------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `discover()`                 | 0         | **Yes**      | —                                                             | Returns the files this plugin has found. Return a sequential table of path strings (single-event mode) or a table keyed by event-name strings whose values are tables of paths (multi-event mode). |
| `get_event_name()`           | 0         | No           | `"lua:{platform}/{category}/{ecosystem}"`                     | Returns the event name under which files are published. Must be unique across all discovery plugins.                                                                                               |
| `get_scanner_name()`         | 0         | No           | ecosystem directory name                                      | Returns the scanner's display name. Must be unique across all discovery plugins.                                                                                                                   |
| `get_scanner_description()`  | 0         | No           | `"Lua discovery plugin: {ecosystem}"`                         | Returns a human-readable description.                                                                                                                                                              |
| `get_scanner_groups()`       | 0         | No           | Derived from the category directory (see the developer guide) | Returns a table of scanner group strings. Use `sbomgen.groups.*` constants.                                                                                                                        |
| `get_localhost_scan_paths()` | 0         | No           | —                                                             | Returns a table of file/directory paths to include when scanning a localhost artifact. Only consulted for `localhost` scans.                                                                       |

### Collection plugins

| **Function**                  | **Arity** | **Required** | **Default (when omitted)**                | **Description**                                                                                                                         |
| ----------------------------- | --------- | ------------ | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `collect(file_path)`          | 1         | **Yes**      | —                                         | Called once per file published to the subscribed event. Parse the file and emit findings via `sbomgen.push_package()`. Returns nothing. |
| `subscribe_to_event()`        | 0         | No           | `"lua:{platform}/{category}/{ecosystem}"` | Returns the event name this collector subscribes to. Should match the corresponding discovery plugin's `get_event_name()`.              |
| `get_collector_name()`        | 0         | No           | ecosystem directory name                  | Returns the collector's display name. Must be unique across all collection plugins.                                                     |
| `get_collector_description()` | 0         | No           | `""` (empty)                              | Returns a human-readable description.                                                                                                   |

## File I/O

All file operations must go through the `sbomgen.*` API. Direct filesystem access via Lua's `io` library is not available (see [Sandbox Restrictions](#sbomgen-plugin-api-reference-sandbox-restrictions "#sbomgen-plugin-api-reference-sandbox-restrictions")). The `sbomgen` file I/O functions route through the artifact interface, ensuring your plugin works identically whether scanning a directory on disk, a container image, a compressed archive, or a mounted volume.

### File access boundary

The `sbomgen.*` file functions confine reads to the artifact under inventory. A path that resolves outside the artifact root — for example via `../` traversal — is rejected, and the call returns an error rather than reading the host filesystem. This applies to `read_file`, `open_file`, `read_dir`, `file_stat`, and the binary/hash helpers that take a path.

The exception is the `localhost` artifact type, which inventories the host itself; there the host filesystem is the artifact, so reads are not confined to a narrower root.

This boundary governs file _reads_ only. It does not constrain what a plugin writes into the SBOM — see [SBOM contents are not sanitized](#sbomgen-plugin-api-reference-sbom-contents-not-sanitized "#sbomgen-plugin-api-reference-sbom-contents-not-sanitized").

### `sbomgen.get_file_list()`

Returns all file paths in the artifact as a table of strings.

- **Returns:** `{string, ...}` — table of absolute file path strings
- **Performance:** This function copies every file path in the artifact into the Lua VM as a Lua string. On large artifacts (e.g., a localhost scan with 300K+ files), this alone takes several seconds. Iterating the returned table in Lua with `string.match()` adds further overhead — a full scan can take 15+ seconds. **The more files in the artifact, the slower your plugin will be.**

###### Note

**Prefer these targeted alternatives whenever possible:**

| **Function**                         | **Use when...**                                                                |
| ------------------------------------ | ------------------------------------------------------------------------------ |
| `sbomgen.find_files_by_name()`       | You know the exact filename(s) to match (e.g., `"requirements.txt"`, `"curl"`) |
| `sbomgen.find_files_by_name_icase()` | Same as above, but case-insensitive                                            |
| `sbomgen.find_files_by_suffix()`     | You need to match path suffixes (e.g., `"/pom.properties"`, `"curlver.h"`)     |
| `sbomgen.find_files_by_path_regex()` | You need full-path regex matching                                              |
| `sbomgen.glob_find_files()`          | You need glob-style basename matching                                          |

These functions perform matching outside the Lua VM and return only the matched paths, completing in under 1 millisecond even on 300K-file artifacts. Use `get_file_list()` only when your matching logic cannot be expressed with any of the above.

The `find_files_by_*` and `glob_find_files` helpers skip symlinks, returning only concrete files, so a symlink alias and its target are not both inventoried. `get_file_list()` returns every entry, including symlinks.

```
-- AVOID in discovery plugins when possible:
local files = sbomgen.get_file_list()
for _, f in ipairs(files) do
    if string.match(f, "pattern$") then ... end
end

-- PREFER:
local matches = sbomgen.find_files_by_name({"target-file.txt"})
```

### `sbomgen.read_file(path)`

Reads the entire contents of a file and returns it as a string.

- **Returns:** `string, err`
- On failure: `nil, error_string`

```
local content, err = sbomgen.read_file("/app/package.json")
if err then
    sbomgen.log_error("read failed: " .. err)
    return
end
```

### `sbomgen.open_file(path)`

Opens a file for streaming reads. Returns a FileHandle object. Use this for large files where loading the entire content into memory is impractical.

- **Returns:** `FileHandle, err`

```
local fh, err = sbomgen.open_file(path)
if err then return end
local line = fh:read_line()
while line do
    -- process line
    line = fh:read_line()
end
fh:close()
```

### `sbomgen.glob_find_files(pattern)`

Returns files matching a Go `filepath.Match` glob pattern. The pattern is matched against the base filename. Symlinks are skipped; only concrete files are returned.

- **Returns:** `{string, ...}, err`

```
local files, err = sbomgen.glob_find_files("*.txt")
```

Use `sbomgen.get_file_list()` with `string.match` for full path pattern matching.

### `sbomgen.find_files_by_name(names)`

Returns files whose basename (last path component) exactly matches one of the given names. The iteration and comparison happen in Go, making this significantly faster than iterating `sbomgen.get_file_list()` in Lua.

- **Parameters:** `names` — table of strings (basenames to match)
- **Returns:** `{string, ...}` — matching file paths, excluding symlinks (no error tuple)

```
local curl_bins = sbomgen.find_files_by_name({"curl", "curl.exe"})
local headers = sbomgen.find_files_by_name({"curlver.h"})
```

### `sbomgen.find_files_by_name_icase(names)`

Returns files whose basename matches one of the given names, ignoring case. For example, `"version"` matches `VERSION`, `Version`, and `version`. Like `find_files_by_name`, matching happens outside the Lua VM.

- **Parameters:** `names` — table of strings (basenames to match, case-insensitive)
- **Returns:** `{string, ...}` — matching file paths, excluding symlinks (no error tuple)

```
local version_files = sbomgen.find_files_by_name_icase({"version"})
local war_files = sbomgen.find_files_by_name_icase({"jenkins.war"})
```

### `sbomgen.find_files_by_suffix(suffixes)`

Returns files whose full (forward-slash-normalized) path ends with one of the given suffixes. Like `find_files_by_name`, matching happens outside the Lua VM.

- **Parameters:** `suffixes` — table of strings (path suffixes to match)
- **Returns:** `{string, ...}` — matching file paths, excluding symlinks (no error tuple)

```
local pom_files = sbomgen.find_files_by_suffix({"/pom.properties"})
local release_headers = sbomgen.find_files_by_suffix({"ap_release.h", "opensslv.h"})
```

### `sbomgen.find_files_by_path_regex(patterns)`

Returns files whose forward-slash-normalized path matches any of the given Go (RE2) regex patterns. Matching happens outside the Lua VM, which makes this efficient on large file lists.

- **Parameters:** `patterns` — table of Go regex strings
- **Returns:** `{string, ...}` — matching file paths, excluding symlinks (no error tuple)
- **Raises:** a Lua error if any pattern fails to compile

```
local configs = sbomgen.find_files_by_path_regex({"/etc/.*\\.conf$", "/opt/.*/config\\.json$"})
```

### Performance: `find_files_by_*` vs `get_file_list`

For discovery plugins, prefer `find_files_by_name`, `find_files_by_suffix`, or `find_files_by_path_regex` over iterating `get_file_list()` in Lua. On a localhost scan with 300K files, iterating the file list in Lua with `string.match()` takes ~15 seconds, while `find_files_by_name` completes in under 1 millisecond. The difference is that `get_file_list()` copies every file path into the Lua VM as a string, then Lua interprets the loop and pattern match for each one. The `find_files_by_*` functions perform the matching outside the Lua VM and return only the matched paths, avoiding both the copy and the per-path interpretation overhead.

Use `get_file_list()` only when you need custom matching logic that cannot be expressed as a basename, suffix, or regex match.

### `sbomgen.read_dir(path)`

Lists entries in a directory.

- **Returns:** `{{name, is_dir}, ...}, err`

```
local entries, err = sbomgen.read_dir("/app/node_modules")
if err then return end
for _, e in ipairs(entries) do
    if e.is_dir then
        sbomgen.log_debug("directory: " .. e.name)
    end
end
```

### `sbomgen.file_stat(path)`

Returns metadata about a file.

- **Returns:** `{is_regular, is_dir, size}, err`

```
local info, err = sbomgen.file_stat(path)
if err then return end
if info.is_regular and info.size > 0 then
    -- process file
end
```

### `sbomgen.read_zip_entry(path, entry_path)`

Reads a single entry from a ZIP, JAR, or WAR archive.

- **Returns:** `string, err`

```
local manifest, err = sbomgen.read_zip_entry(
    "/app/lib/example.jar",
    "META-INF/MANIFEST.MF"
)
```

### `sbomgen.search_binary(path, regex)`

Parses a file as an ELF, PE, or Mach-O binary and searches the default constant/variable section for a Go regex match.

- **Returns:** `string|nil, err` — the matched string, or nil if no match

```
local version, err = sbomgen.search_binary(path, "Version:\\s+([\\d.]+)")
if version then
    sbomgen.log_info("found version: " .. version)
end
```

### `sbomgen.search_binary_all(path, regex [, n])`

Parses a file as an ELF, PE, or Mach-O binary and returns all unique first capture group matches from the default constant/variable section. Pass `n` to limit results.

- **Returns:** `{string, ...}|nil, err` — table of matched strings, or nil if no matches

```
local versions, err = sbomgen.search_binary_all(path, "version[= ]+([\\d.]+)", 5)
if versions then
    for _, v in ipairs(versions) do
        sbomgen.log_info("found: " .. v)
    end
end
```

### `sbomgen.search_binary_raw(path, regex)`

Searches the entire binary file for the first regex match, not limited to a specific section. Use when section-based search (`search_binary`) is insufficient — for example, when version strings are in non-standard sections.

- **Returns:** `string|nil, err` — the matched string, or nil if no match

```
local version, err = sbomgen.search_binary_raw(path, "ProductVersion[\\x00\\s]+([\\d.]+)")
```

## FileHandle Methods

FileHandle objects are returned by `sbomgen.open_file()`.

### `fh:read_line()`

Reads the next line (without the newline character). Returns `nil` at EOF.

- **Returns:** `string|nil, err`

### `fh:read(n)`

Reads up to `n` bytes. Returns `nil` at EOF.

- **Returns:** `string|nil, err`

### `fh:close()`

Closes the file handle. Always close handles when done.

## Binary Utilities

### `sbomgen.hash(data, algorithm)`

Returns the hex-encoded digest of an in-memory byte string under the given algorithm. Pair with `sbomgen.read_file(path)` to hash a file you've already read for parsing — preferred over `sbomgen.hash_file(path)` when you need both the bytes and the digest, since `hash` doesn't re-read the file.

- **Returns:** `string, err`
- **Algorithms:** see [Component Hashes](#sbomgen-plugin-api-reference-component-hashes "#sbomgen-plugin-api-reference-component-hashes") for the list of accepted algorithm constants.

```
local data, err = sbomgen.read_file("/path/to/manifest.json")
if data then
    local sha256 = sbomgen.hash(data, sbomgen.hash_algorithms.SHA256)
    sbomgen.log_info("SHA-256: " .. sha256)
end
```

### `sbomgen.hash_file(path, algorithm)`

Returns the hex-encoded digest of a file's contents under the given algorithm. Routes the read through the artifact I/O layer, so it works uniformly across directory, container, archive, volume, and localhost artifacts. Use this when the digest is the only thing you need from the file.

- **Returns:** `string, err`

```
local sha256, err = sbomgen.hash_file("/app/bin/server", sbomgen.hash_algorithms.SHA256)
if sha256 then
    sbomgen.log_info("SHA-256: " .. sha256)
end
```

### `sbomgen.sha256(path)`

###### Important

**Deprecated.** Use `sbomgen.hash_file(path, sbomgen.hash_algorithms.SHA256)` instead. This alias is retained for backwards compatibility and will continue to work, but it will be removed in a future release. New plugins should call `hash_file` so the algorithm choice is explicit.

Equivalent to `sbomgen.hash_file(path, "SHA-256")`.

- **Returns:** `string, err`

```
local hash, err = sbomgen.sha256("/app/bin/server")
if hash then
    sbomgen.log_info("SHA-256: " .. hash)
end
```

### `sbomgen.contains_bytes(path, patterns)`

Checks whether a file contains each of the given byte patterns. Returns a table of booleans in the same order as the input patterns.

- **Returns:** `{bool, ...}, err`

```
local results, err = sbomgen.contains_bytes(path, {
    "\xff Go buildinf:",   -- Go build identifier
    "/rustc/",             -- Rust build identifier
})
if results then
    local is_go = results[1]
    local is_rust = results[2]
end
```

### `sbomgen.get_pe_version_info(path)`

Parses Windows PE version resources from a binary file. Returns a table with version fields, or `nil, err` if the file is not a PE binary or has no version resource.

- **Returns:** `{product_version, file_version, string_table}, err`

The `product_version` and `file_version` fields come from the PE `FixedFileInfo` structure, formatted as `"major.minor.build.revision"`. The `string_table` field is a nested table keyed by **locale code** (e.g., `"040904B0"` for US English Unicode). Each locale maps to a table of name/value pairs drawn from the PE `StringFileInfo` (`ProductVersion`, `ProductName`, `FileDescription`, etc.). A PE binary may expose one or more locales.

```
local info, err = sbomgen.get_pe_version_info(file_path)
if err then return end

-- Fixed version fields (always flat)
local product_ver = info.product_version  -- e.g. "25.1.0.0"
local file_ver    = info.file_version     -- e.g. "25.1.0.0"

-- String table — iterate locales, or address a known locale by key
for locale, fields in pairs(info.string_table or {}) do
    sbomgen.log_info(string.format("%s ProductName=%s", locale, fields.ProductName or ""))
end

-- US English Unicode is the most common locale for PE files
local us = (info.string_table or {})["040904B0"]
if us then
    local display_ver = us.ProductVersion  -- e.g. "25.01"
    local name        = us.ProductName     -- e.g. "7-Zip"
end
```

### `sbomgen.parse_product_version(path)`

Convenience wrapper that returns just the product version string from a PE binary's FixedFileInfo. Equivalent to calling `get_pe_version_info(path)` and reading `product_version`.

- **Returns:** `string, err`

```
local version, err = sbomgen.parse_product_version(file_path)
if version then
    sbomgen.log_info("product version: " .. version)
end
```

### `sbomgen.parse_file_version(path)`

Convenience wrapper that returns just the file version string from a PE binary's FixedFileInfo. Equivalent to calling `get_pe_version_info(path)` and reading `file_version`.

- **Returns:** `string, err`

```
local version, err = sbomgen.parse_file_version(file_path)
if version then
    sbomgen.log_info("file version: " .. version)
end
```

## Package Output

### `sbomgen.push_package(pkg)`

Pushes a package finding into the SBOM. Only available in collection plugins.

The `pkg` table supports the following fields:

| **Field**        | **Type** | **Required** | **Description**                                                                                                                                                                         |
| ---------------- | -------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`           | string   | Yes          | Package name                                                                                                                                                                            |
| `version`        | string   | No           | Resolved version string                                                                                                                                                                 |
| `namespace`      | string   | No           | PURL namespace (e.g., `"curl"`, `"wordpress/plugin"`)                                                                                                                                   |
| `purl_type`      | string   | Yes          | PURL type (e.g., `"pypi"`, `"npm"`, `"cargo"`, `"deb"`, `"generic"`)                                                                                                                    |
| `component_type` | string   | Yes          | CycloneDX component type; use `sbomgen.component_types.*` constants (e.g., `sbomgen.component_types.LIBRARY`)                                                                           |
| `qualifiers`     | table    | No           | PURL qualifiers as key-value pairs (appear in the package URL)                                                                                                                          |
| `properties`     | table    | No           | CycloneDX component properties as key-value pairs (see [CycloneDX Properties](#sbomgen-plugin-api-reference-cyclonedx-properties "#sbomgen-plugin-api-reference-cyclonedx-properties")) |
| `hashes`         | table    | No           | Component hashes keyed by algorithm name; see [Component Hashes](#sbomgen-plugin-api-reference-component-hashes "#sbomgen-plugin-api-reference-component-hashes")                       |
| `children`       | table    | No           | Nested child packages, each with the same shape as `pkg` (required fields are validated recursively)                                                                                    |

```
sbomgen.push_package({
    name = "requests",
    version = "2.28.1",
    purl_type = "pypi",
    component_type = sbomgen.component_types.LIBRARY,
    qualifiers = { example_qualifier = "example_qualifier_value" },
    properties = {
        -- Use your own namespace; amazon:inspector:* is reserved for Amazon Inspector.
        ["acme:example:extra_field"] = "example_value",
    },
    hashes = {
        [sbomgen.hash_algorithms.SHA256] = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
    },
})
```

## Component Hashes

The optional `hashes` field on `sbomgen.push_package()` records integrity digests for a component. Entries are keyed by algorithm name and serialized into the CycloneDX `components[].hashes` array, matching the schema Amazon Inspector expects.

### Supported algorithms

Use the constants under `sbomgen.hash_algorithms` so the algorithm name passed to `sbomgen.hash()` / `sbomgen.hash_file()` is the same string accepted by `push_package({ hashes = ... })`:

| **Constant**                     | **Value**   | **Hex digest length** |
| -------------------------------- | ----------- | --------------------- |
| `sbomgen.hash_algorithms.SHA1`   | `"SHA-1"`   | 40                    |
| `sbomgen.hash_algorithms.SHA256` | `"SHA-256"` | 64                    |

### Validation rules

`push_package()` validates `hashes` before emitting a finding. A package whose hashes fail validation is dropped and a warning is logged. Validation:

- Algorithm names must match an entry in `sbomgen.hash_algorithms` (case sensitive, exactly `"SHA-1"` or `"SHA-256"`).
- Values must be non-empty, lower-case hexadecimal digits.
- Values must be the correct length for the algorithm (40 chars for SHA-1, 64 chars for SHA-256).
- Validation is recursive: a malformed hash inside `children[].hashes` rejects the whole package.

### Example: hashing a manifest and attaching the digest

```
function collect(file_path)
    local data, err = sbomgen.read_file(file_path)
    if err then return end

    local sha256 = sbomgen.hash(data, sbomgen.hash_algorithms.SHA256)

    sbomgen.push_package({
        name = "skill-manifest",
        version = "1.0.0",
        purl_type = "generic",
        component_type = sbomgen.component_types.DATA,
        hashes = {
            [sbomgen.hash_algorithms.SHA256] = sha256,
        },
    })
end
```

When the digest is the only thing you need from the file, prefer `sbomgen.hash_file(path, algo)` over reading the file twice — it routes the read through the artifact I/O layer in a single pass.

## CycloneDX Properties

CycloneDX properties are key-value metadata attached to a component in the SBOM. They are distinct from PURL qualifiers:

- **`qualifiers`** — PURL qualifiers. These become part of the package URL string (e.g., `pkg:deb/debian/curl@7.88.1?arch=amd64`). Some PURL qualifiers carry semantic meaning to Amazon Inspector and influence vulnerability identification. See [What is a package URL?](sbom-generator-purl-sbom.md "sbom-generator-purl-sbom.md") for Inspector's per-type conventions.
- **`properties`** — CycloneDX component properties. These appear in the SBOM's `components[].properties` array and do not change how the component is identified.

### Reserved namespaces

The `amazon:inspector:*` family of CycloneDX property namespaces is reserved for Amazon Inspector:

- `amazon:inspector:sbom_generator:*` — used by sbomgen and its built-in scanners.
- `amazon:inspector:sbom_scanner:*` — used by the Amazon Inspector Scan API.

**Plugin-defined properties must not use these namespaces.** Writing into a reserved namespace can shadow or conflict with values Inspector relies on, and the resulting SBOM may be interpreted incorrectly during vulnerability identification. See [Using CycloneDX namespaces with Amazon Inspector](cyclonedx-namespace.md "cyclonedx-namespace.md") for the full list of reserved keys.

### Key naming rules

Property keys passed to `sbomgen.push_package()` are processed as follows:

| **Input key**                               | **Resulting key in SBOM**                                | **Recommended for custom plugins?**                                     |
| ------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------- |
| Contains `:` (e.g., `acme:my_plugin:field`) | Used verbatim                                            | *_Yes_<br>• — place every plugin-defined property in your own namespace |
| No `:` (e.g., `field`)                      | Auto-prefixed to `amazon:inspector:sbom_generator:field` | *_No_<br>• — this writes into a reserved namespace                      |

Always include at least one colon in property keys you define. Use a namespace unique to your organization or plugin (for example `acme:python-pip:*`):

```
properties = {
    -- Custom namespace — safe to use (recommended)
    ["acme:python-pip:manifest_path"] = file_path,
    ["acme:python-pip:pinned"]        = "true",

    -- Fully-qualified key outside amazon:inspector:* — also fine
    ["my:custom:namespace:key"] = "value",

    -- No colon: avoid — ends up as "amazon:inspector:sbom_generator:custom_field"
    -- custom_field = "value",
}
```

### Properties set by sbomgen

Sbomgen may attach properties of its own to every component it emits. These values come from the reserved `amazon:inspector:sbom_generator:*` namespace and should not be produced by plugins. Observed runtime behavior:

- `source_path` is always added by sbomgen.
- `source_file_scanner` and `source_package_collector` are added when `--enable-debug-props` is enabled.

The full taxonomy of reserved keys is maintained in the Amazon Inspector user guide: [Using CycloneDX namespaces with Amazon Inspector](cyclonedx-namespace.md "cyclonedx-namespace.md").

### SBOM contents are not sanitized

Sbomgen does not inspect or filter the data a plugin emits. Component names, versions, PURLs, hashes, and property values are written to the SBOM as provided. Sbomgen does not detect or redact secrets, credentials, tokens, or other sensitive data — if a plugin places such a value into a finding, it appears in the output SBOM and travels wherever that SBOM is published.

You are responsible for what your plugins write. Only emit data derived from the artifact you intend to inventory, and treat the SBOM as a shareable artifact when deciding what to include.

## Property Constants

Built-in property key constants are available via `sbomgen.properties`. Every constant below resolves to a key inside the reserved `amazon:inspector:sbom_generator:*` namespace. These constants exist so that sbomgen's built-in scanners emit consistent property keys. **They are not extension points for custom plugins** — using them in a custom plugin writes into a reserved namespace, which can shadow values Inspector relies on. See [Reserved namespaces](#sbomgen-plugin-api-reference-reserved-namespaces "#sbomgen-plugin-api-reference-reserved-namespaces") above.

Custom plugin authors should define properties under their own namespace (for example `acme:my_plugin:*`) rather than reusing these constants.

| **Constant**                                         | **Resolved Value**                                                   |
| ---------------------------------------------------- | -------------------------------------------------------------------- |
| `sbomgen.properties.NAMESPACE`                       | `amazon:inspector:sbom_generator:`                                   |
| `sbomgen.properties.VENDOR`                          | `amazon:inspector:sbom_generator:vendor`                             |
| `sbomgen.properties.FILE_SIZE_BYTES`                 | `amazon:inspector:sbom_generator:file_size_bytes`                    |
| `sbomgen.properties.KERNEL_COMPONENT`                | `amazon:inspector:sbom_generator:kernel_component`                   |
| `sbomgen.properties.RUNNING_KERNEL`                  | `amazon:inspector:sbom_generator:running_kernel`                     |
| `sbomgen.properties.UNRESOLVED_VERSION`              | `amazon:inspector:sbom_generator:unresolved_version`                 |
| `sbomgen.properties.TRANSITIVE_DEPENDENCY`           | `amazon:inspector:sbom_generator:experimental:transitive_dependency` |
| `sbomgen.properties.GO_REPLACE_DIRECTIVE`            | `amazon:inspector:sbom_generator:replaced_by`                        |
| `sbomgen.properties.DUPLICATE_PACKAGE`               | `amazon:inspector:sbom_generator:is_duplicate_package`               |
| `sbomgen.properties.DUPLICATE_PURL`                  | `amazon:inspector:sbom_generator:duplicate_purl`                     |
| `sbomgen.properties.DOCKERFILE_CHECK`                | `amazon:inspector:sbom_generator:dockerfile_finding`                 |
| `sbomgen.properties.CERTIFICATE_FINDING`             | `amazon:inspector:sbom_generator:certificate_finding`                |
| `sbomgen.properties.CERTIFICATE_SUBJECT_NAME`        | `amazon:inspector:sbom_generator:certificate:subject_name`           |
| `sbomgen.properties.CERTIFICATE_ISSUER_NAME`         | `amazon:inspector:sbom_generator:certificate:issuer_name`            |
| `sbomgen.properties.CERTIFICATE_SIGNATURE_ALGORITHM` | `amazon:inspector:sbom_generator:certificate:signature_algorithm`    |
| `sbomgen.properties.CERTIFICATE_NOT_VALID_BEFORE`    | `amazon:inspector:sbom_generator:certificate:not_valid_before`       |
| `sbomgen.properties.CERTIFICATE_NOT_VALID_AFTER`     | `amazon:inspector:sbom_generator:certificate:not_valid_after`        |
| `sbomgen.properties.WINDOWS_REGISTRY_KEY`            | `amazon:inspector:sbom_generator:registry_key`                       |
| `sbomgen.properties.SUBSCRIPTION_ENABLED`            | `amazon:inspector:sbom_generator:subscription:enabled`               |
| `sbomgen.properties.SUBSCRIPTION_NAME`               | `amazon:inspector:sbom_generator:subscription:name`                  |
| `sbomgen.properties.SUBSCRIPTION_LOCKED_VERSION`     | `amazon:inspector:sbom_generator:subscription:locked_version`        |
| `sbomgen.properties.OPENSSL_FULL_VERSION`            | `amazon:inspector:sbom_generator:openssl:full_version`               |
| `sbomgen.properties.HARDENED_IMAGE_VENDOR`           | `amazon:inspector:sbom_generator:hardened_image:vendor`              |

## Scanner Groups

Discovery plugins must declare their scanner groups via `get_scanner_groups()`. Groups categorize scanners and allow users to selectively enable or disable categories. Constants are available via `sbomgen.groups`:

| **Constant**                          | **Value**                         | **Description**                                                     |
| ------------------------------------- | --------------------------------- | ------------------------------------------------------------------- |
| `sbomgen.groups.OS`                   | `"os"`                            | OS package managers (dpkg, rpm, etc.)                               |
| `sbomgen.groups.PROGRAMMING_LANGUAGE` | `"programming-language-packages"` | Language package managers (pip, npm, maven, etc.)                   |
| `sbomgen.groups.BINARY`               | `"binary"`                        | Compiled binary analysis (Go, Rust)                                 |
| `sbomgen.groups.PACKAGE_COLLECTOR`    | `"pkg-scanner"`                   | General package collection                                          |
| `sbomgen.groups.EXTRA_ECOSYSTEMS`     | `"extra-ecosystems"`              | Additional ecosystems (curl, nginx, etc.)                           |
| `sbomgen.groups.CERTIFICATE`          | `"certificate"`                   | Certificate scanning                                                |
| `sbomgen.groups.CUSTOM`               | `"custom"`                        | Automatically added to all custom plugins loaded via `--plugin-dir` |
| `sbomgen.groups.MACHINE_LEARNING`     | `"machine-learning"`              | Machine learning model detection                                    |

Example:

```
function get_scanner_groups()
    return {sbomgen.groups.PROGRAMMING_LANGUAGE, sbomgen.groups.PACKAGE_COLLECTOR}
end
```

## Component Type Constants

The `component_type` field in `push_package()` must be one of the CycloneDX 1.5 component types. Constants are available via `sbomgen.component_types`:

| **Constant**                                     | **Value**                  |
| ------------------------------------------------ | -------------------------- |
| `sbomgen.component_types.APPLICATION`            | `"application"`            |
| `sbomgen.component_types.FRAMEWORK`              | `"framework"`              |
| `sbomgen.component_types.LIBRARY`                | `"library"`                |
| `sbomgen.component_types.CONTAINER`              | `"container"`              |
| `sbomgen.component_types.PLATFORM`               | `"platform"`               |
| `sbomgen.component_types.OPERATING_SYSTEM`       | `"operating-system"`       |
| `sbomgen.component_types.DEVICE`                 | `"device"`                 |
| `sbomgen.component_types.DEVICE_DRIVER`          | `"device-driver"`          |
| `sbomgen.component_types.FIRMWARE`               | `"firmware"`               |
| `sbomgen.component_types.FILE`                   | `"file"`                   |
| `sbomgen.component_types.MACHINE_LEARNING_MODEL` | `"machine-learning-model"` |
| `sbomgen.component_types.DATA`                   | `"data"`                   |

Example:

```
sbomgen.push_package({
    name = "requests",
    version = "2.28.1",
    purl_type = "pypi",
    component_type = sbomgen.component_types.LIBRARY,
})
```

## Hash Algorithm Constants

Constants for the algorithm parameter of `sbomgen.hash()`, `sbomgen.hash_file()`, and the `hashes` field of `sbomgen.push_package()`. The string values match the CycloneDX hash algorithm names so the same constant flows through the entire hashing path without translation.

| **Constant**                     | **Value**   |
| -------------------------------- | ----------- |
| `sbomgen.hash_algorithms.SHA1`   | `"SHA-1"`   |
| `sbomgen.hash_algorithms.SHA256` | `"SHA-256"` |

Example:

```
local digest = sbomgen.hash_file(path, sbomgen.hash_algorithms.SHA256)
sbomgen.push_package({
    name = "example",
    purl_type = "generic",
    component_type = sbomgen.component_types.LIBRARY,
    hashes = { [sbomgen.hash_algorithms.SHA256] = digest },
})
```

## Platform Constants

Constants for comparing against `sbomgen.get_platform()`. Available via `sbomgen.platform`:

| **Constant**               | **Value**   |
| -------------------------- | ----------- |
| `sbomgen.platform.LINUX`   | `"linux"`   |
| `sbomgen.platform.WINDOWS` | `"windows"` |
| `sbomgen.platform.DARWIN`  | `"darwin"`  |

Example:

```
if sbomgen.get_platform() == sbomgen.platform.WINDOWS then
    -- Windows-specific logic
end
```

## Artifact Info

### `sbomgen.get_platform()`

Returns the runtime platform string (e.g., `"linux"`, `"windows"`, `"darwin"`).

### `sbomgen.get_artifact_type()`

Returns the type of artifact being scanned (e.g., `"directory"`, `"archive"`).

### `sbomgen.should_collect_licenses()`

Returns `true` if the user enabled license collection via `--collect-licenses`.

### `sbomgen.get_env_vars()`

Returns environment variables from the artifact as a table of `{key, value}` entries.

```
local env_vars = sbomgen.get_env_vars()
for _, env in ipairs(env_vars) do
    if env.key == "NODE_ENV" then
        sbomgen.log_info("Node environment: " .. env.value)
    end
end
```

### `sbomgen.get_system_drive()`

Returns the system drive letter (e.g., `"C:"`) from the artifact's environment. Reads the `SystemDrive` environment variable, defaulting to `"C:"` if not set. This is the Lua equivalent of `strutils.GetSystemDriverLetter()`.

```
local drive = sbomgen.get_system_drive()
local program_files = drive .. "/Program Files/"
```

### `sbomgen.resolve_glob_paths(patterns)`

Expands filesystem glob patterns against the host filesystem. Localhost-only: returns `nil` plus an error on other artifact types.

```
function get_localhost_scan_paths()
    return sbomgen.resolve_glob_paths({
        "/home/*/.cache/huggingface/hub",
        "/Users/*/.cache/huggingface/hub",
        "C:/Users/*/.cache/huggingface/hub",
    })
end
```

**Behavior:**

- Pattern syntax follows Go's [`filepath.Match`](https://pkg.go.dev/path/filepath#Match "https://pkg.go.dev/path/filepath#Match"): `*`, `?`, `[abc]`, `[a-z]`.
- Input patterns and output paths are normalized: redundant separators (`a//b`), dot segments (`a/./b`), and trailing separators (`a/b/`) are collapsed.
- Output is deduplicated; the first occurrence of a path wins. Input pattern order is preserved across the result.
- Patterns that match nothing return no entries. Empty-string patterns are silently skipped. Malformed patterns (e.g. mismatched brackets) emit a warning and are skipped.

**Cross-platform path separators:**

- **Use forward slashes (`/`) for all paths.** Forward slashes work on Linux, macOS, and Windows; Go's filepath logic translates them to the native separator on Windows.
- **Backslash separators only work on Windows.** On Linux and macOS, `\` is a literal filename character, not a path separator — a pattern like `"C:\\Users\\*"` matches nothing on POSIX systems.
- **Avoid literal Windows-style paths in Lua strings.** A Lua string like `"C:\Users"` is interpreted as `C:<form-feed>sers` because `\U` is not a valid Lua escape (and `\f`, `\n`, `\t` etc. are), so the pattern silently fails. Either use forward slashes, escaped backslashes (`"C:\\Users"`), or a long-bracket raw string (`[[C:\Users]]`).

## System Info

These functions return metadata about the artifact's operating system and hardware. Values may be empty strings if the information is not available (e.g., when scanning a directory without OS metadata).

| **Function**                   | **Returns**                                      |
| ------------------------------ | ------------------------------------------------ |
| `sbomgen.get_os_name()`        | OS name (e.g., `"Ubuntu"`, `"Alpine Linux"`)     |
| `sbomgen.get_os_version()`     | OS version (e.g., `"22.04"`, `"3.18"`)           |
| `sbomgen.get_os_codename()`    | OS codename (e.g., `"jammy"`, `"bookworm"`)      |
| `sbomgen.get_os_id()`          | OS identifier (e.g., `"ubuntu"`, `"alpine"`)     |
| `sbomgen.get_kernel_name()`    | Kernel name (e.g., `"Linux"`)                    |
| `sbomgen.get_kernel_version()` | Kernel version string                            |
| `sbomgen.get_cpu_arch()`       | CPU architecture (e.g., `"x86_64"`, `"aarch64"`) |
| `sbomgen.get_hostname()`       | Hostname of the system                           |

## Regular Expressions

Lua's built-in patterns lack features like alternation (`|`), quantifier ranges (`{n,}`), and lookahead. To close this gap, sbomgen exposes Go's `regexp` package directly. These functions use Go regex syntax (RE2), not Lua patterns.

### `sbomgen.regex_find(str, pattern)`

Returns the first match of a Go regex pattern, or `nil` if no match.

- **Returns:** `string|nil, err`

```
local version = sbomgen.regex_find(content, "\\d+\\.\\d+\\.\\d+")
```

### `sbomgen.regex_match(str, pattern)`

Returns capture groups from the first match. Index 1 is the full match, 2+ are capture groups.

- **Returns:** `{string, ...}|nil, err`

```
local groups = sbomgen.regex_match(content, "(MySQL|MariaDB) (\\d+)\\.(\\d+)\\.(\\d+)")
if groups then
    local db_type = groups[2]   -- "MySQL" or "MariaDB"
    local major   = groups[3]
end
```

### `sbomgen.regex_find_all(str, pattern [, n])`

Returns all non-overlapping matches. Pass `n` to limit results (default: all).

- **Returns:** `{string, ...}|nil, err`

```
local versions = sbomgen.regex_find_all(content, "\\d+\\.\\d+\\.\\d+")
```

### `sbomgen.regex_replace(str, pattern, replacement)`

Replaces all matches. The replacement string can use `$1`, `$2`, etc. for capture group references.

- **Returns:** `string, err`

```
local cleaned = sbomgen.regex_replace(raw_version, "(1[6-9]\\d{8,}|buildkitsandbox.*)$", "")
```

### When to use regex vs Lua patterns

Use Lua's built-in `string.match`/`string.find` for simple patterns — they're faster and don't require escaping backslashes. Use `sbomgen.regex_*` when you need:

- Alternation: `(foo|bar)`
- Quantifier ranges: `\d{8,}`
- Complex character classes not expressible in Lua patterns

## Structured Parsing

Sbomgen exposes lightweight helpers for decoding structured text formats directly into Lua tables.

### `sbomgen.json_decode(str)`

Parses a JSON string into a Lua table.

- **Returns:** `table|nil, err`

```
local doc, err = sbomgen.json_decode('{"name":"requests","version":"2.28.1"}')
if err then return end
sbomgen.log_info(doc.name)
```

### `sbomgen.xml_decode(str)`

Parses an XML string into a Lua table.

- **Returns:** `table|nil, err`

XML values use the following shape:

- `_name` — element name
- `_attr` — attribute table, when present
- `_text` — trimmed text content, when present
- numeric indices `1..n` — child elements

```
local doc, err = sbomgen.xml_decode('<package id="Newtonsoft.Json" version="13.0.3" />')
if err then return end
sbomgen.log_info(doc._attr.id)
```

## Windows Registry

These functions provide read-only access to the Windows registry. On non-Windows artifacts, `registry_open_key` returns an error. The registry accessor is initialized lazily on first use and supports both live Windows API access (localhost scans on Windows) and file-based REGF hive parsing (container/volume scans).

### `sbomgen.registry_open_key(path)`

Opens a registry key. Returns a key handle that must be closed with `registry_close`.

- **Returns:** `key, err`

```
local key, err = sbomgen.registry_open_key("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\7-Zip")
if err then return end
-- use key...
sbomgen.registry_close(key)
```

### `sbomgen.registry_get_string(key, value_name)`

Reads a string value from an open registry key.

- **Returns:** `string, err`

```
local version, err = sbomgen.registry_get_string(key, "DisplayVersion")
```

### `sbomgen.registry_get_integer(key, value_name)`

Reads an integer value from an open registry key.

- **Returns:** `number, err`

### `sbomgen.registry_get_strings(key, value_name)`

Reads a multi-string (REG\_MULTI\_SZ) value from an open registry key. Returns a table of strings.

- **Returns:** `{string, ...}, err`

```
local paths, err = sbomgen.registry_get_strings(key, "DependsOnService")
if paths then
    for _, p in ipairs(paths) do
        sbomgen.log_info("depends on: " .. p)
    end
end
```

### `sbomgen.registry_get_subkeys(key)`

Returns all subkey names under an open registry key.

- **Returns:** `{string, ...}, err`

```
local subkeys, err = sbomgen.registry_get_subkeys(key)
for _, name in ipairs(subkeys) do
    local subkey, err = sbomgen.registry_open_key(parent_path .. "\\" .. name)
    -- ...
end
```

### `sbomgen.registry_close(key)`

Closes a registry key handle. Key handles are also closed automatically by the garbage collector, but explicit closing is recommended.

## Logging

Log messages are written to sbomgen's console output. Every message emitted by a plugin is automatically prefixed with the plugin's source label and ecosystem, for example:

```
[custom:python-pip] Parsing requirements.txt
```

`log_info`, `log_warn`, and `log_error` always print. `log_debug` only prints when sbomgen is invoked with `--verbose`.

| **Function**                 | **Level** | **Visible by default?**   |
| ---------------------------- | --------- | ------------------------- |
| `sbomgen.log_debug(message)` | DEBUG     | No — requires `--verbose` |
| `sbomgen.log_info(message)`  | INFO      | Yes                       |
| `sbomgen.log_warn(message)`  | WARN      | Yes                       |
| `sbomgen.log_error(message)` | ERROR     | Yes                       |

Use `string.format` for formatted messages:

```
sbomgen.log_info(string.format("found %d packages in %s", count, file_path))
```

## Debugging Functions

### `sbomgen.breakpoint(message)`

Prints `message` to stderr and blocks execution until the user presses Enter. If `message` is omitted, prints a default message.

Use this as a crude debugger by placing breakpoints at key points in your plugin and running with `--verbose` to see surrounding log output.

```
sbomgen.log_info("state: " .. some_variable)
sbomgen.breakpoint("paused after state dump — press Enter to continue")
```

## Testing API

Functions under the global `testing` table are only available inside plugin test files (`*_test.lua`), loaded by `inspector-sbomgen plugin test`. They are not available at runtime in discovery or collection plugins. The full `sbomgen.*` API is also available inside test files, but `sbomgen.*` functions that require an artifact (for example `sbomgen.read_file()`) only produce meaningful results when called from inside a scan. For a narrative guide, see the [Plugin testing guide](sbomgen-plugin-testing-guide.md "sbomgen-plugin-testing-guide.md").

### Scan functions

Each scan function creates an artifact of the given kind, runs the current plugin's discovery→collection pipeline against it, and returns the resulting findings. The `path` argument is resolved relative to the test file's directory.

| **Function**                   | **Artifact kind**                     |
| ------------------------------ | ------------------------------------- |
| `testing.scan_directory(path)` | Directory                             |
| `testing.scan_archive(path)`   | Directory (alias of `scan_directory`) |
| `testing.scan_localhost(path)` | Localhost                             |
| `testing.scan_binary(path)`    | Binary                                |
| `testing.scan_volume(path)`    | Volume                                |
| `testing.scan_container(path)` | Container                             |

All six return a result table with the shape below.

### Result shape

Each finding table projects only the fields listed below. In particular, `namespace` and `purl_type` are not projected separately — they are incorporated into the full `purl` string.

```
local result = testing.scan_directory("_testdata/example")
-- result.findings                        -- array of finding tables
-- result.findings[i].name                -- string
-- result.findings[i].version             -- string
-- result.findings[i].component_type      -- string
-- result.findings[i].purl                -- string (the full Package URL, or "" if none)
-- result.findings[i].properties          -- table<string, string>
-- result.findings[i].children            -- array of finding tables (same shape, recursive)
```

### Assertions

| **Function**                | **Signature**                                          | **Description**                                                  |
| --------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------- |
| `testing.assert_equals`     | `(expected: any, actual: any, message?: string)`       | Fails if `tostring(expected) ~= tostring(actual)`.               |
| `testing.assert_not_equals` | `(expected: any, actual: any, message?: string)`       | Fails if `tostring(expected) == tostring(actual)`.               |
| `testing.assert_true`       | `(value: any, message?: string)`                       | Fails if `value` is `false` or `nil`.                            |
| `testing.assert_false`      | `(value: any, message?: string)`                       | Fails if `value` is not `false` and not `nil`.                   |
| `testing.assert_nil`        | `(value: any, message?: string)`                       | Fails if `value` is not `nil`.                                   |
| `testing.assert_not_nil`    | `(value: any, message?: string)`                       | Fails if `value` is `nil`.                                       |
| `testing.assert_contains`   | `(haystack: string, needle: string, message?: string)` | Fails if `haystack` does not contain `needle` (substring match). |
| `testing.assert_matches`    | `(str: string, pattern: string, message?: string)`     | Fails if `str` does not match the given **Go (RE2)*<br>• regex.  |
| `testing.assert_length`     | `(tbl: table, expected: integer, message?: string)`    | Fails if `#tbl` does not equal `expected`.                       |

### Control flow

| **Function**   | **Signature**       | **Description**                                                        |
| -------------- | ------------------- | ---------------------------------------------------------------------- |
| `testing.fail` | `(message: string)` | Fails the current test immediately with the given message.             |
| `testing.skip` | `(message: string)` | Skips the current test. The result is reported as skipped, not failed. |

### Test discovery

Any global Lua function whose name starts with `test_` in a file matching `*_test.lua` is treated as a test. The test file must sit next to an `init.lua` at the normal `{phase}/{platform}/{category}/{ecosystem}/` depth. Fixture data goes in `_testdata/` next to the test file — the runner does not descend into `_testdata/` when searching for test files.

## Error Handling

API functions that can fail return two values: `value, err`. On success, `err` is `nil`. On failure, the first value is `nil` and `err` is an error string.

```
local content, err = sbomgen.read_file(path)
if err then
    sbomgen.log_error("failed to read " .. path .. ": " .. err)
    return
end
-- content is safe to use here
```

If a plugin raises an unhandled Lua error, sbomgen logs a warning and continues with the next file or plugin. Other plugins are not affected.
