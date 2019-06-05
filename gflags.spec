#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gflags
Version  : 2.2.2
Release  : 21
URL      : https://github.com/gflags/gflags/archive/v2.2.2.tar.gz
Source0  : https://github.com/gflags/gflags/archive/v2.2.2.tar.gz
Summary  : @PACKAGE_DESCRIPTION@
Group    : Development/Tools
License  : BSD-3-Clause
Requires: gflags-bin = %{version}-%{release}
Requires: gflags-lib = %{version}-%{release}
Requires: gflags-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
[![Build Status](https://travis-ci.org/gflags/gflags.svg?branch=master)](https://travis-ci.org/gflags/gflags)
[![Build status](https://ci.appveyor.com/api/projects/status/4ctod566ysraus74/branch/master?svg=true)](https://ci.appveyor.com/project/schuhschuh/gflags/branch/master)

%package bin
Summary: bin components for the gflags package.
Group: Binaries
Requires: gflags-license = %{version}-%{release}

%description bin
bin components for the gflags package.


%package dev
Summary: dev components for the gflags package.
Group: Development
Requires: gflags-lib = %{version}-%{release}
Requires: gflags-bin = %{version}-%{release}
Provides: gflags-devel = %{version}-%{release}

%description dev
dev components for the gflags package.


%package lib
Summary: lib components for the gflags package.
Group: Libraries
Requires: gflags-license = %{version}-%{release}

%description lib
lib components for the gflags package.


%package license
Summary: license components for the gflags package.
Group: Default

%description license
license components for the gflags package.


%prep
%setup -q -n gflags-2.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542735933
mkdir -p clr-build
pushd clr-build
%cmake .. -DBUILD_SHARED_LIBS:BOOL=ON
make  %{?_smp_mflags} VERBOSE=1
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
ctest

%install
export SOURCE_DATE_EPOCH=1542735933
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gflags
cp COPYING.txt %{buildroot}/usr/share/package-licenses/gflags/COPYING.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/builddir/.cmake/packages/gflags/1517893d82dfcf97475a559a3d57ec1c

%files bin
%defattr(-,root,root,-)
/usr/bin/gflags_completions.sh

%files dev
%defattr(-,root,root,-)
/usr/include/gflags/gflags.h
/usr/include/gflags/gflags_completions.h
/usr/include/gflags/gflags_declare.h
/usr/include/gflags/gflags_gflags.h
/usr/lib64/cmake/gflags/gflags-config-version.cmake
/usr/lib64/cmake/gflags/gflags-config.cmake
/usr/lib64/cmake/gflags/gflags-nonamespace-targets-relwithdebinfo.cmake
/usr/lib64/cmake/gflags/gflags-nonamespace-targets.cmake
/usr/lib64/cmake/gflags/gflags-targets-relwithdebinfo.cmake
/usr/lib64/cmake/gflags/gflags-targets.cmake
/usr/lib64/libgflags.so
/usr/lib64/libgflags_nothreads.so
/usr/lib64/pkgconfig/gflags.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgflags.so.2.2
/usr/lib64/libgflags.so.2.2.2
/usr/lib64/libgflags_nothreads.so.2.2
/usr/lib64/libgflags_nothreads.so.2.2.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gflags/COPYING.txt
