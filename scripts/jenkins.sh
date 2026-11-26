#!bin/bash
sudo apt update

sudo apt install openjdk-8-jdk -y
https://pkg.jenkins.io/
https://pkg.jenkins.io/debian-stable/
sudo systemctl start jenkins

sudo ststemctl enable jenkins

sudo systemctl status jenkins

##installing docker

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker $USER
sudo usermod -aG docker jenkins

newgrp docker
sudo apt install awscli -y
sudo usermod -a -G docker jenkins

#aws configuration and restarts jenkins
aws configure

#now setup elastic IP ON AWS

###For getting the admin password for jenkins
sudo cat /var/lib/jenkins/secrets/initialAdminPassword