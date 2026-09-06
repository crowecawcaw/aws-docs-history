

# Plugin developer guide
<a name="sbomgen-plugin-developer-guide"></a>

 This guide explains how to extend Amazon Inspector SBOM Generator (inspector-sbomgen) with custom Lua plugins. Plugins let you add support for new package ecosystems without modifying sbomgen's source code or having to re-compile. 

 For the complete function catalog, see the [Plugin API reference](sbomgen-plugin-api-reference.md). For guidance on writing tests, see the [Plugin testing guide](sbomgen-plugin-testing-guide.md). 

## Overview
<a name="sbomgen-plugin-developer-guide-overview"></a>

 Sbomgen plugins are written in Lua, and follow a two step pipeline: 
+ **Discovery** — scan the artifact's file list and report which files are relevant to your ecosystem.
+ **Collection** — parse each discovered file and push package findings into the SBOM.

### Plugin Event Model
<a name="sbomgen-plugin-developer-guide-plugin-event-model"></a>

 Discovery plugins need a way to tell collection plugins that files containing package metadata were discovered in the artifact under inventory. To facilitate this data sharing, discovery plugins define an **event name** and return a list of file paths. Collection plugins **subscribe** to that event and receive each matched file path. This decouples file detection from parsing — you can have one discovery plugin feed multiple collectors (fan-out pattern). However, each discovery plugin must have a unique event name, and each collection plugin must have a unique collector name. See [Plugin Collision Rules](#sbomgen-plugin-developer-guide-plugin-collision-rules) for details. 

 Developers may recognize this as the **observer** design pattern. 

 This design lets a single discovery plugin trigger multiple independent analyses in a performant manner. For example, one discovery plugin can locate every `requirements.txt` in an artifact, then feed: 
+ A **package collector** that parses each line into SBOM findings (`name==version`).
+ A **secrets collector** that flags lines containing API keys or tokens accidentally pinned as versions.
+ A **policy collector** that reports unpinned or wildcard version specifiers.

 Each collector runs independently against the same file list without re-walking the artifact's file system. This also enables plugin authors to add new collection plugins that subscribes to existing events without having to change the corresponding discovery plugin. 

## Quick Start: Creating New Plugins
<a name="sbomgen-plugin-developer-guide-quick-start-creating-new-plugins"></a>

 The fastest way to create a new plugin is using the built-in scaffolding command: 

```
inspector-sbomgen plugin new
```

 The command prompts for a plugin name and project directory. Pressing Enter accepts the default shown in brackets: 

```
Plugin name (identifies the software ecosystem your plugin will inventory, e.g. debian-dpkg, rhel-rpm, python-pip, cmake) [my-custom-ecosystem]: cmake
Project directory [my-sbomgen-plugins]:
```

 You can also pass arguments directly: 

```
inspector-sbomgen plugin new --name cmake --path /tmp/custom-plugins
```

### Starting with a working example
<a name="sbomgen-plugin-developer-guide-starting-with-a-working-example"></a>

 If you want to experiment with plugins before writing your own logic, create a new plugin using the `--with-example` flag: 

```
inspector-sbomgen plugin new --with-example
```

 This generates a fully working plugin project with a sample lockfile parser, test data, and passing tests. The example plugin discovers `example.lock` files, parses `name==version` entries, and pushes packages into the SBOM. You can run the tests immediately to see the plugin system in action, then modify the code to target your actual ecosystem. 

 For advanced scaffolding that includes all optional override functions (`get_scanner_name`, `get_event_name`, `get_scanner_groups`, multi-event discovery, etc.), use the `--with-overrides` flag (more on this later): 

```
inspector-sbomgen plugin new --with-overrides
```

### Completing Your Plugin
<a name="sbomgen-plugin-developer-guide-completing-your-plugin"></a>

 After scaffolding, the generated plugin files contain `TODO` markers indicating where to add your ecosystem-specific logic. Work through these markers to turn the scaffold into a working plugin: 
+ Replace all `TODO` markers with your actual values
+ Update the file pattern in `discover()` to match your target files
+ Implement parsing logic in `collect()` and call `sbomgen.push_package()` for each package

### Test Your Plugin
<a name="sbomgen-plugin-developer-guide-test-your-plugin"></a>

 There are two ways to test your plugins: 

 **1. Built-in test harness** — Use `inspector-sbomgen plugin test` to validate plugin logic during development. This runs your `init_test.lua` test files without needing a real artifact to scan: 

```
inspector-sbomgen plugin test --path ./my-plugins
```

 See the [Plugin testing guide](sbomgen-plugin-testing-guide.md) for details on writing test files and using the `testing.*` API. 

 **2. End-to-end scan** — Invoke your plugin using standard sbomgen commands to verify it works against real artifacts. For this approach, you need to provide both an artifact containing the files your plugin targets (e.g., a directory with `requirements.txt` or equivalent) and the path to your plugin directory: 

```
inspector-sbomgen directory \
    --path /path/to/test/dir \
    --plugin-dir ./my-plugins \
    --disable-native-scanners \
    -o sbom.json
```

 The `--disable-native-scanners` flag ensures only your Lua plugins run, making it easier to test without output from the built-in (native) scanners. 

## IDE Setup
<a name="sbomgen-plugin-developer-guide-ide-setup"></a>

 Sbomgen provides code completion, type checking, and inline documentation for the entire `sbomgen.*` API in VS Code. 

### VS Code with Lua Language Server
<a name="sbomgen-plugin-developer-guide-vs-code-with-lua-language-server"></a>
+ Install the Lua extension: [sumneko.lua](https://marketplace.visualstudio.com/items?itemName=sumneko.lua)
+ Open any `.lua` file in your plugin project

 That's it\! The `plugin new` command generates `.vscode/settings.json` and `library/sbomgen.lua` which are automatically detected by the Lua Language Server. You'll immediately get: 
+ Code completion for all `sbomgen.*` functions
+ Parameter hints with types
+ Hover documentation
+ Type checking

## Plugin Directory Structure
<a name="sbomgen-plugin-developer-guide-plugin-directory-structure"></a>

 Sbomgen discovery and collection plugins must adhere to the following directory structure: 

```
{plugin-dir}/
├── discovery/
│   └── {platform}/
│       └── {category}/
│           └── {ecosystem}/
│               └── init.lua          # REQUIRED entrypoint
└── collection/
    └── {platform}/
        └── {category}/
            └── {ecosystem}/
                └── init.lua          # REQUIRED entrypoint
```

 These directory names carry semantic meaning — sbomgen uses them to derive default metadata for your plugin, including the scanner name, event name, scanner groups, and platform filtering. This reduces the amount of boilerplate developers would otherwise have to write. Choosing the correct values ensures your plugin integrates properly with sbomgen's scanner selection and execution model. 

 The sections below explore the directory structure in greater detail, providing guidance on semantic meaning and conventions. 

### Platform
<a name="sbomgen-plugin-developer-guide-platform"></a>

 The platform directory controls which operating systems your plugin runs on. 


| **Value** | **When to use** | 
| --- | --- | 
| cross-platform | Plugin works on any OS (most plugins) | 
| linux | Linux-specific detection logic | 
| windows | Windows-specific detection logic | 
| macos | macOS-specific detection logic | 

### Category
<a name="sbomgen-plugin-developer-guide-category"></a>

 The category directory determines the default scanner groups assigned to your plugin, which controls whether it runs by default or requires explicit opt-in. See [Scanner Selection](#sbomgen-plugin-developer-guide-scanner-selection) for how groups affect execution. 


| **Value** | **Default groups** | **When to use** | 
| --- | --- | --- | 
| proglang | programming-language-packages, pkg-scanner | Programming language packages (pip, npm, maven, etc.) | 
| os | os, pkg-scanner | OS package managers (dpkg, rpm, apk, etc.) | 
| extra-ecosystems | extra-ecosystems, pkg-scanner | Applications and runtimes (nginx, curl, wordpress, etc.) | 

 If you use a category name that doesn't match any of the above, the category name itself is used as the group. 

### Ecosystem
<a name="sbomgen-plugin-developer-guide-ecosystem"></a>

 A name for the specific package ecosystem (e.g., `python-pip`, `python-poetry`, `debian-dpkg`, `curl`). Hyphenated names are a common convention but not a strict requirement. 

 The scanner name and collector name are derived directly from the ecosystem directory name. 

### Event name pairing
<a name="sbomgen-plugin-developer-guide-event-name-pairing"></a>

 Discovery and collection plugins at the same directory path are automatically paired. For example, a discovery plugin at `discovery/cross-platform/proglang/python-pip/` automatically pairs with `collection/cross-platform/proglang/python-pip/`. 

 You can override this by defining `get_event_name()` and `subscribe_to_event()` in your plugins. 

## Discovery Plugins
<a name="sbomgen-plugin-developer-guide-discovery-plugins"></a>

 A discovery plugin only requires the `discover()` function. All other functions are optional — defaults are derived from the directory path. 

 Most discovery plugins work by locating files whose names or paths identify a specific ecosystem — for example, `requirements.txt` for Python pip, `package.json` for npm, or `Cargo.lock` for Rust cargo. The `sbomgen.find_files_by_*` functions perform this matching outside the Lua VM, which makes them significantly faster than iterating the full file list in Lua: 

```
-- REQUIRED: Scans the artifact and returns a table of file paths.
function discover()
    return sbomgen.find_files_by_name({"requirements.txt"})
end
```

 `discover()` must return a Lua table (array) of strings. If no files are found, return an empty table `{}`. 

### Common discovery patterns
<a name="sbomgen-plugin-developer-guide-common-discovery-patterns"></a>


| **Goal** | **Recommended function** | 
| --- | --- | 
| Match one or more exact filenames | sbomgen.find\_files\_by\_name({names}) | 
| Match filenames case-insensitively | sbomgen.find\_files\_by\_name\_icase({names}) | 
| Match by path suffix (e.g., /pom.properties) | sbomgen.find\_files\_by\_suffix({suffixes}) | 
| Match by full-path regex | sbomgen.find\_files\_by\_path\_regex({patterns}) | 
| Glob-style basename match (e.g., \*.lock) | sbomgen.glob\_find\_files(pattern) | 

 When your logic requires post-filtering — for example, keeping files matching a suffix but excluding build-output directories — combine a `find_files_by_*` call with a Lua loop: 

```
function discover()
    local found = {}
    for _, f in ipairs(sbomgen.find_files_by_suffix({".conda-meta.json"})) do
        if not f:match("[/\\]%.cache[/\\]") then
            table.insert(found, f)
        end
    end
    return found
end
```

 Avoid `sbomgen.get_file_list()` in discovery unless no other matcher fits — it copies every path into the Lua VM and can take several seconds on large artifacts. See the [Plugin API reference](sbomgen-plugin-api-reference.md) for details. 

### Multi-event discovery
<a name="sbomgen-plugin-developer-guide-multi-event-discovery"></a>

 By default, all files returned by `discover()` are published to a single event (from `get_event_name()`). If your scanner needs to route different files to different collectors, return a keyed table instead: 

```
function discover()
    return {
        EventNameFoundCurl = sbomgen.find_files_by_name({"curl", "curl.exe"}),
        EventNameFoundLibcurl = sbomgen.find_files_by_name({"curlver.h"}),
    }
end
```

 When `discover()` returns a table with string keys, each key is treated as a separate event name and its value (a table of file paths) is published to that event. Collection plugins subscribe to specific events via `subscribe_to_event()` as usual. 

 This is backward compatible — returning a sequential table `{"file1", "file2"}` still works as single-event mode. The detection is automatic: tables with any string keys are multi-event, tables with only integer keys (or empty) are single-event. 

 When using multi-event, `get_event_name()` is not used for publishing (the event names come from the returned table keys). However, it is still called during plugin loading for collision detection, so it should return a unique value or be omitted to use the default. 

### Optional discovery functions
<a name="sbomgen-plugin-developer-guide-optional-discovery-functions"></a>

 All of these have sane defaults derived from the directory path. Define them only if you need to override: 


| **Function** | **Default** | **Override when...** | 
| --- | --- | --- | 
| get\_scanner\_name() | {ecosystem} (e.g., python-pip) | You want a custom scanner name | 
| get\_scanner\_description() | "Lua discovery plugin: {ecosystem}" | You want a custom description | 
| get\_scanner\_groups() | Derived from category directory | You need non-standard groups | 
| get\_event\_name() | Derived from directory path | You need custom event routing | 
| get\_localhost\_scan\_paths() | None | Your plugin needs specific paths scanned during localhost scans | 

### Localhost scan paths
<a name="sbomgen-plugin-developer-guide-localhost-scan-paths"></a>

 When sbomgen runs a `localhost` scan, it walks user-specified directories plus any default paths declared by scanners. By default, Lua discovery plugins do not contribute any paths, so files outside the user-specified directories won't appear in the file list. 

 Define `get_localhost_scan_paths()` to return directories or file paths that the localhost walker should include: 

```
function get_localhost_scan_paths()
    return {
        "/usr/bin",
        "/usr/local/bin",
    }
end
```

 The returned paths are appended to the walker's scan list only during `localhost` scans — they have no effect on `container`, `directory`, or `archive` scans. 

### Platform-specific scan paths
<a name="sbomgen-plugin-developer-guide-platform-specific-scan-paths"></a>

 When the files you care about live at different locations on Windows, macOS, and Linux, branch on `sbomgen.get_platform()` and return the appropriate paths for the host: 

```
function get_localhost_scan_paths()
    local platform = sbomgen.get_platform()

    if platform == sbomgen.platform.WINDOWS then
        local drive = sbomgen.get_system_drive()
        return {
            drive .. "/Program Files/MyApp/myapp.exe",
            drive .. "/Program Files (x86)/MyApp/myapp.exe",
        }
    end

    if platform == sbomgen.platform.DARWIN then
        return {"/Applications/MyApp.app/Contents/MacOS/myapp"}
    end

    -- Linux
    return {
        "/usr/bin/myapp",
        "/usr/local/bin/myapp",
    }
end
```

 On Windows, use `sbomgen.get_system_drive()` to resolve the system drive letter (e.g., `"C:"`) rather than hard-coding it. For paths derived from environment variables such as `LOCALAPPDATA` or `PROGRAMFILES`, iterate `sbomgen.get_env_vars()` and look up the value by key. See the [Plugin API reference](sbomgen-plugin-api-reference.md) for details. 

## Collection Plugins
<a name="sbomgen-plugin-developer-guide-collection-plugins"></a>

 A collection plugin only requires the `collect()` function. All other functions are optional. 

 `collect(file_path)` is called once per file discovered by the paired discovery plugin. The typical pattern is: 
+ **Read** the file's contents using `sbomgen.read_file()` (for small files loaded into memory) or `sbomgen.open_file()` (for large files read line-by-line).
+ **Parse** the contents — string matching for simple manifests, `sbomgen.json_decode()` for JSON, `sbomgen.xml_decode()` for XML, or `sbomgen.search_binary()` for compiled binaries.
+ **Publish** each discovered package by calling `sbomgen.push_package()` with the package's metadata.

```
-- REQUIRED: Called once per discovered file.
-- Parse the file and call sbomgen.push_package() for each package found.
function collect(file_path)
    local content, err = sbomgen.read_file(file_path)
    if err or not content then return end

    for line in content:gmatch("[^\r\n]+") do
        local name, version = line:match("^([%w%-%_%.]+)==(.+)$")
        if name and version then
            sbomgen.push_package({
                name = name,
                version = version,
                purl_type = "pypi",
                component_type = sbomgen.component_types.LIBRARY,
            })
        end
    end
end
```

 `collect()` does not return a value. Every `push_package()` call requires `name`, `purl_type`, and `component_type`. See the [Plugin API reference](sbomgen-plugin-api-reference.md) for all supported fields. 

### Attaching metadata to components
<a name="sbomgen-plugin-developer-guide-attaching-metadata-to-components"></a>

 Sbomgen supports two ways to attach metadata to a package component: **PURL qualifiers** and **CycloneDX properties**. They serve different purposes, and the choice between them has implications for how Amazon Inspector identifies vulnerabilities in the resulting SBOM. 


| **Mechanism** | **Where it appears** | **Use for** | 
| --- | --- | --- | 
| qualifiers | Inside the package URL (e.g., pkg:deb/debian/curl@7.88.1?arch=amd64) | Data that is part of the package's identity | 
| properties | In the SBOM's components[].properties array | Descriptive metadata that does not change how the package is identified | 

 **Recommendation: prefer CycloneDX properties (under your own namespace) for custom metadata.** Properties do not alter a component's identity, so they cannot impact Amazon Inspector's vulnerability identification. Reserve PURL qualifiers for cases where your ecosystem's PURL type requires them. 

#### PURL qualifiers
<a name="sbomgen-plugin-developer-guide-purl-qualifiers"></a>

 Some PURL qualifiers have semantic meaning to Amazon Inspector and influence vulnerability identification. For example, on `deb` components Inspector uses qualifiers such as `arch` and `distro` to select the correct vulnerability feed; on `generic` components for compiled binaries, qualifiers such as `go_toolchain` or `rust_toolchain` identify the toolchain used. Setting a qualifier Inspector does not recognize, or omitting one it expects, can cause vulnerabilities to be missed or misattributed. 

 See [What is a package URL?](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-purl-sbom.html) in the Amazon Inspector user guide for the qualifier conventions Inspector recognizes per PURL type. 

 Set qualifiers via the `qualifiers` table on `sbomgen.push_package()`: 

```
sbomgen.push_package({
    name = "curl",
    version = "7.88.1",
    purl_type = "deb",
    namespace = "debian",
    component_type = sbomgen.component_types.LIBRARY,
    qualifiers = {
        arch = "amd64",
        distro = "debian-12",
    },
})
```

 Only set qualifiers when they align with Inspector's expectations for the PURL type. If you need to record metadata that is not part of the package's identity, use CycloneDX properties instead. 

#### CycloneDX properties
<a name="sbomgen-plugin-developer-guide-cyclonedx-properties"></a>

 CycloneDX properties are key-value annotations that appear in the SBOM's `components[].properties` array. They describe a component without affecting how it is identified, so they are the safe choice for plugin-defined metadata. 

 **The `amazon:inspector:*` namespaces are reserved for Amazon Inspector.** Specifically: 
+ `amazon:inspector:sbom_generator:*` — reserved for sbomgen and its built-in scanners.
+ `amazon:inspector:sbom_scanner:*` — reserved for the Amazon Inspector Scan API.

 Plugin authors must not emit keys inside these reserved namespaces. Writing into them can interfere with Inspector's behavior and may be overwritten. For the complete list of reserved keys, see [Using CycloneDX namespaces with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/cyclonedx-namespace.html). 

 Use your own namespace (typically your organization or plugin identifier) when defining properties: 

```
sbomgen.push_package({
    name = "requests",
    version = "2.28.1",
    purl_type = "pypi",
    component_type = sbomgen.component_types.LIBRARY,
    properties = {
        ["acme:python:manifest_path"] = file_path,
        ["acme:python:pinned"] = "true",
        ["acme:python:source"] = "requirements.txt",
    },
})
```

#### Key naming rules
<a name="sbomgen-plugin-developer-guide-key-naming-rules"></a>

 Property keys are processed by sbomgen as follows: 
+ A key that **contains a colon** is used verbatim in the SBOM. Always include at least one colon in your keys so you control the namespace.
+ A key that **does not contain a colon** is automatically prefixed with `amazon:inspector:sbom_generator:` — placing it inside the reserved Inspector namespace. Avoid this shape for custom properties.

```
properties = {
    ["acme:my_plugin:detected_via"] = "lockfile",  -- used as-is (recommended)
    detected_via                   = "lockfile",  -- becomes "amazon:inspector:sbom_generator:detected_via" (avoid)
}
```

 The `sbomgen.properties.*` constants exist so that official scanners emit consistent keys inside the reserved namespace. They are not extension points for custom plugins — use your own namespace instead. 

#### Properties and qualifiers on child components
<a name="sbomgen-plugin-developer-guide-properties-and-qualifiers-on-child-components"></a>

 Nested `children` are independent components. Each child has its own `properties` and `qualifiers` tables; metadata set on the parent does not propagate to children. Set values explicitly on each child that needs them. 

### Optional collection functions
<a name="sbomgen-plugin-developer-guide-optional-collection-functions"></a>


| **Function** | **Default** | **Override when...** | 
| --- | --- | --- | 
| get\_collector\_name() | {ecosystem} (e.g., python-pip) | You want a custom collector name | 
| get\_collector\_description() | empty string | You want a description | 
| subscribe\_to\_event() | Derived from directory path | You need custom event routing | 

## Running Your Plugins
<a name="sbomgen-plugin-developer-guide-running-your-plugins"></a>

 For plugins to produce package metadata, sbomgen must be given an artifact to scan that contains the files your plugin targets (e.g., a directory with `requirements.txt`, `package.json`, or equivalent package manifest files). 

### Basic usage
<a name="sbomgen-plugin-developer-guide-basic-usage"></a>

```
inspector-sbomgen <artifact type> <arguments> --plugin-dir /path/to/plugins
```

 Example: 

```
inspector-sbomgen directory --path /target -o /tmp/sbom.json --plugin-dir /path/to/plugins
```

### With native scanners disabled (Lua-only mode)
<a name="sbomgen-plugin-developer-guide-with-native-scanners-disabled-lua-only-mode"></a>

```
inspector-sbomgen directory --path /target --plugin-dir /path/to/plugins --disable-native-scanners -o sbom.json
```

### With verbose logging
<a name="sbomgen-plugin-developer-guide-with-verbose-logging"></a>

```
inspector-sbomgen directory --path /target --plugin-dir /path/to/plugins --verbose -o sbom.json
```

## Listing Available Scanners
<a name="sbomgen-plugin-developer-guide-listing-available-scanners"></a>

 Use `list-scanners` to see every scanner available to sbomgen. This includes the built-in native scanners, any official Lua plugins bundled with sbomgen, and any custom Lua plugins you've supplied via `--plugin-dir`: 

```
inspector-sbomgen list-scanners --plugin-dir /path/to/plugins
```

```
┌─────────────────────┬────────┬───────────────────────────────┬─────────────────────────────┐
│    SCANNER NAME     │ SOURCE │            GROUPS             │         DESCRIPTION         │
├─────────────────────┼────────┼───────────────────────────────┼─────────────────────────────┤
│ curl                │ custom │ extra-ecosystems              │ Discovers curl version      │
│                     │        │ pkg-scanner                   │ header files (curlver.h)    │
├─────────────────────┼────────┼───────────────────────────────┼─────────────────────────────┤
│ python-requirements │ custom │ pkg-scanner                   │ Discovers requirements*.txt │
│                     │        │ programming-language-packages │ files for Python pip        │
│                     │        │                               │ packages                    │
└─────────────────────┴────────┴───────────────────────────────┴─────────────────────────────┘
```

 The SOURCE column shows where each scanner comes from: 


| **Source** | **Meaning** | 
| --- | --- | 
| native | Built-in scanner bundled with sbomgen | 
| official | Lua plugins bundled with sbomgen | 
| custom | User-provided Lua plugin loaded via --plugin-dir | 

 Running `list-scanners` without `--plugin-dir` still includes both `native` and `official` scanners — those are always available. The `--plugin-dir` flag adds your `custom` scanners to the listing. 

**Components from custom plugins are marked with CycloneDX `scope: "optional"`**  
 Components emitted by user-supplied Lua plugins loaded via `--plugin-dir` are tagged with the CycloneDX `scope: "optional"` field in the resulting SBOM. This distinguishes them from components produced by built-in native scanners and official Lua plugins bundled with sbomgen, which leave `scope` unset (consumers default a missing scope to `"required"` per the CycloneDX specification). The `scope` value applies to every component the plugin emits, including nested children, and you do not need to set it yourself in `sbomgen.push_package()`. 

 To list only Lua scanners without native scanners: 

```
inspector-sbomgen list-scanners --plugin-dir /path/to/plugins --disable-native-scanners
```

## Scanner Selection
<a name="sbomgen-plugin-developer-guide-scanner-selection"></a>

 Lua discovery plugins participate in the same scanner selection model as the built-in native scanners. By default, sbomgen runs all scanners whose groups match the default scanner groups for the artifact type. You can override this with three flags: 

### Run only specific scanners
<a name="sbomgen-plugin-developer-guide-run-only-specific-scanners"></a>

 Use `--scanners` to run only the named scanners. All other scanners are excluded: 

```
inspector-sbomgen directory --path /target \
    --plugin-dir /path/to/plugins \
    --scanners python-requirements \
    -o sbom.json
```

 This runs only the `python-requirements` scanner. You can pass multiple scanner names separated by commas, or pass a scanner group name (e.g., `programming-language-packages`) to enable every scanner that belongs to that group. 

### Exclude specific scanners
<a name="sbomgen-plugin-developer-guide-exclude-specific-scanners"></a>

 Use `--skip-scanners` to exclude named scanners while running everything else: 

```
inspector-sbomgen directory --path /target \
    --plugin-dir /path/to/plugins \
    --skip-scanners python-poetry \
    -o sbom.json
```

 This runs every default scanner except `python-poetry`. Like `--scanners`, this flag also accepts group names, so passing `--skip-scanners programming-language-packages` disables every scanner in that group. 

**Note**  
`--scanners` and `--skip-scanners` are mutually exclusive. Passing both produces an error.

### Add scanners from non-default groups
<a name="sbomgen-plugin-developer-guide-add-scanners-from-non-default-groups"></a>

 The default scanner set depends on the artifact type being scanned (see the matrix in [How groups affect selection](#sbomgen-plugin-developer-guide-how-groups-affect-selection) below). A scanner whose groups are not part of the default set for the artifact type will not run unless you opt it in. Use `--additional-scanners` to append scanners to the default set without replacing it: 

```
inspector-sbomgen directory --path /target \
    --plugin-dir /path/to/plugins \
    --additional-scanners my-extra-scanner \
    -o sbom.json
```

 This runs every default scanner for the artifact type, plus `my-extra-scanner`. The flag accepts a comma-separated list of scanner names or group names, and stacks with the default set rather than replacing it. Use `list-scanners` to check which groups a scanner belongs to. 

### How groups affect selection
<a name="sbomgen-plugin-developer-guide-how-groups-affect-selection"></a>

 The `get_scanner_groups()` function in your discovery plugin determines which groups the scanner belongs to. Whether a scanner runs by default depends on both its groups and the artifact type being scanned. The matrix below shows which groups are included in the default scanner set for each artifact type: 


| **Group** | **`directory` / `archive`** | **`container`** | **`localhost`** | **`volume`** | **`binary`** | 
| --- | --- | --- | --- | --- | --- | 
| os | — | ✓ | ✓ | ✓ | — | 
| programming-language-packages | ✓ | ✓ | ✓ | ✓ | — | 
| binary | ✓ | ✓ | — | — | ✓ | 
| extra-ecosystems | — | ✓ | ✓ | ✓ | — | 
| dockerfile | ✓ | ✓ | — | — | — | 
| custom | ✓ | ✓ | ✓ | ✓ | ✓ | 
| certificate | — | — | — | — | — | 
| machine-learning | — | — | — | — | — | 
| pkg-scanner | — | — | — | — | — | 

 A ✓ means every scanner in that group runs by default for that artifact type. A `—` means the group is not in the default set, so its scanners only run if explicitly selected via `--scanners` or `--additional-scanners`. 

 Notable details: 
+ **`custom`** is always in the default set — custom plugins loaded via `--plugin-dir` automatically receive the `custom` group, so they run by default regardless of artifact type.
+ **`extra-ecosystems`** is default for `container`, `localhost`, and `volume` scans, but not for `directory`, `archive`, or `binary` scans. For those types you must pass `--additional-scanners` (by name or by the `extra-ecosystems` group) to include them.
+ **`pkg-scanner`** is informational — it marks a scanner as a package collector for display in `list-scanners`, but does not by itself cause the scanner to run. Pair it with an execution group (e.g., `programming-language-packages`) in `get_scanner_groups()`.

 For example, a plugin that returns `{sbomgen.groups.EXTRA_ECOSYSTEMS, sbomgen.groups.PACKAGE_COLLECTOR}` will run by default on container, localhost, and volume scans, but will require `--additional-scanners` (or `--scanners`) on directory, archive, and binary scans. 

## Plugin Collision Rules
<a name="sbomgen-plugin-developer-guide-plugin-collision-rules"></a>

 Sbomgen enforces unique metadata across all loaded plugins to prevent silent overwrites and ensure SBOM integrity. When a collision is detected, the later plugin is **skipped** and a warning is logged. 

### What is checked
<a name="sbomgen-plugin-developer-guide-what-is-checked"></a>


| **Metadata** | **Scope** | **On collision** | 
| --- | --- | --- | 
| Discovery event name (get\_event\_name) | All discovery plugins | Second plugin skipped | 
| Scanner name (get\_scanner\_name) | All discovery plugins | Second plugin skipped | 
| Collector name (get\_collector\_name) | All collection plugins | Second plugin skipped | 

### What is allowed
<a name="sbomgen-plugin-developer-guide-what-is-allowed"></a>

 Multiple collection plugins **can** subscribe to the same event via `subscribe_to_event()`. This is the intended fan-out pattern — one discovery plugin can feed multiple collectors that each do different things (e.g., one extracts packages, another detects secrets). 

### Avoiding collisions
<a name="sbomgen-plugin-developer-guide-avoiding-collisions"></a>

 If two plugins use the same scanner name, event name, or collector name, the second one loaded is skipped. To resolve collisions, rename the conflicting metadata by defining the appropriate override function in your plugin (`get_scanner_name()`, `get_event_name()`, or `get_collector_name()`). 

### Collision warning example
<a name="sbomgen-plugin-developer-guide-collision-warning-example"></a>

```
[custom:python-pip] SKIPPED: discovery event name "EventNameFoundPythonRequirements"
is already registered by [official:python-pip]. Each discovery plugin must have a
unique event name. Rename get_event_name() in your plugin to use a unique name.
```

 The warning tells you which plugin was skipped, what collided, which plugin already owns that name, and which function to change. 

## Debugging
<a name="sbomgen-plugin-developer-guide-debugging"></a>

### Console logging
<a name="sbomgen-plugin-developer-guide-console-logging"></a>

 Plugins can emit messages to sbomgen's console output using the following functions: 


| **Function** | **Level** | **Visible by default?** | 
| --- | --- | --- | 
| sbomgen.log\_debug(message) | DEBUG | No — requires --verbose | 
| sbomgen.log\_info(message) | INFO | Yes | 
| sbomgen.log\_warn(message) | WARN | Yes | 
| sbomgen.log\_error(message) | ERROR | Yes | 

 All log output from a plugin is automatically prefixed with the plugin's source and path (e.g., `[custom:python-pip]`), so messages from different plugins are easy to distinguish. `log_info`, `log_warn`, and `log_error` always print; `log_debug` only prints when sbomgen is invoked with `--verbose`. 

```
function discover()
    sbomgen.log_info("starting discovery")
    local files = sbomgen.find_files_by_name({"requirements.txt"})
    sbomgen.log_debug(string.format("matched %d files", #files))
    if #files == 0 then
        sbomgen.log_warn("no requirements.txt files found")
    end
    return files
end
```

### Breakpoints
<a name="sbomgen-plugin-developer-guide-breakpoints"></a>

 Use `sbomgen.breakpoint()` to pause plugin execution and block until you press Enter. This acts as a crude debugger — combine it with log statements to inspect state at specific points. 

```
function discover()
    local files = sbomgen.find_files_by_name({"requirements.txt"})

    sbomgen.log_info(string.format("about to inspect %d files", #files))
    sbomgen.breakpoint("before file inspection — press Enter to continue")

    local found = {}
    for _, f in ipairs(files) do
        if not f:match("[/\\]tests[/\\]") then
            table.insert(found, f)
        end
    end

    sbomgen.log_info(string.format("kept %d files after filtering", #found))
    sbomgen.breakpoint("after filtering — press Enter to continue")

    return found
end
```

 The breakpoint message is printed to stderr. Execution pauses until you press Enter, giving you time to review log output. 

### Common issues
<a name="sbomgen-plugin-developer-guide-common-issues"></a>


| **Symptom** | **Cause** | **Fix** | 
| --- | --- | --- | 
| Plugin not loaded | Missing init.lua | Ensure entrypoint exists at the correct directory depth | 
| "missing required function" | Typo in function name | Check that get\_scanner\_name, get\_scanner\_description, get\_scanner\_groups, discover, get\_event\_name, get\_localhost\_scan\_paths, get\_collector\_name, collect, subscribe\_to\_event are defined | 
| Collection plugin never called | Event name mismatch | Verify get\_event\_name() and subscribe\_to\_event() return the same string | 
| No packages in SBOM | push\_package not called or required fields missing | Ensure name, purl\_type, and component\_type are set in every push\_package call (including children). Use sbomgen.component\_types.\* constants. | 
| Runtime error in plugin | Lua error during execution | Check sbomgen output for warning messages with the error details | 
| "SKIPPED: discovery event name ... is already registered" | Another plugin uses the same event name | Rename get\_event\_name() to a unique value | 
| "SKIPPED: scanner name ... is already registered" | Another plugin uses the same scanner name | Rename get\_scanner\_name() to a unique value | 
| "SKIPPED: collector name ... is already registered" | Another plugin uses the same collector name | Rename get\_collector\_name() to a unique value | 

## API Reference
<a name="sbomgen-plugin-developer-guide-api-reference"></a>

 The complete function catalog is maintained in a companion document: 

 **→ [Plugin API reference](sbomgen-plugin-api-reference.md)** 

 The API reference covers every `sbomgen.*` function (file I/O, binary utilities, package output, regex, structured parsing, Windows registry, logging, debugging), the `testing.*` API available in test files, all built-in constants (`properties`, `groups`, `component_types`, `platform`), and the plugin lifecycle globals. 

## Error Handling
<a name="sbomgen-plugin-developer-guide-error-handling"></a>

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

## Sandbox Restrictions
<a name="sbomgen-plugin-developer-guide-sandbox-restrictions"></a>

 Plugins run in a sandboxed Lua VM with limited standard library access: 


| **Library** | **Available** | **Notes** | 
| --- | --- | --- | 
| base | ✓ | dofile, loadfile, loadstring are removed | 
| string | ✓ | Full string manipulation | 
| table | ✓ | Full table manipulation | 
| math | ✓ | Full math library | 
| package | ✓ | require() restricted to plugin directory | 
| io | ✗ | Use sbomgen.\* I/O functions instead | 
| os | ✗ | Blocked for security | 
| debug | ✗ | Blocked to prevent VM introspection | 
| coroutine | ✗ | Not loaded | 

 Direct filesystem access via `io.open` or `os.execute` is not available. All file operations must go through the `sbomgen` API, which ensures consistent behavior across artifact types. 

 The `sbomgen` file functions confine reads to the artifact under inventory: a path that resolves outside the artifact root (for example via `../` traversal) is rejected and returns an error. The `localhost` artifact type is the exception — it inventories the host itself, so reads are not confined to a narrower root. 

 `require()` can load modules only from within the plugin's own directory tree. Parent-directory traversal such as `require("../shared")` is blocked. 

### SBOM contents are not sanitized
<a name="sbomgen-plugin-developer-guide-sbom-contents-not-sanitized"></a>

 The read boundary above governs what a plugin can read, not what it writes. Sbomgen does not inspect or filter the data a plugin emits into the SBOM, and does not detect or redact secrets, credentials, or other sensitive values. Whatever a plugin places into a finding appears in the output SBOM and travels wherever that SBOM is published, so only emit data derived from the artifact you intend to inventory. 

## Sharing Code Between Plugins
<a name="sbomgen-plugin-developer-guide-sharing-code-between-plugins"></a>

 You can use `require()` to load helper modules from within your plugin's directory: 

```
my-ecosystem/
├── init.lua
└── helpers.lua
```

```
-- helpers.lua
local M = {}
function M.parse_version(s)
    return string.match(s, "(%d+%.%d+%.%d+)")
end
return M
```

```
-- init.lua
local helpers = require("helpers")

function subscribe_to_event() return "MyEvent" end

function collect(file_path)
    local content, err = sbomgen.read_file(file_path)
    if err then return end
    local version = helpers.parse_version(content)
    -- ...
end
```

 Subdirectories with `init.lua` are also supported: 

```
my-ecosystem/
├── init.lua
└── parsers/
    └── init.lua
```

```
local parsers = require("parsers")
```

 `require()` is restricted to your plugin's directory. You cannot load modules from other plugins or system paths. Third-party Lua libraries (e.g., from LuaRocks) are not supported — only local helper modules within the plugin directory can be loaded. 