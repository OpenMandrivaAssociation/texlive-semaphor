# revision 18651
# category Package
# catalog-ctan /fonts/semaphor
# catalog-date 2008-04-15 09:54:26 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-semaphor
Version:	20080415
Release:	1
Summary:	Semaphore alphabet font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/semaphor
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semaphor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semaphor.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
These fonts represent semaphore in a highly schematic, but very
clear, fashion. The fonts are provided as MetaFont source, and
in both OpenType and Adobe Type 1 formats.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/semaphor/smfb10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfbsl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfeb10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfebsl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfer10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfesl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfett10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfpb10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfpbsl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfpr10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfpsl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfptt10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfr10-1.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfr10-2.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfr10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smfsl10.afm
%{_texmfdistdir}/fonts/afm/public/semaphor/smftt10.afm
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfb10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfbsl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfeb10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfebsl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfer10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfesl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfett10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfpb10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfpbsl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfpr10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfpsl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfptt10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfr10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smfsl10.enc
%{_texmfdistdir}/fonts/enc/dvips/semaphor/smftt10.enc
%{_texmfdistdir}/fonts/map/dvips/semaphor/semaf.map
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfb10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfbsl10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfeb10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfebsl10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfer10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfesl10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfett10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfpb10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfpbsl10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfpr10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfpsl10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfptt10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfr10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smfsl10.otf
%{_texmfdistdir}/fonts/opentype/public/semaphor/smftt10.otf
%{_texmfdistdir}/fonts/source/public/semaphor/Makefile
%{_texmfdistdir}/fonts/source/public/semaphor/README
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/semaf.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfbf10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfebf10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfer10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfesl10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfett10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfpbf10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfpr10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfpsl10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfptt10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfr10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smfsl10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/metafont/smftt10.mf
%{_texmfdistdir}/fonts/source/public/semaphor/pfb2otf.pe
%{_texmfdistdir}/fonts/source/public/semaphor/semaf.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfb10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfbsl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfeb10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfebsl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfer10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfesl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfett10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfpb10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfpbsl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfpr10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfpsl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfptt10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfr10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smfsl10.mp
%{_texmfdistdir}/fonts/source/public/semaphor/smftt10.mp
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfb10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfbsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfeb10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfebsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfer10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfesl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfett10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfpb10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfpbsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfpr10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfpsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfptt10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfr10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smfsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/semaphor/smftt10.tfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfb10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfb10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfbsl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfbsl10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfeb10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfeb10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfebsl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfebsl10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfer10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfer10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfesl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfesl10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfett10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfett10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpb10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpb10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpbsl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpbsl10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpr10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpr10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpsl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfpsl10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfptt10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfptt10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfr10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfr10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smfsl10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smfsl10.pfm
%{_texmfdistdir}/fonts/type1/public/semaphor/smftt10.pfb
%{_texmfdistdir}/fonts/type1/public/semaphor/smftt10.pfm
%{_texmfdistdir}/tex/context/third/semaphor/t-type-semaf.tex
%{_texmfdistdir}/tex/latex/semaphor/il2semaf.fd
%{_texmfdistdir}/tex/latex/semaphor/semaf.fd
%{_texmfdistdir}/tex/plain/semaphor/semaf.tex
%doc %{_texmfdistdir}/doc/fonts/semaphor/README
%doc %{_texmfdistdir}/doc/fonts/semaphor/example.pdf
%doc %{_texmfdistdir}/doc/fonts/semaphor/example.tex
%doc %{_texmfdistdir}/doc/fonts/semaphor/test-context.pdf
%doc %{_texmfdistdir}/doc/fonts/semaphor/test-context.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
