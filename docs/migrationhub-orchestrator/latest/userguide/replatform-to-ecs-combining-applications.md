AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Combining multiple

applications in one container

If you are combining multiple applications from your source server to one container,
there are additional requirements for the workflow. You can specify this option when you
are configuring your workflow for the template **Combine applications in one
container** in [Completing the required
steps](replatform-to-ecs.md#replatform-to-ecs-complete-steps "replatform-to-ecs.md#replatform-to-ecs-complete-steps").

###### Note

If you are replatforming a single application to one container, the following
process is not required.

###### Python script

You can use the following content to create a Python script on your application
server. The script helps you create the required configuration file to containerize
multiple application to one container.

- This script only supports applications running on Linux.
- This script only supports Regions that are enabled by default.

```
import boto3
import json
import tarfile
import os
import subprocess
import shutil
from pathlib import Path
from argparse import ArgumentParser
from urllib.parse import urlparse


ANALYSIS_INFO_JSON = "analysis.json"
CONTAINER_FILES_TAR = "ContainerFiles.tar"
COMBINED_APPLICATION = "CombinedApplication"
TAR_BINARY_PATH = "/usr/bin/tar"

def get_bucket(s3path):
    o = urlparse(s3path, allow_fragments=False)
    return o.netloc

def get_key(s3path):
    o = urlparse(s3path, allow_fragments=False)
    key = o.path

    if key.startswith('/'):
        key = key[1:]

    if not key.endswith('/'):
        key += '/'

    return key

def format_path(path):
    if not path.endswith('/'):
        path += '/'
    return path

def upload_to_s3(s3_output_path, workflow_id, analysis_file, container_file):
    s3 = boto3.client('s3')

    bucket = get_bucket(s3_output_path)
    key = get_key(s3_output_path)

    analysis_object = key + workflow_id + "/" + COMBINED_APPLICATION +  "/" + ANALYSIS_INFO_JSON
    container_object = key + workflow_id + "/" +  COMBINED_APPLICATION + "/" + CONTAINER_FILES_TAR

    s3.upload_file(analysis_file, bucket, analysis_object)
    s3.upload_file(container_file, bucket, container_object)

def download_from_s3(region, s3_paths_list, workspace_s3_download_path):

    s3 = boto3.client('s3')

    dir_number=1
    workspace_s3_download_path = format_path(workspace_s3_download_path)

    for s3_path in s3_paths_list:
        download_path = workspace_s3_download_path + 'd' + str(dir_number)
        dir_number += 1
        Path(download_path).mkdir(parents=True, exist_ok=True)

        bucket = get_bucket(s3_path)
        key = get_key(s3_path)

        analysis_key = key + ANALYSIS_INFO_JSON
        container_files_key = key + CONTAINER_FILES_TAR

        download_analysis_path = download_path + '/' + ANALYSIS_INFO_JSON
        download_container_files_path = download_path + '/' + CONTAINER_FILES_TAR

        s3.download_file(bucket, analysis_key, download_analysis_path)
        s3.download_file(bucket, container_files_key, download_container_files_path)

def get_analysis_data(analysis_json):
    data = ""
    with open(analysis_json) as json_data:
        data = json.load(json_data)
        json_data.close()
    return data

def combine_container_files(workspace_path, count, output_path):
    if not workspace_path.endswith('/'):
        workspace_path += '/'

    for dir_number in range(1, count+1):
        container_files_path = workspace_path + 'd' + str(dir_number)
        container_file_tar = container_files_path + '/' + CONTAINER_FILES_TAR

        extract_tar(container_file_tar, output_path)

def tar_container_files(workspace_path, tar_dir):
    os.chdir(workspace_path)
    subprocess.call([TAR_BINARY_PATH, 'czf', "ContainerFiles.tar", "-C", tar_dir, "."])

def combine_analysis(workspace_path, count, analysis_output_path, script_output_path):
    if not workspace_path.endswith('/'):
        workspace_path += '/'

    #First analysis file is used as a template
    download_path = workspace_path + 'd' + str(1)
    analysis_json = download_path + '/' + ANALYSIS_INFO_JSON
    first_data = get_analysis_data(analysis_json)

    cmd_list = []
    ports_list = []

    for dir_number in range(1, count+1):
        download_path = workspace_path + 'd' + str(dir_number)
        analysis_json = download_path + '/' + ANALYSIS_INFO_JSON
        data = get_analysis_data(analysis_json)

        cmd = data['analysisInfo']['cmdline']
        cmd = " ".join(cmd)
        cmd_list.append(cmd)

        ports = data['analysisInfo']['ports']
        ports_list += ports

    start_script_path = create_startup_script(cmd_list, script_output_path)
    os.chmod(start_script_path, 0o754)

    start_script_filename = '/' + Path(start_script_path).name
    cmd_line_list = [start_script_filename]

    first_data['analysisInfo']['cmdline'] = cmd_line_list
    first_data['analysisInfo']['ports'] = ports_list

    analysis_output_path = format_path(analysis_output_path)
    analysis_output_file = analysis_output_path + '/' + ANALYSIS_INFO_JSON
    write_analysis_json_data(first_data, analysis_output_file)

def write_analysis_json_data(data, output_path):
    with open(output_path, 'w') as f:
        json.dump(data, f)

def create_startup_script(cmd_list, output_path):
    start_script_path = output_path + '/start_script.sh';
    with open (start_script_path, 'w') as rsh:
        rsh.write('#! /bin/bash\n')
        for cmd in cmd_list:
            rsh.write('nohup ' + cmd + ' >> /dev/null 2>&1 &\n')
        rsh.close()
    return start_script_path

def extract_tar(tarFilePath, extractTo):
    os.chdir(extractTo)
    subprocess.call([TAR_BINARY_PATH, 'xvf', tarFilePath])

def validate_args(args):
    MIN_COUNT = 2
    MAX_COUNT = 5
    s3_paths_count = len(args.s3_input_path)
    if (s3_paths_count < MIN_COUNT):
        print("ERROR: input_s3_path needs atleast " + str(MIN_COUNT) +" s3 paths")
        exit(0)

    if (s3_paths_count > MAX_COUNT):
        print("ERROR: Max input_s3_paths is " + str(MAX_COUNT))
        exit(0)


def cleanup_workspace(temp_workspace):
    yes = "YES"
    ack = input("Preparing workspace. Deleting dir and it's contents '" + temp_workspace + "'. Please confirm with 'yes' to procced.\n")
    if (ack.casefold() == yes.casefold()):
        if (os.path.exists(temp_workspace) and os.path.isdir(temp_workspace)):
            shutil.rmtree(temp_workspace)
    else:
        print("Please confirm with 'yes' to continue. Exiting.")
        exit(0)

def main():
    parser = ArgumentParser()
    parser.add_argument('--region', help='Region selected during A2C workflow creation', required=True)
    parser.add_argument('--workflow_id', help='Migration Hub Orchestrator workflowId', required=True)
    parser.add_argument('--s3_output_path', help='S3 output path given while creating the workflow', required=True)
    parser.add_argument('--s3_input_path', nargs='+', help='S3 paths which has application artifacts to combine', required=True)
    parser.add_argument('--temp_workspace', nargs='?', default='/tmp', type=str, help='Temp path for file downloads')
    args = parser.parse_args()

    validate_args(args)

    #prepare workspace
    temp_workspace = format_path(args.temp_workspace)
    temp_workspace += 'mho_workspace'

    #cleanup tmp workspace
    cleanup_workspace(temp_workspace)

    #create workspace directories
    Path(temp_workspace).mkdir(parents=True, exist_ok=True)
    apps_count = len(args.s3_input_path)
    temp_output_container_files = temp_workspace + '/outputs/containerfiles'
    os.makedirs(temp_output_container_files, exist_ok=True)
    temp_workspace_output = temp_workspace + "/outputs"

    #download files
    download_from_s3(args.region, args.s3_input_path, temp_workspace)

    #combine files
    combine_container_files(temp_workspace, apps_count, temp_output_container_files)
    combine_analysis(temp_workspace, apps_count, temp_workspace_output, temp_output_container_files)
    tar_container_files(temp_workspace_output, temp_output_container_files)

    #prepare upload
    analysis_json_file_to_upload = temp_workspace_output + "/" + ANALYSIS_INFO_JSON
    container_files_to_upload = temp_workspace_output + "/" + CONTAINER_FILES_TAR
    upload_to_s3(args.s3_output_path, args.workflow_id, analysis_json_file_to_upload, container_files_to_upload)

if __name__=="__main__":
    main()

```

[Show moreShow less](# "#")###### To run the Python script

1.  Install Python 3.8 or later on your application server. For information on how
    to get the latest version of Python, see the official [Python documentation](https://www.python.org/downloads "https://www.python.org/downloads").
2.  Install AWS SDK for Python (Boto3). For more information, see [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python "https://aws.amazon.com/sdk-for-python").
3.  Configure Boto3 credentials. For more information, see [Credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html").
4.  Run the `combine_applications.py` script while specifying
    values for the following parameters:

        1. **region** – The Region where your
         Amazon S3 bucket is located.
        2. **workflow\_id** – The workflow
         ID.
        3. **s3\_input\_path** – The S3 path
         that has the S3 artifacts uploaded that need to be combined.
        4. **s3\_output\_path** – The output
         path given when creating the workflow.
        5. **temp\_workspace** – The workspace
         directory to use. The default is `/tmp/`.

    The following example demonstrates running the script with the required
    parameters:

```
python3 combine_applications.py --region `us-west-2` \
    --workflow_id `mw-abc123` \
    --s3_output_path s3://`bucket-name`/application-transformation/`mw-abc123`/CombinedApplications \
    --s3_input_path s3://`bucket-name`/application-transformation/`appname1`/ s3://`bucket-name`/application-transformation/`appname2`/
```

Once the script has completed, the application artifacts will be uploaded to Amazon S3 with
a path similar to the following:

```
s3://`bucket-name`/application-transformation/`mw-abc123`/CombinedApplications
```
