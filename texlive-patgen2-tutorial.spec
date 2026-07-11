%global tl_name patgen2-tutorial
%global tl_revision 58841

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A tutorial on the use of Patgen 2
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/patgen2-tutorial
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen2-tutorial.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/patgen2-tutorial.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This document describes the use of Patgen 2 to create hyphenation
patterns for wide ranges of languages.

