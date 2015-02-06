%define upstream_name    NEXT
%define upstream_version 0.65

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl5 implementation of NEXT (RFC190)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
NEXT.pm adds a pseudoclass named 'NEXT' to any program that uses it. If a
method 'm' calls '$self->NEXT::m()', the call to 'm' is redispatched as if
the calling method had not originally been found.

In other words, a call to '$self->NEXT::m()' resumes the depth-first,
left-to-right search of '$self''s class hierarchy that resulted in the
original call to 'm'.

Note that this is not the same thing as '$self->SUPER::m()', which begins a
new dispatch that is restricted to searching the ancestors of the current
class. '$self->NEXT::m()' can backtrack past the current class -- to look
for a suitable method in other ancestors of '$self' -- whereas
'$self->SUPER::m()' cannot.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.650.0-2mdv2011.0
+ Revision: 656947
- rebuild for updated spec-helper

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.650.0-1mdv2011.0
+ Revision: 597193
- update to 0.65

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.640.0-2mdv2011.0
+ Revision: 552184
- rebuild

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.640.0-1mdv2010.0
+ Revision: 395221
- import perl-NEXT


* Sun Jul 12 2009 cpan2dist 0.64-1mdv
- initial mdv release, generated with cpan2dist
