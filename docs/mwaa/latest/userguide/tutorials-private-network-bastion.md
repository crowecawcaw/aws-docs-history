# Tutorial: Configuring private network access using a Linux Bastion Host

This tutorial walks you through the steps to create an SSH tunnel from your computer to the to the Apache Airflow webserver for your Amazon Managed Workflows for Apache Airflow environment. It assumes you've already created an Amazon MWAA environment. Once set up, a Linux Bastion Host acts as a jump server allowing a secure connection from your computer to the resources in your VPC. You'll then use a SOCKS proxy management add-on to control the proxy settings in your browser to access your Apache Airflow UI.

###### Sections

- [Private network](#private-network-lb-onconsole "#private-network-lb-onconsole")
- [Use cases](#private-network-lb-usecases "#private-network-lb-usecases")
- [Before you begin](#private-network-lb-prereqs "#private-network-lb-prereqs")
- [Objectives](#private-network-lb-objectives "#private-network-lb-objectives")
- [Step one: Create the bastion instance](#private-network-lb-create-bastion "#private-network-lb-create-bastion")
- [Step two: Create the ssh tunnel](#private-network-lb-create-test "#private-network-lb-create-test")
- [Step three: Configure the bastion security group as an inbound rule](#private-network-lb-create-sgsource "#private-network-lb-create-sgsource")
- [Step four: Copy the Apache Airflow URL](#private-network-lb-view-env "#private-network-lb-view-env")
- [Step five: Configure proxy settings](#private-network-lb-browser-extension "#private-network-lb-browser-extension")
- [Step six: Open the Apache Airflow UI](#private-network-lb-open "#private-network-lb-open")
- [What's next?](#bastion-next-up "#bastion-next-up")

## Private network

This tutorial assumes you've chosen the **Private network** access mode for your Apache Airflow webserver.

![This image displays the architecture for an Amazon MWAA environment with a private webserver.](images/mwaa-private-web-server.png)

The private network access mode limits access to the Apache Airflow UI to users _within your Amazon VPC_ who have been granted access to the
[IAM policy for your environment](access-policies.md "access-policies.md").

When you create an environment with private webserver access, you must package all of your dependencies in a Python wheel archive (`.whl`), then
reference the `.whl` in your `requirements.txt`. For instructions on packaging and installing your dependencies
using wheel, refer to [Managing dependencies using Python wheel](best-practices-dependencies.md#best-practices-dependencies-python-wheels "best-practices-dependencies.md#best-practices-dependencies-python-wheels").

The following image depicts where to find the **Private network** option on the Amazon MWAA console.

![This image depicts where to find the Private network option on the Amazon MWAA console.](images/mwaa-console-private-network.png)

## Use cases

You can use this tutorial after you've created an Amazon MWAA environment. You must use the same Amazon VPC, VPC security groups, and public subnets as your environment.

## Before you begin

1. Check for user permissions. Be sure that your account in AWS Identity and Access Management (IAM) has sufficient permissions to create and manage VPC resources.
2. Use your Amazon MWAA VPC. This tutorial assumes that you are associating the bastion host to an existing VPC. The Amazon VPC must be in the same region as your Amazon MWAA environment and have two private subnets, as defined in [Create the VPC network](vpc-create.md "vpc-create.md").
3. Create an SSH key. You need to create an Amazon EC2 SSH key (**.pem**) in the same Region as your Amazon MWAA environment to connect to the virtual servers. If you don't have an SSH key, refer to [Create or import a key pair](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#prepare-key-pair "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md#prepare-key-pair") in the _Amazon EC2 User Guide_.

## Objectives

In this tutorial, you'll do the following:

1. Create a Linux Bastion Host instance using a [AWS CloudFormation template for an existing VPC](https://fwd.aws/vWMxm "https://fwd.aws/vWMxm").
2. Authorize inbound traffic to the bastion instance's security group using an ingress rule on port `22`.
3. Authorize inbound traffic from an Amazon MWAA environment's security group to the bastion instance's security group.
4. Create an SSH tunnel to the bastion instance.
5. Install and configure the FoxyProxy add-on for the Firefox browser to access the Apache Airflow UI.

## Step one: Create the bastion instance

The following section describes the steps to create the linux bastion instance using a [AWS CloudFormation template for an existing VPC](https://fwd.aws/vWMxm "https://fwd.aws/vWMxm") on the AWS CloudFormation console.

###### To create the Linux Bastion Host

1. Open the [Deploy Quick Start](https://fwd.aws/Jwzqv "https://fwd.aws/Jwzqv") page on the AWS CloudFormation console.
2. Use the region selector in the navigation bar to choose the same AWS Region as your Amazon MWAA environment.
3. Choose **Next**.
4. Enter a name in the **Stack name** text field, such as `mwaa-linux-bastion`.
5. On the **Parameters**, **Network configuration** pane, choose the following options:
   1. Choose your Amazon MWAA environment's **VPC ID**.
   2. Choose your Amazon MWAA environment's **Public subnet 1 ID**.
   3. Choose your Amazon MWAA environment's **Public subnet 2 ID**.
   4. Enter the narrowest possible address range (for example, an internal CIDR range) in **Allowed bastion external access CIDR**.

   ###### Note

   The simplest way to identify a range is to use the same CIDR range as your public subnets. For example, the public subnets in the AWS CloudFormation template on the [Create the VPC network](vpc-create.md "vpc-create.md") page are `10.192.10.0/24` and `10.192.11.0/24`.

6. On the **Amazon EC2 configuration** pane, choose the following:
   1. Choose your SSH key in the dropdown list in **Key pair name**.
   2. Enter a name in **Bastion Host Name**.
   3. Choose **true** for **TCP forwarding**.

   ###### Warning

   TCP forwarding must be set to **true** in this step. Otherwise, you won't be able to create an SSH tunnel in the next step.

7. Choose **Next**, **Next**.
8. Select the acknowledgement, and then choose **Create stack**.

To learn more about the architecture of your Linux Bastion Host, refer to [Linux Bastion Hosts on the AWS Cloud: Architecture](../../../quickstart/latest/linux-bastion/architecture.md "../../../quickstart/latest/linux-bastion/architecture.md").

## Step two: Create the ssh tunnel

The following steps describe how to create the ssh tunnel to your linux bastion. An SSH tunnel recieves the request from your local IP address to the linux bastion, which is why TCP forwarding for the linux bastion was set to `true` in previous steps.

macOS/Linux

###### To create a tunnel using the command line

1. Open the [Instances](https://console.aws.amazon.com/ec2/v2/home#/Instances: "https://console.aws.amazon.com/ec2/v2/home#/Instances:") page on the Amazon EC2 console.
2. Choose an instance.
3. Copy the address in **Public IPv4 DNS**. For example, `ec2-4-82-142-1.compute-1.amazonaws.com`.
4. In your command prompt, navigate to the directory where your SSH key is stored.
5. Run the following command to connect to the bastion instance using ssh. Substitute the sample value with your SSH key name in `mykeypair.pem`.

```
ssh -i `mykeypair.pem` -N -D 8157 ec2-user@`YOUR_PUBLIC_IPV4_DNS`
```

Windows (PuTTY)

###### To create a tunnel using PuTTY

1. Open the [Instances](https://console.aws.amazon.com/ec2/v2/home#/Instances: "https://console.aws.amazon.com/ec2/v2/home#/Instances:") page on the Amazon EC2 console.
2. Choose an instance.
3. Copy the address in **Public IPv4 DNS**. For example, `ec2-4-82-142-1.compute-1.amazonaws.com`.
4. Open [PuTTY](https://www.putty.org/ "https://www.putty.org/"), select **Session**.
5. Enter the host name in **Host Name** as ec2-user@`YOUR_PUBLIC_IPV4_DNS` and the **port** as `22`.
6. Expand the **SSH** tab, select **Auth**. In **Private Key file for authentication**, choose your local "ppk" file.
7. Under SSH, choose the **Tunnels** tab, and then select the _Dynamic_ and _Auto_ options.
8. In **Source Port**, add the `8157` port (or any other unused port), and then leave the **Destination** port blank. Choose **Add**.
9. Choose the **Session** tab and enter a session name. For example `SSH Tunnel`.
10. Choose **Save**, **Open**.

###### Note

You might need to enter a pass phrase for your public key.

###### Note

If you receive a `Permission denied (publickey)` error, we recommend using the [AWSSupport-TroubleshootSSH](../../../systems-manager/latest/userguide/automation-awssupport-troubleshootssh.md "../../../systems-manager/latest/userguide/automation-awssupport-troubleshootssh.md") tool, and choose **Run this Automation (console)** to troubleshoot your SSH setup.

## Step three: Configure the bastion security group as an inbound rule

Access to the servers and regular internet access from the servers is allowed with a special maintenance security group attached to those servers. The following steps describe how to configure the bastion security group as an inbound source of traffic to an environment's VPC security group.

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. On the **Networking** pane, choose **VPC security group**.
4. Choose **Edit inbound rules**.
5. Choose **Add rule**.
6. Choose your VPC security group ID in the **Source** dropdown list.
7. Leave the remaining options blank, or set to their default values.
8. Choose **Save rules**.

## Step four: Copy the Apache Airflow URL

The following steps describe how to open the Amazon MWAA console and copy the URL to the Apache Airflow UI.

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Copy the URL in **Airflow UI** for subsequent steps.

## Step five: Configure proxy settings

If you use an SSH tunnel with dynamic port forwarding, you must use a SOCKS proxy management add-on to control the proxy settings in your browser. For example, you can use the `--proxy-server` feature of Chromium to kick off a browser session, or use the FoxyProxy extension in the Mozilla FireFox browser.

### Option one: Setup an SSH Tunnel using local port forwarding

If you do not wish to use a SOCKS proxy, you can set up an SSH tunnel using local port forwarding. The following example command accesses the Amazon EC2 _ResourceManager_ web interface by forwarding traffic on local port 8157.

1. Open a new command prompt window.
2. Enter the following command to open an SSH tunnel.

```
ssh -i `mykeypair.pem` -N -L 8157:`YOUR_VPC_ENDPOINT_ID`-vpce.`us-east-1`.airflow.amazonaws.com:443 ubuntu@`YOUR_PUBLIC_IPV4_DNS`.`us-east-1`.compute.amazonaws.com
```

`-L` signifies the use of local port forwarding which you can use to specify a local port used to forward data to the identified remote port on the node's local webserver. 3. Enter `http://localhost:8157/` in your browser.

###### Note

You might need to use `https://localhost:8157/`.

### Option two: Proxies using the command line

You can use most web browsers to configure proxies using a command line or configuration parameter. For example, with Chromium you can start the browser with the following command:

```
chromium --proxy-server="socks5://localhost:8157"
```

This starts a browser session which uses the ssh tunnel you created in previous steps to proxy its requests. You can open your Private Amazon MWAA environment URL (with _https://_) as follows:

```
https://`YOUR_VPC_ENDPOINT_ID`-vpce.`us-east-1`.airflow.amazonaws.com/home.
```

### Option three: Proxies using FoxyProxy for Mozilla Firefox

The following example demonstrates a FoxyProxy Standard (version 7.5.1) configuration for Mozilla Firefox. FoxyProxy provides a set of proxy management tools. It lets you use a proxy server for URLs that match patterns corresponding to domains used by the Apache Airflow UI.

1. In Firefox, open the [FoxyProxy Standard](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/ "https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/") extension page.
2. Choose **Add to Firefox**.
3. Choose **Add**.
4. Choose the FoxyProxy icon in your browser's toolbar, choose **Options**.
5. Copy the following code and save locally as `mwaa-proxy.json`. Substitute the sample value in `YOUR_HOST_NAME` with your **Apache Airflow URL**.

```
{
  "e0b7kh1606694837384": {
    "type": 3,
    "color": "#66cc66",
    "title": "airflow",
    "active": true,
    "address": "localhost",
    "port": 8157,
    "proxyDNS": false,
    "username": "",
    "password": "",
    "whitePatterns": [
      {
        "title": "airflow-ui",
        "pattern": "`YOUR_HOST_NAME`",
        "type": 1,
        "protocols": 1,
        "active": true
      }
    ],
    "blackPatterns": [],
    "pacURL": "",
    "index": -1
  },
  "k20d21508277536715": {
    "active": true,
    "title": "Default",
    "notes": "These are the settings that are used when no patterns match a URL.",
    "color": "#0055E5",
    "type": 5,
    "whitePatterns": [
      {
        "title": "all URLs",
        "active": true,
        "pattern": "*",
        "type": 1,
        "protocols": 1
      }
    ],
    "blackPatterns": [],
      "index": 9007199254740991
  },
  "logging": {
    "active": true,
    "maxSize": 500
  },
  "mode": "patterns",
  "browserVersion": "82.0.3",
  "foxyProxyVersion": "7.5.1",
  "foxyProxyEdition": "standard"
}
```

6. On the **Import Settings from FoxyProxy 6.0+** pane, choose **Import Settings** and select the `mwaa-proxy.json` file.
7. Choose **OK**.

## Step six: Open the Apache Airflow UI

The following steps describe how to open your Apache Airflow UI.

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose **Open Airflow UI**.

## What's next?

- Learn how to run Airflow CLI commands on an SSH tunnel to a bastion host in [Apache Airflow CLI command reference](airflow-cli-command-reference.md "airflow-cli-command-reference.md").
- Learn how to upload DAG code to your Amazon S3 bucket in [Adding or updating DAGs](configuring-dag-folder.md "configuring-dag-folder.md").
