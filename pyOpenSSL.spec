#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAE2536227F69F181 (hs@ox.cx)
#
Name     : pyOpenSSL
Version  : 17.2.0
Release  : 39
URL      : https://pypi.debian.net/pyOpenSSL/pyOpenSSL-17.2.0.tar.gz
Source0  : https://pypi.debian.net/pyOpenSSL/pyOpenSSL-17.2.0.tar.gz
Source99 : https://pypi.debian.net/pyOpenSSL/pyOpenSSL-17.2.0.tar.gz.asc
Summary  : Python wrapper module around the OpenSSL library
Group    : Development/Tools
License  : Apache-2.0
Requires: pyOpenSSL-legacypython
Requires: pyOpenSSL-python
Requires: Sphinx
Requires: cryptography
Requires: pretend
Requires: pytest
Requires: six
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cryptography
BuildRequires : enum34
BuildRequires : idna-python
BuildRequires : ipaddress-python
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyasn1
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
pyOpenSSL -- A Python wrapper around the OpenSSL library
        ========================================================

%package legacypython
Summary: legacypython components for the pyOpenSSL package.
Group: Default

%description legacypython
legacypython components for the pyOpenSSL package.


%package python
Summary: python components for the pyOpenSSL package.
Group: Default
Requires: pyOpenSSL-legacypython
Provides: pyopenssl-python

%description python
python components for the pyOpenSSL package.


%prep
%setup -q -n pyOpenSSL-17.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505057789
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505057789
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
