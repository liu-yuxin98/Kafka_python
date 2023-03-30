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

# download and install zookeeper

1. Go to the Apache ZooKeeper website (https://zookeeper.apache.org/releases.html) and download the binary distribution of ZooKeeper.
2. Extract the downloaded file to a directory of your choice. For example, you can extract it to C:\zookeeper.
3. ZooKeeper requires Java to run, so make sure you have Java installed on your machine. You can download Java from the Oracle website (https://www.oracle.com/java/technologies/javase-downloads.html) and install it.
4. In the ZooKeeper directory, rename the conf\zoo_sample.cfg file to conf\zoo.cfg. This is the configuration file that ZooKeeper will use.
5. Open a command prompt or terminal window and navigate to the ZooKeeper directory.
6. To start ZooKeeper, run the following command:

```
bin\zkServer.cmd
```

This will start ZooKeeper on the default port 2181. If you are on a Unix-based system, use the following command instead:

```
bin/zkServer.sh start
```

7. To check if ZooKeeper is running, you can use the following command:

```
telnet localhost 2181
```

If ZooKeeper is running, you should see output that looks like this:

```
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
```

Alternatively, you can use the following command to check if ZooKeeper is running:

```
bin\zkCli.cmd -server localhost:2181
```

# download and install gradle https://gradle.org/install/

1. Go to the Gradle website (https://gradle.org/releases/) and download the binary distribution of Gradle.
2. Extract the downloaded file to a directory of your choice. For example, you can extract it to C:\gradle.
3. Add the Gradle bin directory to your system's path environment variable. To do this, follow these steps:
   3.1 Open the Control Panel and navigate to System and Security > System > Advanced system settings > Environment Variables.
   In the System Variables section, scroll down and find the Path variable, then click the Edit button.
   3.2 Click the New button and add the path to the Gradle bin directory. For example, if you extracted Gradle to C:\gradle, add C:\gradle\bin to the Path variable.
   3.3 Click OK to close all the windows.
4. To check if Gradle is installed correctly, open a command prompt or terminal window and run the following command:

```
gradle -v
```

This command will display the version of Gradle you have installed, along with some other information.

If you see output that looks like this:

```
------------------------------------------------------------
Gradle x.x.x
------------------------------------------------------------

Build time:   ...
...
```

It means Gradle is installed correctly.
