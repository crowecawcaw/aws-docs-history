

# Essential notes for version 2.25 and 3.25
<a name="rn-2-25-essential"></a>

Read these essential notes before you upgrade. Except where noted, each note applies to both Conductor Live and the worker nodes (Elemental Live and Statmux).

## Last minor release of the 2.25 and 3.25 major version
<a name="rn-2-25-essential-last-minor-release"></a>

Versions 2.25.9 and 3.25.9 are the last versions planned for the 2.25 (3.25) major version. We strongly recommend that you upgrade to version 2.26 and 3.26 as soon as possible. Read the release notes for [Release notes for version 2.26 and 3.26](rn-2-26.md) and later versions.

## Change to cluster management 3.25.3
<a name="rn-2-25-essential-cluster-management"></a>

In the release notes for version 3.25.2 of Conductor Live and 2.25.2 of the worker nodes (Elemental Live and Statmux), we described a change to the rules for node recruitment and software downgrades. The change affected these actions when they involve "crossing over the x.25.2 boundary". You cross the boundary when you:
+ Recruit a worker node with version 2.25.2 (or higher) into a cluster where the Conductor Live node is running a version lower than 2.25.2.
+ Downgrade from a version x.25.2 (or higher) to a version below x.25.2.

In version 3.25.3 and 2.25.3, we are now introducing improvements that mean it is no longer necessary to follow those rules.

If you haven't yet recruited or downgraded in the way described in those release notes, then do not follow the procedures in those release notes when you recruit or downgrade. Instead, follow these new procedures.

### Recruiting worker nodes
<a name="rn-2-25-essential-cluster-recruiting"></a>

You might want to recruit a new worker node into a cluster where the nodes are running software versions lower than x.25.2. You might not want to upgrade the cluster yet, but you want to add the new nodes immediately. Follow this procedure:

1. Obtain the new worker node (it is delivered with version 2.25.3 or later installed). Or locate a node that you already have and upgrade the version to 2.25.3 or later.

1. Set the following environment variable to `True`: `LEGACY_RECRUIT`.

1. Recruit the new worker node into the cluster as described in the [AWS Elemental Conductor Live Configuration Guide](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/).

### Recruiting worker nodes after you have crossed the boundary
<a name="rn-2-25-essential-cluster-recruiting-crossed"></a>

Eventually, you will upgrade the Conductor Live nodes and will "cross the boundary". The worker nodes that have `LEGACY_RECRUIT` set to true will determine that Conductor Live has crossed the boundary, and will ignore the value of the environment variable. You don't need to set the environment variable to `False` on these nodes.

### Downgrading nodes
<a name="rn-2-25-essential-cluster-downgrading"></a>

You might have upgraded all the Conductor Live and worker nodes to the high side of the boundary. For example:
+ The Conductor Live nodes are running version 3.25.2.
+ The worker nodes are running 2.26.0.

You might want to downgrade the worker nodes to the low side of the boundary, for example, to version 2.25.0. In version x.25.2 (but only in that version), there was a rule that both the Conductor Live software versions and the worker software versions must be on the same side of the boundary.

With version x.25.3 and later, this rule no longer exists. But keep in mind the existing rule that the Conductor Live and worker nodes can run different versions, as long as the Conductor Live nodes aren't running a higher version than the worker nodes.

## K80 GPU is no longer supported
<a name="rn-2-25-essential-k80-gpu"></a>

This note applies to Elemental Live appliances.

Starting with the 2.25.0 GA software release, all Group 3 Elemental Live appliances containing an NVIDIA K80 GPU are no longer supported by new Elemental Live software releases.

All Group 3 AWS Elemental Live appliances containing a K80 GPU reached End of Life (EOL) status on December 31, 2020.

If you try to upgrade one of these appliances to version 2.25.0 or later, an error message appears and the installation stops. The encoder retains its current version of software. It can be restarted and operated as before with the software version it had active.

To determine the GPU on any Elemental Live appliance, log in and run the following command:

```
sudo nvidia-smi -q | grep Product
```

If your AWS Elemental appliance has a GPU, you see the GPU details. If your appliance does not have a GPU, you get a message saying command not found.