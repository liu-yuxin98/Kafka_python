# steps to use Kafka in windows with python

# download and install kafka from https://kafka.apache.org/downloads

1. Go to the Apache Kafka website (https://kafka.apache.org/downloads) and download the binary distribution of Kafka.
2. Extract the downloaded file to a directory of your choice. I extract it to F:\
3. Kafka requires Java to run, so make sure you have Java installed on your machine. You can download Java from the Oracle
   website (https://www.oracle.com/java/technologies/javase-downloads.html) and install it.
4. Open a command prompt or terminal window and navigate to the Kafka directory you extracted in step 2.
5. To start the Kafka server, run the following command:

```shell
bin\windows\kafka-server-start.bat config\server.properties
```

This will start the Kafka server on the default port 9092. 6. To check if Kafka is running, you can use the following command:

```shell
telnet localhost 9092
```

If Kafka is running, you should see output that looks like this:

```
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
```

if telnet command is not valid in cmd
typle in flollwoing and restart cmd:

```
pkgmgr /iu:"TelnetClient"
```

you can also use

```
bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
```

in you kafka source dir

# download and install zookeeper from https://zookeeper.apache.org/releases.html

# download and install gradle https://gradle.org/install/
