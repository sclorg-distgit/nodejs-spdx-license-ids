%{?scl:%scl_package nodejs-spdx-license-ids}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-spdx-license-ids

%global commit 05c7466fcd62c8642006ef354c95064fcade3a03

%global npm_name spdx-license-ids
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-spdx-license-ids
Version:	1.0.1
Release:	2%{?dist}
Summary:	A list of SPDX license identifiers
Url:		https://github.com/shinnn/spdx-license-ids
Source0:	https://github.com/shinnn/spdx-license-ids/archive/%{commit}/%{npm_name}-%{commit}.tar.gz
License:	Unlicense

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(@shinnn/eslintrc)
BuildRequires:	%{?scl_prefix}npm(each-async)
BuildRequires:	%{?scl_prefix}npm(eslint)
BuildRequires:	%{?scl_prefix}npm(got)
BuildRequires:	%{?scl_prefix}npm(istanbul-coveralls)
BuildRequires:	%{?scl_prefix}npm(istanbul)
BuildRequires:	%{?scl_prefix}npm(require-bower-files)
BuildRequires:	%{?scl_prefix}npm(rm-rf)
BuildRequires:	%{?scl_prefix}npm(stringify-object)
BuildRequires:	%{?scl_prefix}npm(tape)
%endif

%description
A list of SPDX license identifiers

%prep
%setup -q -n %{npm_name}-%{commit}

chmod -x README.md
chmod -x build.js bower.json

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json bower.json build.js spdx-license-ids.json spdx-license-ids-browser.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
node --harmony_arrow_functions test.js
%endif

%files
%{nodejs_sitelib}/spdx-license-ids

%doc README.md
%doc LICENSE

%changelog
* Wed Nov 25 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-2
- Enable scl macros

* Wed Jun 10 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- Initial build
