# Troubleshooting AWS CodeCommit

The following information might help you troubleshoot common issues in AWS CodeCommit.

###### Topics

- [Troubleshooting Git credentials and HTTPS connections to AWS CodeCommit](troubleshooting-gc.md "troubleshooting-gc.md")
- [Troubleshooting git-remote-codecommit and AWS CodeCommit](troubleshooting-grc.md "troubleshooting-grc.md")
- [Troubleshooting SSH connections to
  AWS CodeCommit](troubleshooting-ssh.md "troubleshooting-ssh.md")
- [Troubleshooting the credential helper and HTTPS connections to
  AWS CodeCommit](troubleshooting-ch.md "troubleshooting-ch.md")
- [Troubleshooting Git clients and AWS CodeCommit](troubleshooting-git.md "troubleshooting-git.md")
- [Troubleshooting access errors and AWS CodeCommit](troubleshooting-ae.md "troubleshooting-ae.md")
- [Troubleshooting configuration errors and AWS CodeCommit](troubleshooting-cf.md "troubleshooting-cf.md")
- [Troubleshooting console errors and AWS CodeCommit](troubleshooting-cs.md "troubleshooting-cs.md")
- [Troubleshooting triggers and AWS CodeCommit](troubleshooting-ti.md "troubleshooting-ti.md")
- [Turn on debugging](#troubleshooting-debug "#troubleshooting-debug")

## Turn on debugging

**Problem:** I want to turn on debugging to get more
information about my repository and how Git is executing commands.

**Possible fixes:** Try the following:

1. At the terminal or command prompt, run the following commands on your local machine
   before running Git commands:

On Linux, macOS, or Unix:

```
export GIT_TRACE_PACKET=1
export GIT_TRACE=1
export GIT_CURL_VERBOSE=1
```

On Windows:

```
set GIT_TRACE_PACKET=1
set GIT_TRACE=1
set GIT_CURL_VERBOSE=1
```

###### Note

Setting `GIT_CURL_VERBOSE` is useful for HTTPS connections only.
SSH does not use the `libcurl` library. 2. To get more information about your Git repository, we recommend installing the latest version of
[git-sizer](https://github.com/github/git-sizer?tab=readme-ov-file#getting-started "https://github.com/github/git-sizer?tab=readme-ov-file#getting-started").
Follow the instructions for intalling the utility appropriate to your operating system and environment. Once installed,
at the command line or terminal, change directories to your local repository and then run the following command:

```
git-sizer --verbose
```

###### Tip

Consider saving the output of the command to a file so that you can easily share it with others when troubleshooting problems,
particularly over time.
