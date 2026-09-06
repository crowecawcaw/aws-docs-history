

# Plugin API reference
<a name="sbomgen-plugin-api-reference"></a>

 Complete API reference for inspector-sbomgen Lua plugins. For a guide on writing plugins, see [Plugin developer guide](sbomgen-plugin-developer-guide.md). For testing, see [Plugin testing guide](sbomgen-plugin-testing-guide.md). 

## Overview
<a name="sbomgen-plugin-api-reference-overview"></a>

 All runtime-provided functions are accessed through the global `sbomgen` table (file I/O, regex, logging, constants, etc.). In addition, each plugin defines a small set of top-level global functions (`discover`, `collect`, `get_scanner_name`, `subscribe_to_event`, and so on) that sbomgen calls at defined points in the plugin lifecycle. These are documented in [Plugin Lifecycle Globals](#sbomgen-plugin-api-reference-plugin-lifecycle-globals). 

 Inside `*_test.lua` files, sbomgen additionally exposes a `testing` global that lets test authors drive the discovery→collection pipeline and make assertions. See [Testing API](#sbomgen-plugin-api-reference-testing-api). 

### Sandbox Restrictions
<a name="sbomgen-plugin-api-reference-sandbox-restrictions"></a>

 Plugins run in a sandboxed Lua VM with restricted standard library access. The following Lua standard library modules are **available**: 


| **Module** | **Notes** | 
| --- | --- | 
| base | Core functions (print, type, tostring, tonumber, pairs, ipairs, pcall, error, select, unpack, rawget, rawset, etc.). dofile, loadfile, and loadstring are removed. | 
| string | Full string manipulation (string.match, string.find, string.format, string.gsub, etc.) | 
| table | Full table manipulation (table.insert, table.remove, table.sort, table.concat, etc.) | 
| math | Full math library (math.floor, math.max, math.min, etc.) | 
| package | require() is available but restricted to modules within the plugin's own directory tree. Parent-directory traversal (require("../shared")) is blocked. package.cpath and package.path are cleared. | 

 The following standard library modules are **explicitly disallowed** for security and stability: 


| **Module** | **Reason** | 
| --- | --- | 
| io | Direct filesystem access is blocked. All file operations must go through sbomgen.\* functions, which route through the artifact interface for consistent behavior across artifact types (directory, container, volume, etc.) and confine reads to the artifact under inventory (see [File access boundary](#sbomgen-plugin-api-reference-file-access-boundary)). | 
| os | System-level operations (os.execute, os.remove, os.rename, os.getenv, etc.) are blocked to prevent plugins from modifying the host system. | 
| debug | The debug library is blocked to prevent inspection or modification of the Lua VM internals. | 
| coroutine | Coroutines are not loaded. | 

 These modules are not in the VM's allowlist and cannot be accessed by plugins. 

**Note**  
**Important:** All file I/O must go through `sbomgen.*` functions (e.g., `sbomgen.read_file`, `sbomgen.open_file`, `sbomgen.get_file_list`). Using `io.open` or any direct filesystem access will raise a runtime error. The `sbomgen` API ensures plugins interact with the artifact abstraction layer, which provides consistent behavior whether scanning a directory, container image, archive, or volume.

## Plugin Lifecycle Globals
<a name="sbomgen-plugin-api-reference-plugin-lifecycle-globals"></a>

 A plugin is a Lua file named `init.lua` that defines certain top-level global functions. These globals are **not** on the `sbomgen` table — they are functions the plugin defines for sbomgen to call. The set of valid globals differs between discovery plugins and collection plugins. For every function below, if the plugin omits it, the default shown in the table is used. 

### Discovery plugins
<a name="sbomgen-plugin-api-reference-discovery-plugins"></a>


| **Function** | **Arity** | **Required** | **Default (when omitted)** | **Description** | 
| --- | --- | --- | --- | --- | 
| discover() | 0 | Yes | — | Returns the files this plugin has found. Return a sequential table of path strings (single-event mode) or a table keyed by event-name strings whose values are tables of paths (multi-event mode). | 
| get\_event\_name() | 0 | No | "lua:{platform}/{category}/{ecosystem}" | Returns the event name under which files are published. Must be unique across all discovery plugins. | 
| get\_scanner\_name() | 0 | No | ecosystem directory name | Returns the scanner's display name. Must be unique across all discovery plugins. | 
| get\_scanner\_description() | 0 | No | "Lua discovery plugin: {ecosystem}" | Returns a human-readable description. | 
| get\_scanner\_groups() | 0 | No | Derived from the category directory (see the developer guide) | Returns a table of scanner group strings. Use sbomgen.groups.\* constants. | 
| get\_localhost\_scan\_paths() | 0 | No | — | Returns a table of file/directory paths to include when scanning a localhost artifact. Only consulted for localhost scans. | 

### Collection plugins
<a name="sbomgen-plugin-api-reference-collection-plugins"></a>


| **Function** | **Arity** | **Required** | **Default (when omitted)** | **Description** | 
| --- | --- | --- | --- | --- | 
| collect(file\_path) | 1 | Yes | — | Called once per file published to the subscribed event. Parse the file and emit findings via sbomgen.push\_package(). Returns nothing. | 
| subscribe\_to\_event() | 0 | No | "lua:{platform}/{category}/{ecosystem}" | Returns the event name this collector subscribes to. Should match the corresponding discovery plugin's get\_event\_name(). | 
| get\_collector\_name() | 0 | No | ecosystem directory name | Returns the collector's display name. Must be unique across all collection plugins. | 
| get\_collector\_description() | 0 | No | "" (empty) | Returns a human-readable description. | 

## File I/O
<a name="sbomgen-plugin-api-reference-file-i-o"></a>

 All file operations must go through the `sbomgen.*` API. Direct filesystem access via Lua's `io` library is not available (see [Sandbox Restrictions](#sbomgen-plugin-api-reference-sandbox-restrictions)). The `sbomgen` file I/O functions route through the artifact interface, ensuring your plugin works identically whether scanning a directory on disk, a container image, a compressed archive, or a mounted volume. 

### File access boundary
<a name="sbomgen-plugin-api-reference-file-access-boundary"></a>

 The `sbomgen.*` file functions confine reads to the artifact under inventory. A path that resolves outside the artifact root — for example via `../` traversal — is rejected, and the call returns an error rather than reading the host filesystem. This applies to `read_file`, `open_file`, `read_dir`, `file_stat`, and the binary/hash helpers that take a path. 

 The exception is the `localhost` artifact type, which inventories the host itself; there the host filesystem is the artifact, so reads are not confined to a narrower root. 

 This boundary governs file *reads* only. It does not constrain what a plugin writes into the SBOM — see [SBOM contents are not sanitized](#sbomgen-plugin-api-reference-sbom-contents-not-sanitized). 

### `sbomgen.get_file_list()`
<a name="sbomgen-plugin-api-reference-sbomgen-get-file-list"></a>

 Returns all file paths in the artifact as a table of strings. 
+ **Returns:** `{string, ...}` — table of absolute file path strings
+ **Performance:** This function copies every file path in the artifact into the Lua VM as a Lua string. On large artifacts (e.g., a localhost scan with 300K\+ files), this alone takes several seconds. Iterating the returned table in Lua with `string.match()` adds further overhead — a full scan can take 15\+ seconds. **The more files in the artifact, the slower your plugin will be.**

**Note**  
**Prefer these targeted alternatives whenever possible:**  


| **Function** | **Use when...** | 
| --- | --- | 
| sbomgen.find\_files\_by\_name() | You know the exact filename(s) to match (e.g., "requirements.txt", "curl") | 
| sbomgen.find\_files\_by\_name\_icase() | Same as above, but case-insensitive | 
| sbomgen.find\_files\_by\_suffix() | You need to match path suffixes (e.g., "/pom.properties", "curlver.h") | 
| sbomgen.find\_files\_by\_path\_regex() | You need full-path regex matching | 
| sbomgen.glob\_find\_files() | You need glob-style basename matching | 
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
<a name="sbomgen-plugin-api-reference-sbomgen-read-file-path"></a>

 Reads the entire contents of a file and returns it as a string. 
+ **Returns:** `string, err`
+ On failure: `nil, error_string`

```
local content, err = sbomgen.read_file("/app/package.json")
if err then
    sbomgen.log_error("read failed: " .. err)
    return
end
```

### `sbomgen.open_file(path)`
<a name="sbomgen-plugin-api-reference-sbomgen-open-file-path"></a>

 Opens a file for streaming reads. Returns a FileHandle object. Use this for large files where loading the entire content into memory is impractical. 
+ **Returns:** `FileHandle, err`

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
<a name="sbomgen-plugin-api-reference-sbomgen-glob-find-files-pattern"></a>

 Returns files matching a Go `filepath.Match` glob pattern. The pattern is matched against the base filename. Symlinks are skipped; only concrete files are returned. 
+ **Returns:** `{string, ...}, err`

```
local files, err = sbomgen.glob_find_files("*.txt")
```

 Use `sbomgen.get_file_list()` with `string.match` for full path pattern matching. 

### `sbomgen.find_files_by_name(names)`
<a name="sbomgen-plugin-api-reference-sbomgen-find-files-by-name-names"></a>

 Returns files whose basename (last path component) exactly matches one of the given names. The iteration and comparison happen in Go, making this significantly faster than iterating `sbomgen.get_file_list()` in Lua. 
+ **Parameters:** `names` — table of strings (basenames to match)
+ **Returns:** `{string, ...}` — matching file paths, excluding symlinks (no error tuple)

```
local curl_bins = sbomgen.find_files_by_name({"curl", "curl.exe"})
local headers = sbomgen.find_files_by_name({"curlver.h"})
```

### `sbomgen.find_files_by_name_icase(names)`
<a name="sbomgen-plugin-api-reference-sbomgen-find-files-by-name-icase-names"></a>

 Returns files whose basename matches one of the given names, ignoring case. For example, `"version"` matches `VERSION`, `Version`, and `version`. Like `find_files_by_name`, matching happens outside the Lua VM. 
+ **Parameters:** `names` — table of strings (basenames to match, case-insensitive)
+ **Returns:** `{string, ...}` — matching file paths, excluding symlinks (no error tuple)

```
local version_files = sbomgen.find_files_by_name_icase({"version"})
local war_files = sbomgen.find_files_by_name_icase({"jenkins.war"})
```

### `sbomgen.find_files_by_suffix(suffixes)`
<a name="sbomgen-plugin-api-reference-sbomgen-find-files-by-suffix-suffixes"></a>

 Returns files whose full (forward-slash-normalized) path ends with one of the given suffixes. Like `find_files_by_name`, matching happens outside the Lua VM. 
+ **Parameters:** `suffixes` — table of strings (path suffixes to match)
+ **Returns:** `{string, ...}` — matching file paths, excluding symlinks (no error tuple)

```
local pom_files = sbomgen.find_files_by_suffix({"/pom.properties"})
local release_headers = sbomgen.find_files_by_suffix({"ap_release.h", "opensslv.h"})
```

### `sbomgen.find_files_by_path_regex(patterns)`
<a name="sbomgen-plugin-api-reference-sbomgen-find-files-by-path-regex-patterns"></a>

 Returns files whose forward-slash-normalized path matches any of the given Go (RE2) regex patterns. Matching happens outside the Lua VM, which makes this efficient on large file lists. 
+ **Parameters:** `patterns` — table of Go regex strings
+ **Returns:** `{string, ...}` — matching file paths, excluding symlinks (no error tuple)
+ **Raises:** a Lua error if any pattern fails to compile

```
local configs = sbomgen.find_files_by_path_regex({"/etc/.*\\.conf$", "/opt/.*/config\\.json$"})
```

### Performance: `find_files_by_*` vs `get_file_list`
<a name="sbomgen-plugin-api-reference-performance-find-files-by-vs-get-file-list"></a>

 For discovery plugins, prefer `find_files_by_name`, `find_files_by_suffix`, or `find_files_by_path_regex` over iterating `get_file_list()` in Lua. On a localhost scan with 300K files, iterating the file list in Lua with `string.match()` takes \~15 seconds, while `find_files_by_name` completes in under 1 millisecond. The difference is that `get_file_list()` copies every file path into the Lua VM as a string, then Lua interprets the loop and pattern match for each one. The `find_files_by_*` functions perform the matching outside the Lua VM and return only the matched paths, avoiding both the copy and the per-path interpretation overhead. 

 Use `get_file_list()` only when you need custom matching logic that cannot be expressed as a basename, suffix, or regex match. 

### `sbomgen.read_dir(path)`
<a name="sbomgen-plugin-api-reference-sbomgen-read-dir-path"></a>

 Lists entries in a directory. 
+ **Returns:** `{{name, is_dir}, ...}, err`

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
<a name="sbomgen-plugin-api-reference-sbomgen-file-stat-path"></a>

 Returns metadata about a file. 
+ **Returns:** `{is_regular, is_dir, size}, err`

```
local info, err = sbomgen.file_stat(path)
if err then return end
if info.is_regular and info.size > 0 then
    -- process file
end
```

### `sbomgen.read_zip_entry(path, entry_path)`
<a name="sbomgen-plugin-api-reference-sbomgen-read-zip-entry-path-entry-path"></a>

 Reads a single entry from a ZIP, JAR, or WAR archive. 
+ **Returns:** `string, err`

```
local manifest, err = sbomgen.read_zip_entry(
    "/app/lib/example.jar",
    "META-INF/MANIFEST.MF"
)
```

### `sbomgen.search_binary(path, regex)`
<a name="sbomgen-plugin-api-reference-sbomgen-search-binary-path-regex"></a>

 Parses a file as an ELF, PE, or Mach-O binary and searches the default constant/variable section for a Go regex match. 
+ **Returns:** `string|nil, err` — the matched string, or nil if no match

```
local version, err = sbomgen.search_binary(path, "Version:\\s+([\\d.]+)")
if version then
    sbomgen.log_info("found version: " .. version)
end
```

### `sbomgen.search_binary_all(path, regex [, n])`
<a name="sbomgen-plugin-api-reference-sbomgen-search-binary-all-path-regex-n"></a>

 Parses a file as an ELF, PE, or Mach-O binary and returns all unique first capture group matches from the default constant/variable section. Pass `n` to limit results. 
+ **Returns:** `{string, ...}|nil, err` — table of matched strings, or nil if no matches

```
local versions, err = sbomgen.search_binary_all(path, "version[= ]+([\\d.]+)", 5)
if versions then
    for _, v in ipairs(versions) do
        sbomgen.log_info("found: " .. v)
    end
end
```

### `sbomgen.search_binary_raw(path, regex)`
<a name="sbomgen-plugin-api-reference-sbomgen-search-binary-raw-path-regex"></a>

 Searches the entire binary file for the first regex match, not limited to a specific section. Use when section-based search (`search_binary`) is insufficient — for example, when version strings are in non-standard sections. 
+ **Returns:** `string|nil, err` — the matched string, or nil if no match

```
local version, err = sbomgen.search_binary_raw(path, "ProductVersion[\\x00\\s]+([\\d.]+)")
```

## FileHandle Methods
<a name="sbomgen-plugin-api-reference-filehandle-methods"></a>

 FileHandle objects are returned by `sbomgen.open_file()`. 

### `fh:read_line()`
<a name="sbomgen-plugin-api-reference-fh-read-line"></a>

 Reads the next line (without the newline character). Returns `nil` at EOF. 
+ **Returns:** `string|nil, err`

### `fh:read(n)`
<a name="sbomgen-plugin-api-reference-fh-read-n"></a>

 Reads up to `n` bytes. Returns `nil` at EOF. 
+ **Returns:** `string|nil, err`

### `fh:close()`
<a name="sbomgen-plugin-api-reference-fh-close"></a>

 Closes the file handle. Always close handles when done. 

## Binary Utilities
<a name="sbomgen-plugin-api-reference-binary-utilities"></a>

### `sbomgen.hash(data, algorithm)`
<a name="sbomgen-plugin-api-reference-sbomgen-hash-data-algorithm"></a>

 Returns the hex-encoded digest of an in-memory byte string under the given algorithm. Pair with `sbomgen.read_file(path)` to hash a file you've already read for parsing — preferred over `sbomgen.hash_file(path)` when you need both the bytes and the digest, since `hash` doesn't re-read the file. 
+ **Returns:** `string, err`
+ **Algorithms:** see [Component Hashes](#sbomgen-plugin-api-reference-component-hashes) for the list of accepted algorithm constants.

```
local data, err = sbomgen.read_file("/path/to/manifest.json")
if data then
    local sha256 = sbomgen.hash(data, sbomgen.hash_algorithms.SHA256)
    sbomgen.log_info("SHA-256: " .. sha256)
end
```

### `sbomgen.hash_file(path, algorithm)`
<a name="sbomgen-plugin-api-reference-sbomgen-hash-file-path-algorithm"></a>

 Returns the hex-encoded digest of a file's contents under the given algorithm. Routes the read through the artifact I/O layer, so it works uniformly across directory, container, archive, volume, and localhost artifacts. Use this when the digest is the only thing you need from the file. 
+ **Returns:** `string, err`

```
local sha256, err = sbomgen.hash_file("/app/bin/server", sbomgen.hash_algorithms.SHA256)
if sha256 then
    sbomgen.log_info("SHA-256: " .. sha256)
end
```

### `sbomgen.sha256(path)`
<a name="sbomgen-plugin-api-reference-sbomgen-sha256-path"></a>

**Important**  
 **Deprecated.** Use `sbomgen.hash_file(path, sbomgen.hash_algorithms.SHA256)` instead. This alias is retained for backwards compatibility and will continue to work, but it will be removed in a future release. New plugins should call `hash_file` so the algorithm choice is explicit. 

 Equivalent to `sbomgen.hash_file(path, "SHA-256")`. 
+ **Returns:** `string, err`

```
local hash, err = sbomgen.sha256("/app/bin/server")
if hash then
    sbomgen.log_info("SHA-256: " .. hash)
end
```

### `sbomgen.contains_bytes(path, patterns)`
<a name="sbomgen-plugin-api-reference-sbomgen-contains-bytes-path-patterns"></a>

 Checks whether a file contains each of the given byte patterns. Returns a table of booleans in the same order as the input patterns. 
+ **Returns:** `{bool, ...}, err`

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
<a name="sbomgen-plugin-api-reference-sbomgen-get-pe-version-info-path"></a>

 Parses Windows PE version resources from a binary file. Returns a table with version fields, or `nil, err` if the file is not a PE binary or has no version resource. 
+ **Returns:** `{product_version, file_version, string_table}, err`

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
<a name="sbomgen-plugin-api-reference-sbomgen-parse-product-version-path"></a>

 Convenience wrapper that returns just the product version string from a PE binary's FixedFileInfo. Equivalent to calling `get_pe_version_info(path)` and reading `product_version`. 
+ **Returns:** `string, err`

```
local version, err = sbomgen.parse_product_version(file_path)
if version then
    sbomgen.log_info("product version: " .. version)
end
```

### `sbomgen.parse_file_version(path)`
<a name="sbomgen-plugin-api-reference-sbomgen-parse-file-version-path"></a>

 Convenience wrapper that returns just the file version string from a PE binary's FixedFileInfo. Equivalent to calling `get_pe_version_info(path)` and reading `file_version`. 
+ **Returns:** `string, err`

```
local version, err = sbomgen.parse_file_version(file_path)
if version then
    sbomgen.log_info("file version: " .. version)
end
```

## Package Output
<a name="sbomgen-plugin-api-reference-package-output"></a>

### `sbomgen.push_package(pkg)`
<a name="sbomgen-plugin-api-reference-sbomgen-push-package-pkg"></a>

 Pushes a package finding into the SBOM. Only available in collection plugins. 

 The `pkg` table supports the following fields: 


| **Field** | **Type** | **Required** | **Description** | 
| --- | --- | --- | --- | 
| name | string | Yes | Package name | 
| version | string | No | Resolved version string | 
| namespace | string | No | PURL namespace (e.g., "curl", "wordpress/plugin") | 
| purl\_type | string | Yes | PURL type (e.g., "pypi", "npm", "cargo", "deb", "generic") | 
| component\_type | string | Yes | CycloneDX component type; use sbomgen.component\_types.\* constants (e.g., sbomgen.component\_types.LIBRARY) | 
| qualifiers | table | No | PURL qualifiers as key-value pairs (appear in the package URL) | 
| properties | table | No | CycloneDX component properties as key-value pairs (see [CycloneDX Properties](#sbomgen-plugin-api-reference-cyclonedx-properties)) | 
| hashes | table | No | Component hashes keyed by algorithm name; see [Component Hashes](#sbomgen-plugin-api-reference-component-hashes) | 
| children | table | No | Nested child packages, each with the same shape as pkg (required fields are validated recursively) | 

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
<a name="sbomgen-plugin-api-reference-component-hashes"></a>

 The optional `hashes` field on `sbomgen.push_package()` records integrity digests for a component. Entries are keyed by algorithm name and serialized into the CycloneDX `components[].hashes` array, matching the schema Amazon Inspector expects. 

### Supported algorithms
<a name="sbomgen-plugin-api-reference-component-hashes-supported-algorithms"></a>

 Use the constants under `sbomgen.hash_algorithms` so the algorithm name passed to `sbomgen.hash()` / `sbomgen.hash_file()` is the same string accepted by `push_package({ hashes = ... })`: 


| **Constant** | **Value** | **Hex digest length** | 
| --- | --- | --- | 
| sbomgen.hash\_algorithms.SHA1 | "SHA-1" | 40 | 
| sbomgen.hash\_algorithms.SHA256 | "SHA-256" | 64 | 

### Validation rules
<a name="sbomgen-plugin-api-reference-component-hashes-validation-rules"></a>

 `push_package()` validates `hashes` before emitting a finding. A package whose hashes fail validation is dropped and a warning is logged. Validation: 
+ Algorithm names must match an entry in `sbomgen.hash_algorithms` (case sensitive, exactly `"SHA-1"` or `"SHA-256"`).
+ Values must be non-empty, lower-case hexadecimal digits.
+ Values must be the correct length for the algorithm (40 chars for SHA-1, 64 chars for SHA-256).
+ Validation is recursive: a malformed hash inside `children[].hashes` rejects the whole package.

### Example: hashing a manifest and attaching the digest
<a name="sbomgen-plugin-api-reference-component-hashes-example"></a>

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
<a name="sbomgen-plugin-api-reference-cyclonedx-properties"></a>

 CycloneDX properties are key-value metadata attached to a component in the SBOM. They are distinct from PURL qualifiers: 
+ **`qualifiers`** — PURL qualifiers. These become part of the package URL string (e.g., `pkg:deb/debian/curl@7.88.1?arch=amd64`). Some PURL qualifiers carry semantic meaning to Amazon Inspector and influence vulnerability identification. See [What is a package URL?](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-purl-sbom.html) for Inspector's per-type conventions.
+ **`properties`** — CycloneDX component properties. These appear in the SBOM's `components[].properties` array and do not change how the component is identified.

### Reserved namespaces
<a name="sbomgen-plugin-api-reference-reserved-namespaces"></a>

 The `amazon:inspector:*` family of CycloneDX property namespaces is reserved for Amazon Inspector: 
+ `amazon:inspector:sbom_generator:*` — used by sbomgen and its built-in scanners.
+ `amazon:inspector:sbom_scanner:*` — used by the Amazon Inspector Scan API.

 **Plugin-defined properties must not use these namespaces.** Writing into a reserved namespace can shadow or conflict with values Inspector relies on, and the resulting SBOM may be interpreted incorrectly during vulnerability identification. See [Using CycloneDX namespaces with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/cyclonedx-namespace.html) for the full list of reserved keys. 

### Key naming rules
<a name="sbomgen-plugin-api-reference-key-naming-rules"></a>

 Property keys passed to `sbomgen.push_package()` are processed as follows: 


| **Input key** | **Resulting key in SBOM** | **Recommended for custom plugins?** | 
| --- | --- | --- | 
| Contains : (e.g., acme:my\_plugin:field) | Used verbatim | Yes — place every plugin-defined property in your own namespace | 
| No : (e.g., field) | Auto-prefixed to amazon:inspector:sbom\_generator:field | No — this writes into a reserved namespace | 

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
<a name="sbomgen-plugin-api-reference-properties-set-by-sbomgen"></a>

 Sbomgen may attach properties of its own to every component it emits. These values come from the reserved `amazon:inspector:sbom_generator:*` namespace and should not be produced by plugins. Observed runtime behavior: 
+ `source_path` is always added by sbomgen.
+ `source_file_scanner` and `source_package_collector` are added when `--enable-debug-props` is enabled.

 The full taxonomy of reserved keys is maintained in the Amazon Inspector user guide: [Using CycloneDX namespaces with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/cyclonedx-namespace.html). 

### SBOM contents are not sanitized
<a name="sbomgen-plugin-api-reference-sbom-contents-not-sanitized"></a>

 Sbomgen does not inspect or filter the data a plugin emits. Component names, versions, PURLs, hashes, and property values are written to the SBOM as provided. Sbomgen does not detect or redact secrets, credentials, tokens, or other sensitive data — if a plugin places such a value into a finding, it appears in the output SBOM and travels wherever that SBOM is published. 

 You are responsible for what your plugins write. Only emit data derived from the artifact you intend to inventory, and treat the SBOM as a shareable artifact when deciding what to include. 

## Property Constants
<a name="sbomgen-plugin-api-reference-property-constants"></a>

 Built-in property key constants are available via `sbomgen.properties`. Every constant below resolves to a key inside the reserved `amazon:inspector:sbom_generator:*` namespace. These constants exist so that sbomgen's built-in scanners emit consistent property keys. **They are not extension points for custom plugins** — using them in a custom plugin writes into a reserved namespace, which can shadow values Inspector relies on. See [Reserved namespaces](#sbomgen-plugin-api-reference-reserved-namespaces) above. 

 Custom plugin authors should define properties under their own namespace (for example `acme:my_plugin:*`) rather than reusing these constants. 


| **Constant** | **Resolved Value** | 
| --- | --- | 
| sbomgen.properties.NAMESPACE | amazon:inspector:sbom\_generator: | 
| sbomgen.properties.VENDOR | amazon:inspector:sbom\_generator:vendor | 
| sbomgen.properties.FILE\_SIZE\_BYTES | amazon:inspector:sbom\_generator:file\_size\_bytes | 
| sbomgen.properties.KERNEL\_COMPONENT | amazon:inspector:sbom\_generator:kernel\_component | 
| sbomgen.properties.RUNNING\_KERNEL | amazon:inspector:sbom\_generator:running\_kernel | 
| sbomgen.properties.UNRESOLVED\_VERSION | amazon:inspector:sbom\_generator:unresolved\_version | 
| sbomgen.properties.TRANSITIVE\_DEPENDENCY | amazon:inspector:sbom\_generator:experimental:transitive\_dependency | 
| sbomgen.properties.GO\_REPLACE\_DIRECTIVE | amazon:inspector:sbom\_generator:replaced\_by | 
| sbomgen.properties.DUPLICATE\_PACKAGE | amazon:inspector:sbom\_generator:is\_duplicate\_package | 
| sbomgen.properties.DUPLICATE\_PURL | amazon:inspector:sbom\_generator:duplicate\_purl | 
| sbomgen.properties.DOCKERFILE\_CHECK | amazon:inspector:sbom\_generator:dockerfile\_finding | 
| sbomgen.properties.CERTIFICATE\_FINDING | amazon:inspector:sbom\_generator:certificate\_finding | 
| sbomgen.properties.CERTIFICATE\_SUBJECT\_NAME | amazon:inspector:sbom\_generator:certificate:subject\_name | 
| sbomgen.properties.CERTIFICATE\_ISSUER\_NAME | amazon:inspector:sbom\_generator:certificate:issuer\_name | 
| sbomgen.properties.CERTIFICATE\_SIGNATURE\_ALGORITHM | amazon:inspector:sbom\_generator:certificate:signature\_algorithm | 
| sbomgen.properties.CERTIFICATE\_NOT\_VALID\_BEFORE | amazon:inspector:sbom\_generator:certificate:not\_valid\_before | 
| sbomgen.properties.CERTIFICATE\_NOT\_VALID\_AFTER | amazon:inspector:sbom\_generator:certificate:not\_valid\_after | 
| sbomgen.properties.WINDOWS\_REGISTRY\_KEY | amazon:inspector:sbom\_generator:registry\_key | 
| sbomgen.properties.SUBSCRIPTION\_ENABLED | amazon:inspector:sbom\_generator:subscription:enabled | 
| sbomgen.properties.SUBSCRIPTION\_NAME | amazon:inspector:sbom\_generator:subscription:name | 
| sbomgen.properties.SUBSCRIPTION\_LOCKED\_VERSION | amazon:inspector:sbom\_generator:subscription:locked\_version | 
| sbomgen.properties.OPENSSL\_FULL\_VERSION | amazon:inspector:sbom\_generator:openssl:full\_version | 
| sbomgen.properties.HARDENED\_IMAGE\_VENDOR | amazon:inspector:sbom\_generator:hardened\_image:vendor | 

## Scanner Groups
<a name="sbomgen-plugin-api-reference-scanner-groups"></a>

 Discovery plugins must declare their scanner groups via `get_scanner_groups()`. Groups categorize scanners and allow users to selectively enable or disable categories. Constants are available via `sbomgen.groups`: 


| **Constant** | **Value** | **Description** | 
| --- | --- | --- | 
| sbomgen.groups.OS | "os" | OS package managers (dpkg, rpm, etc.) | 
| sbomgen.groups.PROGRAMMING\_LANGUAGE | "programming-language-packages" | Language package managers (pip, npm, maven, etc.) | 
| sbomgen.groups.BINARY | "binary" | Compiled binary analysis (Go, Rust) | 
| sbomgen.groups.PACKAGE\_COLLECTOR | "pkg-scanner" | General package collection | 
| sbomgen.groups.EXTRA\_ECOSYSTEMS | "extra-ecosystems" | Additional ecosystems (curl, nginx, etc.) | 
| sbomgen.groups.CERTIFICATE | "certificate" | Certificate scanning | 
| sbomgen.groups.CUSTOM | "custom" | Automatically added to all custom plugins loaded via --plugin-dir | 
| sbomgen.groups.MACHINE\_LEARNING | "machine-learning" | Machine learning model detection | 

 Example: 

```
function get_scanner_groups()
    return {sbomgen.groups.PROGRAMMING_LANGUAGE, sbomgen.groups.PACKAGE_COLLECTOR}
end
```

## Component Type Constants
<a name="sbomgen-plugin-api-reference-component-type-constants"></a>

 The `component_type` field in `push_package()` must be one of the CycloneDX 1.5 component types. Constants are available via `sbomgen.component_types`: 


| **Constant** | **Value** | 
| --- | --- | 
| sbomgen.component\_types.APPLICATION | "application" | 
| sbomgen.component\_types.FRAMEWORK | "framework" | 
| sbomgen.component\_types.LIBRARY | "library" | 
| sbomgen.component\_types.CONTAINER | "container" | 
| sbomgen.component\_types.PLATFORM | "platform" | 
| sbomgen.component\_types.OPERATING\_SYSTEM | "operating-system" | 
| sbomgen.component\_types.DEVICE | "device" | 
| sbomgen.component\_types.DEVICE\_DRIVER | "device-driver" | 
| sbomgen.component\_types.FIRMWARE | "firmware" | 
| sbomgen.component\_types.FILE | "file" | 
| sbomgen.component\_types.MACHINE\_LEARNING\_MODEL | "machine-learning-model" | 
| sbomgen.component\_types.DATA | "data" | 

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
<a name="sbomgen-plugin-api-reference-hash-algorithm-constants"></a>

 Constants for the algorithm parameter of `sbomgen.hash()`, `sbomgen.hash_file()`, and the `hashes` field of `sbomgen.push_package()`. The string values match the CycloneDX hash algorithm names so the same constant flows through the entire hashing path without translation. 


| **Constant** | **Value** | 
| --- | --- | 
| sbomgen.hash\_algorithms.SHA1 | "SHA-1" | 
| sbomgen.hash\_algorithms.SHA256 | "SHA-256" | 

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
<a name="sbomgen-plugin-api-reference-platform-constants"></a>

 Constants for comparing against `sbomgen.get_platform()`. Available via `sbomgen.platform`: 


| **Constant** | **Value** | 
| --- | --- | 
| sbomgen.platform.LINUX | "linux" | 
| sbomgen.platform.WINDOWS | "windows" | 
| sbomgen.platform.DARWIN | "darwin" | 

 Example: 

```
if sbomgen.get_platform() == sbomgen.platform.WINDOWS then
    -- Windows-specific logic
end
```

## Artifact Info
<a name="sbomgen-plugin-api-reference-artifact-info"></a>

### `sbomgen.get_platform()`
<a name="sbomgen-plugin-api-reference-sbomgen-get-platform"></a>

 Returns the runtime platform string (e.g., `"linux"`, `"windows"`, `"darwin"`). 

### `sbomgen.get_artifact_type()`
<a name="sbomgen-plugin-api-reference-sbomgen-get-artifact-type"></a>

 Returns the type of artifact being scanned (e.g., `"directory"`, `"archive"`). 

### `sbomgen.should_collect_licenses()`
<a name="sbomgen-plugin-api-reference-sbomgen-should-collect-licenses"></a>

 Returns `true` if the user enabled license collection via `--collect-licenses`. 

### `sbomgen.get_env_vars()`
<a name="sbomgen-plugin-api-reference-sbomgen-get-env-vars"></a>

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
<a name="sbomgen-plugin-api-reference-sbomgen-get-system-drive"></a>

 Returns the system drive letter (e.g., `"C:"`) from the artifact's environment. Reads the `SystemDrive` environment variable, defaulting to `"C:"` if not set. This is the Lua equivalent of `strutils.GetSystemDriverLetter()`. 

```
local drive = sbomgen.get_system_drive()
local program_files = drive .. "/Program Files/"
```

### `sbomgen.resolve_glob_paths(patterns)`
<a name="sbomgen-plugin-api-reference-sbomgen-resolve-glob-paths"></a>

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
+ Pattern syntax follows Go's [`filepath.Match`](https://pkg.go.dev/path/filepath#Match): `*`, `?`, `[abc]`, `[a-z]`.
+ Input patterns and output paths are normalized: redundant separators (`a//b`), dot segments (`a/./b`), and trailing separators (`a/b/`) are collapsed.
+ Output is deduplicated; the first occurrence of a path wins. Input pattern order is preserved across the result.
+ Patterns that match nothing return no entries. Empty-string patterns are silently skipped. Malformed patterns (e.g. mismatched brackets) emit a warning and are skipped.

 **Cross-platform path separators:** 
+ **Use forward slashes (`/`) for all paths.** Forward slashes work on Linux, macOS, and Windows; Go's filepath logic translates them to the native separator on Windows.
+ **Backslash separators only work on Windows.** On Linux and macOS, `\` is a literal filename character, not a path separator — a pattern like `"C:\\Users\\*"` matches nothing on POSIX systems.
+ **Avoid literal Windows-style paths in Lua strings.** A Lua string like `"C:\Users"` is interpreted as `C:<form-feed>sers` because `\U` is not a valid Lua escape (and `\f`, `\n`, `\t` etc. are), so the pattern silently fails. Either use forward slashes, escaped backslashes (`"C:\\Users"`), or a long-bracket raw string (`[[C:\Users]]`).

## System Info
<a name="sbomgen-plugin-api-reference-system-info"></a>

 These functions return metadata about the artifact's operating system and hardware. Values may be empty strings if the information is not available (e.g., when scanning a directory without OS metadata). 


| **Function** | **Returns** | 
| --- | --- | 
| sbomgen.get\_os\_name() | OS name (e.g., "Ubuntu", "Alpine Linux") | 
| sbomgen.get\_os\_version() | OS version (e.g., "22.04", "3.18") | 
| sbomgen.get\_os\_codename() | OS codename (e.g., "jammy", "bookworm") | 
| sbomgen.get\_os\_id() | OS identifier (e.g., "ubuntu", "alpine") | 
| sbomgen.get\_kernel\_name() | Kernel name (e.g., "Linux") | 
| sbomgen.get\_kernel\_version() | Kernel version string | 
| sbomgen.get\_cpu\_arch() | CPU architecture (e.g., "x86\_64", "aarch64") | 
| sbomgen.get\_hostname() | Hostname of the system | 

## Regular Expressions
<a name="sbomgen-plugin-api-reference-regular-expressions"></a>

 Lua's built-in patterns lack features like alternation (`|`), quantifier ranges (`{n,}`), and lookahead. To close this gap, sbomgen exposes Go's `regexp` package directly. These functions use Go regex syntax (RE2), not Lua patterns. 

### `sbomgen.regex_find(str, pattern)`
<a name="sbomgen-plugin-api-reference-sbomgen-regex-find-str-pattern"></a>

 Returns the first match of a Go regex pattern, or `nil` if no match. 
+ **Returns:** `string|nil, err`

```
local version = sbomgen.regex_find(content, "\\d+\\.\\d+\\.\\d+")
```

### `sbomgen.regex_match(str, pattern)`
<a name="sbomgen-plugin-api-reference-sbomgen-regex-match-str-pattern"></a>

 Returns capture groups from the first match. Index 1 is the full match, 2\+ are capture groups. 
+ **Returns:** `{string, ...}|nil, err`

```
local groups = sbomgen.regex_match(content, "(MySQL|MariaDB) (\\d+)\\.(\\d+)\\.(\\d+)")
if groups then
    local db_type = groups[2]   -- "MySQL" or "MariaDB"
    local major   = groups[3]
end
```

### `sbomgen.regex_find_all(str, pattern [, n])`
<a name="sbomgen-plugin-api-reference-sbomgen-regex-find-all-str-pattern-n"></a>

 Returns all non-overlapping matches. Pass `n` to limit results (default: all). 
+ **Returns:** `{string, ...}|nil, err`

```
local versions = sbomgen.regex_find_all(content, "\\d+\\.\\d+\\.\\d+")
```

### `sbomgen.regex_replace(str, pattern, replacement)`
<a name="sbomgen-plugin-api-reference-sbomgen-regex-replace-str-pattern-replacement"></a>

 Replaces all matches. The replacement string can use `$1`, `$2`, etc. for capture group references. 
+ **Returns:** `string, err`

```
local cleaned = sbomgen.regex_replace(raw_version, "(1[6-9]\\d{8,}|buildkitsandbox.*)$", "")
```

### When to use regex vs Lua patterns
<a name="sbomgen-plugin-api-reference-when-to-use-regex-vs-lua-patterns"></a>

 Use Lua's built-in `string.match`/`string.find` for simple patterns — they're faster and don't require escaping backslashes. Use `sbomgen.regex_*` when you need: 
+ Alternation: `(foo|bar)`
+ Quantifier ranges: `\d{8,}`
+ Complex character classes not expressible in Lua patterns

## Structured Parsing
<a name="sbomgen-plugin-api-reference-structured-parsing"></a>

 Sbomgen exposes lightweight helpers for decoding structured text formats directly into Lua tables. 

### `sbomgen.json_decode(str)`
<a name="sbomgen-plugin-api-reference-sbomgen-json-decode-str"></a>

 Parses a JSON string into a Lua table. 
+ **Returns:** `table|nil, err`

```
local doc, err = sbomgen.json_decode('{"name":"requests","version":"2.28.1"}')
if err then return end
sbomgen.log_info(doc.name)
```

### `sbomgen.xml_decode(str)`
<a name="sbomgen-plugin-api-reference-sbomgen-xml-decode-str"></a>

 Parses an XML string into a Lua table. 
+ **Returns:** `table|nil, err`

 XML values use the following shape: 
+ `_name` — element name
+ `_attr` — attribute table, when present
+ `_text` — trimmed text content, when present
+ numeric indices `1..n` — child elements

```
local doc, err = sbomgen.xml_decode('<package id="Newtonsoft.Json" version="13.0.3" />')
if err then return end
sbomgen.log_info(doc._attr.id)
```

## Windows Registry
<a name="sbomgen-plugin-api-reference-windows-registry"></a>

 These functions provide read-only access to the Windows registry. On non-Windows artifacts, `registry_open_key` returns an error. The registry accessor is initialized lazily on first use and supports both live Windows API access (localhost scans on Windows) and file-based REGF hive parsing (container/volume scans). 

### `sbomgen.registry_open_key(path)`
<a name="sbomgen-plugin-api-reference-sbomgen-registry-open-key-path"></a>

 Opens a registry key. Returns a key handle that must be closed with `registry_close`. 
+ **Returns:** `key, err`

```
local key, err = sbomgen.registry_open_key("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\7-Zip")
if err then return end
-- use key...
sbomgen.registry_close(key)
```

### `sbomgen.registry_get_string(key, value_name)`
<a name="sbomgen-plugin-api-reference-sbomgen-registry-get-string-key-value-name"></a>

 Reads a string value from an open registry key. 
+ **Returns:** `string, err`

```
local version, err = sbomgen.registry_get_string(key, "DisplayVersion")
```

### `sbomgen.registry_get_integer(key, value_name)`
<a name="sbomgen-plugin-api-reference-sbomgen-registry-get-integer-key-value-name"></a>

 Reads an integer value from an open registry key. 
+ **Returns:** `number, err`

### `sbomgen.registry_get_strings(key, value_name)`
<a name="sbomgen-plugin-api-reference-sbomgen-registry-get-strings-key-value-name"></a>

 Reads a multi-string (REG\_MULTI\_SZ) value from an open registry key. Returns a table of strings. 
+ **Returns:** `{string, ...}, err`

```
local paths, err = sbomgen.registry_get_strings(key, "DependsOnService")
if paths then
    for _, p in ipairs(paths) do
        sbomgen.log_info("depends on: " .. p)
    end
end
```

### `sbomgen.registry_get_subkeys(key)`
<a name="sbomgen-plugin-api-reference-sbomgen-registry-get-subkeys-key"></a>

 Returns all subkey names under an open registry key. 
+ **Returns:** `{string, ...}, err`

```
local subkeys, err = sbomgen.registry_get_subkeys(key)
for _, name in ipairs(subkeys) do
    local subkey, err = sbomgen.registry_open_key(parent_path .. "\\" .. name)
    -- ...
end
```

### `sbomgen.registry_close(key)`
<a name="sbomgen-plugin-api-reference-sbomgen-registry-close-key"></a>

 Closes a registry key handle. Key handles are also closed automatically by the garbage collector, but explicit closing is recommended. 

## Logging
<a name="sbomgen-plugin-api-reference-logging"></a>

 Log messages are written to sbomgen's console output. Every message emitted by a plugin is automatically prefixed with the plugin's source label and ecosystem, for example: 

```
[custom:python-pip] Parsing requirements.txt
```

 `log_info`, `log_warn`, and `log_error` always print. `log_debug` only prints when sbomgen is invoked with `--verbose`. 


| **Function** | **Level** | **Visible by default?** | 
| --- | --- | --- | 
| sbomgen.log\_debug(message) | DEBUG | No — requires --verbose | 
| sbomgen.log\_info(message) | INFO | Yes | 
| sbomgen.log\_warn(message) | WARN | Yes | 
| sbomgen.log\_error(message) | ERROR | Yes | 

 Use `string.format` for formatted messages: 

```
sbomgen.log_info(string.format("found %d packages in %s", count, file_path))
```

## Debugging Functions
<a name="sbomgen-plugin-api-reference-debugging-functions"></a>

### `sbomgen.breakpoint(message)`
<a name="sbomgen-plugin-api-reference-sbomgen-breakpoint-message"></a>

 Prints `message` to stderr and blocks execution until the user presses Enter. If `message` is omitted, prints a default message. 

 Use this as a crude debugger by placing breakpoints at key points in your plugin and running with `--verbose` to see surrounding log output. 

```
sbomgen.log_info("state: " .. some_variable)
sbomgen.breakpoint("paused after state dump — press Enter to continue")
```

## Testing API
<a name="sbomgen-plugin-api-reference-testing-api"></a>

 Functions under the global `testing` table are only available inside plugin test files (`*_test.lua`), loaded by `inspector-sbomgen plugin test`. They are not available at runtime in discovery or collection plugins. The full `sbomgen.*` API is also available inside test files, but `sbomgen.*` functions that require an artifact (for example `sbomgen.read_file()`) only produce meaningful results when called from inside a scan. For a narrative guide, see the [Plugin testing guide](sbomgen-plugin-testing-guide.md). 

### Scan functions
<a name="sbomgen-plugin-api-reference-scan-functions"></a>

 Each scan function creates an artifact of the given kind, runs the current plugin's discovery→collection pipeline against it, and returns the resulting findings. The `path` argument is resolved relative to the test file's directory. 


| **Function** | **Artifact kind** | 
| --- | --- | 
| testing.scan\_directory(path) | Directory | 
| testing.scan\_archive(path) | Directory (alias of scan\_directory) | 
| testing.scan\_localhost(path) | Localhost | 
| testing.scan\_binary(path) | Binary | 
| testing.scan\_volume(path) | Volume | 
| testing.scan\_container(path) | Container | 

 All six return a result table with the shape below. 

### Result shape
<a name="sbomgen-plugin-api-reference-result-shape"></a>

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
<a name="sbomgen-plugin-api-reference-assertions"></a>


| **Function** | **Signature** | **Description** | 
| --- | --- | --- | 
| testing.assert\_equals | (expected: any, actual: any, message?: string) | Fails if tostring(expected) \~= tostring(actual). | 
| testing.assert\_not\_equals | (expected: any, actual: any, message?: string) | Fails if tostring(expected) == tostring(actual). | 
| testing.assert\_true | (value: any, message?: string) | Fails if value is false or nil. | 
| testing.assert\_false | (value: any, message?: string) | Fails if value is not false and not nil. | 
| testing.assert\_nil | (value: any, message?: string) | Fails if value is not nil. | 
| testing.assert\_not\_nil | (value: any, message?: string) | Fails if value is nil. | 
| testing.assert\_contains | (haystack: string, needle: string, message?: string) | Fails if haystack does not contain needle (substring match). | 
| testing.assert\_matches | (str: string, pattern: string, message?: string) | Fails if str does not match the given Go (RE2) regex. | 
| testing.assert\_length | (tbl: table, expected: integer, message?: string) | Fails if \#tbl does not equal expected. | 

### Control flow
<a name="sbomgen-plugin-api-reference-control-flow"></a>


| **Function** | **Signature** | **Description** | 
| --- | --- | --- | 
| testing.fail | (message: string) | Fails the current test immediately with the given message. | 
| testing.skip | (message: string) | Skips the current test. The result is reported as skipped, not failed. | 

### Test discovery
<a name="sbomgen-plugin-api-reference-test-discovery"></a>

 Any global Lua function whose name starts with `test_` in a file matching `*_test.lua` is treated as a test. The test file must sit next to an `init.lua` at the normal `{phase}/{platform}/{category}/{ecosystem}/` depth. Fixture data goes in `_testdata/` next to the test file — the runner does not descend into `_testdata/` when searching for test files. 

## Error Handling
<a name="sbomgen-plugin-api-reference-error-handling"></a>

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