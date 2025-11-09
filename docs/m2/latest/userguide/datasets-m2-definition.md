AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Mainframe Modernization data set definition reference

If your application requires more than a few data sets for processing, entering them one
by one in the AWS Mainframe Modernization console is inefficient. Instead, we recommend that you create a JSON file
to specify each data set. Different data set types are specified differently in the JSON,
although many parameters are common. This document describes the details of the JSON
required to import different types of data sets.

###### Note

Before you import any data sets, you must transfer the data sets from the mainframe to
AWS. Data sets must be in a format that can be loaded to the selected runtime engine.
In many cases this can be a sequential file but for Rocket Software(formerly Micro Focus) VSAM it will
need to be in their proprietary format. The `DFCONV` utility is the
suggested method of converting the file. Specify the name of the bucket and folder in
the data set definition JSON file.

For more information on Rocket Software runtime engine, see [DFCONV Batch File Conversion](https://www.microfocus.com/documentation/enterprise-developer/ed70/ED-Eclipse/BKFHFHCONVS001.html "https://www.microfocus.com/documentation/enterprise-developer/ed70/ED-Eclipse/BKFHFHCONVS001.html") in the _Rocket Software_ documentation.

For more information on AWS Blu Age, see [Set up configuration for AWS Blu Age Runtime](ba-runtime-config.md "ba-runtime-config.md").

###### Topics

- [Common properties](#datasets-m2-definition-common "#datasets-m2-definition-common")
- [Sample data set request format for
  VSAM](#datasets-m2-definition-vsam "#datasets-m2-definition-vsam")
- [Sample data set request format for GDG
  base](#datasets-m2-definition-gdg "#datasets-m2-definition-gdg")
- [Sample data set request format for PS or GDG
  generations](#datasets-m2-definition-ps "#datasets-m2-definition-ps")
- [Sample data set request format for
  PO](#datasets-m2-definition-po "#datasets-m2-definition-po")

## Common properties

Several parameters are common to all data sets. These parameters cover the following
areas:

- Information about the data set (`datasetName`,
  `datasetOrg`, `recordLength`,
  `encoding`)
- Information about the location you are importing **from**; that is, the source location of the data set. This is not
  the location on the mainframe. It is the path to the Amazon S3 location where you
  uploaded the data set (`externalLocation`).
- Information about the location you are importing **to**; that is, the target location of the data set. This location
  is either a database or a file system, depending on your runtime engine.
  (`storageType` and `relativePath`).
- Information about the data set type (specific data set type, format, encoding,
  and so on).

Each data set definition has the same JSON structure. The following example JSON shows
all these common parameters.

```
{
    "dataSet": {
        "storageType": "Database",
        "datasetName": "MFI01V.MFIDEMO.BNKACC",
        "relativePath": "DATA",
        "datasetOrg": {
            "`type`": {
                *type-specific properties
 ...*
            },
        },
    },
}
```

The following properties are common to all data sets.

**storageType**

Required. Applies to the **target** location.
Specifies whether the data set is stored in a database or a file system.
Possible values are `Database` or `FileSystem`.

- AWS Blu Age runtime engine: file systems are not supported. You must use
  a database.
- Rocket Software runtime engine: databases and file systems are both
  supported. You can use either Amazon Relational Database Service or Amazon Aurora for databases,
  and Amazon Elastic File System or Amazon FSx for Lustre for file systems.

**datasetName**

(Required) Specifies the fully qualified name of the data set as it
appears on the mainframe.

**relativePath**

(Required) Applies to the **target**
location. Specifies the relative location of the data set in the database or
file system.

**datasetOrg**

(Required) Specifies the type of data set. Possible values are
`vsam`, `gdg`, `ps`, `po`,
or `unknown`.

- AWS Blu Age runtime engine: only VSAM type data sets are
  supported.
- Rocket Software runtime engine: VSAM, GDG, PS, PO, or Unknown type data sets
  are supported.

###### Note

If your application requires files that are not COBOL data
files but are PDF or other binary files, you can specify them as
follows:

```

"datasetOrg": {
            "type": PS {
                "format": U
            },
```

## Sample data set request format for

VSAM

- AWS Blu Age runtime engine: supported.
- Rocket Software runtime engine: supported.

If you are importing VSAM data sets, specify `vsam` as the
`datasetOrg`. Your JSON should resemble the following example:

```
{
    "storageType": "Database",
    "datasetName": "AWS.M2.VSAM.KSDS",
    "relativePath": "DATA",
    "datasetOrg": {
        "vsam": {

            "encoding": "A",
            "format": "KS",
            "primaryKey": {
                "length": 11,
                "offset": 0
            }
        }
    },
    "recordLength": {
        "min": 300,
        "max": 300
    }
},
"externalLocation": {
    "s3Location": "s3://$M2_DATA_STORE/catalog/data/AWS.M2.VSAM.KSDS.DAT"
}
```

The following properties are supported for VSAM data sets.

**encoding**

(Required) Specifies the character set encoding of the data set. Possible
values are ASCII (`A`), EBCDIC (`E`), and Unknown
(`?`).

**format**

(Required) Specifies the VSAM data set type and the record format.

- AWS Blu Age runtime engine: possible values are ESDS (`ES`)
  and KSDS (`KS`). Record format can be fixed or
  variable.
- Rocket Software runtime engine: possible values are ESDS (`ES`),
  KSDS (`KS`), and RRDS (`RR`). The VSAM
  definition includes the record format, so you don't need to specify
  it separately.

**primaryKey**

(Required) Applies to VSAM KSDS data sets only. Specifies the primary key.
Consists of the primary key name, key offset, and key length. The
`name` is optional; `offset` and
`length` are required.

**recordLength**

(Required) Specifies the length of a record. For fixed-length record
formats, these values must match.

- AWS Blu Age runtime engine: for VSAM ESDS, and KSDS, `min` is
  optional and `max` is required.
- Rocket Software runtime engine: `min` and `max` are
  required.

**externalLocation**

(Required) Specifies the **source** location:
that is, the Amazon S3 bucket where you uploaded the data set.

### Blu Age engine-specific

properties

The AWS Blu Age runtime engine supports compression for VSAM data sets. The following
example shows how you can specify this property in JSON.

```
{
    *common properties*
        ...
        "datasetOrg": {
            "vsam": {
                *common properties*
                ...
                "compressed": boolean,
                *common properties*
                ...
            }
        }
}
```

Specify the compression property as follows:

**compression**

(Optional) Specifies whether indexes for this data set are stored as
compressed values. If you have a large data set (typically > 100 Mb),
consider setting this flag to `true`.

## Sample data set request format for GDG

base

- AWS Blu Age runtime engine: not supported.
- Rocket Software runtime engine: supported.

If you are importing GDG base data sets, specify `gdg` as the
`datasetOrg`. Your JSON should resemble the following example:

```
{
    "storageType": "Database",
    "datasetName": "AWS.M2.GDG",
    "relativePath": "DATA",
    "datasetOrg": {
        "gdg": {
            "limit": "3",
            "rollDisposition": "Scratch and No Empty"
        }
    }
}
```

The following properties are supported for GDG base data sets.

**limit**

(Required) Specifies the number of active generations, or biases. For a
GDG base cluster, the maximum is 255.

**rollDisposition**

(Optional) Specifies how to handle generation data sets when the maximum
is reached or exceeded. Possible values are `No Scratch and No
 Empty`, `Scratch and No Empty`, `Scratch and
 Empty`, or `No Scratch and Empty`. The default is
`Scratch and No Empty`.

## Sample data set request format for PS or GDG

generations

- AWS Blu Age runtime engine: not supported.
- Rocket Software runtime engine: supported.

If you are importing PS or GDG generations data sets, specify `ps` as the
`datasetOrg`. Your JSON should resemble the following example:

```
{
    "storageType": "Database",
    "datasetName": "AWS.M2.PS.FB",
    "relativePath": "DATA",
    "datasetOrg": {
        "ps": {
            "format": "FB",
            "encoding": "A"
        }
    },
    "recordLength": {
        "min": 300,
        "max": 300
    }
},
"externalLocation": {
    "s3Location": "s3://$M2_DATA_STORE/catalog/data/AWS.M2.PS.LSEQ"
}
}
```

The following properties are supported for PS or GDG generations data sets.

**format**

(Required) Specifies the format of the data set records. Possible values
are `F`, `FA`, `FB`, `FBA`,
`FBM`, `FBS`, `FM`, `FS`,
`LSEQ`, `U`, `V`, `VA`,
`VB`, `VBA`, `VBM`, `VBS`,
`VM`, and `VS`.

**encoding**

(Required) Specifies the character set encoding of the data set. Possible
values are ASCII (`A`), EBCDIC (`E`), and Unknown
(`?`)

**recordLength**

(Required) Specifies the length of a record. You must specify both the
minimum (`min`) and maximum (`max`) length of the
record. For fixed-length record formats, these values must match.

**externalLocation**

(Required) Specifies the **source** location:
that is, the Amazon S3 bucket where you uploaded the data set.

## Sample data set request format for

PO

If you are importing PO data sets, specify `po` as the
`datasetOrg`. Your JSON should resemble the following example:

```
{
    "storageType": "Database",
    "datasetName": "AWS.M2.PO.PROC",
    "relativePath": "DATA",
    "datasetOrg": {
        "po": {
            "format": "LSEQ",
            "encoding": "A",
            "memberFileExtensions": ["PRC"]
        }
    },
    "recordLength": {
        "min": 80,
        "max": 80
    }
},
"externalLocation": {
    "s3Location": "s3://$M2_DATA_STORE/source/proc/"
}
}
```

The following properties are supported for PO data sets.

**format**

(Required) Specifies the format of the data set records. Possible values
are `F`, `FA`, `FB`, `FBA`,
`FBM`, `FBS`, `FM`, `FS`,
`LSEQ`, `U`, `V`, `VA`,
`VB`, `VBA`, `VBM`, `VBS`,
`VM`, and `VS`.

**encoding**

(Required) Specifies the character set encoding of the data set. Possible
values are ASCII (`A`), EBCDIC (`E`), and Unknown
(`?`).

**memberFileExtensions**

(Required) Specifies an array containing one or more filename extensions,
allowing you to specify which files to be included as PDS member.

**recordLength**

(Optional) Specifies the length of a record. Both the minimum
(`min`) and maximum (`max`) length of the record
are optional. For fixed-length record formats, these values must
match.

**externalLocation**

(Required) Specifies the **source** location:
that is, the Amazon S3 bucket where you uploaded the data set.

###### Note

The current implementation for the Rocket Software runtime engine adds PDS entries as dynamic
data sets.
