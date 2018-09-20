# Microsoft Powershell Ubuntu image
FROM microsoft/powershell
LABEL version=lastest

USER root
RUN apt-get update -y
RUN apt-get install wget curl -y

# Import the public repository GPG keys
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl -o /etc/apt/sources.list.d/microsoft.list https://packages.microsoft.com/config/ubuntu/16.04/prod.list
RUN apt-get update
RUN apt-get install mssql-cli -y