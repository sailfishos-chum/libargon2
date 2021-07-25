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
%setup -q -n %{name}-%{version}/argon2

%build
autoreconf -i
%configure
%{__make} %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%post -n libargon2 -p /sbin/ldconfig

%postun -n libargon2 -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/libargon*.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}/argon*.h

%files tools
%defattr(-,root,root,-)
%{_bindir}/argon2*
