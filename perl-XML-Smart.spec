%define module 	XML-Smart
%define version 1.6.9
%define release %mkrel 1

Summary:	A Smart, easy and powerful way to access/create XML files/data.
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Url:		http://search.cpan.org/dist/%{module}
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel, perl-Object-MultiType
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
This module has an easy way to access/create XML data. It's based on the HASH
tree that is made of the XML data, and enable a dynamic access to it with the
Perl syntax for Hashe and Array, without needing to care if you have a Hashe or 
an Array in the tree. In other words, each point in the tree work as a Hash 
and an Array at the same time!
%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%{__make} test <<EOF
n
EOF

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML/Smart
%{perl_vendorlib}/XML/Smart.pm

