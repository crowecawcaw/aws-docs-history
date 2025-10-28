End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# AWS SimSpace Weaver version 1.17.0

This release is an overhaul of the SimSpace Weaver app SDK distributable package.
We replaced outdated Windows batch and Linux Bash scripts with Python-based scripts.

###### Important

Python 3.9 is now a requirement to use the scripts and samples, not just for the Python SDK.

###### Contents

- [Major changes for 1.17.0](service-versions_1-17-0.md#service-versions_1-17-0_changelog "service-versions_1-17-0.md#service-versions_1-17-0_changelog")
- [Update a project to 1.17.0](service-versions_1-17-0.md#service-versions_1-17-0_update-project "service-versions_1-17-0.md#service-versions_1-17-0_update-project")
- [Frequently asked questions about version 1.17.0](service-versions_1-17-0.md#service-versions_1-17-0_faq "service-versions_1-17-0.md#service-versions_1-17-0_faq")

## Major changes for 1.17.0

- Simplified project creation
  - After running `setup.py`, you can create your own project by simply copy-pasting a sample.

- 1-click samples
  - The distribution zip file now contains ready-to-use samples that work after setting up the distribution.

- Each SDK now exists in its own directory: `cpp`, `python`, `unreal`, and `unity`. You might have to update your paths depending on which SDK you use.
- Improvements to helper scripts.
  - Scripts now contain multiple AWS CLI options to maximize their flexibility.
  - Integrated console client launch and connection as part of quick-start.
  - Improved console output.
  - Unreal and Unity sample building now works with `quick-start`, no more manual steps required.
  - SimSpace Weaver Local now works by just calling `quick-start`, no more manual building and launching.
  - SimSpace Weaver Local `quick-start` has integrated support for logging app output.
  - SimSpace Weaver Local can now be launched in a non-GUI environment, such as in an ssh session.
  - The "custom container" feature is now integrated into the `quick-start` script.
  - Increased Amazon Linux 2 (AL2) support: script workflows for Windows and AL2 are now comparable. Previously, AL2 projects required more manual steps and SimSpace Weaver Local wasn't supported for AL2.

- Unreal Engine and Unity plugins are now included as part of the SimSpace Weaver app SDK distributable package.
- Bug fixes for SimSpace Weaver Local
  - Fixed a bug where entities could be assigned the same entity ID.
  - Fixed a bug where two partitions could be assigned the same partition ID.
  - Fixed a bug related to apps attempt to write to entities they did not own.
  - Resolved a memory leak issue.

## Update a project to 1.17.0

1. Setup the 1.17.0 distribution: Go through the setup procedures again because we changed them for 1.17.0. For more information, see [Setting up for SimSpace Weaver](setting-up.md "setting-up.md").
2. Each Weaver App SDK now exists in it’s own directory. Update your build paths to reflect this.
   1. C++ directory: `SimSpaceWeaverAppSdk/cpp`
      - The SimSpace Weaver C++ app SDK now uses a `FindSimSpaceWeaverAppSdk.cmake` file. This file sets up a `weaver` target that gets linked to, and includes important bug fixes when building for Weaver in the AWS Cloud. You should use this instead of linking to the binaries directly.

   2. Python directory: `SimSpaceWeaverAppSdk/python`
   3. Unity plugin: `SimSpaceWeaverAppSdk/unity`
   4. Unreal Engine plugin: `SimSpaceWeaverAppSdk/unreal`

3. The previous `tools` scripts will not work with the new SimSpace Weaver distribution. To use the new `tools` scripts with your project:
   1. Delete your old `tools/windows`, `tools/linux`, and `tools/local` directories.
   2. Copy the `tools` directory of a sample project that uses the same SimSpace Weaver app SDK as your project. Be sure you have run `setup.py` **_before_** you copy this directory.

###### Important

The tools scripts are only guaranteed to work with the sample projects. You might have to edit these scripts, especially the `build.py` script, to work with your project. Any edits will be unique to your project therefore we can't provide any guidance.

## Frequently asked questions about version 1.17.0

###### Do I have to update to version 1.17.0?

This isn't a required update because there are no changes to the SimSpace Weaver API or SimSpace Weaver app SDK. You must update to 1.17.0 if you want to use the 1.17.0 SimSpace Weaver Local, which contains several bug fixes.

###### What is the minimum Python version required?

Python 3.9 is the minimum version.

###### What is the minimum CMake version required?

CMake version 3.13 is the minimum.

###### What is the minimum version of Unreal Engine required?

Unreal Engine 5.0 is the minimum.

###### What is the minimum version of Unity required?

Unity version 2022.3.19.F1 is the minimum.
