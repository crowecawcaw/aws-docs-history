# Referencing genome files from a workflow definition

An HealthOmics reference store object can be referred to with a URI like the
following. Use your own `account ID`, `reference store ID`, and `reference ID` where indicated.

```
omics://``account ID``.storage.us-west-2.amazonaws.com/``reference store id``/reference/``id``
```

Some workflows will require both the `SOURCE` and `INDEX`
files for the reference genome. The previous URI is the default short form and will
default to the SOURCE file. In order to specify either file, you can use the long
URI form, as follows.

```
omics://``account ID``.storage.us-west-2.amazonaws.com/``reference store id``/reference/``id``/source
omics://``account ID``.storage.us-west-2.amazonaws.com/``reference store id``/reference/``id``/index
```

Using a sequence read set would have a similar pattern, as shown.

```
aws omics create-workflow \
     --name ``workflow name`` \
     --main ``sample workflow.wdl`` \
     --definition-uri omics://``account ID``.storage.us-west-2.amazonaws.com/``sequence_store_id``/readSet/``id`` \
     --parameter-template ``file://parameters_sample_description.json``
```

Some read sets, such as those based on FASTQ, can contain paired reads. In the
following examples, they're referred to as SOURCE1 and SOURCE2. Formats such as BAM
and CRAM will only have a SOURCE1 file. Some read sets will contain INDEX files such
as `bai` or `crai` files. The preceding URI is the default
short form and will default to the SOURCE1 file. To specify the exact file or index,
you can use the long URI form, as follows.

```
omics://123456789012.storage.us-west-2.amazonaws.com/<sequence_store_id>/readSet/<id>/source1
omics://123456789012.storage.us-west-2.amazonaws.com/<sequence_store_id>/readSet/<id>/source2
omics://123456789012.storage.us-west-2.amazonaws.com/<sequence_store_id>/readSet/<id>/index
```

The following is an example of an input JSON file that uses two Omics Storage
URIs.

```
{
   "input_fasta": "omics://123456789012.storage.us-west-2.amazonaws.com/<reference_store_id>/reference/<id>",
   "input_cram": "omics://123456789012.storage.us-west-2.amazonaws.com/<sequence_store_id>/readSet/<id>"
}
```

Reference the input JSON file in the AWS CLI by adding `--inputs
 file://<input_file.json>` to your **start-run**
request.
