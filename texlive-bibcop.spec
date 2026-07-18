%global tl_name bibcop
%global tl_revision 79293
%global tl_bin_links bibcop:%{_texmfdistdir}/scripts/bibcop/bibcop.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.33
Release:	%{tl_revision}.1
Summary:	Style checker for .bib files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/utils/bibcop
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibcop.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibcop.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibcop.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(bibcop.bin)
Requires:	texlive(iexec)
Requires:	texlive(pgfopts)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
This LaTeX package checks the quality of your .bib file and emits
warning messages if any issues are found. For this, the TeX processor
must be run with the --shell-escape option, and Perl must be installed.
bibcop.pl can also be used as a standalone command line tool. The
package does not work on Windows.

