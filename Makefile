PKG_NAME := mvn-maven-clean-plugin
URL = https://github.com/apache/maven-clean-plugin/archive/maven-clean-plugin-3.0.0.tar.gz
ARCHIVES = https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/3.0.0/maven-clean-plugin-3.0.0.pom : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/3.0.0/maven-clean-plugin-3.0.0.jar :  https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/2.5/maven-clean-plugin-2.5.jar : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/2.5/maven-clean-plugin-2.5.pom :

include ../common/Makefile.common
