#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyOpenSSL
Version  : 21.0.0
Release  : 100
URL      : https://files.pythonhosted.org/packages/54/9a/2a43c5dbf4507f86f7c43cba4195d5e25a81c988fd7b0ea779dfc9c6973f/pyOpenSSL-21.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/54/9a/2a43c5dbf4507f86f7c43cba4195d5e25a81c988fd7b0ea779dfc9c6973f/pyOpenSSL-21.0.0.tar.gz
Summary  : Python wrapper module around the OpenSSL library
Group    : Development/Tools
License  : Apache-2.0
Requires: pyOpenSSL-license = %{version}-%{release}
Requires: pyOpenSSL-python = %{version}-%{release}
Requires: pyOpenSSL-python3 = %{version}-%{release}
Requires: cryptography
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cryptography
BuildRequires : idna-python
BuildRequires : openssl-dev
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyasn1
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
pyOpenSSL -- A Python wrapper around the OpenSSL library
        ========================================================

%package license
Summary: license components for the pyOpenSSL package.
Group: Default

%description license
license components for the pyOpenSSL package.


%package python
Summary: python components for the pyOpenSSL package.
Group: Default
Requires: pyOpenSSL-python3 = %{version}-%{release}
Provides: pyopenssl-python

%description python
python components for the pyOpenSSL package.


%package python3
Summary: python3 components for the pyOpenSSL package.
Group: Default
Requires: python3-core
Provides: pypi(pyopenssl)
Requires: pypi(cryptography)
Requires: pypi(six)

%description python3
python3 components for the pyOpenSSL package.


%prep
%setup -q -n pyOpenSSL-21.0.0
cd %{_builddir}/pyOpenSSL-21.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632932425
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyOpenSSL
cp %{_builddir}/pyOpenSSL-21.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pyOpenSSL/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyOpenSSL/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
