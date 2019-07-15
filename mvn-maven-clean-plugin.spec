#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-clean-plugin
Version  : 3.0.0
Release  : 2
URL      : https://github.com/apache/maven-clean-plugin/archive/maven-clean-plugin-3.0.0.tar.gz
Source0  : https://github.com/apache/maven-clean-plugin/archive/maven-clean-plugin-3.0.0.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/3.0.0/maven-clean-plugin-3.0.0.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/3.0.0/maven-clean-plugin-3.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-clean-plugin-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-clean-plugin package.
Group: Data

%description data
data components for the mvn-maven-clean-plugin package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-clean-plugin/3.0.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-clean-plugin/3.0.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-clean-plugin/3.0.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-clean-plugin/3.0.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-clean-plugin/3.0.0/maven-clean-plugin-3.0.0.jar
/usr/share/java/.m2/repository/org/apache/maven/plugins/maven-clean-plugin/3.0.0/maven-clean-plugin-3.0.0.pom
