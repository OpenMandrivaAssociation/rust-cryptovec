# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate cryptovec

Name:           rust-%{crate}
Version:        0.4.6
Release:        4%{?dist}
Summary:        Vector which zeroes its memory on clears and reallocations

# https://nest.pijul.com/pijul_org/cryptovec/discussions/9
License:        ASL 2.0
URL:            https://crates.io/crates/cryptovec
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No windows
Patch0:         cryptovec-0.4.5-fix-metadata.diff
# And now, code - https://nest.pijul.com/pijul_org/cryptovec/discussions/10
Patch1:         guard-windows-externs.diff
# https://nest.pijul.com/pijul_org/cryptovec/discussions/8
Patch2:         fix-doctests.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(libc/default) >= 0.2.0 with crate(libc/default) < 0.3.0)

%global _description \
A vector which zeroes its memory on clears and reallocations.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.4.6-1
- Update to 0.4.6
- Adapt to new packaging

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Josh Stone <jistone@redhat.com> - 0.4.5-1
- Update to 0.4.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.4-2
- Rebuild for rust-packaging v5

* Thu Dec 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4

* Fri Nov 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Tue Jun 20 2017 Martin Sehnoutka <msehnout@redhat.com> - 0.3.4-1
- Initial package
