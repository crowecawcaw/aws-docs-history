

# Supported languages and source files

AWS Continuum selects source files for code vulnerability scans by their file extensions. A scan needs at least one supported source file outside the excluded folders across the selected repositories.

The following table lists the supported languages and source file types. File extensions are case-sensitive. For example, `app.py` qualifies as a Python source file, but `app.PY` doesn't.


**Supported source file extensions**  

| Language or source file type | File extensions | 
| --- | --- | 
| C | .c, .h | 
| C\+\+ | .cc, .cpp, .cxx, .hh, .hpp, .hxx | 
| C\# | .cs | 
| Go | .go | 
| GraphQL | .graphql | 
| Java | .java | 
| JavaScript | .js, .jsx | 
| Kotlin | .kt | 
| PHP | .php | 
| Python | .py | 
| Ruby | .rb | 
| Rust | .rs | 
| Scala | .scala | 
| Shell | .bash, .sh, .zsh | 
| SQL | .sql | 
| Svelte | .svelte | 
| Swift | .swift | 
| TypeScript | .ts, .tsx | 
| Vue | .vue | 

Extensions not listed in the table don't qualify as source files. For example, `.mjs` and `.cjs` don't qualify, even though JavaScript is supported. A repository can contain both supported source files and other file types. The presence of other file types doesn't prevent a scan when supported source files are available.

## Excluded folders
<a name="cv-supported-languages-excluded-folders"></a>

When AWS Continuum selects source files, it skips folders with the following names and all their contents. These exclusions apply at any depth in a repository:
+ `.git`, `.hg`, and `.svn`
+ `node_modules`, `.venv`, and `venv`
+ `__pycache__`, `.mypy_cache`, `.pytest_cache`, and `.tox`
+ `build`, `dist`, `target`, `.next`, and `.nuxt`

Source files in these folders don't qualify for a scan, even if their extensions appear in the table.