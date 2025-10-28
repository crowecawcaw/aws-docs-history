# Connecting to Amazon Neptune databases using IAM

authentication with Gremlin Go

## Overview

This guide demonstrates how to connect to a Amazon Neptune database with IAM authentication
enabled using the Gremlin Go driver, with Signature Version 4 authentication and the AWS SDK for GO v2.

## Prerequisites

- An Amazon Neptune cluster with IAM authentication enabled.
- Go 1.22 or later (refer to minimal supported versions for
  [Gremlin Go](https://pkg.go.dev/github.com/apache/tinkerpop/gremlin-go/v3/driver "https://pkg.go.dev/github.com/apache/tinkerpop/gremlin-go/v3/driver") and
  [AWS SDK for Go v2](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2 "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2")).
- AWS credentials configured (via environment variables, shared credentials file, or IAM role)

## Create a basic connection

Use the following code example as guidance on how to establish a basic connection with IAM authentication
using the Gremlin Go driver.

```
package main

import (
	"context"
	"fmt"
	"github.com/aws/aws-sdk-go-v2/config"
	"net/http"
	"strings"
	"time"

	gremlingo "github.com/apache/tinkerpop/gremlin-go/v3/driver"
	v4 "github.com/aws/aws-sdk-go-v2/aws/signer/v4"
)

const emptyStringSHA256 = `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

func main() {
	neptuneEndpoint := "you.cluster.endpoint.neptune.amazonaws.com"
	connString := "wss://" + neptuneEndpoint + ":8182/gremlin"
	service := "neptune-db"
	defaultRegion := "us-east-1"

	// Create request to sign
	req, err := http.NewRequest(http.MethodGet, connString, strings.NewReader(""))
	if err != nil {
		fmt.Println(err)
		return
	}

	// Loads the default config with default credentials provider
	// See https://github.com/aws/aws-sdk-go-v2 for additional docs on API usage
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		fmt.Println(err)
		return
	}
	// Retrieve loaded credentials
	cr, err := cfg.Credentials.Retrieve(context.TODO())
	if err != nil {
		fmt.Println(err)
		return
	}

	region := defaultRegion
	if cfg.Region != "" {
		// region set inside config profile, or via AWS_REGION or AWS_DEFAULT_REGION environment variable will be loaded
		region = cfg.Region
	}

	signer := v4.NewSigner()
	// Sign request
	err = signer.SignHTTP(context.TODO(), cr, req, emptyStringSHA256, service, "us-east-2", time.Now())
	if err != nil {
		fmt.Println(err)
		return
	}

	// Pass the signed request header into gremlingo.HeaderAuthInfo()
	driverRemoteConnection, err := gremlingo.NewDriverRemoteConnection(connString,
		func(settings *gremlingo.DriverRemoteConnectionSettings) {
			settings.TraversalSource = "g"
			settings.AuthInfo = gremlingo.HeaderAuthInfo(req.Header)
			// settings.TlsConfig = &tls.Config{InsecureSkipVerify: true} // Use this only if you're on a Mac running Go 1.18+ doing local dev. See https://github.com/golang/go/issues/51991
		})
	if err != nil {
		fmt.Println(err)
		return
	}

	// Cleanup
	defer driverRemoteConnection.Close()

	// Creating graph traversal
	g := gremlingo.Traversal_().WithRemote(driverRemoteConnection)

	// Query execution
	count, err := g.V().Limit(5).Count().Next()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Vertex count:", *count)
}
```

##

Gremlin Go Dynamic Credential Refresh

Gremlin Go has DynamicAuth which allows the injection of a function pointer to retrieve credentials and generate
the header, which prevents header expiry with long-running connections.

```
package main

import (
	"context"
	"crypto/tls"
	"fmt"
	"github.com/aws/aws-sdk-go-v2/config"
	"net/http"
	"strings"
	"time"

	gremlingo "github.com/apache/tinkerpop/gremlin-go/v3/driver"
	v4 "github.com/aws/aws-sdk-go-v2/aws/signer/v4"
)

const emptyStringSHA256 = `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

func main() {
	neptuneEndpoint := "you.cluster.endpoint.neptune.amazonaws.com"
	connString := "wss://" + neptuneEndpoint + ":8182/gremlin"
	service := "neptune-db"
	defaultRegion := "us-east-1"

	//Create the request to sign
	req, err := http.NewRequest(http.MethodGet, connString, strings.NewReader(""))
	if err != nil {
		fmt.Println(err)
		return
	}

	// Loads the default config with default credentials provider
	// See https://github.com/aws/aws-sdk-go-v2 for additional docs on API usage
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		fmt.Println(err)
		return
	}

	region := defaultRegion
	if cfg.Region != "" {
		// region set inside config profile, or via AWS_REGION or AWS_DEFAULT_REGION environment variable will be loaded
		region = cfg.Region
	}

	signer := v4.NewSigner()

	// This is the function that will be used for dynamic refreseh of credentials and signed headers
	gen := func() gremlingo.AuthInfoProvider {
		// Retrieve loaded credentials
		cr, err := cfg.Credentials.Retrieve(context.TODO())
		fmt.Println("AWS Credentials: ", cr)
		if err != nil {
			fmt.Println(err)
			return
		}
		// Sign request
		err = signer.SignHTTP(context.TODO(), cr, req, emptyStringSHA256, service, region, time.Now())
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Println(req.Header)
		return gremlingo.HeaderAuthInfo(req.Header)
	}

	// Pass the function into gremlingo.NewDynamicAuth(), which will generate the AuthInfoProvider to pass into gremlingo.DriverRemoteConnectionSettings below
	auth := gremlingo.NewDynamicAuth(gen)

	driverRemoteConnection, err := gremlingo.NewDriverRemoteConnection(connString,
		func(settings *gremlingo.DriverRemoteConnectionSettings) {
			settings.TraversalSource = "g"
			settings.AuthInfo = auth
			// settings.TlsConfig = &tls.Config{InsecureSkipVerify: true} // Use this only if you're on a Mac running Go 1.18+ doing local dev. See https://github.com/golang/go/issues/51991

		})
	if err != nil {
		fmt.Println(err)
		return
	}

	// Cleanup
	defer driverRemoteConnection.Close()

	// Creating graph traversal
	g := gremlingo.Traversal_().WithRemote(driverRemoteConnection)

	// Query execution
	count, err := g.V().Limit(5).Count().Next()
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Vertex count:", *count)
}
```
