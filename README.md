# CS445-FP
## Colin Brennan

## What is this repository for?
  - The project is setup to implement Gradle, Java 17, Python 3.8, as well as Apache Tomcat 10.
  - The assumption is that this is ran on a fresh installation of Ubuntu 20.04.3

## Set Up
1. Install Python 3.8 if not already installed as well as Java 17
```
sudo apt update
sudo apt-get install python3.8
sudo apt-get install python3-pip python-dev
sudo apt install openjdk-17-jdk
python3 --version
pip3 --version
```

2. Install Gradle 7.4.2
```
VERSION=7.4.2
wget https://services.gradle.org/distributions/gradle-${VERSION}-bin.zip -P /tmp
sudo unzip -d /opt/gradle /tmp/gradle-${VERSION}-bin.zip
```

3. Set up Enviornment Variables for new Gradle setup
```
sudo apt-get install vim
sudo vim /etc/profile.d/gradle.sh
```

Once the file is open you need to append the following into it.
```
export GRADLE_HOME=/opt/gradle/gradle-7.4.2
export PATH=${GRADLE_HOME}/bin:${PATH}
```

Change permissions and load enviornment variables
```
sudo chmod +x /etc/profile.d/gradle.sh
source /etc/profile.d/gradle.sh
gradle -v
```

4. Install Github and Clone Repo
```
sudo apt-get install git
mkdir Colin-FP
cd Colin-FP
git init
git pull https://github.com/cbrennan1/CS-445
```


