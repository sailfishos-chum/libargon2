Name:       libargon2
Version:    2019.03.26.87e5513
Release:    1
Summary:    A multi-arch library implementing the Argon2 password hashing algorithm.
Group:      Applications/Utilities
URL:        https://github.com/WOnder93/argon2
License:    MIT

%description
This project is based on the original source code by the Argon2 authors. The goal of this project is to provide efficient Argon2 implementations for various HW architectures (x86, SSE, ARM, PowerPC, ...).

%package devel
Summary:    Development headers and libraries for libargon2.
Requires:   %{name} = %{version}-%{release}

%description devel
This project is based on the original source code by the Argon2 authors. The goal of this project is to provide efficient Argon2 implementations for various HW architectures (x86, SSE, ARM, PowerPC, ...).

%build
cd argon2/qmake
%qmake5 ARCH=generic
make

%install
rm -rf %{buildroot}
cd argon2/qmake
%qmake5_install
cp -a ../include %{buildroot}/usr/

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/libargon*.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}/argon*.h
