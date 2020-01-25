%define		status		stable
%define		pearname	Net_Growl
Summary:	%{pearname} - Send notifications to Growl from PHP on MACOSX
Name:		php-pear-%{pearname}
Version:	2.7.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	01af463327e325cef03ebe4eea3933ce
URL:		http://pear.php.net/package/Net_Growl/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Growl is a MACOSX application that listen to notifications sent by
applications and displays them on the desktop using different display
styles. Net_Growl offers the possibility to send notifications to
Growl from your PHP application through network communication using
UDP.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/Growl.php
%{php_pear_dir}/Net/Growl
%{php_pear_dir}/data/Net_Growl
