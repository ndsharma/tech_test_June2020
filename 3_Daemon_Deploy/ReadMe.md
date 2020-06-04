Author - Nitin Dutt Sharma
Document Version - 1.0
Date - 03/06/2020

Purpose
=========

This document provides relevant information about the software versions installed, the dependencies of files present and how these file interact with each other.

Objective
----------
The objective of this development is to containerise a daemon that listens on port 3000 and deploy it into a kubernetes cluster.

Requirements
-------------
I used docker version 19+ and minikube version: v1.11.0 on Windows 10 machine but code should work on other type of kubernetes installation as well.

Files
----------
1) Dockerfile - this file builds the docker image which is basically a tomcat image with some modified server.xml, tomcat-users.xml and sample.war  file copied to the container. The created image has been pushed to the docker registry so this step is not needed to be run again.
2) server.xml - is a Tomcat server.xml file with connector port modified to port 3000 to meet the requirement.
3) sample.war - is a simple Tomcat war file to get the UI to demonstrate that the app is listening on port 3000.
4) tomcat-users.xml - File contains the information and credentials about tomcat users and roles. The username and password for manager and admin GUI is "tomcat"
5) deployment.yaml - This file actually deploys the pods to the kubernetes cluster.
6) service.yaml - Service yaml file to expose the container port 3000 to node port 30000 and give app cluster a single ip for further addition or deletion of nodes.

Execution
----------
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Optional - To create the docker image from the Dockerfile
docker build -t daemon3000:1.0
dockdr run -d -p hostport:containerport ImageID
