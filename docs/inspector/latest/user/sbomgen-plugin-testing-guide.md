

# Plugin testing guide
<a name="sbomgen-plugin-testing-guide"></a>

 Plugin authors write and test Lua plugins entirely in Lua — no Go toolchain required. Tests are co-located with the plugin under `init_test.lua` and run via the `inspector-sbomgen plugin test` command. 

 For general plugin authoring, see the [Plugin developer guide](sbomgen-plugin-developer-guide.md). For the complete function catalog (including the `testing.*` API), see the [Plugin API reference](sbomgen-plugin-api-reference.md). 

```
-- init_test.lua (next to init.lua)
function test_discovers_curl_version()
    local result = testing.scan_directory("_testdata/include/curl")
    testing.assert_equals(1, #result.findings)
    testing.assert_equals("libcurl", result.findings[1].name)
    testing.assert_equals("8.14.1", result.findings[1].version)
end
```

```
# Run every test under a plugin directory
inspector-sbomgen plugin test --path ./my-plugins

# Verbose output — show each test name and result
inspector-sbomgen plugin test --path ./my-plugins -v
```

## Quick Start
<a name="sbomgen-plugin-testing-guide-quick-start"></a>

### 1. Create a test file
<a name="sbomgen-plugin-testing-guide-1-create-a-test-file"></a>

 Place `init_test.lua` next to your plugin's `init.lua`: 

```
my-plugin/
├── discovery/cross-platform/extra-ecosystems/curl/
│   ├── init.lua
│   ├── init_test.lua
│   └── _testdata/
│       └── include/curl/curlver.h
```

### 2. Write test functions
<a name="sbomgen-plugin-testing-guide-2-write-test-functions"></a>

 Any global function starting with `test_` is discovered and executed: 

```
function test_finds_libcurl()
    local result = testing.scan_directory("_testdata/include/curl")
    testing.assert_equals(1, #result.findings)
    testing.assert_equals("libcurl", result.findings[1].name)
end

function test_no_findings_for_empty_dir()
    local result = testing.scan_directory("_testdata/empty")
    testing.assert_equals(0, #result.findings)
end
```

### 3. Run tests
<a name="sbomgen-plugin-testing-guide-3-run-tests"></a>

```
inspector-sbomgen plugin test --path ./my-plugin
```

## Directory Layout
<a name="sbomgen-plugin-testing-guide-directory-layout"></a>

### Plugin structure
<a name="sbomgen-plugin-testing-guide-plugin-structure"></a>

 Test files and test data are co-located with the plugin: 

```
my-plugins/
├── discovery/
│   └── cross-platform/
│       └── extra-ecosystems/
│           └── curl/
│               ├── init.lua          # plugin source
│               ├── init_test.lua     # test file
│               └── _testdata/        # test fixtures
│                   ├── include/curl/curlver.h
│                   └── binaries/unix/curl
├── collection/
│   └── cross-platform/
│       └── extra-ecosystems/
│           └── curl-installation/
│               ├── init.lua
│               └── init_test.lua
```

### Test file naming
<a name="sbomgen-plugin-testing-guide-test-file-naming"></a>
+ Default: `init_test.lua` next to the plugin's `init.lua`
+ Multiple test files per plugin: any file matching `*_test.lua` is discovered
+ Examples: `init_test.lua`, `parsing_test.lua`, `discovery_test.lua`

### Test data: `_testdata/`
<a name="sbomgen-plugin-testing-guide-test-data-testdata"></a>

 Test data lives in `_testdata/` next to the plugin. The leading underscore is a convention that keeps fixtures visually separate from plugin source; the `plugin test` command does not descend into `_testdata/` when searching for `*_test.lua` files, so fixtures are never mistaken for test files. 

 Test files reference fixtures with relative paths: 

```
local result = testing.scan_directory("_testdata/include/curl")
```

 Paths are resolved relative to the directory containing the test file. 

## The `testing.*` API
<a name="sbomgen-plugin-testing-guide-the-testing-api"></a>

### Scan Functions
<a name="sbomgen-plugin-testing-guide-scan-functions"></a>

 Each scan function creates an artifact, runs the plugin's discovery → collection pipeline, and returns findings. The test author never manually creates artifacts, event buses, or registries. 

```
-- Scan a directory of test fixtures (most common)
local result = testing.scan_directory("_testdata/curl")

-- Alias for scan_directory (archives use the same backend)
local result = testing.scan_archive("_testdata/app.tar.gz")

-- Scan as a localhost artifact
local result = testing.scan_localhost("_testdata/curl")

-- Scan a compiled binary
local result = testing.scan_binary("_testdata/binaries/curl")

-- Scan a mounted volume
local result = testing.scan_volume("_testdata/volume-root")

-- Scan a container image tarball
local result = testing.scan_container("_testdata/images/alpine.tar")
```

 Each scan function: 
+ Creates a fresh artifact for each call (no state leaks between calls)
+ Loads only the current plugin's discovery \+ collection pair
+ Returns a result table

### Result Table
<a name="sbomgen-plugin-testing-guide-result-table"></a>

```
result.findings              -- array of finding tables
result.findings[1].name      -- package name (string)
result.findings[1].version   -- package version (string)
result.findings[1].purl      -- package URL (string)
result.findings[1].component_type -- component type (string)
result.findings[1].properties    -- table<string, string>
result.findings[1].children      -- array of nested finding tables (same shape)
```

### Assertions
<a name="sbomgen-plugin-testing-guide-assertions"></a>

```
-- Equality
testing.assert_equals(expected, actual, message?)
testing.assert_not_equals(expected, actual, message?)

-- Truthiness
testing.assert_true(value, message?)
testing.assert_false(value, message?)

-- Nil checks
testing.assert_nil(value, message?)
testing.assert_not_nil(value, message?)

-- String
testing.assert_contains(haystack, needle, message?)
testing.assert_matches(string, pattern, message?)

-- Tables
testing.assert_length(table, expected_length, message?)

-- Control flow
testing.fail(message)    -- immediately fail the current test
testing.skip(message)    -- skip the current test (not a failure)
```

### Standard `sbomgen.*` API
<a name="sbomgen-plugin-testing-guide-standard-sbomgen-api"></a>

 The full `sbomgen.*` API (file I/O, regex, system info, logging, etc.) is available in test files, same as in production plugins. However, `sbomgen.*` functions that require an artifact (e.g., `sbomgen.read_file()`) only work inside a `testing.scan_*` callback — they are not available at the top level of a test function. 

## Running Tests
<a name="sbomgen-plugin-testing-guide-running-tests"></a>

```
# Run all tests under a plugin directory
inspector-sbomgen plugin test --path ./my-plugins

# Filter by regex pattern
inspector-sbomgen plugin test --path ./my-plugins --run curl

# Verbose output (show each test name and result)
inspector-sbomgen plugin test --path ./my-plugins -v

# Stop on the first failing test
inspector-sbomgen plugin test --path ./my-plugins --fail-fast
```

 The `--path` flag accepts a plugin root directory (containing `discovery/` and/or `collection/`) or a single ecosystem directory (auto-detected). The command exits non-zero if any test fails. 

### Output format
<a name="sbomgen-plugin-testing-guide-output-format"></a>

 With `-v`, each test prints a `=== RUN` line and a result line (`--- PASS`, `--- FAIL`, or `--- SKIP`). Without `-v`, only failing tests print. A summary line is printed at the end: 

```
=== RUN   curl/discovery/init_test/test_discovers_libcurl_header
--- PASS: curl/discovery/init_test/test_discovers_libcurl_header (0.04s)
=== RUN   curl/discovery/init_test/test_discovers_curl_binary_unix
--- PASS: curl/discovery/init_test/test_discovers_curl_binary_unix (0.04s)
=== RUN   curl/discovery/init_test/test_no_findings_for_unrelated_files
--- PASS: curl/discovery/init_test/test_no_findings_for_unrelated_files (0.04s)
ok    3 tests passed
```

## Testing Plugin Helpers
<a name="sbomgen-plugin-testing-guide-testing-plugin-helpers"></a>

 The test file is loaded into the same Lua VM as the plugin's `init.lua`. Global functions defined in the plugin are callable from tests. To test helper functions, expose them as globals or in a module table: 

```
-- init.lua
M = {}
function M.parse_version(raw)
    return string.match(raw, "(%d+%.%d+%.%d+)")
end

function collect(file_path)
    local ver = M.parse_version(...)
    -- ...
end
```

```
-- init_test.lua
function test_parse_version_extracts_semver()
    testing.assert_equals("1.2.3", M.parse_version("curl/1.2.3"))
end

function test_parse_version_returns_nil_for_garbage()
    testing.assert_nil(M.parse_version("not-a-version"))
end
```

 Functions declared `local` in `init.lua` are not visible to the test file. This is standard Lua scoping. 

## Behavior and Invariants
<a name="sbomgen-plugin-testing-guide-behavior-and-invariants"></a>

### Shared VM, shared state
<a name="sbomgen-plugin-testing-guide-shared-vm-shared-state"></a>

 Test functions within a single file share a Lua VM. A global variable set in one `test_*` function is visible to subsequent functions. If two functions define the same global, the second overwrites the first. Each test should be self-contained and not depend on state from other tests. 

### Non-deterministic execution order
<a name="sbomgen-plugin-testing-guide-non-deterministic-execution-order"></a>

 Test functions are discovered by iterating Lua's global table, which uses hash-based ordering. **Tests are not guaranteed to run in the order they are defined.** Do not write tests that depend on execution order. 

### Fresh artifact per scan call
<a name="sbomgen-plugin-testing-guide-fresh-artifact-per-scan-call"></a>

 Each call to `testing.scan_directory()` (or any scan function) creates a completely new artifact. There is no state carried between scan calls within a test or across tests. 

### Plugin loading
<a name="sbomgen-plugin-testing-guide-plugin-loading"></a>

 Plugins are loaded once per test run, not once per test file. The test runner loads all plugins from the provided filesystem, then matches each test file to its corresponding plugin VM by phase, platform, category, and ecosystem. 

### Assertion behavior
<a name="sbomgen-plugin-testing-guide-assertion-behavior"></a>

 When an assertion fails, the failure is recorded but the test function continues executing — subsequent assertions and statements still run. If more than one assertion fails in the same test, the **most recent** failure is the message reported in the summary; earlier failures are overwritten. To stop a test on its first failure, return from the function after the failing assertion (or use `testing.fail()` inside a conditional). 

## Limitations
<a name="sbomgen-plugin-testing-guide-limitations"></a>
+ **`local` functions are not testable.** Only global functions from `init.lua` are visible to the test file. Expose helpers via a module table if they need testing.
+ **No `sbomgen.*` file I/O outside scan calls.** Functions like `sbomgen.read_file()` require an artifact context, which only exists inside `testing.scan_*` calls.
+ **No lifecycle hooks.** There is no `before_each`, `after_each`, `setup`, or `teardown`. Each test function manages its own state.
+ **No test timeout.** A test function that loops forever will hang the runner.
+ **No coverage reporting.** There is no way to measure which lines of `init.lua` were exercised.
+ **No benchmarks.** The test framework does not support performance benchmarks.

## Developer Responsibilities
<a name="sbomgen-plugin-testing-guide-developer-responsibilities"></a>

### When writing a new Lua plugin
<a name="sbomgen-plugin-testing-guide-when-writing-a-new-lua-plugin"></a>
+ Create `init_test.lua` next to your `init.lua`
+ Create `_testdata/` with minimal fixtures that exercise your plugin's logic
+ Write `test_*` functions covering: successful detection, version extraction, edge cases, and no-match scenarios
+ Run tests locally before submitting

### Test data guidelines
<a name="sbomgen-plugin-testing-guide-test-data-guidelines"></a>
+ Keep fixtures minimal — use the smallest file that exercises the behavior
+ Avoid committing large binaries to `_testdata/` when a small text fixture would suffice
+ Each plugin's `_testdata/` should be self-contained — no references to files outside the plugin directory. At runtime, `sbomgen.*` reads are confined to the artifact under inventory, so a plugin that depends on files elsewhere on the host will not work outside `localhost` scans.
+ Use representative, non-sensitive fixtures. Sbomgen does not redact SBOM contents, so never commit real secrets or credentials to `_testdata/`.