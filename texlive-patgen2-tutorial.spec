# revision 16490
# category Package
# catalog-ctan /info/patgen2
# catalog-date 2009-12-24 15:14:53 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-patgen2-tutorial
Version:	20091224
Release:	9
Summary:	A tutorial on the use of Patgen 2
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/patgen2
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen2-tutorial.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen2-tutorial.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This document describes the use of Patgen 2 to create
hyphenation patterns for wide ranges of languages.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/support/patgen2-tutorial/patgen2.pdf
%doc %{_texmfdistdir}/doc/support/patgen2-tutorial/patgen2.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091224-2
+ Revision: 754705
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091224-1
+ Revision: 719205
- texlive-patgen2-tutorial
- texlive-patgen2-tutorial
- texlive-patgen2-tutorial
- texlive-patgen2-tutorial

