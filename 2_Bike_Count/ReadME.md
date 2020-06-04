Author - Nitin Dutt Sharma
Document Version - 1.0
Date - 03/06/2020

Purpose
=========

This document provides relevant information about the software versions installed, the dependencies of files present and how these file interact with each other.

Objective
----------
The objective of this development is to build a code that outputs how many Santander Cycles are available at the bike stand outside the Bank of England.

Requirements
-------------
The bash script can run on any RHEL based server but I used CentOS 7 based system. Script needs jq packages installed on the server using
"yum install jq"

Python script uses python version 3.6+. The requests and json libraries should be present on the server with python version 3.6+ installed.

Execution
----------
The script can be executed using following commands. Bash script needs to me made executable using
chmod +x bike_count.sh

./bike_count.sh
python3 bike_count.py
