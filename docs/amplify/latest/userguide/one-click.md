# Using the Deploy to Amplify button to share a GitHub project

###### Important

One-click deployment using the **Deploy to Amplify Hosting** button is no longer available. To deploy from a repository, create a new application in Amplify Hosting. For instructions, see [Getting started with deploying an app to Amplify
Hosting](getting-started.md "getting-started.md").

The **Deploy to Amplify Hosting** button enables you to share
GitHub projects publicly or within your team. The following is an image of the button:

![The Deploy to Amplify Hosting button.](images/OneClickButton.png)

## Adding

the Deploy to Amplify Hosting button to a repository or blog

Add the button to your GitHub README.md file, blog post, or any other markup page that
renders HTML. The button has the following two components:

1. An SVG image located at the URL `https://oneclick.amplifyapp.com/button.svg`
2. The Amplify console URL with a link to your GitHub repository. Your can either copy
   your repository's URL, such as
   `https://github.com/username/repository`, or you can provide a deep
   link into a specific folder, such as
   `https://github.com/username/repository/tree/branchname/folder`.
   Amplify Hosting will deploy the default branch in your repository. Additional
   branches can be connected after the app is connected.

Use the following example to add the button to a markdown file, such as your GitHub
README.md. Replace `https://github.com/username/repository` with the URL to your
repository.

```
[![amplifybutton](https://oneclick.amplifyapp.com/button.svg)](https://console.aws.amazon.com/amplify/home#/deploy?repo=`https://github.com/username/repository`)
```

Use the following example to add the button to any HTML document. Replace `https://github.com/username/repository` with the URL to your
repository.

```
<a href="https://console.aws.amazon.com/amplify/home#/deploy?repo=`https://github.com/username/repository"`>
    <img src="https://oneclick.amplifyapp.com/button.svg" alt="Deploy to Amplify Hosting">
</a>
```
