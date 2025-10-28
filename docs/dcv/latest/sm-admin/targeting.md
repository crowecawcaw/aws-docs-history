# Using tags to target Amazon DCV servers

You can assign custom tags to Session Manager Agents to help identify and categorize them and the Amazon DCV servers with
which they are associated. When creating a new Amazon DCV session, you can target a group of Amazon DCV servers based on
the tags that are assigned to their respective Agents. For more information about how to target Amazon DCV servers
based on Agent tags, see [CreateSessionRequests](../sm-dev/CreateSessions.md "../sm-dev/CreateSessions.md") in the _Session Manager Developer Guide_.

A tag consists of a tag key and value pair, and you can use any information pair that makes
sense for your use case or environment. You can choose to tag Agents based on their host's
hardware configuration. For example, you can tag all Agents with hosts that have 4 GB of
memory with `ram=4GB`. Or you can tag Agents based on purpose. For example, you
can tag all Agents running on production hosts with `purpose=production`.

###### To assign tags to an Agent

1. Using your preferred text editor, create a new file and give it a descriptive name, for
   example `agent_tags.toml`. The file type must be `.toml`, and
   the file contents must be specified in the TOML file format.
2. In the file, add each new tag key and value pair on a new line using the
   `key=value` format. For example:

```
tag1="abc"
tag2="xyz"
```

3. Open the Agent configuration file (`/etc/dcv-session-manager-agent/agent.conf`
   for Linux or `C:\Program Files\NICE\DCVSessionManagerAgent\conf\agent.conf` for Windows). For `tags_folder`, and
   specify the path to the directory in which the tag file is located.

If the directory contains multiple tag files, all of the tags defined across the files apply the Agent.
The files are read in alphabetical order. If multiple files contain a tag with the same key, the value
is overwritten with the value from the last read file. 4. Save and close the file. 5. Stop and restart the Agent.

    * Windows



    ```
    `C:\>` sc stop DcvSessionManagerAgentService
    ```


    ```
    `C:\>` sc start DcvSessionManagerAgentService
    ```
    * Linux



    ```
    `$` sudo systemctl stop dcv-session-manager-agent
    ```


    ```
    `$` sudo systemctl start dcv-session-manager-agent
    ```
