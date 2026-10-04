

# Expressions in job templates
<a name="build-job-bundle-expressions"></a>

A job template uses `{{ }}` format strings to insert values into job names, commands, arguments, and embedded files. With the `EXPR` extension to Open Job Description, the text inside `{{ }}` is an *expression*. An expression can be a plain reference such as `{{Param.{{Name}}}}`, or it can compute a value with arithmetic, comparisons, `if`/`else` conditionals, string and path operations, and list comprehensions. The syntax is a subset of Python.

Expressions are the glue between the parameters a user submits and the command line an application accepts. A memory requirement in GiB becomes the MiB a host requirement expects. A frame range parameter becomes start and end frame arguments. A file sequence pattern becomes the file for the task's frame. A flag appears in the argument list only when a boolean parameter is set. Expressions work with every job parameter type, including the boolean, list, and frame range types described in [Job parameter types](build-job-bundle-parameter-types.md). For the full specification, see the [Open Job Description expression language](https://github.com/OpenJobDescription/openjd-specifications/wiki/2026-02-Expression-Language) on the GitHub website.

The following examples show common expressions. Each one is a single format string in a job template.


| Expression | What it does | 
| --- | --- | 
| {{ Param.WorkerMemoryGiB \* 1024 }} | Converts a memory requirement that a user enters in GiB to the MiB that the amount.worker.memory host requirement expects. | 
| {{ Param.InputSequence.with\_number(Task.Param.Frame) }} | Turns a file sequence pattern such as /data/timestep\_\#\#\#\#.h5, or the first file of the sequence such as /data/timestep\_0001.h5, into the file for the task's frame, /data/timestep\_0072.h5 for frame 72. | 
| {{ 64 if Param.Precision == 'fp16' else 16 }} | Chooses a batch size based on a string parameter with allowed values. | 
| {{ '--gpu' if Param.UseGpu else null }} | Adds the --gpu argument when a boolean parameter is true. When the expression evaluates to null in an args list, Deadline Cloud omits the argument entirely. | 
| {{ repr\_sh(Param.InputFile) }} | Quotes a path for a bash script so that spaces and special characters in the file name are safe. | 
| {{ Param.Cameras.join(',') }} | Joins a LIST[STRING] parameter, such as the cameras to render in a scene, into a comma-separated string. | 

Deadline Cloud checks expressions when you submit the job. It parses every expression, verifies that each referenced parameter exists, and type-checks the operations against the declared parameter types. A misspelled parameter name or a string method called on an integer fails the submission with a message that points to the error, before any worker picks up a task.

Expressions are deterministic and self-contained. There are no user-defined functions. An expression can't read files, reach the network, or inspect environment variables, so a template's behavior depends only on its parameter values.

Evaluation also has fixed limits on memory and on the number of operations. These limits are large enough for template logic, and they stop a template from consuming unbounded resources during job creation.

A template opts in to expressions by listing `EXPR` in its `extensions`. In a template without the extension, `{{ }}` accepts only a parameter reference such as `{{Param.Frames}}`.

To decide whether to use an expression or a script, consider where the logic belongs. An expression is the right choice for glue between parameter values and a command line. Use an expression to compute a number, derive a path, choose between two values, or include or exclude an argument. If you need to inspect the file system, call an application, or iterate over results with custom logic, put that logic in the step's script. The script can still receive expression results as arguments.

For more information about expressions, see the following topics:
+ [Add expressions to a job template](build-job-bundle-expressions-add.md) – Enable the extension in a template and write your first expressions.
+ [Job parameter types](build-job-bundle-parameter-types.md) – Look up every job parameter type, including the boolean, list, and frame range types that the `EXPR` extension adds.
+ [Expression quick reference](build-job-bundle-expressions-reference.md) – Look up the variables, operators, and functions available in an expression.