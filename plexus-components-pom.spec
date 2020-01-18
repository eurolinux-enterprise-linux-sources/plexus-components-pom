%global short_name plexus-components

Name:           %{short_name}-pom
Version:        1.2
Release:        7%{?dist}
Summary:        Plexus Components POM
BuildArch:      noarch
Group:          Development/Libraries
License:        ASL 2.0
URL:            http://plexus.codehaus.org/%{short_name}
Source0:        http://repo.maven.apache.org/maven2/org/codehaus/plexus/%{short_name}/%{version}/%{short_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  plexus-pom

%description
This package provides Plexus Components parent POM used by different
Plexus packages.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2-7
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Dec  7 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-4
- Build with xmvn

* Tue Nov 13 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-3
- Add missing BR/R: plexus-pom

* Mon Nov 12 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-2
- Install LICENSE file

* Wed Oct 31 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Initial packaging
