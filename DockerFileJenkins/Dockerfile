# From the Jenkins supported version
FROM jenkins/jenkins:lts
LABEL version=0.1

#using root for installation
USER root
RUN apt-get update -y


#Plug-ins Installation
    #Install Kubernetes pluginin
RUN /usr/local/bin/install-plugins.sh kubernetes:1.12.4

    #Install ssh plug-in
RUN /usr/local/bin/install-plugins.sh ssh-slaves:1.28

    #Install PowerShell plug-in
RUN /usr/local/bin/install-plugins.sh powershell:1.3


    # Install git for version control
RUN /usr/local/bin/install-plugins.sh git:3.9.1

    # Install docker plug-in
RUN /usr/local/bin/install-plugins.sh docker-plugin:1.1.5


    # Misc plug-ins
RUN /usr/local/bin/install-plugins.sh cloudbees-folder:6.5.1
RUN /usr/local/bin/install-plugins.sh antisamy-markup-formatter:1.5
RUN /usr/local/bin/install-plugins.sh credentials-binding:1.16
RUN /usr/local/bin/install-plugins.sh workflow-aggregator:2.5
RUN /usr/local/bin/install-plugins.sh github-branch-source:2.3.3
RUN /usr/local/bin/install-plugins.sh pipeline-github-lib:1.0
RUN /usr/local/bin/install-plugins.sh pipeline-stage-view:2.10


#update container one more time
RUN apt-get update -y


#Dropping back to jenkins user security reasons
USER jenkins