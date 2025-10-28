# Creating Kinesis Agent for Windows Plugins

For most situations, creating an Amazon Kinesis Agent for Microsoft Windows plugin is not necessary. Kinesis Agent for Windows is highly
configurable and contains powerful sources and sinks, such as `DirectorySource`
and `KinesisStream`, which are sufficient for most scenarios. For details about
the existing sources and sinks, see [Configuring Amazon Kinesis Agent for Microsoft Windows](configuring-kinesis-agent-windows.md "configuring-kinesis-agent-windows.md").

For unusual scenarios, it might be necessary to extend Kinesis Agent for Windows using a custom plugin. Some
of these scenarios include the following:

- Packaging a complex `DirectorySource` declaration using the
  `Regex` or `Delimited` record parsers so that it is easy
  to apply in many different kinds of configuration files.
- Creating a novel source that is not file based or that exceeds the parsing
  capabilities provided by the existing record parsers.
- Creating a sink for an AWS service that is not currently supported.

###### Topics

- [Getting Started with Kinesis Agent for Windows
  Plugins](#creating-kinesis-agent-windows-plugins-overview "#creating-kinesis-agent-windows-plugins-overview")
- [Implementing Kinesis Agent for Windows Plugin
  Factories](#creating-kinesis-agent-windows-plugins-factory "#creating-kinesis-agent-windows-plugins-factory")
- [Implementing Kinesis Agent for Windows Plugin
  Sources](#creating-kinesis-agent-windows-plugins-source "#creating-kinesis-agent-windows-plugins-source")
- [Implementing Kinesis Agent for Windows Plugin
  Sinks](#creating-kinesis-agent-windows-plugins-sink "#creating-kinesis-agent-windows-plugins-sink")

## Getting Started with Kinesis Agent for Windows

Plugins

There is nothing special about custom plugins. All the existing sources and sinks use
the same mechanisms that custom plugins use to load when Kinesis Agent for Windows starts up, and they
instantiate relevant plugins after reading the `appsettings.json`
configuration file.

When Kinesis Agent for Windows starts up, the following sequence occurs:

1. Kinesis Agent for Windows scans assemblies in the installation directory
   (`%PROGRAMFILES%\Amazon\AWSKinesisTap`) for classes that
   implement the `IFactory<T>` interface defined in the
   `Amazon.KinesisTap.Core` assembly. This interface is
   defined in
   `Amazon.KinesisTap.Core\Infrastructure\IFactory.cs` in
   the Kinesis Agent for Windows source code.
2. Kinesis Agent for Windows loads the assemblies containing these classes and invokes the
   `RegisterFactory` method on these classes.
3. Kinesis Agent for Windows loads the `appsettings.json` configuration file. For
   each source and sink in the configuration file, the `SourceType` and
   `SinkType` key-value pairs are examined. If there are factories
   registered with the same name as the values of the `SourceType` and
   `SinkType` key-value pairs, the `CreateInstance`
   method is invoked on those factories. The `CreateInstance` method is
   passed configuration and other information as an `IPluginContext`
   object. The `CreateInstance` method is responsible for configuring
   and initializing the plugin.

For a plugin to work correctly, there must be a registered factory class that creates
the plugin, and the plugin class itself must be defined.

The Kinesis Agent for Windows source code is located at [Kinesis Agent windows](https://github.com/awslabs/kinesis-agent-windows "https://github.com/awslabs/kinesis-agent-windows").

## Implementing Kinesis Agent for Windows Plugin

Factories

Follow these steps to implement a Kinesis Agent for Windows plugin factory.

###### To create a Kinesis Agent for Windows plugin factory

1. Create a C# library project targeting .NET Framework 4.6.
2. Add a reference to the `Amazon.KinesisTap.Core` assembly.
   This assembly is located in the `%PROGRAMFILES%\Amazon\AWSKinesisTap` directory
   after Kinesis Agent for Windows installation.
3. Use `NuGet` to install the
   `Microsoft.Extensions.Configuration.Abstractions`
   package.
4. Use `NuGet` to install the `System.Reactive`
   package.
5. Use `NuGet` to install the
   `Microsoft.Extensions.Logging` package.
6. Create a factory class that implements either
   `IFactory<IEventSource>` for sources or
   `IFactory<IEventSink>` for sinks. Add the
   `RegisterFactory` and `CreateInstance` methods.

For example, the following code creates a Kinesis Agent for Windows plugin factory that creates a
source that generates random data:

```
using System;
using Amazon.KinesisTap.Core;
using Microsoft.Extensions.Configuration;

namespace MyCompany.MySources
{
    public class RandomSourceFactory : IFactory<ISource>
    {
        public void RegisterFactory(IFactoryCatalog<ISource> catalog)
        {
            catalog.RegisterFactory("randomsource", this);
        }

        public ISource CreateInstance(string entry, IPlugInContext context)
        {
            IConfiguration config = context.Configuration;

            switch (entry.ToLower())
            {
                case "randomsource":
                    string rateString = config["Rate"];
                    string maxString = config["Max"];
                    TimeSpan rate;
                    int max;

                    if (string.IsNullOrWhiteSpace(rateString))
                    {
                        rate = TimeSpan.FromSeconds(30);
                    }
                    else
                    {
                        if (!TimeSpan.TryParse(rateString, out rate))
                        {
                            throw new Exception($"Rate {rateString} is invalid for RandomSource.");
                        }
                    }

                    if (string.IsNullOrWhiteSpace(maxString))
                    {
                        max = 1000;
                    }
                    else
                    {
                        if (!int.TryParse(maxString, out max))
                        {
                            throw new Exception($"Max {maxString} is invalid for RandomSource.");
                        }
                    }

                    return new RandomSource(rate, max, context);
                default:
                    throw new ArgumentException($"Source {entry} is not recognized.", entry);
            }
        }
    }
}
```

The `switch` statement is used in the `CreateInstance`
method in case you eventually want to enhance the factory to create different
kinds of instances.

To create a sink factory that creates a sink that does nothing, use a class
similar to the following:

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Amazon.KinesisTap.Core;
using Microsoft.Extensions.Configuration;

namespace MyCompany.MySinks
{
    public class NullSinkFactory : IFactory<IEventSink>
    {
        public void RegisterFactory(IFactoryCatalog<IEventSink> catalog)
        {
            catalog.RegisterFactory("nullsink", this);
        }

        public IEventSink CreateInstance(string entry, IPlugInContext context)
        {
            IConfiguration config = context.Configuration;

            switch (entry.ToLower())
            {
                case "nullsink":
                    return new NullSink(context);
                default:
                    throw new Exception("Unrecognized sink type {entry}.");
            }
        }
    }
}
```

## Implementing Kinesis Agent for Windows Plugin

Sources

Follow these steps to implement a Kinesis Agent for Windows plugin source.

###### To create a Kinesis Agent for Windows plugin source

1. Add a class that implements the `IEventSource<out T>`
   interface to the previously created project for the source.

For example, use the following code to define a source that generates random
data:

```
using System;
using System.Reactive.Subjects;
using System.Timers;
using Amazon.KinesisTap.Core;
using Microsoft.Extensions.Logging;

namespace MyCompany.MySources
{
    public class RandomSource : EventSource<RandomData>, IDisposable
    {
        private TimeSpan _rate;
        private int _max;
        private Timer _timer = null;
        private Random _random = new Random();
        private ISubject<IEnvelope<RandomData>> _recordSubject = new Subject<IEnvelope<RandomData>>();



        public RandomSource(TimeSpan rate, int max, IPlugInContext context) : base(context)
        {
            _rate = rate;
            _max = max;
        }

        public override void Start()
        {
            try
            {
                CleanupTimer();
                _timer = new Timer(_rate.TotalMilliseconds);
                _timer.Elapsed += (Object source, ElapsedEventArgs args) =>
                {
                    var data = new RandomData()
                    {
                        RandomValue = _random.Next(_max)
                    };
                    _recordSubject.OnNext(new Envelope<RandomData>(data));
                };
                _timer.AutoReset = true;
                _timer.Enabled = true;
                _logger?.LogInformation($"Random source id {this.Id} started with rate {_rate.TotalMilliseconds}.");
            }
            catch (Exception e)
            {
                _logger?.LogError($"Exception during start of RandomSource id {this.Id}: {e}");
            }
        }

        public override void Stop()
        {
            try
            {
                CleanupTimer();
                _logger?.LogInformation($"Random source id {this.Id} stopped.");
            }
            catch (Exception e)
            {
                _logger?.LogError($"Exception during stop of RandomSource id {this.Id}: {e}");
            }
        }

        private void CleanupTimer()
        {
            if (_timer != null)
            {
                _timer.Enabled = false;
                _timer?.Dispose();
                _timer = null;
            }
        }

        public override IDisposable Subscribe(IObserver<IEnvelope<RandomData>> observer)
        {
            return this._recordSubject.Subscribe(observer);
        }

        public void Dispose()
        {
            CleanupTimer();
        }
    }
}
```

In this example, the `RandomSource` class inherits from the
`EventSource<T>` class because it provides the
`Id` property. Although this example doesn't support bookmarking,
this base class is also useful for implementing that functionality. Envelopes
provide a way to store metadata and wrap arbitrary data for streaming to sinks.
The `RandomData` class is defined in the next step and represents the
type of output object from this source. 2. Add a class to the previously defined project that contains the data that is
streamed from the source.

For example, a container for random data could be defined as the
following:

```
namespace MyCompany.MySources
{
    public class RandomData
    {
        public int RandomValue { get; set; }
    }
}
```

3. Compile the previously defined project.
4. Copy the assembly to the installation directory for Kinesis Agent for Windows.
5. Create or update an `appsettings.json` configuration file that uses
   the new source, and place it in the installation directory for Kinesis Agent for Windows.
6. Stop and then start Kinesis Agent for Windows.
7. Check the current Kinesis Agent for Windows log file (usually located in the
   `%PROGRAMDATA%\Amazon\AWSKinesisTap\logs` directory) to
   ensure that there are no issues with the custom source plugin.
8. Ensure that data is arriving at the desired AWS service.

For an example of how to extend the `DirectorySource` functionality to
implement parsing of a particular log format, see
`Amazon.KinesisTap.Uls\UlsSourceFactory.cs` and
`Amazon.KinesisTap.Uls\UlsLogParser.cs` in the Kinesis Agent for Windows source
code.

For an example of how to create a source that provides bookmarking functionality, see
`Amazon.KinesisTap.Windows\WindowsSourceFactory.cs` and
`Amazon.KinesisTap.Windows\EventLogSource.cs` in the Kinesis Agent for Windows source
code.

## Implementing Kinesis Agent for Windows Plugin

Sinks

Follow these steps to implement a Kinesis Agent for Windows plugin sink.

###### To create a Kinesis Agent for Windows plugin sink

1. Add a class to the previously defined project that implements the
   `IEventSink` interface.

For example, the following code implements a sink that does nothing other than
log the arrival of records, which are then discarded.

```
using Amazon.KinesisTap.Core;
using Microsoft.Extensions.Logging;

namespace MyCompany.MySinks
{
    public class NullSink : EventSink
    {
        public NullSink(IPlugInContext context) : base(context)
        {
        }

        public override void OnNext(IEnvelope envelope)
        {
            _logger.LogInformation($"Null sink {Id} received {GetRecord(envelope)}.");
        }

        public override void Start()
        {
            _logger.LogInformation($"Null sink {Id} starting.");
        }

        public override void Stop()
        {
            _logger.LogInformation($"Null sink {Id} stopped.");
        }
    }
}
```

In this example, the `NullSink` sink class inherits from the
`EventSink` class because it provides the ability to transform
records into different serialization formats such as JSON and XML. 2. Compile the previously defined project. 3. Copy the assembly to the installation directory for Kinesis Agent for Windows. 4. Create or update an `appsettings.json` configuration file that uses
the new sink, and place it in the installation directory for Kinesis Agent for Windows. For example,
to use the `RandomSource` and `NullSink` custom plugins,
you could use the following `appsettings.json` configuration
file:

```
{
  "Sources": [
  {
	"Id": "MyRandomSource",
	"SourceType": "RandomSource",
	"Rate": "00:00:10",
	"Max": 50
  }

  ],
  "Sinks": [
  {
    "Id": "MyNullSink",
	"SinkType": "NullSink",
	"Format": "json"
  }
  ],
  "Pipes": [
    {
	  "Id": "MyRandomToNullPipe",
	  "SourceRef": "MyRandomSource",
	  "SinkRef": "MyNullSink"
	}
  ]
}
```

This configuration creates a source that sends an instance of
`RandomData` with a `RandomValue` set to a random
number between 0 and 50 every 10 seconds. It creates a sink that transforms the
incoming `RandomData` instances to JSON, logs that JSON, and then
discards the instances. Be sure to include both example factories, the
`RandomSource` source class, and the `NullSink` sink
class in the previously defined project to use the example configuration
file. 5. Stop and then start Kinesis Agent for Windows. 6. Check the current Kinesis Agent for Windows log file (usually located in the
`%PROGRAMDATA%\Amazon\AWSKinesisTap\logs` directory) to
ensure that there are no issues with the custom sink plugin. 7. Ensure that data is arriving at the desired AWS service. Because the example
`NullSink` does not stream to an AWS service, you can verify the
correct operation of the sink by looking for log messages indicating that
records have been received.

For example, you can see a log file similar to the following:

```
2018-10-18 12:36:36.3647 Amazon.KinesisTap.Hosting.LogManager INFO Registered factory Amazon.KinesisTap.AWS.AWSEventSinkFactory.
2018-10-18 12:36:36.4018 Amazon.KinesisTap.Hosting.LogManager INFO Registered factory Amazon.KinesisTap.Windows.PerformanceCounterSinkFactory.
2018-10-18 12:36:36.4018 Amazon.KinesisTap.Hosting.LogManager INFO Registered factory MyCompany.MySinks.NullSinkFactory.
2018-10-18 12:36:36.6926 Amazon.KinesisTap.Hosting.LogManager INFO Registered factory Amazon.KinesisTap.Core.DirectorySourceFactory.
2018-10-18 12:36:36.6926 Amazon.KinesisTap.Hosting.LogManager INFO Registered factory Amazon.KinesisTap.ExchangeSource.ExchangeSourceFactory.
2018-10-18 12:36:36.6926 Amazon.KinesisTap.Hosting.LogManager INFO Registered factory Amazon.KinesisTap.Uls.UlsSourceFactory.
2018-10-18 12:36:36.6926 Amazon.KinesisTap.Hosting.LogManager INFO Registered factory Amazon.KinesisTap.Windows.WindowsSourceFactory.
2018-10-18 12:36:36.6926 Amazon.KinesisTap.Hosting.LogManager INFO Registered factory MyCompany.MySources.RandomSourceFactory.
2018-10-18 12:36:36.9601 Amazon.KinesisTap.Hosting.LogManager INFO Registered factory Amazon.KinesisTap.Core.Pipes.PipeFactory.
2018-10-18 12:36:37.4694 Amazon.KinesisTap.Hosting.LogManager INFO Registered factory Amazon.KinesisTap.AutoUpdate.AutoUpdateFactory.
2018-10-18 12:36:37.4807 Amazon.KinesisTap.Hosting.LogManager INFO Performance counter sink  started.
2018-10-18 12:36:37.6250 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink starting.
2018-10-18 12:36:37.6250 Amazon.KinesisTap.Hosting.LogManager INFO Connected source MyRandomSource to sink MyNullSink
2018-10-18 12:36:37.6333 Amazon.KinesisTap.Hosting.LogManager INFO Random source id MyRandomSource started with rate 10000.
2018-10-18 12:36:47.8084 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":14}.
2018-10-18 12:36:57.6339 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":5}.
2018-10-18 12:37:07.6490 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":9}.
2018-10-18 12:37:17.6494 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":47}.
2018-10-18 12:37:27.6520 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":25}.
2018-10-18 12:37:37.6676 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":21}.
2018-10-18 12:37:47.6688 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":29}.
2018-10-18 12:37:57.6700 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":22}.
2018-10-18 12:38:07.6838 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":32}.
2018-10-18 12:38:17.6848 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":12}.
2018-10-18 12:38:27.6866 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":46}.
2018-10-18 12:38:37.6880 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":48}.
2018-10-18 12:38:47.6893 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":39}.
2018-10-18 12:38:57.6906 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":18}.
2018-10-18 12:39:07.6995 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":6}.
2018-10-18 12:39:17.7004 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":0}.
2018-10-18 12:39:27.7021 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":3}.
2018-10-18 12:39:37.7023 Amazon.KinesisTap.Hosting.LogManager INFO Null sink MyNullSink received {"RandomValue":19}.
```

If you are creating a sink that accesses AWS services, there are base classes that you
might find helpful. For a sink that uses the `AWSBufferedEventSink` base
class, see `Amazon.KinesisTap.AWS\CloudWatchLogsSink.cs` in the
source code for Kinesis Agent for Windows.
