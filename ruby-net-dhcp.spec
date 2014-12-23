# TODO
# - use system oui.txt
#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	net-dhcp
Summary:	set of classes to low level handle the DHCP protocol
Name:		ruby-%{pkgname}
Version:	1.3.2
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	1aa897d190bad9bb11fb20b8a093658b
URL:		http://github.com/mjtko/net-dhcp-ruby
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-bueller
BuildRequires:	ruby-bundler
BuildRequires:	ruby-rake
BuildRequires:	ruby-rdoc
BuildRequires:	ruby-rspec
BuildRequires:	ruby-simplecov
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aim of Net::DHCP is to provide a set of classes to low level
handle the DHCP protocol (RFC2131, RFC2132, etc.). With Net::DHCP you
will be able to craft custom DHCP packages and have access to all the
fields defined for the protocol.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/net-dhcp
%{ruby_vendorlibdir}/net-dhcp.rb
%dir %{ruby_vendorlibdir}/net-dhcp
%{ruby_vendorlibdir}/net-dhcp/version.rb

%{ruby_vendorlibdir}/net/dhcp.rb
%dir %{ruby_vendorlibdir}/net/dhcp
%{ruby_vendorlibdir}/net/dhcp/constants.rb
%{ruby_vendorlibdir}/net/dhcp/core.rb
%{ruby_vendorlibdir}/net/dhcp/options.rb
%{ruby_vendorlibdir}/net/dhcp/oui.txt
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
