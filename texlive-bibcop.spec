%global tl_name bibcop
%global tl_revision 79293

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
Requires(pre):	texlive-tlpkg
Requires:	texlive(bibcop.bin)
Requires:	texlive(iexec)
Requires:	texlive(pgfopts)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package checks the quality of your .bib file and emits
warning messages if any issues are found. For this, the TeX processor
must be run with the --shell-escape option, and Perl must be installed.
bibcop.pl can also be used as a standalone command line tool. The
package does not work on Windows.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/source
%dir %{_datadir}/texmf-dist/texmf-dist/tex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/bibcop
%dir %{_datadir}/texmf-dist/texmf-dist/source/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/bibcop
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%dir %{_datadir}/texmf-dist/texmf-dist/source/bibtex/bibcop
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex/bibcop
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/bibcop/DEPENDS.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/bibcop/LICENSE.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/bibcop/README.md
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/bibcop/bibcop-logo.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/bibcop/bibcop.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bibcop.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bibcop.man1.pdf
%{_datadir}/texmf-dist/texmf-dist/scripts/bibcop/bibcop.pl
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/bibcop/bibcop.dtx
%doc %{_datadir}/texmf-dist/texmf-dist/source/bibtex/bibcop/bibcop.ins
%{_datadir}/texmf-dist/texmf-dist/tex/latex/bibcop/bibcop.sty
