

# Step 7: Encrypt data
<a name="encrypt-data"></a>

To perform this step, you must acquire the AWS Clean Rooms collaboration ID and the shared secret key. For more information, see the [Prerequisites](prerequisites.md).

In the following example, we run the encryption on `ads.csv`, using the schema that we created called `ads.json`.

**To encrypt data**

1. Store the shared secret key for the collaboration in [Step 6: Store the shared secret key in an environment variable](store-key.md).

1. From the command line, enter the following command. 

   `java -jar c3r-cli.jar encrypt {{<name of input .csv file>}} --schema={{<name of schema .json file>}} --id={{<collaboration id>}} --output={{<name of output.csv file>}} {{<optional flags>}}`

1. For {{<name of input .csv file>}}, enter the name of the input .csv file.

1. For `schema=`, enter the name of the .json encryption schema file.

1. For `id=`, enter the collaboration ID.

1. For `output=`, enter the name of the output file (for example, `ads-output.csv`).

1. Include any of the command line flags described in [Cryptographic computing parameters](crypto-computing-parameters.md) and [Optional flags in Cryptographic Computing for Clean Rooms](crypto-computing-optional-flags.md).

1. Run the command.

In the example for `ads.csv`, we run the following command.

**java -jar c3r-cli.jar encrypt {{ads.csv}} --schema={{ads.json}} --id={{123e4567-e89b-42d3-a456-556642440000}} --output={{ads-output.csv}}**

In the example for **sales.csv**, we run the following command.

**java -jar c3r-cli.jar encrypt {{sales.csv}} --schema={{sales.json}} --id={{123e4567-e89b-42d3-a456-556642440000}}**

**Note**  
In this example, we don't specify an output file name (`--output={{sales-output.csv}}`). As a result, the default output file name `name-of-file.out.csv` was generated.

You are now ready to verify the encrypted data.