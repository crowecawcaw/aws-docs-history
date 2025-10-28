# Optimizing the Launch Performance of Your Applications with the Image Assistant CLI Operations

AppStream 2.0 lets you optimize the launch performance of your applications for your
users’ streaming sessions. When you do so by using the Image Assistant CLI operations,
you can specify the files to optimize for your application launch. Adding
files to the application optimization manifest reduces the time that it
takes for the application to launch for the first time on a new fleet instance. However,
this also increases the time that it takes for the fleet instances to be made available
to users. The optimization manifest is a line-delimited text file that is per
application.

###### Note

If you onboard application optimization manifests by using both the Image Assistant CLI operations and the Image Assistant GUI, the manifests are merged.

Following is an example of an application optimization manifest file:

```
C:\Program Files (x86)\Notepad++\autoCompletion
C:\Program Files (x86)\Notepad++\localization
C:\Program Files (x86)\Notepad++\plugins
C:\Program Files (x86)\Notepad++\themes
C:\Program Files (x86)\Notepad++\updater
C:\Program Files (x86)\Notepad++\userDefineLangs
C:\Program Files (x86)\Notepad++\change.log
C:\Program Files (x86)\Notepad++\config.xml
C:\Program Files (x86)\Notepad++\contextMenu.xml
C:\Program Files (x86)\Notepad++\doLocalConf.xml
C:\Program Files (x86)\Notepad++\functionList.xml
C:\Program Files (x86)\Notepad++\langs.model.xml
C:\Program Files (x86)\Notepad++\license.txt
C:\Program Files (x86)\Notepad++\notepad++.exe
C:\Program Files (x86)\Notepad++\readme.txt
C:\Program Files (x86)\Notepad++\SciLexer.dll
C:\Program Files (x86)\Notepad++\shortcuts.xml
C:\Program Files (x86)\Notepad++\stylers.model.xml
```

For more information about optimizing the launch performance of your
applications, see _Optimizing the Launch Performance of Your Applications_ in [Default Application and Windows Settings and Application Launch Performance in Amazon AppStream 2.0](customizing-appstream-images.md "customizing-appstream-images.md").
