%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.01-2
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Telugu
%define languagecode te
%define lc_ctype te_IN

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.60.0
Release:       %mkrel 6
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   LGPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-6mdv2011.0
+ Revision: 616610
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.60.0-5mdv2010.0
+ Revision: 423967
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 0.60.0-4mdv2009.0
+ Revision: 226183
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.60.0-3mdv2008.1
+ Revision: 182658
- provide enchant-dictionary

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.60.0-2mdv2008.1
+ Revision: 140690
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/


* Mon Mar 05 2007 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-2mdv2007.0
+ Revision: 132951
- Import aspell-te

* Mon Mar 05 2007 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Mon Nov 28 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.60.0-1mdk
- first version

