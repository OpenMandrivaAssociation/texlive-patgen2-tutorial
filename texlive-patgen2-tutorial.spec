Name:		texlive-patgen2-tutorial
Version:	58841
Release:	2
Summary:	A tutorial on the use of Patgen 2
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/patgen2
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen2-tutorial.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen2-tutorial.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This document describes the use of Patgen 2 to create
hyphenation patterns for wide ranges of languages.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/support/patgen2-tutorial

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
