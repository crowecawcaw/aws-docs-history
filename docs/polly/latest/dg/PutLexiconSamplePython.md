# PutLexicon

The following code sample show how to use Python (boto3)-based applications to
store a pronunciation lexicon in an AWS Region.

For more information on this operation, see the reference for the [`PutLexicon`](API_PutLexicon.md "API_PutLexicon.md")
API.

Note the following:

- You need to update the code by providing a local lexicon file name and
  a stored lexicon name.
- The example assumes you have lexicon files created in a subdirectory
  called `pls`. You need to update the path as
  appropriate.
  The following code example uses default credentials stored in the AWS SDK
  configuration file. For information about creating the configuration file, see
  [Setting up the AWS CLI](setup-cli.md "setup-cli.md").

For more information on this operation, see the reference for the [`PutLexicon`](API_PutLexicon.md "API_PutLexicon.md")
API.

```
from argparse import ArgumentParser

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError

# Define and parse the command line arguments
cli = ArgumentParser(description="PutLexicon example")
cli.add_argument("path", type=str, metavar="FILE_PATH")
cli.add_argument("-n", "--name", type=str, required=True,
                 metavar="LEXICON_NAME", dest="name")
arguments = cli.parse_args()

# Create a client using the credentials and region defined in the adminuser
# section of the AWS credentials and configuration files
session = Session(profile_name="adminuser")
polly = session.client("polly")

# Open the PLS lexicon file for reading
try:
    with open(arguments.path, "r") as lexicon_file:
        # Read the pls file contents
        lexicon_data = lexicon_file.read()

        # Store the PLS lexicon on the service.
        # If a lexicon with that name already exists,
        # its contents will be updated
        response = polly.put_lexicon(Name=arguments.name,
                                      Content=lexicon_data)
except (IOError, BotoCoreError, ClientError) as error:
    # Could not open/read the file or the service returned an error,
    # exit gracefully
    cli.error(error)

print(u"The \"{0}\" lexicon is now available for use.".format(arguments.name))
```
