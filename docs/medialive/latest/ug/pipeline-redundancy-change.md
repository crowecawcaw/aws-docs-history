# Changing pipeline redundancy in an existing

channel

To enable or disable pipeline redundancy on an existing MediaLive channel, you must update
the channel class.

## Changing the channel to a

single-pipeline channel

You can change a standard channel to single-pipeline, to remove one of the
pipelines in the channel and to remove pipeline redundancy.

To change the channel class, the channel must be idle (not running).

###### To change the channel class to a single-pipeline channel

1.  On the **Channels** page, choose the channel. (Don't
    choose the channel name.)
2.  On the menu, choose **Actions**, then choose
    **Other channel actions**, then choose **Update
    channel class to SINGLE_PIPELINE**.
3.  In the dialog box, choose **Confirm**. MediaLive performs the
    following actions:

        * It removes the second pipeline (pipeline 1) in the channel.
        * It removes the second destination address in each output
         group.
        * It *doesn't* remove the second
         endpoint on the inputs. The inputs aren't changed in any way.
         Instead, when you restart the channel, MediaLive simply ignores the
         second endpoint.

    While MediaLive is performing these actions, the channel has a status of
    **UPDATING**. When the update is completed, the status
    changes to **IDLE**.

4.  You might want to notify the upstream system for each push input that it
    no longer needs to push input to the second endpoint. You also might want to
    notify the downstream system for each output group that it should no longer
    expect output at its second destination.

## Changing the channel class to standard –

option A

You can change a single-pipeline channel to a standard channel. Follow this
procedure if you originally set up the single-pipeline channel with [standard-class inputs and upgrade
potential](single-channel-upgrade.md "single-channel-upgrade.md").

Perform these steps:

1. Arrange with your upstream systems to start sending two instances of the
   source content.
2. [Stop the
   channel](starting-stopping-deleting-a-channel.md "starting-stopping-deleting-a-channel.md").
3. Change the channel class to standard class. See the steps after this
   list.

You have now upgraded the channel from a single-pipeline channel with
standard-class inputs to a standard channel with standard-class
inputs. 4. [Restart the
channel](starting-stopping-deleting-a-channel.md "starting-stopping-deleting-a-channel.md").

###### To change the channel class

1. Obtain a second destination address for each output group. Each address is
   at the downstream system of each output group.

For example, if the channel has an HLS output group (with an HTTPS server
as its downstream system) and an Archive output group (with an Amazon S3 bucket
as its downstream system), you must enter the URL to a new destination
address at the HTTPS server, and the URL to a new folder in the Amazon S3
bucket.

Plan these destinations now, in the same way as you planned the
destination addresses when you originally set up the channel. For more
information, see [Setup: Creating output groups and outputs](medialive-outputs.md "medialive-outputs.md"), and read the
information about coordinating for the type of output group that you are
creating. 2. On the **Channels** page, choose the channel. (Don't
choose the channel name.) 3. On the menu, choose **Actions**, **Other channel
actions**, **Update channel class to
STANDARD**. 4. In the dialog box, choose **Confirm**. 5. On the **Update channel class to Standard** page, enter
the destination addresses that you identified in step 1. There is one field
for each output group in the channel. 6. Choose **Submit**. MediaLive updates the channel and creates
a new pipeline called pipeline 1. The source for this pipeline is the
previously dormant URL. When you start the channel, MediaLive ingests content
from that URL, produces output, and sends the output to the new destinations
in every output group.

## Changing the class—option B

When you originally created the channel, might have been sure that you wouldn't
need to convert the channel, to a standard channel. Therefore, you [set up the channel](single-pipeline-no-upgrade.md "single-pipeline-no-upgrade.md") as a
single-pipeline channel with single-class inputs.

You might now decide that you do need to change the channel to a standard channel.
You can do so, but notice that the procedure involves detaching, upgrading, and edit
the inputs, as well as upgrading the channel.

Perform these steps:

1. Arrange with your upstream systems to start sending two instances of the
   source content.
2. [Stop the
   channel](starting-stopping-deleting-a-channel.md "starting-stopping-deleting-a-channel.md").
3. Detach each single-class input. To detach the inputs, you must [edit the channel](editing-deleting-channel.md "editing-deleting-channel.md") and remove
   the attached inputs.
4. [Edit each input](edit-input.md "edit-input.md") to convert it to
   standard class, and to add a second source.
5. Edit the channel to change the channel class to standard class. See the
   steps after this list.
6. [Edit the channel](editing-deleting-channel.md "editing-deleting-channel.md") to
   reattach each input.

You have now upgraded the channel from a single-pipeline channel with
single-class inputs to a standard channel with standard-class inputs. 7. [Restart the
channel](starting-stopping-deleting-a-channel.md "starting-stopping-deleting-a-channel.md").

###### To change the channel class

1. Obtain a second destination address for each output group. Each address is
   at the downstream systems of each output group.

For example, if the channel has an HLS output group (with an HTTPS server
as its downstream system) and an Archive output group (with an Amazon S3 bucket
as its downstream system), you must enter the URL to a new destination
address at the HTTPS server, and the URL to a new folder in the Amazon S3
bucket.

Plan these destinations now, in the same way as you planned the
destination addresses when you originally set up the channel. You might need
to contact the owner of each downstream system. 2. Edit the URLs in every single-class input to include a second URL, for the
second source that will provide content to the newly added pipeline.

    * For a push input, [edit the input](edit-input.md "edit-input.md")
     to include an address for the second input source. Give that address
     to the owner of the upstream system, so that they can push source
     content to that address. You should also find out from the upstream
     system the address that the new source will be pushed from. Make
     sure that this address is covered by the input security group for
     the channel.


    * For a pull input, obtain a new address from the owner of the
     downstream system. [Edit the input](edit-input.md "edit-input.md")
     to include that address. After the second pipeline is created, MediaLive
     will be able to pull the second source content (for the second
     pipeline).

3. On the **Channels** page, choose the channel. (Don't
   choose the channel name.)
4. On the menu, choose **Actions**, **Other channel
   actions**, **Update channel class to
   STANDARD**.
5. In the dialog box, choose **Confirm**.
6. On the **Update channel class to STANDARD** page, enter
   the destination addresses that you identified in step 1. There is one field
   for each output group in the channel.
7. Choose **Submit**. MediaLive updates the channel and creates
   a new pipeline called pipeline 1. When you start the channel, MediaLive sends
   the output from this pipeline to the new destinations in every output group.
