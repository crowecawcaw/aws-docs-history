

# Delete a package or package version
<a name="delete-package"></a>

You can delete one or more package versions at a time using the `delete-package-versions` command. To remove a package from a repository completely, including all associated versions and configuration, use the `delete-package` command. A package can exist in a repository without any package versions. This can happen when all versions are deleted using the `delete-package-versions` command, or if the package was created without any versions using the `put-package-origin-configuration` API operation (see [Editing package origin controls](package-origin-controls.md)).

**Topics**
+ [Deleting a package (AWS CLI)](#delete-package-CLI)
+ [Deleting a package (console)](#delete-package-console)
+ [Deleting a package version (AWS CLI)](#delete-package-version-CLI)
+ [Deleting a package version (console)](#delete-package-version-console)
+ [Deleting an npm package or package version](#delete-package-npm)
+ [Deleting a Maven package or package version](#delete-package-maven)
+ [Best practices for deleting packages or package versions](#delete-package-bp)

## Deleting a package (AWS CLI)
<a name="delete-package-CLI"></a>

You can delete a package, including all of its package versions and configuration, using the `delete-package` command. The following example deletes the PyPI package named `my-package` in the repo `my_repo` in the `my_domain` domain:

```
aws codeartifact delete-package --domain {{my_domain}} --domain-owner {{111122223333}} \
--repository {{my_repo}} --format {{pypi}} \
--package {{my-package}}
```

Sample output:

```
{
   "deletedPackage": { 
      "format": "pypi",
      "originConfiguration": { 
         "restrictions": { 
            "publish": "ALLOW",
            "upstream": "BLOCK"
         }
      },
      "package": "my-package"
   }
}
```

You can confirm that the package was deleted by running `describe-package` for the same package name:

```
aws codeartifact describe-package --domain {{my_domain}} --domain-owner {{111122223333}} \
--repository {{my_repo}} --format {{pypi}} --package {{my-package}}
```

## Deleting a package (console)
<a name="delete-package-console"></a>

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home).

1. In the navigation pane, choose **Repositories**.

1. Choose the **Repository** from which you want to delete a package.

1. Choose the **Package** you want to delete.

1. Choose **Delete Package**.

## Deleting a package version (AWS CLI)
<a name="delete-package-version-CLI"></a>

You can delete one or more package versions at a time using the `delete-package-versions` command. The following example deletes versions `4.0.0`, `4.0.1`, and `5.0.0` of the PyPI package named `my-package` in the `my_repo` in the `my_domain` domain:

```
aws codeartifact delete-package-versions --domain {{my_domain}} --domain-owner {{111122223333}} \
--repository {{my_repo}} --format {{pypi}} \
--package {{my-package}} --versions {{4.0.0 4.0.1 5.0.0}}
```

Sample output:

```
{
   "successfulVersions": {
      "4.0.0": {
         "revision": "oxwwYC9dDeuBoCt6+PDSwL6OMZ7rXeiXy44BM32Iawo=",
            "status": "Deleted"
      },
      "4.0.1": {
         "revision": "byaaQR748wrsdBaT+PDSwL6OMZ7rXeiBKM0551aqWmo=",
            "status": "Deleted"
      },
      "5.0.0": {
         "revision": "yubm34QWeST345ts+ASeioPI354rXeiSWr734PotwRw=",
            "status": "Deleted"
      }
   },
   "failedVersions": {}
}
```

You can confirm that the versions were deleted by running `list-package-versions` for the same package name:

```
aws codeartifact list-package-versions --domain {{my_domain}} --domain-owner {{111122223333}} \
--repository {{my_repo}} --format {{pypi}} --package {{my-package}}
```

## Deleting a package version (console)
<a name="delete-package-version-console"></a>

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home).

1. In the navigation pane, choose **Repositories**.

1. Choose the **Repository** from which you want to delete package versions.

1. Choose the **Package** from which you want to delete versions.

1. Select the **Package Version** that you want to delete.

1. Choose **Delete**.
**Note**  
In the console, you can only delete one package version at a time. To delete more than one at a time, use the CLI.

## Deleting an npm package or package version
<a name="delete-package-npm"></a>

To delete an npm package or individual package versions, set the `--format` option to `npm`. To delete a package version in a scoped npm package, use the `--namespace` option to specify the scope. For example, to delete the package `@types/react`, use `--namespace types`. Omit the `@` symbol when using `--namespace`. 

```
aws codeartifact delete-package-versions --domain {{my_domain}} --domain-owner {{111122223333}} \
--repository {{my_repo}} --format npm --namespace {{types}} \
--package {{react}} --versions {{0.12.2}}
```

To delete the package `@types/react`, including all of its versions:

```
aws codeartifact delete-package --domain {{my_domain}} --domain-owner {{111122223333}} \
--repository {{my_repo}} --format npm --namespace {{types}} \
--package {{react}}
```

## Deleting a Maven package or package version
<a name="delete-package-maven"></a>

To delete a Maven package or individual package versions, set the `--format` option to `maven` and specify the package to delete by passing the Maven group ID with the `--namespace` option and the Maven artifactID with the `--name` option. For example, the following shows how to delete a single version of `com.google.guava:guava`:

```
 aws codeartifact delete-package-versions --domain {{my_domain}} --domain-owner {{111122223333}} \
--repository {{my_repo}} --format maven --namespace {{com.google.guava}} \
--package {{guava}} --versions {{27.1-jre}}
```

The following example shows how to delete the package `com.google.guava:guava`, including all of its versions:

```
 aws codeartifact delete-package --domain {{my_domain}} --domain-owner {{111122223333}} \
--repository {{my_repo}} --format maven --namespace {{com.google.guava}} \
--package {{guava}}
```

## Best practices for deleting packages or package versions
<a name="delete-package-bp"></a>

If you do need to delete a package version, as a best practice we recommend creating a repository to store a backup copy of the package version you'd like to delete. You can do this by first calling `copy-package-versions` to the backup repository: 

```
aws codeartifact copy-package-versions --domain {{my_domain}} --domain-owner {{111122223333}} --source-repository {{my_repo}} \
 --destination-repository {{repo-2}} --package {{my-package}} --format npm \
 --versions {{6.0.2 4.0.0}}
```

Once you've copied the package version, you can then call `delete-package-versions` on package or package version you'd like to delete.

```
aws codeartifact delete-package-versions --domain {{my_domain}} --domain-owner {{111122223333}} \
--repository {{my_repo}} --format {{pypi}} \
--package {{my-package}} --versions {{4.0.0 4.0.1 5.0.0}}
```