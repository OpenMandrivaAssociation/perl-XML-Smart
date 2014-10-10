%define module 	XML-Smart
%define upstream_version 1.78

Summary:	A Smart, easy and powerful way to access/create XML files/data
Name: 		perl-%{module}
Version: 	%perl_convert_version %{upstream_version}
Release: 	2
License: 	GPL
Url:		http://search.cpan.org/dist/%{module}
Group:		Development/Perl
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/XML/XML-Smart-%{upstream_version}.tar.gz
BuildRequires:	perl-devel, perl-Object-MultiType
BuildArch:	noarch

%description
This module has an easy way to access/create XML data. It's based on the HASH
tree that is made of the XML data, and enable a dynamic access to it with the
Perl syntax for Hashe and Array, without needing to care if you have a Hashe or
an Array in the tree. In other words, each point in the tree work as a Hash 
and an Array at the same time!
%prep
%setup -q -n %{module}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%{__make} test <<EOF
n
EOF

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML/Smart
%{perl_vendorlib}/XML/Smart.pm



%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 1.6.9-7mdv2011.0
+ Revision: 664893
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.6.9-6mdv2010.0
+ Revision: 430666
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.6.9-5mdv2009.0
+ Revision: 258881
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.6.9-4mdv2009.0
+ Revision: 246784
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 1.6.9-2mdv2008.1
+ Revision: 166717
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.9-2mdv2008.0
+ Revision: 87113
- rebuild


* Mon Aug 21 2006 Erwan Velu <erwan@seanodes.com> 1.6.9-1mdv2007.0
- Initial release



