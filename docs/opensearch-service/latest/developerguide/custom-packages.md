# Importing and managing packages in Amazon OpenSearch Service

Amazon OpenSearch Service lets you upload custom dictionary files, such as stop words and synonyms, and
associate plugins with your domain. These plugins can be pre-packaged, custom, or third-party,
which gives you flexibility to extend your domain’s functionality. The generic term for all
these types of files is _packages_.

- **Dictionary files** help refine search results by
  instructing OpenSearch to ignore common high-frequency words or to treat similar terms, like
  "frozen custard," "gelato," and "ice cream," as equivalent. They can also improve [stemming](https://en.wikipedia.org/wiki/Stemming "https://en.wikipedia.org/wiki/Stemming"), as seen with the Japanese
  (kuromoji) analysis plugin.
- **Pre-packaged plugins** provide built-in functionality,
  such as the Amazon Personalize plugin for personalized search results. These plugins use the
  `ZIP-PLUGIN` package type. For more information, see [Plugins by engine version in Amazon OpenSearch Service](supported-plugins.md "supported-plugins.md").
- **Custom and third-party plugins** allow you to add
  tailored features or integrate with external systems, which offers even more flexibility for
  your domain. Like pre-packaged plugins, you upload custom plugins as `ZIP-PLUGIN`
  packages. For third-party plugins, you must also import the plugin license and configuration
  files as separate packages, then associate them all with the domain.

For more information, see the following topics:

    + [Managing custom plugins in Amazon OpenSearch Service](custom-plugins.md "custom-plugins.md")
    + [Installing third-party plugins in Amazon OpenSearch Service](plugins-third-party.md "plugins-third-party.md")

###### Note

You can associate a maximum of 20 plugins with a single domain. This limit includes all
plugin types—optional, third-party, and custom plugins.

###### Topics

- [Required permissions](#custom-packages-iam "#custom-packages-iam")
- [Uploading packages to Amazon S3](#custom-packages-gs "#custom-packages-gs")
- [Importing and associating packages](#custom-packages-assoc "#custom-packages-assoc")
- [Using packages with OpenSearch](#custom-packages-using "#custom-packages-using")
- [Updating packages](#custom-packages-updating "#custom-packages-updating")
- [Manually updating indexes with a
  new dictionary](#custom-packages-updating-index-analyzers "#custom-packages-updating-index-analyzers")
- [Dissociating and removing packages](#custom-packages-dissoc "#custom-packages-dissoc")
- [Managing custom plugins in Amazon OpenSearch Service](custom-plugins.md "custom-plugins.md")
- [Installing third-party plugins in Amazon OpenSearch Service](plugins-third-party.md "plugins-third-party.md")

## Required permissions

Users without administrator access require certain AWS Identity and Access Management (IAM) actions in order to
manage packages:

- `es:CreatePackage` – Create a package
- `es:DeletePackage` – Delete a package
- `es:AssociatePackage` – Associate a package to a domain
- `es:DissociatePackage` – Dissociate a package from a domain

You also need permissions on the Amazon S3 bucket path or object where the custom package
resides.

Grant all permission within IAM, not in the domain access policy. For more information,
see [Identity and Access Management in Amazon OpenSearch Service](ac.md "ac.md").

## Uploading packages to Amazon S3

This section covers how to upload custom dictionary packages, since pre-packaged plugin
packages are already installed. Before you can associate a custom dictionary with your domain,
you must upload it to an Amazon S3 bucket. For instructions, see [Uploading objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") in the _Amazon Simple Storage Service User Guide_. Supported plugins don't need to be uploaded.

If your dictionary contains sensitive information, specify [server-side encryption with S3-managed
keys](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md") when you upload it. OpenSearch Service can't access files in S3 that you protect using an
AWS KMS key.

After you upload the file, make note of its S3 path. The path format is
`s3://`amzn-s3-demo-bucket`/`file-path`/`file-name``.

You can use the following synonyms file for testing purposes. Save it as
`synonyms.txt`.

```
danish, croissant, pastry
ice cream, gelato, frozen custard
sneaker, tennis shoe, running shoe
basketball shoe, hightop

```

Certain dictionaries, such as Hunspell dictionaries, use multiple files and require their
own directories on the file system. At this time, OpenSearch Service only supports single-file
dictionaries.

## Importing and associating packages

The console is the simplest way to import a custom dictionary into OpenSearch Service. When you import a
dictionary from Amazon S3, OpenSearch Service stores its own copy of the package and automatically encrypts that
copy using AES-256 with OpenSearch Service-managed keys.

Optional plugins are already pre-installed in OpenSearch Service so you don't need to upload them
yourself, but you do need to associate a plugin to a domain. Available plugins are listed on
the **Packages** screen in the console.

1. In the Amazon OpenSearch Service console, choose **Packages**.
2. Choose **Import package**.
3. Give the package a descriptive name.
4. Provide the S3 path to the file, and then choose
   **Import**.
5. Return to the **Packages** screen.
6. When the package status is **Available**, select it.
7. Choose **Associate to a domain**.
8. Select a domain, and then choose **Next**. Review the packages
   and choose **Associate**.
9. In the navigation pane, choose your domain and go to the
   **Packages** tab.
10. If the package is a custom dictionary, note the ID when the package becomes
    **Available**. Use
    `analyzers/`id`` as the file path in [requests to OpenSearch](#custom-packages-using "#custom-packages-using").

## Using packages with OpenSearch

This section covers how to use both types of packages: custom dictionaries and
pre-packaged plugins.

### Using custom dictionaries

After you associate a file to a domain, you can use it in parameters such as
`synonyms_path`, `stopwords_path`, and `user_dictionary`
when you create tokenizers and token filters. The exact parameter varies by object. Several
objects support `synonyms_path` and `stopwords_path`, but
`user_dictionary` is exclusive to the kuromoji plugin.

For the IK (Chinese) Analysis plugin, you can upload a custom dictionary file as a
custom package and associate it to a domain, and the plugin automatically picks it up
without requiring a `user_dictionary` parameter. If your file is a synonyms file,
use the `synonyms_path` parameter.

The following example adds a synonyms file to a new index:

```
PUT `my-index`
{
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "`my_analyzer`": {
            "type": "custom",
            "tokenizer": "standard",
            "filter": ["`my_filter`"]
          }
        },
        "filter": {
          "`my_filter`": {
            "type": "synonym",
            "synonyms_path": "analyzers/`F111111111`",
            "updateable": true
          }
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "`description`": {
        "type": "text",
        "analyzer": "standard",
        "search_analyzer": "`my_analyzer`"
      }
    }
  }
}
```

This request creates a custom analyzer for the index that uses the standard tokenizer
and a synonym token filter.

- Tokenizers break streams of characters into _tokens_ (typically words) based on some set of rules. The simplest example
  is the whitespace tokenizer, which breaks the preceding characters into a token each
  time it encounters a whitespace character. A more complex example is the standard
  tokenizer, which uses a set of grammar-based rules to work across many languages.
- Token filters add, modify, or delete tokens. For example, a synonym token filter
  adds tokens when it finds a word in the synonyms list. The stop token filter removes
  tokens when finds a word in the stop words list.

This request also adds a text field (`description`) to the mapping and tells
OpenSearch to use the new analyzer as its search analyzer. You can see that it still uses the
standard analyzer as its index analyzer.

Finally, note the line `"updateable": true` in the token filter. This field
only applies to search analyzers, not index analyzers, and is critical if you later want to
[update the search analyzer](#custom-packages-updating "#custom-packages-updating")
automatically.

For testing purposes, add some documents to the index:

```
POST _bulk
{ "index": { "_index": "my-index", "_id": "1" } }
{ "description": "ice cream" }
{ "index": { "_index": "my-index", "_id": "2" } }
{ "description": "croissant" }
{ "index": { "_index": "my-index", "_id": "3" } }
{ "description": "tennis shoe" }
{ "index": { "_index": "my-index", "_id": "4" } }
{ "description": "hightop" }

```

Then search them using a synonym:

```
GET my-index/_search
{
  "query": {
    "match": {
      "description": "gelato"
    }
  }
}
```

In this case, OpenSearch returns the following response:

```
{
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.99463606,
    "hits": [{
      "_index": "my-index",
      "_type": "_doc",
      "_id": "1",
      "_score": 0.99463606,
      "_source": {
        "description": "ice cream"
      }
    }]
  }
}
```

###### Tip

Dictionary files use Java heap space proportional to their size. For example, a 2 GiB
dictionary file might consume 2 GiB of heap space on a node. If you use large files,
ensure that your nodes have enough heap space to accommodate them. [Monitor](managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-cluster-metrics "managedomains-cloudwatchmetrics.md#managedomains-cloudwatchmetrics-cluster-metrics") the
`JVMMemoryPressure` metric, and scale your cluster as necessary.

### Using pre-packaged plugins

OpenSearch Service lets you associate pre-installed, optional OpenSearch plugins to use with your
domain. An pre-packaged plugin package is compatible with a specific OpenSearch version, and
can only be associated to domains with that version. The list of available packages for your
domain includes all supported plugins that are compatible with your domain version. After
you associate a plugin to a domain, an installation process on the domain begins. Then, you
can reference and use the plugin when you make requests to OpenSearch Service.

Associating and dissociating a plugin requires a blue/green deployment. For more
information, see [Changes that usually cause blue/green deployments](managedomains-configuration-changes.md#bg "managedomains-configuration-changes.md#bg").

Optional plugins include language analyzers and customized search results. For example,
the Amazon Personalize Search Ranking plugin uses machine learning to personalize search results for
your customers. For more information about this plugin, see [Personalizing search results from
OpenSearch](../../../personalize/latest/dg/personalize-opensearch.md "../../../personalize/latest/dg/personalize-opensearch.md"). For a list of all supported plugins, see [Plugins by engine version in Amazon OpenSearch Service](supported-plugins.md "supported-plugins.md").

#### Sudachi plugin

For the [Sudachi plugin](https://github.com/WorksApplications/elasticsearch-sudachi "https://github.com/WorksApplications/elasticsearch-sudachi"), when you reassociate a dictionary file, it doesn't immediately
reflect on the domain. The dictionary refreshes when the next blue/green deployment runs
on the domain as part of a configuration change or other update. Alternatively, you can
create a new package with the updated data, create a new index using this new package,
reindex the existing index to the new index, and then delete the old index. If you prefer
to use the reindexing approach, use an index alias so that there's no disruption to your
traffic.

Additionally, the Sudachi plugin only supports binary Sudachi dictionaries, which you
can upload with the [CreatePackage](../APIReference/API_CreatePackage.md "../APIReference/API_CreatePackage.md") API operation. For information on the pre-built system dictionary
and process for compiling user dictionaries, see the [Sudachi
documentation](https://github.com/WorksApplications/elasticsearch-sudachi "https://github.com/WorksApplications/elasticsearch-sudachi").

The following example demonstrates how to use system and user dictionaries with the
Sudachi tokenizer. You must upload these dictionaries as custom packages with type
`TXT-DICTIONARY` and provide their package IDs in the additional
settings.

```
PUT sudachi_sample
{
  "settings": {
    "index": {
      "analysis": {
        "tokenizer": {
          "sudachi_tokenizer": {
            "type": "sudachi_tokenizer",
            "additional_settings": "{\"systemDict\": \"`<system-dictionary-package-id>`\",\"userDict\": [\"`<user-dictionary-package-id>`\"]}"
        }
        },
        "analyzer": {
          "sudachi_analyzer": {
            "filter": ["my_searchfilter"],
            "tokenizer": "sudachi_tokenizer",
            "type": "custom"
          }
        },
        "filter":{
          "my_searchfilter": {
            "type": "sudachi_split",
            "mode": "search"
          }
        }
      }
    }
  }
}
```

## Updating packages

This section only covers how to update a custom dictionary package, because pre-packaged
plugin packages are already updated for you. Uploading a new version of a dictionary to Amazon S3
does _not_ automatically update the package on Amazon OpenSearch Service. OpenSearch Service
stores its own copy of the file, so if you upload a new version to S3, you must manually
update it.

Each of your associated domains stores _its_ own copy of
the file, as well. To keep search behavior predictable, domains continue to use their current
package version until you explicitly update them. To update a custom package, modify the file
in Amazon S3 Control, update the package in OpenSearch Service, and then apply the update.

1.  In the OpenSearch Service console, choose **Packages**.
2.  Choose a package and **Update**.
3.  Provide a new S3 path to the file, and then choose **Update
    package**.
4.  Return to the **Packages** screen.
5.  When the package status changes to **Available**, select it. Then
    choose one or more associated domains, **Apply update**, and confirm.
    Wait for the association status to change to **Active**.
6.  The next steps vary depending on how you configured your indexes:

        * If your domain is running OpenSearch or Elasticsearch 7.8 or later, and only
         uses search analyzers with the [updateable](#custom-packages-using "#custom-packages-using") field set to true, you don't need to take any further action.
         OpenSearch Service automatically updates your indexes using the [\_plugins/\_refresh\_search\_analyzers API](https://docs.opensearch.org/latest/im-plugin/refresh-analyzer/index/ "https://docs.opensearch.org/latest/im-plugin/refresh-analyzer/index/").
        * If your domain is running Elasticsearch 7.7 or earlier, uses index analyzers,
         or doesn't use the `updateable` field, see [Manually updating indexes with a
         new dictionary](#custom-packages-updating-index-analyzers "#custom-packages-updating-index-analyzers").

    Although the console is the simplest method, you can also use the AWS CLI, SDKs, or
    configuration API to update OpenSearch Service packages. For more information, see the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md")
    and [Amazon OpenSearch Service API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

Instead of manually updating a package in the console, you can use the SDKs to
automate the update process. The following sample Python script uploads a new package file
to Amazon S3, updates the package in OpenSearch Service, and applies the new package to the specified domain.
After confirming the update was successful, it makes a sample call to OpenSearch
demonstrating the new synonyms have been applied.

You must provide values for `host`, `region`,
`file_name`, `bucket_name`, `s3_key`,
`package_id`, `domain_name`, and `query`.

```
from requests_aws4auth import AWS4Auth
import boto3
import requests
import time
import json
import sys

host = ''  # The OpenSearch domain endpoint with https:// and a trailing slash. For example, https://my-test-domain.us-east-1.es.amazonaws.com/
region = ''  # For example, us-east-1
file_name = ''  # The path to the file to upload
bucket_name = ''  # The name of the S3 bucket to upload to
s3_key = ''  # The name of the S3 key (file name) to upload to
package_id = ''  # The unique identifier of the OpenSearch package to update
domain_name = ''  # The domain to associate the package with
query = ''  # A test query to confirm the package has been successfully updated

service = 'es'
credentials = boto3.Session().get_credentials()
client = boto3.client('opensearch')
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key,
                   region, service, session_token=credentials.token)


def upload_to_s3(file_name, bucket_name, s3_key):
    """Uploads file to S3"""
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket_name, s3_key)
        print('Upload successful')
        return True
    except FileNotFoundError:
        sys.exit('File not found. Make sure you specified the correct file path.')


def update_package(package_id, bucket_name, s3_key):
    """Updates the package in OpenSearch Service"""
    print(package_id, bucket_name, s3_key)
    response = client.update_package(
        PackageID=package_id,
        PackageSource={
            'S3BucketName': bucket_name,
            'S3Key': s3_key
        }
    )
    print(response)


def associate_package(package_id, domain_name):
    """Associates the package to the domain"""
    response = client.associate_package(
        PackageID=package_id, DomainName=domain_name)
    print(response)
    print('Associating...')


def wait_for_update(domain_name, package_id):
    """Waits for the package to be updated"""
    response = client.list_packages_for_domain(DomainName=domain_name)
    package_details = response['DomainPackageDetailsList']
    for package in package_details:
        if package['PackageID'] == package_id:
            status = package['DomainPackageStatus']
            if status == 'ACTIVE':
                print('Association successful.')
                return
            elif status == 'ASSOCIATION_FAILED':
                sys.exit('Association failed. Please try again.')
            else:
                time.sleep(10)  # Wait 10 seconds before rechecking the status
                wait_for_update(domain_name, package_id)


def sample_search(query):
    """Makes a sample search call to OpenSearch"""
    path = '_search'
    params = {'q': query}
    url = host + path
    response = requests.get(url, params=params, auth=awsauth)
    print('Searching for ' + '"' + query + '"')
    print(response.text)
```

###### Note

If you receive a "package not found" error when you run the script using the AWS CLI,
it likely means Boto3 is using whichever Region is specified in
~/.aws/config, which isn't the Region your S3 bucket is in. Either run
`aws configure` and specify the correct Region, or
explicitly add the Region to the client:

```
client = boto3.client('opensearch', region_name='us-east-1')
```

## Manually updating indexes with a

new dictionary

Manual index updates only apply to custom dictionaries, not pre-packaged plugins. To use
an updated dictionary, you must manually update your indexes if you meet any of the following
conditions:

- Your domain runs Elasticsearch 7.7 or earlier.
- You use custom packages as index analyzers.
- You use custom packages as search analyzers, but don't include the [updateable](#custom-packages-using "#custom-packages-using") field.

To update analyzers with the new package files, you have two options:

- Close and open any indexes that you want to update:

```
POST `my-index`/_close
POST `my-index`/_open
```

- Reindex the indexes. First, create an index that uses the updated synonyms file (or an
  entirely new file). Note that only UTF-8 is supported.

```
PUT `my-new-index`
{
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "synonym_analyzer": {
            "type": "custom",
            "tokenizer": "standard",
            "filter": ["synonym_filter"]
          }
        },
        "filter": {
          "synonym_filter": {
            "type": "synonym",
            "synonyms_path": "analyzers/`F222222222`"
          }
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "`description`": {
        "type": "text",
        "analyzer": "synonym_analyzer"
      }
    }
  }
}
```

Then [reindex](https://docs.opensearch.org/latest/opensearch/reindex-data/ "https://docs.opensearch.org/latest/opensearch/reindex-data/")
the old index to that new index:

```
POST _reindex
{
  "source": {
    "index": "`my-index`"
  },
  "dest": {
    "index": "`my-new-index`"
  }
}
```

If you frequently update index analyzers, use [index aliases](https://docs.opensearch.org/latest/opensearch/index-alias/ "https://docs.opensearch.org/latest/opensearch/index-alias/") to
maintain a consistent path to the latest index:

```
POST _aliases
{
  "actions": [
    {
      "remove": {
        "index": "`my-index`",
        "alias": "`latest-index`"
      }
    },
    {
      "add": {
        "index": "`my-new-index`",
        "alias": "`latest-index`"
      }
    }
  ]
}
```

If you don't need the old index, delete it:

```
DELETE `my-index`
```

## Dissociating and removing packages

Dissociating a package, whether it's a custom dictionary or pre-packaged plugin, from a
domain means that you can no longer use that package when you create new indexes. After a
package is dissociated, existing indexes that were using the package can no longer use it. You
must remove the package from any index before you can dissociate it, otherwise the
dissociation fails.

The console is the simplest way to dissociate a package from a domain and remove it from
OpenSearch Service. Removing a package from OpenSearch Service does _not_ remove it from
its original location on Amazon S3.

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home").
2. In the navigation pane, choose **Domains**.
3. Choose the domain, then navigate to the **Packages** tab.
4. Select a package, **Actions**, and then choose
   **Dissociate**. Confirm your choice.
5. Wait for the package to disappear from the list. You might need to refresh your
   browser.
6. If you want to use the package with other domains, stop here. To continue with
   removing the package (if it's a custom dictionary), choose
   **Packages** in the navigation pane.
7. Select the package and choose **Delete**.

Alternately, use the AWS CLI, SDKs, or configuration API to dissociate and remove packages.
For more information, see the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md") and [Amazon OpenSearch Service API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").
