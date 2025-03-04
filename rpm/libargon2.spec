%define keepstatic 1

Name:       libargon2
Version:    2019.03.26
Release:    1
Summary:    A multi-arch library implementing the Argon2 password hashing algorithm.
Group:      Applications/Utilities
URL:        https://github.com/WOnder93/argon2
License:    MIT
Source:     %{name}-%{version}.tar.gz

BuildRequires: gcc libtool autoconf automake

%description
This project is based on the original source code by the Argon2 authors. The goal of this project is to provide efficient Argon2 implementations for various HW architectures (x86, SSE, ARM, PowerPC, ...).

%package static
Summary:    Static library for libargon2.

%description static
%{summary}

%package devel
Summary:    Development headers and libraries for libargon2.
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}

%package tools
Summary:    Tools supplied with libargon2.
Requires:   %{name} = %{version}-%{release}

%description tools
%{summary}

%prep
%autosetup -n %{name}-%{version}/argon2

%build
autoreconf -i
%configure
%{make_build}

%install
%make_install

%post -n libargon2 -p /sbin/ldconfig

%postun -n libargon2 -p /sbin/ldconfig

%files
%{_libdir}/libargon*.so*

%files static
%{_libdir}/libargon*.a

%files devel
%{_includedir}/argon*.h

%files tools
%{_bindir}/argon2*
