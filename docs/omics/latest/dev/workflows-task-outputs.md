AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Task outputs in a HealthOmics workflow definition

You specify task outputs in the workflow definition. By default, HealthOmics discards all intermediate task files when
the workflow completes. To export an intermediate file, you define it as an output.

If you use call caching, HealthOmics saves task outputs to the cache, including any intermediate files that you define
as outputs.

The following topics include task definition examples for each of the workflow definition languages.

###### Topics

- [Task outputs for WDL](#workflow-task-outputs-wdl "#workflow-task-outputs-wdl")
- [Task outputs for Nextflow](#workflow-task-outputs-nextflow "#workflow-task-outputs-nextflow")
- [Task outputs for CWL](#workflow-task-outputs-cwl "#workflow-task-outputs-cwl")

## Task outputs for WDL

For workflow definitions written in WDL, define your outputs in the top level workflow
**outputs** section.

HealthOmics

###### Topics

- [Task output for STDOUT](#task-outputs-wdl-stdout "#task-outputs-wdl-stdout")
- [Task output for STDERR](#task-outputs-wdl-stderr "#task-outputs-wdl-stderr")
- [Task output to a file](#task-outputs-wdl-file "#task-outputs-wdl-file")
- [Task output to an array of files](#task-outputs-wdl-files "#task-outputs-wdl-files")

### Task output for STDOUT

This example creates a task named `SayHello` that echoes the STDOUT content to the task output
file. The WDL **stdout** function captures the STDOUT content (in this example, the input string
**Hello World!**) in file **stdout_file**.

Because HealthOmics creates logs for all STDOUT content, the output also appears in CloudWatch Logs, along with other STDERR
logging information for the task.

```
version 1.0
 workflow HelloWorld {
    input {
        String message = "Hello, World!"
        String ubuntu_container = "123456789012.dkr.ecr.us-east-1.amazonaws.com/dockerhub/library/ubuntu:20.04"
    }

    call SayHello {
        input:
            message = message,
            container = ubuntu_container
    }

    output {
        File stdout_file = SayHello.stdout_file
    }
}

task SayHello {
    input {
        String message
        String container
    }

    command <<<
        echo "~{message}"
        echo "Current date: $(date)"
        echo "This message was printed to STDOUT"
    >>>

    runtime {
        docker: container
        cpu: 1
        memory: "2 GB"
    }

    output {
        File stdout_file = stdout()
    }
}
```

### Task output for STDERR

This example creates a task named `SayHello` that echoes the STDERR content to the task output
file. The WDL **stderr** function captures the STDERR content (in this example, the input string
**Hello World!**) in file **stderr_file**.

Because HealthOmics creates logs for all STDERR content, the output will appear in CloudWatch Logs, along with other STDERR
logging information for the task.

```
version 1.0
 workflow HelloWorld {
    input {
        String message = "Hello, World!"
        String ubuntu_container = "123456789012.dkr.ecr.us-east-1.amazonaws.com/dockerhub/library/ubuntu:20.04"
    }

    call SayHello {
        input:
            message = message,
            container = ubuntu_container
    }

    output {
        File stderr_file = SayHello.stderr_file
    }
}

task SayHello {
    input {
        String message
        String container
    }

    command <<<
        echo "~{message}" >&2
        echo "Current date: $(date)" >&2
        echo "This message was printed to STDERR" >&2
    >>>

    runtime {
        docker: container
        cpu: 1
        memory: "2 GB"
    }

    output {
        File stderr_file = stderr()
    }
}
```

### Task output to a file

In this example, the SayHello task creates two files (message.txt and info.txt) and explicitly declares
these files as the named outputs (message_file and info_file).

```
version 1.0
workflow HelloWorld {
    input {
        String message = "Hello, World!"
        String ubuntu_container = "123456789012.dkr.ecr.us-east-1.amazonaws.com/dockerhub/library/ubuntu:20.04"
    }

    call SayHello {
        input:
            message = message,
            container = ubuntu_container
    }

    output {
        File message_file = SayHello.message_file
        File info_file = SayHello.info_file
    }
}

task SayHello {
    input {
        String message
        String container
    }

    command <<<
        # Create message file
        echo "~{message}" > message.txt

        # Create info file with date and additional information
        echo "Current date: $(date)" > info.txt
        echo "This message was saved to a file" >> info.txt
    >>>

    runtime {
        docker: container
        cpu: 1
        memory: "2 GB"
    }

    output {
        File message_file = "message.txt"
        File info_file = "info.txt"
    }
}
```

### Task output to an array of files

In this example, the `GenerateGreetings` task generates an array of files as the task output. The
task dynamically generates one greeting file for each member of the input array `names`. Because the
file names are not known until runtime, the output definition uses the WDL glob() function to output all files
that match the pattern `*_greeting.txt`.

```
version 1.0
 workflow HelloArray {
    input {
        Array[String] names = ["World", "Friend", "Developer"]
        String ubuntu_container = "123456789012.dkr.ecr.us-east-1.amazonaws.com/dockerhub/library/ubuntu:20.04"
    }

    call GenerateGreetings {
        input:
            names = names,
            container = ubuntu_container
    }

    output {
        Array[File] greeting_files = GenerateGreetings.greeting_files
    }
}

task GenerateGreetings {
    input {
        Array[String] names
        String container
    }

    command  <<<
        # Create a greeting file for each name
        for name in ~{sep=" " names}; do
            echo "Hello, $name!" > ${name}_greeting.txt
        done
    >>>

    runtime {
        docker: container
        cpu: 1
        memory: "2 GB"
    }

    output {
        Array[File] greeting_files = glob("*_greeting.txt")
    }
 }
```

## Task outputs for Nextflow

For workflow definitions written in Nextflow, define a **publishDir** directive to export
task content to your output Amazon S3 bucket. Set the **publishDir** value to
`/mnt/workflow/pubdir`.

For HealthOmics to export files to Amazon S3, the files must be in this directory.

If a task produces a group of output files for use as inputs to a subsequent task, we recommend that you group
these files in a directory and emit the directory as a task output. Enumerating each individual file can result in an I/O
bottleneck in the underlying file system. For example:

```
process my_task {
      ...
      // recommended
      output "output-folder/", emit: output

      // not recommended
      // output "output-folder/**", emit: output
      ...
  }
```

## Task outputs for CWL

For workflow definitions written in CWL, you can specify the task outputs using `CommandLineTool` tasks.
The following sections show examples of `CommandLineTool` tasks that
define different types of outputs.

###### Topics

- [Task output for STDOUT](#task-outputs-cwl-stdout "#task-outputs-cwl-stdout")
- [Task output for STDERR](#task-outputs-cwl-stderr "#task-outputs-cwl-stderr")
- [Task output to a file](#task-outputs-cwl-file "#task-outputs-cwl-file")
- [Task output to an array of files](#task-outputs-cwl-files "#task-outputs-cwl-files")

### Task output for STDOUT

This example creates a `CommandLineTool` task that echoes the STDOUT content to a text output
file named **output.txt**. For example, if you provide the following input, the resulting task output is
**Hello World!** in the **output.txt** file.

```
{
    "message": "Hello World!"
}
```

The `outputs` directive specifies that the output name is **example_out** and it’s
type is `stdout`. For a downstream task to consume the output of this task, it would refer to the
output as `example_out`.

Because HealthOmics creates logs for all STDERR and STDOUT content, the output also appears in CloudWatch Logs, along with
other STDERR logging information for the task.

```
cwlVersion: v1.2
class: CommandLineTool
baseCommand: echo
stdout: output.txt
inputs:
  message:
    type: string
    inputBinding:
      position: 1
outputs:
  example_out:
    type: stdout

requirements:
    DockerRequirement:
        dockerPull: 123456789012.dkr.ecr.us-east-1.amazonaws.com/dockerhub/library/ubuntu:20.04
    ResourceRequirement:
        ramMin: 2048
        coresMin: 1
```

### Task output for STDERR

This example creates a `CommandLineTool` task that echoes the STDERR content to a text output
file named **stderr.txt**. The task modifies the `baseCommand` so that
`echo` writes to STDERR (instead of STDOUT).

The `outputs` directive specifies that the output name is **stderr_out** and it’s
type is `stderr`.

Because HealthOmics creates logs for all STDERR and STDOUT content, the output will appear in CloudWatch Logs, along with
other STDERR logging information for the task.

```
cwlVersion: v1.2
class: CommandLineTool
baseCommand: [bash, -c]
stderr: stderr.txt
inputs:
  message:
    type: string
    inputBinding:
      position: 1
      shellQuote: true
      valueFrom: "echo $(self) >&2"
outputs:
  stderr_out:
    type: stderr

requirements:
    DockerRequirement:
        dockerPull: 123456789012.dkr.ecr.us-east-1.amazonaws.com/dockerhub/library/ubuntu:20.04
    ResourceRequirement:
        ramMin: 2048
        coresMin: 1
```

### Task output to a file

This example creates a `CommandLineTool` task that creates a compressed tar archive from the
input files. You provide the name of the archive as an input parameter (archive_name).

The **outputs** directive specifies that the `archive_file` output type is
`File`, and it uses a reference to the input parameter `archive_name` to bind to the
output file.

```
cwlVersion: v1.2
class: CommandLineTool
baseCommand: [tar, cfz]
inputs:
  archive_name:
    type: string
    inputBinding:
      position: 1
  input_files:
    type: File[]
    inputBinding:
      position: 2

outputs:
  archive_file:
    type: File
    outputBinding:
      glob: "$(inputs.archive_name)"

requirements:
    DockerRequirement:
        dockerPull: 123456789012.dkr.ecr.us-east-1.amazonaws.com/dockerhub/library/ubuntu:20.04
    ResourceRequirement:
        ramMin: 2048
        coresMin: 1
```

### Task output to an array of files

In this example, the `CommandLineTool` task creates an array of files
using the `touch` command. The command uses the strings in the `files-to-create`
input parameter to name the files. The command outputs an array of files. The array includes any
files in the working directory that match the `glob` pattern.
This example uses a wildcard pattern ("\*") that matches all files.

```
cwlVersion: v1.2
class: CommandLineTool
baseCommand: touch
inputs:
  files-to-create:
    type:
      type: array
      items: string
    inputBinding:
      position: 1
outputs:
  output-files:
    type:
      type: array
      items: File
    outputBinding:
      glob: "*"

requirements:
    DockerRequirement:
        dockerPull: 123456789012.dkr.ecr.us-east-1.amazonaws.com/dockerhub/library/ubuntu:20.04
    ResourceRequirement:
        ramMin: 2048
        coresMin: 1
```
