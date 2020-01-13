Name:           metasploit-release
Version:        8
Release:        1%{?dist}
Summary:        Metasploit Framework package repository configuration

License:        BSD-3-Clause
URL:            https://rpm.metasploit.com/
Source0:        metasploit-framework.repo
Source1:	RPM-GPG-KEY-Metasploit

BuildArch:	noarch

%description
This package contains repository configuration for Metasploit Framework.

%prep

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

%files
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/RPM-GPG-KEY-*

%changelog
* Mon Jan 13 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> 8-1
- Initial release.
