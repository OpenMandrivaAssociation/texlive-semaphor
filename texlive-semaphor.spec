%global tl_name semaphor
%global tl_revision 18651

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Semaphore alphabet font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/semaphor
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semaphor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/semaphor.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
These fonts represent semaphore in a highly schematic, but very clear,
fashion. The fonts are provided as Metafont source, and in both OpenType
and Adobe Type 1 formats.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from semaphor:
MixedMap semaf.map
TL_DROPIN_EOF
