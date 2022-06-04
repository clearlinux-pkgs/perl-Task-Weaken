#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Task-Weaken
Version  : 1.06
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Weaken-1.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Weaken-1.06.tar.gz
Summary  : 'Ensure that a platform has weaken support'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Task-Weaken-license = %{version}-%{release}
Requires: perl-Task-Weaken-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Task-Weaken,
version 1.06:
Ensure that a platform has weaken support

%package dev
Summary: dev components for the perl-Task-Weaken package.
Group: Development
Provides: perl-Task-Weaken-devel = %{version}-%{release}
Requires: perl-Task-Weaken = %{version}-%{release}

%description dev
dev components for the perl-Task-Weaken package.


%package license
Summary: license components for the perl-Task-Weaken package.
Group: Default

%description license
license components for the perl-Task-Weaken package.


%package perl
Summary: perl components for the perl-Task-Weaken package.
Group: Default
Requires: perl-Task-Weaken = %{version}-%{release}

%description perl
perl components for the perl-Task-Weaken package.


%prep
%setup -q -n Task-Weaken-1.06
cd %{_builddir}/Task-Weaken-1.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Task-Weaken
cp %{_builddir}/Task-Weaken-1.06/LICENSE %{buildroot}/usr/share/package-licenses/perl-Task-Weaken/b768ef63d60a77d5a05a71fb19b6b1d2805ad944
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Task::Weaken.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Task-Weaken/b768ef63d60a77d5a05a71fb19b6b1d2805ad944

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
