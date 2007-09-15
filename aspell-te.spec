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
Release:       %mkrel 2
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

