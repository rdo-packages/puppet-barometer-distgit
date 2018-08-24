Name:           puppet-barometer
Version:        1.0
Release:        1%{?dist}
Summary:        Scripts to create puppet-baromter rpm.

License:        ASL 2.0
URL:            https://wiki.opnfv.org/display/fastpath/%{name}+Home
Source0:        https://github.com/opnfv/puppet-barometer/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet-java
Requires:       puppet >= 2.7.0

%description
Puppet module to support Baromter on Apex by having the puppet-module built into RDO.

%prep
%setup -q -n %{name}-%{version}
find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/puppet-barometer-1.0-1.el7.centos.x86_64/usr/share/opnfv/puppet-barometer
cp -rp * %{buildroot}/%{_datadir}/puppet-barometer-1.0-1.el7.centos.x86_64/usr/share/opnfv/puppet-barometer


%files
%{_datadir}/puppet-barometer-1.0-1.el7.centos.x86_64/usr/share/opnfv/puppet-barometer
%doc



%changelog
