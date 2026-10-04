

# Expression quick reference
<a name="build-job-bundle-expressions-reference"></a>

Expressions use a subset of Python expression syntax. Values have one of the types `bool`, `int`, `float`, `string`, `path`, `range_expr`, or `list[{{T}}]`. Job parameters have the lowercase form of their declared type, so a `PATH` parameter is a `path` value and a `CHUNK[INT]` task parameter is a `range_expr`. Any function can also be called as a method on its first argument, so `upper(Param.Name)` and `Param.Name.upper()` are the same. This page lists the parts of the language that job templates use most. For the complete function library, see the [Open Job Description function library](https://github.com/OpenJobDescription/openjd-specifications/wiki/2026-02-Expression-Language#2-function-library) on the GitHub website.

The following variables are available. Job parameters are known when the job is created, so an expression that uses only `Param` values is evaluated then. Task and session variables are known only on the worker, so an expression that uses them is type-checked at submission and evaluated when the task runs.


| Variable | Type | Description | 
| --- | --- | --- | 
| Param.{{Name}} | Declared type | A job parameter value. For PATH and LIST[PATH] parameters, path mapping rules have been applied. | 
| RawParam.{{Name}} | string | The original value of a PATH parameter as submitted, before path mapping. Use it to manipulate a path from another operating system before calling apply\_path\_mapping(). | 
| Task.Param.{{Name}} | Declared type | A task parameter value. A CHUNK[INT] parameter is a range\_expr; call list() on it to iterate the frames. | 
| Task.File.{{Name}}, Env.File.{{Name}} | path | The location on the worker where an embedded file was written. | 
| Session.WorkingDirectory | path | The session's temporary working directory on the worker. | 
| Job.Name, Step.Name | string | The resolved job name and the current step name. | 

The following operators and functions cover most template logic.


| Category | Operators and functions | Example | 
| --- | --- | --- | 
| Arithmetic | \+ - \* / // % \*\*, abs(), min(), max(), sum(), floor(), ceil(), round() | {{ min(Param.FrameRange) }} and {{ max(Param.FrameRange) }} for the first and last frame of a frame range parameter | 
| Comparison and logic | == \!= < <= > >=, in, not in, and, or, not, {{a}} if {{test}} else {{b}} | {{ 'large' if Param.Epochs >= 100 else 'small' }} | 
| Conversion | string(), int(), float(), bool(), path(), list(), range\_expr() | {{ len(list(Task.Param.Frame)) }} | 
| Strings | upper(), lower(), strip(), replace(), split(), join(), startswith(), endswith(), zfill(), removeprefix(), removesuffix(), slicing [{{start}}:{{stop}}] | {{ zfill(Task.Param.Frame, 4) }} | 
| Regular expressions | re\_match(), re\_search(), re\_findall(), re\_sub(), re\_split(), re\_escape() | {{ re\_search(Param.Dataset.stem, r'\_v(\\d\+)')[1] }} | 
| Paths | / to join, \+ to append text, .name, .stem, .suffix, .parent, .parts, with\_suffix(), with\_stem(), with\_number(), as\_posix(), apply\_path\_mapping() | {{ Param.OutputPattern.with\_number(Task.Param.Frame) }} | 
| Lists | len(), indexing [{{i}}], [{{expr}} for {{x}} in {{list}}], sorted(), reversed(), unique(), flatten(), range() | {{ [Param.OutputDir / f for f in Param.Files] }} | 
| Script quoting | repr\_sh() for bash, repr\_pwsh() for PowerShell, repr\_cmd() for Windows CMD, repr\_py() for Python, repr\_json() for JSON | {{ repr\_pwsh(list(Task.Param.Frame)) }} | 
| Validation | fail({{message}}) stops job creation with a message | {{ Param.Count if Param.Count > 0 else fail('Count must be positive') }} | 

The `with_number()` function replaces the frame number in a file name, whether the name holds a placeholder or an actual number. It recognizes hash padding such as `####`, printf-style `%04d`, and a run of digits such as `0001`, and it pads the result to the same width. So a parameter value can be a pattern or the first file of a sequence: `path('/renders/shot_####.exr')`, `path('/renders/shot_%04d.exr')`, and `path('/renders/shot_0001.exr')` all give `/renders/shot_0072.exr` for `with_number(72)`. When the name has none of these, the function appends a four-digit number to the stem.

A few behaviors differ from Python. The `and` and `or` operators return one of their operands, and only `false` and `null` count as false, so `0`, an empty string, and an empty list do not. This makes `or` a way to supply a fallback for an unset value: `{{ Param.OutputName or Param.InputFile.stem }}` uses the input file's name when the optional parameter is `null`, and an empty string is kept as given. The condition in `{{a}} if {{test}} else {{b}}` must be a boolean. Integers are 64-bit and an overflow is an error rather than a silent wrap. Comparing values of different types with `==` is `false` rather than an error, except that `int` compares with `float` and `string` compares with `path`. The JSON literals `null`, `true`, and `false` are accepted alongside `None`, `True`, and `False`.

For more information, see the following resources:
+ The [Open Job Description expression language](https://github.com/OpenJobDescription/openjd-specifications/wiki/2026-02-Expression-Language) on the GitHub website – The grammar, type system, evaluation rules, and every operator and function with its signature.
+ [Add expressions to a job template](build-job-bundle-expressions-add.md) – Add expressions to a template.