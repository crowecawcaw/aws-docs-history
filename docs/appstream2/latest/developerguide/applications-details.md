# Applications Details

Applications details contains information about pre-warm manifests and app catalog configurations.

## Application PreWarm Manifests

When creating WorkSpaces Applications images you may specify applications to be made available to your users. To speed up the application's launch time you can prepare a PreWarm manifest. This is essentially a catalog of the files that your application needs to launch when users launch your application. During instance provisioning these files will be prepared ahead of session connections to speed up application launch times in user sessions.

Prewarm manifests must be pre-created on your AMI before being imported into the WorkSpaces Applications environment. You can choose to either create one common Prewarm manifest file or one per each application. This changes how you will import your AMI later.

### Common Prewarm Manifest

For each application you wish to prewarm, launch the application and perform any initial interactions your users may perform. Then, use the following command targeting the directory where your applications data is stored.

```
dir -path "C:\Path\To\Folder\To\Optimize" -Recurse -ErrorAction SilentlyContinue | %{$_.FullName} | Out-File "C:\ProgramData\Amazon\Photon\Prewarm\PrewarmManifest.txt" -encoding UTF8 -append
```

This will append the files to optimize for each application into the common `C:\\ProgramData\\Amazon\\Photon\\Prewarm\\PrewarmManifest.txt` file. There is no additional action needed to perform application prewarming. WorkSpaces Applications will look for the prewarm file at the above location and use it if it is present.

This process is optional and as the size of the prewarm manifest increases, fleet provisioning time will also increase. So take care to balance optimization with fleet provisioning.

### Application Specific Manifests

During image import, you may wish to specify separate application manifest files per application for easier tracking of the prewarm assets per application. To do this perform the same steps as above, but instead of creating a common `C:\\ProgramData\\Amazon\\Photon\\Prewarm\\PrewarmManifest.txt` file, create a file per application on your AMI.

For each application you wish to prewarm, launch the application and perform any initial interactions your users may perform. Then, use the following command targeting the directory where your applications data is stored.

```
dir -path "C:\Path\To\Folder\To\Optimize" -Recurse -ErrorAction SilentlyContinue | %{$_.FullName} | Out-File "C:\Path\To\My\<ApplicationName>PreWarm.txt" -encoding UTF8 -append
```

We will use these application prewarm files during the image import process. Again this is completely optional. You may choose to use this method, the Common Prewarm Manifest method, or no Prewarm manifest at all.

## Application Catalog Configs

`AppCatalogConfig` which allows you to specify the applications you wish to register to your WorkSpaces Applications image during AMI import. The `AppCatalogConfig` is a JSON list of Application configuration objects of the following structure.

```
[
    {
        "Name": "Rufus", //Required and must be unique among the list of applications
        "DisplayName": "Rufus",
        "AbsoluteAppPath": "Rufus", //Required
        "AbsoluteIconPath": "Rufus",
        "AbsoluteManifestPath": "Rufus",
        "WorkingDirectory": "Rufus",
        "LaunchParameters": "Rufus"
    }

    ...

    // Up to 50 applications total
 ]
```

The only required fields per application are the `Name` and the `AbsoluteAppPath`. The details of each field as follows:

Name [**Required**]

- A given name for your application to identify it
- Between 1 and 100 characters
- Allowed characters regex `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,99}$`
- Must be unique in a given AppCatalogConfig

DisplayName

- The display name for a given application to display to users
- Between 0 and 100 characters
- Allowed characters regex `^[a-zA-Z0-9][a-zA-Z0-9_. -]{0,99}$`

AbsoluteAppPath [**Required**]

- The path to the executable to launch your application
  - This is the executable that will be launched when users select your application

- Between 1 and 32767 characters
  - This character length upper limit is to support extended file paths in Windows. Ensure your AMI and application is properly configured to support Windows extended file paths if using file paths larger than 260 characters.

- Use escaped file path strings such as
  - `"C:\\Windows\\System32\\notepad.exe"`

AbsoluteManifestPath

- Only applicable if you are using [Application Specific Manifests](#application-specific-manifests "#application-specific-manifests")
- Path to prewarm manifest file for this application
- Between 0 and 32767 characters
  - This character length upper limit is to support extended file paths in Windows. Ensure your AMI and application is properly configured to support Windows extended file paths if using file paths larger than 260 characters.

- Use escaped file path strings such as
  - `"C:\\Path\\To\\PrewarmManifest.txt"`

AbsoluteIconPath

- Path to icon file on the AMI to use for the application.
  - This icon will be shown to users when streaming to this image.
  - If none is provided the icon will be derived from the executable itself.
  - Take care to select icon files with appropriately handled background transparency for a good client experience for your users
    - Use PNG images

- Between 1 and 32767 characters
  - This character length upper limit is to support extended file paths in Windows. Ensure your AMI and application is properly configured to support Windows extended file paths if using file paths larger than 260 characters.

- Use escaped file path strings such as
  - `"C:\\Path\\To\\ApplicationIcon.png"`

WorkingDirectory

- The working directory to launch your application in
- Between 0 and 32767 characters
  - This character length upper limit is to support extended file paths in Windows. Ensure your AMI and application is properly configured to support Windows extended file paths if using file paths larger than 260 characters.

- Use escaped file path strings such as
  - `"C:\\Path\\To\\Working\\Directory"`

LaunchParameters

- A string to use as the launch parameters for the executable specified in `AbsoluteAppPath`
- Between 0 and 1024 characters
- Use escaped strings with the full list of required launch parameters such as the following example which shows how you may use PowerShell scripts as your applications by using the PowerShell executable as your app with a script provided in the launch parameters
  - AbsoluteAppPath
    - `"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"`

  - LaunchParameters
    - `"-File \"C:\\Path\\To\\App\\Script.ps1\""`

### Sample AppCatalogConfig

This is a bare bones example of an AppCatalogConfig for Notepad, Google Chrome, and Mozilla Firefox

```
[
    {
        "Name": "Notepad",
        "DisplayName": "Notepad",
        "AbsoluteAppPath": "C:\\Windows\\System32\\notepad.exe"
    },
    {
        "Name": "Chrome",
        "DisplayName": "Chrome",
        "AbsoluteAppPath": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "LaunchParameters": "https://www.amazon.com/"
    },
    {
        "Name": "Firefox",
        "DisplayName": "Firefox",
        "AbsoluteAppPath": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
        "LaunchParameters": "https://aws.amazon.com/"
    }
 ]
```
