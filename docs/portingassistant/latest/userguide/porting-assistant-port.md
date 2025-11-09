AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer be open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Port a solution

You can port a project using the assessment tool or the CLI console application.

## Port a solution using the assessment

tool

To port a solution using the assessment tool, perform the following steps:

1. From the main page of Porting Assistant for .NET, choose **Get
   started**.
2. On the **Edit settings** page, choose the target .NET
   framework and AWS named profile to allow Porting Assistant to assess your
   solution. You can also add the AWS named profile using the [AWS CLI](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md").
3. From the main page of the assessment tool, select **Assessed
   solutions** from the left navigation pane.
4. On the **Assessed Solutions** page, select a solutions
   file. You will be directed to the**Assessment overview**
   page.
5. Under the **Projects** tab, select the project you want
   to port. Choose **Port project**. The Porting Assistant
   will ask how you want to save your ported project. Select whether you want
   to copy the ported project to a new location or modify the project in place.

###### Note

The project is ported to the version used in the assessment. If you
want to port to a different version, you must reassess the project after
changing the version in your settings.

After you select the destination folder and choose
**Save**, or select to modify the project file in
place, you will be directed to the **Port projects**
page. 6. Porting Assistant begins to port the new solution, and you are directed to
the **Assessment overview** page. The status of the port
appears at the top of the page. You can view the port status of a package by
selecting it on the **Assessment overview** page and
looking at the **Port status** in the overview
section.

###### Important

When you port a solution, your project files and code are modified. Your
project file is modified to include compatible packages you selected and other
packages detected by the assessment. In addition, Porting Assistant adds or
backs up code files based on the type of projects detected. Some code files are
changed to make them more compatible with .NET Core. The result is not a
completely ported project. The project may not build, and additional source code
changes may be required. Any added or modified code must be verified and tested
before it can be considered production ready.

## Port a solution using the Porting Assistant CLI

console application

You can port a solution using the Porting Assistant CLI console application. The CLI is
packaged with the Porting Assistant for .NET tool. After you install the Porting Assistant for .NET tool, the CLI can be found
in the following location:
`C:\Users\`<user_name>`\AppData\Local\Programs\Porting
 Assistant for
 .NET\resources\netcore_build\PortingAssistant.Client.CLI.exe`.

The following parameters can be defined when you port a solution using the
Porting Assistant CLI console application:

- `--solution-path (-s)`

**Definition**: The path to your solution
file

**Required**: Yes

- `--output-path (-o)`

**Definition**: The path where the assessment
JSON file is stored.

**Required**: Yes

- `--target (-t)`

**Definition**: The .NET version to use for
the assessment.

**Required**: No

**Options**:

    + `netcore3.1`
    + `net5.0`
    + `net6.0` (default)
    + `net7.0`

- `--ignore-projects (-i)`

**Definition**: Projects that are not
assessed.

**Required**: No

**Value**:

Comma separated project names. For example `project1,
 project2`.

- `--porting-projects (-p)`

**Definition**: Projects to port.

**Required**: No

**Value**:

Comma separated project names. For example `project1,
 project2`.

**Example command**

You can run the following command when you have a solution with five projects,
named `project1`, `project2`, `project3`,
`project4`, and `project5`, and you want to port
`project1` and `project2`.

```
& 'C:\Users\`<username>`\AppData\Local\Programs\Porting Assistant for .NET\resources\netcore_build\PortingAssistant.Client.CLI.exe' assess --solution-path "`<path_to_solution/example_solution.sln>`" --output-path "`<path_to_output_dir>`” --target “`net5.0`” --porting-projects “`project1,project2`”
```
