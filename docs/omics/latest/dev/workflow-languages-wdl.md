# WDL workflow definition specifics

The following topics provide details about types and directives available for WDL workflow definitions in
HealthOmics.

###### Topics

- [Implicit type conversion in WDL lenient](#workflow-wdl-type-conversion "#workflow-wdl-type-conversion")
- [Namespace definition in input.json](#workflow-wdl-namespace-defn "#workflow-wdl-namespace-defn")
- [Primitive types in WDL](#workflow-wdl-primitive-types "#workflow-wdl-primitive-types")
- [Complex types in WDL](#workflow-wdl-complex-types "#workflow-wdl-complex-types")
- [Directives in WDL](#workflow-wdl-directives "#workflow-wdl-directives")
- [Task metadata in WDL](#workflow-wdl-task-metadata "#workflow-wdl-task-metadata")
- [WDL workflow definition example](#wdl-example "#wdl-example")

## Implicit type conversion in WDL lenient

HealthOmics supports implicit type conversion in the input.json file and the workflow definition.
To use implicit type casting, specify the workflow engine as WDL lenient when you create the workflow.
WDL lenient is designed to handle workflows migrated from Cromwell. It supports customer Cromwell
directives and some non-conformant logic.

WDL lenient supports type conversion for the following items in the list of WDL’s [limited exceptions](https://github.com/openwdl/wdl/blob/wdl-1.2/SPEC.md#-limited-exceptions "https://github.com/openwdl/wdl/blob/wdl-1.2/SPEC.md#-limited-exceptions"):

- Float to Int, where the coercion results in no loss of precision (such as 1.0 maps to 1).
- String to Int/Float, where the coercion results in no loss of precision.
- Map[W, X] to Array[Pair[Y, Z]], in the case where W is coercible to Y and X is coercible to Z.
- Array[Pair[W, X]] to Map[Y, Z], in the case where W is coercible to Y and X is coercible to Z (such as 1.0
  maps to 1).

To use implicit type casting, specify the workflow engine as WDL_LENIENT when you create the workflow or
workflow version.

In the console, the workflow engine parameter is named **Language**.
In the API, the workflow engine parameter is named **engine**.
For more information, see [Create a private workflow](create-private-workflow.md "create-private-workflow.md") or
[Create a workflow version](workflows-version-create.md "workflows-version-create.md").

## Namespace definition in input.json

HealthOmics supports fully qualified variables in input.json. For example, if you declare two input variables
named number1 and number2 in workflow **SumWorkflow**:

```
workflow SumWorkflow {
  input {
    Int number1
    Int number2
  }
}
```

You can use them as fully qualified variables in input.json:

```
{
    "SumWorkflow.number1": 15,
    "SumWorkflow.number2": 27
}
```

## Primitive types in WDL

The following table shows how inputs in WDL map to the matching primitive types. HealthOmics provides limited support
for type coercion, so we recommend that you set explicit types.

| Primitive types | WDL type  | JSON type     | Example WDL                                     | Example JSON key and value                                                                                                                                                                                                                                                                                                                                                                   | Notes |
| --------------- | --------- | ------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `Boolean`       | `boolean` | `Boolean b`   | `"b": true`                                     | The value must be lower case and unquoted.                                                                                                                                                                                                                                                                                                                                                   |
| `Int`           | `integer` | `Int i`       | `"i": 7`                                        | Must be unquoted.                                                                                                                                                                                                                                                                                                                                                                            |
| `Float`         | `number`  | `Float f`     | `"f": 42.2`                                     | Must be unquoted.                                                                                                                                                                                                                                                                                                                                                                            |
| `String`        | `string`  | `String s`    | `"s": "characters"`                             | JSON strings that are a URI must be mapped to a WDL file to be<br>imported.                                                                                                                                                                                                                                                                                                                  |
| `File`          | `string`  | `File f`      | `"f": "s3://amzn-s3-demo-bucket1/path/to/file"` | Amazon S3 and HealthOmics storage URIs are imported as long as the IAM<br>role provided for the workflow has read access to these objects. No<br>other URI schemes are supported (such as `file://`,<br>`https://`, and `ftp://`). The URI must<br>specify an object. It cannot be a directory meaning it can not end with<br>a `/`.                                                         |
| `Directory`     | `string`  | `Directory d` | `"d": "s3://bucket/path/"`                      | The `Directory` type isn't included in WDL 1.0 or 1.1, so<br>you will need to add `version development` to the header of<br>the WDL file. The URI must be a Amazon S3 URI and with a prefix that ends<br>with a '/'. All contents of the directory will be recursively copied to<br>the workflow as a single download. The `Directory` should<br>only contain files related to the workflow. |

## Complex types in WDL

The following table show how inputs in WDL map to the matching complex JSON types.
Complex types in WDL are data structures comprised of primitive types. Data structures
such as lists will be converted to arrays.

| Complex types | WDL type | JSON type                                                                                                               | Example WDL                                                                                                                                                             | Example JSON key and value                                                                                                                                | Notes |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `Array`       | `array`  | `Array[Int] nums`                                                                                                       | `“nums": [1, 2, 3]`                                                                                                                                                     | The members of the array must follow the format of the WDL array<br>type.                                                                                 |
| `Pair`        | `object` | `Pair[String, Int] str_to_i`                                                                                            | `“str_to_i": {"left": "0", "right": 1}`                                                                                                                                 | Each value of the pair must use the JSON format of its matching WDL<br>type.                                                                              |
| `Map`         | `object` | `Map[Int, String] int_to_string`                                                                                        | `"int_to_string": { 2: "hello", 1: "goodbye" }`                                                                                                                         | Each entry in the map must use the JSON format of its matching WDL<br>type.                                                                               |
| `Struct`      | `object` | `<br>struct SampleBamAndIndex {<br>String sample_name<br>File bam<br>File bam_index<br>} SampleBamAndIndex b_and_i<br>` | `<br>"b_and_i": {<br>"sample_name": "NA12878",<br>"bam": "s3://amzn-s3-demo-bucket1/NA12878.bam",<br>"bam_index": "s3://amzn-s3-demo-bucket1/NA12878.bam.bai"<br>}<br>` | The names of the struct members must exactly match the names of the<br>JSON object keys. Each value must use the JSON format of the matching<br>WDL type. |
| `Object`      | N/A      | N/A                                                                                                                     | N/A                                                                                                                                                                     | The WDL `Object` type is outdated and should be replaced<br>by `Struct` in all cases.                                                                     |

## Directives in WDL

HealthOmics supports the following directives in all WDL versions that HealthOmics supports.

### Configure GPU resources

HealthOmics supports runtime attributes **acceleratorType** and **acceleratorCount**
with all supported [GPU
instances](task-accelerators.md "task-accelerators.md"). HealthOmics also supports aliases named **gpuType** and
**gpuCount**, which have the same functionality as their accelerator counterparts. If the WDL
definition contains both directives, HealthOmics uses the accelerator values.

The following example shows how to use these directives:

```
runtime {
    gpuCount: 2
    gpuType: "nvidia-tesla-t4"
}
```

### Configure task retry for service errors

HealthOmics supports up to two retries for a task that failed because of service errors (5XX HTTP status codes).
You can configure the maximum number of retries (1 or 2) and you can opt out of retries for service errors. By
default, HealthOmics attempts a maximum of two retries.

The following example sets `preemptible` to opt out of retries for service errors:

```
{
  preemptible: 0
}
```

For more information about task retries in HealthOmics, see [Task Retries](monitoring-runs.md#run-status-task-retries "monitoring-runs.md#run-status-task-retries").

### Configure task retry for out of memory

HealthOmics supports retries for a task that failed because it ran out of memory (container exit code 137, 4XX HTTP
status code). HealthOmics doubles the amount of memory for each retry attempt.

By default, HealthOmics doesn't retry for this type of failure. Use the `maxRetries` directive to
specify the maximum number of retries.

The following example sets `maxRetries` to 3, so that HealthOmics attempts a maximum of four attempts to
complete the task (the initial attempt plus three retries):

```
runtime {
    maxRetries: 3
}
```

###### Note

Task retry for out of memory requires GNU findutils 4.2.3+. The default HealthOmics image container includes this
package. If you specify a custom image in your WDL definition, make sure that the image includes GNU findutils
4.2.3+.

### Configure return codes

The **returnCodes** attribute provides a mechanism to specify a return code, or a set of
return codes, that indicates a successful execution of a task. The WDL engine honors the return codes that you
specify in the **runtime** section of the WDL definition, and sets the tasks status
accordingly.

```
runtime {
    returnCodes: 1
}
```

HealthOmics also supports an alias named **continueOnReturnCode**, which has
the same capabilities as **returnCodes**. If you specify both attributes, HealthOmics uses the
**returnCodes** value.

## Task metadata in WDL

HealthOmics supports the following metadata options for WDL tasks.

### Disable task-level caching with the volatile attribute

The **volatile** attribute allows you to disable call caching for specific tasks in your WDL workflow.
When a task is marked as volatile, it will always execute and never use cached results, even when caching is enabled for the run.

Add the **volatile** attribute to the **meta** section of your task definition:

```
task my_volatile_task {
    meta {
        volatile: true
    }

    input {
        String input_file
    }

    command {
        echo "Processing ${input_file}" > output.txt
    }

    output {
        File result = "output.txt"
    }
}
```

## WDL workflow definition example

The following examples show private workflow definitions for converting from
`CRAM` to `BAM` in WDL. The `CRAM` to
`BAM` workflow defines two tasks and uses tools from the
`genomes-in-the-cloud` container, which is shown in the example and is
publicly available.

The following example shows how to include the Amazon ECR container as a parameter. This allows HealthOmics to verify the
access permissions to your container before it starts the run the run.

```
{
   ...
   "gotc_docker":"<account_id>.dkr.ecr.<region>.amazonaws.com/genomes-in-the-cloud:2.4.7-1603303710"
}
```

The following example shows how to specify which files to use in your run, when the files are in an Amazon S3
bucket.

```
{
    "input_cram": "s3://amzn-s3-demo-bucket1/inputs/NA12878.cram",
    "ref_dict": "s3://amzn-s3-demo-bucket1/inputs/Homo_sapiens_assembly38.dict",
    "ref_fasta": "s3://amzn-s3-demo-bucket1/inputs/Homo_sapiens_assembly38.fasta",
    "ref_fasta_index": "s3://amzn-s3-demo-bucket1/inputs/Homo_sapiens_assembly38.fasta.fai",
    "sample_name": "NA12878"
}
```

If you want to specify files from a sequence store, indicate that as shown in the
following example, using the URI for the sequence store.

```
{
    "input_cram": "omics://429915189008.storage.us-west-2.amazonaws.com/111122223333/readSet/4500843795/source1",
    "ref_dict": "s3://amzn-s3-demo-bucket1/inputs/Homo_sapiens_assembly38.dict",
    "ref_fasta": "s3://amzn-s3-demo-bucket1/inputs/Homo_sapiens_assembly38.fasta",
    "ref_fasta_index": "s3://amzn-s3-demo-bucket1/inputs/Homo_sapiens_assembly38.fasta.fai",
    "sample_name": "NA12878"
}
```

You can then define your workflow in WDL as shown in the following example.

```
 version 1.0
workflow CramToBamFlow {
    input {
        File ref_fasta
        File ref_fasta_index
        File ref_dict
        File input_cram
        String sample_name
        String gotc_docker = "<account>.dkr.ecr.us-west-2.amazonaws.com/genomes-in-the-
cloud:latest"
    }
    #Converts CRAM to SAM to BAM and makes BAI.
    call CramToBamTask{
         input:
            ref_fasta = ref_fasta,
            ref_fasta_index = ref_fasta_index,
            ref_dict = ref_dict,
            input_cram = input_cram,
            sample_name = sample_name,
            docker_image = gotc_docker,
     }
     #Validates Bam.
     call ValidateSamFile{
        input:
           input_bam = CramToBamTask.outputBam,
           docker_image = gotc_docker,
     }
     #Outputs Bam, Bai, and validation report to the FireCloud data model.
     output {
         File outputBam = CramToBamTask.outputBam
         File outputBai = CramToBamTask.outputBai
         File validation_report = ValidateSamFile.report
      }
}
#Task definitions.
task CramToBamTask {
    input {
       # Command parameters
       File ref_fasta
       File ref_fasta_index
       File ref_dict
       File input_cram
       String sample_name
       # Runtime parameters
       String docker_image
    }
   #Calls samtools view to do the conversion.
   command {
       set -eo pipefail

       samtools view -h -T ~{ref_fasta} ~{input_cram} |
       samtools view -b -o ~{sample_name}.bam -
       samtools index -b ~{sample_name}.bam
       mv ~{sample_name}.bam.bai ~{sample_name}.bai
    }

    #Runtime attributes:
    runtime {
        docker: docker_image
    }

    #Outputs a BAM and BAI with the same sample name
     output {
         File outputBam = "~{sample_name}.bam"
         File outputBai = "~{sample_name}.bai"
    }
}

#Validates BAM output to ensure it wasn't corrupted during the file conversion.
task ValidateSamFile {
   input {
      File input_bam
      Int machine_mem_size = 4
      String docker_image
   }
   String output_name = basename(input_bam, ".bam") + ".validation_report"
   Int command_mem_size = machine_mem_size - 1
   command {
       java -Xmx~{command_mem_size}G -jar /usr/gitc/picard.jar \
       ValidateSamFile \
       INPUT=~{input_bam} \
       OUTPUT=~{output_name} \
       MODE=SUMMARY \
       IS_BISULFITE_SEQUENCED=false
    }
    runtime {
    docker: docker_image
    }
   #A text file is generated that lists errors or warnings that apply.
    output {
        File report = "~{output_name}"
    }
}
```
