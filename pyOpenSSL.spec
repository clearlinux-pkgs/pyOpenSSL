#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyOpenSSL
Version  : 19.0.0
Release  : 69
URL      : https://pypi.debian.net/pyOpenSSL/pyOpenSSL-19.0.0.tar.gz
Source0  : https://pypi.debian.net/pyOpenSSL/pyOpenSSL-19.0.0.tar.gz
Summary  : Python wrapper module around the OpenSSL library
Group    : Development/Tools
License  : Apache-2.0
Requires: pyOpenSSL-license = %{version}-%{release}
Requires: pyOpenSSL-python = %{version}-%{release}
Requires: pyOpenSSL-python3 = %{version}-%{release}
Requires: cryptography
Requires: six
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : cffi-legacypython
BuildRequires : cffi-python
BuildRequires : cryptography
BuildRequires : cryptography-legacypython
BuildRequires : enum34
BuildRequires : enum34-legacypython
BuildRequires : idna-python
BuildRequires : ipaddress-legacypython
BuildRequires : ipaddress-python
BuildRequires : openssl-dev
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyasn1
BuildRequires : pyasn1-legacypython
BuildRequires : pycparser
BuildRequires : pycparser-legacypython
BuildRequires : pycparser-python
BuildRequires : pytest
BuildRequires : setuptools-legacypython
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
pyOpenSSL -- A Python wrapper around the OpenSSL library
        ========================================================

%package legacypython
Summary: legacypython components for the pyOpenSSL package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pyOpenSSL package.


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

%description python3
python3 components for the pyOpenSSL package.


%prep
%setup -q -n pyOpenSSL-19.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553560137
export LDFLAGS="${LDFLAGS} -fno-lto"
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1553560137
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyOpenSSL
cp LICENSE %{buildroot}/usr/share/package-licenses/pyOpenSSL/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyOpenSSL/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
